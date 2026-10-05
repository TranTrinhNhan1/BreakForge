"""Deterministic synthetic data and a small streaming detector benchmark."""

from __future__ import annotations

from dataclasses import asdict, dataclass
import math
import random
from statistics import fmean, pstdev
from typing import Iterable

from breakforge import StructuralBreakDetector
from breakforge.preprocessing.rosenblatt import CausalGaussianAR1PIT


MECHANISMS = (
    "mean_shift",
    "variance_shift",
    "ar_coefficient_shift",
    "persistence_reversal",
    "frequency_shift",
    "heavy_tail_shift",
    "no_change",
)

DETECTOR_NAMES = (
    "raw_level_cusum",
    "standardized_residual_cusum",
    "breakforge_reference",
)

CALIBRATION_QUANTILE = 0.95
DEFAULT_HISTORY_LENGTH = 256
DEFAULT_STREAM_LENGTH = 512


@dataclass(frozen=True)
class SyntheticSeries:
    """One generated reference history and its online observations."""

    history: tuple[float, ...]
    stream: tuple[float, ...]
    change_index: int | None


@dataclass(frozen=True)
class BenchmarkResult:
    """Metrics for one mechanism and detector under a fixed benchmark setup."""

    mechanism: str
    detector: str
    seed: int
    repetitions: int
    calibration_repetitions: int
    history_length: int
    stream_length: int
    change_index: int | None
    threshold_quantile: float
    threshold: float
    auc_vs_no_change: float | None
    false_positive_rate: float
    detection_rate: float
    median_detection_delay: float | None
    median_pre_break_score: float | None
    median_post_break_increment: float | None

    def to_dict(self) -> dict[str, str | int | float | None]:
        """Return a stable, CSV-friendly record."""
        return asdict(self)


def generate_synthetic_series(
    mechanism: str,
    seed: int,
    history_length: int = DEFAULT_HISTORY_LENGTH,
    stream_length: int = DEFAULT_STREAM_LENGTH,
) -> SyntheticSeries:
    """Generate a seeded series with an optional change halfway through stream.

    The reference history follows the pre-change mechanism. The online stream
    contains a stable pre-change prefix followed by the selected alternative
    mechanism. ``no_change`` is a separate, unchanged control process.
    """
    if mechanism not in MECHANISMS:
        raise ValueError(f"unknown mechanism: {mechanism}")
    if history_length < 3:
        raise ValueError("history_length must be at least 3")
    if stream_length < 2:
        raise ValueError("stream_length must be at least 2")

    rng = random.Random(seed)
    change_index = None if mechanism == "no_change" else stream_length // 2
    absolute_change = history_length + (change_index or 0)
    values: list[float] = []
    previous = rng.gauss(0.0, 1.0)

    for index in range(history_length + stream_length):
        changed = change_index is not None and index >= absolute_change
        if mechanism == "frequency_shift":
            frequency = 0.025 if not changed else 0.12
            noise = rng.gauss(0.0, 0.35)
            value = math.sin(2.0 * math.pi * frequency * index) + noise
        else:
            if mechanism in {"ar_coefficient_shift", "persistence_reversal"}:
                phi_before, phi_after = 0.7, -0.2
                if mechanism == "persistence_reversal":
                    phi_before, phi_after = 0.85, -0.85
            else:
                phi_before = phi_after = 0.65

            phi = phi_after if changed else phi_before
            sigma = 2.0 if mechanism == "variance_shift" and changed else 1.0
            if mechanism == "heavy_tail_shift" and changed:
                # A variance-one Student-t(3) innovation, generated from
                # independent standard normals without a scientific package.
                chi_square = math.fsum(rng.gauss(0.0, 1.0) ** 2 for _ in range(3))
                noise = rng.gauss(0.0, 1.0) / math.sqrt(chi_square / 3.0) / math.sqrt(3.0)
            else:
                noise = rng.gauss(0.0, sigma)

            shift = 1.0 if mechanism == "mean_shift" and changed else 0.0
            value = phi * previous + shift + noise

        values.append(value)
        previous = value

    history = tuple(values[:history_length])
    stream = tuple(values[history_length:])
    return SyntheticSeries(history, stream, change_index)


class _CUSUM:
    """Reference-scaled two-sided CUSUM for a scalar stream."""

    def __init__(self, allowance: float = 0.25) -> None:
        self.allowance = allowance
        self.center = 0.0
        self.scale = 1.0
        self.previous = 0.0
        self.positive = 0.0
        self.negative = 0.0
        self.score = 0.0

    def fit(self, history: Iterable[float]) -> _CUSUM:
        values = [float(value) for value in history]
        if len(values) < 3 or any(not math.isfinite(value) for value in values):
            raise ValueError("history must contain at least three finite values")
        self.center = fmean(values)
        self.scale = max(pstdev(values), 1e-12)
        self.previous = values[-1]
        self.reset()
        return self

    def update(self, value: float) -> float:
        current = float(value)
        if not math.isfinite(current):
            raise ValueError("stream observations must be finite")
        z_score = (current - self.center) / self.scale
        self.positive = max(0.0, self.positive + z_score - self.allowance)
        self.negative = max(0.0, self.negative - z_score - self.allowance)
        self.score = max(self.score, self.positive, self.negative)
        self.previous = current
        return self.score

    def reset(self) -> None:
        self.positive = 0.0
        self.negative = 0.0
        self.score = 0.0


class _InnovationCUSUM(_CUSUM):
    """Two-sided CUSUM over fixed-reference conditional innovations."""

    def __init__(self, allowance: float = 0.25) -> None:
        super().__init__(allowance)
        self.normalizer = CausalGaussianAR1PIT()

    def fit(self, history: Iterable[float]) -> _InnovationCUSUM:
        self.normalizer.fit(history)
        self.reset()
        return self

    def update(self, value: float) -> float:
        z_score = self.normalizer.update(value).z_score
        self.positive = max(0.0, self.positive + z_score - self.allowance)
        self.negative = max(0.0, self.negative - z_score - self.allowance)
        self.score = max(self.score, self.positive, self.negative)
        return self.score

    def reset(self) -> None:
        super().reset()
        self.normalizer.reset()


def _new_detectors() -> dict[str, object]:
    return {
        "raw_level_cusum": _CUSUM(),
        "standardized_residual_cusum": _InnovationCUSUM(),
        "breakforge_reference": StructuralBreakDetector(),
    }


def _run_stream(detector: object, series: SyntheticSeries) -> tuple[list[float], float]:
    detector.fit(series.history)
    scores = [detector.update(value) for value in series.stream]
    return scores, scores[-1]


def _quantile(values: list[float], quantile: float) -> float:
    ordered = sorted(values)
    index = max(0, math.ceil(quantile * len(ordered)) - 1)
    return ordered[index]


def _auc(positive: list[float], negative: list[float]) -> float:
    wins = 0.0
    for positive_score in positive:
        for negative_score in negative:
            if positive_score > negative_score:
                wins += 1.0
            elif positive_score == negative_score:
                wins += 0.5
    return wins / (len(positive) * len(negative))


def _median(values: list[float]) -> float | None:
    if not values:
        return None
    ordered = sorted(values)
    middle = len(ordered) // 2
    if len(ordered) % 2:
        return ordered[middle]
    return (ordered[middle - 1] + ordered[middle]) / 2.0


def run_synthetic_benchmark(
    seed: int = 20261005,
    repetitions: int = 40,
    calibration_repetitions: int = 80,
    history_length: int = DEFAULT_HISTORY_LENGTH,
    stream_length: int = DEFAULT_STREAM_LENGTH,
) -> list[BenchmarkResult]:
    """Compare simple and conditional CUSUMs across seeded change mechanisms.

    A detector-specific threshold is the nearest-rank 95th percentile of
    independent no-change calibration streams. Reported false-positive rates
    use a separate no-change evaluation sample. AUC compares each changed
    mechanism with that same null evaluation sample; delay counts threshold
    crossings that first occur after the known change point.
    """
    if repetitions < 1 or calibration_repetitions < 1:
        raise ValueError("repetitions must be positive integers")
    if history_length < 3 or stream_length < 2:
        raise ValueError("history_length >= 3 and stream_length >= 2 are required")
    if stream_length // 2 < 1:
        raise ValueError("stream_length must leave an online pre-change prefix")

    calibrations: dict[str, list[float]] = {name: [] for name in DETECTOR_NAMES}
    for repetition in range(calibration_repetitions):
        series = generate_synthetic_series(
            "no_change",
            seed + 1_000_000 + repetition,
            history_length,
            stream_length,
        )
        for name, detector in _new_detectors().items():
            _, final_score = _run_stream(detector, series)
            calibrations[name].append(final_score)

    thresholds = {
        name: _quantile(scores, CALIBRATION_QUANTILE)
        for name, scores in calibrations.items()
    }

    controls: dict[str, list[float]] = {name: [] for name in DETECTOR_NAMES}
    false_positives: dict[str, int] = {name: 0 for name in DETECTOR_NAMES}
    positive_scores: dict[str, dict[str, list[float]]] = {
        mechanism: {name: [] for name in DETECTOR_NAMES}
        for mechanism in MECHANISMS
        if mechanism != "no_change"
    }
    pre_scores: dict[str, dict[str, list[float]]] = {
        mechanism: {name: [] for name in DETECTOR_NAMES}
        for mechanism in MECHANISMS
        if mechanism != "no_change"
    }
    increments: dict[str, dict[str, list[float]]] = {
        mechanism: {name: [] for name in DETECTOR_NAMES}
        for mechanism in MECHANISMS
        if mechanism != "no_change"
    }
    delays: dict[str, dict[str, list[float]]] = {
        mechanism: {name: [] for name in DETECTOR_NAMES}
        for mechanism in MECHANISMS
        if mechanism != "no_change"
    }
    detections: dict[str, dict[str, int]] = {
        mechanism: {name: 0 for name in DETECTOR_NAMES}
        for mechanism in MECHANISMS
        if mechanism != "no_change"
    }

    for repetition in range(repetitions):
        control = generate_synthetic_series(
            "no_change", seed + 2_000_000 + repetition, history_length, stream_length
        )
        for name, detector in _new_detectors().items():
            scores, final_score = _run_stream(detector, control)
            controls[name].append(final_score)
            if any(score >= thresholds[name] for score in scores):
                false_positives[name] += 1

        for mechanism_index, mechanism in enumerate(MECHANISMS[:-1]):
            series = generate_synthetic_series(
                mechanism,
                seed + 3_000_000 + mechanism_index * repetitions + repetition,
                history_length,
                stream_length,
            )
            assert series.change_index is not None
            change_index = series.change_index
            for name, detector in _new_detectors().items():
                scores, final_score = _run_stream(detector, series)
                positive_scores[mechanism][name].append(final_score)
                before = scores[change_index - 1]
                pre_scores[mechanism][name].append(before)
                increments[mechanism][name].append(max(0.0, final_score - before))
                crossed_before = any(score >= thresholds[name] for score in scores[:change_index])
                if not crossed_before:
                    for index in range(change_index, len(scores)):
                        if scores[index] >= thresholds[name]:
                            delays[mechanism][name].append(float(index - change_index))
                            detections[mechanism][name] += 1
                            break

    results: list[BenchmarkResult] = []
    false_positive_rates = {
        name: false_positives[name] / repetitions for name in DETECTOR_NAMES
    }
    for mechanism in MECHANISMS:
        for name in DETECTOR_NAMES:
            if mechanism == "no_change":
                auc = None
                detection_rate = false_positive_rates[name]
                median_delay = None
                median_pre = None
                median_increment = None
                change_index = None
            else:
                auc = _auc(positive_scores[mechanism][name], controls[name])
                detection_rate = detections[mechanism][name] / repetitions
                median_delay = _median(delays[mechanism][name])
                median_pre = _median(pre_scores[mechanism][name])
                median_increment = _median(increments[mechanism][name])
                change_index = stream_length // 2

            results.append(
                BenchmarkResult(
                    mechanism=mechanism,
                    detector=name,
                    seed=seed,
                    repetitions=repetitions,
                    calibration_repetitions=calibration_repetitions,
                    history_length=history_length,
                    stream_length=stream_length,
                    change_index=change_index,
                    threshold_quantile=CALIBRATION_QUANTILE,
                    threshold=thresholds[name],
                    auc_vs_no_change=auc,
                    false_positive_rate=false_positive_rates[name],
                    detection_rate=detection_rate,
                    median_detection_delay=median_delay,
                    median_pre_break_score=median_pre,
                    median_post_break_increment=median_increment,
                )
            )
    return results

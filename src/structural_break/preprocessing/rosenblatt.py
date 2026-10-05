"""Conditional Gaussian PIT transforms for a fixed AR(1) reference model."""

from __future__ import annotations

from dataclasses import dataclass
import math
from statistics import NormalDist
from typing import Iterable


_NORMAL = NormalDist()
_PIT_MARGIN = 1e-12


@dataclass(frozen=True)
class PITObservation:
    """Conditional transform for one newly observed value."""

    pit: float
    z_score: float
    innovation: float


class CausalGaussianAR1PIT:
    """Fit a Gaussian AR(1) reference and transform observations one at a time.

    ``fit`` uses only the supplied historical values. Each ``update`` predicts
    the current value from the last historical/online value, computes its
    innovation, then applies the Gaussian CDF. The fitted parameters stay fixed
    until another ``fit`` call.
    """

    def __init__(self) -> None:
        self._parameters: tuple[float, float, float] | None = None
        self._reference_last: float | None = None
        self._previous: float | None = None

    def fit(self, history: Iterable[float]) -> CausalGaussianAR1PIT:
        """Estimate AR(1) mean, coefficient, and innovation scale from history."""
        values = [float(value) for value in history]
        if len(values) < 3:
            raise ValueError("history must contain at least three observations")
        if any(not math.isfinite(value) for value in values):
            raise ValueError("history observations must be finite")

        mean = math.fsum(values) / len(values)
        lagged = values[:-1]
        denominator = math.fsum((value - mean) ** 2 for value in lagged)
        if denominator <= 1e-24:
            coefficient = 0.0
        else:
            covariance = math.fsum(
                (lagged[index] - mean) * (values[index + 1] - mean)
                for index in range(len(lagged))
            )
            coefficient = max(-0.98, min(0.98, covariance / denominator))

        residuals = [
            values[index] - mean - coefficient * (values[index - 1] - mean)
            for index in range(1, len(values))
        ]
        scale = math.sqrt(math.fsum(value * value for value in residuals) / len(residuals))
        scale = max(scale, 1e-12)

        self._parameters = (mean, coefficient, scale)
        self._reference_last = values[-1]
        self.reset()
        return self

    def update(self, value: float) -> PITObservation:
        """Transform and consume one value using only the fitted state and prefix."""
        if self._parameters is None or self._previous is None:
            raise RuntimeError("fit(history) must be called before update(value)")
        current = float(value)
        if not math.isfinite(current):
            raise ValueError("stream observations must be finite")

        mean, coefficient, scale = self._parameters
        predicted = mean + coefficient * (self._previous - mean)
        innovation = current - predicted
        z_score = innovation / scale
        pit = _NORMAL.cdf(z_score)
        pit = max(_PIT_MARGIN, min(1.0 - _PIT_MARGIN, pit))
        self._previous = current
        return PITObservation(pit=pit, z_score=z_score, innovation=innovation)

    def reset(self) -> None:
        """Restore the last fitted observation as the start of a new stream."""
        if self._reference_last is None:
            raise RuntimeError("fit(history) must be called before reset()")
        self._previous = self._reference_last

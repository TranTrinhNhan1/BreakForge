"""Sequential CUSUM evidence over conditional Gaussian innovations."""

from __future__ import annotations

import math
from typing import Iterable

from breakforge.preprocessing.rosenblatt import CausalGaussianAR1PIT


_MEAN_ABSOLUTE_STANDARD_NORMAL = math.sqrt(2.0 / math.pi)


class StructuralBreakDetector:
    """A deterministic reference detector with causal ``fit``/``update`` calls.

    Positive and negative innovation CUSUMs detect location changes. A centered
    absolute-innovation CUSUM responds to scale and other distribution changes.
    The returned score is the running maximum of these evidence channels; it is
    not a probability or a calibrated significance measure.
    """

    def __init__(self, allowance: float = 0.25) -> None:
        if not math.isfinite(allowance) or allowance < 0.0:
            raise ValueError("allowance must be a finite non-negative number")
        self.allowance = float(allowance)
        self._normalizer: CausalGaussianAR1PIT | None = None
        self._positive = 0.0
        self._negative = 0.0
        self._absolute = 0.0
        self._score = 0.0

    @property
    def score(self) -> float:
        """Maximum evidence observed since ``fit`` or the most recent reset."""
        return self._score

    def fit(self, history: Iterable[float]) -> StructuralBreakDetector:
        """Fit a fixed Gaussian AR(1) reference to historical observations."""
        self._normalizer = CausalGaussianAR1PIT().fit(history)
        self.reset()
        return self

    def update(self, value: float) -> float:
        """Consume one observation and return the current sequential evidence."""
        if self._normalizer is None:
            raise RuntimeError("fit(history) must be called before update(value)")
        innovation = self._normalizer.update(value).z_score
        self._positive = max(0.0, self._positive + innovation - self.allowance)
        self._negative = max(0.0, self._negative - innovation - self.allowance)
        self._absolute = max(
            0.0,
            self._absolute
            + abs(innovation)
            - _MEAN_ABSOLUTE_STANDARD_NORMAL
            - self.allowance,
        )
        self._score = max(self._score, self._positive, self._negative, self._absolute)
        return self._score

    def reset(self) -> None:
        """Clear sequential evidence and restart from the fitted history endpoint."""
        if self._normalizer is None:
            raise RuntimeError("fit(history) must be called before reset()")
        self._positive = 0.0
        self._negative = 0.0
        self._absolute = 0.0
        self._score = 0.0
        self._normalizer.reset()

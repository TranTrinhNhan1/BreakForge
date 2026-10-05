"""Helpers that preserve one-observation-at-a-time inference semantics."""

from __future__ import annotations

from collections.abc import Iterable, Iterator

from breakforge.detectors.baseline import StructuralBreakDetector


def score_stream(
    detector: StructuralBreakDetector,
    observations: Iterable[float],
) -> Iterator[float]:
    """Yield one score per observation by calling ``update`` in stream order."""
    for observation in observations:
        yield detector.update(observation)

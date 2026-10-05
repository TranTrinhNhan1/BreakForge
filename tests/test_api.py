import math

import breakforge as sb


def test_fit_and_update_return_current_streaming_evidence() -> None:
    detector_type = getattr(sb, "StructuralBreakDetector", None)
    assert detector_type is not None

    detector = detector_type()
    assert detector.fit([-1.0, -0.6, -0.2, 0.2, 0.6, 1.0]) is detector

    score = detector.update(1.4)

    assert isinstance(score, float)
    assert math.isfinite(score)
    assert score == detector.score

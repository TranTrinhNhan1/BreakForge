def test_breakforge_namespace_exposes_streaming_detector():
    from breakforge import StructuralBreakDetector

    detector = StructuralBreakDetector().fit([0.0, 1.0, -0.5, 0.3])
    score = detector.update(1.2)

    assert score >= 0.0
    detector.reset()
    assert detector.score == 0.0

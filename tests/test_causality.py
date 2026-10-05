import structural_break as sb


REFERENCE = [-1.2, -0.7, -0.1, 0.5, 0.8, 0.2, -0.4, -0.9]


def _detector():
    detector_type = getattr(sb, "StructuralBreakDetector", None)
    assert detector_type is not None
    return detector_type().fit(REFERENCE)


def _scores(values: list[float]) -> list[float]:
    detector = _detector()
    return [detector.update(value) for value in values]


def test_future_suffix_does_not_change_scores_for_an_observed_prefix() -> None:
    prefix = [0.1, 0.4, 1.1, 0.7]
    suffix_a = [20.0, -15.0, 30.0]
    suffix_b = [-40.0, 25.0]

    scores_a = _scores(prefix + suffix_a)[: len(prefix)]
    scores_b = _scores(prefix + suffix_b)[: len(prefix)]

    assert scores_a == scores_b


def test_reset_removes_all_state_from_the_previous_series() -> None:
    detector = _detector()
    for value in [8.0, 9.0, 10.0, 8.5]:
        detector.update(value)

    detector.reset()
    after_reset = [detector.update(value) for value in [0.2, -0.3, 0.1, 0.7]]
    fresh = _scores([0.2, -0.3, 0.1, 0.7])

    assert after_reset == fresh


def test_identical_inputs_produce_identical_scores() -> None:
    stream = [0.2, -0.3, 0.1, 0.7, 1.2, -0.8]

    assert _scores(stream) == _scores(stream)

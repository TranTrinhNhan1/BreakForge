from importlib import import_module, util

import structural_break as sb


def test_stream_helper_matches_explicit_one_value_updates() -> None:
    module_spec = util.find_spec("structural_break.validation.streaming")
    assert module_spec is not None
    score_stream = import_module("structural_break.validation.streaming").score_stream
    detector_type = getattr(sb, "StructuralBreakDetector", None)
    assert detector_type is not None
    history = [-1.2, -0.7, -0.1, 0.5, 0.8, 0.2, -0.4, -0.9]
    observations = [0.2, -0.3, 0.1, 0.7, 1.2]

    explicit = detector_type().fit(history)
    expected = [explicit.update(value) for value in observations]
    wrapped = detector_type().fit(history)

    assert list(score_stream(wrapped, iter(observations))) == expected

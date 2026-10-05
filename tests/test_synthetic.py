from contextlib import redirect_stdout
from importlib import import_module, util
from io import StringIO
import sys

import breakforge as sb


def _estimate_ar1(values: list[float]) -> float:
    previous = values[:-1]
    current = values[1:]
    mean_previous = sum(previous) / len(previous)
    mean_current = sum(current) / len(current)
    covariance = sum(
        (left - mean_previous) * (right - mean_current)
        for left, right in zip(previous, current)
    )
    variance = sum((value - mean_previous) ** 2 for value in previous)
    return covariance / variance


def test_synthetic_generator_is_deterministic_and_contains_the_requested_break() -> None:
    module_spec = util.find_spec("examples.synthetic_break_demo")
    assert module_spec is not None
    generate_ar_break = import_module("examples.synthetic_break_demo").generate_ar_break

    history, online, tau = generate_ar_break(
        seed=42,
        history_length=300,
        online_length=1_200,
        break_at=600,
    )
    repeated = generate_ar_break(
        seed=42,
        history_length=300,
        online_length=1_200,
        break_at=600,
    )

    assert (history, online, tau) == repeated
    assert tau == 600
    assert 0.5 < _estimate_ar1(online[20:tau]) < 0.85
    assert -0.4 < _estimate_ar1(online[tau + 20 :]) < 0.05

    detector = sb.StructuralBreakDetector().fit(history)
    scores = [detector.update(value) for value in online]
    assert max(scores[tau:]) > max(scores[:tau])


def test_synthetic_demo_shows_evidence_after_the_break(monkeypatch) -> None:
    demo = import_module("examples.synthetic_break_demo")
    output = StringIO()
    monkeypatch.setattr(sys, "argv", ["synthetic_break_demo.py"])

    with redirect_stdout(output):
        demo.main()

    assert "true break index: 500" in output.getvalue()
    assert "score after 100 post-break observations:" in output.getvalue()

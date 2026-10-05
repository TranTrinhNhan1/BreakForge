"""Run a synthetic AR structural-break stream without competition data."""

from __future__ import annotations

import argparse
from pathlib import Path
import random

from breakforge import StructuralBreakDetector


def generate_ar_break(
    seed: int = 7,
    history_length: int = 400,
    online_length: int = 1_000,
    break_at: int = 500,
) -> tuple[list[float], list[float], int]:
    """Generate AR(1) reference and stream data with a coefficient/scale break."""
    if history_length < 3:
        raise ValueError("history_length must be at least 3")
    if online_length < 1:
        raise ValueError("online_length must be positive")
    if not 0 < break_at < online_length:
        raise ValueError("break_at must be inside the online stream")

    rng = random.Random(seed)
    history: list[float] = []
    current = 0.0
    for _ in range(history_length):
        current = 0.7 * current + rng.gauss(0.0, 1.0)
        history.append(current)

    online: list[float] = []
    for index in range(online_length):
        if index < break_at:
            coefficient, scale = 0.7, 1.0
        else:
            coefficient, scale = -0.2, 2.0
        current = coefficient * current + rng.gauss(0.0, scale)
        online.append(current)
    return history, online, break_at


def _save_plot(
    history: list[float],
    online: list[float],
    scores: list[float],
    break_at: int,
    output: Path,
) -> None:
    try:
        import matplotlib.pyplot as plt
    except ImportError as error:
        raise SystemExit("Plotting requires matplotlib; install with `pip install -e '.[plot]'`.") from error

    output.parent.mkdir(parents=True, exist_ok=True)
    time = range(len(online))
    figure, axes = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
    axes[0].plot(time, online, linewidth=0.8, color="#315a9b")
    axes[0].axvline(break_at, linestyle="--", color="#c13a32", label="true break")
    axes[0].set_ylabel("value")
    axes[0].legend(loc="upper left")
    axes[1].plot(time, scores, linewidth=1.2, color="#287a57")
    axes[1].axvline(break_at, linestyle="--", color="#c13a32")
    axes[1].set_xlabel("online timestep")
    axes[1].set_ylabel("CUSUM evidence")
    figure.tight_layout()
    figure.savefig(output, dpi=150)
    plt.close(figure)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=7)
    parser.add_argument("--history-length", type=int, default=400)
    parser.add_argument("--online-length", type=int, default=1_000)
    parser.add_argument("--break-at", type=int, default=500)
    parser.add_argument("--plot", action="store_true", help="write a PNG plot")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("reports/figures/generated/synthetic_break_demo.png"),
        help="plot path used with --plot",
    )
    arguments = parser.parse_args()

    history, online, break_at = generate_ar_break(
        seed=arguments.seed,
        history_length=arguments.history_length,
        online_length=arguments.online_length,
        break_at=arguments.break_at,
    )
    detector = StructuralBreakDetector().fit(history)
    scores = [detector.update(value) for value in online]
    summary_index = min(break_at + 99, len(scores) - 1)
    post_break_observations = summary_index - break_at + 1

    print(f"seed: {arguments.seed}")
    print(f"reference observations: {len(history)}")
    print(f"online observations: {len(online)}")
    print(f"true break index: {break_at}")
    print(f"score before break: {scores[break_at - 1]:.3f}")
    print(
        f"score after {post_break_observations} post-break observations: "
        f"{scores[summary_index]:.3f}"
    )
    print(f"final score: {scores[-1]:.3f} (uncalibrated evidence, not a probability)")

    if arguments.plot:
        _save_plot(history, online, scores, break_at, arguments.output)
        print(f"plot: {arguments.output}")


if __name__ == "__main__":
    main()

"""Run and optionally save the data-independent BreakForge benchmark."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

from breakforge.validation.synthetic import BenchmarkResult, run_synthetic_benchmark


def _write_csv(results: list[BenchmarkResult], destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    rows = [result.to_dict() for result in results]
    with destination.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20261005)
    parser.add_argument("--repetitions", type=int, default=40)
    parser.add_argument("--calibration-repetitions", type=int, default=80)
    parser.add_argument("--history-length", type=int, default=256)
    parser.add_argument("--stream-length", type=int, default=512)
    parser.add_argument(
        "--output",
        type=Path,
        help="write detailed results to this CSV path instead of printing a summary",
    )
    args = parser.parse_args()

    results = run_synthetic_benchmark(
        seed=args.seed,
        repetitions=args.repetitions,
        calibration_repetitions=args.calibration_repetitions,
        history_length=args.history_length,
        stream_length=args.stream_length,
    )
    if args.output is not None:
        _write_csv(results, args.output)
        print(f"wrote {len(results)} synthetic benchmark rows to {args.output}")
        return

    print("Synthetic results use generated data and are not competition estimates.")
    print("mechanism,detector,AUC,FPR,detect_rate,median_delay")
    for row in results:
        auc = "" if row.auc_vs_no_change is None else f"{row.auc_vs_no_change:.4f}"
        delay = "" if row.median_detection_delay is None else f"{row.median_detection_delay:.1f}"
        print(
            f"{row.mechanism},{row.detector},{auc},"
            f"{row.false_positive_rate:.4f},{row.detection_rate:.4f},{delay}"
        )


if __name__ == "__main__":
    main()

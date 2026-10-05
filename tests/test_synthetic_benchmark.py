import csv
from pathlib import Path
import subprocess
import sys

from breakforge.validation.synthetic import (
    DETECTOR_NAMES,
    MECHANISMS,
    generate_synthetic_series,
    run_synthetic_benchmark,
)


def test_synthetic_mechanisms_cover_multiple_changes_and_a_null_control():
    assert set(MECHANISMS) == {
        "mean_shift",
        "variance_shift",
        "ar_coefficient_shift",
        "persistence_reversal",
        "frequency_shift",
        "heavy_tail_shift",
        "no_change",
    }

    for name in MECHANISMS:
        first = generate_synthetic_series(name, seed=19)
        second = generate_synthetic_series(name, seed=19)
        assert first == second
        assert len(first.history) == 256
        assert len(first.stream) == 512
        assert (first.change_index is None) == (name == "no_change")


def test_small_benchmark_is_deterministic_and_reports_each_detector():
    first = run_synthetic_benchmark(
        seed=31,
        repetitions=3,
        calibration_repetitions=8,
    )
    second = run_synthetic_benchmark(
        seed=31,
        repetitions=3,
        calibration_repetitions=8,
    )

    assert first == second
    assert {row.mechanism for row in first} == set(MECHANISMS)
    assert {row.detector for row in first} == set(DETECTOR_NAMES)
    assert len(first) == len(MECHANISMS) * len(DETECTOR_NAMES)
    for row in first:
        assert 0.0 <= row.false_positive_rate <= 1.0
        assert 0.0 <= row.detection_rate <= 1.0
        if row.auc_vs_no_change is not None:
            assert 0.0 <= row.auc_vs_no_change <= 1.0


def test_benchmark_command_writes_a_reproducible_csv(tmp_path):
    repo_root = Path(__file__).parents[1]
    output = tmp_path / "benchmark.csv"

    subprocess.run(
        [
            sys.executable,
            "scripts/synthetic_benchmark.py",
            "--seed",
            "2",
            "--repetitions",
            "2",
            "--calibration-repetitions",
            "4",
            "--output",
            str(output),
        ],
        cwd=repo_root,
        check=True,
        capture_output=True,
        text=True,
    )

    with output.open(newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))
    contents = output.read_bytes()
    assert contents.endswith(b"\n")
    assert b"\r\n" not in contents
    assert len(rows) == len(MECHANISMS) * len(DETECTOR_NAMES)
    assert {row["seed"] for row in rows} == {"2"}
    assert all(row["mechanism"] in MECHANISMS for row in rows)
    null_rows = [row for row in rows if row["mechanism"] == "no_change"]
    assert len(null_rows) == len(DETECTOR_NAMES)
    assert all(row["auc_vs_no_change"] == "" for row in null_rows)

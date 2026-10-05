import csv
import json
import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]


def test_evaluate_script_scores_user_supplied_csv_stream(tmp_path: Path) -> None:
    history = tmp_path / "history.csv"
    stream = tmp_path / "stream.csv"
    config = tmp_path / "config.json"
    output = tmp_path / "scores.csv"
    history.write_text("value\n0\n1\n0\n-1\n0\n1\n0\n-1\n", encoding="utf-8")
    stream.write_text("value\n0.2\n-0.3\n0.1\n0.7\n1.2\n", encoding="utf-8")
    config.write_text(json.dumps({"allowance": 0.25}), encoding="utf-8")
    environment = os.environ.copy()
    environment["PYTHONPATH"] = str(ROOT / "src")

    result = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "evaluate.py"),
            "--history",
            str(history),
            "--stream",
            str(stream),
            "--config",
            str(config),
            "--output",
            str(output),
        ],
        cwd=ROOT,
        env=environment,
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr
    with output.open(newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))
    assert [int(row["step_idx"]) for row in rows] == [0, 1, 2, 3, 4]
    assert all(float(row["score"]) >= 0.0 for row in rows)

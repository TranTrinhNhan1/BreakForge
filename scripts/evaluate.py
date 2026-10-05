"""Score a user-supplied one-column history and online-stream CSV."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

from structural_break import StructuralBreakDetector


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def read_values(path: Path) -> list[float]:
    """Read a CSV column named ``value`` or a single-column CSV."""
    with path.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        if not reader.fieldnames:
            raise ValueError(f"{path} must contain a CSV header")
        if "value" in reader.fieldnames:
            column = "value"
        elif len(reader.fieldnames) == 1:
            column = reader.fieldnames[0]
        else:
            raise ValueError(f"{path} must have a 'value' column or exactly one column")

        values = []
        for row_number, row in enumerate(reader, start=2):
            raw = row.get(column)
            if raw is None or not raw.strip():
                raise ValueError(f"missing value in {path} at row {row_number}")
            try:
                values.append(float(raw))
            except ValueError as error:
                raise ValueError(f"invalid numeric value in {path} at row {row_number}") from error
    if not values:
        raise ValueError(f"{path} contains no observations")
    return values


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--history", type=Path, required=True, help="CSV reference history")
    parser.add_argument("--stream", type=Path, required=True, help="CSV online values in order")
    parser.add_argument(
        "--config",
        type=Path,
        default=PROJECT_ROOT / "configs" / "reference.json",
        help="JSON configuration containing an allowance value",
    )
    parser.add_argument("--output", type=Path, default=Path("scores.csv"))
    arguments = parser.parse_args()

    try:
        history = read_values(arguments.history)
        stream = read_values(arguments.stream)
        with arguments.config.open(encoding="utf-8") as file:
            config = json.load(file)
        detector = StructuralBreakDetector(allowance=float(config["allowance"]))
        detector.fit(history)
        scores = [detector.update(value) for value in stream]
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as error:
        parser.error(str(error))

    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    with arguments.output.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["step_idx", "score"])
        writer.writerows(enumerate(scores))
    print(f"wrote {len(scores)} causal scores to {arguments.output}")


if __name__ == "__main__":
    main()

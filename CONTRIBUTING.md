# Contributing

Contributions that improve the causal reference implementation, validation utilities, documentation, or reproducible research record are welcome.

## Development setup

Python 3.10 or newer is required. From the repository root:

```bash
python -m venv .venv
# macOS / Linux
.venv/bin/python -m pip install -e '.[dev,plot]'
.venv/bin/python -m pytest -q
.venv/bin/python examples/synthetic_break_demo.py
```

On Windows PowerShell, replace `.venv/bin/python` with `.venv\Scripts\python.exe`.

The core package has no runtime dependencies outside the Python standard library. Matplotlib is optional and used only for plots.

## Changes to streaming behavior

Every prediction at time `t` must depend only on the fitted reference and observations through `x_t`. A change that adds a detector or stateful transform should include tests for future-suffix invariance, state reset, deterministic replay, and streaming/batch parity when a batch implementation exists. Fold-aware training utilities should test ID-level exclusion and document what they do not guarantee.

Scores should be named and documented according to their meaning. Do not describe an uncalibrated evidence score as a probability, p-value, false-alarm guarantee, or change probability.

## Research contributions

For a new method family or experiment, record:

- the hypothesis and causal information set;
- the configuration, random seed, code revision, and dataset provenance;
- the grouped split and metric definition;
- a matched simple control with the same window, normalization, and feature budget where possible;
- selection history, incomplete folds, and known leakage risks;
- negative or inconclusive outcomes as well as positive findings.

Keep raw competition data, labels, per-series predictions, credentials, and private platform artifacts out of pull requests. Users are responsible for supplying data they are authorized to use. Aggregate findings should follow the repository's [results policy](docs/results.md) and [competition data notes](docs/competition.md).

## Pull requests

Keep changes focused. Explain the intended behavior and any scientific assumptions, add or update documentation, run the fast suite, and include the relevant reproduction command for reported results. Do not add a score to a benchmark table unless its provenance and validation protocol can be stated clearly.

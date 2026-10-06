# BreakForge

**A Research Framework for Causal Structural Break Detection**

[![CI](https://github.com/TranTrinhNhan1/BreakForge/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/TranTrinhNhan1/BreakForge/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/github/license/TranTrinhNhan1/BreakForge)](LICENSE)

BreakForge is a research framework for causal, real-time structural-break detection in heterogeneous univariate time series. The ADIA Lab / CrunchDAO challenge motivated the problem; this project makes the streaming method, validation lessons, and research history reusable beyond the competition.

## Problem and causal contract

Given reference history and a stream `x_0, x_1, ...`, produce break evidence at each time `t`. A score may use the fitted reference and observations through `x_t`, never future values or final stream length. `fit(history)` freezes the reference, `update(x_t)` consumes one value, and `reset()` clears online state between independent series.

## Architecture

```mermaid
flowchart LR
    H["Historical reference"] --> M["Fit Gaussian AR(1)"]
    M --> C["Conditional mean and scale"]
    X["Arriving observation x_t"] --> Z["Standardized innovation"]
    C --> Z
    Z --> P["Optional Gaussian PIT"]
    Z --> S["Signed and magnitude CUSUMs"]
    S --> E["Uncalibrated break evidence"]
```

The public reference uses conditional Gaussian innovations and sequential CUSUM evidence. Its score is not a calibrated probability or alarm guarantee. PIT interpretation depends on the fitted conditional model being adequate.

## Quick start

The synthetic AR-break demo needs no competition data or credentials:

```bash
git clone https://github.com/TranTrinhNhan1/BreakForge.git
cd BreakForge
python -m venv .venv
# macOS / Linux
.venv/bin/python -m pip install -e .
.venv/bin/python examples/synthetic_break_demo.py
```

The demo simulates AR coefficient and noise-scale breaks. On Windows PowerShell, replace `.venv/bin/python` with `.venv\Scripts\python.exe`. To save a plot, install `.[plot]` and add `--plot`.

## Streaming API

```python
from breakforge import StructuralBreakDetector

detector = StructuralBreakDetector(allowance=0.25).fit(history)
for x_t in stream:
    score = detector.update(x_t)
detector.reset()
```

Inputs must be finite real values; `fit` requires at least three history observations. `update` returns a non-decreasing, uncalibrated score. Reset the detector between independent series.

## Methods investigated

Research covered conditional PIT/Rosenblatt normalization; statistical and sequential detectors; kernels and density ratios; spectral and path features; Bayesian and dynamical models; conformal methods; learned representations; and stacked heads. The report-backed catalog contains 145 evidence records (139 method or variant records and six procedures or audits); repeated runs are grouped. A separate crosswalk maps 111 historical score records to 96 recorded model/feature groups. These records preserve hypotheses, controls, and limits; they are not distinct-method counts or clean benchmarks. See the [method catalog](docs/method_catalog.md), [failed experiments](docs/failed_experiments.md), [run crosswalk](reports/curated_results/run_variant_crosswalk.csv), and [additional report index](reports/additional_report_index.csv).

## Results

### Public synthetic benchmark

Across six generated break mechanisms, the reference detector's AUC ranges from 0.4781 to 1.0000. The heavy-tail case is near chance (0.4781 AUC; 0.075 detection rate). These fixed-seed results describe selected synthetic generators, not general performance. Full metrics and settings are in [results](docs/results.md).

| Generated mechanism | Raw CUSUM AUC | Conditional CUSUM AUC | BreakForge AUC |
|---|---:|---:|---:|
| Mean shift | 1.0000 | 1.0000 | 1.0000 |
| Variance shift | 0.8406 | 0.9663 | 1.0000 |
| AR coefficient shift | 0.2844 | 0.2938 | 0.9006 |
| Persistence reversal | 0.6431 | 0.4806 | 1.0000 |
| Frequency shift | 0.0175 | 0.0238 | 0.8288 |
| Heavy-tail shift | 0.4244 | 0.4838 | 0.4781 |

On unchanged streams, false-positive rates were 0.125 for raw CUSUM and 0.025 for both conditional detectors. Results are `SYNTHETIC_ONLY` (40 evaluation and 80 calibration streams per setting; seed `20261005`); see [protocol and full metrics](docs/results.md#clean-reproducible-synthetic-benchmark).

### Official competition result

The strongest verified private result is TS-AUC **0.6213427008** (`CLOUD_PRIVATE; VERIFIED_OFFICIAL`), submission #21 / run 120227. Final rank is unverified, package identity is incomplete, and this was a different system. It is not a BreakForge benchmark.

Historical CV results remain labeled for future-length leakage, nested-OOF contamination, post-selection, or partial folds. They do not establish clean competition performance. See [results](docs/results.md) and the [validation guide](docs/validation.md).

## Validation lessons

- A real-time score cannot use `final_online_length` or other future-derived values.
- Every upstream fit in stacked evaluation must exclude the outer held-out group.
- Repeatedly selected folds do not provide an untouched estimate.

See the [validation guide](docs/validation.md) for exact-stream protocols, grouped folds, and causality tests.

## What did not work

Some high historical scores depended on future information or contaminated stacked features. Several selected methods lost their apparent advantage against matched controls or on reduced diagnostics. These findings apply to tested configurations, not whole method families.

## Competition origin and data

The Structural Break: Real-Time challenge motivated this work and its streaming constraints. Competition data, labels, predictions, and submission bundles are excluded. Users must supply data they are authorized to use; see [competition background](docs/competition.md).

## Repository structure

```text
src/breakforge/       causal detector, conditional PIT, validation utilities
examples/             synthetic streaming demonstrations
tests/                causality, reset, parity, determinism, fold isolation
configs/              reference configuration
scripts/              reproduction and user-data evaluation
reports/              synthetic results and curated research records
docs/                 methodology, validation, results, and research history
research_archive/     indexed conclusions from selected research
```

## Reproducibility and documentation

Run the tests and regenerate the synthetic benchmark with:

```bash
.venv/bin/python -m pip install -e '.[dev]'
.venv/bin/python -m pytest -q
.venv/bin/python scripts/synthetic_benchmark.py
```

On Windows PowerShell, replace `.venv/bin/python` with `.venv\Scripts\python.exe`. For methodology, validation, history, and workflow, start at the [documentation index](docs/README.md).

## References

See the curated [references and further reading](docs/references.md).

## Citation

Use the project metadata in [CITATION.cff](CITATION.cff).

## License

BreakForge is distributed under the [MIT License](LICENSE).

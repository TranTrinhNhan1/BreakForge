# BreakForge

**A Research Framework for Causal Structural Break Detection**

[![CI](https://github.com/TranTrinhNhan1/BreakForge/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/TranTrinhNhan1/BreakForge/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/github/license/TranTrinhNhan1/BreakForge)](LICENSE)

BreakForge studies causal, real-time break detection in heterogeneous univariate time series. The research grew out of the ADIA Lab / CrunchDAO Structural Break: Real-Time challenge and is presented here as a reusable research framework, with a small public reference detector and an honest record of methods, controls, and validation failures.

## Problem and approach

At time `t`, a detector may use its fitted reference and observations through `x_t`. It must not depend on future observations or the final stream length. BreakForge illustrates conditional normalization with a fixed Gaussian AR(1), then accumulates sequential evidence from each standardized innovation.

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

The public score is evidence, not a calibrated probability or alarm guarantee. The PIT is available separately; its interpretation depends on the conditional model being adequate.

## Quick start

```bash
pip install -e .
python examples/synthetic_break_demo.py
```

The demo generates its own AR process with a change in coefficient and noise scale. It needs no Crunch runtime or competition data. Add `--plot` after installing `pip install -e '.[plot]'` to save a figure.

## Streaming API

```python
from breakforge import StructuralBreakDetector

detector = StructuralBreakDetector(allowance=0.25)
detector.fit(history)  # estimate and freeze the reference

for x_t in stream:
    score = detector.update(x_t)  # consume one observation

detector.reset()  # clear online state while keeping the fitted reference
```

Inputs must be finite real values; `fit` requires at least three reference observations. `update` returns a non-decreasing, uncalibrated score. Resetting between series prevents state from leaking across IDs. See [methodology](docs/methodology.md) for assumptions and [validation](docs/validation.md) for the causal contract.

## Validation and results

| Evidence | Result | Interpretation |
|---|---:|---|
| Public synthetic benchmark | AUC 0.8288–1.0000 on five tested break mechanisms | Fixed-seed, 40 streams per mechanism; synthetic only |
| Heavy-tail synthetic shift | AUC 0.4781; detection rate 0.075 | A tested failure case for this reference detector |
| Official private run #21 / 120227 | TS-AUC 0.6213427008 | Different system from the public API; final rank unverified |

The synthetic benchmark is reproducible with `python scripts/synthetic_benchmark.py`; configuration, code revision, metric definition, and limits are in [results](docs/results.md). Historical competition CV values are not clean benchmarks: some used final-length information, some had nested-OOF contamination, and many were selected on the same folds. The high historical values remain visible with labels in [results](docs/results.md) and [validation](docs/validation.md).

## Methods investigated

The research covered rolling statistics, conditional PIT/Rosenblatt transforms, sequential tests, kernels, density ratios, spectral and wavelet features, Koopman/DMD, path signatures, Bayesian methods, conformal inference, and learned representations. Selected configurations did not establish that any broad family is ineffective. See the [method catalog](docs/method_catalog.md), [failed experiments](docs/failed_experiments.md), and the [131-report index](reports/experiment_index.csv).

## What did not work

Some high historical CV scores depended on the final stream length or on upstream OOF predictions that had seen nominally held-out folds. A selected DMD/Koopman blend scored higher on those CV folds than the Trial 11 reference but lower on its reduced diagnostic. These are configuration-level observations, not clean benchmarks or family-wide conclusions; see the [labeled results](docs/results.md) and [validation postmortem](docs/validation.md).

## Competition context and data

The challenge supplied the research problem and real-time constraints. CrunchDAO announced the Real-Time edition closed on 2026-10-02; see its [closure notice](https://forum.crunchdao.com/t/2026-w40-closing-of-structural-break-real-time/1222) and [streaming leakage clarification](https://forum.crunchdao.com/t/leaderboard-comparability-after-the-june-8-real-time-data-access-fix-were-pre-fix-scores-rescored/1188). Competition data, labels, per-series predictions, and submission bundles are not included. Users must supply data they are authorized to use. The public examples and tests work without them.

## Repository map

```text
src/breakforge/       Causal detector, conditional PIT, validation utilities
examples/             Synthetic streaming demonstrations
tests/                Causality, reset, parity, determinism, fold isolation
configs/              Small reference configuration
scripts/              Reproduction and user-data evaluation
reports/              Synthetic results and curated historical aggregates
docs/                 Methods, validation, results, research history, references
research_archive/     Indexed conclusions from selected research
```

## Reproducibility

```bash
pip install -e '.[dev]'
pytest -q
python examples/synthetic_break_demo.py
```

The core has no runtime dependencies beyond Python's standard library. Plotting is optional; no Crunch credentials, cloud services, or private data are needed for the quick start.

## Citation and license

Use the metadata in [CITATION.cff](CITATION.cff). BreakForge is distributed under the [MIT License](LICENSE). See [references](docs/references.md) and [contribution guidance](CONTRIBUTING.md).

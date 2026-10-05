# BreakForge: Structural Break Detection in Time Series

A research framework for causal, real-time structural-break detection in heterogeneous univariate time series. The online work grew out of ADIA Lab and CrunchDAO's **Structural Break: Real-Time** edition; the methods and synthetic examples are intended to be useful beyond that competition.

The reference implementation is deliberately compact: it fits a Gaussian AR(1) model on historical data, converts each arriving observation to a conditional innovation/PIT, and accumulates sequential evidence. It is a transparent baseline for research, not a leaderboard claim.

## Overview

At time `t`, an online score may depend on the reference history and observations through `x_t`. It must not depend on later observations, the final stream length, or the end of a sequence. The package exposes a resettable detector, a conditional PIT transform, fold-isolation helpers, and tests for these guarantees.

## Architecture

```mermaid
flowchart LR
    H[Historical reference] --> M[Fit fixed Gaussian AR(1)]
    M --> P[Conditional mean and scale]
    X[One arriving value x_t] --> E[Innovation e_t]
    P --> E
    E --> Z[Standardized innovation z_t]
    Z --> U[Gaussian PIT u_t = Phi(z_t)]
    Z --> C[Signed mean and absolute-value CUSUMs]
    C --> S[Running maximum evidence score]
    S --> NEXT[Emit score before consuming x_(t+1)]
```

The public detector uses the standardized innovation for its sequential evidence. The PIT is also available directly for analyses and alternative detectors. Neither the score nor the PIT is a calibrated probability unless a separate calibration procedure is justified and validated.

## Quick start

```bash
pip install -e .
python examples/synthetic_break_demo.py
```

The demo generates its own AR process. Before the break it uses `x_t = 0.7 x_(t-1) + ε_t`; after the break it uses `x_t = -0.2 x_(t-1) + 2 ε_t`. It prints the true change index and sequential evidence without loading competition data.

To write a plot, install the optional plotting extra and pass `--plot`:

```bash
pip install -e '.[plot]'
python examples/synthetic_break_demo.py --plot
```

## Streaming API

```python
from breakforge import StructuralBreakDetector

detector = StructuralBreakDetector(allowance=0.25)
detector.fit(history)                 # fixed reference fit

for value in stream:                   # one observation at a time
    score = detector.update(value)     # consumes only this value and prior state
    print(score)

detector.reset()                       # retain the fit; clear online state
```

`history` and each stream item must be finite real numbers. `fit` requires at least three history observations. `update` returns a non-decreasing, uncalibrated CUSUM evidence score; `detector.score` exposes the current value. `reset()` restarts from the fitted history endpoint so one series cannot contaminate the next.

See [methodology](docs/methodology.md) for model assumptions and [validation](docs/validation.md) for the causal contract, fold isolation, and historical leakage findings.

## Methods investigated

The research explored rolling statistics, spectral and dynamical-system features (including Koopman/DMD), conditional PIT/Rosenblatt normalization, sequential tests, signatures, conformal methods, density ratios, Bayesian models, and representation learning. The public reference API contains only the small causal Gaussian AR(1) plus CUSUM baseline. [Failed experiments](docs/failed_experiments.md) separates tested configurations from broader claims about method families.

## Validation and results

The public tests cover future-suffix invariance, state reset, determinism, streaming replay parity, and ID-level fold isolation. The verified private competition score was **0.6213427008 TS-AUC**; the final rank was not independently verified. This single result is not a reproducible benchmark. The small synthetic benchmark is reproducible and deliberately shows where the reference detector struggles, especially under heavy-tailed changes.

| Evidence | Result | Interpretation |
|---|---:|---|
| Official private Real-Time evaluation | 0.6213427008 TS-AUC | Verified aggregate; no rank or generalization claim |
| Synthetic mean, variance, AR, persistence, and frequency shifts | AUC 0.8288–1.0000 for BreakForge | Fixed-seed, small generated benchmark; see full per-mechanism table |
| Synthetic heavy-tail shift | AUC 0.4781; detection rate 0.075 | Weak under this tested data-generating process |

Historical CV values are selection-exposed or otherwise limited and are labeled separately in [results.md](docs/results.md); they are not clean benchmark estimates. See [validation.md](docs/validation.md) for the evaluation dependency diagram and holdout history.

## Competition background

This project’s online research came from the **Structural Break: Real-Time** edition, which CrunchDAO reported closed on 2026-10-02. It is distinct from the earlier 2025 ADIA Lab Structural Break Challenge documentation, which describes both segments supplied together for a batch decision. The Real-Time edition used streaming inference and required each score to use only history and the online prefix. [CrunchDAO's closure notice](https://forum.crunchdao.com/t/2026-w40-closing-of-structural-break-real-time/1222), [Real-Time leakage clarification](https://forum.crunchdao.com/t/leaderboard-comparability-after-the-june-8-real-time-data-access-fix-were-pre-fix-scores-rescored/1188), and [original batch challenge documentation](https://docs.crunchdao.com/competitions/competitions/adia-lab-structural-break-challenge) are linked for context.

Competition datasets cannot be redistributed. This repository does not require or include them; users must supply data they are authorized to use. See [competition notes](docs/competition.md).

## Repository map

```text
src/breakforge/   Public detector, conditional PIT, and validation helpers
examples/               Synthetic, data-independent demonstrations
tests/                  Fast causality and fold-isolation tests
configs/                Small reference configuration
scripts/                Reproduction and user-data evaluation commands
docs/                   Methodology, validation, history, and citations
reports/                Curated results only, with validity labels
research_archive/       Indexed summaries of selected historical evidence
```

The raw experiment tree, data, and private runtime artifacts are excluded from the public Git interface. Selected research history and its status are indexed in [research_archive/README.md](research_archive/README.md).

## Reproducibility

```bash
pip install -e '.[dev]'
pytest -q
python examples/synthetic_break_demo.py
```

The core runtime uses only the Python standard library. Plotting is optional. Competition-specific evaluation is not part of the public quick start.

## References, citation, and license

See [results](docs/results.md), [references](docs/references.md), [CITATION.cff](CITATION.cff), and [LICENSE](LICENSE). Contribution guidelines are in [CONTRIBUTING.md](CONTRIBUTING.md); security reports should follow [SECURITY.md](SECURITY.md).

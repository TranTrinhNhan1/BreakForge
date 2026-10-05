# v1.0.0 — Post-Competition Research Release (draft)

This draft describes the intended contents of the public release. It is not an announcement that the release gates have passed.

## Included

- A compact, deterministic, CPU-only causal streaming API for a fixed Gaussian AR(1) reference and sequential CUSUM evidence.
- Conditional Gaussian PIT / standardized innovation normalization with explicit assumptions and failure cases.
- Exact-stream and fold-isolation validation helpers, with regression tests for causality, reset behavior, determinism, and replay parity.
- A synthetic AR structural-break demonstration that requires no competition data or CrunchDAO runtime.
- A research retrospective covering validation leakage, nested OOF contamination, matched controls, and experiments that were deprioritized.
- A reproducible synthetic benchmark and an explicitly separated, verified aggregate official competition score.
- Curated historical research comparisons with validity labels and selection caveats.
- A curated reference list, research archive index, reference configuration, and user-data CSV evaluation script.

## Validation and performance

This release makes no leaderboard-rank, state-of-the-art, or generalized performance claim. The one private official score is a verified aggregate, not a public reproducible benchmark. Historical evaluation results have differing validity and provenance; the documentation labels known issues and does not treat them as clean benchmarks.

## Release limitations

- Competition data and private results are not redistributed.
- A clean competition benchmark replay is not available from the public files.
- Source ownership, third-party provenance, repository authors, and final license still require resolution.
- The current score is uncalibrated evidence; no false-alarm guarantee is claimed.

## GitHub metadata proposal

- **Description:** Research framework for causal, real-time structural-break detection in heterogeneous univariate time series.
- **Topics:** `time-series`, `change-point-detection`, `structural-break`, `sequential-analysis`, `streaming`, `statistical-learning`.
- **Homepage:** leave unset unless a project page or canonical paper is established.

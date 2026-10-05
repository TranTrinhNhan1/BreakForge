# Curated results

Public result categories stay separate:

1. **Clean / reproducible results:** the synthetic benchmark is generated from public code and a fixed seed. Its configuration, code revision, metrics, and limitations are documented in [results.md](../../docs/results.md); the complete output is [`synthetic_benchmark.csv`](../synthetic_benchmark.csv).
2. **Official competition runs:** scored, timed-out, stopped, and protocol-failure outcomes are indexed in [`official_runs.csv`](official_runs.csv) and summarized in [results.md](../../docs/results.md). Only one score is named as the verified private reference; these outcomes are not a reproducible benchmark or rank claim.
3. **Historical research results:** selected aggregate CV results are recorded in [`historical_research.csv`](historical_research.csv), with explicit labels including `VALID_EXACT_STREAM`, `INVALID_FUTURE_LENGTH`, `POST_SELECTION_CV`, and `NON_NESTED_META_CV`.

Competition-derived results are aggregates only. The repository excludes source data, labels, series IDs, predictions, and artifacts that would reproduce or expose the competition dataset. See the [competition data policy](../../docs/competition.md).

# Research method catalog

The project explored a broad set of causal evidence channels for heterogeneous univariate streams. The [machine-readable catalog](../reports/method_catalog.csv) records the tested hypothesis, implementation summary, information-set notes, matched control when available, validation scope, disposition, and source-report identifiers for each catalog entry.

The catalog covers all 131 report-index identifiers (`MTH-*`) after grouping staged reports that describe the same underlying recipe. It also records five code-only experiment branches whose useful aggregate outcomes were found outside those reports. These are catalog records, not a count of distinct algorithms: entries include detectors, feature representations, scoring heads, training or selection procedures, and one validation audit. Seeds, folds, and repeat runs are not counted as separate methods. The audit entry is explicitly typed as such, and stage records with the same method are grouped under one catalog ID.

The identifiers `MTH-*` and `CAT-*` were assigned for this release. The original reports and experiment workspaces remain in a private research archive because they include private-data paths, predictions, intermediate artifacts, and unreviewed runtime details. A source digest verifies which local report informed an index record, but it does not make that report or its results independently reproducible. Selected aggregate outcomes and their caveats are published separately in [results](results.md) and [`historical_research.csv`](../reports/curated_results/historical_research.csv).

## How to read the catalog

- **Research family** groups related ideas for navigation; it does not imply that the experiments are equivalent.
- **Method or variant** preserves the report title. A changed statistic, representation, calibration rule, or model objective remains visible as its own entry; staged evaluations of the same recipe share a catalog ID.
- **Causal evidence** distinguishes a stated causal design from a reported prefix or future-mutation check. Neither label substitutes for inspecting the implementation and audit scope.
- **Evaluation scope** separates synthetic feasibility, full grouped-fold records, partial-fold screens, and package replays. A package replay does not certify model selection or fold independence.
- **Validation labels** preserve known caveats such as `POST_SELECTION_CV`, `NON_NESTED_META_CV`, `PARTIAL_FOLD`, and `INVALID_FUTURE_LENGTH`. `UNKNOWN_FROM_PUBLIC_INDEX` means the available release summary does not justify a stronger claim.
- **Matched control** is `not captured` when the source summary did not preserve enough detail. Family-level examples and the reason matched controls matter are in [failed and inconclusive experiments](failed_experiments.md); a reader should not infer a matched comparison where none is documented.

## Main research threads

### Conditional normalization and sequential evidence

Historical AR residuals, empirical-CDF probability integral transforms, Gaussian scores, GARCH-style transforms, and copula variants were investigated as representations for the online stream. These transformations can make a heterogeneous series easier to compare with its own history, but they do not guarantee independent or uniform innovations when the conditional model is misspecified. On top of these representations, the project examined CUSUM and generalized likelihood evidence, predictive ranks, restart mixtures, conformal martingales, betting processes, candidate-change-time mixtures, and Bayesian run-length methods.

### Statistical, kernel, and distributional comparisons

The experiments compared rolling location and scale summaries, quantile displacement, self-normalized statistics, kernel mean embeddings, RFF/MMD and U-statistics, density-ratio proxies, and Wasserstein-style comparisons. The public synthetic benchmark includes a compact reference detector and two simple CUSUM controls. Historical screens generally used grouped CV-A slices or private competition streams, so their outcomes remain in the historical ledger with the relevant selection and fold labels.

### Dynamics and ordered structure

The catalog includes AR likelihood and coefficient-drift models, Bayesian context trees, DMD/Koopman and Markov-transition features, SINDy and ODE-inspired summaries, spectral and bispectral features, wavelet methods, ordinal patterns, signatures, recurrence geometry, visibility graphs, persistent Laplacians, matrix profiles, and subspace projections. These methods target dynamics or ordering that low-order moments may miss. A tested configuration that underperformed a matched control is recorded as a configuration-level result, not as a rejection of its entire research family.

### Learned representations and combinations

Temporal-neighborhood encoders, reference/current embeddings, contrastive and predictive-coding objectives, neural score models, GRU heads, TabPFN feasibility, CNN pilots, pairwise ranking, tree-based heads, stacked blends, and automated search are included. Their evaluation is especially sensitive to fold isolation: every upstream learned representation and score used by a meta-model must be fit without access to its outer evaluation group.

## Matched controls

The catalog marks a report-specific control as unknown if the public index did not retain it. The general comparison rule used in this retrospective is to match the information set, stream, window, normalization, compute budget, and threshold calibration, then reduce the proposed method to a simple control such as low-order moments, autocorrelation, the same conditional innovations with a CUSUM, or the frozen reference head. This guards against crediting an elaborate representation for extra context, tuning, or a stronger downstream model.

The clean, public comparison is the [reproducible synthetic benchmark](results.md#clean-reproducible-synthetic-benchmark). Competition-derived comparisons remain separate because private inputs and artifacts are unavailable for independent replay.

## Scope and limitations

The catalog is a curated map, not a downloadable implementation of every experiment. It summarizes source reports and code-only metric records while keeping private data, OOF predictions, checkpoints, logs, and local paths out of the release. The source reports were written during active research and include exploratory or post-selection estimates. Consult [validation](validation.md) before interpreting a score, and [research journey](research_journey.md) for how the protocol changed after the future-length and nested-OOF audits.

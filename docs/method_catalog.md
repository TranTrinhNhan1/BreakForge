# Research method catalog

The project explored a broad set of evidence channels for heterogeneous univariate streams. The [machine-readable catalog](../reports/method_catalog.csv) has 140 records: 129 report-level `CAT-*` records cover all 131 indexed `MTH-*` reports (two catalog records combine pairs of staged reports), plus eleven supplemental `SUP-*` evidence records. It records a hypothesis, implementation, control, validation scope, or disposition when a release-safe summary supports it; missing fields are marked explicitly.

The catalog covers all 131 report-index identifiers (`MTH-*`) after grouping staged reports that describe the same underlying recipe. Eleven supplemental records summarize evidence found outside those reports. Under the catalog type rule, 135 records describe methods or variants: 114 detector/evidence methods, 13 representations/models, seven combinations/scoring heads, and one baseline. The other five records are four training/selection procedures and one validation audit. These are records, not distinct algorithms: staged reports are grouped and seeds, folds, and repeat runs are not separate methods. The audit entry is explicitly typed as such, and stage records with the same method are grouped under one catalog ID.

A separate 111-record score inventory preserves run-level records from the source experiment ledger. Its 30 source model-family labels are summarized in [`source_model_family_inventory.csv`](../reports/curated_results/source_model_family_inventory.csv). That appendix groups records by the recorded implementation family; it does not count methods. The source score ledger has no complete, verified one-to-one link from each run ID to a `CAT-*` or `MTH-*` record, so the two inventories remain separate rather than implying unsupported mappings. The score inventory is private-data-derived, has unknown validation protocols, and is ineligible as a benchmark.

The identifiers `MTH-*` and `CAT-*` were assigned for this release. The report index keeps the source titles and SHA-256 digests; the original report text, raw predictions, model artifacts, and competition data are not included. The 131 report digests were checked against the source records used for this curation. A matching digest verifies the source mapping, but it does not make an experiment independently reproducible. Selected aggregate outcomes and their caveats are published separately in [results](results.md) and [`historical_research.csv`](../reports/curated_results/historical_research.csv).

## How to read the catalog

- **Research family** groups related ideas for navigation; it does not imply that the experiments are equivalent.
- **Method or variant** preserves the report title. A changed statistic, representation, calibration rule, or model objective remains visible as its own entry; staged evaluations of the same recipe share a catalog ID.
- **Causal evidence** distinguishes a stated causal design from a reported prefix or future-mutation check. Neither label substitutes for inspecting the implementation and audit scope.
- **Evaluation scope** separates synthetic feasibility, full grouped-fold records, partial-fold screens, and package replays. A package replay does not certify model selection or fold independence.
- **Validation labels** preserve known caveats such as `POST_SELECTION_CV`, `NON_NESTED_META_CV`, `PARTIAL_FOLD`, and `INVALID_FUTURE_LENGTH`. `UNKNOWN_FROM_PUBLIC_INDEX` means the reviewed public summary does not justify a stronger claim.
- **Missing detail** is labeled `Not preserved in the public summary` or `UNKNOWN_FROM_PUBLIC_INDEX`. This is not evidence that a method, control, or audit was absent; it means the release does not publish a verified detail for that field.
- **Matched control** is report-specific only when the catalog names one. Otherwise the row says that a control was not preserved in its public summary; family-level examples and comparison principles are in [failed and inconclusive experiments](failed_experiments.md).
- **Implementation status**, **validation stage**, and **final status** are structured fields in the CSV. `NOT_SHIPPED` means the historical prototype is not part of the public core; `UNKNOWN_FROM_PUBLIC_INDEX` records where the source summary does not support a stronger stage claim.

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

The catalog marks a report-specific control as unknown when no release-safe control summary was retained. The general comparison rule used in this retrospective is to match the information set, stream, window, normalization, compute budget, and threshold calibration, then reduce the proposed method to a simple control such as low-order moments, autocorrelation, the same conditional innovations with a CUSUM, or the frozen reference head. This guards against crediting an elaborate representation for extra context, tuning, or a stronger downstream model.

The clean, public comparison is the [reproducible synthetic benchmark](results.md#clean-reproducible-synthetic-benchmark). Competition-derived comparisons remain separate because private inputs and artifacts are unavailable for independent replay.

## Scope and limitations

The catalog is a curated map, not a downloadable implementation of every experiment. It summarizes source reports and code-only metric records while keeping private data, OOF predictions, checkpoints, logs, and data locations out of the release. The source reports were written during active research and include exploratory or post-selection estimates. Consult [validation](validation.md) before interpreting a score, and [research journey](research_journey.md) for how the protocol changed after the future-length and nested-OOF audits.

## Complete method and variant register

This release contains **140 curated records**: **129 `CAT-*` records** cover **131 indexed `MTH-*` research reports**, and eleven `SUP-*` records summarize additional evidence. Under the record-type rule, **135 records describe methods or variants** (114 detector/evidence methods, 13 representations/models, seven combinations/scoring heads, and one baseline); the remaining five are four training/selection procedures and one validation audit. Two catalog entries each combine two staged reports, so these totals are not counts of independent algorithms. Report IDs and source evidence IDs preserve provenance. The original reports and private inputs are not distributed. Matching a source digest verifies which record informed the summary; it does not make the experiment independently reproducible.

Each entry retains the experiment question, implementation or explicit unknown, matched control, evaluation scope, validation labels, outcome, limits, and open question where the reviewed source supports them. `UNKNOWN_FROM_PUBLIC_INDEX` and similar labels are retained when the source record does not justify a stronger statement.

### Conditional normalization and score transforms

<details>
<summary><code>CAT-002</code> · <code>MTH-002</code> · Adjusted-Range ECDF CUSUM / RSMS — Search Report</summary>

**Record type:** detector or evidence method.

**Reported family label:** Adjusted Range Ecdf Rsms.

**Question or hypothesis:** On the production Rosenblatt-normalized innovation stream, historical empirical-CDF influence scores (several quantile indicators) may provide causal, self-normalized cumulative evidence for marginal and dynamic changes. The adjusted-range denominator is estimated only from the historical segment. The RSMS monitoring boundary may help rank early breaks when streams have different history lengths. This is a detector-feature experiment, not a change to the locked model. It does not yet implement Bayesian integration over candidate break time `tau`.

**Implementation:** Five historical empirical-CDF quantile-indicator channels feed adjusted-range CUSUM/RSMS evidence on the history-normalized innovation stream. The range denominator is fitted from history only; the candidate adds detector features rather than changing the locked model.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Adjusted-Range ECDF CUSUM / RSMS — Search Report

**Matched control:** The matched P2+auxiliary+CRM baseline was replayed on the same grouped folds.

**Causal evidence:** The adjusted range uses a history-only denominator; sampled exact online-transform replay and future-suffix mutation checks were reported.

**Evaluation scope:** Grouped CV-A F4/F1 Stage-1 screen; no promotion.

**Validation labels:** VALID_EXACT_STREAM; PARTIAL_FOLD; POST_SELECTION_CV

**Result and disposition:** Stage-1 grouped-fold screen completed; the combined candidate declined on both screened folds and was not promoted.

**Limit / reason deprioritized:** The combined candidate declined on both screened folds. No Stage-2 or deployment integration followed.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `PARTIAL_GROUPED_CV_A`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-009</code> · <code>MTH-009</code> · Bayesian Restart Likelihood on Rosenblatt Scores</summary>

**Record type:** detector or evidence method.

**Reported family label:** Bayesian Restart Likelihood.

**Question or hypothesis:** Integrating likelihood-ratio evidence over candidate change starts and a small set of post-change alternatives may preserve weak persistent evidence that a single maximum scan misses. This experiment adds evidence features to a previously computed, history-only Rosenblatt normal-score stream; it does not refit the normalization.

**Implementation:** The frozen input is the history-only Rosenblatt stream, built from historical AR residuals, pre-update EWMA scale, and a historical empirical-CDF normal score. The restart likelihood features compare the fixed reference with a small set of post-change alternatives and mix evidence over candidate starts; no future observation or final stream length is used.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Bayesian Restart Likelihood on Rosenblatt Scores

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** Grouped CV-A: eta was selected using F4/F2, then frozen and evaluated on F1/F3/F0. The feature update consumes one observation at a time; no reduced evaluation, CV-B, provider run, or deployment package.

**Validation labels:** VALID_EXACT_STREAM; POST_SELECTION_CV; CLOUD_PRIVATE

**Result and disposition:** Status: Stage 1 plus frozen Stage 2 transfer complete; exploratory only, not promoted. Scope: New causal evidence features over the existing history-whitened stream; no deployment-package change.

**Limit / reason deprioritized:** No further reason for deprioritization is preserved in the public summary.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `GROUPED_CV_A_FULL_OR_REPLAY`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-020</code> · <code>MTH-020</code> · Boundary-Reflected Conditional Copula KDE — Stage 0</summary>

**Record type:** detector or evidence method.

**Reported family label:** Conditional Copula.

**Question or hypothesis:** After history-fitted AR/Rosenblatt whitening, nonlinear or asymmetric lag-one dependence may remain. This Stage-0 experiment fitted a boundary-reflected conditional KDE to historical lag pairs and tested a history-conditional PIT for online evidence. It stopped before supervised CV; no transfer or detection-performance claim follows.

**Implementation:** Fit a boundary-reflected conditional Gaussian KDE to history-only lag-one pairs, then evaluate online pairs against that frozen conditional reference. The screen stopped before supervised CV.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Boundary-Reflected Conditional Copula KDE — Stage 0

**Matched control:** The Stage-0 diagnostic compared the conditional KDE with simpler Gaussian and independence conditional models; it produced no supervised matched-head result.

**Causal evidence:** The conditional reference was fit from history and frozen for the online diagnostic; no future stream values entered the estimator.

**Evaluation scope:** Stage-0 conditional-density diagnostic only; no CV-A, CV-B, or reduced evaluation.

**Validation labels:** VALID_EXACT_STREAM; SYNTHETIC_OR_STAGE0_ONLY

**Result and disposition:** Stopped before supervised CV. The tested lag-one conditional KDE was a feasibility diagnostic only and did not establish a TS-AUC result.

**Limit / reason deprioritized:** The tested lag-one estimator was overfit and lost to independence/Gaussian alternatives; no TS-AUC result was produced.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `SYNTHETIC_ONLY_SCREEN`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-022</code> · <code>MTH-022</code> · Conditional Expectile Score-CUSUM — Synthetic Stage 0 Report</summary>

**Record type:** detector or evidence method.

**Reported family label:** Conditional Expectile.

**Question or hypothesis:** Not preserved in the public summary; see the report title and source digest.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Not preserved in the public summary.

**Tested settings or stage:** Conditional Expectile Score-CUSUM — Synthetic Stage 0 Report

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** synthetic_screen

**Validation labels:** UNKNOWN_FROM_PUBLIC_INDEX

**Result and disposition:** The conditional expectile score-CUSUM failed its synthetic gate and was closed.

**Limit / reason deprioritized:** No further reason for deprioritization is preserved in the public summary.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `SYNTHETIC_ONLY_SCREEN`.

**Final status:** `HISTORICAL_RESULT_RECORDED_STATUS_UNSPECIFIED`.
</details>

<details>
<summary><code>CAT-023</code> · <code>MTH-023</code> · Conditional Hyvarinen Score Evidence on the Rosenblatt Stream</summary>

**Record type:** detector or evidence method.

**Reported family label:** Conditional Hyvarinen.

**Question or hypothesis:** The hypothesis was that after the production-style historical Rosenblatt transform, a recent-online conditional density fit would reveal changes in the innovation law that are weak in raw-value features. For each current online innovation, cubic Hermite score models compare a history reference against causally fitted recent-online alternatives. Their score differences are aggregated using fixed-window CUSUM and candidate-change-time mixtures.

**Implementation:** Cubic Hermite score models compared a history reference with causally fitted recent-online alternatives. Score differences were aggregated with fixed-window CUSUMs and candidate-change-time mixtures. The screen covered marginal and conditional variants at windows 16, 32, 64, and 128; W128 channels were frozen before the F0/F2/F3 screen.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Conditional Hyvarinen Score Evidence on the Rosenblatt Stream

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** feasibility_or_planned

**Validation labels:** UNKNOWN_FROM_PUBLIC_INDEX

**Result and disposition:** Status: Stage 0–2 completed; this exact estimator/head is not promoted.

**Limit / reason deprioritized:** No further reason for deprioritization is preserved in the public summary.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `FEASIBILITY_OR_PLANNED`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-024</code> · <code>MTH-024</code> · Causal Conditional-PIT Complement Search</summary>

**Record type:** detector or evidence method.

**Reported family label:** Conditional Pit.

**Question or hypothesis:** Can a history-fitted conditional PIT provide an innovation representation that makes online change evidence more comparable across heterogeneous streams?

**Implementation:** The original batch normalization selected its historical-null segment using the final online length, which is unavailable at inference time. The repair fits and calibrates from history and the observed prefix only; it remained an unpromoted complement to the locked stream.

**Reference / online information:** Not preserved in the public summary.

**Tested settings or stage:** Causal Conditional-PIT Complement Search

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** A future-length leakage was discovered and removed; the repaired transform was checked with exact-prefix and future-suffix mutation tests.

**Evaluation scope:** An early path used final online length and was later repaired to use history/prefix information. The selected head/blend was tuned on F4/F0, frozen for all five CV-A folds, and checked once on a reduced diagnostic; CV-B remained sealed.

**Validation labels:** INVALID_FUTURE_LENGTH; VALID_EXACT_STREAM (repaired path); POST_SELECTION_CV; CLOUD_PRIVATE

**Result and disposition:** The initial PIT path used final online length and is labeled INVALID_FUTURE_LENGTH. A history/prefix-only repair passed causality checks but remained an unpromoted complement to the locked Trial-52 stream.

**Limit / reason deprioritized:** The invalid historical score is not reusable as a causal result. The repaired conditional-PIT feature did not establish an independent gain over existing evidence.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `GROUPED_CV_A_FULL_OR_REPLAY`.

**Final status:** `HISTORICAL_RESULT_RECORDED_STATUS_UNSPECIFIED`.
</details>

<details>
<summary><code>CAT-062</code> · <code>MTH-062</code> · NP-FOCuS on the Exact Rosenblatt Stream</summary>

**Record type:** detector or evidence method.

**Reported family label:** Np Focus Rosenblatt.

**Question or hypothesis:** The locked Trial52 system turns each observation into a history-initialized, causal Rosenblatt normal score and then integrates parametric evidence over a small set of recent durations. This experiment asks whether the *full Bernoulli likelihood-ratio scan over candidate change locations* on history-calibrated quantile indicators captures marginal-distribution change evidence not represented by those existing parametric duration mixtures.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** NP-FOCuS on the Exact Rosenblatt Stream

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** grouped_cv_a_partial

**Validation labels:** PARTIAL_FOLD_WHERE_APPLICABLE

**Result and disposition:** Not promoted: a small F4 gain did not offset the larger F1 regression, the two-fold mean declined, and the standalone score remained weak.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `PARTIAL_GROUPED_CV_A`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-096</code> · <code>MTH-096</code> · Historical Conditional-EWMA PIT — Search Report</summary>

**Record type:** detector or evidence method.

**Reported family label:** Rosenblatt Conditional Ecdf.

**Question or hypothesis:** The current stream standardizes online AR innovations with a causal EWMA conditional scale, while its historical ECDF reference uses AR residuals divided by one global scale. The proposed coherent alternative applies that same pre-observation EWMA recursion to historical residuals, then continues its terminal variance into online monitoring. This is a plausible calibration consistency issue, not evidence by itself that the deployed PIT is invalid.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Historical Conditional-EWMA PIT — Search Report

**Matched control:** To distinguish reference standardization from carrying the scale state, a predeclared 2×2 ablation used four fresh seeds and the same mechanisms: | Arm | GARCH Δ KS | Log-SV Δ KS | GARCH Δ abs ACF1(z²) | Log-SV Δ abs ACF1(z²) | CV-A eligible | |---|---:|---:|---:|---:|---| | Conditional reference, reset state | −0.004236 | −0.000174 | −0.000517 | +0.000034 | No |

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** Synthetic Stage 0 on 384 streams; prefix/suffix invariance was reported. No CV-A/B, reduced, private-data, provider, or deployment evaluation.

**Validation labels:** SYNTHETIC_ONLY; VALID_EXACT_STREAM

**Result and disposition:** The fixed historical-EWMA-reference recipe was closed after Stage 0; no challenge-fold validation was run.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `SYNTHETIC_ONLY_SCREEN`.

**Final status:** `HISTORICAL_RESULT_RECORDED_STATUS_UNSPECIFIED`.
</details>

<details>
<summary><code>CAT-098</code> · <code>MTH-098</code> · History-Fitted GARCH PIT Whitening — Stage 0</summary>

**Record type:** detector or evidence method.

**Reported family label:** Rosenblatt Garch Ecdf.

**Question or hypothesis:** The current real-time Rosenblatt pipeline uses a fixed-beta EWMA conditional scale. This experiment tested a distinct history-fitted Gaussian-QMLE GARCH(1,1) scale model: fit only on historical AR innovations; standardize the historical reference by strictly pre-observation scales; continue the fitted variance state online; then form the empirical-CDF normal scores against the standardized historical reference.

**Implementation:** The current real-time Rosenblatt pipeline uses a fixed-beta EWMA conditional scale. This experiment tested a distinct history-fitted Gaussian-QMLE GARCH(1,1) scale model: fit only on historical AR innovations; standardize the historical reference by strictly pre-observation scales; continue the fitted variance state online; then form the empirical-CDF normal scores against the standardized historical reference.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** History-Fitted GARCH PIT Whitening — Stage 0

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** feasibility_or_planned

**Validation labels:** UNKNOWN_FROM_PUBLIC_INDEX

**Result and disposition:** The history-fitted GARCH PIT branch remained a Stage-0 feasibility result; no clean challenge benchmark or public model was produced.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `FEASIBILITY_OR_PLANNED`.

**Final status:** `HISTORICAL_RESULT_RECORDED_STATUS_UNSPECIFIED`.
</details>

<details>
<summary><code>CAT-099</code> · <code>MTH-099</code> · Search Report: Historical-Null Hard-Negative Weighting</summary>

**Record type:** detector or evidence method.

**Reported family label:** Rosenblatt Hard Negative.

**Question or hypothesis:** The historical segment contains no break. Rows whose historical-null evidence looks unusually break-like may therefore act as hard negatives. This screen tested whether moderately upweighting those negative training rows improves the P2 historical-null robust-z head.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Search Report: Historical-Null Hard-Negative Weighting

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** grouped_cv_a_partial

**Validation labels:** PARTIAL_FOLD_WHERE_APPLICABLE

**Result and disposition:** Every tested positive hard-negative weighting setting hurt the screened reference on F4/F0; no further promotion.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `PARTIAL_GROUPED_CV_A`.

**Final status:** `HISTORICAL_RESULT_RECORDED_STATUS_UNSPECIFIED`.
</details>

<details>
<summary><code>CAT-100</code> · <code>MTH-100</code> · Exact Rosenblatt-Stream Historical CMM — Search Report</summary>

**Record type:** detector or evidence method.

**Reported family label:** Rosenblatt History Cmm.

**Question or hypothesis:** Test whether a causal candidate-start conformal-martingale mixture over the history-fitted Rosenblatt stream adds break evidence beyond static AR-residual ranks. The report evaluates fixed start-prior and betting-density banks and a compact scoring head; its assumptions do not justify an e-process or false-alarm guarantee for the fitted dependent stream.

**Implementation:** A history-fitted AR residual, EWMA conditional scale, and historical ECDF produce normal-score innovations. A fixed-bank CMM updates on the online prefix; unit and near-harmonic start priors and bidirectional Beta betting banks were screened. Compact channels were also combined with a baseline score and stream age in a fixed LightGBM head.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Exact Rosenblatt-Stream Historical CMM — Search Report

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** grouped_cv_a_full_or_replay

**Validation labels:** UNKNOWN_FROM_PUBLIC_INDEX

**Result and disposition:** Decision: Close this fixed Beta-bank / start-prior / binary-head recipe after the frozen Fold 4/Fold 1 screen. Do not promote it. This does not reject every conformal martingale, betting construction, or state-aware e-process.

**Limit / reason deprioritized:** No further reason for deprioritization is preserved in the public summary.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `GROUPED_CV_A_FULL_OR_REPLAY`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-104</code> · <code>MTH-104</code> · Search Report: Self-Normalized Whitened Change Statistics</summary>

**Record type:** detector or evidence method.

**Reported family label:** Rosenblatt Selfnorm.

**Question or hypothesis:** Self-normalized sequential statistics on Rosenblatt-whitened innovations may reduce sensitivity to unstable long-run variance estimates and improve the difficult Fold 4 without adding a large feature block.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Search Report: Self-Normalized Whitened Change Statistics

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** Settings were selected on F4/F0, then frozen for five-fold CV-A evaluation. No reduced-data result is reported.

**Validation labels:** POST_SELECTION_CV; CLOUD_PRIVATE

**Result and disposition:** Retained only as a Fold-4 diagnostic; not deployed or submitted.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `GROUPED_CV_A_FULL_OR_REPLAY`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-105</code> · <code>MTH-105</code> · Rosenblatt Tail-Channel Replication — Synthetic Stage 0</summary>

**Record type:** detector or evidence method.

**Reported family label:** Rosenblatt Tail Channel.

**Question or hypothesis:** An earlier synthetic screen suggested that the existing Rosenblatt tail channel may respond more strongly than joint evidence to a Gaussian-to-t(5) change. This replication used four fresh, pre-frozen seeds with the same causal transform and generator; it added no feature and trained no model.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Rosenblatt Tail-Channel Replication — Synthetic Stage 0

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** feasibility_or_planned

**Validation labels:** UNKNOWN_FROM_PUBLIC_INDEX

**Result and disposition:** Fresh-seed synthetic mechanism replication passed; no challenge-fold result or promotion followed.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `SYNTHETIC_ONLY_SCREEN`.

**Final status:** `HISTORICAL_RESULT_RECORDED_STATUS_UNSPECIFIED`.
</details>

<details>
<summary><code>CAT-106</code> · <code>MTH-106</code> · Hill-Style Tail-Excess Severity — Synthetic Stage 0</summary>

**Record type:** detector or evidence method.

**Reported family label:** Rosenblatt Tail Excess.

**Question or hypothesis:** Clean V3 already includes and uses binary-threshold tail evidence (`rw_tail_*`) as well as joint evidence. This test did not address a missing generic tail channel. It asked the narrower question of whether the *magnitudes* of Rosenblatt-score threshold exceedances add a useful causal signal beyond the already-present tail log-mixture.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Hill-Style Tail-Excess Severity — Synthetic Stage 0

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** synthetic_screen

**Validation labels:** UNKNOWN_FROM_PUBLIC_INDEX

**Result and disposition:** The fixed Gamma-integrated tail-excess recipe failed its synthetic gate and was closed.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `SYNTHETIC_ONLY_SCREEN`.

**Final status:** `HISTORICAL_RESULT_RECORDED_STATUS_UNSPECIFIED`.
</details>

<details>
<summary><code>CAT-110</code> · <code>MTH-110</code> · SDNML on the Exact Rosenblatt Stream</summary>

**Record type:** detector or evidence method.

**Reported family label:** Sd Nml.

**Question or hypothesis:** Not preserved in the public summary; see the report title and source digest.

**Implementation:** Urabe et al. (2011) introduce sequentially discounting normalized maximum-likelihood coding for online change detection with an autoregressive model ([DOI](https://doi.org/10.1007/978-3-642-20847-8_16)). This experiment used an autoregressive code-length score on the history-normalized innovation stream; its Stage-0 gate failed.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** SDNML on the Exact Rosenblatt Stream

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** feasibility_or_planned

**Validation labels:** UNKNOWN_FROM_PUBLIC_INDEX

**Result and disposition:** The frozen two-layer SDNML score failed its synthetic gate; this tested configuration was not promoted.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `FEASIBILITY_OR_PLANNED`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

### Conformal and sequential inference

<details>
<summary><code>CAT-021</code> · <code>MTH-021</code> · Conditional Conformal Test Martingale — Research Report</summary>

**Record type:** detector or evidence method.

**Reported family label:** Conditional Ctm.

**Question or hypothesis:** When a scalar causal forecast-residual stream is stable, its historical holdout residuals provide a fixed null reference. A conditional conformal test martingale (CCTM) can use that reference without absorbing post-break observations: a DKW uncertainty penalty corrects repeated ECDF reuse, while online Newton steps (ONS) choose a predictable direction for betting.

**Implementation:** Split a synthetic or per-ID historical series chronologically: fit the fixed AR score map on the prefix, calculate held-out historical residuals for `D0`, then freeze the map and reference before online scoring. - At online time `t`, calculate the current residual from history and current `x_t` only; map it and its absolute value through their fixed reference ECDFs; apply CCTM bets using `eta_t` learned through `t-1`; then update ONS. - Keep `D0` immutable.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Conditional Conformal Test Martingale — Research Report

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** causal_design_or_exact_stream_reported; audit_scope_varies

**Evaluation scope:** synthetic_screen

**Validation labels:** UNKNOWN_FROM_PUBLIC_INDEX

**Result and disposition:** The candidate-start conformal mixture passed selected IID synthetic gates, but dependent-AR null stress was severe and the fold screen was weak; no blend was promoted.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `SYNTHETIC_ONLY_SCREEN`.

**Final status:** `HISTORICAL_RESULT_RECORDED_STATUS_UNSPECIFIED`.
</details>

<details>
<summary><code>CAT-026</code> · <code>MTH-026</code> · Sequential Insertion-Rank Conformal Restart Evidence</summary>

**Record type:** detector or evidence method.

**Reported family label:** Conformal Restart Martingale.

**Question or hypothesis:** Bhattacharyya and Ramdas propose conformal martingales with local restarts and aggregate restart evidence for change detection. Their paper assumes exchangeable/IID observations for the stated validity and delay guarantees. This challenge adaptation uses estimated AR innovations that may remain dependent, with deterministic midranks for ties; no conformal validity, e-process, PFA, or ARL guarantee is claimed.

**Implementation:** A fixed historical reference supplies insertion ranks for each online standardized residual. The implementation uses deterministic midranks for ties and mixes likelihood-ratio evidence over candidate restart times. The score is an empirical ranking feature, not a conformal guarantee, e-process, or calibrated false-alarm procedure.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Sequential Insertion-Rank Conformal Restart Evidence

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** grouped_cv_a_full_or_replay

**Validation labels:** UNKNOWN_FROM_PUBLIC_INDEX

**Result and disposition:** A post-selection CV-A lift and one weak reduced diagnostic did not justify promotion; the empirical rank score has no conformal or e-process guarantee.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `GROUPED_CV_A_FULL_OR_REPLAY`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-027</code> · <code>MTH-027</code> · Conformal Restart Maximum and tau Mixture</summary>

**Record type:** detector or evidence method.

**Reported family label:** Conformal Restart Max.

**Question or hypothesis:** A maximum over candidate restart times after a finite betting-power mixture may preserve a local alternative diluted by a restart sum. A normalized prior-weighted mixture over restart times may handle an unknown change location better than a maximum or an unweighted restart recurrence.

**Implementation:** Apply a restart maximum and normalized candidate-time prior mixtures, including harmonic and near-harmonic priors, to the existing causal Rosenblatt/P2 evidence streams.

**Reference / online information:** The restart evidence updates on the fixed history-normalized score stream using only the observed prefix; no final online length is used.

**Tested settings or stage:** Conformal Restart Maximum and tau Mixture

**Matched control:** The fixed P2+Aux+CRM baseline on the same grouped CV-A F4/F1 screen.

**Causal evidence:** The six existing CRM outputs were preserved bitwise. Twenty-seven future-suffix prefix checks passed; normalized prior mass and the restart-mixture calculation were also checked.

**Evaluation scope:** Two-fold grouped CV-A F4/F1 Stage-1 screen; no full-fold or package evaluation.

**Validation labels:** VALID_EXACT_STREAM; PARTIAL_FOLD; POST_SELECTION_CV

**Result and disposition:** No candidate was promoted. The restart maximum was slightly negative on both screened means, and the normalized-prior variants lost on F1.

**Limit / reason deprioritized:** Only two folds were screened after prior model development; results are post-selection and do not settle other restart constructions.

**Open question:** Would a restart maximum or normalized candidate-time mixture help under a nested full-fold evaluation?


**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `PARTIAL_GROUPED_CV_A`.

**Final status:** `HISTORICAL_RESULT_RECORDED_STATUS_UNSPECIFIED`.
</details>

<details>
<summary><code>CAT-036</code> · <code>MTH-036</code> · DMD Residual Rank Betting — Search Report</summary>

**Record type:** detector or evidence method.

**Reported family label:** Dmd Residual Betting.

**Question or hypothesis:** The existing delay-DMD head measures online operator adaptation and predictive log-score gain. This experiment asks whether the magnitude and sign of its history-operator one-step residual provide complementary evidence when ranked against a historical residual reference, then accumulated with fixed betting functions and a candidate-change-time mixture. The claim is empirical feature usefulness only.

**Implementation:** For each historical ridge fit, compute the leverage-adjusted leave-one-out residual r_i=(y_i-yhat_i)/(1-h_i), then calibrate online residuals against that history-only reference. Online evidence is emitted one observation at a time.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** DMD Residual Rank Betting — Search Report

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** causal_design_or_exact_stream_reported; audit_scope_varies

**Evaluation scope:** grouped_cv_a_partial

**Validation labels:** PARTIAL_FOLD_WHERE_APPLICABLE

**Result and disposition:** The fixed-power residual-rank betting block improved one fold but lost on the held F1/F3 folds; not promoted.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `PARTIAL_GROUPED_CV_A`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-039</code> · <code>MTH-039</code> · Causal Evidence Portfolio Optimizer — Stage 1</summary>

**Record type:** detector or evidence method.

**Reported family label:** Evidence Portfolio Optimizer.

**Question or hypothesis:** Can label-blind causal evidence streams for historical-null Rosenblatt evidence, sequential RFF, conditional dynamics, residual betting, martingale evidence, and spectral discrepancy be combined by a compact nonnegative portfolio? Does Optuna TPE or a metaheuristic improve on random search when judged on outer grouped folds?

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Causal Evidence Portfolio Optimizer — Stage 1

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** Grouped leave-one-fold-out evaluation over all five CV-A folds; portfolio signs and weights for each outer fold were learned on the other four. CV-B remained sealed; no reduced diagnostic or provider run.

**Validation labels:** POST_SELECTION_CV; CLOUD_PRIVATE

**Result and disposition:** Causal Evidence Portfolio Optimizer — Stage 1 Decision: Not promising as a standalone candidate; do not promote or spend more budget tuning these six channels.

**Limit / reason deprioritized:** No further reason for deprioritization is preserved in the public summary.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `GROUPED_CV_A_FULL_OR_REPLAY`.

**Final status:** `HISTORICAL_RESULT_RECORDED_STATUS_UNSPECIFIED`.
</details>

<details>
<summary><code>CAT-043</code> · <code>MTH-043</code> · Fixed-History Conformal Mixture Martingale</summary>

**Record type:** detector or evidence method.

**Reported family label:** Fixed History Cmm.

**Question or hypothesis:** Can a fixed historical rank bank, combined with a shared betting-density mixture over candidate post-change starts, retain localized evidence and add information beyond the existing history-seeded insertion-rank CRM? The first implementation uses static AR residual ranks rather than the full conditional Rosenblatt pipeline.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Fixed-History Conformal Mixture Martingale

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** causal_design_or_exact_stream_reported; audit_scope_varies

**Evaluation scope:** Synthetic feasibility followed by CV-A F4/F1 selection and frozen checks on F0/F2/F3. Feature-level bitwise replay and prefix checks were reported; integrated main.infer parity was not tested.

**Validation labels:** VALID_EXACT_STREAM; POST_SELECTION_CV; CLOUD_PRIVATE

**Result and disposition:** The synthetic tail gain did not transfer to challenge CV-A; OOF errors remained correlated and exact deployed-package parity was not established.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `GROUPED_CV_A_FULL_OR_REPLAY`.

**Final status:** `HISTORICAL_RESULT_RECORDED_STATUS_UNSPECIFIED`.
</details>

<details>
<summary><code>CAT-068</code> · <code>MTH-068</code> · ONS Betting Evidence on Rosenblatt Innovations</summary>

**Record type:** detector or evidence method.

**Reported family label:** Ons Betting.

**Question or hypothesis:** A predictable bet that adapts its stake to the observed innovation stream may turn a weak directional departure into compact cumulative evidence. This is different from the existing predictive-rank martingale, which bets on conditionally centered rank payoffs, and from Bayesian restart likelihood, which mixes fixed likelihood alternatives over candidate start times.

**Implementation:** The source `rw_z` is the existing history-fitted AR residual, divided by a pre-update EWMA scale, then mapped through a historical ECDF to a normal score. For each stream, transform the observed score at step `t` to `u_t = tanh(rw_z_t)`, so `u_t ∈ (-1, 1)`. Starting with wealth `W_0=1`, stake `lambda_1=0`, and curvature accumulator `A_0=1`, update in this order: 1. Consume the current bounded score with the already-known stake: `log(W_t) = log(W_(t-1)) + log(1 + lambda_t * u_t)`. 2.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** ONS Betting Evidence on Rosenblatt Innovations

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** Staged full five-fold CV-A evaluation with a negative mean result, followed by one reduced-transfer diagnostic. CV-B was not accessed; feature construction was label-blind.

**Validation labels:** VALID_EXACT_STREAM; POST_SELECTION_CV; CLOUD_PRIVATE

**Result and disposition:** The ONS betting feature was evaluated with a frozen small blend; the selected increment did not justify promotion.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `GROUPED_CV_A_FULL_OR_REPLAY`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-076</code> · <code>MTH-076</code> · P6 Causal Martingale Search Report</summary>

**Record type:** detector or evidence method.

**Reported family label:** P6 Causal Martingale.

**Question or hypothesis:** Not preserved in the public summary; see the report title and source digest.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** P6 Causal Martingale Search Report

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** grouped_cv_a_partial

**Validation labels:** PARTIAL_FOLD_WHERE_APPLICABLE

**Result and disposition:** Stage 1: Fold 4 and Fold 0; no test-reduced labels.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `PARTIAL_GROUPED_CV_A`.

**Final status:** `HISTORICAL_RESULT_RECORDED_STATUS_UNSPECIFIED`.
</details>

<details>
<summary><code>CAT-090</code> · <code>MTH-090</code> · Predictive Rank Martingale on Direct Standardized Innovations</summary>

**Record type:** detector or evidence method.

**Reported family label:** Predictive Rank Martingale.

**Question or hypothesis:** Predictive-rank martingale (PRM) evidence on continuous standardized innovations, before ECDF normal-score quantization, may preserve rank detail that is lost when the online score stream contains ties. A compact order/dispersion evidence head could complement Trial 11's causal whitened kernel-CUSUM score, especially on difficult Fold 4.

**Implementation:** Fit BIC-selected AR (maximum order 12) on the historical segment only. - Scale historical residuals by the historical standard deviation. - For each online value, compute the one-step innovation and divide by the pre-update EWMA conditional scale (`beta=0.99`); then update the scale. - Use standardized residuals directly for fixed-reference predictive ranks, before mapping online values through the ECDF normal-score transform. - Run separate order and dispersion PRM states on levels and first differences; seed deterministic tie randomization from history/content.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Predictive Rank Martingale on Direct Standardized Innovations

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** Staged CV-A evaluation on F4/F2, then F1/F3, then F0, with complete fold-excluded OOF predictions in the final stage. The candidate was not promoted.

**Validation labels:** POST_SELECTION_CV; CLOUD_PRIVATE

**Result and disposition:** Status: Tested; this head/configuration is not promoted.

**Limit / reason deprioritized:** No further reason for deprioritization is preserved in the public summary.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `GROUPED_CV_A_FULL_OR_REPLAY`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-091</code> · <code>MTH-091</code> · Predictive-Rank Conditional-LR Restart Screen</summary>

**Record type:** detector or evidence method.

**Reported family label:** Predictive Rank Restart.

**Question or hypothesis:** Can evidence mixed over candidate restart times improve causal monitoring of predictive ranks beyond CRM-style adaptive ranks and direct predictive-rank betting? This was an exploratory feature screen.

**Implementation:** Keep the historical rank reference fixed, form a Pólya-urn predictive rank distribution with order and dispersion alternatives, and mix cumulative likelihood-ratio evidence over candidate restart times. Seven causal features were emitted. This empirical score does not claim conformal coverage or an anytime-valid guarantee.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Predictive-Rank Conditional-LR Restart Screen

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** feasibility_or_planned

**Validation labels:** UNKNOWN_FROM_PUBLIC_INDEX

**Result and disposition:** The exploratory CV-A screen was completed; the predictive-rank restart feature was not promoted.

**Limit / reason deprioritized:** No further reason for deprioritization is preserved in the public summary.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `FEASIBILITY_OR_PLANNED`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-101</code> · <code>MTH-101</code> · Whitened Predictive-Rank Martingale / E-Process</summary>

**Record type:** detector or evidence method.

**Reported family label:** Rosenblatt Martingale.

**Question or hypothesis:** After historical AR-BIC residual whitening, predictive rank payoffs and sequential betting evidence may expose changes in location, scale, tail, or dependence. Prefix log-wealth, normalized wealth, CUSUM, rolling evidence, and recent-vs-previous contrasts were tested as causal features for the supervised break model. This report applies only to this implementation and search space.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Whitened Predictive-Rank Martingale / E-Process

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** causal_design_or_exact_stream_reported; audit_scope_varies

**Evaluation scope:** CV-A F4/F0 screen only; no reduced-data result is reported and the candidate was not promoted to full-fold evaluation.

**Validation labels:** PARTIAL_FOLD; POST_SELECTION_CV; CLOUD_PRIVATE

**Result and disposition:** The whitened predictive-rank martingale had little or no complementarity in the full selected CV screen; not promoted.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `PARTIAL_GROUPED_CV_A`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-125</code> · <code>MTH-125</code> · Venn–Abers E-Evidence on the Causal Rosenblatt Stream — 2026-09-26</summary>

**Record type:** detector or evidence method.

**Reported family label:** Venn Abers.

**Question or hypothesis:** Not preserved in the public summary; see the report title and source digest.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Venn–Abers E-Evidence on the Causal Rosenblatt Stream — 2026-09-26

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** feasibility_or_planned

**Validation labels:** UNKNOWN_FROM_PUBLIC_INDEX

**Result and disposition:** Decision: Do not promote this fixed-bin Venn–Abers adaptation.

**Limit / reason deprioritized:** No further reason for deprioritization is preserved in the public summary.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `FEASIBILITY_OR_PLANNED`.

**Final status:** `HISTORICAL_RESULT_RECORDED_STATUS_UNSPECIFIED`.
</details>

<details>
<summary><code>CAT-130</code> · <code>MTH-130</code> · WATCH-Inspired Weighted-Conformal Context Evidence — Stage 1</summary>

**Record type:** detector or evidence method.

**Reported family label:** Weighted Conformal.

**Question or hypothesis:** Prinster et al. (2025), [WATCH](https://proceedings.mlr.press/v267/prinster25a.html), motivate weighted conformal ranks for adaptive monitoring. This experiment tested a causal context-weighted rank feature and does not claim WATCH coverage or martingale guarantees.

**Implementation:** At online step t, estimate context weights only from prior observed context pairs, calculate weighted p-values for positive, negative, and absolute innovation nonconformity, emit the features, and then update the context counts. Weights are clipped to [1/20, 20]; no future observation is used.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** WATCH-Inspired Weighted-Conformal Context Evidence — Stage 1

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** Synthetic calibration screens followed by a grouped CV-A F4/F2 screen. Feature construction was label-blind; no full-fold or provider evaluation is reported.

**Validation labels:** PARTIAL_FOLD; POST_SELECTION_CV; CLOUD_PRIVATE

**Result and disposition:** WATCH-Inspired Weighted-Conformal Context Evidence — Stage 1 Status: tested on Stage-1 folds; this binned context adaptation is not promoted.

**Limit / reason deprioritized:** No further reason for deprioritization is preserved in the public summary.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `PARTIAL_GROUPED_CV_A`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>SUP-004</code> · <code>SRC-018</code> · Transformation-prediction score on causal trailing windows (CODiT/TTPE-inspired)</summary>

**Record type:** detector or evidence method.

**Reported family label:** CODiT-inspired transformation prediction.

**Question or hypothesis:** A history-calibrated score for predicting transformations of a trailing window may flag changes in local temporal structure.

**Implementation:** A fixed five-class transformation predictor on width-64 trailing windows; synthetic-only screen with a history-ECDF score map.

**Reference / online information:** The source record reports history-only normalization and a window ending at the current observation; a prefix mutation check passed for that synthetic implementation.

**Tested settings or stage:** Five transformations; four synthetic test seeds; fixed blend coefficient.

**Matched control:** History-ECDF-calibrated joint reference detector on the same synthetic streams.

**Causal evidence:** prefix mutation audit reported in the synthetic source record

**Evaluation scope:** synthetic_only_frozen_stage0

**Validation labels:** SYNTHETIC_ONLY; FROZEN_GATE_FAILED

**Result and disposition:** The transformation score was near chance, the fixed blend reduced the reference score, and the frozen advancement gate failed. No conformal or Fisher-validity guarantee was claimed.

**Limit / reason deprioritized:** This synthetic adaptation did not meet its predeclared continuation criteria; it was not tested on competition folds.

**Open question:** Can a transformation task be designed that adds stable evidence beyond low-order and conditional-residual controls?



**Implementation status:** `SUPPLEMENTAL_SUMMARY_ONLY_NOT_SHIPPED`.

**Validation stage:** `SYNTHETIC_ONLY_SCREEN`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

### Dynamical and Bayesian models

<details>
<summary><code>CAT-003</code> · <code>MTH-003</code> · AR(p)-Aware FOCuS Evidence — Search Report</summary>

**Record type:** detector or evidence method.

**Reported family label:** Ar Focus.

**Question or hypothesis:** Given a history-fitted AR(p) process, a permanent location shift produces a transient response in the first p prewhitened innovations and a constant response afterward. Weighting those innovations by the AR response may detect autocorrelated location changes that a rolling mean of AR residuals misses.

**Implementation:** Fit historical mean, AR order 0–12, and innovation scale using the reference history. Compute generalized-likelihood evidence over a fixed geometric grid of candidate durations 1–4096. This is a Stage-1 fixed-grid approximation, not the paper’s exact pruned AR(p)-FOCuS algorithm.

**Reference / online information:** AR parameters and scale use history only. At online time t, the score uses observations through t and a predeclared duration grid; the final online length is not used.

**Tested settings or stage:** AR(p)-Aware FOCuS Evidence — Search Report

**Matched control:** Plain rolling-mean / generalized-likelihood evidence on AR residuals and an IID-based scan. The comparison remained a two-fold feasibility screen.

**Causal evidence:** The vectorized scan matched an independent scalar prefix replay, and future-suffix mutation preserved all earlier features for the tested fixed-grid implementation.

**Evaluation scope:** Grouped CV-A F4/F2 feasibility screen; AR-order and scan variants were compared on the same two folds.

**Validation labels:** VALID_EXACT_STREAM; PARTIAL_FOLD; POST_SELECTION_CV

**Result and disposition:** The F4/F2 screen showed no stable across-fold gain; raw AR-adjusted scans were marginally higher than the IID scan on each screened fold, but the feature-only heads remained near chance. Not promoted.

**Limit / reason deprioritized:** The screen showed no stable across-fold gain, and the feature-only heads remained near chance. The experiment did not implement exact pruned AR(p)-FOCuS.

**Open question:** Would an exact AR(p)-FOCuS implementation or the fixed-grid approximation add value for non-location breaks under a full-fold, nested evaluation?


**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `PARTIAL_GROUPED_CV_A`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-004</code> · <code>MTH-004</code> · AR-Score Gaussian GLR with Convex-Hull Pruning</summary>

**Record type:** detector or evidence method.

**Reported family label:** Ar Score Mdfocus.

**Question or hypothesis:** HYPOTHESIS: A structural break can change the conditional dynamics even when raw-value marginal evidence is weak. A history-fitted AR model yields a causal score vector for its coefficients; a shift in the vector mean can be detected by an online multivariate Gaussian GLR, potentially complementing the existing Rosenblatt/P2 and CRM evidence.

**Implementation:** Fit a history-only AR model, transform observations to a causal coefficient-score vector, and monitor shifts in its mean with a multivariate Gaussian GLR. Convex-hull pruning limits candidate change points; the selected feature head combined AR(2) evidence with stream age.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** AR-Score Gaussian GLR with Convex-Hull Pruning

**Matched control:** The AR(2) GLR-plus-age setting and 10% blend were frozen before the held-fold comparison. A same-schema P2+auxiliary+CRM model with an alternate fixed seed served as a generic model-averaging control.

**Causal evidence:** History-only AR fitting and whitening; online score and GLR updates use the current prefix. Sampled prefix replay was reported.

**Evaluation scope:** exact_stream_or_package_replay_scope_unspecified

**Validation labels:** VALID_EXACT_STREAM; POST_SELECTION_CV

**Result and disposition:** Synthetic feasibility and staged CV-A were completed; the AR(2) GLR-plus-age head remains exploratory and was not promoted.

**Limit / reason deprioritized:** The candidate-specific increment was small and did not justify reduced evaluation or package integration; this closes the tested AR(2) configuration only.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `EXACT_STREAM_SCOPE_UNSPECIFIED`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-006</code> · <code>MTH-006</code> · Bayesian AR Context-Tree Evidence</summary>

**Record type:** detector or evidence method.

**Reported family label:** Bayesian Ar Context Tree.

**Question or hypothesis:** Papageorgiou & Kontoyiannis' BCT-AR work motivates integrating over conditional-memory context trees with Gaussian autoregressive leaves. This experiment tested a compact, causal adaptation on the existing exact-stream Rosenblatt innovations. It is distinct from the earlier categorical KT/CTW screen: leaves use conjugate continuous AR likelihoods, not categorical probabilities.

**Implementation:** Papageorgiou & Kontoyiannis' BCT-AR work motivates integrating over conditional-memory context trees with Gaussian autoregressive leaves. This experiment tested a compact, causal adaptation on the existing exact-stream Rosenblatt innovations. It is distinct from the earlier categorical KT/CTW screen: leaves use conjugate continuous AR likelihoods, not categorical probabilities. It is also not a full Bayesian change-point/run-length model and does not integrate the candidate break time `tau`.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Bayesian AR Context-Tree Evidence

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** causal_design_or_exact_stream_reported; audit_scope_varies

**Evaluation scope:** exact_stream_or_package_replay_scope_unspecified

**Validation labels:** UNKNOWN_FROM_PUBLIC_INDEX

**Result and disposition:** The compact context-tree head had a small post-selection CV-A increment, weak standalone performance, highly correlated errors, and a negative frozen reduced diagnostic; not promoted.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `EXACT_STREAM_SCOPE_UNSPECIFIED`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-007</code> · <code>MTH-007</code> · Bayesian Random-Walk AR Coefficient Drift — Search Report</summary>

**Record type:** detector or evidence method.

**Reported family label:** Bayesian Ar Drift.

**Question or hypothesis:** Can posterior-predictive evidence from a causal online model of drifting AR coefficients identify changes in conditional dynamics that a fixed historical whitener misses? This is distinct from the existing scalar score-driven AR(1), run-length MBO(q), and point-estimate DMD/RLS experiments: it maintains a posterior over a vector of lag coefficients and scores each observation before updating that posterior.

**Implementation:** The input is the exact causal Trial-11 historical Rosenblatt/normal-score innovation stream. For AR order p in {1, 4}, the coefficient posterior is initialized from the historical stream. A Gaussian random-walk state model uses process covariance Q = q P0, q in {0.01, 0.1, 1}. At every online step, the observation is first scored under (a) the frozen historical predictive reference and (b) the current posterior-predictive AR model; only then is the coefficient posterior updated. The resulting prequential log-score contrasts are summarized by EWMA-32 and positive CUSUM, for 12 causal features total.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Bayesian Random-Walk AR Coefficient Drift — Search Report

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** causal_design_or_exact_stream_reported; audit_scope_varies

**Evaluation scope:** Five-fold grouped CV-A and one frozen reduced-transfer diagnostic; exact streaming-transform replay and prefix/suffix checks were reported on 131 sampled IDs. No provider run or deployment package.

**Validation labels:** VALID_EXACT_STREAM; POST_SELECTION_CV; CLOUD_PRIVATE

**Result and disposition:** Status: completed exploratory CV-A and one frozen reduced transfer diagnostic; not promoted.

**Limit / reason deprioritized:** No further reason for deprioritization is preserved in the public summary.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `GROUPED_CV_A_FULL_OR_REPLAY`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-008</code> · <code>MTH-008</code> · Bayesian Context-Tree Segmentation — 2026-09-26</summary>

**Record type:** detector or evidence method.

**Reported family label:** Bayesian Context Tree Segmentation.

**Question or hypothesis:** Can a finite-grid Bayesian context-tree model describe piecewise-homogeneous categorical streams with variable-memory Markov structure and infer change locations?

**Implementation:** The starting point is Lungu, Papageorgiou, and Kontoyiannis (2022), [*Change-point Detection and Segmentation of Discrete Data using Bayesian Context Trees*](https://arxiv.org/abs/2203.04341). The paper models finite-alphabet piecewise-homogeneous variable-memory Markov sequences, independently marginalizes each segment under a BCT/Dirichlet prior, carries the preceding maximum-depth context into a new segment, and assigns change locations a prior proportional to the product of segment lengths. Its location inference is retrospective, not an online causal detector.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Bayesian Context-Tree Segmentation — 2026-09-26

**Matched control:** P2+auxiliary+CRM feature head on the same screened folds.

**Causal evidence:** The tested change-location inference is retrospective and uses the sequence segmentation; it is not an online causal detector.

**Evaluation scope:** Synthetic Stage 0 and grouped CV-A F4/F1 screen; fixed blend confirmation used the same development folds.

**Validation labels:** RETROSPECTIVE_NOT_ONLINE; PARTIAL_FOLD; POST_SELECTION_CV

**Result and disposition:** The finite-grid categorical context-tree head lost to its matched control on screened folds; the selected blend did not establish transfer. Closed before reduced evaluation or package integration.

**Limit / reason deprioritized:** The categorical feature head lost to the matched control; the fold-selected blend did not establish transfer. This does not reject continuous Bayesian AR context models.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `SYNTHETIC_ONLY_SCREEN`.

**Final status:** `HISTORICAL_RESULT_RECORDED_STATUS_UNSPECIFIED`.
</details>

<details>
<summary><code>CAT-028</code> · <code>MTH-028</code> · Whitened Categorical Context-Tree Mixture — Search Report</summary>

**Record type:** detector or evidence method.

**Reported family label:** Context Tree.

**Question or hypothesis:** After the history-only AR/Rosenblatt transform, discretize the normalized stream and compare a frozen historical context-tree predictor with an identically initialized predictor updated sequentially on the observed online prefix.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Whitened Categorical Context-Tree Mixture — Search Report

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** causal_design_or_exact_stream_reported; audit_scope_varies

**Evaluation scope:** exact_stream_or_package_replay_scope_unspecified

**Validation labels:** UNKNOWN_FROM_PUBLIC_INDEX

**Result and disposition:** Status: Stage-1 completed; tested configurations not promoted.

**Limit / reason deprioritized:** No further reason for deprioritization is preserved in the public summary.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `EXACT_STREAM_SCOPE_UNSPECIFIED`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-031</code> · <code>MTH-031</code> · Cross-ID Bayesian Meta-Prior for Dynamics</summary>

**Record type:** detector or evidence method.

**Reported family label:** Cross Id Bayesian Meta Prior.

**Question or hypothesis:** Huang and Michailidis (2026), [*PAC-Bayesian Meta-Learning for Few-Shot Identification of Linear Dynamical Systems*](https://arxiv.org/abs/2609.24117), model each task's transition matrix with a shared matrix-normal prior, learn its mean and covariance across training tasks using a fit-plus-KL objective, then adapt to a new task with a closed-form posterior.

**Implementation:** Each ID is a task. AR coefficients are fitted after centering/scaling only by that ID's historical segment; a cohort Gaussian prior is learned from other IDs' histories only. - The prior uses a robust empirical mean and method-of-moments covariance, subtracting average task-estimator covariance and flooring eigenvalues.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Cross-ID Bayesian Meta-Prior for Dynamics

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** causal_design_or_exact_stream_reported; audit_scope_varies

**Evaluation scope:** exact_stream_or_package_replay_scope_unspecified

**Validation labels:** UNKNOWN_FROM_PUBLIC_INDEX

**Result and disposition:** The support-query forecasting gain weakened at longer support and the selected TS-AUC lift was tiny; the tested empirical-prior estimator and blend were not promoted.

**Limit / reason deprioritized:** No further reason for deprioritization is preserved in the public summary.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `EXACT_STREAM_SCOPE_UNSPECIFIED`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-034</code> · <code>MTH-034</code> · Delay-DMD / Koopman Dynamics Evidence — Search Report</summary>

**Record type:** detector or evidence method.

**Reported family label:** Dmd Koopman.

**Question or hypothesis:** After historical AR/Rosenblatt normal-score whitening, the online sequence may change its conditional transition law. This experiment compared a compact historical delay operator with a prequential online operator, targeting dynamics that short-window marginal discrepancies may miss.

**Implementation:** On the history-fitted AR/scale/Rosenblatt stream, form causal delay states and fit a fixed linear delay operator from reference history. Compare prequential operator and residual summaries with that frozen reference to produce drift evidence. O-MAGIC was reviewed but not ported because no governing ODE is provided.

**Reference / online information:** Reference: historical AR, scale, and empirical normal-score transform plus a delay operator fit on history. Online: update causal delay-state and residual/operator summaries through the current timestep; no centered window or final horizon is used.

**Tested settings or stage:** Stages included F4/F0 feasibility screening, F1–F3 follow-up, five-fold grouped CV-A cross-fitting, and a frozen one-shot reduced diagnostic. The candidate used delay order 2 and windows 32/64; the feature-only head was also assessed separately.

**Matched control:** The same grouped folds used the Trial-11 kernel-CUSUM reference; a feature-only head isolated the DMD contribution from the blend. The blended head consumed Trial-11 OOF scores, which were not nested against the outer folds.

**Causal evidence:** Independent value-by-value whitening and per-step RLS replay matched on audited samples. Prefix invariance was checked across the development panel for the frozen feature path, with a separate smaller sampled parity audit. These checks do not remove fold-selection or meta-OOF contamination.

**Evaluation scope:** Multi-stage grouped CV-A: two-fold F4/F0 screening, F1–F3 follow-up, then five-fold cross-fitting. A selected candidate was checked once on a reduced diagnostic after freezing; no CV-B labels were used.

**Validation labels:** VALID_EXACT_STREAM; NON_NESTED_META_CV; POST_SELECTION_CV; REDUCED_ONLY; CLOUD_PRIVATE

**Result and disposition:** The selected delay-order-2 blend improved the development folds but fell below its Trial-11 comparator on the one-shot reduced diagnostic. The feature-only grouped-CV head was much weaker than the blend. The configuration was not promoted.

**Limit / reason deprioritized:** The CV-A record was selection-exposed and its blend reused non-nested Trial-11 OOF scores. The single reduced diagnostic showed a transfer gap and cannot be reused for tuning. These results concern the tested configuration, not all DMD or Koopman approaches.

**Open question:** Can causal DMD residual features retain value under nested outer-fold training and matched low-order controls, with package-level prefix parity?



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `GROUPED_CV_A_FULL_OR_REPLAY`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-035</code> · <code>MTH-035</code> · DMD Residual-Rank Markov Transition — Search Report</summary>

**Record type:** detector or evidence method.

**Reported family label:** Dmd Markov Transition.

**Question or hypothesis:** The marginal distribution of a history-calibrated DMD residual rank can remain similar while its conditional transition law changes. A smoothed transition model, fit using only the historical reference, could expose persistence or switching patterns that the baseline score and ordinary residual magnitude do not represent directly.

**Implementation:** Fit a ridge linear predictor to the historical whitened stream, calibrate residuals with analytic leave-one-out correction, and convert signed residuals to historical-calibrated ranks. Discretize ranks into four bins, estimate a smoothed historical transition matrix, and emit current-rank and cumulative likelihood-ratio features over tilted transition alternatives.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** DMD Residual-Rank Markov Transition — Search Report

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** Four-stage evaluation: F2/F4 feasibility, F1/F3 screen, frozen p=4 five-fold cross-fit, and one frozen reduced diagnostic. The recorded feature path excludes future and terminal-length information.

**Validation labels:** VALID_EXACT_STREAM; POST_SELECTION_CV; CLOUD_PRIVATE

**Result and disposition:** The four-bin residual-rank transition head was weak, its selected CV-A gain was negligible, and reduced transfer was negative; not promoted.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `GROUPED_CV_A_FULL_OR_REPLAY`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-037</code> · <code>MTH-037</code> · Dynamic Geometric Tau-Grid — Stage 1 Report</summary>

**Record type:** detector or evidence method.

**Reported family label:** Dynamic Tau Grid.

**Question or hypothesis:** Not preserved in the public summary; see the report title and source digest.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Dynamic Geometric Tau-Grid — Stage 1 Report

**Matched control:** The Trial 11 exact-stream reference served as the matched baseline. A fixed 20% feature blend was compared on the screened folds; those folds also informed the feature choice, so the comparison is post-selection.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** grouped_cv_a_partial

**Validation labels:** PARTIAL_FOLD_WHERE_APPLICABLE

**Result and disposition:** Only a partial-fold, post-selection screen was completed. The frozen candidate was not established as an independent improvement.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `PARTIAL_GROUPED_CV_A`.

**Final status:** `HISTORICAL_RESULT_RECORDED_STATUS_UNSPECIFIED`.
</details>

<details>
<summary><code>CAT-047</code> · <code>MTH-047</code> · Latent Switching AR on Rosenblatt Innovations — Search Report</summary>

**Record type:** detector or evidence method.

**Reported family label:** Latent Switching Ar.

**Question or hypothesis:** Hypothesis: after the production causal Rosenblatt transform, a break in dependence may appear as a change between latent conditional-AR modes.

**Implementation:** Fit a Gaussian mixture to standardized lag-1 pairs from training histories, then derive state-specific conditional-AR emissions, transitions, and empirical age hazards. A one-pass state-age filter emits transition surprisal and smoothed switching evidence; this observable approximation is not a reproduction of the cited latent-state model.

**Reference / online information:** Input stream: history-fitted BIC-AR residuals, conditional EWMA scale, and historical empirical-CDF normal scores. Fit regime parameters on training histories only; online filtering uses observations through the current timestep.

**Tested settings or stage:** Grouped CV-A Stage-1 screens on F4 and F1, with 2/3 mixture states and geometric or empirical-duration filters; standalone transition-surprise features and a non-deployable complementarity diagnostic were assessed.

**Matched control:** Trial-11 OOF evidence was used for a complementarity diagnostic; no report-specific matched low-order transition control was preserved. That diagnostic ranked validation rows jointly and is not a causal per-ID detector.

**Causal evidence:** The whitening adapter matched the stateful streaming implementation bitwise on the audited sample. The state-age filter is one-pass and uses no future online values. The parity sample does not establish full-panel package parity.

**Evaluation scope:** Two-fold grouped CV-A feature screen (F4/F1); no full CV-A, CV-B, reduced evaluation, private run, or deployment package followed.

**Validation labels:** VALID_EXACT_STREAM; PARTIAL_FOLD; POST_SELECTION_CV; NON_NESTED_META_CV; CLOUD_PRIVATE

**Result and disposition:** The selected state-transition features were near chance on the challenge folds; the synthetic pilot was circular because its generator matched the fitted switching-AR assumptions. The specific lag-1 Gaussian-mixture approximation was stopped before later stages.

**Limit / reason deprioritized:** The targeted transition signal did not transfer to the screened challenge folds. This does not reject richer latent switching models or other transition representations.

**Open question:** Would a more expressive history-fitted regime representation yield useful dependence-change evidence under nested folds and an independent matched control?



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `PARTIAL_GROUPED_CV_A`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-050</code> · <code>MTH-050</code> · MBO(q) Run-Length Evidence on Rosenblatt Innovations</summary>

**Record type:** detector or evidence method.

**Reported family label:** Mbo Q Dependent.

**Question or hypothesis:** Not preserved in the public summary; see the report title and source digest.

**Implementation:** Primary source: Tsaknaki, Lillo, and Mazzarisi (2024), [“Bayesian Autoregressive Online Change-Point Detection with Time-Varying Parameters”](https://arxiv.org/abs/2407.16376). This experiment tests the paper's dependent MBO(q) likelihood, not the older IID-normal inverse-gamma BOCPD addon and not the score-driven MBOC/MBOV predictive-score features. The adaptation first fits the AR/Rosenblatt normal-score reference on each ID's historical segment only.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** MBO(q) Run-Length Evidence on Rosenblatt Innovations

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** Scalar and joint-head stages covered four development folds. The source summary does not establish a complete five-fold evaluation; no CV-B or reduced evaluation is reported.

**Validation labels:** PARTIAL_FOLD; POST_SELECTION_CV; CLOUD_PRIVATE

**Result and disposition:** Status: Scalar Stage 1/2 and fold-excluded joint-head Stage 1/2 are complete; no MBO(q) candidate is promoted.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `PARTIAL_GROUPED_CV_A`.

**Final status:** `HISTORICAL_RESULT_RECORDED_STATUS_UNSPECIFIED`.
</details>

<details>
<summary><code>CAT-061</code> · <code>MTH-061</code> · Normal–Inverse-Gamma Mean/Scale Evidence over Candidate Tau — Stage 0</summary>

**Record type:** detector or evidence method.

**Reported family label:** Normal Inverse Gamma Tau.

**Question or hypothesis:** Can a conjugate normal-inverse-gamma model accumulate causal mean-and-scale evidence across candidate post-change durations, complementing the normalized-innovation baseline? This was a synthetic feasibility screen only.

**Implementation:** For each candidate duration in {4, 8, 16, 32, 64, 128, 256, 512}, maintain a normal-inverse-gamma model for mean and scale and combine prequential evidence over durations available at the current time. No final online length is used.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Normal–Inverse-Gamma Mean/Scale Evidence over Candidate Tau — Stage 0

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** feasibility_or_planned

**Validation labels:** UNKNOWN_FROM_PUBLIC_INDEX

**Result and disposition:** Synthetic feasibility only; the tested normal-inverse-gamma mean/scale feature was weaker than the P2 reference.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `FEASIBILITY_OR_PLANNED`.

**Final status:** `HISTORICAL_RESULT_RECORDED_STATUS_UNSPECIFIED`.
</details>

<details>
<summary><code>CAT-064</code> · <code>MTH-064</code> · Causal ODE-Inspired Segment Evidence — Search Report</summary>

**Record type:** detector or evidence method.

**Reported family label:** Ode Segment Tau.

**Question or hypothesis:** Zhang and Yao (2026), [“Structural Change Detection in Dynamic Systems”](https://arxiv.org/abs/2606.27614), compare fitted segment parameters and residual fit in an ODE regression setting. Their method is retrospective and its assumptions/guarantees do not transfer to this challenge. This experiment tested a causal discrete-time AR(2) adaptation, not the paper's ODE estimator or its theoretical claims.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Causal ODE-Inspired Segment Evidence — Search Report

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** grouped_cv_a_partial

**Validation labels:** UNKNOWN_FROM_PUBLIC_INDEX

**Result and disposition:** Status - Stage 0 passed direct sufficient-statistic checks, synthetic AR(2) switch - Stage 1 completed on CV-A folds F4 and F1.

**Limit / reason deprioritized:** No further reason for deprioritization is preserved in the public summary.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `PARTIAL_GROUPED_CV_A`.

**Final status:** `HISTORICAL_RESULT_RECORDED_STATUS_UNSPECIFIED`.
</details>

<details>
<summary><code>CAT-080</code> · <code>MTH-080</code> · P6 Causal Candidate-Tau Search Report</summary>

**Record type:** detector or evidence method.

**Reported family label:** P6 Causal Tau.

**Question or hypothesis:** Not preserved in the public summary; see the report title and source digest.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Not preserved in the public summary.

**Tested settings or stage:** P6 Causal Candidate-Tau Search Report

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** Reported across all five CV-A folds; the public source summary does not preserve a CV-B, reduced, or provider evaluation.

**Validation labels:** POST_SELECTION_CV; CLOUD_PRIVATE

**Result and disposition:** The tested P6 candidate-change-time configuration remained exploratory and was not promoted.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `GROUPED_CV_A_FULL_OR_REPLAY`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-089</code> · <code>MTH-089</code> · Predictive-Path HMM Beam Evidence</summary>

**Record type:** detector or evidence method.

**Reported family label:** Predictive Hmm Beam.

**Question or hypothesis:** Can a causal posterior over a small set of candidate break paths expose conditional-dynamics changes in the history-whitened innovation stream that are complementary to the current P2 evidence? This tests a different inductive bias from rolling-window scans: persistent predictive compatibility between a frozen reference regime and an adaptive post-switch regime.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Predictive-Path HMM Beam Evidence

**Matched control:** The Trial 11 exact-stream baseline was replayed on the same folds. The two-channel HMM head and 10% blend were frozen before the held-fold comparison; the result remains a selected diagnostic.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** synthetic_screen

**Validation labels:** UNKNOWN_FROM_PUBLIC_INDEX

**Result and disposition:** The matched generic-seed control explained most of the screened predictive-HMM blend gain; this configuration was closed without promotion.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `SYNTHETIC_ONLY_SCREEN`.

**Final status:** `HISTORICAL_RESULT_RECORDED_STATUS_UNSPECIFIED`.
</details>

<details>
<summary><code>CAT-107</code> · <code>MTH-107</code> · Search Report: Rosenblatt–Tau Whitening</summary>

**Record type:** detector or evidence method.

**Reported family label:** Rosenblatt Tau.

**Question or hypothesis:** Does full reference-DGP whitening plus compact tau-integrated evidence add complementary signal to the current V19 components?

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Search Report: Rosenblatt–Tau Whitening

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** The source report describes grouped CV-A TS-AUC variants, but the public summary does not establish the exact fold set or whether a reduced diagnostic was included.

**Validation labels:** UNKNOWN_FROM_PUBLIC_INDEX

**Result and disposition:** The historical P2 value is INVALID_FUTURE_LENGTH. The corrected causal reference is reported separately; the invalid score is not a real-time benchmark.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `UNKNOWN_FROM_PUBLIC_INDEX`.

**Final status:** `HISTORICAL_RESULT_RECORDED_STATUS_UNSPECIFIED`.
</details>

<details>
<summary><code>CAT-109</code> · <code>MTH-109</code> · Score-Driven Conditional Dynamics on Rosenblatt Innovations</summary>

**Record type:** detector or evidence method.

**Reported family label:** Score Driven Dynamics.

**Question or hypothesis:** Not preserved in the public summary; see the report title and source digest.

**Implementation:** Paper: Tsaknaki, Lillo, and Mazzarisi, “Bayesian Autoregressive Online Change-Point Detection with Time-Varying Parameters,” current arXiv v2 posted 2025-09-29, originally 2024. [primary source](https://arxiv.org/abs/2407.16376). The paper defines an autoregressive Bayesian online change-point framework within regimes, then introduces score-driven time-varying autocorrelation (MBOC) and GARCH-like time-varying variance (MBOV) updates. Original assumptions: Gaussian observations with a piecewise-constant regime mean; covariance-stationary dependence within each regime for MBO(q).

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Score-Driven Conditional Dynamics on Rosenblatt Innovations

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** prefix_or_future_mutation_audit_reported

**Evaluation scope:** The staged source describes an initial F2/F4 CV-A screen and one frozen reduced diagnostic, but the public summary does not establish whether a complete five-fold CV-A evaluation followed.

**Validation labels:** UNKNOWN_FROM_PUBLIC_INDEX

**Result and disposition:** Status: Stage 1–3 and one frozen reduced diagnostic complete; not promoted because reduced transfer was negative.

**Limit / reason deprioritized:** No further reason for deprioritization is preserved in the public summary.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `UNKNOWN_FROM_PUBLIC_INDEX`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-112</code> · <code>MTH-112</code> · History-Frozen Soft-AR Gate Screen</summary>

**Record type:** detector or evidence method.

**Reported family label:** Soft Bct.

**Question or hypothesis:** Not preserved in the public summary; see the report title and source digest.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Not preserved in the public summary.

**Tested settings or stage:** History-Frozen Soft-AR Gate Screen

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** Full exact-stream CV-A evaluation followed by one reduced diagnostic after settings were frozen.

**Validation labels:** VALID_EXACT_STREAM; POST_SELECTION_CV; CLOUD_PRIVATE

**Result and disposition:** The history-frozen soft-AR gate remained a staged exploratory result; no promotion claim is made.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `GROUPED_CV_A_FULL_OR_REPLAY`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-113</code> · <code>MTH-113</code> · History-Fit Variational Soft-AR Tree — Stage 0/1</summary>

**Record type:** detector or evidence method.

**Reported family label:** Soft Bct Variational.

**Question or hypothesis:** A learned soft routing tree over recent Rosenblatt innovations can fit state-dependent AR dynamics that a single global AR, quantized hard-context tree, or hand-fixed two-expert gate misses. A prequential posterior-predictive gain against the history-frozen version may therefore add useful early-break ranking evidence, with different errors from the current package.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** History-Fit Variational Soft-AR Tree — Stage 0/1

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** prefix_or_future_mutation_audit_reported

**Evaluation scope:** grouped_cv_a_partial

**Validation labels:** PARTIAL_FOLD_WHERE_APPLICABLE

**Result and disposition:** The variational soft-AR tree was tested only in Stage 0/1 feasibility work; no full grouped-CV result was established.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `PARTIAL_GROUPED_CV_A`.

**Final status:** `HISTORICAL_RESULT_RECORDED_STATUS_UNSPECIFIED`.
</details>

<details>
<summary><code>CAT-114</code> · <code>MTH-114</code> · Sparse Polynomial Transition Evidence — Search Report</summary>

**Record type:** detector or evidence method.

**Reported family label:** Sparse Transition Sindy.

**Question or hypothesis:** PAPER: Quade, Abel, Kutz, and Brunton (2018), [“Sparse Identification of Nonlinear Dynamics for Rapid Model Recovery”](https://doi.org/10.1063/1.5027470). SINDy represents a governing dynamic law in a candidate nonlinear library and uses sequentially thresholded ridge regression to retain a small number of terms. Abrupt-SINDy motivates monitoring coefficient changes and term additions/deletions.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Sparse Polynomial Transition Evidence — Search Report

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** causal_design_or_exact_stream_reported; audit_scope_varies

**Evaluation scope:** exact_stream_or_package_replay_scope_unspecified

**Validation labels:** UNKNOWN_FROM_PUBLIC_INDEX

**Result and disposition:** The selected sparse-polynomial transition screen did not transfer across the tested CV-A folds; not promoted.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `EXACT_STREAM_SCOPE_UNSPECIFIED`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-115</code> · <code>MTH-115</code> · Sparse Transition Bayes Factors Integrated over Candidate Change Time</summary>

**Record type:** detector or evidence method.

**Reported family label:** Sparse Transition Tau.

**Question or hypothesis:** Datta, Zou, and Banerjee (2019), [“Bayesian High-Dimensional Regression for Change Point Analysis”](https://doi.org/10.4310/SII.2019.v12.n2.a6), motivate integrating segment-specific regression evidence over a candidate change time. The tested low-dimensional adaptation is distinct from the paper’s full high-dimensional model.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Sparse Transition Bayes Factors Integrated over Candidate Change Time

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** prefix_or_future_mutation_audit_reported

**Evaluation scope:** grouped_cv_a_partial

**Validation labels:** PARTIAL_FOLD_WHERE_APPLICABLE

**Result and disposition:** The sparse-transition Bayes-factor screen was negative on the tested F4/F1 folds; not promoted.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `PARTIAL_GROUPED_CV_A`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-122</code> · <code>MTH-122</code> · Search Report: TNC Reference-Current Encoder</summary>

**Record type:** representation or model.

**Reported family label:** Tnc Reference Encoder.

**Question or hypothesis:** Temporal-neighborhood contrastive pretraining on historical Rosenblatt innovations may learn a representation whose causal distance from the historical reference complements the Trial13 statistical head, especially on the weak Fold 4.

**Implementation:** To test the B1 formulation more directly, I trained a second compact encoder on two historical-only streams at once: standardized raw values and the AR/ECDF-normalized innovation stream. Each stream supplied value, first difference, absolute value, and sign channels, for eight input channels total. The shared dilated CNN used window 16, a 16-dimensional embedding, 200,000 contrastive pairs, eight epochs, and the same causal reference-versus-current feature construction. Raw standardization used only each ID's historical mean and standard deviation; the online branch ended at the current observed value.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Search Report: TNC Reference-Current Encoder

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** Two-fold screens preceded a full CV-A result recorded in the final stage; no reduced-data result is reported. The result was not replayed in the submission package.

**Validation labels:** POST_SELECTION_CV; CLOUD_PRIVATE

**Result and disposition:** The temporal-neighborhood encoder showed only a small CV-A result; exact package parity was incomplete, so it was not promoted.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `GROUPED_CV_A_FULL_OR_REPLAY`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-131</code> · <code>MTH-131</code> · Search Report: Whitened Historical-Reference Neural Encoder</summary>

**Record type:** representation or model.

**Reported family label:** Whitened Reference Encoder.

**Question or hypothesis:** A shared encoder comparing a fixed historical whitened tail with the observed online prefix may learn a reference-versus-current discrepancy that row-wise tree features miss. This is a different formulation from the earlier raw-input TCN: both branches encode a historical reference and a causal current window.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Search Report: Whitened Historical-Reference Neural Encoder

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** One CV-A screen on F4/F0; no reduced-data result is reported and the candidate was not promoted.

**Validation labels:** PARTIAL_FOLD; POST_SELECTION_CV; CLOUD_PRIVATE

**Result and disposition:** The whitened historical-reference encoder was unstable across folds and did not justify promotion.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `PARTIAL_GROUPED_CV_A`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>SUP-001</code> · <code>SRC-015</code> · Bayesian online change-point run-length features</summary>

**Record type:** detector or evidence method.

**Reported family label:** BOCPD run-length features.

**Question or hypothesis:** Posterior run-length summaries and predictive surprise may add causal break evidence to the locked feature baseline.

**Implementation:** Run-length expectation, short-run mass, entropy, predictive surprise, run-length mode, and cumulative surprise; five-fold grouped OOF metrics are present in a local result record.

**Reference / online information:** The result record alone does not establish update-level prefix parity.

**Tested settings or stage:** One compact LightGBM expert and fixed-weight blends against the same baseline.

**Matched control:** Same-fold fixed baseline in the result record.

**Causal evidence:** not independently established from the result record

**Evaluation scope:** grouped_cv_a_full_oof_result_record

**Validation labels:** POST_SELECTION_CV; CAUSALITY_AUDIT_UNKNOWN

**Result and disposition:** Standalone expert and every tested positive blend weight were below the matched baseline mean; do not promote this configuration.

**Limit / reason deprioritized:** The tested expert did not complement the baseline in grouped CV-A; no independent causal audit is present in the result record.

**Open question:** Can run-length evidence add value with an independently validated online implementation and a genuinely nested training path?



**Implementation status:** `SUPPLEMENTAL_SUMMARY_ONLY_NOT_SHIPPED`.

**Validation stage:** `GROUPED_CV_A_FULL_OR_REPLAY`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

### Kernel, discrepancy, and density comparison

<details>
<summary><code>CAT-001</code> · <code>MTH-001</code> · Adaptive Online Kernel Forgetting — Stage 1</summary>

**Record type:** detector or evidence method.

**Reported family label:** Adaptive Kernel Forgetting.

**Question or hypothesis:** Jiang and Bodenham's [*Adaptive online kernel changepoint detection*](https://arxiv.org/abs/2609.22545) adapts an RKHS mean embedding's forgetting factor online using a directional gradient. Unlike the repository's fixed-rate/dyadic RFF-MMD stream, this experiment asks whether the per-observation memory adaptation adds useful ranking information after historical Rosenblatt whitening.

**Implementation:** A one-dimensional Gaussian random Fourier feature map used 32 frequencies, bandwidth 1, and fixed seed 20260925. It emitted mean-embedding norm, log norm, novelty, gradient, and forgetting-factor evidence; slow, medium, and fast update rates and blend weights 0.02/0.05/0.10 were screened.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Adaptive Online Kernel Forgetting — Stage 1

**Matched control:** Trial-11 exact-stream reference; a same-schema P2+auxiliary+CRM model with an alternate fixed seed controlled for generic model averaging.

**Causal evidence:** History-centered embedding; online forgetting factor updates one observation at a time. Sampled prefix/parity checks were reported; they do not establish fold-independent estimation.

**Evaluation scope:** Grouped CV-A: F4/F2 screen, followed by a frozen F1/F3/F0 check. No reduced, package, or cloud evaluation.

**Validation labels:** VALID_EXACT_STREAM; POST_SELECTION_CV

**Result and disposition:** Adaptive Online Kernel Forgetting — Stage 1 Status: completed feasibility screen; tested configurations not promoted.

**Limit / reason deprioritized:** The selected-fold lift did not replicate on F0/F1/F3 and was within the expected scale of CV-A selection. This rejects the tested scalar RFF configuration, not adaptive kernels generally.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `GROUPED_CV_A_SCREEN_OR_REPLAY`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-025</code> · <code>MTH-025</code> · Conditional Relative-Pearson Transition Evidence — Stage 0</summary>

**Record type:** detector or evidence method.

**Reported family label:** Conditional Rulsif.

**Question or hypothesis:** After historical AR/Rosenblatt whitening, the causal transition law P(z_t | context(z_(t-1))) may change while a marginal rank detector remains weak. This experiment estimated a bounded relative density ratio between historical and recent conditional response distributions within history-defined lag-context bins.

**Implementation:** Use `z_t` from the exact BIC-AR residual → pre-update EWMA scale → historical-ECDF normal-score stream. Transform history through the same history-fitted ECDF and verify online scores against cached `rw_z`. - Define `X_t=z_(t-1)` and `Y_t=z_t`. Fit lag-context cutpoints and historical conditional response moments from history only.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Conditional Relative-Pearson Transition Evidence — Stage 0

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** prefix_or_future_mutation_audit_reported

**Evaluation scope:** synthetic_screen

**Validation labels:** UNKNOWN_FROM_PUBLIC_INDEX

**Result and disposition:** Conditional Relative-Pearson Transition Evidence — Stage 0 Status: Stage-1 F4/F2 feasibility screen is positive but small; two 2-bin settings are frozen for F1/F3 confirmation.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `SYNTHETIC_ONLY_SCREEN`.

**Final status:** `HISTORICAL_RESULT_RECORDED_STATUS_UNSPECIFIED`.
</details>

<details>
<summary><code>CAT-030</code> · <code>MTH-030</code> · History-Seeded CRM + Conditional RuLSIF Fusion</summary>

**Record type:** combination or scoring head.

**Reported family label:** Crm Rulsif Fusion.

**Question or hypothesis:** History-seeded conformal restart martingale (CRM) summarizes insertion-rank evidence from standardized innovations. Conditional RuLSIF summarizes changes in the response distribution conditional on a lag-context bin. Because these are different estimators, a LightGBM head with both feature blocks might improve on either alone. This is a feature-only ablation; no base-model prediction is an input.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Not preserved in the public summary.

**Tested settings or stage:** History-Seeded CRM + Conditional RuLSIF Fusion

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** grouped_cv_a_full_or_replay

**Validation labels:** UNKNOWN_FROM_PUBLIC_INDEX

**Result and disposition:** Status: Full five-fold grouped CV-A and one frozen reduced diagnostic complete; not promoted.

**Limit / reason deprioritized:** No further reason for deprioritization is preserved in the public summary.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `GROUPED_CV_A_FULL_OR_REPLAY`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-033</code> · <code>MTH-033</code> · Dependence-Aware Two-Sample U-Statistic — Research Record</summary>

**Record type:** detector or evidence method.

**Reported family label:** Dependence U Statistic.

**Question or hypothesis:** After the history-fitted Rosenblatt transform, changes in dependence can remain even when the marginal innovation stream is close to standard normal. A history-versus-current-window unbiased two-sample U-statistic on scalar and lag-1 delay states may encode changes that a one-sample MMD-to-Gaussian score or scalar mean/scale feature misses.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Not preserved in the public summary.

**Tested settings or stage:** Dependence-Aware Two-Sample U-Statistic — Research Record

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** synthetic_screen

**Validation labels:** UNKNOWN_FROM_PUBLIC_INDEX

**Result and disposition:** Status: Stage 0 implementation and synthetic feasibility pending.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `SYNTHETIC_ONLY_SCREEN`.

**Final status:** `HISTORICAL_RESULT_RECORDED_STATUS_UNSPECIFIED`.
</details>

<details>
<summary><code>CAT-045</code> · <code>MTH-045</code> · History-Anchored Full-Scan RFF U-Statistic</summary>

**Record type:** detector or evidence method.

**Reported family label:** History Full Scan U.

**Question or hypothesis:** Use a finite-RFF unbiased two-sample MMD U-statistic to compare the causal history-plus-observed-prefix sample against geometrically spaced current online suffixes. The hypothesis was that an expanding reference anchor, quadratic distributional evidence, and diagonal correction might capture breaks not represented by a static-history first-order RFF monitor.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** History-Anchored Full-Scan RFF U-Statistic

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** Synthetic Stage 0 plus a CV-A F4/F1 screen; settings were selected on the screened folds. No full-fold confirmation is reported.

**Validation labels:** PARTIAL_FOLD; POST_SELECTION_CV; CLOUD_PRIVATE

**Result and disposition:** The adjusted-range full-scan variant was closed after its null-calibration checks failed; not promoted.

**Limit / reason deprioritized:** No further reason for deprioritization is preserved in the public summary.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `PARTIAL_GROUPED_CV_A`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-060</code> · <code>MTH-060</code> · History-Fitted Nonlinear RFF Dynamics Residuals — Search Report</summary>

**Record type:** detector or evidence method.

**Reported family label:** Nonlinear Rff Dynamics.

**Question or hypothesis:** After history-fitted AR/Rosenblatt whitening, the conditional transition law may change while the one-dimensional marginal remains similar. The experiment tested whether a compact nonlinear map from recent whitened lags to the next innovation could yield prediction-residual evidence beyond linear delay-DMD.

**Implementation:** Map fixed lag states into Gaussian random Fourier features, fit a ridge predictor using only an early historical segment, calibrate residuals on a separate historical tail, then refit on history. Online scores use causal standardized prediction residuals; no future data or final stream length is used.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** History-Fitted Nonlinear RFF Dynamics Residuals — Search Report

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** feasibility_or_planned

**Validation labels:** UNKNOWN_FROM_PUBLIC_INDEX

**Result and disposition:** The history-fitted nonlinear RFF residuals were weak and nearly collinear with existing evidence; the configuration was not promoted.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `FEASIBILITY_OR_PLANNED`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-063</code> · <code>MTH-063</code> · Object-Valued Self-Normalized RFF Monitor — 2026-09-26</summary>

**Record type:** detector or evidence method.

**Reported family label:** Object Monitor Rff.

**Question or hypothesis:** Not preserved in the public summary; see the report title and source digest.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Not preserved in the public summary.

**Tested settings or stage:** Object-Valued Self-Normalized RFF Monitor — 2026-09-26

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** grouped_cv_a_partial

**Validation labels:** PARTIAL_FOLD_WHERE_APPLICABLE

**Result and disposition:** The object-valued self-normalized RFF monitor remained an auxiliary, unpromoted experiment.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `PARTIAL_GROUPED_CV_A`.

**Final status:** `HISTORICAL_RESULT_RECORDED_STATUS_UNSPECIFIED`.
</details>

<details>
<summary><code>CAT-066</code> · <code>MTH-066</code> · Online Nonlinear RFF Dynamics Drift — Search Report</summary>

**Record type:** detector or evidence method.

**Reported family label:** Online Rff Dynamics Drift.

**Question or hypothesis:** The earlier history-fitted RFF transition model kept its dynamics coefficients static. This experiment tests whether a causal, prequential RLS update can expose a change in the conditional transition law through predictive-score gain and parameter drift. It is distinct from D3's RFF-MMD statistic: RFFs here map lag states into a nonlinear transition-regression basis.

**Implementation:** For each ID, build lag states from the existing causal Rosenblatt-whitened stream, center/scale with historical states, and map to eight fixed RFFs. - Fit a ridge transition map on historical observations. During online scoring, compute frozen-reference and adaptive residuals before updating the current RLS state; then update RLS and emit a history-information-normalized coefficient-drift feature. - Emit four features per forgetting factor: frozen-vs-adaptive squared-error gain, its span-32 EMA, coefficient drift, and adaptive residual log-square.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Online Nonlinear RFF Dynamics Drift — Search Report

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** Stage 1 screened F4/F2, followed by frozen transfer-fold checks and a stitched five-fold descriptive blend. The report notes that the downstream Trial-11 baseline has a separate nested-OOF contamination issue.

**Validation labels:** VALID_EXACT_STREAM; POST_SELECTION_CV; CLOUD_PRIVATE

**Result and disposition:** Status: Stage-1 screen plus frozen transfer folds complete; not promoted.

**Limit / reason deprioritized:** No further reason for deprioritization is preserved in the public summary.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `GROUPED_CV_A_FULL_OR_REPLAY`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-074</code> · <code>MTH-074</code> · P5 Kernel CUSUM Search Report</summary>

**Record type:** detector or evidence method.

**Reported family label:** P5 Kernel Cusum.

**Question or hypothesis:** Not preserved in the public summary; see the report title and source digest.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Not preserved in the public summary.

**Tested settings or stage:** P5 Kernel CUSUM Search Report

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** CV-A F4/F0 screen only; the candidate was not promoted to full CV-A or deployment evaluation.

**Validation labels:** PARTIAL_FOLD; POST_SELECTION_CV; CLOUD_PRIVATE

**Result and disposition:** The screened history-seeded kernel-CUSUM variants were weak and were not promoted.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `PARTIAL_GROUPED_CV_A`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-075</code> · <code>MTH-075</code> · P6 Causal Density-Ratio Search Report</summary>

**Record type:** detector or evidence method.

**Reported family label:** P6 Causal Density Ratio.

**Question or hypothesis:** Not preserved in the public summary; see the report title and source digest.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Not preserved in the public summary.

**Tested settings or stage:** P6 Causal Density-Ratio Search Report

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** grouped_cv_a_partial

**Validation labels:** PARTIAL_FOLD_WHERE_APPLICABLE

**Result and disposition:** Stage 1: Fold 4 and Fold 0; no test-reduced labels.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `PARTIAL_GROUPED_CV_A`.

**Final status:** `HISTORICAL_RESULT_RECORDED_STATUS_UNSPECIFIED`.
</details>

<details>
<summary><code>CAT-078</code> · <code>MTH-078</code> · P6 Causal Quantile-Displacement Search Report</summary>

**Record type:** detector or evidence method.

**Reported family label:** P6 Causal Qwd.

**Question or hypothesis:** Not preserved in the public summary; see the report title and source digest.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Not preserved in the public summary.

**Tested settings or stage:** P6 Causal Quantile-Displacement Search Report

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** grouped_cv_a_partial

**Validation labels:** PARTIAL_FOLD_WHERE_APPLICABLE

**Result and disposition:** Stage 1: Fold 4 and Fold 0 only, standard Trial-20 head; no test-reduced labels.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `PARTIAL_GROUPED_CV_A`.

**Final status:** `HISTORICAL_RESULT_RECORDED_STATUS_UNSPECIFIED`.
</details>

<details>
<summary><code>CAT-092</code> · <code>MTH-092</code> · History-Calibrated Gaussian MMD / Shiryaev–Roberts Screen</summary>

**Record type:** detector or evidence method.

**Reported family label:** Probability Flow Mmd Sr.

**Question or hypothesis:** Kraevskiy & Prokhorov, “Change Detection in Probability Flow ODE: Online Testing in Diffusion Latent Spaces,” arXiv:2608.22807 (2026-08-24), map pre-change observations to a Gaussian latent reference, evaluate RBF MMD, then accumulate a likelihood-ratio mixture with a Shiryaev–Roberts recursion.

**Implementation:** On a history-fitted Rosenblatt/normal-score stream, compute one-sample RBF-MMD against a standard-normal reference on non-overlapping online blocks. Historical blocks calibrate score location/scale and exponential-tilt alternatives; a likelihood mixture updates a Shiryaev–Roberts statistic after each complete block. MMD-only and SR-only ablations were also tested.

**Reference / online information:** The reference distribution and empirical calibration come from historical blocks only. Online evidence updates only when a block is complete; partial future blocks are not used. Fitted Rosenblatt scores are not proven IID.

**Tested settings or stage:** Stage 1 feature-head CV-A screen on F4/F1; targeted Stage 2 ablated MMD-only and SR-only components with the same evaluator. Fold choice was pre-specified; these were two-fold screens, not full-CV estimates.

**Matched control:** The same frozen 54-feature P2+auxiliary+CRM head was evaluated without the candidate block, then with MMD-only and SR-only ablations. These controls isolate components but do not provide a clean independent benchmark.

**Causal evidence:** Six unit tests covered finite-sample MMD behavior, calibration, prefix causality, whitening shape/finiteness, and insufficient history. The tests support implementation behavior but not a sequential-validity guarantee.

**Evaluation scope:** Two-fold grouped CV-A feature-head diagnostics plus a targeted component ablation; no full CV-A, reduced evaluation, CV-B, private run, or deployment package.

**Validation labels:** VALID_EXACT_STREAM; PARTIAL_FOLD; POST_SELECTION_CV; CLOUD_PRIVATE

**Result and disposition:** The SR-only component retained most of one fold’s movement but lost signal on the other; the tested variants were not promoted. This is an empirical adaptation of the evidence accumulator, not the cited probability-flow ODE method.

**Limit / reason deprioritized:** The two-fold results are selection-sensitive, empirical calibration may be noisy, and neither IID normal scores nor formal false-alarm or restart guarantees were established.

**Open question:** Would blockwise MMD/SR evidence add value under nested grouped evaluation with an independent calibration and false-alarm study?



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `PARTIAL_GROUPED_CV_A`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-097</code> · <code>MTH-097</code> · Search Report: Direct Density-Ratio Evidence on Whitened States</summary>

**Record type:** detector or evidence method.

**Reported family label:** Rosenblatt Density Ratio.

**Question or hypothesis:** A classifier or density-ratio witness that distinguishes historical whitened states from a recent online window may expose changes that are not represented by the existing supervised components. The first implementation tests a cheap, causal linear witness before attempting per-window logistic or neural witnesses.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Search Report: Direct Density-Ratio Evidence on Whitened States

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** causal_design_or_exact_stream_reported; audit_scope_varies

**Evaluation scope:** A candidate was selected using frozen OOF labels from F4/F0, then evaluated on all five frozen CV-A folds. No reduced-data result is reported.

**Validation labels:** POST_SELECTION_CV; CLOUD_PRIVATE

**Result and disposition:** The causal direct-density-ratio feature did not add useful complementary evidence to the tested reference and was not promoted.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `GROUPED_CV_A_FULL_OR_REPLAY`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-103</code> · <code>MTH-103</code> · Search Report: Whitened-State RFF / Multi-Kernel MMD</summary>

**Record type:** detector or evidence method.

**Reported family label:** Rosenblatt Rff.

**Question or hypothesis:** RFF discrepancies on a fully whitened innovation stream may capture nonlinear distribution changes that moment and tau evidence miss. The search explicitly compared scalar `rw_z` with a state representation containing `z`, `Δz`, `|z|`, `z²`, lag-1 and lag-4 products, and sign.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Search Report: Whitened-State RFF / Multi-Kernel MMD

**Matched control:** The public summary does not retain a report-specific matched-control result. Family-level comparison principles and examples are documented in docs/failed_experiments.md.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** F4/F0 screen followed by a frozen five-fold CV-A evaluation. No reduced-data result is reported.

**Validation labels:** POST_SELECTION_CV; CLOUD_PRIVATE

**Result and disposition:** The full grouped-CV variant was not promoted; its replay did not establish an independent result or justify reduced evaluation.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `GROUPED_CV_A_FULL_OR_REPLAY`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-118</code> · <code>MTH-118</code> · Finite-Basis Stein-Score Evidence — 2026-09-25</summary>

**Record type:** detector or evidence method.

**Reported family label:** Stein Score Evidence.

**Question or hypothesis:** A finite-basis Stein operator for a standard-normal reference may produce causal evidence when the normalized innovation stream departs from its historical regime. The experiment used inverse-multiquadric basis functions and a rolling-window score; theoretical validity depends on the stated reference and boundary assumptions.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Finite-Basis Stein-Score Evidence — 2026-09-25

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** Feature groups and blend were evaluated across five CV-A folds; one frozen reduced diagnostic regressed and the candidate was not promoted.

**Validation labels:** POST_SELECTION_CV; CLOUD_PRIVATE

**Result and disposition:** The finite-basis rolling Stein-score recipe was not promoted after a negative selected CV-A screen; no e-process guarantee is claimed.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `GROUPED_CV_A_FULL_OR_REPLAY`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-119</code> · <code>MTH-119</code> · Stein Score Mixture over Candidate Change Times — 2026-09-25</summary>

**Record type:** detector or evidence method.

**Reported family label:** Stein Tau Mixture.

**Question or hypothesis:** The preceding finite-basis experiment mixed bounded Stein score functions but did not integrate over candidate change times. This follow-up uses each fixed center/sign expert as a bounded betting payoff on the causal Rosenblatt stream `rw_z`, then mixes over possible start times `tau` using a proper prior. For expert payoff `u_t` and fixed bet `lambda=.25`, the factor is `q_t=1+lambda*u_t`.

**Implementation:** The preceding finite-basis experiment mixed bounded Stein score functions but did not integrate over candidate change times. This follow-up uses each fixed center/sign expert as a bounded betting payoff on the causal Rosenblatt stream `rw_z`, then mixes over possible start times `tau` using a proper prior. For expert payoff `u_t` and fixed bet `lambda=.25`, the factor is `q_t=1+lambda*u_t`. The active wealth recurrence is `A_t=q_t(A_(t-1)+w_t)`; the prior mass for starts after `t` is added as the unstarted tail, and evidence is averaged over seven centers and both signs.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Stein Score Mixture over Candidate Change Times — 2026-09-25

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** prefix_or_future_mutation_audit_reported

**Evaluation scope:** Staged CV-A evaluation covered all five folds; one frozen reduced diagnostic was negative and the candidate was not promoted.

**Validation labels:** POST_SELECTION_CV; CLOUD_PRIVATE

**Result and disposition:** Decision: Do not promote this feature-head experiment.

**Limit / reason deprioritized:** No further reason for deprioritization is preserved in the public summary.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `GROUPED_CV_A_FULL_OR_REPLAY`.

**Final status:** `HISTORICAL_RESULT_RECORDED_STATUS_UNSPECIFIED`.
</details>

### Learned representations and neural methods

<details>
<summary><code>CAT-042</code> · <code>MTH-042</code> · Feature-to-TabPFN: Exact-Stream Feasibility Audit</summary>

**Record type:** representation or model.

**Reported family label:** Feature To Tabpfn Feasibility.

**Question or hypothesis:** A tabular foundation model might combine compact evidence from distinct causal families more effectively than the current LightGBM heads. The tested question here is narrower: can TS2TabPFN or stock TabPFN be used as a per-time-step predictor under this challenge's strict value-by-value inference contract?

**Implementation:** The packaged `infer()` is a generator over `(historical, online)` streams. For each online value it updates state and yields that step's score immediately; it does not receive an entire query matrix in advance. The training corpus has about 5,036,517 online rows across 10,000 IDs. The causal adaptation would need to map a compact evidence vector available at age `t` to a score using only fold-excluded training examples, and it must emit the score for `t` without using any later online row.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Feature-to-TabPFN: Exact-Stream Feasibility Audit

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** exact_stream_or_package_replay_scope_unspecified

**Validation labels:** UNKNOWN_FROM_PUBLIC_INDEX

**Result and disposition:** The TabPFN branch stopped at literature/runtime feasibility; no direct score search or package integration was run.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `EXACT_STREAM_SCOPE_UNSPECIFIED`.

**Final status:** `HISTORICAL_RESULT_RECORDED_STATUS_UNSPECIFIED`.
</details>

<details>
<summary><code>CAT-054</code> · <code>MTH-054;MTH-055</code> · Neural DSM CUSUM Allowance — Synthetic Stage 0; Neural DSM CUSUM Allowance — F4/F1 Feasibility Screen</summary>

**Record type:** detector or evidence method.

**Reported family label:** Neural Dsm Allowance Stage0.

**Question or hypothesis:** Not preserved in the public summary; see the report title and source digest.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Not preserved in the public summary.

**Tested settings or stage:** Neural DSM CUSUM Allowance — Synthetic Stage 0; Neural DSM CUSUM Allowance — F4/F1 Feasibility Screen

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** synthetic_screen

**Validation labels:** PARTIAL_FOLD_WHERE_APPLICABLE

**Result and disposition:** A synthetic gate passed, but the fixed score correction remained a limited exploratory screen and was not promoted.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `SYNTHETIC_ONLY_SCREEN`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-056</code> · <code>MTH-056;MTH-059</code> · Neural Denoising Score-Matching CUSUM — Synthetic Stage-0; Neural DSM on Actual Rosenblatt Streams — Stage1</summary>

**Record type:** detector or evidence method.

**Reported family label:** Neural Dsm Stage0.

**Question or hypothesis:** The finite Gaussian-KDE score estimator tested in an earlier exploratory branch was closed before Stage 2. This experiment tests a distinct neural denoising score-matching estimator, not another KDE bandwidth setting. The primary reference is Zhou et al. (2025), [“Sequential Change Point Detection via Denoising Score Matching”](https://arxiv.org/abs/2501.12667).

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Not preserved in the public summary.

**Tested settings or stage:** Neural Denoising Score-Matching CUSUM — Synthetic Stage-0; Neural DSM on Actual Rosenblatt Streams — Stage1

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** synthetic_screen

**Validation labels:** UNKNOWN_FROM_PUBLIC_INDEX

**Result and disposition:** Synthetic and actual-stream feasibility screens were completed; the tested neural denoising score-matching CUSUM was not promoted. This configuration-level result does not rule out other score models.

**Limit / reason deprioritized:** No further reason for deprioritization is preserved in the public summary.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `SYNTHETIC_ONLY_SCREEN`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-057</code> · <code>MTH-057</code> · Neural DSM Stage-0b — Fresh-Seed Rank-Blend Diagnostic</summary>

**Record type:** representation or model.

**Reported family label:** Neural Dsm Stage0B.

**Question or hypothesis:** Not preserved in the public summary; see the report title and source digest.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Neural DSM Stage-0b — Fresh-Seed Rank-Blend Diagnostic

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** synthetic_screen

**Validation labels:** UNKNOWN_FROM_PUBLIC_INDEX

**Result and disposition:** The frozen fresh-seed synthetic criterion passed, but the tested rank blend did not establish a transferable public detector; not promoted.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `SYNTHETIC_ONLY_SCREEN`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-058</code> · <code>MTH-058</code> · Neural DSM Stage-0c — Per-Stream Historical-Z Blend</summary>

**Record type:** representation or model.

**Reported family label:** Neural Dsm Stage0C.

**Question or hypothesis:** Not preserved in the public summary; see the report title and source digest.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Neural DSM Stage-0c — Per-Stream Historical-Z Blend

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** synthetic_screen

**Validation labels:** UNKNOWN_FROM_PUBLIC_INDEX

**Result and disposition:** A narrow synthetic dependence screen passed; the per-stream blend remained exploratory and was not promoted.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `SYNTHETIC_ONLY_SCREEN`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-065</code> · <code>MTH-065</code> · One-Change Hazard and Monotone-GRU Evidence</summary>

**Record type:** representation or model.

**Reported family label:** One Change Hazard.

**Question or hypothesis:** Not preserved in the public summary; see the report title and source digest.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** One-Change Hazard and Monotone-GRU Evidence

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** Full grouped CV-A stepwise replay plus one frozen reduced diagnostic; the candidate was not promoted.

**Validation labels:** POST_SELECTION_CV; CLOUD_PRIVATE

**Result and disposition:** Status: full grouped CV-A stepwise replay and one frozen reduced diagnostic complete; not promoted.

**Limit / reason deprioritized:** No further reason for deprioritization is preserved in the public summary.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `GROUPED_CV_A_FULL_OR_REPLAY`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-088</code> · <code>MTH-088</code> · Probabilistic Predictive Coding — Stage 1 Feasibility Screen</summary>

**Record type:** representation or model.

**Reported family label:** Ppc Predictive Coding.

**Question or hypothesis:** Not preserved in the public summary; see the report title and source digest.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Not preserved in the public summary.

**Tested settings or stage:** Probabilistic Predictive Coding — Stage 1 Feasibility Screen

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** feasibility_or_planned

**Validation labels:** UNKNOWN_FROM_PUBLIC_INDEX

**Result and disposition:** Probabilistic Predictive Coding — Stage 1 Feasibility Screen Decision: Do not promote this implementation. The CV-A scores are near chance, fixed blends do not improve, and sampled single-stream numerical parity failed.

**Limit / reason deprioritized:** No further reason for deprioritization is preserved in the public summary.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `FEASIBILITY_OR_PLANNED`.

**Final status:** `HISTORICAL_RESULT_RECORDED_STATUS_UNSPECIFIED`.
</details>

<details>
<summary><code>SUP-002</code> · <code>SRC-016</code> · Contrastive current-versus-reference window-gap features</summary>

**Record type:** representation or model.

**Reported family label:** Contrastive adjacent-window features.

**Question or hypothesis:** Contrastive representations of recent and reference windows may capture distributional differences beyond the baseline summary.

**Implementation:** A compact head used signed and unsigned gaps in mean, variance, energy, and sign rate; result record reports grouped five-fold OOF metrics.

**Reference / online information:** The result record does not independently establish prefix-only implementation semantics.

**Tested settings or stage:** One fixed feature set and compact head; tested blends against the same-fold baseline.

**Matched control:** Same-fold fixed baseline in the result record.

**Causal evidence:** not independently established from the result record

**Evaluation scope:** grouped_cv_a_full_oof_result_record

**Validation labels:** POST_SELECTION_CV; CAUSALITY_AUDIT_UNKNOWN

**Result and disposition:** The expert and tested positive blend weights were below the matched baseline mean; not promoted.

**Limit / reason deprioritized:** The tested contrastive features did not improve the baseline in grouped CV-A; no independent causal audit is present.

**Open question:** Would a nested, prefix-audited contrastive representation add value under a matched training budget?



**Implementation status:** `SUPPLEMENTAL_SUMMARY_ONLY_NOT_SHIPPED`.

**Validation stage:** `GROUPED_CV_A_FULL_OR_REPLAY`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>SUP-003</code> · <code>SRC-017</code> · Siamese convolutional comparison of current and historical windows</summary>

**Record type:** representation or model.

**Reported family label:** Causal Siamese CNN.

**Question or hypothesis:** A shared temporal encoder may expose local representation shifts between a reference window and current observations.

**Implementation:** A single-fold feasibility record reports a short, low-epoch CNN screen and blend diagnostics.

**Reference / online information:** The artifact is a single-fold score record; exact streaming parity was not established here.

**Tested settings or stage:** One window setting, two training epochs, one held fold.

**Matched control:** Trial-13 baseline on the same fold (F4) is reported as a comparator in the research summary.

**Causal evidence:** not independently established from the result record

**Evaluation scope:** one_fold_feasibility_screen

**Validation labels:** PARTIAL_FOLD; POST_SELECTION_CV; CAUSALITY_AUDIT_UNKNOWN

**Result and disposition:** The one-fold CNN score was near chance and tested blends were below the same-fold baseline; not promoted.

**Limit / reason deprioritized:** Single-fold evidence cannot support a transfer claim; no complete stream-parity audit accompanies the result record.

**Open question:** Does a strictly causal, nested Siamese model help on more than one held-out group?



**Implementation status:** `SUPPLEMENTAL_SUMMARY_ONLY_NOT_SHIPPED`.

**Validation stage:** `PARTIAL_GROUPED_CV_A`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>SUP-005</code> · <code>SRC-019;SRC-020</code> · Dual-reference contrastive encoder using raw and Rosenblatt-normalized windows</summary>

**Record type:** representation or model.

**Reported family label:** Dual-reference TNC encoder.

**Question or hypothesis:** Combining raw-series and normalized-innovation reference comparisons may provide complementary representations.

**Implementation:** Window-16 temporal-neighborhood encoder with two reference views and an auxiliary scoring head.

**Reference / online information:** Metadata describe training and feature extraction; the two-fold result is a partial screen and does not establish complete online inference parity.

**Tested settings or stage:** One width-16 training configuration; head evaluated on F4 and F0.

**Matched control:** Trial-13 baseline on the same two folds.

**Causal evidence:** not independently established from the two-fold result record

**Evaluation scope:** grouped_cv_a_partial_f4_f0

**Validation labels:** PARTIAL_FOLD; POST_SELECTION_CV; CAUSALITY_AUDIT_UNKNOWN

**Result and disposition:** The auxiliary head was below the Trial-13 baseline on both screened folds; no blend improvement was demonstrated.

**Limit / reason deprioritized:** Two folds do not establish generalization, and the feature path lacks an independent causal audit in the public record.

**Open question:** Would dual-view embeddings add value under nested representation fitting and full prefix parity?



**Implementation status:** `SUPPLEMENTAL_SUMMARY_ONLY_NOT_SHIPPED`.

**Validation stage:** `PARTIAL_GROUPED_CV_A`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

### Other causal evidence methods

<details>
<summary><code>CAT-015</code> · <code>MTH-015</code> · Causal P2 Multiscale Evidence Fusion — Search Report</summary>

**Record type:** combination or scoring head.

**Reported family label:** Causal Evidence Fusion.

**Question or hypothesis:** P2's AR-whitened, tau-integrated Rosenblatt evidence may become more useful when its historical null calibration adapts causally to observed stream age and is combined with orthogonal dynamics, martingale, and spectral evidence. This is a synthesis experiment using already-reviewed method families, not a claim of new theoretical guarantees.

**Implementation:** The 48-input head combines 15 raw P2/Rosenblatt features, 10 history-null robust-z features, 22 dynamics features, and stream age. A matched ablation also evaluated the 47-input version without age.

**Reference / online information:** Features use a history-initialized conditional-normalization stream and online values through the current prefix. All 48 components passed a component-level prefix audit; integrated candidate inference parity remains unverified.

**Tested settings or stage:** Causal P2 Multiscale Evidence Fusion — Search Report

**Matched control:** Clean Baseline V2 direct head on the same grouped CV-A folds; its reduced-only score is retained as a separate one-time control.

**Causal evidence:** All feature components passed a full component-level prefix-parity audit. This does not establish parity of the integrated 47/48-input inference package.

**Evaluation scope:** Five-fold grouped CV-A matched-capacity ablation; Arm C had one reduced-only diagnostic, and Arm D had retrospective paired-ID resampling. No package or official private evaluation.

**Validation labels:** CLOUD_PRIVATE; POST_SELECTION_CV; FEATURE_COMPONENT_PARITY_ONLY; PACKAGE_PARITY_UNKNOWN; REDUCED_ONLY (Arm C only)

**Result and disposition:** Arm C (47 inputs) averaged 0.610056 CV-A versus 0.5992524 for the matched control, but scored 0.5135546 on the one reduced-only diagnostic versus 0.520526 for the control. Arm D (48 inputs) averaged 0.6104292; its paired-ID bootstrap mean delta was +0.0113107 with descriptive interval +0.0073494 to +0.0155046. Neither head was promoted.

**Limit / reason deprioritized:** CV-A and feature development were repeatedly exposed. Bootstrap uncertainty is conditional on saved predictions. Integrated inference/package parity is open, and the no-age Arm C fell below its control on the reduced diagnostic.

**Open question:** Would the CV-A lift persist with complete integrated-prefix parity and an independent nested or sealed evaluation?


**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `GROUPED_CV_A_FULL_OR_REPLAY`.

**Final status:** `HISTORICAL_RESULT_RECORDED_STATUS_UNSPECIFIED`.
</details>

<details>
<summary><code>CAT-018</code> · <code>MTH-018</code> · CHASM-Inspired History-Calibrated MEWMA — Stage 0/1</summary>

**Record type:** detector or evidence method.

**Reported family label:** Chasm Mewma.

**Question or hypothesis:** The prior p=2 CHASM screen monitored raw spectral displacement and velocity norms but omitted the paper's central complex MEWMA/Mahalanobis normalization. History-calibrated covariance may distinguish coherent spectral motion from ordinary estimator noise, especially when the direction of eigenvalue motion matters more than its raw magnitude. A one-step-lag online covariance variant may adapt to heteroscedastic velocity while retaining a causal score.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** CHASM-Inspired History-Calibrated MEWMA — Stage 0/1

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** causal_design_or_exact_stream_reported; audit_scope_varies

**Evaluation scope:** exact_stream_or_package_replay_scope_unspecified

**Validation labels:** UNKNOWN_FROM_PUBLIC_INDEX

**Result and disposition:** CHASM-Inspired History-Calibrated MEWMA — Stage 0/1 Status: Stage 0, the frozen F4/F0 Stage-1 screen, and the predeclared Stage-2 cumulative-maximum screen are complete. No CV-B or test-reduced labels have been accessed for this candidate.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `EXACT_STREAM_SCOPE_UNSPECIFIED`.

**Final status:** `HISTORICAL_RESULT_RECORDED_STATUS_UNSPECIFIED`.
</details>

<details>
<summary><code>CAT-029</code> · <code>MTH-029</code> · State-Conditioned Online Quantile Calibration (CPTC-Inspired)</summary>

**Record type:** detector or evidence method.

**Reported family label:** Cptc State Calibration.

**Question or hypothesis:** The current exact package ranks with a causal whitened detector. A separate state-conditioned calibration path may expose whether its standardized innovation is surprising under the currently predicted stable/recent-change state. This tests calibration-state interactions, not another raw rolling statistic. The initial state predictor is a *pre-observation* Bayesian AR run-length posterior; a separate global quantile calibrator is the control.

**Implementation:** Fit the historical AR/Rosenblatt reference from each ID's historical rows only; use the exact cached `rw_z` stream used by the D2+D3 package. - Initialize the q=1, hazard-1/128 run-length model as an established historical regime with a capped long-run state. Before processing each online value, predict the probability that its current run length is at most eight. This is the stable/recent state mass used to route calibration. - Seed both calibration states with the same historical 90th-percentile absolute innovation.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** State-Conditioned Online Quantile Calibration (CPTC-Inspired)

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** exact_stream_or_package_replay_scope_unspecified

**Validation labels:** UNKNOWN_FROM_PUBLIC_INDEX

**Result and disposition:** Status: Stage 3 completed for one frozen joint-head blend; not promoted.

**Limit / reason deprioritized:** No further reason for deprioritization is preserved in the public summary.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `EXACT_STREAM_SCOPE_UNSPECIFIED`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-040</code> · <code>MTH-040</code> · Feature-Based ICM with Ellipsoidal-kNN Delay-State Nonconformity</summary>

**Record type:** detector or evidence method.

**Reported family label:** Feature Icm Ellipsoid.

**Question or hypothesis:** Not preserved in the public summary; see the report title and source digest.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Feature-Based ICM with Ellipsoidal-kNN Delay-State Nonconformity

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** feasibility_or_planned

**Validation labels:** UNKNOWN_FROM_PUBLIC_INDEX

**Result and disposition:** Status: Stage 0 completed; primary synthetic gate passed. No challenge CV was run.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `FEASIBILITY_OR_PLANNED`.

**Final status:** `HISTORICAL_RESULT_RECORDED_STATUS_UNSPECIFIED`.
</details>

<details>
<summary><code>CAT-044</code> · <code>MTH-044</code> · Fixed-Share Predictive Expert Aggregation</summary>

**Record type:** detector or evidence method.

**Reported family label:** Fixed Share Forecast.

**Question or hypothesis:** Not preserved in the public summary; see the report title and source digest.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Fixed-Share Predictive Expert Aggregation

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** causal_design_or_exact_stream_reported; audit_scope_varies

**Evaluation scope:** grouped_cv_a_full_or_replay

**Validation labels:** PARTIAL_FOLD_WHERE_APPLICABLE

**Result and disposition:** The tested fixed-share predictive-expert recipe failed its synthetic prequential-loss gate and was closed.

**Limit / reason deprioritized:** No further reason for deprioritization is preserved in the public summary.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `PARTIAL_GROUPED_CV_A`.

**Final status:** `HISTORICAL_RESULT_RECORDED_STATUS_UNSPECIFIED`.
</details>

<details>
<summary><code>CAT-046</code> · <code>MTH-046</code> · Hölder-Weighted Max-Norm Evidence on Whitened Innovations</summary>

**Record type:** detector or evidence method.

**Reported family label:** Holder Multiscale.

**Question or hypothesis:** Not preserved in the public summary; see the report title and source digest.

**Implementation:** Inspired by Bastian et al. (2026), [*Change Point Detection and Localization in High-Dimensional Time Series*](https://arxiv.org/abs/2608.14344), which scans weighted historical/current contrasts over candidate suffix lengths. This adaptation applies a geometric suffix scan with a Hölder weight to causal Rosenblatt-normal-score channels, then emits one maximum score per stream position. Channels cover location, clipped nonlinear transforms, scale, empirical-tail indicators, and lag dependence. It is a ranking feature, not a calibrated test or a transfer of the paper's theoretical guarantees.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Hölder-Weighted Max-Norm Evidence on Whitened Innovations

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** Synthetic Stage 0 plus a grouped CV-A F4/F1 screen. No reduced or provider evaluation and no full-fold transfer result are reported.

**Validation labels:** PARTIAL_FOLD; POST_SELECTION_CV; CLOUD_PRIVATE

**Result and disposition:** Decision Do not promote the tested variants.

**Limit / reason deprioritized:** No further reason for deprioritization is preserved in the public summary.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `PARTIAL_GROUPED_CV_A`.

**Final status:** `HISTORICAL_RESULT_RECORDED_STATUS_UNSPECIFIED`.
</details>

<details>
<summary><code>CAT-051</code> · <code>MTH-051</code> · MPS-Style Causal Expert-Set Evidence</summary>

**Record type:** detector or evidence method.

**Reported family label:** Mps Expert Set.

**Question or hypothesis:** HYPOTHESIS: An online prediction set over history-fitted experts may surface changes in which forecasting dynamics are competitive, while its coverage state provides a common uncertainty scale across streams. PAPER: Li & Zheng, *Online Conformal Model Selection for Nonstationary Time Series*, arXiv:2506.05544v2 (2026-01-28), [primary source](https://arxiv.org/abs/2506.05544).

**Implementation:** Transform each ID with the history-only Rosenblatt stream, fit a small bank of AR predictors on an early historical segment, and estimate their variances on a separate historical tail. Score the tail and online prefix prequentially, then form one-sided confidence sets over cumulative expert losses. This is an experimental expert-set feature; conformal coverage is not claimed.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** MPS-Style Causal Expert-Set Evidence

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** synthetic_screen

**Validation labels:** UNKNOWN_FROM_PUBLIC_INDEX

**Result and disposition:** The corrected synthetic gate and one label-blind calibration screen were completed; no promotion or deployment result was established.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `SYNTHETIC_ONLY_SCREEN`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-067</code> · <code>MTH-067</code> · Online Segment Parameter Contrast — Search Report</summary>

**Record type:** detector or evidence method.

**Reported family label:** Online Segment Parameter Contrast.

**Question or hypothesis:** A causal contrast between adjacent observed windows may detect changes in conditional dynamics that marginal-only evidence misses. Zhang and Yao (2026), [“Structural Change Detection in Dynamic Systems”](https://arxiv.org/abs/2606.27614), inspired this segment-contrast idea; their retrospective ODE procedure and guarantees do not transfer to this adaptation. Scores use completed prefixes only.

**Implementation:** For AR lag orders `p=1,2` and windows `w={16,32,64,128}`, fit ridge-stabilized AR regressions on two adjacent windows of length `w`. Emit a history-scaled Wald contrast of the AR coefficients and a BIC-style gain from separate segments versus one pooled segment. Also emit per-step maxima across windows and causal cumulative maxima. Inputs were tested in two representations: history-calibrated whitened innovations and raw values standardized by a historical robust MAD. Each lag produced 24 features.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Online Segment Parameter Contrast — Search Report

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** grouped_cv_a_partial

**Validation labels:** UNKNOWN_FROM_PUBLIC_INDEX

**Result and disposition:** Status: Stage-1 F4/F2 screens complete; exact tested configurations stopped before Stage 2.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `PARTIAL_GROUPED_CV_A`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-072</code> · <code>MTH-072</code> · P2 Hierarchical Age-Conditioned Null</summary>

**Record type:** detector or evidence method.

**Reported family label:** P2 Hierarchical Null.

**Question or hypothesis:** Per-ID age-conditioned historical null profiles can be noisy. Shrink the per-ID median/MAD toward historical-only DGP-group and global profiles, while using only the current age bin at inference. Group labels are assigned once from historical descriptors using persistent, alternating, heavy-tail, extreme-tail, near-white, and ordinary regimes.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** P2 Hierarchical Age-Conditioned Null

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** Full CV-A screen followed by a one-time reduced-data diagnostic that informed selection; CV-B was not run. The reduced diagnostic is not a sealed holdout.

**Validation labels:** POST_SELECTION_CV; CLOUD_PRIVATE

**Result and disposition:** The age-conditioned follow-up did not improve overall transfer after fold-4/fold-0 tuning; no variant was promoted.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `GROUPED_CV_A_FULL_OR_REPLAY`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-082</code> · <code>MTH-082</code> · Simulation-Based Parameter Changepoint Evidence</summary>

**Record type:** detector or evidence method.

**Reported family label:** Param Cp Sbi.

**Question or hypothesis:** Can an amortized posterior over low-dimensional dynamical parameters turn a causal sliding window into a useful online break signal, and does integrating that evidence over candidate break times recover persistent changes?

**Implementation:** The Stage-0/1 simulator is the contractive univariate nonlinear AR model `x[t] = phi*x[t-1] + beta*tanh(1.5*x[t-1]) + sigma*epsilon[t]`. A five-component diagonal Gaussian-mixture NPE estimates `(phi,beta)` from per-window centered and standardized observations. `phi`, `beta`, and the noise scale are sampled from a restricted stable prior. For each challenge ID, history-only sliding windows estimate the reference posterior center and uncertainty; each online posterior uses a trailing window ending at the current observation.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Simulation-Based Parameter Changepoint Evidence

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** causal_design_or_exact_stream_reported; audit_scope_varies

**Evaluation scope:** exact_stream_or_package_replay_scope_unspecified

**Validation labels:** UNKNOWN_FROM_PUBLIC_INDEX

**Result and disposition:** The simulation-based parameter-inference representation showed a synthetic-to-challenge mismatch and was not promoted; this does not reject SBI generally.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `EXACT_STREAM_SCOPE_UNSPECIFIED`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-083</code> · <code>MTH-083</code> · PBML-LTI Fit–KL Prior: Historical Support/Query Stage 0</summary>

**Record type:** detector or evidence method.

**Reported family label:** Pbml Lti Fit Kl Prior.

**Question or hypothesis:** PAPER: Huang and Michailidis (2026), [“PAC-Bayesian Meta-Learning for Few-Shot Identification of Linear Dynamical Systems”](https://arxiv.org/abs/2609.24117), PBML-LTI (2026). The paper fits a Gaussian transition prior by minimizing posterior expected Gaussian fit plus posterior-to-prior KL, with hyper-prior and stability regularizers. Its [primary source](https://arxiv.org/abs/2609.24117) documents the paper's default training settings.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** PBML-LTI Fit–KL Prior: Historical Support/Query Stage 0

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** feasibility_or_planned

**Validation labels:** UNKNOWN_FROM_PUBLIC_INDEX

**Result and disposition:** PBML-LTI Fit–KL Prior: Historical Support/Query Stage 0 Decision: Stop this univariate AR(4) fit–KL adaptation before supervised CV-A.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `FEASIBILITY_OR_PLANNED`.

**Final status:** `HISTORICAL_RESULT_RECORDED_STATUS_UNSPECIFIED`.
</details>

<details>
<summary><code>CAT-086</code> · <code>MTH-086</code> · PFA-Weighted Restart Evidence — Search Report</summary>

**Record type:** detector or evidence method.

**Reported family label:** Pfa Weighted Restart.

**Question or hypothesis:** Integrating evidence over candidate change locations with a restart prior may preserve weak persistent evidence better than a single maximum scan or uniform mixture. Bhattacharyya and Ramdas (2026), [“Change Detection with Conformal Martingales: New Optimal Constructions, and Suboptimality of Existing Methods”](https://arxiv.org/abs/2609.27179), motivated this screen; its guarantees are not claimed for the tested adaptation.

**Implementation:** For each online standardized innovation, form insertion-rank evidence against a reference seeded by historical BIC-selected AR residuals. Mix restart-specific betting wealth over candidate starts using a summable restart prior and betting powers 0.25, 0.50, and 0.75; emit upper-, lower-, and absolute-tail channels for eta values 0.05, 0.10, and 0.20. The update is causal and does not use final stream length.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** PFA-Weighted Restart Evidence — Search Report

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** prefix_or_future_mutation_audit_reported

**Evaluation scope:** exact_stream_or_package_replay_scope_unspecified

**Validation labels:** UNKNOWN_FROM_PUBLIC_INDEX

**Result and disposition:** Status: staged CV-A diagnostic complete; not promoted.

**Limit / reason deprioritized:** No further reason for deprioritization is preserved in the public summary.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `EXACT_STREAM_SCOPE_UNSPECIFIED`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-093</code> · <code>MTH-093</code> · Restarted Threshold-Bet CDF Mixture</summary>

**Record type:** detector or evidence method.

**Reported family label:** Rcmm Threshold Bets.

**Question or hypothesis:** Existing conformal-restart work already covers candidate-start weighted sums and maxima, power-density betting, and directional/absolute rank channels. Those restart aggregators and priors are not new here. The orthogonal part is the betting function: an omnibus threshold-CDF family can target departures of the calibrated p-value distribution at different quantiles.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Not preserved in the public summary.

**Tested settings or stage:** Restarted Threshold-Bet CDF Mixture

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** synthetic_screen

**Validation labels:** PARTIAL_FOLD_WHERE_APPLICABLE

**Result and disposition:** The synthetic gate passed, but the preregistered F4/F1 screen was only exploratory and did not justify promotion.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `SYNTHETIC_ONLY_SCREEN`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-095</code> · <code>MTH-095</code> · Robust Summary NPE / RNPE-Inspired Change Evidence</summary>

**Record type:** detector or evidence method.

**Reported family label:** Robust Npe Summary Rnpe.

**Question or hypothesis:** Synthetic-to-challenge mismatch may make an amortized posterior drift over compact causal summaries more useful when (a) the simulator prior is locally preconditioned around observed histories and (b) posterior inference marginalizes summary misspecification instead of treating every summary as exact. This could add a low-correlation source of evidence to Trial52.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Robust Summary NPE / RNPE-Inspired Change Evidence

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** feasibility_or_planned

**Validation labels:** UNKNOWN_FROM_PUBLIC_INDEX

**Result and disposition:** Status: Original Stage 0–2 and the combined forest-preconditioned PRNPE-inspired Stage 0/1 are complete; no variant is promoted.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `FEASIBILITY_OR_PLANNED`.

**Final status:** `HISTORICAL_RESULT_RECORDED_STATUS_UNSPECIFIED`.
</details>

<details>
<summary><code>CAT-127</code> · <code>MTH-127</code> · VSBT-Inspired Prefix Tree — Synthetic Stage 0</summary>

**Record type:** detector or evidence method.

**Reported family label:** Vsbt Prefix Tree.

**Question or hypothesis:** Not preserved in the public summary; see the report title and source digest.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** VSBT-Inspired Prefix Tree — Synthetic Stage 0

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** synthetic_screen

**Validation labels:** UNKNOWN_FROM_PUBLIC_INDEX

**Result and disposition:** Synthetic feasibility only; the hard-split prefix-tree screen had poor calibration and no challenge-fold validation.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `SYNTHETIC_ONLY_SCREEN`.

**Final status:** `HISTORICAL_RESULT_RECORDED_STATUS_UNSPECIFIED`.
</details>

<details>
<summary><code>CAT-128</code> · <code>MTH-128</code> · Causal Prefix VSBT-Inspired Soft Gate</summary>

**Record type:** detector or evidence method.

**Reported family label:** Vsbt Soft Gate.

**Question or hypothesis:** A softly estimated temporal regime assignment, paired with separate autoregressive experts, may retain change evidence for dependence and tail breaks that is not well summarized by the current P2 mean/scale channels. The goal is complementary causal evidence, not a retrospective estimate of the final break point.

**Implementation:** A causal variational soft gate assigns observations between autoregressive experts using only the observed prefix. The screen varied outer variational iterations (1, 2, 3), with separate post-regime, split, and transition feature blocks.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Causal Prefix VSBT-Inspired Soft Gate

**Matched control:** The frozen baseline was replayed on the same grouped CV-A folds. Paired synthetic configurations varied only the outer variational iteration count (1, 2, or 3) on identical streams; the fold result is a two-fold transfer screen, not standard four-fold training.

**Causal evidence:** Online assignments use prefix observations only; exact-stream features were replayed on the screened folds.

**Evaluation scope:** Synthetic feasibility plus a two-fold grouped CV-A F4/F2 screen; each fold used only the other screened fold for training.

**Validation labels:** VALID_EXACT_STREAM; PARTIAL_FOLD; POST_SELECTION_CV

**Result and disposition:** The exact-stream CV-A screen showed a small exploratory lift, but the adaptation was not promoted.

**Limit / reason deprioritized:** The matched mean lift was small and exploratory; the feature/head adaptation was not promoted.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `SYNTHETIC_ONLY_SCREEN`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

### Path, geometry, and ordinal structure

<details>
<summary><code>CAT-005</code> · <code>MTH-005</code> · Whitened Delay-State Attractor Network — Search Report</summary>

**Record type:** detector or evidence method.

**Reported family label:** Attractor Network.

**Question or hypothesis:** Can a geometric model of the historical delay-state attractor produce conditional-dynamics evidence that adds information beyond the current Rosenblatt innovation, DMD, ordinal-transition, and rolling-statistic families? The main comparison is the feature-only head on grouped CV-A F4/F0; a fixed 0.10 blend with exact D2+D3 package OOF predictions is descriptive only.

**Implementation:** Apply the history-fitted BIC-AR/Rosenblatt transform, embed standardized scores in causal delay states (dimensions 2 or 3), and fit phase-state centers and transition counts from historical states only. Freeze those references online; emit nearest-center distance, smoothed transition surprisal, entropy-normalized surprisal, and a causal EWMA for each observed state.

**Reference / online information:** Reference: history-fitted AR residuals, empirical normal scores, conditional-scale state, and phase-state geometry. Online: assign delay states through the current observation to frozen historical centers and transition probabilities; future samples are not used.

**Tested settings or stage:** Stage 1 grouped CV-A F4/F0 feature-head screen; delay dimensions 2/3 and 8/16 state centers, four features per setting. The method stopped before full CV-A or reduced evaluation.

**Matched control:** The feature-only head was compared with the D2+D3 exact-package OOF replay; a fixed 0.10 blend was descriptive. No same-window low-order-moment ablation was preserved. The blended comparison inherits its upstream OOF and selection caveat.

**Causal evidence:** Three runtime tests passed, including exact-prefix equality after mutating an unseen suffix. A sampled value-by-value whitening replay matched the streaming reference. The evidence covers the feature path, not a promoted package.

**Evaluation scope:** Partial grouped CV-A F4/F0 screen with fold-excluded heads and label-blind feature construction; stopped before full CV-A, reduced evaluation, CV-B, private run, or deployment integration.

**Validation labels:** VALID_EXACT_STREAM; PARTIAL_FOLD; POST_SELECTION_CV; NON_NESTED_META_CV; CLOUD_PRIVATE

**Result and disposition:** Frozen feature-only heads were near chance on both screened folds; no tested blend had a positive two-fold mean change. The specific history-frozen K-means/transition-surprise variant was stopped before further evaluation.

**Limit / reason deprioritized:** Only two folds were inspected, and the blended comparator used OOF predictions with prior fold exposure. The result does not evaluate attractor networks or Markov methods as whole families.

**Open question:** Would a nested, predeclared evaluation against same-window moment and transition controls show incremental value from history-fitted state geometry?



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `PARTIAL_GROUPED_CV_A`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-016</code> · <code>MTH-016</code> · Causal Recurrence Geometry Search</summary>

**Record type:** detector or evidence method.

**Reported family label:** Causal Recurrence Geometry.

**Question or hypothesis:** Can short-window recurrence geometry of the exact history-initialized Rosenblatt innovation stream add useful evidence beyond the existing P2-style summary head, particularly for nonlinear dependence/volatility changes?

**Implementation:** Iwayama et al. (2013) reconstructs dynamical states with delay coordinates, forms a recurrence network from a distance threshold, and uses global community/spectral structure to identify regime changes. Walker, Zaitouny, and Correa (2021) uses recurrence-network modularity to score candidate temporal splits. These are global/offline procedures and their original assumptions and guarantees do not transfer to this per-timestep TS-AUC task. The experiment instead embeds each whitened innovation as `(rw_z[t], rw_z[t-1], rw_z[t-2])`.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Causal Recurrence Geometry Search

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** Synthetic Stage 0, grouped CV-A screening on F4/F1, frozen checks on F0/F2/F3, and one reduced diagnostic. Exact-prefix and future-suffix checks were reported on nine sampled IDs.

**Validation labels:** VALID_EXACT_STREAM; POST_SELECTION_CV; CLOUD_PRIVATE

**Result and disposition:** The synthetic gain did not transfer to a meaningful CV-A improvement; the tested configuration was not advanced.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `GROUPED_CV_A_FULL_OR_REPLAY`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-048</code> · <code>MTH-048</code> · Time-Augmented Hoff Lead–Lag Signatures</summary>

**Record type:** detector or evidence method.

**Reported family label:** Lead Lag Signatures.

**Question or hypothesis:** The earlier `(time, rw_z)` signature screens did not represent the Hoff lead–lag lift. In one dimension, the antisymmetric second-level signature of the lead–lag path recovers realized quadratic variation. A time-augmented lead–lag signature can additionally encode when variation accrued within a trailing window and how that variation interacts with the path.

**Implementation:** Compute time-augmented lead–lag signatures from the causal increment stream over 64- and 128-step windows. The frozen schema spans signature levels 1–3 (72 features); it measures how variation accrues within a window, beyond total variation alone.

**Reference / online information:** Reference and current-window features use the same history-normalized Rosenblatt increment stream. Each online window ends at the current observation. Sampled suffix-mutation and prefix replay left earlier features unchanged; complete correction-head package parity was not established.

**Tested settings or stage:** Synthetic cross-seed feasibility screen; grouped CV-A F1/F4 feasibility screen; frozen F0/F2/F3 follow-up; one-shot reduced transfer diagnostic; sampled inference parity; alternate-seed and age-only controls.

**Matched control:** A frozen same-window control used log variance, skewness, excess kurtosis, and mean absolute increment on the same causal increment stream. An age-only control was also tested but cannot rank same-age IDs, so it is not a generic feature-head null.

**Causal evidence:** Exact-prefix replay and 384 direct signature/window checks passed for the feature builder. A separate sampled audit reproduced base outputs and found no change to prior candidate features after suffix mutation. This is feature-source parity, not full correction-head package parity.

**Evaluation scope:** Two-fold F1/F4 grouped CV-A selection followed by a frozen F0/F2/F3 screen; one reduced diagnostic was read after freezing. The reduced result is not a sealed holdout and does not support further selection.

**Validation labels:** VALID_EXACT_STREAM; PARTIAL_FOLD; POST_SELECTION_CV; REDUCED_ONLY; CLOUD_PRIVATE; FEATURE_COMPONENT_PARITY_ONLY; PACKAGE_PARITY_UNKNOWN

**Result and disposition:** Lead–lag features showed modest synthetic cross-seed signal but did not establish superiority to simple moments. The matched moment control was competitive and fold contrasts varied; the reduced result and seed check did not establish stable transfer. No deployment followed.

**Limit / reason deprioritized:** Selection used the same CV-A folds later summarized; the reduced set had prior exposure elsewhere in the project. Feature parity is sampled and does not establish correction-head package parity.

**Open question:** Would lead–lag features add value to a nested, predeclared detector when compared with same-window moment controls and an independently sealed evaluation?



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `SYNTHETIC_ONLY_SCREEN`.

**Final status:** `HISTORICAL_RESULT_RECORDED_STATUS_UNSPECIFIED`.
</details>

<details>
<summary><code>CAT-049</code> · <code>MTH-049</code> · Historical Motif Novelty via Matrix-Profile Distances</summary>

**Record type:** detector or evidence method.

**Reported family label:** Matrix Profile Novelty.

**Question or hypothesis:** The existing recurrence-network, finite-RFF two-sample, and signature screens summarize local geometry or distributions. This experiment tests a different question: does a current causal subsequence become geometrically unlike every historical motif for the same ID? The candidate is a history-to-online nearest-subsequence discord score, not a self-join over the complete stream.

**Implementation:** The matrix-profile idea uses nearest-neighbor distances to summarize motif and discord novelty. This adaptation selects a fixed bank of historical subsequences, reserves a disjoint history tail for calibration, and compares each trailing online window with that bank using causal Rosenblatt-normalized values.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Historical Motif Novelty via Matrix-Profile Distances

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** causal_design_or_exact_stream_reported; audit_scope_varies

**Evaluation scope:** Frozen synthetic Stage 0 gate only; no competition folds, CV-B, reduced data, provider evaluation, or deployment package.

**Validation labels:** SYNTHETIC_ONLY; VALID_EXACT_STREAM

**Result and disposition:** The synthetic feasibility gate passed, but the frozen matrix-profile feature did not transfer to the screened challenge folds; not promoted.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `SYNTHETIC_ONLY_SCREEN`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-052</code> · <code>MTH-052</code> · Multi-Rank Subspace Projection — Search Report</summary>

**Record type:** detector or evidence method.

**Reported family label:** Mrsc Subspace Projection.

**Question or hypothesis:** Lee et al., “Multi-rank Subspace Change-point Detection for Monitoring Robotic Swarms,” arXiv:2506.18562v3 (revised 2026-08-16), propose MRS-C for emerging low-rank covariance structure. A rolling estimate of the leading signal subspace yields projection energy `Z_t = ||Uhat_t^T x_t||²`; a one-sided CUSUM accumulates `Z_t - Delta`.

**Implementation:** The tested feature forms lag vectors from the exact historical-reference Rosenblatt stream, estimates a covariance whitener on history only, and scores the current vector against a rank-2 subspace fit solely to the previous 32 lag-vectors. The basis refreshes every four observations. Historical prequential projection energies calibrate location/scale; outputs are a standardized projection energy, a fixed-drift positive-part CUSUM, and the previous-window top-subspace energy share. This is an empirical adaptation; overlapping lag vectors are dependent and no source guarantee transfers.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Multi-Rank Subspace Projection — Search Report

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** grouped_cv_a_partial

**Validation labels:** PARTIAL_FOLD_WHERE_APPLICABLE

**Result and disposition:** The multi-rank subspace candidate passed synthetic feasibility but underperformed on the screened F4/F1 folds; not promoted.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `PARTIAL_GROUPED_CV_A`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-069</code> · <code>MTH-069</code> · Ordinal Turn-Rate / Sequential Evidence — Search Report</summary>

**Record type:** detector or evidence method.

**Reported family label:** Ordinal Turn Rate.

**Question or hypothesis:** A change in the rate of strict local extrema may reveal dependence changes that marginal evidence misses. The experiment tested an ordinal turn-rate event and a Bernoulli likelihood-ratio mixture over candidate change starts after history-fitted AR/Rosenblatt normalization.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Ordinal Turn-Rate / Sequential Evidence — Search Report

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** feasibility_or_planned

**Validation labels:** UNKNOWN_FROM_PUBLIC_INDEX

**Result and disposition:** Status: Stage 0 plus staged CV-A transfer diagnostics complete; no promotion.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `FEASIBILITY_OR_PLANNED`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-077</code> · <code>MTH-077</code> · P6 Causal Ordinal Search Report</summary>

**Record type:** detector or evidence method.

**Reported family label:** P6 Causal Ordinal.

**Question or hypothesis:** Not preserved in the public summary; see the report title and source digest.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Not preserved in the public summary.

**Tested settings or stage:** P6 Causal Ordinal Search Report

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** grouped_cv_a_partial

**Validation labels:** PARTIAL_FOLD_WHERE_APPLICABLE

**Result and disposition:** Stage 1: Fold 4 and Fold 0 only; no test-reduced labels.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `PARTIAL_GROUPED_CV_A`.

**Final status:** `HISTORICAL_RESULT_RECORDED_STATUS_UNSPECIFIED`.
</details>

<details>
<summary><code>CAT-084</code> · <code>MTH-084</code> · Persistent-Laplacian Geometry for Causal Break Evidence</summary>

**Record type:** detector or evidence method.

**Reported family label:** Persistent Laplacian.

**Question or hypothesis:** The positive spectrum of a small delay-state graph Laplacian may capture within-scale connectivity changes that are missed by scalar marginal and innovation evidence. This is a new geometric representation, not another rolling-moment family. The narrow Stage-0 question is whether its causal history-referenced features add transferable synthetic signal, particularly for dynamics changes with nearly unchanged marginal behavior.

**Implementation:** Fit coordinate centers/scales and three graph-distance thresholds from the historical segment only. - At an online update, embed the latest 24 observed innovations into 22 three-lag points.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Persistent-Laplacian Geometry for Causal Break Evidence

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** causal_design_or_exact_stream_reported; audit_scope_varies

**Evaluation scope:** Synthetic Stage 0 followed by a frozen CV-A F4/F1 feasibility screen. No CV-B, reduced, provider, or deployment evaluation.

**Validation labels:** PARTIAL_FOLD; POST_SELECTION_CV; CLOUD_PRIVATE

**Result and disposition:** rolling-moment family.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `PARTIAL_GROUPED_CV_A`.

**Final status:** `HISTORICAL_RESULT_RECORDED_STATUS_UNSPECIFIED`.
</details>

<details>
<summary><code>CAT-085</code> · <code>MTH-085</code> · Persistent q=1 Laplacian Features — Stage 0 Report</summary>

**Record type:** detector or evidence method.

**Reported family label:** Persistent Laplacian Q1.

**Question or hypothesis:** Nie and Yue, “Online Change-Point Detection with Persistent Laplacian Features,” arXiv:2607.08635v2, combine delay-embedded Vietoris–Rips filtrations, persistent Betti features and positive persistent-Laplacian spectra, then ridge-whiten labeled Phase-I features and apply Page CUSUM.

**Implementation:** Use history-only Rosenblatt scores and distance quantiles to scale causal delay windows. The Stage-0 screens included GF(2) persistent beta-1 counts and a q=1 persistent combinatorial-Laplacian spectrum with three-dimensional delay states, 24-point windows, fixed historical scale pairs, and positive eigenvalues.

**Reference / online information:** Reference distance quantiles and whitening are fit from synthetic history only; each delay window uses observations available through its endpoint. The features are a representation screen, not the cited paper’s full Phase-I/Page-CUSUM procedure.

**Tested settings or stage:** Two synthetic Stage-0 screens: an earlier persistent-Betti feature screen and a fixed q=1 spectrum/scale/head screen. No competition CV, reduced evaluation, private run, or package integration.

**Matched control:** A synthetic feasibility comparison was run, but no report-specific, same-window low-order-moment matched-control result is preserved.

**Causal evidence:** History-only reference scales and causal delay windows were used; whitening matched the streaming transform on synthetic checks. Unit checks covered finite, deterministic output and prefix causality.

**Evaluation scope:** Synthetic Stage-0 feasibility only; no competition-derived labels or folds were accessed.

**Validation labels:** SYNTHETIC_ONLY; VALID_EXACT_STREAM.

**Result and disposition:** Both synthetic screens were completed and the tested q=1 recipes were stopped before competition evaluation. They do not establish structural-break performance on real or competition data.

**Limit / reason deprioritized:** The tested fixed q=1 spectrum/scale/head recipes were not advanced to supervised or competition evaluation; the paper’s assumptions and guarantees do not transfer to estimated Rosenblatt scores.

**Open question:** Could a simpler matched geometry summary justify a supervised test, and would its assumptions remain credible for dependent estimated innovations?



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `SYNTHETIC_ONLY_SCREEN`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-102</code> · <code>MTH-102</code> · Search Report: Whitened Ordinal-Pattern Evidence</summary>

**Record type:** detector or evidence method.

**Reported family label:** Rosenblatt Ordinal.

**Question or hypothesis:** Ordinal/permutation patterns on the Rosenblatt-normalized innovation stream may detect changes in local dependence and oscillation that are robust to scale and monotone transforms. The expert was evaluated as a supervised add-on and as a complement to the current Optuna trial-20 model.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Search Report: Whitened Ordinal-Pattern Evidence

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** F4/F0 selection followed by a frozen five-fold CV-A evaluation. No reduced-data result is reported.

**Validation labels:** POST_SELECTION_CV; CLOUD_PRIVATE

**Result and disposition:** The tested ordinal-pattern feature failed its selected full-CV screen and was not promoted.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `GROUPED_CV_A_FULL_OR_REPLAY`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-108</code> · <code>MTH-108</code> · Time-Augmented Rough-Path Signatures — Search Report</summary>

**Record type:** detector or evidence method.

**Reported family label:** Rough Path Signatures.

**Question or hypothesis:** Wang & Chakraborty study quickest detection using truncated signatures of time-augmented paths and derive a signature half-space stopping structure. Their theory assumes independent pre-/post-change rough paths, regularity moment bounds, and a lower bound on path separation. Their quickest-stopping objective and Brownian/fractional-Brownian simulations do not establish supervised time-series AUC gains for this benchmark.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Not preserved in the public summary.

**Tested settings or stage:** Time-Augmented Rough-Path Signatures — Search Report

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** Two-fold CV-A screen on F2/F4. The report says feature generation did not use labels, CV-B, or test_reduced; the stage was not promoted.

**Validation labels:** PARTIAL_FOLD; POST_SELECTION_CV; CLOUD_PRIVATE

**Result and disposition:** Status: Stage-1 complete; tested representation not promoted.

**Limit / reason deprioritized:** No further reason for deprioritization is preserved in the public summary.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `PARTIAL_GROUPED_CV_A`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-111</code> · <code>MTH-111</code> · History-Reference Signature-Metric Novelty — Stage 1</summary>

**Record type:** detector or evidence method.

**Reported family label:** Signature Metric Evidence.

**Question or hypothesis:** The prior time-augmented signature experiment fed 22 path coordinates to a supervised head and found little standalone signal. This experiment asks a different question: can a recent online path be recognized as geometrically unusual relative to the same ID's historical paths by using a truncated signature semi-metric and local neighborhood support? This is a path-space novelty detector, not another direct signature-coordinate head.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** History-Reference Signature-Metric Novelty — Stage 1

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** grouped_cv_a_partial

**Validation labels:** PARTIAL_FOLD_WHERE_APPLICABLE

**Result and disposition:** History-Reference Signature-Metric Novelty — Stage 1 Status: Two-fold feasibility screen complete; tested candidate not promoted.

**Limit / reason deprioritized:** No further reason for deprioritization is preserved in the public summary.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `PARTIAL_GROUPED_CV_A`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-126</code> · <code>MTH-126</code> · Visibility-Graph Backward-Degree Evidence</summary>

**Record type:** detector or evidence method.

**Reported family label:** Visibility Graph Bdi.

**Question or hypothesis:** The geometry of a history-whitened innovation path can change while the scalar marginal and dependence evidence remains ambiguous. A causal backward visibility degree compresses local peak/line-of-sight structure into a small streaming statistic; horizontal visibility supplies an ordinal-only control against natural visibility's amplitude-sensitive geometry.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Visibility-Graph Backward-Degree Evidence

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** Synthetic Stage 0 followed by a frozen CV-A F4/F1 screen; no CV-B, reduced, provider, or deployment evaluation.

**Validation labels:** PARTIAL_FOLD; POST_SELECTION_CV; CLOUD_PRIVATE

**Result and disposition:** The tested visibility-graph backward-degree feature/head and 20% blend were not promoted.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `PARTIAL_GROUPED_CV_A`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

### Spectral and multiscale evidence

<details>
<summary><code>CAT-010</code> · <code>MTH-010</code> · Causal C3 Lag-Surface Search Report</summary>

**Record type:** detector or evidence method.

**Reported family label:** Bispectral C3 Surface.

**Question or hypothesis:** Not preserved in the public summary; see the report title and source digest.

**Implementation:** Each completed 32-point block contributes its lag-pair third central moments for lags 1–6. The full surface is compared with the historical surface distribution; a compact alternative uses the first 3×3 two-dimensional DCT coefficients. The studentized version independently centers and RMS-scales each complete block before computing third moments. Features update only at a completed block boundary; a partial tail holds its previous value. The Stage-1 cache used the locked `RosenblattStreamingState` and exact `_online_scores` path, with sampled direct-step replay checks.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Causal C3 Lag-Surface Search Report

**Matched control:** The exact Trial-52 stream served as the feature-head reference; synthetic screens compared block cumulant variants with low-order controls.

**Causal evidence:** Features update only at completed 32-point block boundaries and carry forward through a partial tail. Sampled direct-step replay was exact.

**Evaluation scope:** grouped_cv_a_partial

**Validation labels:** VALID_EXACT_STREAM; PARTIAL_FOLD; POST_SELECTION_CV

**Result and disposition:** The synthetic response did not transfer to the screened CV-A folds. The tested lag-6/block-32 configurations were closed without promotion.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `PARTIAL_GROUPED_CV_A`.

**Final status:** `HISTORICAL_RESULT_RECORDED_STATUS_UNSPECIFIED`.
</details>

<details>
<summary><code>CAT-011</code> · <code>MTH-011</code> · Causal Bispectral Phase-Coupling Evidence</summary>

**Record type:** detector or evidence method.

**Reported family label:** Bispectral Phase Coupling.

**Question or hypothesis:** History-whitened streams may undergo a change in phase-coupled nonlinear dependence while their one-point marginal distribution, mean, variance, and linear autocovariance remain unchanged. A causal lagged third cumulant is one time-domain coefficient of the third-order cumulant surface whose Fourier transform is the bispectrum. It may therefore detect information absent from the current marginal-moment and first/second-order lag-product features.

**Implementation:** The candidate measures history-standardized third-order phase coupling with rolling lagged cumulant features. It was compared with a low-order moment and lag-product control using the same windows; this summary does not establish a universal advantage.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Causal Bispectral Phase-Coupling Evidence

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** synthetic_screen

**Validation labels:** PARTIAL_FOLD_WHERE_APPLICABLE

**Result and disposition:** The fixed-lag C3 recipe and its small post-screen blend were closed without promotion; this does not reject other bispectral methods.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `SYNTHETIC_ONLY_SCREEN`.

**Final status:** `HISTORICAL_RESULT_RECORDED_STATUS_UNSPECIFIED`.
</details>

<details>
<summary><code>CAT-012</code> · <code>MTH-012</code> · Causal Frequency-Triplet Bispectral Change Evidence</summary>

**Record type:** detector or evidence method.

**Reported family label:** Bispectral Triplet Online.

**Question or hypothesis:** Quadratic phase coupling at frequencies satisfying f3=f1+f2 can change while first-order spectral power and second-order dependence remain similar. The experiment tested a causal frequency-triplet bispectral feature on completed blocks, then compared it with a small time-domain control.

**Implementation:** Estimate phase-coupling features for fixed frequency triplets with k3=k1+k2 on completed blocks. The synthetic generator uses integer-bin sinusoids with independent block phases; the online feature emits only after a block completes.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Causal Frequency-Triplet Bispectral Change Evidence

**Matched control:** A low-order moment and lag-product control used the same block/window information; the exact Trial-52 stream was the supervised-head reference.

**Causal evidence:** Unit checks covered prefix mutation, block-end emission, finite/aligned output, partial-tail carry-forward, and sampled direct-step parity.

**Evaluation scope:** Synthetic Stage 0 and exact-stream grouped CV-A F4/F1 screen.

**Validation labels:** VALID_EXACT_STREAM; PARTIAL_FOLD; POST_SELECTION_CV

**Result and disposition:** Close this fixed three-triplet, block-32, horizon-4 feature head; do not promote it. The result does not reject other bispectral estimators or lag grids.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `SYNTHETIC_ONLY_SCREEN`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-017</code> · <code>MTH-017</code> · Causal Wavelet Scattering on Rosenblatt Innovations</summary>

**Record type:** detector or evidence method.

**Reported family label:** Causal Wavelet Scattering.

**Question or hypothesis:** Mallat's wavelet scattering cascade repeatedly applies localized wavelet filters and modulus nonlinearities. For stationary processes, expected scattering coefficients depend on higher-order moments and can distinguish processes whose second-order moments (and thus power spectra) agree. This suggested that second-order modulation paths might reveal nonlinear dependence changes missed by a plain spectral summary.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Causal Wavelet Scattering on Rosenblatt Innovations

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** synthetic_screen

**Validation labels:** UNKNOWN_FROM_PUBLIC_INDEX

**Result and disposition:** Status: Two cross-seed synthetic screens negative; this fixed feature/head recipe is not advanced to competition folds.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `SYNTHETIC_ONLY_SCREEN`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-019</code> · <code>MTH-019</code> · CHASM-Inspired Spectral-Velocity Evidence — Stage 0</summary>

**Record type:** detector or evidence method.

**Reported family label:** Chasm Spectral.

**Question or hypothesis:** After history-fitted AR/Rosenblatt whitening, a univariate break may change delay-state transition eigenvalues even when raw marginal evidence is weak. This experiment tracked the spectrum and its velocity for a causal order-2 delay operator.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** CHASM-Inspired Spectral-Velocity Evidence — Stage 0

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** causal_design_or_exact_stream_reported; audit_scope_varies

**Evaluation scope:** grouped_cv_a_full_or_replay

**Validation labels:** UNKNOWN_FROM_PUBLIC_INDEX

**Result and disposition:** CHASM-Inspired Spectral-Velocity Evidence — Stage 0 Status: staged five-fold CV-A and one frozen reduced diagnostic complete; this approximation is not promoted.

**Limit / reason deprioritized:** No further reason for deprioritization is preserved in the public summary.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `GROUPED_CV_A_FULL_OR_REPLAY`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-116</code> · <code>MTH-116</code> · Spectral Delay-State LSS — Search Report</summary>

**Record type:** detector or evidence method.

**Reported family label:** Spectral Delay Lss.

**Question or hypothesis:** Does the relative covariance eigen-spectrum of short causal delay-vectors expose dynamics changes left in the exact historical Rosenblatt stream, and does it improve a matched supervised ranking head beyond joint evidence plus stream age?

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Spectral Delay-State LSS — Search Report

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** Synthetic Stage 0 followed by a CV-A F4/F1 screen. The source says CV-A/B, reduced, provider, and deployment stages were not completed beyond this screen.

**Validation labels:** PARTIAL_FOLD; POST_SELECTION_CV; CLOUD_PRIVATE

**Result and disposition:** The synthetic spectral-delay-state gate did not justify the next validation stage; the tested recipe was closed before challenge-fold evaluation.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `PARTIAL_GROUPED_CV_A`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-117</code> · <code>MTH-117</code> · HAC-Spectral Calibration of Full-Scan U Evidence</summary>

**Record type:** detector or evidence method.

**Reported family label:** Spectral Hac U Calibration.

**Question or hypothesis:** The existing finite-RFF full-scan U-statistic yields useful break evidence, but its uncalibrated running maximum may have history- and dependence-specific null scales. Transforming that path using the weak-dependence spectral null distribution may improve early-age ranking and reduce false-alert heterogeneity. The causal transfer of the HAC component is the specific hypothesis; another RFF kernel, suffix set, or scalar normalization is not.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** HAC-Spectral Calibration of Full-Scan U Evidence

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** feasibility_or_planned

**Validation labels:** UNKNOWN_FROM_PUBLIC_INDEX

**Result and disposition:** The preregistered HAC spectral-calibration gate failed; no challenge validation or deployment was run.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `FEASIBILITY_OR_PLANNED`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-121</code> · <code>MTH-121</code> · Search Report: Causal Time-Frequency Discrepancy</summary>

**Record type:** detector or evidence method.

**Reported family label:** Tfc Discrepancy.

**Question or hypothesis:** Persistent structural changes can alter periodicity, roughness, or spectral concentration even when low-order moments are similar. A causal FFT summary of the normalized innovation prefix was compared with a historical spectral reference at windows 16, 32, and 64.

**Implementation:** For the spectral branch, compare history-only Rosenblatt FFT references with current-prefix windows (16/32/64) using delta and robust-z discrepancies in total power, low/mid/high frequency fractions, spectral entropy, and peak frequency. A separate TF-C pilot used causal time-frequency embeddings and a fold-excluded head.

**Reference / online information:** Spectral references use historical normalized innovations only; each current window ends at the current timestep. The TF-C pilot pretrained on historical data with target-fold IDs excluded and formed online embeddings from prefixes.

**Tested settings or stage:** FFT feature and Trial-13 head screens on CV-A folds F4/F0; no full-CV or exact-stream replay followed. The TF-C pilot used two causal-window unit tests and screened fold-excluded heads on F1/F3; no reduced evaluation or deployment package was run.

**Matched control:** The Trial-13 head was the frozen baseline for the FFT add-on. TF-C used Trial-11 OOF features as a reference; no same-window low-order spectral/moment control was preserved.

**Causal evidence:** The FFT features are built from history and observed prefixes. The TF-C pilot passed two causal-window unit tests, but the report explicitly does not establish full-package parity or a five-fold evaluation.

**Evaluation scope:** Partial grouped CV-A screens: FFT feature/head on F4/F0 and a separate TF-C pilot on F1/F3; no full CV-A, reduced labels, CV-B, private run, or package integration.

**Validation labels:** PARTIAL_FOLD; POST_SELECTION_CV; CLOUD_PRIVATE; FEATURE_COMPONENT_PARITY_ONLY

**Result and disposition:** The FFT head did not show stable complementarity across its two folds. The tested 64-step TF-C configuration was stopped after its limited fold screen; this does not reject other time-frequency encoders or objectives.

**Limit / reason deprioritized:** Both branches were screened on few folds and selected through development CV-A; the TF-C causal-window tests do not prove full detector parity or transfer.

**Open question:** Would a predeclared time-frequency representation outperform matched moment and spectral controls under nested folds and exact package replay?



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `PARTIAL_GROUPED_CV_A`.

**Final status:** `HISTORICAL_RESULT_RECORDED_STATUS_UNSPECIFIED`.
</details>

<details>
<summary><code>CAT-129</code> · <code>MTH-129</code> · Causal Haar Scaling-Exponent Change</summary>

**Record type:** detector or evidence method.

**Reported family label:** Wavelet Long Memory Change.

**Question or hypothesis:** A break in long-memory strength changes the slope of log Haar coefficient variance against log scale. A history-referenced, causal slope contrast may capture dependence changes that the current autoregressive/scale Rosenblatt evidence misses.

**Implementation:** For each fixed window `W in {64,128}`, compute a weighted regression slope of `log2(var(Haar_j))` on octave `log2(scale)` from history only. At online time `t`, compute the same slope using `online[t-W+1:t]` only, then emit its signed and absolute difference from the historical slope. The fixed scales are `[1,2,4,8]` for W64 and `[1,2,4,8,16]` for W128. Non-decimated Haar details update as observations arrive. Features are zero until their window is ready. The code does not use the final stream length, future values, labels, or a candidate break time.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Causal Haar Scaling-Exponent Change

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** causal_design_or_exact_stream_reported; audit_scope_varies

**Evaluation scope:** exact_stream_or_package_replay_scope_unspecified

**Validation labels:** UNKNOWN_FROM_PUBLIC_INDEX

**Result and disposition:** Status: Stage 0 and staged CV-A feasibility complete; exact recipe not promoted.

**Limit / reason deprioritized:** No further reason for deprioritization is preserved in the public summary.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `EXACT_STREAM_SCOPE_UNSPECIFIED`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

### Statistical and sequential baselines

<details>
<summary><code>CAT-032</code> · <code>MTH-032</code> · Denoising Score-Matching CUSUM on Whitened Lag States</summary>

**Record type:** detector or evidence method.

**Reported family label:** Denoising Score Cusum.

**Question or hypothesis:** The Trial-11 pipeline is strong at marginal/conditional innovation evidence, but may miss nonlinear changes in the joint geometry of adjacent whitened innovations. Estimating smoothed score functions for historical and recent lag-state distributions, then contrasting their Hyvärinen scores, could detect conditional changes that raw moments and a first-order lag product miss.

**Implementation:** 1. Transform historical and online values with the existing history-fitted Rosenblatt stream. Form lag states `u_t = (rw_z[t], rw_z[t-1])`, carrying the last historical innovation into the first online state. 2. Select at most 64 reference centers from the first 80% of historical lag-states. Reserve the remaining history for a null-calibration stream. 3. Approximate denoising score matching with the exact score of the empirical Gaussian-smoothed distribution `p_sigma(u) = mean_i N(u; center_i, sigma^2 I)`.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Denoising Score-Matching CUSUM on Whitened Lag States

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** synthetic_screen

**Validation labels:** UNKNOWN_FROM_PUBLIC_INDEX

**Result and disposition:** The finite Gaussian-KDE score adaptation was stopped before Stage 2 after near-chance F4/F1 ranking and unstable null evidence.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `SYNTHETIC_ONLY_SCREEN`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-070</code> · <code>MTH-070</code> · P1 Time-Conditioned Historical Null</summary>

**Record type:** detector or evidence method.

**Reported family label:** P1 Time Conditioned Null.

**Question or hypothesis:** A historical null may vary with stream age without using the final online horizon. This causal adaptation selects a predeclared age bin from the current observed step and does not inspect future length.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** P1 Time-Conditioned Historical Null

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** UNKNOWN_FROM_PUBLIC_INDEX

**Validation labels:** VALID_EXACT_STREAM; PARTIAL_FOLD; POST_SELECTION_CV

**Result and disposition:** The age-conditioned historical-null feature was treated as a complementary expert; any blend weight was to be frozen before CV-B access. The public summary does not establish an independent performance estimate.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `PARTIAL_GROUPED_CV_A`.

**Final status:** `HISTORICAL_RESULT_RECORDED_STATUS_UNSPECIFIED`.
</details>

<details>
<summary><code>CAT-071</code> · <code>MTH-071</code> · P2 Causal Baseline Lock</summary>

**Record type:** baseline.

**Reported family label:** P2 Causal Baseline.

**Question or hypothesis:** The historical-null P2 score must be measured under the same causal information constraint as `infer()`. The old batch cache is retained only as an `INVALID_OR_LEAKED_REFERENCE` because its null segment length depends on the final online horizon.

**Implementation:** P2 fits its AR/Rosenblatt reference and historical null from the reference segment, then emits causal multiscale evidence using observations through the current step. The locked version excludes final online length from null calibration.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** P2 Causal Baseline Lock

**Matched control:** This is the locked causal baseline; the previous batch/cache path using final horizon is retained only as an INVALID_FUTURE_LENGTH comparison.

**Causal evidence:** Full exact-stream CV-A replay; score at each time depends only on history and the observed online prefix.

**Evaluation scope:** Five-fold grouped CV-A plus a reduced transfer diagnostic on private competition data; not reproducible from the public repository.

**Validation labels:** VALID_EXACT_STREAM; GROUPED_CV_A; PRIVATE_DATA_UNAVAILABLE

**Result and disposition:** Locked causal P2 reference: five-fold exact-stream CV-A mean TS-AUC 0.630553 and reduced diagnostic 0.599657. Competition data and artifacts are unavailable for independent reproduction.

**Limit / reason deprioritized:** This historical competition baseline is not the compact public Gaussian AR(1) API and cannot be replayed without authorized private inputs and artifacts.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_COMPETITION_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `GROUPED_CV_A_FULL_OR_REPLAY`.

**Final status:** `HISTORICAL_REFERENCE`.
</details>

<details>
<summary><code>CAT-079</code> · <code>MTH-079</code> · P6 Causal Self-Normalized Search Report</summary>

**Record type:** detector or evidence method.

**Reported family label:** P6 Causal Selfnorm.

**Question or hypothesis:** Not preserved in the public summary; see the report title and source digest.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Not preserved in the public summary.

**Tested settings or stage:** P6 Causal Self-Normalized Search Report

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** grouped_cv_a_partial

**Validation labels:** PARTIAL_FOLD_WHERE_APPLICABLE

**Result and disposition:** Stage 1: Fold 4 and Fold 0 only, standard Trial-20 head; no test-reduced labels.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `PARTIAL_GROUPED_CV_A`.

**Final status:** `HISTORICAL_RESULT_RECORDED_STATUS_UNSPECIFIED`.
</details>

<details>
<summary><code>CAT-087</code> · <code>MTH-087</code> · Predictive-Mixture CuSum (PM-CuSum) — Search Report</summary>

**Record type:** detector or evidence method.

**Reported family label:** Pm Cusum.

**Question or hypothesis:** Halme, Poor, and Koivunen, *Adaptive Sequential Change Detection using Mixtures of Predictive Distributions*, arXiv:2606.05072v3 (2026), propose window-specific predictive densities mixed by fixed-share weights, followed by a predictive-mixture likelihood ratio and CuSum recursion. Their formal setup assumes independent observations, known pre-change density `q`, and an unknown post-change distribution in a specified class.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Predictive-Mixture CuSum (PM-CuSum) — Search Report

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** Synthetic Stage 0 gates passed, then a frozen CV-A F4/F1 screen was run. No CV-B, reduced, provider, or deployment evaluation.

**Validation labels:** PARTIAL_FOLD; POST_SELECTION_CV; CLOUD_PRIVATE

**Result and disposition:** The frozen predictive-mixture CUSUM passed synthetic gates but remained an exploratory F4/F1 screen; it was not promoted.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `PARTIAL_GROUPED_CV_A`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

### Supervised heads, ensembles, and selection

<details>
<summary><code>CAT-013</code> · <code>MTH-013</code> · Break Incidence × Conditional Timing — Search Report</summary>

**Record type:** detector or evidence method.

**Reported family label:** Break Presence Factorization.

**Question or hypothesis:** Does the causal factorization P(y_t=1 | X[0:t]) = P(B=1 | X[0:t]) × P(y_t=1 | B=1, X[0:t]) improve pointwise TS-AUC by modeling ID-level break existence separately from break timing?

**Implementation:** Use causal Rosenblatt features including standardized innovations, mean-shift evidence, joint log-mixture and maximum evidence, and observed stream age. Compare a break-incidence head multiplied by a broken-ID-only timing head with a pointwise LightGBM control using official pair-count weights.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Break Incidence × Conditional Timing — Search Report

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** Frozen synthetic Stage 0 only; no CV-A/B, reduced, competition-private, provider, GPU, or deployment evaluation. Direct and prefix/suffix replays matched in the recorded checks.

**Validation labels:** SYNTHETIC_ONLY; VALID_EXACT_STREAM

**Result and disposition:** The exact incidence-by-timing product and training scheme were closed; no promotion.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `SYNTHETIC_ONLY_SCREEN`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-014</code> · <code>MTH-014</code> · CatBoost P2+Auxiliary Heads and Sampled PairLogit</summary>

**Record type:** combination or scoring head.

**Reported family label:** Catboost Pairwise P2 Aux.

**Question or hypothesis:** Can CatBoost's symmetric-tree classifier or a ranking objective improve the feature-only P2+auxiliary head on pair-weighted stepwise TS-AUC? The input is the existing 48-column causal feature cache: 15 whitened/Rosenblatt evidence features, 10 historical-null P2 features, 4 Koopman features, 4 DMD-residual features, 8 Rosenblatt-martingale features, 6 time-frequency features, and stream age.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** CatBoost P2+Auxiliary Heads and Sampled PairLogit

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** feasibility_or_planned

**Validation labels:** POST_SELECTION_CV

**Result and disposition:** Status: research-only; no package change or model promotion.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `FEASIBILITY_OR_PLANNED`.

**Final status:** `HISTORICAL_RESULT_RECORDED_STATUS_UNSPECIFIED`.
</details>

<details>
<summary><code>CAT-038</code> · <code>MTH-038</code> · OOF Ensemble Audit</summary>

**Record type:** validation audit.

**Reported family label:** Ensemble Audit.

**Question or hypothesis:** Not preserved in the public summary; see the report title and source digest.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Not preserved in the public summary.

**Tested settings or stage:** OOF Ensemble Audit

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** Audit of saved pairwise OOF outputs over all five CV-A folds; this was an OOF-result audit, not a new inference evaluation. The report states that test_reduced labels were not used.

**Validation labels:** POST_SELECTION_CV; CLOUD_PRIVATE

**Result and disposition:** Pairwise OOF results did not justify a joint multi-expert ensemble; the selected blend remains vulnerable to selection noise.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_AUDIT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `GROUPED_CV_A_FULL_OR_REPLAY`.

**Final status:** `AUDIT_ONLY`.
</details>

<details>
<summary><code>CAT-041</code> · <code>MTH-041</code> · Feature-Only Blend Weight Optimizer — 2026-09-27</summary>

**Record type:** selection or training method.

**Reported family label:** Feature Only Blend Optimizer.

**Question or hypothesis:** Does a low-dimensional optimizer improve a blend between two grouped-ID- excluded, feature-only heads, and do Optuna TPE, simulated annealing, or Nevergrad DE/PSO outperform a simple grid on held-out IDs?

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Not preserved in the public summary.

**Tested settings or stage:** Feature-Only Blend Weight Optimizer — 2026-09-27

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** Five-fold outer evaluation of feature-only blend weights; each outer-fold head excluded that fold and the scalar weight used 1,200 disjoint IDs. CV-B, reduced labels, provider evaluation, and package integration were not used.

**Validation labels:** POST_SELECTION_CV; CLOUD_PRIVATE

**Result and disposition:** The exact two-head blend/weight-optimizer recipe was stopped and not promoted.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `GROUPED_CV_A_FULL_OR_REPLAY`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-053</code> · <code>MTH-053</code> · Nested Causal Feature-Only Pairwise Correction</summary>

**Record type:** combination or scoring head.

**Reported family label:** Nested Causal Pairwise Correction.

**Question or hypothesis:** Per-step pairwise reweighting may improve ranking even when the base detector uses only label-blind causal evidence features. To avoid the old P11 failure, all base scores used to identify hard training examples must be cross-fitted inside the outer training folds, and neither head may consume supervised fold-specific prediction columns.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Nested Causal Feature-Only Pairwise Correction

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** Nested causal feature-only pairwise correction evaluated across all five outer folds; the recorded outer/inner exclusions are described per fold. The family had prior CV-A selection exposure.

**Validation labels:** POST_SELECTION_CV; CLOUD_PRIVATE

**Result and disposition:** Retained as an exploratory complementary feature family, not a promotion candidate; the tested pairwise correction did not improve the selected reference.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `GROUPED_CV_A_FULL_OR_REPLAY`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-073</code> · <code>MTH-073</code> · P3 Causal Head Search Report</summary>

**Record type:** combination or scoring head.

**Reported family label:** P3 Causal Head.

**Question or hypothesis:** Not preserved in the public summary; see the report title and source digest.

**Implementation:** P3 is a causal historical-null head selected as fixed trial 13 after an F0/F4 search, then evaluated on all five grouped CV-A folds.

**Reference / online information:** Not preserved in the public summary.

**Tested settings or stage:** P3 Causal Head Search Report

**Matched control:** Locked P2/Trial-11 reference on the same folds; selection used F0/F4 before the five-fold confirmation.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** grouped_cv_a_full_or_replay

**Validation labels:** VALID_EXACT_STREAM; POST_SELECTION_CV

**Result and disposition:** The fixed P3 trial was confirmed on five CV-A folds after F0/F4-informed selection; mean TS-AUC 0.631890 is POST_SELECTION_CV, not an independent benchmark.

**Limit / reason deprioritized:** The five-fold mean remains post-selection because the fixed trial was chosen after inspecting two folds; it is not an independent estimate or clean benchmark.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `GROUPED_CV_A_FULL_OR_REPLAY`.

**Final status:** `HISTORICAL_RESULT_RECORDED_STATUS_UNSPECIFIED`.
</details>

<details>
<summary><code>CAT-081</code> · <code>MTH-081</code> · Pairwise TS-AUC Objective — Search Report</summary>

**Record type:** selection or training method.

**Reported family label:** Pairwise Ts Auc.

**Question or hypothesis:** Not preserved in the public summary; see the report title and source digest.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Not preserved in the public summary.

**Tested settings or stage:** Pairwise TS-AUC Objective — Search Report

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** CV-A F4/F1 screen plus one frozen reduced diagnostic. X-only feature construction and stream parity were checked on five IDs; CV-B, provider evaluation, and package integration were not used.

**Validation labels:** VALID_EXACT_STREAM; PARTIAL_FOLD; POST_SELECTION_CV; CLOUD_PRIVATE

**Result and disposition:** The direct sampled-pairwise head failed its continuation gate on both screened CV-A folds; it produced no new best or submission candidate.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `PARTIAL_GROUPED_CV_A`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-094</code> · <code>MTH-094</code> · Search Report: Robust DGP-Group Training</summary>

**Record type:** selection or training method.

**Reported family label:** Robust Dgp Groups.

**Question or hypothesis:** Fold 4 may represent a difficult historical DGP group. History-only descriptors and group-balanced loss may reduce worst-group failure without hard-routing IDs or relying on online labels.

**Implementation:** Build history-only descriptors (log length and scale, lag-1 autocorrelation, sign-change rate, log difference scale, standardized tail rate, excess kurtosis, log MAD, and spectral entropy); fit K-means groups on each training fold only. Apply group-frequency powers to the supervised loss, with variants that also expose descriptors as model inputs; no hard routing occurs online.

**Reference / online information:** Clustering descriptors and group frequencies are estimated from training histories within each fold. They influence training weights or optional model inputs; no online labels or inference-time group routing are used.

**Tested settings or stage:** Successive grouped CV-A screens on F4/F0 used group counts and weighting exponents, then a five-fold confirmation and later cross-fitted retests on the CPIT/Trial-52 head. No CV-B or reduced labels were used to choose the final retests.

**Matched control:** The V19, P2, and later Trial-19/Trial-52 heads served as architecture-matched references. Variants compared descriptor-as-input against weighting-only, with the baseline training objective otherwise held fixed.

**Causal evidence:** All descriptors are computed from history and the group assignments are training-time metadata; no online routing or labels are used. The public report does not establish an end-to-end streaming detector parity audit for the later heads.

**Evaluation scope:** Repeated grouped CV-A: initial F4/F0 screen and TPE search, five-fold confirmation, and later all-fold cross-fitted retests. These followed earlier CV-A screening; no CV-B or reduced evaluation selected the final setting.

**Validation labels:** POST_SELECTION_CV; CLOUD_PRIVATE

**Result and disposition:** Some settings improved a difficult fold slightly, but the gain was not global and errors remained highly correlated with the baseline. The K-means group-weighting branch was deprioritized and not deployed.

**Limit / reason deprioritized:** The multi-stage search reused CV-A for screening and confirmation, and subgroup gains did not translate into a robust overall improvement. The result does not disprove domain-robust training generally.

**Open question:** Would a more complementary history-only representation or a preregistered worst-group objective improve transfer under independent grouped evaluation?



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `GROUPED_CV_A_FULL_OR_REPLAY`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-120</code> · <code>MTH-120</code> · Constrained Symbolic Causal Evidence Discovery</summary>

**Record type:** selection or training method.

**Reported family label:** Symbolic Evidence Discovery.

**Question or hypothesis:** Six mature, label-blind causal evidence channels were combined by a linear simplex portfolio, but that search remained far below the package reference. The unresolved question is whether detector evidence is complementary only conditionally: a maximum can represent an OR/robust-alarm rule, a minimum an AND/consensus rule, and a positive geometric mean a soft conjunction. This is a deliberately small program-search family, not another feature sweep.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Constrained Symbolic Causal Evidence Discovery

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** F4 screen only; expression selection used inner leave-one-fold-out checks over F1/F2/F3. There was no F0, full CV-A, CV-B, reduced, provider, or package evaluation.

**Validation labels:** PARTIAL_FOLD; POST_SELECTION_CV; CLOUD_PRIVATE

**Result and disposition:** Status: Stage 1 complete on F4; the tested 51-expression grammar is not promoted and does not advance to F0.

**Limit / reason deprioritized:** No further reason for deprioritization is preserved in the public summary.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `PARTIAL_GROUPED_CV_A`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-123</code> · <code>MTH-123</code> · Tri-Modal Feature-Head Blend Diagnostic</summary>

**Record type:** combination or scoring head.

**Reported family label:** Tri Modal Blend.

**Question or hypothesis:** The P2+aux+CRM feature-head baseline may benefit from a small blend of Candidate 9 (historical-manifold OSN-RFF/full-scan-U) and VSBT post-regime predictions, which use different detector constructions.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Tri-Modal Feature-Head Blend Diagnostic

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** grouped_cv_a_full_or_replay

**Validation labels:** UNKNOWN_FROM_PUBLIC_INDEX

**Result and disposition:** The tri-modal blend was a post-hoc diagnostic and produced no new best; not promoted.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `GROUPED_CV_A_FULL_OR_REPLAY`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>

<details>
<summary><code>CAT-124</code> · <code>MTH-124</code> · Same-Step LambdaRank Head</summary>

**Record type:** combination or scoring head.

**Reported family label:** V19 Lambdarank Head.

**Question or hypothesis:** TS-AUC compares IDs at the same online step, so a grouped LambdaRank head may learn the within-step ordering directly and complement the frozen V19 score. The search deliberately includes raw component scores, per-step component ranks, time features, and classifier/ranker blending rather than treating the first fixed LambdaRank configuration as a verdict on ranking objectives.

**Implementation:** Implementation details are not preserved in the public summary.

**Reference / online information:** Reference and information-set details are not preserved in the public summary.

**Tested settings or stage:** Same-Step LambdaRank Head

**Matched control:** No report-specific control detail is preserved in the public summary. This does not imply that no control was run; see docs/failed_experiments.md for family-level examples.

**Causal evidence:** UNKNOWN_FROM_PUBLIC_INDEX

**Evaluation scope:** F4/F0 search followed by a frozen five-fold CV-A evaluation. No reduced-data result is reported.

**Validation labels:** POST_SELECTION_CV; CLOUD_PRIVATE

**Result and disposition:** The same-step LambdaRank head did not pass its focused screen and was not deployed.

**Limit / reason deprioritized:** No additional limitation is preserved in the public summary; see the result and validation fields.

**Open question:** Not recorded in the public summary.



**Implementation status:** `HISTORICAL_EXPERIMENT_IMPLEMENTATION_NOT_SHIPPED`.

**Validation stage:** `GROUPED_CV_A_FULL_OR_REPLAY`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.
</details>


<details>
<summary><code>SUP-006</code> · <code>SRC-029</code> · Static history-ACF descriptor for a causal reference head</summary>

**Record type:** detector or evidence method.

**Reported family label:** Historical ACF conditioning.

**Question or hypothesis:** A history-only lag-1 dependence descriptor may help a compact detector rank breaks across alternating, middle, and persistent history regimes.

**Implementation:** One standardized historical ACF descriptor was added to the fixed 15-feature Clean V2 synthetic control; the descriptor was computed once from reference history.

**Reference / online information:** The direct head was trained on three synthetic seeds and evaluated on the held-out seed. Online evidence used the observed prefix, with no online refitting or group routing.

**Tested settings or stage:** Preregistered four-seed held-out synthetic Stage 0 with three history regimes and fixed change mechanisms.

**Matched control:** The 15-feature Clean V2 control and a shuffled-ACF placebo on matched synthetic streams.

**Causal evidence:** Prefix-mutation checks reported zero score changes before the mutation point.

**Evaluation scope:** Synthetic-only four-seed Stage 0; no competition folds, reduced data, private evaluation, or deployment were accessed.

**Validation labels:** `SYNTHETIC_ONLY; SYNTHETIC_STAGE0; FROZEN_GATE_FAILED`.

**Result and disposition:** The mean candidate-control delta was +0.0051 and positive on three of four held seeds, but the predeclared condition for both ACF tails failed. The fixed recipe was closed.

**Limit / reason deprioritized:** The result covers one descriptor, head, and synthetic design; it does not rule out history-conditioned detection generally.

**Open question:** Would a separately preregistered history-regime representation help under independent DGPs and a matched low-order control?

**Source evidence:** `SRC-029`.

**Implementation status:** `HISTORICAL_SYNTHETIC_PROTOTYPE_NOT_SHIPPED`.

**Validation stage:** `SYNTHETIC_ONLY_SCREEN`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.

</details>

<details>
<summary><code>SUP-007</code> · <code>SRC-035</code> · History-only rank calibration before mixture</summary>

**Record type:** detector or evidence method.

**Reported family label:** Rosenblatt componentwise null-rank calibration.

**Question or hypothesis:** Calibrating each causal window component against its history-only null distribution before mixing may reduce cross-window scale imbalance.

**Implementation:** Each fixed trailing-window component on the causal Rosenblatt stream was upper-tail ranked against overlapping history-only windows of the same length, then combined into a fixed rank-mixture score.

**Reference / online information:** The historical implementation updated the Rosenblatt state one observation at a time. Each online window ended at the current observation; calibration samples came from reference history only.

**Tested settings or stage:** Synthetic Stage 0 with four fresh seeds, five change mechanisms, stationary AR(2) and GARCH null stress cases, and exact-online-age pair-weighted AUC.

**Matched control:** Raw production tail-log-mixture was primary; tail maximum, joint log-mixture, scale maximum, and age-only scores were descriptive controls.

**Causal evidence:** Prefix invariance, deterministic regeneration, finite-score, matched-prefix, and per-step reconstruction checks passed for the recorded synthetic implementation.

**Evaluation scope:** Synthetic-only four-seed Stage 0. Overlapping calibration windows were not shown to be exchangeable with future windows.

**Validation labels:** `SYNTHETIC_ONLY; SYNTHETIC_STAGE0; FROZEN_GATE_FAILED; NO_P_VALUE_OR_E_VALUE_GUARANTEE`.

**Result and disposition:** The mean heavy-tail contrast was positive but below the preregistered +0.020 advancement threshold. The fixed recipe was closed without a competition-data evaluation.

**Limit / reason deprioritized:** Serial dependence in history windows prevents treating these ranks as valid p-values or an e-process without additional assumptions and evidence.

**Open question:** Can a history-calibrated componentwise score help under dependent-null calibration with a defensible coverage or sequential-validity argument?

**Source evidence:** `SRC-035`.

**Implementation status:** `HISTORICAL_SYNTHETIC_PROTOTYPE_NOT_SHIPPED`.

**Validation stage:** `SYNTHETIC_ONLY_SCREEN`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.

</details>

<details>
<summary><code>SUP-008</code> · <code>SRC-036</code> · History-only rank calibration after mixture</summary>

**Record type:** detector or evidence method.

**Reported family label:** Rosenblatt total-score null-rank calibration.

**Question or hypothesis:** Applying an ID-specific history-only rank map after window evidence is integrated may change cross-stream rankings differently from calibrating each component first.

**Implementation:** The raw tail log-mixture was computed first, then ranked against overlapping history-only mixture endpoints in the corresponding online-age band. Componentwise rank-then-mixture and fixed detector controls used the same streams.

**Reference / online information:** History endpoints and age bands defined the calibration map; online scores used only the observed prefix. The recorded synthetic implementation passed prefix-mutation and deterministic-regeneration checks.

**Tested settings or stage:** Four fresh synthetic seeds, five change mechanisms, and stationary AR(2)/GARCH null stress cases.

**Matched control:** Raw tail log-mixture was primary; componentwise rank-then-mixture, joint and scale evidence, tail maximum, and age-only scores were also reported.

**Causal evidence:** Prefix invariance passed for the tested synthetic streams. Calibration-window exchangeability and sequential validity were not established.

**Evaluation scope:** Synthetic-only Stage 0 with exact-online-age scoring; historical endpoints overlap and are dependent.

**Validation labels:** `SYNTHETIC_ONLY; SYNTHETIC_STAGE0; FROZEN_GATE_FAILED; NO_P_VALUE_OR_E_VALUE_GUARANTEE`.

**Result and disposition:** The total-score rank map had a negative mean heavy-tail delta versus raw scores and was negative on all four seeds. The frozen advancement gate failed; no competition-data screen followed.

**Limit / reason deprioritized:** The tested recipe did not improve the fixed synthetic control and does not provide a conformal or sequential-validity guarantee.

**Open question:** Can another calibration map improve cross-stream comparability while retaining a justified null calibration under serial dependence?

**Source evidence:** `SRC-036`.

**Implementation status:** `HISTORICAL_SYNTHETIC_PROTOTYPE_NOT_SHIPPED`.

**Validation stage:** `SYNTHETIC_ONLY_SCREEN`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.

</details>

<details>
<summary><code>SUP-009</code> · <code>SRC-038</code> · Saved V5 LightGBM replay on a 196-feature matrix</summary>

**Record type:** representation or model.

**Reported family label:** V5 saved LightGBM transfer screen.

**Question or hypothesis:** Do saved V5 LightGBM models retain their grouped-fold ranking and transfer to a reduced private diagnostic?

**Implementation:** Replayed saved LightGBM V5 models using raw scores from a 196-feature matrix. The published source record does not preserve the model configuration or training source revision.

**Reference / online information:** The source labels the feature matrix as causal, but the public record does not include feature-generation code or an exact package revision. Per-step prefix invariance and package parity are therefore not independently established.

**Tested settings or stage:** Five grouped folds on private competition-derived data and one test_reduced diagnostic; raw scores; 196 features.

**Matched control:** No same-feature or model-matched control is preserved for this transfer audit.

**Causal evidence:** Causality is not independently established from the saved-model aggregate record.

**Evaluation scope:** Five-fold grouped replay plus a reduced-data diagnostic; shared research folds and private inputs.

**Validation labels:** `UNKNOWN_PROVENANCE; POST_SELECTION_CV; CLOUD_PRIVATE; REDUCED_ONLY; CAUSALITY_AUDIT_UNKNOWN`.

**Result and disposition:** Raw five-fold TS-AUC mean 0.5810991 (folds 0.5784017, 0.5818181, 0.5784581, 0.6000968, 0.5667206); test_reduced TS-AUC 0.5052849. Not promoted.

**Limit / reason deprioritized:** The reduced diagnostic was substantially below the fold mean; the saved model, feature pipeline, selection path, and exact causal inference revision are not reproducible from the release record.

**Open question:** Would a source-pinned, prefix-audited V5 model outperform simple controls on an untouched authorized dataset?

**Source evidence:** `SRC-038`.

**Implementation status:** `HISTORICAL_SAVED_MODEL_REPLAY_NOT_SHIPPED`.

**Validation stage:** `FIVE_FOLD_GROUPED_REPLAY_PLUS_REDUCED_DIAGNOSTIC`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.

</details>

<details>
<summary><code>SUP-010</code> · <code>SRC-039;SRC-040</code> · CatBoost fold-0 screen and six-trial tuning</summary>

**Record type:** representation or model.

**Reported family label:** CatBoost on V5 causal feature matrix.

**Question or hypothesis:** Can CatBoost provide a useful tree-model inductive bias on the 196-feature V5 matrix compared with the retained LightGBM direction?

**Implementation:** A fold-0 CatBoost screen used 60 iterations, depth 7, learning rate 0.05, and pair weighting. Separate Optuna and SMAC3 screens ran six trials each on the same 196-feature cache.

**Reference / online information:** The results are held-fold scores only. The reviewed records do not establish per-step inference semantics or full package parity.

**Tested settings or stage:** Frozen ID fold 0; raw score 0.5853518, one memory blend 0.5870524, Optuna best blend_0.60 0.5869706, and SMAC3 best 0.5852159. test_reduced was not evaluated.

**Matched control:** The report cites a retained v19 LightGBM fold-0 reference of approximately 0.6345. This is contextual only: feature and model capacity were not matched.

**Causal evidence:** No independent prefix-invariance or package-parity audit is preserved for this tree model.

**Evaluation scope:** Single-fold private-data screen and small tuning studies; no complete five-fold or reduced-data evaluation.

**Validation labels:** `CLOUD_PRIVATE; PARTIAL_FOLD; POST_SELECTION_CV; CAUSALITY_AUDIT_UNKNOWN`.

**Result and disposition:** All reported CatBoost fold-0 variants were well below the approximately 0.6345 contextual v19 reference. The tested configuration was not promoted.

**Limit / reason deprioritized:** One held fold and six-trial tuner searches do not establish transfer or family-wide weakness; the comparator was not a matched-capacity control.

**Open question:** Would CatBoost add value in a preregistered, source-pinned comparison with identical features, nested selection, and full causal replay?

**Source evidence:** `SRC-039;SRC-040`.

**Implementation status:** `HISTORICAL_RESEARCH_EXPERIMENT_NOT_SHIPPED`.

**Validation stage:** `FOLD_0_SCREEN_WITH_SMALL_TUNING_STUDIES`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.

</details>

<details>
<summary><code>SUP-011</code> · <code>SRC-040</code> · XGBoost fold-0 screen and six-trial tuning</summary>

**Record type:** representation or model.

**Reported family label:** XGBoost on V5 causal feature matrix.

**Question or hypothesis:** Can XGBoost improve the V5 feature-matrix ranking through a different boosted-tree implementation and regularization?

**Implementation:** A 45-round, depth-7 XGBoost model with min_child_weight 100 and pair weighting was screened on the 196-feature matrix; Optuna and SMAC3 each ran six trials.

**Reference / online information:** The results are held-fold scores only. The reviewed record does not establish per-step inference semantics or full package parity.

**Tested settings or stage:** Frozen ID fold 0; best reported blend_0.60 TS-AUC was 0.5895990 for both tuner screens. test_reduced was not evaluated.

**Matched control:** The audit cites a retained v19 LightGBM fold-0 reference of approximately 0.6345. This is contextual only: feature and model capacity were not matched.

**Causal evidence:** No independent prefix-invariance or package-parity audit is preserved for this tree model.

**Evaluation scope:** Single-fold private-data screen and small tuning studies; no complete five-fold or reduced-data evaluation.

**Validation labels:** `CLOUD_PRIVATE; PARTIAL_FOLD; POST_SELECTION_CV; CAUSALITY_AUDIT_UNKNOWN`.

**Result and disposition:** The tested XGBoost configuration scored 0.5895990 on fold 0 and was not promoted.

**Limit / reason deprioritized:** One held fold and six-trial tuner searches do not establish transfer or family-wide weakness; the comparator was not a matched-capacity control.

**Open question:** Would a preregistered XGBoost study with identical feature inputs, nested selection, and exact causal package replay add value?

**Source evidence:** `SRC-040`.

**Implementation status:** `HISTORICAL_RESEARCH_EXPERIMENT_NOT_SHIPPED`.

**Validation stage:** `FOLD_0_SCREEN_WITH_SMALL_TUNING_STUDIES`.

**Final status:** `NOT_PROMOTED_IN_AVAILABLE_RECORD`.

</details>

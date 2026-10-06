# Results and evidence status

## Official competition result

| Competition | Submission / run | Metric | Verified private-evaluation score | Validity label | Final rank |
|---|---|---|---:|---|---|
| ADIA Lab / CrunchDAO Structural Break: Real-Time (2026) | #21 / 120227 | Time-stratified AUC (TS-AUC) | **0.6213427008** | `CLOUD_PRIVATE; VERIFIED_OFFICIAL` | Not independently verified |

The score is linked to a completed provider run and submission record, but the provider did not return an aggregate package digest, so exact serialized-package identity is not established. This submitted system was different from the compact Gaussian AR(1) detector currently exposed as BreakForge's public reference API. The score does not measure that public detector and does not establish performance beyond the competition distribution. No team alias, dataset, labels, series IDs, predictions, or submission bundle is published. Competition data remain subject to the platform's no-redistribution rule; see [competition background and data policy](competition.md).

### Recorded official run outcomes

The following nine provider-linked outcomes retain an unsuccessful package attempt and lower-scoring runs alongside the reported score. The machine-readable index and evidence labels are in [`official_runs.csv`](../reports/curated_results/official_runs.csv).

| Submission | Run | Recorded outcome | TS-AUC | Validity label | Note |
|---|---:|---|---:|---|---|
| #1 | 119852 | Package assembly failure | — | `CLOUD_PRIVATE; OFFICIAL_RUN; PACKAGE_ASSEMBLY_FAILURE; NO_SCORE` | Import failed before inference; repaired submission #2 is listed separately. |
| #2 | 119859 | Completed | 0.6213426077 | `CLOUD_PRIVATE; VERIFIED_OFFICIAL` | Effectively tied with #21; the tiny difference does not establish an improvement. |
| #21 | 120227 | Completed | 0.6213427008 | `CLOUD_PRIVATE; VERIFIED_OFFICIAL` | Highest verified private score among the records summarized here. |
| #3 | 120060 | Completed | 0.6210239249 | `CLOUD_PRIVATE; VERIFIED_OFFICIAL` | Below #2/#21. |
| #28 | 120828 | Completed | 0.6210238431 | `CLOUD_PRIVATE; VERIFIED_OFFICIAL` | Close to #3. |
| #29 | 121939 | Stopped before score | — | `CLOUD_PRIVATE; OFFICIAL_RUN; NO_SCORE` | No private score was returned. |
| #18 | 119641 | Timed out after 3,020 seconds | — | `CLOUD_PRIVATE; OFFICIAL_RUN; NO_SCORE` | No private score was returned. |
| #22 | 117904 | No prediction record | — | `CLOUD_PRIVATE; OFFICIAL_RUN; NO_SCORE` | No private score was available. |
| Unknown | 119099 | Protocol failure | — | `CLOUD_PRIVATE; OFFICIAL_RUN; NO_SCORE` | No private score was returned. |

These results describe one private competition distribution and a small number of submissions. The final rank and team attribution were not independently verified. Per-series predictions and private data remain unavailable and are not redistributed.

This page separates official private-evaluation outcomes, public synthetic evidence, historical competition-derived research, and a one-time holdout audit. Only the synthetic benchmark is reproducible from this repository. Private competition inputs, fold assignments, predictions, and model artifacts are not included.

## Clean, reproducible synthetic benchmark

The fixed benchmark compares three streaming detectors on six generated break mechanisms and an unchanged control. Each process has a 256-observation reference history and a 512-observation stream; the break occurs at stream index 256. Every result below is labeled `SYNTHETIC_ONLY`. Generator, detector implementations, complete per-run metrics, seed, configuration, and code revision are in [`breakforge.validation.synthetic`](../src/breakforge/validation/synthetic.py) and [`synthetic_benchmark.csv`](../reports/synthetic_benchmark.csv).

| Generated mechanism | Raw level CUSUM AUC | Conditional innovation CUSUM AUC | BreakForge reference AUC | BreakForge detection rate | BreakForge median delay | Validity label |
|---|---:|---:|---:|---:|---:|---|
| Mean shift | 1.0000 | 1.0000 | 1.0000 | 0.950 | 22.0 | `SYNTHETIC_ONLY` |
| Variance shift | 0.8406 | 0.9663 | 1.0000 | 0.950 | 33.5 | `SYNTHETIC_ONLY` |
| AR coefficient shift | 0.2844 | 0.2938 | 0.9006 | 0.675 | 150.0 | `SYNTHETIC_ONLY` |
| Persistence reversal | 0.6431 | 0.4806 | 1.0000 | 0.950 | 15.0 | `SYNTHETIC_ONLY` |
| Frequency shift | 0.0175 | 0.0238 | 0.8288 | 0.550 | 168.0 | `SYNTHETIC_ONLY` |
| Heavy-tail shift | 0.4244 | 0.4838 | 0.4781 | 0.075 | 17.0 | `SYNTHETIC_ONLY` |
| No change | — | — | — | 0.025 false-positive rate | — | `SYNTHETIC_ONLY` |

On unchanged evaluation streams, the raw level CUSUM false-positive rate was 0.125 and both conditional detectors had a rate of 0.025. Thresholds were calibrated separately for each detector using the nearest-rank 95th percentile of 80 independent generated null streams. Evaluation used another 40 null streams and 40 streams per changed mechanism. AUC is the pairwise ranking probability of final stream scores against null controls, counting ties as one half. Detection rate counts a trace only if it crosses the calibrated threshold after the known break and had not crossed before it. Delay is the median number of observations after the break among detected traces.

Reproduce the checked-in table with:

```bash
python scripts/synthetic_benchmark.py \
  --seed 20261005 \
  --repetitions 40 \
  --calibration-repetitions 80 \
  --history-length 256 \
  --stream-length 512 \
  --output reports/synthetic_benchmark.csv
```

The checked-in table was regenerated from code revision `326c000` with the public reference configuration (`allowance: 0.25`); all data are synthetic. The CSV records `SYNTHETIC_ONLY` and the Git revision used by the benchmark script. The sample is intentionally small: false-positive rates move in increments of 0.025, uncertainty intervals are not estimated, and each row represents one chosen data-generating process. These results describe implementation behavior, not broad performance or transfer. Other historical synthetic feasibility screens are described in the method catalog; they are not merged into this reproducible benchmark because their code and protocols are not part of the public reproduction path.

## Historical competition-derived research

The complete curated ledger is [`historical_research.csv`](../reports/curated_results/historical_research.csv). It records 54 selected, high, invalid, partial-fold, code-only, and archived protocol-mixed comparisons from the source records summarized for release. It includes fold set and scores when available, reported mean, sample standard deviation computed from the displayed fold values, worst fold, secondary diagnostic, matched control where known, selection status, inference status, private-run outcome, and source evidence label. Missing settings, seeds, or code revisions are explicitly marked unknown instead of being reconstructed.

All numeric outcomes in this section are historical research on private competition-derived data. Each row in the machine-readable ledger carries explicit validity labels; these values are not clean public benchmarks.

### Comparability groups

The `result_group` field keeps the historical records in their original evidence classes. The counts below describe ledger rows, not independent methods. Different model stages or fold-screened candidates may still be incomparable within a group; use each row's metric, folds, control, configuration, and validation labels before comparing values.

| `result_group` | Rows | Evidence represented | Comparison rule |
|---|---:|---|---|
| `causal_reference` | 1 | Locked, exact-stream grouped CV-A reference | Private-data research baseline; not comparable with the official provider score or synthetic benchmark. |
| `historical_cva` | 13 | Historical grouped CV-A experiment records | Compare only when fold set, metric, configuration stage, and selection status match. |
| `selected_cva_head` | 6 | Supervised heads selected or confirmed using CV-A | Treat as post-selection diagnostics; not a clean benchmark. |
| `archived_protocol_mixed` | 30 | Legacy scoreboard rows with mixed or unaudited stream/protocol details | Do not rank against exact-stream or reproducible results. |
| `code_only_historical_cva` | 2 | Code-adjacent full-CV-A result records | Read the row-level selection and causality labels; not independently reproducible here. |
| `code_only_partial_cva` | 2 | Code-adjacent partial-fold screens | Do not interpret as full-fold estimates. |

The synthetic benchmark is published as a separate clean group above. Official provider runs are a separate private-evaluation group in `official_runs.csv`. Neither is pooled with these 54 competition-derived research records.

These are not clean public benchmarks: their source data are private competition data, the raw data and predictions are omitted, and selected research comparisons share folds. The canonical labels used in the result ledgers are:

| Label | Meaning |
|---|---|
| `VERIFIED_OFFICIAL` | A completed official provider run and its reported score were verified. This does not verify the serialized package digest or final rank. |
| `VALID_EXACT_STREAM` | Inference used only the reference and the observed prefix. This does not establish independent fold isolation or model selection. |
| `VALID_CLEAN_CV` | A clean, nested evaluation with isolated groups and no selection on the reported folds. No competition-derived CV score in this release meets this standard. |
| `NON_NESTED_META_CV` | Outer-fold information could flow through a stacked feature or upstream model. |
| `POST_SELECTION_CV` | Reported folds informed repeated model or configuration choices. |
| `INVALID_FUTURE_LENGTH` | A score path used the final, not-yet-observed stream length. |
| `PARTIAL_FOLD` | The evaluation did not cover the planned fold set. |
| `REDUCED_ONLY` | A reduced diagnostic was run; it is not a full evaluation or sealed holdout. |
| `SYNTHETIC_ONLY` | The result uses generated data and supports only the stated synthetic setup. |
| `CLOUD_PRIVATE` | The result depends on private competition data or provider evaluation and cannot be reproduced from this repository. |
| `UNKNOWN_PROVENANCE` | The available record does not establish the evaluation protocol or provenance needed for a stronger label. |

The labels describe different evidence dimensions and can appear together. A causal inference label does not imply an independent CV estimate, and a private official score is not directly comparable to a synthetic benchmark. The CSV ledgers also retain outcome and scope tags such as `OFFICIAL_RUN`, `NO_SCORE`, `FULL_GROUPED_CV_A`, `PACKAGE_PARITY_UNKNOWN`, and `FEATURE_COMPONENT_PARITY_ONLY`; those tags add detail and do not replace the canonical validity labels above.

### Selected causal and post-selection CV-A rows

| Candidate | Five-fold CV-A mean TS-AUC | Reduced diagnostic | Status | Interpretation |
|---|---:|---:|---|---|
| P2 locked causal multiscale reference | 0.630553 | 0.599657 | `VALID_EXACT_STREAM`; grouped CV-A; private data | Locked causal reference; not reproducible without the private inputs and artifacts. |
| Trial 11, history-seeded online kernel CUSUM | 0.634438 | 0.599603 | `VALID_EXACT_STREAM`; `NON_NESTED_META_CV`; `POST_SELECTION_CV` | Exact-package replay; stacked CV artifacts are not an independent outer-fold estimate. Official run #21 is listed above. |
| Trial 52, TNC residual plus temporal/sequential heads | 0.634039 | 0.599747 | `VALID_EXACT_STREAM`; `NON_NESTED_META_CV`; `POST_SELECTION_CV` | Exact-package replay; chained score heads consume fold-specific base predictions. Run #18 timed out without a score. |
| Trial 11 + D3 sequential RFF exact-package replay | 0.634570 | 0.600201 | `VALID_EXACT_STREAM`; `NON_NESTED_META_CV`; `POST_SELECTION_CV` | Exact replay, but folds F0/F4 informed screening and the upstream meta-feature path was not nested. Run #3 completed at 0.6210239 privately. |
| Delay-DMD / Koopman operator-drift blend | 0.635642 | 0.591874 | `VALID_EXACT_STREAM`; `NON_NESTED_META_CV`; `POST_SELECTION_CV` | The head included Trial 11's score; its selected CV mean did not carry to the reduced diagnostic. |
| P3 causal historical-null head, fixed trial 13 | 0.631890 | Not measured | `POST_SELECTION_CV`; F0/F4 informed selection | Fixed trial was confirmed on five folds after the two-fold search; not an independent five-fold estimate. |
| Score-driven AR(1)/GARCH evidence | 0.634768 | 0.598097 | `POST_SELECTION_CV` | Research head; small CV increase did not carry to the reduced diagnostic. |
| Continuous Bayesian-AR context tree | 0.634711 | 0.598650 | `POST_SELECTION_CV` | Similar selected-CV/reduced pattern; not promoted. |
| History-frozen Soft-BCT-inspired gate | 0.634578 | 0.598314 | `POST_SELECTION_CV` | This was not the paper's full variational Soft-BCT method. |
| Monotone GRU, repeated-state BCE | 0.634716 | 0.597635 | `POST_SELECTION_CV` | Research cross-fit only; no full package/private confirmation. |
| Monotone GRU, event/censoring likelihood | 0.634572 | 0.599227 | `POST_SELECTION_CV` | Research cross-fit only; no full package/private confirmation. |
| CRM/RuLSIF blend | 0.636180 | Not measured | `NON_NESTED_META_CV`; `POST_SELECTION_CV` | Upstream meta-features were not independently nested; no reduced, package, or private confirmation. |
| Post-hoc Trial 11 + Candidate 9 + VSBT blend | 0.636313 | Not measured | `NON_NESTED_META_CV`; `POST_SELECTION_CV` | Weights followed CV-A review; upstream stacked predictions were contaminated and no package/private evaluation was run. |
| D3 + CPIT group-balance cross-fit head | 0.634566 | Not measured | `POST_SELECTION_CV`; `NON_NESTED_META_CV` | Cross-fit head only; no complete package replay or private result. |
| D3 + CPIT Trial 19 exact OOF blend | 0.634526 | Not measured | `POST_SELECTION_CV`; `NON_NESTED_META_CV` | OOF blend, not a package replay; F0/F4 informed screening. |
| D3 direct blend with Trial 52 | 0.634292 | Not measured | `POST_SELECTION_CV`; package parity unverified | The selected difference does not establish an independent gain. |

The CSV also retains the complete archived protocol-mixed scoreboard slice rather than only its highest rows. Such rows are marked `UNKNOWN_PROVENANCE; POST_SELECTION_CV` unless a source audit justifies a stronger label. Two known future-length examples are shown separately below. Do not compare protocol-mixed values with the exact-stream rows above.

### Future-length-invalid historical values

These values are preserved because they shaped the research record, but the audited scoring/calibration path used the final online-sequence length. They are not real-time results and must not be ranked against causal methods.

| Historical configuration | CV-A mean TS-AUC | Reduced diagnostic | Status | Why invalid |
|---|---:|---:|---|---|
| P2 historical-null robust-z anchor | 0.6505362 | 0.6409083 | `INVALID_FUTURE_LENGTH` | The null segment length was selected using the complete online-sequence length. |
| P11 nested-weight audit, gamma 5 / eta 0.015 | 0.6504968 | 0.6530942 | `INVALID_FUTURE_LENGTH`; `POST_SELECTION_CV` | An upstream null-profile segment used the final online length; this was one of several tuned settings. |

### Supplemental negative results

Two code-adjacent grouped CV-A records tested BOCPD run-length features and contrastive current/reference window-gap features against the same fixed baseline. Each expert's five-fold mean was lower than its matched baseline, and every tested positive-weight blend also reduced that baseline score. These records are labeled `POST_SELECTION_CV`; their result files do not independently establish prefix-level causality. A dual-reference TNC head was below its Trial-13 control on both screened folds, and a Siamese CNN was near chance on one fold with lower-scoring tested blends. These are configuration-specific negative results, not evidence against their full method families. Their aggregate records and source hashes are in the CSV and evidence table below.

## One-time grouped holdout diagnostics

Four CV-B TS-AUC values were inspected in one grouped-ID audit. They are published in [`holdout_diagnostics.csv`](../reports/curated_results/holdout_diagnostics.csv) with candidate mapping, source hash, and split counts. The contemporaneous access log records no tuning after score inspection. Later metadata and holdout-ID-list exposure means the split is not treated as a sealed final holdout; it must not be used for additional selection or described as a clean final test. The private data are unavailable, so these values cannot be reproduced here.

| Candidate | One-time CV-B TS-AUC | Status |
|---|---:|---|
| Locked P2 baseline | 0.631215137 | `CLOUD_PRIVATE; ONE_TIME_EXPOSED_DIAGNOSTIC` |
| P2 baseline with temporal-memory correction | 0.632359428 | `CLOUD_PRIVATE; ONE_TIME_EXPOSED_DIAGNOSTIC` |
| Trial-13 causal head | 0.621222442 | `CLOUD_PRIVATE; ONE_TIME_EXPOSED_DIAGNOSTIC` |
| Trial-13 head with temporal-memory correction | 0.622432583 | `CLOUD_PRIVATE; ONE_TIME_EXPOSED_DIAGNOSTIC` |

### Late P2+Aux attribution and transfer diagnostic

The late matched-capacity ablation found that the fixed P2+Aux head scored above the Clean Baseline V2 head on the exposed five-fold CV-A comparison. These are aggregate results from private competition-derived data.

| Candidate | CV-A mean TS-AUC | Matched-control CV-A mean | One-time reduced diagnostic | Validity label |
|---|---:|---:|---:|---|
| P2+Aux Arm C (47 inputs; no age) | 0.610056 | 0.5992524 | 0.5135546 | `CLOUD_PRIVATE; POST_SELECTION_CV; FEATURE_COMPONENT_PARITY_ONLY; PACKAGE_PARITY_UNKNOWN; REDUCED_ONLY` |
| P2+Aux Arm D (48 inputs; with age) | 0.6104292 | 0.5992524 | — | `CLOUD_PRIVATE; POST_SELECTION_CV; FEATURE_COMPONENT_PARITY_ONLY; PACKAGE_PARITY_UNKNOWN` |

For Arm D, the paired-ID bootstrap mean delta was +0.0113107 (descriptive 95% interval +0.0073494 to +0.0155046 over 512 resamples; `CLOUD_PRIVATE; POST_SELECTION_CV`). This resampling is conditional on the saved OOF predictions and does not quantify model-selection or training uncertainty. The reduced Arm C value is `REDUCED_ONLY`, not a sealed holdout.

Component-level prefix parity was verified for the 48 feature inputs, but the integrated candidate inference package was not verified. The bootstrap resampled saved predictions and does not account for model search or training uncertainty. The two rows and their exact source evidence are in [`historical_research.csv`](../reports/curated_results/historical_research.csv). The CV lift does not justify promotion: the package-level audit is incomplete and the no-age arm scored below its matched control on the reduced diagnostic.

## Evidence integrity

The source records are not distributed. Their digests identify the evidence used for this summary without exposing private contents or paths. A digest supports provenance bookkeeping; it does not make a private result independently reproducible.

| Evidence label | Record type | SHA-256 |
|---|---|---|
| `SRC-001` | Provider score receipt | `51f99ff26754bc8cbfe5d50cffa406ef1669a9da0628c95d5cb5c229a98fdcc9` |
| `SRC-002` | Provider run readback | `8cb2abe9f081db8792f0c34a4941f567f9f67d4f03dd374f0eb2c4cf73f865a4` |
| `SRC-003` | Historical model and fold summary | `7bb92134e643986f714a517078fef3c3b9349332a612d75afb44d6c839b3fa5c` |
| `SRC-004` | Holdout access log | `867aaf212bc2be830c8861c5fdefbc7e1cf629e09114229229b8fb0b69ad3045` |
| `SRC-005` | Causality and future-length audit | `1026ac95f13d8b0279a037f4aa0163d217fbc5bda99375968f832a5d89786948` |
| `SRC-006` | Historical model scoreboard | `1fd9e2a7bcb43774473aab6c7e890a0ad8a7b905a3af69b99e43bfe208b8ea81` |
| `SRC-007` | Nested OOF validity audit | `2d5e8fc7d85fd27be39e01016ee8579ddea96543c82df50902a835f63ce8f93b` |
| `SRC-008` | Post-hoc blend review | `fc42f8203e9e9904e7f879fffa351010de6862e990d897199dcfb3f38037f4f9` |
| `SRC-009` | Submission #3 / run 120060 audit | `aea3271428d070347f9ce1d13d71b2b4f89a61f4d6faccb1f93b3bcfc071bde2` |
| `SRC-010` | Submission #28 / run 120828 audit | `5bd0da24ac6e40332f531c5d646b8c9ad029aef822613d1d50960ed50cee67b4` |
| `SRC-011` | Submission #29 / run 121939 audit | `d9c9382e34aa5b31eb1b25346bf9ce90c5a3b50de9ecaf65c9f919546b592b93` |
| `SRC-012` | Submission #22 / run 117904 audit | `679b1d0c87737e9586a7ad45e7c8bb5df43b930ab788ff1d4448acc4679e2a67` |
| `SRC-013` | Run 119099 protocol-failure audit | `58242b8623b8762bf7d2950010fb68386da531404c7e44025088d174cd48fe39` |
| `SRC-014` | One-time grouped holdout metrics | `9608c553a2e4d3cca340c8b8ffc5b5cfcbe30eb87d4a9b9efe903b28d1793c84` |
| `SRC-015` | BOCPD run-length result record | `b9ab82eabcfa013fbe91c65c9138b96027c8482282ff43c4d6048d545a9fe1a0` |
| `SRC-016` | Contrastive feature result record | `a5020737f9a70989a0c155a8fbcc55bd58151c48c571de351165f851a65aac04` |
| `SRC-017` | Siamese CNN one-fold result record | `1ccee991f5b93090a31e4e4e80a89e704ad98a69fd2daf918bdb0926e99434f5` |
| `SRC-018` | Synthetic transformation-prediction screen | `04d818e7c9dc5c05f4fc29c047f019b1231b3e51bc770135753c3c1229ba5659` |
| `SRC-019` | Dual-reference encoder head result | `58c43b01441729ff4f102137f6e5934bc0430ebc5ab2194926edae54410eee4e` |
| `SRC-020` | Dual-reference encoder metadata | `94b31b6dee262a41d98eaa40d4b7e7618ac9a518e1bb917fb6271a91fe43a39d` |
| `SRC-021` | Submission #1 package-import failure audit | `d11e7c95f51192aedac4aa99fb314a91a673175a0ca44be4f2f29c6e4f07e23f` |
| `SRC-022` | P2+Aux matched-capacity attribution ablation | `18895f847894e680f6aecc799e157cf5ad335049f9822d37bcef9c4274134d46` |
| `SRC-023` | P2+Aux paired-ID bootstrap comparison | `d14c218b87a7f54cf3e9203c6bbd100bbb91872a4d52c255381e020908dc285f` |
| `SRC-024` | P2+Aux feature-component prefix-parity audit | `2cfb5a770856081836e284b49575d0a07a7944ffcdbf810c6cc3f17c374e1b9c` |
| `SRC-025` | P2+Aux full-fit reduced diagnostic | `6a5ab544b553d4208d54393ce84adbc22fec038bb8d16820da02da8572057ebc` |
| `SRC-026` | Clean Baseline V2 online-age diagnostic | `b23d9851899f2519b718da42dc4654090f32cd0ed8dac061cbcc14509661fd46` |
| `SRC-027` | Clean Baseline V2 history-group diagnostic | `84811a834f7851a37e4484e6cc27b2d46d49e7cf897a72295f5663b8ca188841` |
| `SRC-028` | Historical ACF metric-weight audit | `d5ce26fd01790297920a6bdf9da8f1911ba0dad4d694f0163ca8c30110b7309b` |
| `SRC-029` | History-ACF synthetic Stage-0 | `17fb593a39c1327771cad31e97a10ec79735011e020e2df578332cf0b436a62e` |
| `SRC-030` | Robust-history null matched-control diagnostic | `4ad12d1362199e22289b3035b21ccdbeca6b27f12b7550774cae0d1312cab3a0` |
| `SRC-031` | Break-stream under-detection diagnostic | `94a8a9b6a0dbae8d842e99dab2e11212f681a2c1b737d0f7b3da70746fb660fa` |
| `SRC-032` | Pair-weight and break-age metric audit | `e649132f76ed31315748910a9be776038d57e83b5fdfadac0986771ab8112c25` |
| `SRC-033` | Synthetic break-magnitude screening study | `b90290b81d589c8291c0f3eb645abc242942176b03e8c92c093faad8e971d5f1` |
| `SRC-034` | Synthetic null-growth correction to break-magnitude study | `8db38003b15bd8be22831d7fccc1a46f21691ace34e512df5fb73ceff24ebe41` |
| `SRC-035` | Rosenblatt componentwise null-rank synthetic Stage 0 receipt | `38f6cf13f9813c71ef7d7db79abb3d0e5241b5dbf1ffa194f885bfcb52bd8c2e` |
| `SRC-036` | Rosenblatt total-score null-rank synthetic Stage 0 receipt | `9642333c2d5b647be8a96a43d988eef8d36828880c1f21123319a567be034231` |

See [validation](validation.md) for the leakage postmortems and the [method catalog](method_catalog.md) for experiment-level scope and disposition.

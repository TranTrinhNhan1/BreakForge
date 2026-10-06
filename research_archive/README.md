# Curated research archive

The release includes a [source-indexed inventory of 131 research reports](../reports/experiment_index.csv) and a [curated method and variant catalog](../reports/method_catalog.csv). Its `MTH-*` and `CAT-*` keys were assigned for this release and are not original experiment IDs. The source index records report titles and SHA-256 digests; the method catalog groups staged reports and adds eight supplemental evidence summaries whose reviewed records were outside the report index. The source report text, runtime logs, prediction arrays, model artifacts, and competition data are not distributed. A digest supports source mapping but is not a reproduction package. Method-level and result-level validation labels appear where evidence supports them; other inventory entries remain historical or explicitly unknown.

This archive preserves the scientific conclusions of the broader project
without including raw competition data, predictions, model binaries, logs, or
private working files. The summaries below use stable public evidence labels rather than filesystem locations.

| Evidence label | Research question | Status / validity | Public account | Key lesson |
|---|---|---|---|---|
| `VAL-01` | Can a streaming score use the final unseen sequence length? | Affected historical results: `INVALID_FUTURE_LENGTH`; prefix-only implementations: `VALID_EXACT_STREAM` only where separately verified. | [Validation](../docs/validation.md), [research journey](../docs/research_journey.md) | The final horizon cannot choose a feature, null, calibration rule, or threshold. |
| `VAL-02` | Can held-out groups flow through upstream stacked models? | Historical stacked estimates include `NON_NESTED_META_CV`. | [Validation](../docs/validation.md) | Every fit in an evaluation dependency graph must exclude the outer held-out group. |
| `VAL-03` | Were candidate choices made on the same folds later reported? | Some estimates are `POST_SELECTION_CV` or `PARTIAL_FOLD`; they are not clean benchmarks. | [Validation](../docs/validation.md), [failed experiments](../docs/failed_experiments.md) | Repeated selection and incomplete fold coverage reduce the meaning of a score. |
| `MTH-01` | Does conditional normalization help compare heterogeneous streams? | Investigated; public core contains a small Gaussian AR(1) PIT illustration. | [Methodology](../docs/methodology.md), [method catalog](../docs/method_catalog.md), [references](../docs/references.md) | A PIT inherits the conditional model's misspecification and dependence limits. |
| `MTH-02` | How can evidence accumulate online? | Multiple sequential families investigated; the public CUSUM score is uncalibrated. | [Methodology](../docs/methodology.md), [failed experiments](../docs/failed_experiments.md) | Evidence accumulation is distinct from a calibrated false-alarm guarantee. |
| `MTH-03` | Did richer features improve on simple matched controls? | Selected comparisons were informative but selection-exposed; no universal family claim is made. | [Method catalog](../docs/method_catalog.md), [failed experiments](../docs/failed_experiments.md) | Hold window, scaling, and feature budget fixed before attributing gains to representation. |
| `MTH-04` | Do dynamics, frequency, and path representations transfer? | Tested configurations only; no family-wide rejection. | [Method catalog](../docs/method_catalog.md), [failed experiments](../docs/failed_experiments.md), [references](../docs/references.md) | Embedding, rank, window, scaling, and noise choices can dominate apparent effects. |
| `MTH-05` | Do learned or pretrained representations transfer to break detection? | Incompletely reproduced; not part of the public reference implementation. | [Research journey](../docs/research_journey.md), [method catalog](../docs/method_catalog.md), [failed experiments](../docs/failed_experiments.md) | Forecasting or pretraining performance alone does not establish detection transfer. |
| `DATA-01` | Can the historical challenge data be redistributed? | Excluded; platform guidance prohibits sharing the competition dataset. | [Competition notes](../docs/competition.md) | The synthetic examples keep the package usable without restricted data. |
| `RUN-01` (`SRC-021`) | Why did the first recorded cloud attempt fail? | `CLOUD_PRIVATE; OFFICIAL_RUN; PACKAGE_ASSEMBLY_FAILURE; NO_SCORE`. | [Results](../docs/results.md) | The attempt failed before inference because of package assembly; the repaired run is a separate record. |
| `AUX-01` (`SRC-022`–`SRC-025`) | Do matched P2+Aux features add to the Clean Baseline V2 head? | `CLOUD_PRIVATE; POST_SELECTION_CV; FEATURE_COMPONENT_PARITY_ONLY; PACKAGE_PARITY_UNKNOWN; REDUCED_ONLY` where applicable. | [Results](../docs/results.md), [failed experiments](../docs/failed_experiments.md) | A CV-A lift and a weaker reduced diagnostic do not justify promotion without integrated inference parity. |
| `ACF-01` (`SRC-026`–`SRC-029`) | Do online-age or historical-ACF partitions support a new detector feature? | `CLOUD_PRIVATE; DESCRIPTIVE_OOF_DIAGNOSTIC` for subgroup audits; `SYNTHETIC_STAGE0_HELD_SEED` for the fixed ACF recipe. | [Failed experiments](../docs/failed_experiments.md), [research journey](../docs/research_journey.md) | Subgroup gaps did not explain a mechanism; the static ACF recipe failed a preregistered group condition. |
| `NULL-01` (`SRC-030`–`SRC-031`) | Does robust history-null calibration fix under-detection? | `SYNTHETIC_STAGE0; MATCHED_CONTROL` and `CLOUD_PRIVATE; OOF_DIAGNOSTIC`. | [Failed experiments](../docs/failed_experiments.md) | The tested robust correction failed its matched-control gate, and the under-detection claim was not supported. |
| `SNR-01` (`SRC-032`–`SRC-034`) | Does weak break-age ranking establish a hard signal ceiling? | `CLOUD_PRIVATE; EXPLORATORY_METRIC_AUDIT` and `SYNTHETIC_STAGE0; PRIVATE_BREAK_MAGNITUDE_DIAGNOSTIC; INTERPRETATION_CORRECTED`. | [Failed experiments](../docs/failed_experiments.md), [research journey](../docs/research_journey.md) | The threshold-based ceiling reading was downgraded after raw null scores rose with stream age. |
| `RANK-01` (`SRC-035`–`SRC-036`) | Can history-only ranks calibrate component or integrated Rosenblatt evidence? | `SYNTHETIC_ONLY; SYNTHETIC_STAGE0; FROZEN_GATE_FAILED`; prefix and deterministic checks passed, but overlap exchangeability and sequential validity were not established. | [Method catalog](../docs/method_catalog.md), [failed experiments](../docs/failed_experiments.md) | Neither tested rank-calibration recipe passed its frozen advancement gate; the ranks are not claimed as valid p-values or e-values. |

## Validity labels

- `VALID_EXACT_STREAM` describes prefix-only inference; it does not establish
  independent training folds or generalization.
- `INVALID_FUTURE_LENGTH` marks inference or calibration that used the final
  unseen stream length.
- `NON_NESTED_META_CV` marks outer-fold information that could reach an
  upstream representation or stacked feature.
- `POST_SELECTION_CV` marks results used during repeated candidate selection.
- `PARTIAL_FOLD` marks incomplete planned evaluation coverage.
- `UNKNOWN` or `UNKNOWN_FROM_PUBLIC_INDEX` means the available provenance or
  rights do not support a stronger claim.

The curated public account is in [the research journey](../docs/research_journey.md)
and [failed experiments](../docs/failed_experiments.md). Raw research artifacts
remain outside this public archive.

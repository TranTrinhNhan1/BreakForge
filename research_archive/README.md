# Curated research archive

The release includes a [source-indexed inventory of 131 research reports](../reports/experiment_index.csv) and a [curated method and variant catalog](../reports/method_catalog.csv). Its `MTH-*` and `CAT-*` keys were assigned for this release and are not original experiment IDs. The source index records report titles and SHA-256 digests; the method catalog groups staged reports and adds five supplemental experiment summaries whose reviewed evidence was outside the report index. The source report text, runtime logs, prediction arrays, model artifacts, and competition data are not distributed. A digest supports source mapping but is not a reproduction package. Validity labels apply only where explicitly documented in [the result tables](../docs/results.md); other inventory entries remain historical and unassessed.

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

## Validity labels

- `VALID_EXACT_STREAM` describes prefix-only inference; it does not establish
  independent training folds or generalization.
- `INVALID_FUTURE_LENGTH` marks inference or calibration that used the final
  unseen stream length.
- `NON_NESTED_META_CV` marks outer-fold information that could reach an
  upstream representation or stacked feature.
- `POST_SELECTION_CV` marks results used during repeated candidate selection.
- `PARTIAL_FOLD` marks incomplete planned evaluation coverage.
- `UNKNOWN` means the available provenance or rights do not support a stronger
  claim.

The curated public account is in [the research journey](../docs/research_journey.md)
and [failed experiments](../docs/failed_experiments.md). Raw research artifacts
remain outside this public archive.

# Historical score inventory

[`experiment_score_inventory.csv`](../reports/curated_results/experiment_score_inventory.csv) lists all 111 experiment records in a local structured research ledger. It is a source inventory, not a benchmark table. Keep it separate from the 57-row curated comparison ledger in [`historical_research.csv`](../reports/curated_results/historical_research.csv).

The original ledger is not included. It contains local artifact paths and has inconsistent CSV field counts caused by unescaped commas. The public inventory keeps the experiment IDs, broad model families, source row order, score fields that can be recovered, and flags for records that need further review. Local paths, artifact pointers, fold hashes, and code commit IDs are omitted.

## What was recovered

- **80 five-score vectors** have recorded mean, population standard deviation, and worst score that agree with the five values to within `2e-5`.
- **8 five-score vectors** have one or more recorded summary values that disagree with those checks. Their source values are retained as recorded and marked `FIVE_FOLD_SUMMARY_MISMATCH`; they have not been repaired.
- **23 records** contain only partial or ambiguous score evidence. Distinct score-like values are listed without assigning them to folds or treating them as cross-validation results.
- **18 source rows** have a different field count from the 29-column header.
- **4 full score vectors** exactly match a vector in the curated ledger after rounding both vectors to six decimal places. This identifies exact numeric overlap only; other records may describe the same experiment without an exact match.

The consistency checks are simple arithmetic checks, not validation of the evaluation design. All rows have `validation_protocol=NOT_RECONSTRUCTED` and `benchmark_eligible=NO`. In particular, these checks do not establish exact-stream inference, fold isolation, nested out-of-fold independence, absence of future information, or a sealed holdout.

## Reading the CSV

`five_score_values_in_source_order` contains five values when a complete vector was recovered. It preserves the source order; the row does not independently verify which fold each position represents. `recorded_cv_mean`, `recorded_cv_std`, `recorded_cv_worst`, and `recorded_robust_cv` preserve the adjacent summary fields used for the consistency check.

For partial records, `partial_score_values_unassigned` contains distinct numeric values found in the score area. It intentionally carries no fold labels. Do not compare those values with five-fold means or use them to rank methods.

The source table does not retain enough information to reconstruct configurations, seeds, code revisions, data provenance, or the validation protocol for every row. The inventory therefore preserves the existence and score evidence of the experiments without presenting them as reproducible results. The curated ledger remains the place to compare historical outcomes with explicit evidence and validity labels.

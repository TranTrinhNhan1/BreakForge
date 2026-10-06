# Historical score inventory

[`experiment_score_inventory.csv`](../reports/curated_results/experiment_score_inventory.csv) lists all 111 experiment records in a local structured research ledger. It is a source inventory, not a benchmark table. Keep it separate from the 57-row curated comparison ledger in [`historical_research.csv`](../reports/curated_results/historical_research.csv).

The original ledger is not included. It has inconsistent CSV field counts caused by unescaped commas and includes artifact pointers that cannot be resolved from this release. The public inventory keeps experiment IDs, broad model families, source row order, recoverable score fields, and flags for records that need further review. Artifact pointers, fold hashes, and source code commit IDs are omitted.

Every inventory row cites `SRC-041` and carries a label from the result-validity taxonomy. Full and summary-mismatch records are labeled `CLOUD_PRIVATE;UNKNOWN_PROVENANCE`; partial or ambiguous records also carry `PARTIAL_FOLD`. These labels keep private-data dependence and unknown evaluation design visible even where source arithmetic is consistent.

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

The score table alone does not retain enough information to reconstruct configurations, seeds, code revisions, or validation protocols for every row. A separate [run-variant crosswalk](../reports/curated_results/run_variant_crosswalk.csv) joins all 111 experiment IDs to their recorded hypotheses, feature blocks, hyperparameters, postprocessing, and source run group. It provides six direct catalog links, five related-family links, and explicitly leaves 85 groups without a verified method-catalog mapping. This metadata crosswalk does not resolve the evaluation protocol or make any score benchmark-eligible.

`SRC-041` is the SHA-256 digest of the withheld structured source ledger. It supports source identification only; the raw file is not distributed because it contains machine-local artifact references and malformed rows.

The [grouped model-family appendix](../reports/curated_results/source_model_family_inventory.csv) aggregates the 111 records into 30 labels and retains the arithmetic-status counts. The [96-group appendix](../reports/curated_results/run_variant_groups.csv) adds the exact feature-block grouping rule and catalog-link status. The groups organize source runs; they are not counts of distinct methods. The 19 supplemental report-result rows are separately labeled in [`additional_report_results.csv`](../reports/curated_results/additional_report_results.csv) and are not folded into the 57-row curated comparison ledger.

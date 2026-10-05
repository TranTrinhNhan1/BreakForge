# Research workflow

This project treats a detector as a scientific hypothesis that must survive
causal, statistical, and reproducibility checks.

## Record each experiment

Before running a comparison, record:

- the hypothesis and the signal the method is intended to detect;
- the complete causal input set available at each update;
- the model, representation, window, calibration, and sequential state;
- fixed seeds, data provenance, code revision, and metric definition;
- the matched baseline and the validation split used for selection.

Keep tuning and confirmation separate. If a result influences a design choice,
record that selection and do not describe the same score as an untouched
estimate. A held-out group must be excluded from every upstream fit that can
affect its prediction, including representations and stacked features.

## Review the inference path

Replay observations in order and check that scores for an observed prefix are
unchanged when later observations differ. Compare batch and streaming paths if
both exist. Reset detector state between independent series and verify that a
fixed seed and input produce repeatable output.

## Report evidence and failures

Publish enough metadata to interpret a result: experiment identifier, method
variant, validation class, fold coverage, selection status, metric, and a
source artifact or immutable digest. Keep competition data, predictions, and
other restricted files out of the repository. When provenance or rights are
unclear, label them `UNKNOWN` and omit unsupported numeric claims.

Use matched controls that keep windows, normalization, and feature budgets
comparable. A complex representation earns credit only for an incremental
effect that survives that control. Preserve negative and inconclusive results
with the same care as selected methods.

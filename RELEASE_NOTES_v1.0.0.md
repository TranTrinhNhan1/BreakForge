# BreakForge v1.0.0 — Post-Competition Research Release

BreakForge presents a compact, causal streaming reference implementation and a curated account of research into structural-break detection in heterogeneous univariate time series.

## Highlights

- A resettable, deterministic CPU detector with a fitted Gaussian AR(1) reference, conditional standardized innovations, optional Gaussian PIT values, and sequential CUSUM evidence.
- A synthetic AR-break demonstration and seeded benchmark that require no competition data or Crunch runtime.
- Exact-stream, suffix-invariance, reset, replay-parity, determinism, and fold-isolation validation utilities and tests.
- A 137-record method/evidence catalog, an index of all 131 research reports and their digests, research journey, matched-control discussion, and curated failed/inconclusive experiments.
- Late P2+Aux matched-capacity findings, package-parity limitations, the failed first package-import attempt, and corrections to the ACF, robust-null, and break-magnitude diagnostics.
- Separate reporting for synthetic reproducible results, official private-run outcomes, and historical CV results with `INVALID_FUTURE_LENGTH`, `NON_NESTED_META_CV`, `POST_SELECTION_CV`, and `PARTIAL_FOLD` labels.
- Primary-source references and an MIT-licensed, installable Python package.

## Results and limitations

The official score reported in this repository is a private competition metric from a system distinct from the public reference API. The final rank is not independently verified. It is not a public benchmark and does not establish generalization. No competition data, labels, per-series outputs, or submission bundle are included.

No competition-derived CV result in this release qualifies as a clean independent benchmark. Historical scores remain available with their validation limitations, including future-length leakage and nested-OOF contamination. The synthetic benchmark is small and covers selected data-generating processes; the public CUSUM score is uncalibrated and does not provide a false-alarm guarantee.

## Install and reproduce

```bash
pip install -e .
python examples/synthetic_break_demo.py

pip install -e '.[dev]'
pytest -q
python scripts/synthetic_benchmark.py \
  --seed 20261005 \
  --repetitions 40 \
  --calibration-repetitions 80 \
  --history-length 256 \
  --stream-length 512 \
  --output reports/synthetic_benchmark.csv
```

Competition evaluation requires user-supplied data and authorization. The public synthetic workflow does not require competition access.

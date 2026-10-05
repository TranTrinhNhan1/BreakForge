# Public Release Audit

**Audit date:** 2026-10-06 (Asia/Bangkok)

**Audited branch and commit:** `main`, `30a1763` (`docs(references): use accessible institutional record`)
**Repository:** [TranTrinhNhan1/BreakForge](https://github.com/TranTrinhNhan1/BreakForge)

## Release status

The public source tree installs and its local smoke checks pass. This audit does **not** certify a final `v1.0.0` release yet: the GitHub Actions run for the audited commit was queued when checked, and the existing `v1.0.0` tag points to an earlier commit (`ff0625f`). No GitHub Release object exists for that tag. The tag has not been moved.

GitHub's [active Actions incident](https://www.githubstatus.com/incidents/3q1yb5m7ltvb) reports delays assigning GitHub-hosted runners, matching the queued runs observed here. The incident update at 2026-10-05 19:50 UTC said GitHub was still investigating. This explains the current CI delay; it is not evidence of a project test failure.

## Security and data

- Scanned 127 Git blobs reachable from the public clone's fetched branches and tags. The scan found no credential-pattern matches, sensitive-name candidates, restricted-data/model/archive file extensions, or blobs larger than 5 MB. The largest blob was the curated method catalog (201,213 bytes).
- Reviewed the current public tree: it contains curated source, configuration, documentation, synthetic results, and aggregate historical summaries. No CrunchDAO competition datasets, per-series labels or predictions, model weights, or submission bundles are tracked.
- Private research workspaces and raw competition artifacts are outside this public clone and were not included in the publication. Competition-specific reproduction requires authorized user-supplied data.
- The repository uses the MIT License. The public core was reviewed for copied or vendored code; no unresolved incompatible component was identified.

These checks cover recognizable credential formats and the Git objects available in the public clone. They do not prove the absence of every possible undisclosed secret format.

## Installation and verification

From a new HTTPS clone at `30a1763`:

| Check | Result |
|---|---|
| `pip install -e ".[dev]"` | Passed on Python 3.14.4 |
| Package import (`StructuralBreakDetector`, `CausalGaussianAR1PIT`) | Passed |
| `python -m pytest -q` | **14 passed** |
| `python examples/synthetic_break_demo.py` | Passed; score increased after the planted break |
| `python scripts/synthetic_benchmark.py --repetitions 2 --calibration-repetitions 4 ...` | Passed; wrote 21 synthetic benchmark rows |
| `cffconvert --validate` | Passed; Citation File Format 1.2.0 |
| Internal Markdown links | 98 targets passed before this audit file was added |
| README Mermaid architecture diagram | Parsed successfully with Mermaid 12.1.0 |

The current GitHub Actions run is [queued](https://github.com/TranTrinhNhan1/BreakForge/actions). A complete Python 3.10, 3.11, and 3.12 matrix passed on `ff0625f`, before the latest documentation-only commits. Three subsequent runs ended with queued matrix jobs cancelled; the jobs that ran completed successfully. No test-step failure was reported in those runs. The latest commit's workflow result must be checked before tagging a release.

The README and reference-list external links were checked separately. Publisher and DOI hosts may return HTTP 403 to automated requests; this is not treated as a broken citation when an authoritative page resolves. The older Statistica Sinica page had a TLS validation failure in this environment and was replaced by a Lund University publication record, which returned HTTP 200.

## Results and scientific limitations

- The reproducible benchmark in this repository is synthetic and covers selected change mechanisms. It is a smoke-testable comparison, not evidence of general performance across heterogeneous real-world series.
- The reported official competition score is a private provider result; the final rank was not independently verified. Competition data and predictions are not redistributed.
- Historical competition-derived results are not a clean independent benchmark. The documentation labels future-length leakage, non-nested meta-CV, post-selection, partial-fold, and unknown-protocol results separately.
- The public AR(1)-PIT/CUSUM reference score is uncalibrated evidence, not a probability or false-alarm guarantee. PIT and Gaussian-score interpretations depend on the quality of the conditional model and its assumptions.
- The method catalog is a curated index, not a reconstruction of every experiment. Missing configurations, matched controls, seeds, or validation details remain marked unknown where the public evidence does not support a claim.

## Remaining release actions

1. Confirm the latest GitHub Actions matrix finishes successfully on Python 3.10, 3.11, and 3.12.
2. Review the difference between `main` and the existing `v1.0.0` tag before any final tag or release action. The tag has not been rewritten.
3. Only after those checks, prepare the GitHub Release from the reviewed commit and verify the published release notes.

Suggested GitHub description: **Research framework for causal structural-break detection in heterogeneous univariate time series.**

Suggested topics: `time-series`, `change-point-detection`, `structural-break`, `sequential-analysis`, `streaming`, `statistical-learning`.

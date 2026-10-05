# Competition background and data policy

The project's research originated in work around ADIA Lab and CrunchDAO structural-break tasks, but two related editions had different evaluation interfaces.

- The [2025 ADIA Lab Structural Break Challenge documentation](https://docs.crunchdao.com/competitions/competitions/adia-lab-structural-break-challenge) describes a batch decision with both segments available together.
- The separate [Structural Break: Real-Time edition](https://forum.crunchdao.com/t/2026-w40-closing-of-structural-break-real-time/1222) used streaming inference and was reported closed on 2026-10-02.

The public library focuses on the broader real-time research problem. At time `t`, its prediction uses the fitted reference and stream prefix through `x_t`; it does not depend on future observations or the final sequence length.

## Leakage and evaluation status

In its [June 2026 leaderboard clarification](https://forum.crunchdao.com/t/leaderboard-comparability-after-the-june-8-real-time-data-access-fix-were-pre-fix-scores-rescored/1188), CrunchDAO staff said evaluations before the June 8 data-access fix were invalidated and excluded from the leaderboard because the pre-fix interface allowed information about the online segment length. This project labels affected historical paths `INVALID_FUTURE_LENGTH` and does not present them as valid results.

## Data and results

CrunchDAO's [data-sharing clarification](https://forum.crunchdao.com/t/sharing-finding/1095) says competition data must not be shared outside the platform. This repository therefore contains no train/test data, labels, fold maps, cached copies, raw OOF predictions, or competition-derived model artifacts. Any future competition-specific adapter must operate on data supplied by a user who is authorized to use it.

No private score, rank, run ID, or submission artifact is included in this release draft. They will be added only after official verification, publication-rights review, and a clear validity classification. Local competition data and result files are intentionally excluded from Git.

## Reproducing research without platform data

The synthetic example demonstrates the reference model and exact streaming mechanics without any CrunchDAO runtime or data. It is not a substitute benchmark and does not support a claim about competition performance or distributional transfer. A clean competition benchmark cannot currently be reconstructed from public files in this repository.

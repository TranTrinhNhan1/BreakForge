# Methods investigated and experiments deprioritized

This is a curated summary of research families, not a claim that each family has been disproven. A result about one implementation, window, dataset, or tuning budget does not establish that an entire method class fails. Historical quantitative results are omitted where validation independence, private-data rights, or reproducible provenance are unresolved.

| Family | Hypothesis | What was explored | Control and observed lesson | Status / unresolved question |
|---|---|---|---|---|
| Rolling statistics | Local changes in mean, variance, quantiles, or autocorrelation expose breaks. | Windowed moments and contrasts at multiple horizons. | Compare with fewer moments on the same windows; windowing alone can account for apparent gains. | Retain as a useful baseline family. No universal window or clean cross-domain benchmark was established. |
| Spectral features | A change in periodicity or frequency content can reveal a regime transition. | Compact spectral summaries and windowed frequency comparisons. | Compare with time-domain moments under the same window and normalization. | Tested configurations were not selected for the compact reference API. This does not rule out spectral methods for periodic domains. |
| Koopman / DMD | Local transition operators or modes change when system dynamics change. | Windowed DMD/Koopman-inspired summaries and parameter variants. | Match window, dimensionality, and normalization against low-order features. | Sensitive to rank, embedding, and noise. No robust advantage was established across the historical heterogeneous task. |
| Signatures / rough paths | Ordered path interactions add information beyond unordered moments. | Truncated sequential representations and related path summaries. | Compare identical windows with low-order statistics and matched feature budgets. | More costly and tuning-sensitive; tested configurations did not justify the public baseline. Broader applications remain open. |
| Conformal methods | Online nonconformity or e-values can provide distribution-robust change evidence. | Conformal scores and martingale-style accumulation. | Match the base nonconformity model and carefully specify exchangeability assumptions. | Validity assumptions and dependence handling require care; explored configurations were not a complete, calibrated reference detector. |
| Sequential detectors | Accumulating small deviations can improve detection over isolated windows. | CUSUM-like, likelihood-ratio, and martingale evidence. | Compare to the same per-step inputs and calibrate false alarms/delay under the target protocol. | The public baseline includes simple CUSUM channels. It does not claim controlled false-alarm performance. |
| Representation learning | A learned embedding can transfer change-relevant structure across series. | Supervised and self-supervised representations, including pretrained time-series models. | Compare with simple feature controls and audit pretraining overlap, model version, and domain shift. | Cost and transfer evidence were not sufficient for the lightweight public reference. Generalization remains unresolved. |
| Foundation models | Broad pretraining can provide useful forecasts or representations without per-series labels. | Forecast-derived residuals and pretrained representations were considered. | Compare to lightweight conditional models on the same information set; verify pretraining provenance. | Not reproduced as a public dependency or clean benchmark. Forecasting quality alone does not establish break-detection quality. |
| Bayesian methods | Posterior run-length or model evidence can represent uncertainty about a break. | Online Bayesian and change-hypothesis formulations. | Compare prior/hazard sensitivity and computational cost against sequential baselines. | Useful framework, but prior sensitivity and implementation breadth prevented a single validated public reference here. |
| Density ratios | Pre/post predictive ratios can expose distribution changes. | Ratio-style comparisons and learned density evidence. | Use matched window splits and inspect ratio calibration and sample reuse. | Sensitive to training split and calibration; no fully nested, clean public result is available. |
| Optimal transport | Distributional distances can detect broad changes without a parametric density. | Wasserstein/transport-inspired comparisons were investigated. | Compare equal windows and sample counts against simpler distribution summaries. | Computation and window dependence remain concerns; no preferred public configuration was established. |
| Metaheuristics | Automated search may find useful feature or detector combinations. | Search and optimization over configurations. | Reserve nested/sealed validation for selection; account for every trial. | Search increases post-selection bias unless validation is nested. Some historical CV comparisons are `POST_SELECTION_CV`. |

## Why matched controls matter

Suppose a path signature or DMD feature outperforms a baseline built on a different window, scaling rule, feature count, or preprocessing path. That difference does not isolate the proposed method. A matched control keeps those choices fixed and replaces only the sophisticated representation with an appropriate simple alternative, such as low-order moments on the same windows. If the gain disappears, the complex representation has not shown incremental value under that protocol.

An internal matched comparison found limited incremental value for one richer representation relative to a low-order feature control, but the supporting CV process was selection-exposed. It is therefore a qualitative research lesson, not a clean public performance claim. The raw scores and private dataset identifiers are not published here.

## Interpretation policy

- “Underperformed” means the tested configuration did not earn a place in the reference implementation under the available protocol.
- “Disproven” would require a much broader theorem or empirical program; this document does not use that label for these families.
- A historical score affected by `INVALID_FUTURE_LENGTH`, `NON_NESTED_META_CV`, `POST_SELECTION_CV`, or `PARTIAL_FOLD` is not a clean benchmark.
- A method family can remain scientifically interesting even when the experiments here were inconclusive.

See [validation](validation.md) for the labels and [research archive](../research_archive/README.md) for the source-audit index.

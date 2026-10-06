# Research journey

The project began with the ADIA Lab / CrunchDAO structural-break problem and expanded into a broader investigation of causal inference for heterogeneous univariate streams. The competition motivated the constraints; the useful outcome is the record of methods, controls, and validation lessons.

## 1. Statistical baseline

The first experiments used compact statistical summaries and simple change evidence. These established a transparent reference point and made it possible to separate changes in location, scale, and dependence.

## 2. Rolling features

Rolling moments, quantiles, and local contrasts were explored because they are easy to compute online. They remain useful diagnostics, but window length and reference behavior matter. Several feature expansions were compared against simpler controls rather than assumed to add value because they were more elaborate.

## 3. Early high local scores

Some early local evaluation runs produced encouraging scores. The project later learned that a strong local number is not sufficient evidence: the inference protocol, fold dependencies, result selection, and data version all affect what the number means.

## 4. Future-length leakage discovery

An audit separated harmless use of an already available input container's length from use of the final, unseen online-segment length to choose null or calibration behavior. The latter violates real-time causality. Those results were reclassified as `INVALID_FUTURE_LENGTH`. This became a direct design constraint for the public `update(x)` API.

## 5. Exact-stream rebuild

The inference path was rebuilt around a prefix-only contract: at time `t`, use the reference and values through `x_t`. Exact replay and suffix-invariance checks were treated as first-class tests. Exact-stream inference validates the prediction path, though it does not by itself validate how a stacked model was trained.

## 6. Conditional and Rosenblatt-style normalization

Conditional prediction and probability integral transforms offered a common representation for heterogeneous series: compare each new observation with its conditional reference distribution, then analyze its normalized innovation. This can simplify downstream detection when the conditional model is adequate. It can fail when that model is misspecified, parameters drift, or dependence remains after transformation. The current public implementation exposes a deliberately small Gaussian AR(1) instance.

## 7. Sequential detection

CUSUM-like and other sequential evidence methods were investigated to accumulate weak changes as data arrive. A sequential score can be useful without being a calibrated probability. Thresholds, false-alarm rates, and detection delays require protocol-specific calibration and should not be inferred from an uncalibrated score trace.

## 8. Dynamics, Koopman, and DMD

Local dynamical summaries and DMD/Koopman-inspired features were explored to detect changes in transition behavior. These methods are sensitive to embedding, window, scaling, rank, and noise choices. Comparisons against matched low-order statistics are important before attributing gains to a richer dynamics representation.

## 9. Representation learning

Learned representations, including pretrained time-series models, were investigated as candidate ways to transfer useful structure across series. They introduce additional questions: pretraining data overlap, domain shift, model version, compute cost, and whether forecasting representations support this detection objective. These experiments did not establish a generally transferable detector.

## 10. Matched controls

The project compared some sophisticated representations to controls using the same windows and comparable low-order moments. A complex method is informative only when its apparent gain survives a control that captures windowing, normalization, parameter count, and evaluation choices. Internal comparisons were also subject to selection bias, so numerical claims are withheld unless their evidence can be reconstructed and published.

## 11. Nested-OOF audit

An evaluation-DAG review found that outer validation information could flow into upstream fitted representations used to generate inner OOF features for a meta-model. This is a separate problem from future-length leakage and from test-time causality. A detector can be exact-stream causal and still have contaminated CV. Historical stacked evaluations affected by this path are labeled `NON_NESTED_META_CV`.

## 12. Private-transfer lessons

The challenge used heterogeneous, private competition data. That is not a substitute for broad evidence on public deployment distributions. The dataset cannot be included in this repository, and a faithful clean benchmark replay is unavailable from the checked-in public artifacts. Transfer claims are therefore limited; synthetic examples demonstrate mechanics, not external validity.

## 13. Late-cycle matched controls and corrections

The final matched-capacity P2+Aux ablation showed a selected CV-A lift over the Clean Baseline V2 head. A paired-ID bootstrap described uncertainty conditional on saved OOF predictions, but did not remove prior fold exposure. The no-age version fell below its control on one reduced-only diagnostic, and full integrated inference parity remained open. Those results stay `CLOUD_PRIVATE; POST_SELECTION_CV` and were not promoted.

Separate audits clarified several misleading patterns. A static history-ACF feature failed one preregistered synthetic group condition and was closed as a fixed recipe (`SYNTHETIC_STAGE0_HELD_SEED`). A robust-history-null correction failed its matched-control gate, and the associated under-detection claim was not supported. Metric-weight analysis showed why online-age subgroup AUC should not be treated as a direct measure of score contribution. A synthetic break-magnitude screen also needed correction: a raw maximum score rose with stream age under null, so its threshold-based “ceiling” interpretation was downgraded. These are specific diagnostics, not universal conclusions about their method families.

Two history-only rank-calibration variants were also screened on synthetic Rosenblatt streams. Componentwise rank-then-mixture missed its frozen effect-size gate, while the post-mixture rank map did not beat the raw score on the tested heavy-tail mechanism. Prefix invariance passed, but overlapping calibration windows did not justify conformal or sequential-validity claims. Both recipes were closed without challenge-data evaluation.

## 14. Post-competition cleanup

The public release extracts a small, deterministic, CPU-only reference implementation and its regression tests. Detailed source reports and raw artifacts are not included; selected lessons are summarized without publishing restricted data or scores presented without their validity limits. The resulting repository is intended to be a starting point for reproducible work, not a claim that the competition produced a universally superior detector.

For method-by-method scope and controls, see [failed experiments](failed_experiments.md). For validation labels and protocols, see [validation](validation.md).

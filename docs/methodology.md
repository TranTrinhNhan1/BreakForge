# Methodology

## Reference and online phases

The reference implementation separates a fixed reference fit from sequential inference:

1. `fit(history)` estimates one Gaussian AR(1) reference from a finite historical segment.
2. Each `update(x_t)` predicts the arriving value from the last observed value and the frozen reference parameters.
3. The update returns a running evidence score after consuming `x_t`.

No online observation changes the fitted mean, autoregressive coefficient, or residual scale. `reset()` clears the sequential evidence and restores the last value of the fitted history as the stream start. Call `fit()` again to establish a different reference.

## Conditional innovation and PIT

For reference observations with mean estimate `mu`, lag coefficient `phi`, and residual scale `sigma`, the one-step conditional model is

```text
x_t | x_(t-1) ~ Normal(mu + phi * (x_(t-1) - mu), sigma^2)
e_t          = x_t - [mu + phi * (x_(t-1) - mu)]
z_t          = e_t / sigma
u_t          = Phi(z_t)
```

`u_t` is the conditional probability integral transform (PIT). Under the correctly specified continuous conditional distribution, the sequential conditional transforms have the uniformity properties associated with the Rosenblatt transform. This implementation uses a fitted Gaussian AR(1) approximation; it does not establish that the model is correct for an arbitrary series. Serial dependence, heavy tails, time-varying parameters, outliers, or a poor reference fit can leave the transformed values dependent or non-uniform.

The Gaussian score `z_t = Phi^-1(u_t)` is the standardized innovation already computed by the model. Extreme PIT values are clipped numerically before being returned. This protects the representation from exact zero and one; it is not a statistical correction.

The fitted autoregressive coefficient is clipped to `[-0.98, 0.98]`, and the residual scale has a small positive floor. These guard against unstable recursion and division by zero in degenerate histories. They are engineering safeguards, not theoretical guarantees.

## Sequential evidence

The reference detector maintains three one-sided CUSUM channels over standardized innovations:

```text
C+_t = max(0, C+_(t-1) + z_t - k)
C-_t = max(0, C-_(t-1) - z_t - k)
Cabs_t = max(0, Cabs_(t-1) + |z_t| - sqrt(2/pi) - k)
s_t = max(s_(t-1), C+_t, C-_t, Cabs_t)
```

`k` is the configured non-negative allowance. The first two channels accumulate sustained positive or negative shifts; the absolute-value channel responds to unusually large innovation magnitude, including scale changes. `s_t` is non-decreasing because it is the running maximum of the channels. It is an uncalibrated evidence score, not a probability, p-value, change probability, or guaranteed alarm threshold. Thresholds and false-alarm rates require a separate calibration protocol on representative data.

## Public API and state

```python
from breakforge import StructuralBreakDetector

detector = StructuralBreakDetector(allowance=0.25).fit(history)
for value in stream:
    score = detector.update(value)
detector.reset()
```

- Input: finite real-valued observations; the reference history contains at least three values.
- `fit(history)`: estimates and freezes the reference model, then resets online state.
- `update(x)`: consumes one value and returns the score through that value.
- `score`: current running maximum evidence.
- `reset()`: clears CUSUMs and begins a new stream from the final fitted-history value.

Because every call consumes exactly one new value, the API does not need a future stream length. See [validation](validation.md) for the causal contract and its tests.

## Scope

This compact implementation is a reproducible reference baseline, not a reproduction of every competition experiment. It intentionally has no GPU, CrunchDAO, or competition-data dependency. The historical project investigated richer statistical, spectral, dynamical, sequential, and learned representations; curated summaries and limitations are in [failed experiments](failed_experiments.md) and [research journey](research_journey.md).

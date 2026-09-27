---
id: "T3 preregistration"
type: "report"
updated: "2026-09-26"
---
# T3 — pre-registration: the overoptimization slope against published coefficients (C9)

Written before any published number was retrieved. **Serves:** testable predictions (ROADMAP §1): the cheapest
external contact the project has (Status §3, question 4).

## What is known before looking

- From memory, and already in [[B04]]: Gao, Schulman & Hilton (ICML 2023) fit gold reward against
  `d = √KL(π‖π_init)` as `R_bon(d) = d(α_bon − β_bon·d)` for best-of-n and `R_RL(d) = d(α_RL − β_RL·log d)` for RL,
  per proxy reward-model size, with a larger "gold" reward model as the target.
- **Not known:** their numeric coefficients; whether they report the gold reward's standard deviation under
  the initial policy; whether they report the proxy–gold correlation, or a pairwise agreement rate, under the
  initial policy. These decide whether the test can run at all.

## The prediction under test

[[C09]], as registered since v6: for a Gibbs path, `α = √2·ρ·sd`, where `ρ` is the proxy–gold correlation
and `sd` the gold standard deviation, both under the initial policy ([[B04]], exact in the jointly Gaussian case).
For best-of-n in the Gaussian case, the ratio of gold gain to `d` (with the standard KL upper bound
`log n − (n−1)/n`) is `c_n·ρ·sd` with `c_n` = 1.284, 1.291, 1.304, 1.315, 1.325, 1.334 at `n` = 2, 4, 16, 64,
256, 1000 (theory only; computed from the Gaussian maximum, no data). The bound overstates the true KL, so the
Gaussian best-of-n slope lies between `c_n` and `√2` times `ρ·sd`.

| # | Claim | Prediction | Falsified if |
|---|---|---|---|
| P1 | C9 as registered | for every proxy size with complete data, `α_bon / (√2·ρ·sd)` lies in `[1/1.5, 1.5]` | any size outside the band by more than its stated transcription uncertainty |
| P2 | the Gaussian best-of-n refinement | the same ratio against `1.30·ρ·sd` lies in `[1/1.5, 1.5]` | as P1 |
| P3 | RL paths are not Gibbs paths | no prediction for `α_RL`; reported only | — |

## Data rules, fixed now

1. **Source S1:** Gao, Schulman & Hilton (2023), the paper and its appendices. Coefficients are taken from
   tables or text. A value read off a figure is allowed only with a stated reading uncertainty of at least
   ±10 %, and is flagged.
2. **`ρ`:** reported directly; or derived from a reported pairwise agreement rate `a` between proxy and gold
   under the initial policy, by Sheppard's formula `ρ = sin(π(a − ½))`. That bridge assumes Gaussianity and is
   flagged wherever it is used. Held-out preference accuracy against *human* labels is **not** a substitute.
3. **`sd`:** reported directly, or fixed by a normalization the paper states (for example, gold scores
   standardized under the initial policy). Otherwise it is missing.
4. **Source S2,** only if S1 lacks `ρ` or `sd`: other published work that fits the same `√KL` form for best-of-n
   and reports both quantities for the same models. Every source searched is listed, found or not.
5. **If no source gives all three quantities for one model, C9 is recorded as not testable from published
   data.** That is a clean negative about the cheapest route. The next route — replication with small open
   models (T3b) — is not run in this step.
6. **If the sources cannot be reached from this environment,** that is recorded; nothing is filled from memory.

## Decision rules

- **D1.** P1 decides C9. A falsified C9 is recorded, not repaired: [[B04]]'s Gaussian identity stays proved, and
  what fails is its use as a prediction for real reward models.
- **D2.** A result inside the band is reported with its width: agreement within a factor 1.5 is weak evidence,
  because many models predict a slope of order `ρ·sd`.

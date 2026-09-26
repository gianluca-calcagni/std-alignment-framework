---
id: "Prop 22"
type: "proposition"
title: "the first-order effect of any smooth optimizer; tier 1, v6.3"
section: "Core 08 Capability what optimization pressure does"
order: 46
layer: "explanation"
tier: ["1"]
assumes: []
status: "proved"
depends_on: ["Prop 14", "Def 13"]
mentions: []
checks: ["V08", "V25"]
sources: []
aliases: ["Proposition 22", "Prop. 22"]
updated: "2026-09-26"
---
# Prop 22 — the first-order effect of any smooth optimizer; tier 1, v6.3
<!-- gen:header -->
> [!abstract] Proposition · tier 1 · proved · in [[Core 08 Capability what optimization pressure does]]
<!-- /gen:header -->

## Statement

**Proposition 22 (the first-order effect of any smooth optimizer; tier 1, v6.3).** Let `p_t` be any
differentiable path with `p_0 = q` and initial velocity `v = ṗ_0`, so `Σ_x v_x = 0`. Then

```
d/dt E_{p_t}F |_{t=0} = Σ_x v_x F_x = Cov_q(v/q, F).
```

Two cases:
- **Gibbs actor:** `v/q = F̂ − E_qF̂`, which gives `Cov_q(F̂, F)` — Prop. [[Prop 14|14]](ii).
- **Vanilla softmax policy gradient** on `E_pF̂`, from logits `log q`, with step `η`:
  `v_x = η·q_x·(q_x(F̂_x − E_qF̂) − Σ_y q_y²(F̂_y − E_qF̂))`. This gives
  `η·Σ_x q_x²(F_x − E_qF)(F̂_x − E_qF̂)`, a **`q²`-weighted** covariance.

## Proof

*Proof.* Differentiate `Σ_x p_t(x)F_x`. For the policy gradient, use `∂p_x/∂θ_y = p_x(1{x=y} − p_y)` with
`θ̇ = η·q ⊙ (F̂ − E_qF̂)`. ∎

## Notes and checks

*Note (R7-2).* `p_0 = q` is the path's starting point. For an optimizer that starts from its own reference,
read `q_A` throughout. The first-order criterion is then a covariance under `q_A`, not under the declared `q`.

*Check.* [[V25]]: the Gibbs path to `9·10⁻⁷` (finite difference), the policy-gradient formula to relative
`4·10⁻⁵`. The two optimizers' initial effects have **opposite signs in 80 of 2,000** random instances.

*Reading.* **Whether a small amount of optimization helps depends on the optimizer's geometry, not only on the
proxy and the target.** Prop. [[Prop 14|14]](ii)'s criterion `Cov_q(F̂, F) > 0` is the Gibbs (natural-gradient) case. For a
vanilla gradient the criterion weights behaviours by `q²`, so a few high-probability behaviours dominate. The
independent review's T-B built an instance where `Cov_q > 0` but the vanilla-gradient effect is negative.
The same holds for best-of-n, whose first-order weight is the **rank** of `F̂`, not its value. Its sign
disagrees with `Cov_q(F̂,F)` in 2.45 % of R6's random instances, and on a constructed instance with
`Cov_q = +18.6` (R6, P6–P7).

**Measured** ([[V08|V8]]: 300 random instances per error scale, `β ∈ [2⁻², 2¹¹·⁷⁵]`):

| error scale | 0.2 | 1 | 4 | 8 |
|---|---|---|---|---|
| total regret monotone decreasing in `β` | 0.86 | 0.53 | 0.38 | 0.37 |
| monotone increasing | 0.00 | 0.01 | 0.14 | 0.25 |
| strict interior optimum | 0.14 | 0.45 | 0.43 | 0.30 |
| raw alignment regret non-monotone | 0.99 | 0.77 | 0.58 | 0.47 |
| raw alignment regret negative somewhere | 0.79 | 0.62 | 0.52 | 0.53 |
| P(monotone decreasing \| argmax agrees) | 1.00 | 0.97 | 0.85 | 0.88 |
| median `β` minimizing total regret | 64 | 22.6 | 4 | 1.7 |

The comparative static "optimal `β` falls as error grows" reproduces on this generator. **It is a property
of the generator, not a theorem**; Prop. [[Prop 14|14]] constrains only its endpoints.

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Def 13]] — actor models; R7-1
- [[Prop 14]]

## Used by
- [[B05]] — When does optimizing a proxy help at all? — Laidlaw et al.; Holmström & Milgrom (1991)
- [[C06]] — What optimization pressure does (Prop. 14)
- [[C07]] — The actor model *(the weakest joint for the AI substrate; tiers corrected in v6.4)*

## Mentions
- none

## Mentioned in
- none

## Checks
- [[V08]]
- [[V25]]

## Sources
- none

## Retractions touching this note
- [[R066]]
<!-- /gen:links -->

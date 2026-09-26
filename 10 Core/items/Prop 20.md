---
id: "Prop 20"
type: "proposition"
title: "Goodhart as a covariance — any optimizer; tier 1"
section: "Core 08 Capability what optimization pressure does"
order: 44
layer: "explanation"
tier: ["1"]
assumes: []
status: "proved"
depends_on: ["Def 13"]
mentions: ["B11", "Prop 14", "Prop 21", "R5_LOG"]
checks: ["V20", "V26"]
sources: []
aliases: ["Proposition 20", "Prop. 20"]
updated: "2026-09-26"
---
# Prop 20 — Goodhart as a covariance — any optimizer; tier 1
<!-- gen:header -->
> [!abstract] Proposition · tier 1 · proved · in [[Core 08 Capability what optimization pressure does]]
<!-- /gen:header -->

## Statement

**Proposition 20 (Goodhart as a covariance — any optimizer; tier 1).** Let `p ≪ q` be the behaviour of *any*
actor and `w = dp/dq`. Then:

```
E_pF − E_qF = Cov_q(w, F̂) − Cov_q(w, E)          (target gain = proxy gain − covariance of the choices with the error)
E_{p₁}F − E_{p₂}F = Cov_q(w₁ − w₂, F)             (regret between any two actors)
```

## Proof

*Proof.* `E_pG − E_qG = Cov_q(w, G)` for any `G`, since `E_q w = 1` (Price's selection term).
Apply it with `G = F = F̂ − E`, and to the difference of two actors. ∎

## Notes and checks

*Note (R7-2: which base measure).* The identity holds for **any** base measure `q` with `p ≪ q`. Read with the
declared reference, it measures gain relative to the intended default. Read with an optimizer's own starting
point `q_A`, it describes that optimizer's selection. For an actor starting from its own default, the second
reading is the explanatory one, and weights relative to `q` pick up the factor `q_A/q`.

*Attribution.* The identity `E_pG − E_qG = Cov_q(w, G)` is Price's selection term; the dictionary reads it for
biology in [[B11|B11(i)]]. *(Moved from the proof in v7.0: the dictionary derives from this proposition, not the
reverse; citing it inside the proof created the cycle B11 → B04 → Prop 21 → Prop 20 → B11.)*

*Check.* [[V20]]: best-of-`k` on the proxy (its exact distribution), top-`m` selection, and arbitrary
distributions — none of them tilts — to `2·10⁻¹⁵`.

*Reading.* Whatever the optimizer, it raises the proxy by `Cov_q(w, F̂)`, and the target by that amount
minus `Cov_q(w, E)`: **Goodhart's law is the covariance between the optimizer's selection weights and the
evaluator's error.** Prop. [[Prop 14|14]](ii) is its first-order form for the tilt, where `w ≈ 1 + β(F̂ − E_qF̂)`.

This is a restatement with a useful property — it holds for every actor — **not a finding**. It does
discriminate between optimizers in at least one case. The independent review ([[R5_LOG]], T-F) placed a
single overrated state and compared actors at matched proxy gain. Best-of-n's covariance with the error was
1.1–21× smaller than the Gibbs actor's, with the gap shrinking as selection strengthens. The reason is that
best-of-n's weight on any state is at most `n·q(x)` ([[V26]]), however large the error there.

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Def 13]] — actor models; R7-1

## Used by
- [[C07]] — The actor model *(the weakest joint for the AI substrate; tiers corrected in v6.4)*
- [[Prop 21]] — no overoptimization under an affine regression — for any actor that sees only the evaluator; tier 1, v6.3

## Mentions
- [[B11]] — Quantitative genetics — selection on a proxy trait *(new in v6.1)*
- [[Prop 14]]
- [[Prop 21]] — no overoptimization under an affine regression — for any actor that sees only the evaluator; tier 1, v6.3
- [[R5_LOG]]

## Mentioned in
- none

## Checks
- [[V20]]
- [[V26]]

## Sources
- none

## Retractions touching this note
- none
<!-- /gen:links -->

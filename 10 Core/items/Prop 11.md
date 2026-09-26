---
id: "Prop 11"
type: "proposition"
title: "the order is structural, not a matter of tightness"
section: "Core 06 The divergence fixes the norm"
order: 28
layer: "explanation"
tier: ["1", "4 (E)"]
assumes: ["Hyp E"]
status: "proved"
depends_on: ["Prop 10", "Def 13"]
mentions: []
checks: ["V06"]
sources: ["src Huang 2025", "src Kwa 2024"]
aliases: ["Proposition 11", "Prop. 11"]
updated: "2026-09-26"
---
# Prop 11 — the order is structural, not a matter of tightness
<!-- gen:header -->
> [!abstract] Proposition · tier 1 / 4 (E) · assumes [[Hyp E]] · proved · in [[Core 06 The divergence fixes the norm]]
<!-- /gen:header -->

## Statement

**Proposition 11 (the order is structural, not a matter of tightness).** Let `(X, 𝒜, q)` be a general
probability space and `E ∈ L¹(q)`.
(i) If `q(E > m) > 0` for all `m` and `log 1/q(E > m) = o(m)` as `m → ∞`, then for every `δ > 0`,
`sup_{KL(p‖q)≤δ} E_pE = +∞`. (Also `E_q e^{λE} = ∞` for every `λ > 0`, so for bounded `F` the entropic model
cannot be run on `F̂`: *[this remark assumes (E)]*.)
(ii) If `Var_q E < ∞`, then `sup_{χ²(p‖q)≤δ} E_pE ≤ E_qE + √(δ·Var_q E)`.
Pareto tails with shape `a > 2` satisfy both hypotheses.

## Proof

*Proof.* (i) Let `r = q(E>m)`, `q_m = q(·|E>m)`, `p = (1−ε)q + εq_m`. KL is convex in its first argument and
`KL(q_m‖q) = log 1/r`, so `KL(p‖q) ≤ ε·log 1/r`. Also `E_pE ≥ (1−ε)E_qE + εm`. Since `E ∈ L¹`, `r → 0`. Take
`ε = δ/log(1/r)` (≤ 1 for large `m`): then `KL ≤ δ` and `E_pE ≥ (1−ε)E_qE + δm/log(1/r) → ∞`. For the
parenthetical: `E_q e^{λE} ≥ e^{λm}r(m) = e^{λm − o(m)} → ∞`. (ii) Prop. [[Prop 10|10]](c). ∎

## Notes and checks

*Check.* [[V06|V6]], Pareto `a = 3` (`Var = 0.75`): the χ²-exposure bound at `δ = 0.1` is 0.274. Mixtures with exact
`KL ≤ 0.093` reach `E_pE − E_qE = 1.08, 54.3, 2.7·10⁵, 1.4·10¹³` at `m = 10², 10⁴, 10⁸, 10¹⁶`.

> **Choosing a regularizer is choosing which norm of the evaluator's error must be controlled.** KL needs
> exponential moments, χ² needs a variance, `D_∞` needs only a mean but pays the density ratio. Errors with
> finite variance and heavy tails are controlled by χ² and not by KL at any budget.

*Prior art.* Huang et al. (ICLR 2025, χPO) argue, via coverage and single-policy concentrability, that KL
regularization is too weak to prevent overoptimization and that χ² regularization is preferable. Kwa et
al. (NeurIPS 2024) give the tail version. Mroueh & Nitsure give transportation and Rényi bounds. Prop. [[Prop 10|10]]
organizes these as one conjugate pairing; that organization is the part not found stated elsewhere.

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Def 13]] — actor models; R7-1
- [[Prop 10]] — conjugate pairings

## Used by
- [[B02]] — The conjugacy scale *(merges four v5 entries)*
- [[C04]] — The divergence order is structural (Props 10, 11)
- [[C07]] — The actor model *(the weakest joint for the AI substrate; tiers corrected in v6.4)*
- [[C14]] — Does the arrangement have content? *(successor to v5 A9; answered in R3)*

## Mentions
- none

## Mentioned in
- [[Prop 4]] — an error confined to one region saturates

## Checks
- [[V06]]

## Sources
- [[src Huang 2025]]
- [[src Kwa 2024]]

## Retractions touching this note
- [[R043]]
- [[R048]]
<!-- /gen:links -->

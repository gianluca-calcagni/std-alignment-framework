---
id: "Prop 6"
type: "proposition"
title: "the width, computed"
section: "Core 04 Capacity"
order: 21
layer: "explanation"
tier: ["1"]
assumes: []
status: "proved"
depends_on: ["Lemma 5.1", "Def 13", "Def 5", "Def 6"]
mentions: []
checks: ["V04"]
sources: ["src Ben-Tal 2013", "src Donsker 1975", "src Namkoong 2017"]
aliases: ["Proposition 6", "Prop. 6"]
updated: "2026-09-26"
---
# Prop 6 — the width, computed
<!-- gen:header -->
> [!abstract] Proposition · tier 1 · proved · in [[Core 04 Capacity]]
<!-- /gen:header -->

## Statement

**Proposition 6 (the width, computed).**
(i) (Donsker–Varadhan) `σ_δ(E) = inf_{λ>0} [δ + Λ_q(λ)]/λ`.
(ii) As `δ → 0`: `σ_δ(E) = √(2δ·Var_q E) + O(δ)`, so `w_δ(E) = 2√(2δ·Var_q E) + O(δ)`.
(iii) For `δ ≥ log 1/q(argmax E)`: `σ_δ(E) = max E − E_qE`. For `δ` large enough on both sides,
`w_δ(E) = osc(E)`.

## Proof

*Proof.* (i) Weak duality: for `p ∈ C_δ`, `λ > 0`, the Gibbs variational inequality gives
`λ(E_pE − E_qE) ≤ KL(p‖q) + Λ_q(λ) ≤ δ + Λ_q(λ)`. Equality holds at `p = p_{E,λ_δ}`, which attains `σ_δ` by
Lemma [[Lemma 5.1|5.1]]. In the case `λ_δ = ∞`, `[δ + Λ_q(λ)]/λ → max E − E_qE` as `λ → ∞`.
(ii) With `λ = λ_δ(E)`: `σ_δ = Λ_q'(λ)` and `δ = λΛ_q'(λ) − Λ_q(λ)`. Taylor at 0 with `v = Var_q E`:
`δ = vλ²/2 + O(λ³)`, so `λ = √(2δ/v) + O(δ)` and `σ_δ = vλ + O(λ²) = √(2δv) + O(δ)`.
(iii) From Lemma [[Lemma 5.1|5.1]]. ∎

## Notes and checks

*Check.* [[V04|V4]]: DV formula to `2.0·10⁻¹²`; `σ_δ/√(2δ·Var) = 1.0010, 1.0031, 1.0094` at `δ = 10⁻⁴, 10⁻³, 10⁻²`;
exact saturation at large `δ`.

*Prior art.* `σ_δ(E)` is the worst-case expectation of distributionally robust optimization over a KL ball;
(i) is the standard KL-DRO dual (Ben-Tal et al., Management Science 2013). The χ² analogue is the
variance-regularization view of χ²-DRO (Namkoong & Duchi, NeurIPS 2017). The DRO literature therefore
imports directly into the capacity layer.

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Def 5]] — capacity actor
- [[Def 6]] — width
- [[Def 13]] — actor models; R7-1
- [[Lemma 5.1]] — form of the capacity actor

## Used by
- [[B03]] — Goodhart variants — Manheim & Garrabrant (2018)
- [[C02]] — The width is the exact worst case (Thm 5, Lemma 5.1, Prop. 6)
- [[C07]] — The actor model *(the weakest joint for the AI substrate; tiers corrected in v6.4)*
- [[C08]] — Crossing curves *(tested in R5 on best-of-n and vanilla policy gradient: holds)*
- [[Thm 9]] — the worst-case regret is not separable

## Mentions
- none

## Mentioned in
- none

## Checks
- [[V04]]

## Sources
- [[src Ben-Tal 2013]]
- [[src Donsker 1975]]
- [[src Namkoong 2017]]

## Retractions touching this note
- none
<!-- /gen:links -->

---
id: "Lemma 5.1"
type: "lemma"
title: "form of the capacity actor"
section: "Core 04 Capacity"
order: 17
layer: "measurement"
tier: ["—"]
assumes: []
status: "proved"
depends_on: ["Def 5", "Def 2"]
mentions: ["Prop 14"]
checks: ["F1", "V33"]
sources: []
aliases: ["Lemma 5.1", "Lemma. 5.1"]
updated: "2026-09-26"
---
# Lemma 5.1 — form of the capacity actor
<!-- gen:header -->
> [!abstract] Lemma · tier — · proved · in [[Core 04 Capacity]]
<!-- /gen:header -->

## Statement

**Lemma 5.1 (form of the capacity actor).** For non-constant `G`, `t ↦ KL(p_{G,t}‖q)` is continuous and
strictly increasing on `[0,∞)`, from 0 at `t = 0` towards its limit `log 1/q(argmax G)` as `t → ∞`. Let
`λ_δ(G)` be the unique `t` with `KL(p_{G,t}‖q) = δ`, or `+∞` if `δ ≥ log 1/q(argmax G)`. Then
`p_{G, min(β, λ_δ(G))}` maximizes `J_G` over `C_δ`. It is the unique maximizer except when `β = ∞` and
`δ > log 1/q(argmax G)`. Moreover, `t ↦ E_{p_{G,t}}G` is strictly increasing on `ℝ`, with derivative
`Var_{p_{G,t}}(G) > 0`.

## Proof

*Proof.* `d/dt E_{p_{G,t}}G = Var_{p_{G,t}}(G)` (the exponential family), which is positive because `G` is
non-constant and `p_{G,t}` has full support. `d/dt KL(p_{G,t}‖q) = t·Var_{p_{G,t}}(G) > 0`, and `p_{G,t} → q(·|argmax G)` as `t → ∞`. If
`β ≤ λ_δ`, the unconstrained maximizer `p_{G,β}` is feasible, hence optimal. If `β > λ_δ`, the problem is a
concave maximization over a convex set with a Slater point (`q`). The Lagrangian
`E_pG − (1/β + μ)·KL(p‖q) + μδ` is maximized by `p_{G,1/(1/β+μ)}`. The choice `μ = 1/λ_δ − 1/β ≥ 0`
satisfies complementary slackness. Uniqueness for `β < ∞` follows from strict concavity of `J_G`. For
`β = ∞` the same argument holds with `1/β = 0`, and the maximizer is unique when `δ ≤ log 1/q(argmax G)`
(a non-constant linear functional on a strictly convex set). For larger `δ`, every distribution on
`argmax G` inside `C_δ` is a maximizer, and `p_{G,∞}` is the one of least KL. All results below hold for
any choice of maximizer. ∎

## Notes and checks

*Check.* [[V33]] (R7-3): the divergence and the mean increase strictly on every resolvable grid step of 2,000 instances.
The derivative identity holds to relative `5.5·10⁻⁵` wherever `Var > 10⁻⁴`, and the limit to `9·10⁻¹⁶`. [[F1]] (rows `cap` and
`cap_inf`): the capacity solution against a generic constrained optimizer. *(Before R7-3 no check was linked here, and the
monotone mean — then Prop. 14(i) — had never been checked numerically.)*

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Def 2]] — the bounded actor
- [[Def 5]] — capacity actor

## Used by
- [[C02]] — The width is the exact worst case (Thm 5, Lemma 5.1, Prop. 6)
- [[Cor 5.2]] — the exchange rate is a shadow price
- [[Cor 17.1]] — the capacity actor's regret is the budget convention
- [[Def 10]] — intent ray and misalignment measures; v6.4, R7-0
- [[Prop 6]] — the width, computed
- [[Prop 14]]
- [[Prop 24]] — the v6.4 measures against the contract; tier 1
- [[Prop 26]] — reference misspecification is measured misalignment; R7-2
- [[Prop 27]] — instrumental tracking — the weight on external reward is a shadow price; R7-4
- [[Prop 31]] — target sets against the contract; R7-7
- [[Prop 32]] — the ordinal measure; R7-7
- [[Prop 33]] — capped measures against the contract; R7-6a
- [[Prop 35]] — the intended segment against the contract; R7-6b

## Mentions
- [[Prop 14]]

## Mentioned in
- none

## Checks
- [[F1]]
- [[V33]]

## Sources
- none

## Retractions touching this note
- [[R076]]
<!-- /gen:links -->

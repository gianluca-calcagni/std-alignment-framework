---
id: "Thm 17"
type: "theorem"
title: "every regret notion is a point on one convex curve"
section: "Core 07 Identification, gauge, and the intent ray"
order: 37
layer: "measurement"
tier: ["1"]
assumes: []
status: "proved"
depends_on: ["Def 10", "Thm 13", "Thm 1", "Def 3"]
mentions: []
checks: ["V14"]
sources: []
aliases: ["Theorem 17", "Thm. 17"]
updated: "2026-09-26"
---
# Thm 17 — every regret notion is a point on one convex curve
<!-- gen:header -->
> [!abstract] Theorem · tier 1 · proved · in [[Core 07 Identification, gauge, and the intent ray]]
<!-- /gen:header -->

## Statement

**Theorem 17 (every regret notion is a point on one convex curve).** Let `M(t) = KL(p̂‖p_{F,t})` (Def. [[Def 10|10]]).

(i) `M` is convex on `ℝ`; its minimum over `[0, ∞)` is `D_⊥`, attained at `t̂⁺`.

(ii) `M(β) = β·R_J`. This is the **same-price** counterfactual: the intended actor has the actual actor's
exchange rate.

(iii) If `λ ∈ (0, ∞)` satisfies `KL(p_{F,λ}‖q) = KL(p̂‖q)`, then `E_{p_{F,λ}}F − E_{p̂}F = M(λ)/λ`. This is the
**same-budget** counterfactual: the intended actor has spent the same information. Its raw regret is exact
because the information costs are equal.

(iv) `D_⊥` and `M(λ)` are unchanged under `F ↦ aF + c` with `a > 0`; `M(β)` is not.

## Proof

*Proof.*
(i) By Thm [[Thm 13|13]](a), `M(t) = M(t̂) + [A(t) − A(t̂) − (t − t̂)A'(t̂)]`, a constant plus the Bregman divergence of
the convex function `A`. A convex function whose unconstrained minimizer is `t̂` has its minimizer over
`[0, ∞)` at `t̂⁺`.
(ii) Theorem [[Thm 1|1]].
(iii) Theorem [[Thm 1|1]] at exchange rate `λ` gives `J^λ_F(p_{F,λ}) − J^λ_F(p̂) = M(λ)/λ`; the terms `KL(·‖q)/λ` are
equal and cancel.
(iv) `p_{aF+c,t} = p_{F,at}`, so the half-ray is the same set of distributions. `D_⊥` is an infimum over that
set, and the budget-matched point is the unique point of that set with `KL(·‖q) = KL(p̂‖q)`, so both are
unchanged. `M(β)` becomes `KL(p̂‖p_{F,aβ})`. ∎

## Notes and checks

*Check.* [[V14]]: minimum over a grid never below `D_⊥`; (iii) to `6·10⁻¹²`.

*Measured* ([[V14]]): over 1,218 random pairs of errors, the same-price and same-budget conventions **rank the
two errors differently in 11.4 %** of pairs. The convention is therefore part of the definition, not a
detail.

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Def 3]] — regrets
- [[Def 10]] — intent ray and misalignment measures; v6.4, R7-0
- [[Thm 1]] — regret is a divergence
- [[Thm 13]] — intent-ray decomposition

## Used by
- [[B01]] — Anchor
- [[C05]] — Decomposition, gauge and conventions (Thm 13, Prop. 16, Thm 17, Def. 8)
- [[C07]] — The actor model *(the weakest joint for the AI substrate; tiers corrected in v6.4)*
- [[C14]] — Does the arrangement have content? *(successor to v5 A9; answered in R3)*
- [[Cor 17.1]] — the capacity actor's regret is the budget convention
- [[Prop 16]] — gauge group and identified quantities
- [[Prop 24]] — the v6.4 measures against the contract; tier 1

## Mentions
- none

## Mentioned in
- [[Overview 0]] — alignment instance — static, single-target module; not a definition — the formal definition is Definition 12
- [[Prop 15]] — the identity for any convex regularizer and any target that keeps the objective concave

## Checks
- [[V14]]

## Sources
- none

## Retractions touching this note
- [[R068]]
<!-- /gen:links -->

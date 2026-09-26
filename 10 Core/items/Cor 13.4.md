---
id: "Cor 13.4"
type: "corollary"
title: "second order"
section: "Core 07 Identification, gauge, and the intent ray"
order: 36
layer: "explanation"
tier: ["4 (E)"]
assumes: ["Hyp E"]
status: "proved"
depends_on: ["Cor 1.3", "Def 3", "Def 10", "Thm 13"]
mentions: []
checks: ["V07"]
sources: []
aliases: ["Corollary 13.4", "Cor. 13.4"]
updated: "2026-09-26"
---
# Cor 13.4 — second order
<!-- gen:header -->
> [!abstract] Corollary · tier 4 (E) · assumes [[Hyp E]] · proved · in [[Core 07 Identification, gauge, and the intent ray]]
<!-- /gen:header -->

## Statement

**Corollary 13.4 (second order).** *[Assumes (E).]* For `E = εE₀`, write `a = Cov_{p*}(E₀,F)/Var_{p*}(F)` and
`E₀⊥ = E₀ − aF` (uncorrelated with `F` under `p*`). As `ε → 0` we have `t̂ → β > 0`, so the full-ray and
half-ray decompositions coincide and `X_anti = 0`:
`D_⊥ = (β²ε²/2)·Var_{p*}(E₀⊥) + O(ε³)` and `D_∥ = (β²ε²/2)·a²·Var_{p*}(F) + O(ε³)`.

## Proof

*Proof.* `t̂ − β = βεa + O(ε²)` from the moment condition. Hence `D_∥ = A''(β)(t̂−β)²/2 + O(ε³)`. And
`β·R_J = (β²ε²/2)·Var_{p*}(E₀) + O(ε³)` from Cor. [[Cor 1.3|1.3]]. Subtract, using
`Var(E₀) = a²·Var(F) + Var(E₀⊥)`. ∎

## Notes and checks

*Check.* [[V07|V7]]: at `ε = 0.003` the two ratios are 1.0009 and 0.968. The `D_∥` ratio converges slowly when
`|a|` is small, as the `O(ε³)` remainder predicts.

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Cor 1.3]] — CGF and integral forms
- [[Def 3]] — regrets
- [[Def 10]] — intent ray and misalignment measures; v6.4, R7-0
- [[Thm 13]] — intent-ray decomposition

## Used by
- [[Prop 26]] — reference misspecification is measured misalignment; R7-2

## Mentions
- none

## Mentioned in
- none

## Checks
- [[V07]]

## Sources
- none

## Retractions touching this note
- none
<!-- /gen:links -->

---
id: "Thm 5"
type: "theorem"
title: "the width is the exact worst case"
section: "Core 04 Capacity"
order: 20
layer: "explanation"
tier: ["2"]
assumes: []
status: "proved"
depends_on: ["Def 13", "Def 5", "Def 15", "Def 2", "Def 6"]
mentions: []
checks: ["V04"]
sources: []
aliases: ["Theorem 5", "Thm. 5"]
updated: "2026-09-26"
---
# Thm 5 — the width is the exact worst case
<!-- gen:header -->
> [!abstract] Theorem · tier 2 · proved · in [[Core 04 Capacity]]
<!-- /gen:header -->

## Statement

**Theorem 5 (the width is the exact worst case).**
(i) For every `β ∈ (0,∞]`, `δ > 0`, `F`, `E`: `0 ≤ R^C ≤ E_{p^C_{F̂}}E − E_{p^C_F}E ≤ w_δ(E)`.
(ii) For `β = ∞`: `sup_F R^C(F; E, δ) = w_δ(E)`, approached by `F = −cE`, `c ↑ 1`.
(iii) For `β < ∞` with `β > λ_δ(E) + λ_δ(−E)`: `sup_F R^C ≥ (1 − λ_δ(E)/β)·w_δ(E)`.

## Proof

*Proof.* (i) `p^C_F` maximizes `J_F` over `C_δ` and `p^C_{F̂} ∈ C_δ`, so `R^C ≥ 0`. `p^C_{F̂}` maximizes `J_{F̂}`
over `C_δ` and `p^C_F ∈ C_δ`, so `J_{F̂}(p^C_{F̂}) ≥ J_{F̂}(p^C_F)`, which rearranges to the middle
inequality. Both measures lie in `C_δ`, which gives the last one.
(ii) With `F = −cE`, `0<c<1`: `p^C_F` minimizes `E_pE` over `C_δ` and `p^C_{F̂}` maximizes it (`F̂ = (1−c)E`;
for `β = ∞` positive rescaling does not move the argmax). So `R^C = c·[σ_δ(E) + σ_δ(−E)] = c·w_δ(E)`.
(iii) The same construction with both constraints binding gives `c·w_δ`, because the KL terms cancel at
`KL = δ`. Binding requires `cβ ≥ λ_δ(−E)` and `(1−c)β ≥ λ_δ(E)`. ∎

## Notes and checks

*Check.* [[V04|V4]]: 0 violations / 3,000 (mixed finite and infinite `β`); `R^C/w` p5/p50/p95 = 0.009 / 0.095 /
0.268; the construction with `c = 0.999` returns `R^C/w = 0.9990` in every instance.

> **No bound depending only on `(E, δ)` can be below `w_δ(E)`.** The width is the capacity-form normal
> form, and it is a support function, not a product.

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Def 2]] — the bounded actor
- [[Def 5]] — capacity actor
- [[Def 6]] — width
- [[Def 13]] — actor models; R7-1
- [[Def 15]] — the capacity model; R7-3

## Used by
- [[B01]] — Anchor
- [[C02]] — The width is the exact worst case (Thm 5, Lemma 5.1, Prop. 6)
- [[C07]] — The actor model *(the weakest joint for the AI substrate; tiers corrected in v6.4)*
- [[Prop 7]] — a bound with realized travel from the reference
- [[Rem 7.1]] — historical note: the v5 normal form
- [[Thm 9]] — the worst-case regret is not separable

## Mentions
- none

## Mentioned in
- [[Cor 17.1]] — the capacity actor's regret is the budget convention
- [[Prop 23]] — argmax selectors on a common candidate set — tier 2′, v6.4

## Checks
- [[V04]]

## Sources
- none

## Retractions touching this note
- [[R032]]
- [[R076]]
<!-- /gen:links -->

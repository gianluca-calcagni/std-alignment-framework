---
id: "Cor 17.1"
type: "corollary"
title: "the capacity actor's regret is the budget convention"
section: "Core 07 Identification, gauge, and the intent ray"
order: 42
layer: "explanation"
tier: ["4 (C)"]
assumes: ["Hyp C"]
status: "proved"
depends_on: ["Lemma 5.1", "Thm 17", "Def 13", "Def 5", "Def 15", "Def 2"]
mentions: ["Def 22", "Def 8", "Thm 5"]
checks: ["V18", "V19"]
sources: []
aliases: ["Corollary 17.1", "Cor. 17.1"]
updated: "2026-09-26"
---
# Cor 17.1 — the capacity actor's regret is the budget convention
<!-- gen:header -->
> [!abstract] Corollary · tier 4 (C) · assumes [[Hyp C]] · proved · in [[Core 07 Identification, gauge, and the intent ray]]
<!-- /gen:header -->

## Statement

**Corollary 17.1 (the capacity actor's regret is the budget convention).** *[Assumes (C).]* Let `δ < log 1/q(argmax F)` and
`δ < log 1/q(argmax F̂)`, and let `β > max(λ_δ(F), λ_δ(F̂))`, so that both capacity constraints bind. Then
`p^C_F` is the budget-matched intended actor of `p̂^C`, and

```
R^C = M(λ)/λ,   with λ = λ_δ(F).
```

If instead `δ ≥ log 1/q(argmax F)` and `β = ∞`, then `R^C = max F − E_{p̂^C}F`, the raw regret of the
saturated case.

## Proof

*Proof.* By Lemma [[Lemma 5.1|5.1]], `p^C_F = p_{F,λ_δ(F)}` and `p̂^C = p_{F̂,λ_δ(F̂)}`, with `KL(·‖q) = δ` for both. So
`p^C_F` is the budget match of `p̂^C`, and the information terms of `J_F` cancel, leaving the raw regret. That
equals `M(λ)/λ` by Thm [[Thm 17|17]](iii). The saturated case follows from `E_{p^C_F}F = max F`. ∎

## Notes and checks

*Check.* [[V18]]: 2,903 binding instances, to `1.2·10⁻¹³`; the saturated example is [[V19]].

> **Theorem [[Thm 5|5]]'s worst-case regret (§4) and the budget convention (§7) are the same object.** The pure
> capacity actor's regret is the same-budget regret, and the width `w_δ(E)` bounds it over all targets. This
> is a reason, beyond gauge invariance, to use the budget convention as the default. *(Since v7.9 the default is
> free and budget is declared (Def. [[Def 8|8]]); this identity is why the value shortfall `ΔV` is taken at equal effort,
> Def. [[Def 22|22]].)*

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Def 2]] — the bounded actor
- [[Def 5]] — capacity actor
- [[Def 13]] — actor models; R7-1
- [[Def 15]] — the capacity model; R7-3
- [[Lemma 5.1]] — form of the capacity actor
- [[Thm 17]] — every regret notion is a point on one convex curve

## Used by
- none

## Mentions
- [[Def 8]] — conventions, misalignment, ε-alignment; revised in R7-0
- [[Def 22]] — value shortfall at equal effort; R8-1
- [[Thm 5]] — the width is the exact worst case

## Mentioned in
- [[Def 22]] — value shortfall at equal effort; R8-1

## Checks
- [[V18]]
- [[V19]]

## Sources
- none

## Retractions touching this note
- none
<!-- /gen:links -->

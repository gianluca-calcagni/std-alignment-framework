---
id: "Def 10"
type: "definition"
title: "intent ray and misalignment measures; v6.4, R7-0"
section: "Core 07 Identification, gauge, and the intent ray"
order: 29
layer: "measurement"
tier: []
assumes: []
status: "definition"
depends_on: ["Lemma 5.1"]
mentions: ["Def 1", "Def 11", "Def 17", "Prop 26", "Prop 31", "Thm 13"]
checks: []
sources: []
aliases: ["Definition 10", "Def. 10"]
updated: "2026-09-26"
---
# Def 10 — intent ray and misalignment measures; v6.4, R7-0
<!-- gen:header -->
> [!abstract] Definition · definition · in [[Core 07 Identification, gauge, and the intent ray]]
<!-- /gen:header -->

## Statement

**Definition 10 (intent ray and misalignment measures; v6.4, R7-0).** Let `F` be non-constant, and let
`p̂` be a full-support actual behaviour.
- The **intent half-ray** is `𝓡⁺_F = {p_{F,t} : t ≥ 0}`, with `p_{F,t} ∝ q·e^{tF}`.
- The **regret curve** is `M(t) = KL(p̂‖p_{F,t})` for `t ∈ ℝ`.
- The **price measure** at a declared price `β` is `M_price = M(β)`.
- The **free measure** is `M_free = D_⊥ = inf_{t≥0} M(t)`.
- The **budget measure** is `M_budget = M(λ)`, where `λ ≥ 0` is the unique `t` with
  `KL(p_{F,t}‖q) = KL(p̂‖q)`. This `λ` exists and is unique iff `KL(p̂‖q) < log 1/q(argmax F)`, by Lemma [[Lemma 5.1|5.1]]:
  `t ↦ KL(p_{F,t}‖q)` is continuous and strictly increasing, from 0 towards `log 1/q(argmax F)`. Otherwise
  `M_budget` is undefined: this is saturation.

## Notes and checks

*Note (R7-7).* These are the measures of the cardinal target set `[F]₊`: the only one v7.3 had. Def. [[Def 17|17]] defines
them for any target set, as the divergence from a union of half-rays, and Prop. [[Prop 31|31]](a) shows that `[F]₊` gives
back exactly the measures here.

*Note (R7-2).* Every tilt here is of the **declared** reference `q` (Def. [[Def 1|1]]), and the budget is matched as
`KL(·‖q)` against it. The actor's own reference plays no role: a measure that used it would depend on the
explanation of the behaviour, not on the behaviour (Def. [[Def 11|11]], M4). Prop. [[Prop 26|26]] gives the consequence.

*Note.* A definition may cite an earlier result only for well-definedness; this one cites Lemma [[Lemma 5.1|5.1]] (§4).
Named quantities that need `t̂` — `D_∥`, `X_anti` — are introduced in Thm [[Thm 13|13]], after `t̂` is shown to exist.

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Lemma 5.1]] — form of the capacity actor

## Used by
- [[B01]] — Anchor
- [[B13]] — Potential games — collective behaviour is a tilt (Blume 1993) *(new in v6.2)*
- [[C05]] — Decomposition, gauge and conventions (Thm 13, Prop. 16, Thm 17, Def. 8)
- [[Cor 13.1]]
- [[Cor 13.2]] — convention-freedom
- [[Cor 13.3]] — rescaling is purely axial
- [[Cor 13.4]] — second order
- [[Def 8]] — conventions, misalignment, ε-alignment; revised in R7-0
- [[Def 12]] — alignment instance; formal
- [[Def 17]] — target sets; R7-7
- [[Prop 16]] — gauge group and identified quantities
- [[Prop 24]] — the v6.4 measures against the contract; tier 1
- [[Prop 26]] — reference misspecification is measured misalignment; R7-2
- [[Prop 30]] — the fake-alignment gap; R7-4
- [[Prop 31]] — target sets against the contract; R7-7
- [[Prop 32]] — the ordinal measure; R7-7
- [[Rem 13.5]] — whether rescaling is harmful depends on the declared convention; v6.3
- [[Thm 13]] — intent-ray decomposition
- [[Thm 17]] — every regret notion is a point on one convex curve

## Mentions
- [[Def 1]] — objects
- [[Def 11]] — the misalignment contract; R7-0
- [[Def 17]] — target sets; R7-7
- [[Prop 26]] — reference misspecification is measured misalignment; R7-2
- [[Prop 31]] — target sets against the contract; R7-7
- [[Thm 13]] — intent-ray decomposition

## Mentioned in
- [[Overview 0]] — alignment instance — static, single-target module; not a definition — the formal definition is Definition 12

## Checks
- none

## Sources
- none

## Retractions touching this note
- none
<!-- /gen:links -->

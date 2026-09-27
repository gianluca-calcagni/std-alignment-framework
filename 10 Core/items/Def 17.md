---
id: "Def 17"
type: "definition"
title: "target sets; R7-7"
section: "Core 07 Identification, gauge, and the intent ray"
order: 42.5
layer: "measurement"
tier: []
assumes: []
status: "definition"
depends_on: ["Def 1", "Def 10"]
mentions: ["Def 8", "Prop 16", "Prop 31", "Prop 32", "R7-5 go-no-go", "ROADMAP"]
checks: ["V35"]
sources: []
aliases: ["Definition 17", "Def. 17"]
updated: "2026-09-26"
---
# Def 17 — target sets; R7-7
<!-- gen:header -->
> [!abstract] Definition · definition · in [[Core 07 Identification, gauge, and the intent ray]]
<!-- /gen:header -->

## Statement

**Definition 17 (target sets; R7-7).** Let `Δ°` be the set of full-support distributions on `X`.
- A **target set** `𝒯` is a non-empty set of non-constant functions on `X`, closed under positive affine maps:
  `G ∈ 𝒯` implies `aG + c ∈ 𝒯` for every `a > 0` and `c ∈ ℝ`. Each member is an admissible statement of one intent.
- The **cardinal** target set of a non-constant `F` is `[F]₊ = {aF + c : a > 0, c ∈ ℝ}`. The **ordinal** target
  set is `[F]_ord = {φ∘F : φ : ℝ → ℝ strictly increasing}`.
- The **intended set** under the free convention, `I_free(𝒯)`, is the closure in `Δ°` of the union of the
  half-rays `{p_{G,t} : t ≥ 0}` over `G ∈ 𝒯` (Def. [[Def 1|1]]). Under the budget convention, for an actual behaviour
  `p̂` with `k = KL(p̂‖q)`, it is `I_budget(𝒯) = I_free(𝒯) ∩ {p : KL(p‖q) = k}`.
- For a full-support `p̂` and `κ ∈ {budget, free}`, the **measure** is `M_κ(𝒯) = inf_{p ∈ I_κ(𝒯)} KL(p̂‖p)`.
  `M_budget(𝒯)` is undefined when `I_budget(𝒯)` is empty. The **ordinal measure** is `M_ord = M_free([F]_ord)`.
- The **ordinal cone** of `F` is `C_F = {p ∈ Δ° : p/q is a non-decreasing function of F}`.

## Notes and checks

*Note (what v7.3 declared silently).* For `𝒯 = [F]₊` the intended sets are the half-ray and its budget point,
and the measures are those of Def. [[Def 10|10]] (Prop. [[Prop 31|31]](a)). Until R7-7 every instance declared the cardinal set
without saying so.

*Note (which set to declare).* The **cardinal** set says that the principal's exchange rates between outcomes
are part of the intent. The **ordinal** set says that only their order is. Best-of-n and quantilizers run on
the true target pursue its order with a different shape: they are misaligned under the cardinal set and aligned
under the ordinal set (Prop. [[Prop 32|32]]; [[R7-5 go-no-go]]). This is a declaration, like the convention `κ`
(Def. [[Def 8|8]]); the framework does not make it.

*Note (the price convention).* It needs a representative carrying a unit relative to `β` (Prop. [[Prop 16|16]]). So it is
defined only for a cardinal set with a declared representative, as in Def. [[Def 10|10]]. An ordinal target has no unit.

*Note (several principals).* A family of target sets, one per principal, is measured member by member. The
framework defines no aggregate; one must be declared. This changes the census exception "no single target"
(16 items) from "not formalized" to "measured per principal, with aggregation undeclared". The frozen census
routing is not re-run ([[ROADMAP]] §3).

*Note (computing the budget measure).* `M_budget([F]_ord)` has no closed form: its intended set meets a convex
cone with a level set of a convex function, and the minimization is not convex. [[V35]] computes it from five
starts. Its zero set needs no solver: `M_budget([F]_ord) = 0` iff `M_ord = 0` (Prop. [[Prop 32|32]](f)).

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Def 1]] — objects
- [[Def 10]] — intent ray and misalignment measures; v6.4, R7-0

## Used by
- [[Def 11]] — the misalignment contract; R7-0
- [[Def 12]] — alignment instance; formal
- [[Def 21]] — declared resolution; R7-10
- [[Prop 31]] — target sets against the contract; R7-7
- [[Prop 32]] — the ordinal measure; R7-7
- [[Prop 34]] — the core as a declared intended set; R7-9
- [[Prop 36]] — declared resolution against the core; R7-10

## Mentions
- [[Def 8]] — conventions, misalignment, ε-alignment; revised in R7-0
- [[Prop 16]] — gauge group and identified quantities
- [[Prop 31]] — target sets against the contract; R7-7
- [[Prop 32]] — the ordinal measure; R7-7
- [[R7-5 go-no-go]]
- [[ROADMAP]]

## Mentioned in
- [[Def 8]] — conventions, misalignment, ε-alignment; revised in R7-0
- [[Def 10]] — intent ray and misalignment measures; v6.4, R7-0
- [[Def 18]] — intensity caps and distributional targets; R7-6a
- [[Def 19]] — declared intended set; R7-9
- [[Overview 0]] — alignment instance — static, single-target module; not a definition — the formal definition is Definition 12

## Checks
- [[V35]]

## Sources
- none

## Retractions touching this note
- none
<!-- /gen:links -->

---
id: "Def 8"
type: "definition"
title: "conventions, misalignment, ε-alignment; revised in R7-0"
section: "Core 07 Identification, gauge, and the intent ray"
order: 41
layer: "measurement"
tier: []
assumes: []
status: "definition"
depends_on: ["Def 10", "Def 3"]
mentions: ["Def 14", "Def 17", "Def 18", "Def 20", "Def 22", "Prop 12", "Prop 15", "Prop 18", "Prop 24", "Prop 25", "Prop 32", "Prop 36", "Prop 37", "R057", "R074", "R075", "R8 foundations review", "Thm 17"]
checks: ["F5", "V32"]
sources: []
aliases: ["Definition 8", "Def. 8"]
updated: "2026-09-26"
---
# Def 8 — conventions, misalignment, ε-alignment; revised in R7-0
<!-- gen:header -->
> [!abstract] Definition · definition · in [[Core 07 Identification, gauge, and the intent ray]]
<!-- /gen:header -->

## Statement

**Definition 8 (conventions, misalignment, ε-alignment; revised in R7-0).** A **counterfactual convention**
`κ` fixes the intended behaviour, and with it a measure from Def. [[Def 10|10]]:

| Convention | Intended behaviour | Measure | Named |
|---|---|---|---|
| free | any point of the half-ray `𝓡⁺_F` | `M_free = D_⊥` | **misalignment** (the default), capability-free |
| budget | `p_{F,λ}`, same KL to `q` as `p̂` | `M_budget` | **misalignment** at equal effort (declared) |
| price | `p_{F,β}`, the declared price | `M_price = β·R_J` | **regret** at a price |

The actor is **ε-aligned with `F` under `κ ∈ {budget, free}`** iff the measure is at most `ε` nats. Under the
price convention, `M_price ≤ ε` defines **ε-regret**, not ε-alignment. The budget measure is defined only below saturation
(Def. [[Def 10|10]]).

## Notes and checks

*Note (R8-1: the default is free).* Until v7.8 the default was budget. It misreads style drift as pursuit
(Prop. [[Prop 36|36]](c)), is undefined at saturation, and has no closed form under an ordinal target. The free measure has
none of these defects, and caps and floors (Defs. [[Def 18|18]], [[Def 20|20]]) now declare intensity explicitly. Budget stays
available as a declaration: "compare at equal effort" ([[R8 foundations review]], A5).

*Note (R8-1: stakes).* The measures are unit-free (M3), so nats do not say how much is at stake. Severity enters in
two places: through `F` (mass `ε` on an outcome `ΔF` below the intended ones costs about `ε·t·ΔF` nats), and through the
intended intensity, so at low intensity a harm inherited from `q` is barely charged. Hence every diagnosis reports, next to the measure, the value shortfall `ΔV` of Def. [[Def 22|22]]
(Prop. [[Prop 37|37]]: `M_budget = λ·ΔV`), and, for a principal with a safety concern, a declared floor as the standard
declaration: a minimum `v_min` in `F`'s units (Prop. [[Prop 37|37]](d)). A harm-weighted divergence was considered and
rejected: it can be negative, or it is a different principal (Prop. [[Prop 15|15]]), and it double-counts what `F` encodes
([[R8 foundations review]], A1).

*Note (R7-7: target sets).* The table is the case of the cardinal target set `[F]₊`. With a declared target set
`𝒯`, the budget and free measures are those of Def. [[Def 17|17]], and ε-alignment is with `𝒯`. The price convention needs
a unit, so it applies to a cardinal set with a declared representative only. Under an ordinal target the free
measure has a closed form (Prop. [[Prop 32|32]]); the budget measure has none.

*Note.*
- **Why the price measure is called a regret rather than misalignment:** Prop. [[Prop 24|24]](c). It charges an agent that
  pursues the right target at the wrong intensity. *(v6.1–v6.4 defined ε-alignment under the price convention
  too; [[R074|row 74]].)*
- **Which reference (R7-2).** All three conventions use the declared reference `q`. Matching the budget
  against the actor's own reference instead was considered and rejected. Behaviour does not identify that
  reference (Prop. [[Prop 12|12]]). So one behaviour, attributed to two (reference, evaluator) pairs, would receive
  different measures — differing by a median of 0.22 nats and up to 10.6 in [[V32]].
- `M_free ≤ min(M_budget, M_price)` whenever these are defined, since `M_free` is an infimum over the
  half-ray.
- **Comparing a mechanism with itself** — the same algorithm run on the target with the same resource — needs
  an actor model. So it is not a convention of this table but an explanation-layer comparison (Def. [[Def 14|14]],
  Prop. [[Prop 25|25]]). *(v6.4 listed it here as an "own-resource convention"; [[R075|row 75]].)*
- The curve `M(t)` remains available for any actor as a divergence from the Gibbs ray; it is a *regret* only
  under the conventions above.
- **Saturation.** Beyond `KL(p̂‖q) ≥ log 1/q(argmax F)` the actual actor has spent more information than the
  target can use. Every budget-matched intended actor attains `max F`, and is supported on `argmax F`. Report
  `M_free` and the raw same-budget regret `max F − E_{p̂}F` instead. *(v6.1 as first released used `p_{F,∞}`
  here, which gives `+∞` even for an essentially aligned actor — [[F5]]; [[R057|row 57]].)*
- Below saturation, `M(λ) = λ·(raw regret)` exactly (Thm [[Thm 17|17]](iii)); approaching saturation it grows like `λ → ∞` at fixed raw regret. Regret in nats is
  value times the exchange rate, so highly optimized actors register large nat regrets even for small value
  losses. That is also why they are easy to detect (Prop. [[Prop 18|18]]).

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Def 3]] — regrets
- [[Def 10]] — intent ray and misalignment measures; v6.4, R7-0

## Used by
- [[C05]] — Decomposition, gauge and conventions (Thm 13, Prop. 16, Thm 17, Def. 8)
- [[C07]] — The actor model *(the weakest joint for the AI substrate; tiers corrected in v6.4)*
- [[Def 12]] — alignment instance; formal
- [[Def 23]] — the declaration; R8-2
- [[Prop 24]] — the v6.4 measures against the contract; tier 1

## Mentions
- [[Def 14]] — mechanism-relative comparison; explanation layer; R7-1
- [[Def 17]] — target sets; R7-7
- [[Def 18]] — intensity caps and distributional targets; R7-6a
- [[Def 20]] — minimum intensity and the intended segment; R7-6b
- [[Def 22]] — value shortfall at equal effort; R8-1
- [[Prop 12]] — what behaviour identifies
- [[Prop 15]] — the identity for any convex regularizer and any target that keeps the objective concave
- [[Prop 18]] — harm bounds detectability
- [[Prop 24]] — the v6.4 measures against the contract; tier 1
- [[Prop 25]] — mechanism-relative comparisons against the contract; tier 1 given the attribution
- [[Prop 32]] — the ordinal measure; R7-7
- [[Prop 36]] — declared resolution against the core; R7-10
- [[Prop 37]] — the value shortfall; R8-1
- [[R8 foundations review]]
- [[R057]]
- [[R074]]
- [[R075]]
- [[Thm 17]] — every regret notion is a point on one convex curve

## Mentioned in
- [[Cor 17.1]] — the capacity actor's regret is the budget convention
- [[Def 17]] — target sets; R7-7
- [[Def 19]] — declared intended set; R7-9
- [[Overview 0]] — alignment instance — static, single-target module; not a definition — the formal definition is Definition 12
- [[Prop 25]] — mechanism-relative comparisons against the contract; tier 1 given the attribution
- [[Prop 26]] — reference misspecification is measured misalignment; R7-2

## Checks
- [[F5]]
- [[V32]]

## Sources
- none

## Retractions touching this note
- [[R056]]
- [[R057]]
- [[R069]]
- [[R074]]
- [[R075]]
<!-- /gen:links -->

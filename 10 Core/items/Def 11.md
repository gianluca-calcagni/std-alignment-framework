---
id: "Def 11"
type: "definition"
title: "the misalignment contract; R7-0"
section: "Core 09 Observation what an overseer can detect"
order: 50
layer: "measurement"
tier: []
assumes: []
status: "definition"
depends_on: ["Def 9"]
mentions: ["Def 14", "Prop 25", "Prop 26"]
checks: []
sources: []
aliases: ["Definition 11", "Def. 11"]
updated: "2026-09-26"
---
# Def 11 — the misalignment contract; R7-0
<!-- gen:header -->
> [!abstract] Definition · definition · in [[Core 09 Observation what an overseer can detect]]
<!-- /gen:header -->

## Statement

**Definition 11 (the misalignment contract; R7-0).** A **misalignment measure** assigns to a non-constant
target `F`, a declared convention `κ`, and a full-support actual behaviour `p̂` a value `M ∈ [0, ∞]`, or
declares it undefined. It must satisfy:

| | Axiom |
|---|---|
| **M1** (identity) | `M = 0` iff `p̂` is an intended behaviour under `κ` |
| **M2** (sign) | `M ≥ 0` |
| **M3** (representation) | `M` is unchanged when `F` is replaced by `aF + c`, `a > 0`, and every declared quantity carrying the unit of `F` is transformed with it (`β ↦ β/a`) |
| **M4** (behavioural) | `M` depends on the agent only through `p̂`, or its per-context laws |
| **M5** (misdirection, not intensity) | if `p̂ = p_{F,t}` for some `t ≥ 0` — the agent pursues the target itself, at some intensity — then `M = 0` |
| **M6** (substrate-free) | `M` is defined for every full-support `p̂ ∈ Δ(X)`, or declared undefined by an explicit rule |
| **M8** (contexts) | with contexts (Def. [[Def 9\|9]]), `M` applies per context `c`, with aggregates `Σ_c ρ(c)·M_c` for the deployment and evaluation context laws `ρ_dep`, `ρ_ev` |

Two further conditions bind **the R7 refactor**, not a measure as such:
- **M7:** every refactored measure coincides with its v6.4 counterpart whenever the dropped assumptions hold.
- **M9:** the sanity suite of `verify.py` V30 passes.

## Notes and checks

*Note (mechanism-relative comparisons).* A comparison between a mechanism and the same mechanism run on the
target (Def. [[Def 14|14]]) depends on the attributed mechanism and resource. So it fails M4 by construction, and it is
an explanation-layer quantity, not a misalignment measure (Prop. [[Prop 25|25]]).

*Note (R7-2: the reference in M5).* M5 exempts intensity **relative to the declared reference** `q`. An agent
pursuing the target from its own default `q_A` is exempt only if its default leans along the target,
`log(q_A/q) = aF + c` with `β + a ≥ 0` (Prop. [[Prop 26|26]](c)). Otherwise its default is part of what it does, and it
registers. Attributing that departure to the default rather than to the evaluator is an explanation-layer
question.

*Note (a limit of any behavioural measure).* M4 and M5 together exempt only **systematic intensity**. An agent
that pursues the target but errs unsystematically — noise, slips — is behaviourally misdirected, and every
measure satisfying M4 must register it as such. Separating "wrong objective" from "unsystematic error" needs
an actor model: the explanation layer, not the measurement layer.

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Def 9]] — contexts

## Used by
- [[Prop 30]] — the fake-alignment gap; R7-4

## Mentions
- [[Def 14]] — mechanism-relative comparison; explanation layer; R7-1
- [[Prop 25]] — mechanism-relative comparisons against the contract; tier 1 given the attribution
- [[Prop 26]] — reference misspecification is measured misalignment; R7-2

## Mentioned in
- [[Def 10]] — intent ray and misalignment measures; v6.4, R7-0
- [[Def 13]] — actor models; R7-1
- [[Overview 0]] — alignment instance — static, single-target module; not a definition — the formal definition is Definition 12

## Checks
- none

## Sources
- none

## Retractions touching this note
- none
<!-- /gen:links -->

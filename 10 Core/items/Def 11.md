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
depends_on: ["Def 17", "Def 18", "Def 9"]
mentions: ["Def 14", "Def 19", "Prop 25", "Prop 26", "Prop 31", "Prop 34"]
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

**Definition 11 (the misalignment contract; R7-0, restated for target sets in R7-7).** A **misalignment measure**
assigns to a target set `𝒯` (Def. [[Def 17|17]]; by default the cardinal set `[F]₊` of a non-constant target `F`), a
declared convention `κ`, and a full-support actual behaviour `p̂` a value `M ∈ [0, ∞]`, or declares it undefined. It
must satisfy:

| | Axiom |
|---|---|
| **M1** (identity) | `M = 0` iff `p̂` is an intended behaviour under `κ`: for a target set under the budget or free convention, iff `p̂ ∈ I_κ(𝒯)` |
| **M2** (sign) | `M ≥ 0` |
| **M3** (representation) | `M` depends on the target only through the declared set `𝒯`, and every declared quantity carrying the unit of a representative is transformed with it (`β ↦ β/a` when `F ↦ aF + c`). For `[F]₊` this is invariance under `F ↦ aF + c`, `a > 0`; for `[F]_ord`, under every strictly increasing map |
| **M4** (behavioural) | `M` depends on the agent only through `p̂`, or its per-context laws |
| **M5** (misdirection, not intensity) | if `p̂ = p_{G,t}` for some `G ∈ 𝒯` and `t ≥ 0`, within the declared cap if there is one (Def. [[Def 18\|18]]) — the agent pursues an admissible statement of the target, at an intended intensity — then `M = 0`. For `[F]₊` with no cap this reads `p̂ = p_{F,t}` |
| **M6** (substrate-free) | `M` is defined for every full-support `p̂ ∈ Δ(X)`, or declared undefined by an explicit rule |
| **M8** (contexts) | with contexts (Def. [[Def 9\|9]]), `M` applies per context `c`, with aggregates `Σ_c ρ(c)·M_c` for the deployment and evaluation context laws `ρ_dep`, `ρ_ev` |

Two further conditions bind **the R7 refactor**, not a measure as such:
- **M7:** every refactored measure coincides with its v6.4 counterpart whenever the dropped assumptions hold.
- **M9:** the sanity suite of `verify.py` V30 passes.

## Notes and checks

*Note (R7-9).* Every axiom here is a condition on the declared intended set `𝓘` (Def. [[Def 19|19]]): M1, M2, M4 and M6 hold
for any `𝓘` closed in `Δ°`; M5 says `𝓘` contains the declared pursuit family; M3 says `𝓘` depends on the target only
through the declared set (Prop. [[Prop 34|34]](b)).

*Note (R7-7).* Until R7-7 the contract took a single non-constant target `F`, and M1, M3 and M5 referred to it.
With `𝒯 = [F]₊` each reads exactly as before, so every measure that satisfied the contract still does (M7).
What the target set adds is the declaration of how much of `F` is intended: its exchange rates (`[F]₊`) or
only its order (`[F]_ord`). The measures for any target set are in Prop. [[Prop 31|31]].


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
- [[Def 17]] — target sets; R7-7
- [[Def 18]] — intensity caps and distributional targets; R7-6a

## Used by
- [[Prop 30]] — the fake-alignment gap; R7-4
- [[Prop 31]] — target sets against the contract; R7-7
- [[Prop 33]] — capped measures against the contract; R7-6a
- [[Prop 34]] — the core as a declared intended set; R7-9

## Mentions
- [[Def 14]] — mechanism-relative comparison; explanation layer; R7-1
- [[Def 19]] — declared intended set; R7-9
- [[Prop 25]] — mechanism-relative comparisons against the contract; tier 1 given the attribution
- [[Prop 26]] — reference misspecification is measured misalignment; R7-2
- [[Prop 31]] — target sets against the contract; R7-7
- [[Prop 34]] — the core as a declared intended set; R7-9

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

---
id: "Def 9"
type: "definition"
title: "contexts"
section: "Core 09 Observation what an overseer can detect"
order: 48
layer: "measurement"
tier: []
assumes: []
status: "definition"
depends_on: []
mentions: ["B07", "Prop 19"]
checks: []
sources: []
aliases: ["Definition 9", "Def. 9"]
updated: "2026-09-26"
---
# Def 9 — contexts
<!-- gen:header -->
> [!abstract] Definition · definition · in [[Core 09 Observation what an overseer can detect]]
<!-- /gen:header -->

## Statement

**Definition 9 (contexts).** Let `𝒞` be a finite set of contexts. Each context `c` has a reference
`q(·|c)`, a target `F(c,·)`, an actual behaviour `p̂_c` (any full-support distribution), and the intended
behaviour `p*_c = p_{F(c,·),β}(·|c)`. Contexts are drawn from an **evaluation** distribution `ρ_ev` when the
overseer samples, and from a **deployment** distribution `ρ_dep` in use. Contexts are exogenous: the actor does
not choose `c`.

## Notes and checks

*Note.* Under (E) per context, `p̂_c = p_{F̂(c,·),β}(·|c)` for an evaluator `F̂(c,·)`. v6.4 built this into the
definition.

*Note.* This is the same structure as the closed-loop lift of [[B07|B7]], with contexts in the role
of disturbances; [[B07|B7(d)]] is Prop. [[Prop 19|19]](i). The two differ only in what varies: [[B07|B7]] measures capacity against a
single reference across disturbances; here each context carries its own reference.

<!-- gen:links -->
## Depends on (logical: statement and proof)
- none

## Used by
- [[B12]] — Human choice — logit, defaults, rational inattention, present bias *(new in v6.2)*
- [[Def 11]] — the misalignment contract; R7-0
- [[Def 12]] — alignment instance; formal
- [[Def 16]] — external reward, contingency and coupling; R7-4
- [[Prop 19]] — the evaluation gap
- [[Prop 24]] — the v6.4 measures against the contract; tier 1
- [[Prop 30]] — the fake-alignment gap; R7-4
- [[Prop 31]] — target sets against the contract; R7-7
- [[Prop 33]] — capped measures against the contract; R7-6a
- [[Prop 34]] — the core as a declared intended set; R7-9

## Mentions
- [[B07]] — Ashby (requisite variety); Conant & Ashby (good regulator)
- [[Prop 19]] — the evaluation gap

## Mentioned in
- [[Def 22]] — value shortfall at equal effort; R8-1
- [[Def 23]] — the declaration; R8-2

## Checks
- none

## Sources
- none

## Retractions touching this note
- none
<!-- /gen:links -->

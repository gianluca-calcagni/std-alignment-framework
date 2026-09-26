---
id: "Def 14"
type: "definition"
title: "mechanism-relative comparison; explanation layer; R7-1"
section: "Core 09 Observation what an overseer can detect"
order: 53
layer: "explanation"
tier: []
assumes: []
status: "definition"
depends_on: ["Def 13"]
mentions: []
checks: []
sources: []
aliases: ["Definition 14", "Def. 14"]
updated: "2026-09-26"
---
# Def 14 — mechanism-relative comparison; explanation layer; R7-1
<!-- gen:header -->
> [!abstract] Definition · definition · in [[Core 09 Observation what an overseer can detect]]
<!-- /gen:header -->

## Statement

**Definition 14 (mechanism-relative comparison; explanation layer; R7-1).** Let the actual behaviour be
attributed to an actor model `A` (Def. [[Def 13|13]]) with the actor's reference `q_A` and resource `r`:
`p̂ = A(F̂; q_A, r)`. The **mechanism-relative intended behaviour** is `A(F; q_A, r)`: the same mechanism, run on
the target, from the same reference, with the same resource. Define

```
R_own = E_{A(F;q_A,r)}F − E_{p̂}F        (value units),
M_own = KL(p̂ ‖ A(F; q_A, r))            (nats; when A(F; q_A, r) has full support).
```

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Def 13]] — actor models; R7-1

## Used by
- [[C07]] — The actor model *(the weakest joint for the AI substrate; tiers corrected in v6.4)*
- [[Prop 25]] — mechanism-relative comparisons against the contract; tier 1 given the attribution

## Mentions
- none

## Mentioned in
- [[Def 8]] — conventions, misalignment, ε-alignment; revised in R7-0
- [[Def 11]] — the misalignment contract; R7-0
- [[Def 13]] — actor models; R7-1
- [[Prop 18]] — harm bounds detectability

## Checks
- none

## Sources
- none

## Retractions touching this note
- [[R075]]
<!-- /gen:links -->

---
id: "Def 1"
type: "definition"
title: "objects"
section: "Core 01 Setting"
order: 2
layer: "measurement"
tier: []
assumes: []
status: "definition"
depends_on: []
mentions: ["Def 13"]
checks: []
sources: []
aliases: ["Definition 1", "Def. 1"]
updated: "2026-09-26"
---
# Def 1 — objects
<!-- gen:header -->
> [!abstract] Definition · definition · in [[Core 01 Setting]]
<!-- /gen:header -->

## Statement

**Definition 1 (objects).**

| Symbol | Object |
|---|---|
| `q` | the **declared reference**: the default behaviour against which intended pursuit of the target is defined. It is part of the specification of intent, like the target and the convention (R7-2) |
| `F` | the **target** |
| `β ∈ (0, ∞]` | the **exchange rate** between value and information (inverse temperature) |
| `p_{G,t} ∝ q·e^{tG}` | the Gibbs tilt of `q` by `G` at `t ∈ ℝ`; `p_{G,∞} := q(· \| argmax G)` |
| `p^r_{G,t} ∝ r·e^{tG}` | the same tilt of any other full-support reference `r`; `p_{G,t} = p^q_{G,t}` |
| `p* = p_{F,β}` | the **intended behaviour** at price `β`: the entropic counterfactual |
| `p̂` | the **actual behaviour**: *any* full-support distribution on `X`. No actor model is assumed (R7-1) |
| `osc(G) = max G − min G` | oscillation |

## Notes and checks

*Note (R7-2, R7-3).* Everything here belongs to the **measurement layer**: the declared reference, the target,
the price, the Gibbs family, and the intended and actual behaviour. The evaluator `F̂ = F + E`, the error `E`, its
cumulant generating functions `Λ`, `Λ_q`, and the actor's own default `q_A` belong to the **explanation layer**
(Def. [[Def 13|13]]). Until R7-3 the evaluator and error were defined here; until R7-2 one `q` served as both the declared
and the actor's reference.

<!-- gen:links -->
## Depends on (logical: statement and proof)
- none

## Used by
- [[B12]] — Human choice — logit, defaults, rational inattention, present bias *(new in v6.2)*
- [[Def 12]] — alignment instance; formal
- [[Def 17]] — target sets; R7-7
- [[Prop 12]] — what behaviour identifies

## Mentions
- [[Def 13]] — actor models; R7-1

## Mentioned in
- [[Def 10]] — intent ray and misalignment measures; v6.4, R7-0
- [[Overview 0]] — alignment instance — static, single-target module; not a definition — the formal definition is Definition 12

## Checks
- none

## Sources
- none

## Retractions touching this note
- none
<!-- /gen:links -->

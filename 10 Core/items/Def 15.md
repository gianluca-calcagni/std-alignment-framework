---
id: "Def 15"
type: "definition"
title: "the capacity model; R7-3"
section: "Core 04 Capacity"
order: 16.5
layer: "explanation"
tier: []
assumes: []
status: "definition"
depends_on: ["Def 13", "Def 5", "Def 2"]
mentions: ["Hyp C"]
checks: []
sources: []
aliases: ["Definition 15", "Def. 15"]
updated: "2026-09-26"
---
# Def 15 — the capacity model; R7-3
<!-- gen:header -->
> [!abstract] Definition · definition · in [[Core 04 Capacity]]
<!-- /gen:header -->

## Statement

**Definition 15 (the capacity model; R7-3).** The **capacity model** is the actor model (Def. 13) that
returns the capacity actor of Def. 5, `A(G; q, δ) = p^C_G`, with the budget `δ` as its resource.

**Hypothesis (C).** The actual behaviour is the capacity model run on the evaluator: `p̂ = p^C_{F̂}`. Under
(C) the regret is `R^C = J_F(p^C_F) − J_F(p^C_{F̂})`.

## Notes and checks

*Note.* Stated in Def. [[Def 5|5]] until R7-3, and moved here so that Def. 5 stays in the measurement layer. The capacity set
is a KL ball around the declared reference. A capacity actor constrained around its own reference has no clean
transfer ([[Hyp C]]).

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Def 2]] — the bounded actor
- [[Def 5]] — capacity actor
- [[Def 13]] — actor models; R7-1

## Used by
- [[C02]] — The width is the exact worst case (Thm 5, Lemma 5.1, Prop. 6)
- [[C03]] — Non-separability (Lemma 8, Thm 9)
- [[Cor 17.1]] — the capacity actor's regret is the budget convention
- [[Prop 7]] — a bound with realized travel from the reference
- [[Rem 7.1]] — historical note: the v5 normal form
- [[Thm 5]] — the width is the exact worst case

## Mentions
- [[Hyp C]] — the capacity actor model

## Mentioned in
- [[Def 5]] — capacity actor
- [[Def 12]] — alignment instance; formal
- [[Def 13]] — actor models; R7-1

## Checks
- none

## Sources
- none

## Retractions touching this note
- none
<!-- /gen:links -->

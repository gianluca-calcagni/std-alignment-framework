---
id: "Def 12"
type: "definition"
title: "alignment instance; formal"
section: "Core 09 Observation what an overseer can detect"
order: 52
layer: "measurement"
tier: []
assumes: []
status: "definition"
depends_on: ["Def 1", "Def 8", "Def 9", "Def 10"]
mentions: ["Cor 5.2", "Def 13", "Def 15", "Def 7", "Prop 16"]
checks: []
sources: []
aliases: ["Definition 12", "Def. 12"]
updated: "2026-09-26"
---
# Def 12 — alignment instance; formal
<!-- gen:header -->
> [!abstract] Definition · definition · in [[Core 09 Observation what an overseer can detect]]
<!-- /gen:header -->

## Statement

**Definition 12 (alignment instance; formal; measurement layer since R7-3).** An **alignment instance** is a
tuple `(X, q, F, κ)`, with a price `β ∈ (0, ∞)` when `κ` is the price convention:
- a finite behaviour set `X` with a full-support **declared** reference `q` (standing assumption S);
- a non-constant target `F` (Def. [[Def 1|1]]);
- a convention `κ` (Def. [[Def 8|8]]).

Optionally, it also has contexts (Def. [[Def 9|9]]). Given an actual behaviour `p̂`, an instance determines every
misalignment measure (Def. [[Def 10|10]]).

## Notes and checks

*Note.* By Cor. [[Cor 5.2|5.2]], one resource suffices for the soft actor or the pure capacity actor. The target proper is
the positive-affine class `[F]₊`. An instance fixes a representative only when it reports value-unit or
price-convention quantities (Prop. [[Prop 16|16]], Def. [[Def 7|7]]). No principal is assumed: the target can be teleonomic, such as
fitness.

*Note (R7-3).* An **explanation** of an instance adds an evaluator `F̂`, an actor model `A`, the actor's own
reference `q_A` and the model's resource (Def. [[Def 13|13]]; the capacity model and its budget `δ`, Def. [[Def 15|15]]). Until
R7-3 the instance itself contained `F̂` and a resource `R`. Neither is needed to measure misalignment: the
budget measure matches the actual behaviour's own divergence, and the free measure needs no resource.

<!-- gen:links -->
## Depends on (logical: statement and proof)
- [[Def 1]] — objects
- [[Def 8]] — conventions, misalignment, ε-alignment; revised in R7-0
- [[Def 9]] — contexts
- [[Def 10]] — intent ray and misalignment measures; v6.4, R7-0

## Used by
- none

## Mentions
- [[Cor 5.2]] — the exchange rate is a shadow price
- [[Def 7]] — reporting rule
- [[Def 13]] — actor models; R7-1
- [[Def 15]] — the capacity model; R7-3
- [[Prop 16]] — gauge group and identified quantities

## Mentioned in
- [[Overview 0]] — alignment instance — static, single-target module; not a definition — the formal definition is Definition 12

## Checks
- none

## Sources
- none

## Retractions touching this note
- none
<!-- /gen:links -->

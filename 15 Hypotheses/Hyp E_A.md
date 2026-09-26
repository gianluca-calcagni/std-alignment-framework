---
id: "Hyp E_A"
type: "hypothesis"
title: "the entropic actor model from the actor's own reference"
defined_in: ["Def 13"]
assumed_by: ["Prop 12", "Prop 16", "Prop 26", "Rem 16.1"]
aliases: ["(E_A)", "Hypothesis (E_A)"]
updated: "2026-09-26"
---
# Hyp E_A — the entropic actor model from the actor's own reference
<!-- gen:header -->
> [!important] Hypothesis about the actual actor · assumed by 4 results
<!-- /gen:header -->

## Statement

The actual behaviour is the entropic model run on the evaluator from the actor's own full-support reference
`q_A`: `p̂ = p^{q_A}_{F̂,β}`. Hypothesis (E) is the special case `q_A = q`, where `q` is the declared reference.

## Where it is defined

[[Def 13]] (R7-2). This note is an index. The authoritative statement is in [[Def 13]].

## What it adds, and what it cannot

By [[Prop 26]](a), every (E) result holds under (E_A) with the error replaced by `E + log(q_A/q)/β`. So (E_A)
adds no new *predictions* about behaviour. It adds an *attribution*: part of the departure is ascribed to the
actor's default rather than to its evaluator. Behaviour alone cannot confirm that attribution
([[Prop 26]](b), [[Prop 12]](ii)). Default experiments under exclusion can ([[B12]]).

<!-- gen:links -->
## Assumed by
- [[Prop 12]] — what behaviour identifies
- [[Prop 16]] — gauge group and identified quantities
- [[Prop 26]] — reference misspecification is measured misalignment; R7-2
- [[Rem 16.1]] — reference misspecification
<!-- /gen:links -->

---
id: "Hyp E"
type: "hypothesis"
title: "the entropic actor model"
defined_in: ["Def 13"]
assumed_by: ["Cor 1.1", "Cor 1.2", "Cor 1.3", "Cor 1.4", "Cor 1.5", "Cor 13.1", "Cor 13.3", "Cor 13.4", "Prop 2", "Prop 3", "Prop 4", "Prop 11", "Prop 14", "Rem 13.5"]
aliases: ["(E)", "Hypothesis (E)"]
updated: "2026-09-26"
---
# Hyp E — the entropic actor model
<!-- gen:header -->
> [!important] Hypothesis about the actual actor · assumed by 14 results
<!-- /gen:header -->

## Statement

The actual behaviour is the entropic model run on the evaluator from the **declared** reference:
`p̂ = p_{F̂,β}`. That is, the actor's own reference equals the declared one, `q_A = q`. The general case is
[[Hyp E_A]] (R7-2).

## Where it is defined

[[Def 13]] (actor models). This note is an index. The authoritative statement is in [[Def 13]], and the two must agree.

## Why it is a hypothesis and not a definition

Since R7-1 the actual behaviour is any distribution. Results that need `p̂` to be a Gibbs tilt of the evaluator carry the tag *[Assumes (E).]* in their statement; `tools/vault.py lint` fails if one does not. Under (E), behaviour identifies the evaluator only up to the gauge of [[Prop 12]] and [[Prop 16]]. Every (E) result
also holds under (E_A), with the effective error of [[Prop 26]](a).

<!-- gen:links -->
## Assumed by
- [[Cor 1.1]]
- [[Cor 1.2]] — the optimality gap is a symmetric divergence
- [[Cor 1.3]] — CGF and integral forms
- [[Cor 1.4]] — historical note: why v5 found "tight to about 2×"
- [[Cor 1.5]] — stacked stages compose additively
- [[Cor 13.1]]
- [[Cor 13.3]] — rescaling is purely axial
- [[Cor 13.4]] — second order
- [[Prop 2]] — sharp error-only bound
- [[Prop 3]] — only the upper tail matters
- [[Prop 4]] — an error confined to one region saturates
- [[Prop 11]] — the order is structural, not a matter of tightness
- [[Prop 14]]
- [[Rem 13.5]] — whether rescaling is harmful depends on the declared convention; v6.3
<!-- /gen:links -->

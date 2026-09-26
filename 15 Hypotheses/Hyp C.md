---
id: "Hyp C"
type: "hypothesis"
title: "the capacity actor model"
defined_in: ["Def 15"]
assumed_by: ["Cor 17.1"]
aliases: ["(C)", "Hypothesis (C)"]
updated: "2026-09-26"
---
# Hyp C — the capacity actor model
<!-- gen:header -->
> [!important] Hypothesis about the actual actor · assumed by 1 results
<!-- /gen:header -->

## Statement

The actual behaviour is the capacity model run on the evaluator: `p̂ = p^C_{F̂}`, the maximizer of `J_{F̂}` over `C_δ = {p : KL(p‖q) ≤ δ}`.

## Where it is defined

[[Def 15]] (since R7-3; it was in [[Def 5]] before). This note is an index. The authoritative statement is in [[Def 15]].

## Reference (R7-2)

The capacity set `C_δ` is a KL ball around the **declared** reference `q`. A capacity actor constrained around
its own reference `q_A` has no clean transfer like [[Prop 26]](a): its optimum `p^{q_A}_{F̂,λ}` absorbs
`log(q_A/q)/λ`, with `λ` depending on the budget. So (C) is stated only with `q_A = q`. Results under (C) do not
extend to own-reference capacity actors without a separate argument.

<!-- gen:links -->
## Assumed by
- [[Cor 17.1]] — the capacity actor's regret is the budget convention
<!-- /gen:links -->

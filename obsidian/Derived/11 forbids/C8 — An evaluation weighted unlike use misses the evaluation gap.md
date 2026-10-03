---
kind: corollary
id: C8
aliases: ["C8"]
source: "derived/forbids.md"
---
# C8 — An evaluation weighted unlike use misses the evaluation gap
> [!info] Generated from [derived/forbids.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/forbids.md#c8--an-evaluation-weighted-unlike-use-misses-the-evaluation-gap). Edit the source, not this note.

## Statement
When each condition is judged on its own terms, the misalignment in use exceeds the misalignment in an
evaluation that meets the conditions in other proportions by exactly `Γ = Σ_c (ρ_dep(c) − ρ_ev(c))·M_c` ([[P24 — The evaluation gap|P24]]). An
evaluation that over-samples the conditions where the actor is closest to its specification understates the
misalignment in use.

## In plain terms
An evaluation that meets easy situations more often than real use does reports less misalignment
than real use has, by a computable amount.

## Proof
[[P24 — The evaluation gap|P24]](ii); over-sampling the conditions with the smaller `M_c` makes `Γ` positive.

## Lineage
v7.10: §11.8 and Prop 19.

## Checks
- [`checks/test_estimation.py::test_the_evaluation_gap`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_estimation.py)

## Depends on
- [[P24 — The evaluation gap|P24]] — The evaluation gap

## Used by
- no later item

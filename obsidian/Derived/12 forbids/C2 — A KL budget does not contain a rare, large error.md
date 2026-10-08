---
kind: corollary
id: C2
aliases: ["C2"]
source: "derived/forbids.md"
---
# C2 — A KL budget does not contain a rare, large error
> [!info] Generated from [derived/forbids.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/forbids.md#c2--a-kl-budget-does-not-contain-a-rare-large-error). Edit the source, not this note.

## Statement
For every budget `δ > 0` and every number `B`, there are a default and an error `E` with `Var_q(E) = 1`
whose largest rise over the departure budget `δ` ([[P27 — The best use of a departure budget|P27]]) exceeds `B`, while its largest rise over the `χ²` budget `δ` is
at most `δ^{1/2}`.

## In plain terms
Limiting how far an actor departs in KL does not limit the damage of an error that is rare but
large, however small the error's variance; limiting it in `χ²` does.

## Proof
[[P31 — Budgets of other shapes|P31]](vi) with the variance held at `1`: the KL rise is at least `min(1, δ/log(1/r))·M·(1 − r)` with
`M = (r·(1 − r))^{−1/2}`, which grows without bound as `r → 0`, and the `χ²` rise is at most `(δ·1)^{1/2}`.

## Lineage
v7.10: §11.2 and Prop 11, in the form on finite outcomes of [[P31 — Budgets of other shapes|P31]](vi).

## Checks
- [`checks/test_feasibility.py::test_feasible_sets_of_other_shapes`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_feasibility.py)

## Depends on
- [[P27 — The best use of a departure budget|P27]] — The best use of a departure budget
- [[P31 — Budgets of other shapes|P31]] — Budgets of other shapes

## Used by
- no later item

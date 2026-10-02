---
kind: premise
id: A3
aliases: ["A3"]
source: "CORE.md"
---
# A3 — Pursuit is the best trade-off
> [!info] Generated from [CORE.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/CORE.md#a3--pursuit-is-the-best-trade-off). Edit the source, not this note.

## Statement
To pursue an objective at an intensity is to choose the behaviour with the largest average of the
objective minus a cost of departing from the default, priced at the reciprocal of the intensity. With the default
fixed, the cost depends only on the behaviour, and is differentiable.

## In plain terms
Pursuing harder means accepting more cost of change for more of what is pursued. The cost of change
depends only on how the behaviour changes, not on what is pursued.

## Why this choice
- *It says what intensity means.* The reciprocal of the intensity is the price of one nat of departure, in the
  objective's units: an actor that pursues intensely treats departure as cheap.
- *Together with A2 it fixes the cost.* The steepest climb is also the best trade-off for exactly one cost: the KL
  divergence from the default (`derived/value.md`). A2 is a geometric premise and A3 an economic one; they agree in one
  way only.

## Lineage
v7.10: Def 2 (the bounded actor, with the KL cost assumed) and Thm 1. New: the cost is derived, not
assumed.

## Depends on
- nothing

## Used by
- [[D3 — Specification, declaration and misalignment|D3]] — Specification, declaration and misalignment
- [[D10 — Evaluator, regression and residual|D10]] — Evaluator, regression and residual
- [[D11 — Sample and evidence|D11]] — Sample and evidence

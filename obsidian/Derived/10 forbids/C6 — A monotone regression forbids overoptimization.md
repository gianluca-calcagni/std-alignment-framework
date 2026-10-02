---
kind: corollary
id: C6
aliases: ["C6"]
source: "derived/forbids.md"
---
# C6 — A monotone regression forbids overoptimization
> [!info] Generated from [derived/forbids.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/forbids.md#c6--a-monotone-regression-forbids-overoptimization). Edit the source, not this note.

## Statement
If the regression of the objective on an evaluator is non-decreasing in it ([[D10 — Evaluator, regression and residual|D10]]), no path from `q`
whose revealed objectives are non-decreasing in the evaluator lowers the objective's average. In particular, none does
when the regression is affine with a non-negative slope.

## In plain terms
If, under the default, outcomes the evaluator scores higher are never worse on average for the
principal, following the evaluator harder never hurts the principal on average.

## Proof
[[P19 — A monotone regression rules out overoptimization|P19]]; an affine function with a non-negative slope is non-decreasing.

## Notes
The archive's form was a target and an evaluator jointly Gaussian under the default, which have an affine
regression; on finitely many outcomes, the affine case is what remains of it.

## Lineage
v7.10: §11.6, Prop 21 and the dictionary's B §4.

## Checks
- [`checks/test_evaluator.py::test_a_monotone_regression_rules_out_overoptimization`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_evaluator.py)

## Depends on
- [[D10 — Evaluator, regression and residual|D10]] — Evaluator, regression and residual
- [[P19 — A monotone regression rules out overoptimization|P19]] — A monotone regression rules out overoptimization

## Used by
- no later item

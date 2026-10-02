---
kind: corollary
id: C11
aliases: ["C11"]
source: "derived/forbids.md"
---
# C11 — No recovery after the fall
> [!info] Generated from [derived/forbids.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/forbids.md#c11--no-recovery-after-the-fall). Edit the source, not this note.

## Statement
If the regression of the objective on an evaluator is single-peaked, then along the pursuit of the
evaluator, and along best-of-`n`, the objective's average never falls and then rises again ([[P25 — The target's curve turns no more often than the regression|P25]](iii) and its Notes).

## In plain terms
When the evaluator's scores are worth more to the principal up to a point and less beyond it,
pushing harder on the evaluator can help and then hurt, but it never helps again after it has started to hurt.

## Proof
[[P25 — The target's curve turns no more often than the regression|P25]](iii), and its Notes for best-of-`n`.

## Lineage
v10: [[P25 — The target's curve turns no more often than the regression|P25]]. New as a forbidden statement.

## Checks
- [`checks/test_evaluator.py::test_the_target_curve_turns_no_more_often_than_the_regression`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_evaluator.py)

## Depends on
- [[P25 — The target's curve turns no more often than the regression|P25]] — The target's curve turns no more often than the regression

## Used by
- no later item

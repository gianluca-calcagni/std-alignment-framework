---
kind: corollary
id: C1
aliases: ["C1"]
source: "derived/forbids.md"
---
# C1 — No ranking of errors holds at every budget
> [!info] Generated from [derived/forbids.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/forbids.md#c1--no-ranking-of-errors-holds-at-every-budget). Edit the source, not this note.

## Statement
Let `E₁` and `E₂` be the errors of two evaluators known in the objective's units ([[P29 — The width is the exact worst case|P29]]), with
`Var_q(E₁) > Var_q(E₂)` and `max E₁ − min E₁ < max E₂ − min E₂`. Then `w_δ(E₁) > w_δ(E₂)` for every small enough budget
`δ`, and `w_δ(E₁) < w_δ(E₂)` for every `δ` at least as large as each `−log q(argmax E_i)` and `−log q(argmin E_i)`. So
the worst case of the objective lost ([[P29 — The width is the exact worst case|P29]](ii)) ranks the two errors one way at small budgets and the other way at
large ones.

## In plain terms
An error that is spread out and an error that is rare but large cannot be ranked once and for all.
Under a small budget of departure the spread-out error does more damage; under a large one, the rare large error does.

## Proof
By [[P28 — The width of a departure budget|P28]](ii), `w_δ(E) = 2·(2δ·Var_q(E))^{1/2} + O(δ^{3/2})`, so the larger variance gives the larger width
for small `δ`. By [[P28 — The width of a departure budget|P28]](iii), once `δ` reaches both ends of `E`, `w_δ(E)` is the range of `E`, so the larger range gives
the larger width. By [[P29 — The width is the exact worst case|P29]](ii), the width is the worst case of the objective lost.

## Notes
The archive also measured the crossing for actual optimizers, not only for the worst case: for the pursuit
of the evaluator, best-of-`n` and policy gradient, at different departures for each (v7.10: R5, R6). Those are its
measurements; the core proves the crossing for the worst case only, and a worked case could test the rest.

## Lineage
v7.10: §11.1, Thm 9 and the boundary claim C8 (crossing curves). The core's form uses [[P28 — The width of a departure budget|P28]] and [[P29 — The width is the exact worst case|P29]].

## Checks
- [`checks/test_forbids.py::test_no_ranking_of_errors_holds_at_every_budget`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_forbids.py)

## Depends on
- [[P28 — The width of a departure budget|P28]] — The width of a departure budget
- [[P29 — The width is the exact worst case|P29]] — The width is the exact worst case

## Used by
- no later item

---
kind: corollary
id: C4
aliases: ["C4"]
source: "derived/forbids.md"
---
# C4 — Rescaling the objective is not misalignment
> [!info] Generated from [derived/forbids.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/forbids.md#c4--rescaling-the-objective-is-not-misalignment). Edit the source, not this note.

## Statement
An actor that pursues `s·F` from `q`, for any `s > 0` and any intensity, has misalignment `0` and stakes
`0` under the standard specification of `F`.

## In plain terms
Pursuing the objective harder or more gently than someone else would is not pursuing the wrong
thing.

## Proof
`tilt(q, t·s·F) = p_{F, t·s}` is on the pursuit ray ([[D2 — Pursuit of an objective|D2]]), so its misalignment is `0` ([[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]](ii)) and its
stakes are `0` ([[P9 — What is at stake|P9]](iv)).

## Notes
The archive found that rescaling costs something only when the intended behaviour is required to keep the
actor's price of departing, the price convention the core does not use.

## Lineage
v7.10: §11.4, Cor 13.3 and Remark 13.5.

## Checks
- [`checks/test_misalignment.py::test_zero_exactly_on_the_intended_set`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_misalignment.py)
- [`checks/test_stakes.py::test_zero_stakes`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_stakes.py)

## Depends on
- [[D2 — Pursuit of an objective|D2]] — Pursuit of an objective
- [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]] — Misalignment is attained, and zero exactly on the intended behaviours and their limits
- [[P9 — What is at stake|P9]] — What is at stake

## Used by
- no later item

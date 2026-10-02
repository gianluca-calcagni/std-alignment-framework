---
kind: corollary
id: C12
aliases: ["C12"]
source: "derived/forbids.md"
---
# C12 — No misalignment, no stakes
> [!info] Generated from [derived/forbids.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/forbids.md#c12--no-misalignment-no-stakes). Edit the source, not this note.

## Statement
Under the standard specification of a non-constant `F`, `M(p̂) = 0` implies `S(p̂) = 0`; and the stakes
are `0` with a positive misalignment only when the actor puts all its mass on the outcomes where `F` is largest, split
otherwise than the default splits them ([[P9 — What is at stake|P9]](iv)).

## In plain terms
An actor that does what was intended loses nothing of the objective. The only way to lose nothing
while being misaligned is to choose only best outcomes, in proportions of one's own.

## Proof
[[P9 — What is at stake|P9]](iv).

## Lineage
v8: [[P9 — What is at stake|P9]](iv). New as a forbidden statement.

## Checks
- [`checks/test_stakes.py::test_zero_stakes`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_stakes.py)

## Depends on
- [[P9 — What is at stake|P9]] — What is at stake

## Used by
- no later item

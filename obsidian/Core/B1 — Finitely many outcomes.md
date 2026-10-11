---
kind: background condition
id: B1
aliases: ["B1"]
source: "CORE.md"
---
# B1 — Finitely many outcomes
> [!info] Generated from [CORE.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/CORE.md#b1--finitely-many-outcomes). Edit the source, not this note.

## Statement
The outcomes of a decision are finitely many.

## In plain terms
Whatever happens is sorted into one of finitely many results that a record can tell apart.

## Status
A background condition, assumed without loss of generality for every quantity that finite descriptions
determine.

## Why this choice
- *A record decides finitely many events.* A record of finitely many decisions, each read at finite precision, settles
  which of finitely many results occurred, and nothing finer. The outcomes are the possibilities of a domain in which
  every statement about one decision is decidable, and such a domain is discrete [[References|@carcassi2021]]: finitely many outcomes
  are the general case of what a finite record can tell apart.
- *Nothing a record measures is lost.* On outcomes that are not finite, the divergence is the supremum of its values
  over finite descriptions, so each misalignment the framework reports there is a limit of misalignments on finitely
  many outcomes (`CORE-GENERAL.md`, GA1 and GD3; `general/dictionary.md`). What does not carry over, the existence of
  nearest behaviours, heavy tails and atoms, is listed there, and is the qualifier of this condition.
- *Exactness.* Every statement can be proved with finite sums and checked exactly on random instances.

## Lineage
v12: [[A1 — Behaviour suffices|A1]]'s "finitely many outcomes" and [[D1 — Outcomes, behaviours, divergence and tilt|D1]]'s first reason; new as a condition in v13.

## Depends on
- nothing

## Used by
- [[B2 — Episodes and conditions as outcomes|B2]] — Episodes and conditions as outcomes
- [[D4 — Resolution|D4]] — Resolution

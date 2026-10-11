---
kind: imported axiom
id: M1
aliases: ["M1"]
source: "CORE.md"
---
# M1 — Probability on finitely many outcomes
> [!info] Generated from [CORE.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/CORE.md#m1--probability-on-finitely-many-outcomes). Edit the source, not this note.

## Statement
On a finite set, a probability gives each element a non-negative mass, and the masses add up to one. The
probability of a subset is the sum of the masses of its elements; given a subset of positive probability, the
probability of another is the probability of their intersection divided by that of the first. The average of a function
is the sum of its values, each weighted by its mass.

## In plain terms
Shares of a whole: each thing that can happen gets a share, the shares add up to one, and an
average weighs each value by its share.

## Status
Imported from probability theory as it is: Kolmogorov's axioms in their finite case, where additivity over
countably many sets reduces to finite sums. It assumes nothing about actors or principals.

## Why this choice
- *It is the mathematics of ensembles.* Decisions can be mixed: an actor that acts one way on a share `a` of occasions
  and another way on the rest acts as their mixture with weights `a` and `1 − a`. With finitely many outcomes that
  exclude each other, every ensemble is one such mixture of the outcomes, in one way only, so the ensembles are the
  points of a simplex, as classical ensembles are, and an average is an affine function of the ensemble, as statistical
  quantities are [[References|@carcassi2026e]].
- *Nothing more is needed.* Every result of the finite core uses finite sums. The general core replaces the sums by
  integrals against a measure, and ratios of masses by densities (`CORE-GENERAL.md`).

## Lineage
New in v13: used silently before, in [[D1 — Outcomes, behaviours, divergence and tilt|D1]].

## Depends on
- nothing

## Used by
- [[D1 — Outcomes, behaviours, divergence and tilt|D1]] — Outcomes, behaviours, divergence and tilt

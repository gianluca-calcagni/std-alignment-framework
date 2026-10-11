---
kind: imported axiom
id: M2
aliases: ["M2"]
source: "CORE.md"
---
# M2 — Independent repetition
> [!info] Generated from [CORE.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/CORE.md#m2--independent-repetition). Edit the source, not this note.

## Statement
Decisions drawn independently from one probability have, jointly, the product of their probabilities.
The share of an outcome `x` among `n` such decisions has average `p(x)` and variance `p(x)·(1 − p(x))/n`, so it lies
within `ε > 0` of `p(x)` with probability at least `1 − p(x)·(1 − p(x))/(n·ε²)`.

## In plain terms
When decisions do not influence each other, the shares in a long record come as close as one likes
to the actor's behaviour, with a known chance of missing.

## Status
Imported from probability theory: independence as the product of probabilities. The bound is Chebyshev's
inequality, shown below; nothing else is imported.

## Why this choice
- *It is the bridge from records to behaviours.* A behaviour is never observed; the shares in a record are. This is what
  lets a record verify a behaviour to any precision, in the statistical sense, and why section 2 reads a behaviour as
  the shares over unboundedly many decisions.
- *The bound, in one line.* The share is the average of `n` independent indicators, each of average `p(x)` and variance
  `p(x)·(1 − p(x))`, so its variance is `p(x)·(1 − p(x))/n`, and Chebyshev's inequality bounds the chance of a
  deviation of at least `ε` by that variance over `ε²`.

## Lineage
New in v13: before, part of [[D11 — Record, sample and evidence|D11]]'s reasons.

## Depends on
- nothing

## Used by
- [[M3 — Imported theorems|M3]] — Imported theorems
- [[D1 — Outcomes, behaviours, divergence and tilt|D1]] — Outcomes, behaviours, divergence and tilt
- [[D11 — Record, sample and evidence|D11]] — Record, sample and evidence
- [[P55 — What a record of counts certifies, at every size|P55]] — What a record of counts certifies, at every size

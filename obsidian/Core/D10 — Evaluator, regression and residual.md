---
kind: definition
id: D10
aliases: ["D10"]
source: "CORE.md"
---
# D10 — Evaluator, regression and residual
> [!info] Generated from [CORE.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/CORE.md#d10--evaluator-regression-and-residual). Edit the source, not this note.

## Statement
Let `F` be the principal's objective, which this section calls the target. An **evaluator** is an
objective `F̂ : X → ℝ` put forward as the one the actor pursues: known, when it is a function the actor is rewarded on,
or revealed, when it is read from a full-support actual behaviour `p̂` as `F̂ = log(p̂/q)`; as the objective of a
pursuit at some intensity, a revealed evaluator is fixed only up to a positive factor and an added constant. Let `𝒱` be
the resolution whose cells are the level sets of `F̂` ([[D4 — Resolution|D4]]). The **regression** of the target on the evaluator is the
cell average `m = E_q[F|𝒱]`, and the **residual** is `R = F − m`.

## In plain terms
The evaluator is what the actor actually works toward: a reward it is paid on, a measure it is
judged by, or, when nothing else is known, the objective its own behaviour reveals. The regression is what the
evaluator tells, on average under the default, about the principal's objective; the residual is the part of the
principal's objective that the evaluator does not see.

## Why this choice
- *It adds no assumption.* By [[A3 — Pursuit is the best trade-off|A3]] and [[P1 — Every behaviour is a tilt of any other|P1]], every full-support behaviour is the best trade-off for one objective,
  `log(p̂/q)` at intensity 1, fixed up to a constant ([[P1 — Every behaviour is a tilt of any other|P1]](ii)): every actor has a revealed evaluator. A known evaluator
  is a hypothesis about the actor, which behaviour can test ([[P1 — Every behaviour is a tilt of any other|P1]], [[P3 — A fixed objective is visible in the changes of behaviour|P3]]).
- *It is the actor's counterpart of the principal's objective.* The principal declares a pursuit of `F` from `q`; the
  actor reveals a pursuit of `F̂` from the same `q`. Misalignment compares two pursuits from one default, in one
  currency.
- *It is universal.* A reward model in fine-tuning, selection through one sex, a fine, a report card, a measured bonus:
  each ontology has one.
- *The residual, not the difference.* The difference `F̂ − F`, v7.10's evaluator error, depends on the scale of `F̂`,
  which behaviour never identifies. The regression and the residual depend on `F̂` only through its level sets, and
  whether the regression rises with `F̂` only through their order: neither changes under an increasing transformation
  of `F̂`. The residual averages to zero in every cell of `𝒱` under the default, so an actor that sees outcomes only
  through the evaluator can neither gain nor lose through it (`derived/evaluator.md`).
- *Regression in the statistical sense.* `m` is the best predictor of `F` from `F̂` in mean square under the default.

## Notes
The evaluator is a proxy or reward model in machine learning, a performance measure in the economics of
incentives, and the fitness of a selection regime in biology. Goodhart's law is about the gap between an evaluator and
a target; the residual separates the part of that gap that an actor seeing only the evaluator cannot exploit. When
`F̂` gives distinct outcomes distinct values, every cell of `𝒱` is a single outcome, so `m = F` and `R = 0`. The
regression says more than the target itself only when the evaluator is coarser than the outcomes, as a test passed or
failed, a grade, a count or an indicator is.

## Lineage
v7.10: Def 13 (`F̂ = F + E`, an evaluator and its error `E`) and Def 12's note (an explanation adds an
evaluator). New: the revealed evaluator, and the regression and residual in place of the error, which needed a scale.

## Depends on
- [[A3 — Pursuit is the best trade-off|A3]] — Pursuit is the best trade-off
- [[D4 — Resolution|D4]] — Resolution
- [[P1 — Every behaviour is a tilt of any other|P1]] — Every behaviour is a tilt of any other
- [[P3 — A fixed objective is visible in the changes of behaviour|P3]] — A fixed objective is visible in the changes of behaviour

## Used by
- [[P18 — Through the evaluator, only the regression counts|P18]] — Through the evaluator, only the regression counts
- [[P25 — The target's curve turns no more often than the regression|P25]] — The target's curve turns no more often than the regression
- [[P26 — The regression on bins governs at small intensity|P26]] — The regression on bins governs at small intensity
- [[P29 — The width is the exact worst case|P29]] — The width is the exact worst case
- [[P33 — Error bounds for a known evaluator|P33]] — Error bounds for a known evaluator
- [[C6 — A monotone regression forbids overoptimization|C6]] — A monotone regression forbids overoptimization

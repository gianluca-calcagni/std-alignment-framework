---
kind: definition
id: D1
aliases: ["D1"]
source: "CORE.md"
---
# D1 — Outcomes, behaviours, divergence and tilt
> [!info] Generated from [CORE.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/CORE.md#d1--outcomes-behaviours-divergence-and-tilt). Edit the source, not this note.

## Statement
`X` is a finite set of **outcomes**, with at least two elements. A **behaviour** is a probability
distribution `p` on `X`. `Δ` is the set of behaviours, and `Δ°` the set of **full-support** behaviours, those with
`p(x) > 0` for every `x`. For `p ∈ Δ` and `F : X → ℝ`, `E_p[F] = Σ_x p(x)·F(x)` and `Var_p(F) = E_p[F²] − E_p[F]²`, and
`Cov_p(F, G) = E_p[F·G] − E_p[F]·E_p[G]`; for a set `C ⊆ X` with `p(C) > 0`, `p(·|C)` is `p` conditioned on `C`. For
`p, r ∈ Δ`, the **Kullback–Leibler divergence** is `KL(p‖r) = Σ_{x : p(x) > 0} p(x)·log(p(x)/r(x))`, which is finite
when `r(x) > 0` wherever `p(x) > 0`, and `+∞` otherwise. The **tilt** of `r ∈ Δ°` by `F : X → ℝ` is the behaviour
`tilt(r, F) = r·e^F / E_r[e^F]`.

## In plain terms
Outcomes are the things that can happen, and a behaviour says how often each one happens; full
support means that nothing is ruled out entirely. KL measures how far one behaviour is from another; it is not
symmetric, so the order matters. Tilting reweights a behaviour toward the outcomes that a function scores higher.

## Why this choice
- *Finite outcomes.* Every statement can then be proved with finite sums, and checked exactly on random instances.
  General outcome spaces add conditions (absolute continuity, integrability of `e^F`, and compactness in the existence
  arguments). They come back when an item needs them.
- *Full support, where it is needed.* It keeps every logarithm finite. A behaviour that rules an outcome out, such as a
  deterministic one, is still a behaviour: it is allowed as the first argument of KL, and it is a limit of full-support
  behaviours.
- *Behaviour is any distribution* ([[A1 — Behaviour suffices|A1]]). No model of how an actor produces its behaviour is assumed. The core measures
  behaviour; how it is produced is not part of it.
- *KL and the tilt are notation here.* The items that use them argue that they are the right tools.

## Notes
A behaviour is a policy in reinforcement learning, a mixed strategy in game theory, a distribution of choices
in economics, and a distribution of types in a population in biology. The tilt is exponential tilting in statistics.

## Lineage
v7.10: Def 1 (the objects), and R7-1's rule that the actual behaviour is any distribution (Def 13). v7.10's
R7-8 (measurable spaces) stays deferred, as it was there.

## Depends on
- [[A1 — Behaviour suffices|A1]] — Behaviour suffices

## Used by
- [[C5 — The first effect of optimization depends on the optimizer; its end, on the evaluator's top|C5]] — The first effect of optimization depends on the optimizer; its end, on the evaluator's top

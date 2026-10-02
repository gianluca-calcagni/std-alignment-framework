---
kind: corollary
id: C5
aliases: ["C5"]
source: "derived/forbids.md"
---
# C5 — The first effect of optimization depends on the optimizer; its end, on the evaluator's top
> [!info] Generated from [derived/forbids.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/forbids.md#c5--the-first-effect-of-optimization-depends-on-the-optimizer-its-end-on-the-evaluators-top). Edit the source, not this note.

## Statement
Let `F̂` be an evaluator and `F` the objective.
(i) Along any path of behaviours from `q`, the objective's average starts to move at the rate `Cov_q(F_0, F)`, where
`F_0` is the path's first revealed objective; along the pursuit of `F̂`, at the rate `Cov_q(F̂, F)`.
(ii) One step of softmax policy gradient on `E_p[F̂]`, from the logits `log q`, is the tilt of `q` by `η·g` with
`g = q·(F̂ − E_q[F̂])`: it first pursues the evaluator weighted by the default. Its rate is
`η·Σ_x q(x)²·(F̂(x) − E_q[F̂])·(F(x) − E_q[F])`, which can have the opposite sign to `Cov_q(F̂, F)`.
(iii) Along the pursuit of `F̂`, the objective's average tends to its average under `q` over the outcomes where `F̂` is
largest, which is `max F` exactly when `F` is largest at all of them.

## In plain terms
Whether pushing on an evaluator helps at first depends on how one pushes: the plain pursuit of the
evaluator and a gradient step can start in opposite directions. Where pushing hard ends depends only on the outcomes
the evaluator scores highest.

## Proof
(i) is [[P13 — What the start of a change gains|P13]](i), with [[P20 — Where overoptimization starts, and how it ends|P20]](i) for the pursuit. (ii) The derivative of `E_{softmax(θ)}[F̂]` in the logit
`θ(x)` is `p(x)·(F̂(x) − E_p[F̂])`; at `θ = log q` it is `g`, and the logits `log q + η·g` give `tilt(q, η·g)` ([[D1 — Outcomes, behaviours, divergence and tilt|D1]]).
The revealed objective of `η ↦ tilt(q, η·g)` at `η = 0` is `g − E_q[g]`, so by (i) the rate is
`η·Cov_q(g, F) = η·Σ_x q(x)²·(F̂(x) − E_q[F̂])·(F(x) − E_q[F])`. The check exhibits instances where it and
`Cov_q(F̂, F)` have opposite signs. (iii) is [[P20 — Where overoptimization starts, and how it ends|P20]](ii): the limit is the regression at the largest value of `F̂`, which
is `max F` exactly when `F = max F` on that level set, since `q` gives each outcome positive mass.

## Lineage
v7.10: §11.5, Prop 14 (initial and terminal effects) and Prop 22 (the first-order effect of any smooth
optimizer). New: the gradient step as the pursuit of `q·(F̂ − E_q[F̂])`.

## Checks
- [`checks/test_forbids.py::test_the_first_effect_depends_on_the_optimizer`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_forbids.py)

## Depends on
- [[D1 — Outcomes, behaviours, divergence and tilt|D1]] — Outcomes, behaviours, divergence and tilt
- [[P13 — What the start of a change gains|P13]] — What the start of a change gains
- [[P20 — Where overoptimization starts, and how it ends|P20]] — Where overoptimization starts, and how it ends

## Used by
- no later item

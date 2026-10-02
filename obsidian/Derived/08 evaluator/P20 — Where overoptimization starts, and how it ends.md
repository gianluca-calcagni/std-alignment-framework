---
kind: proposition
id: P20
aliases: ["P20"]
source: "derived/evaluator.md"
---
# P20 — Where overoptimization starts, and how it ends
> [!info] Generated from [derived/evaluator.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/evaluator.md#p20--where-overoptimization-starts-and-how-it-ends). Edit the source, not this note.

## Statement
Let `F̂` be a non-constant evaluator, with regression `m`, and let `p_t = tilt(q, t·F̂)` be its pursuit.
Write `v_1 > v_2` for the two largest values of `F̂`, and `m(v_1)`, `m(v_2)` for the regression on their level sets.
(i) `d/dt E_{p_t}[F] = Cov_{p_t}(F̂, m) = Cov_{p_t}(F̂, F)`: the target's average is stationary exactly where, under the
current behaviour, the evaluator stops correlating with the target.
(ii) As `t → ∞`, `E_{p_t}[F] → m(v_1)`. If `m(v_2) > m(v_1)`, then `E_{p_t}[F]` is decreasing for all large enough `t`;
if `m(v_2) < m(v_1)`, it is increasing for all large enough `t`.

## In plain terms
Following the evaluator, the principal's objective stops improving exactly where, among the
outcomes the actor now favours, the evaluator no longer says anything about it. At very high effort, the objective
settles at its average over the outcomes the evaluator scores highest. If the outcomes it scores just below those are
better for the principal, pushing harder eventually does harm.

## Proof
(i) The pursuit is limited to `𝒱`, so `E_{p_t}[F] = E_{p_t}[m]` ([[P18 — Through the evaluator, only the regression counts|P18]](i)); its revealed objective is `F̂ −
E_{p_t}[F̂]`, so [[P13 — What the start of a change gains|P13]](i) gives `Cov_{p_t}(F̂, m)`. And `Cov_{p_t}(F̂, R) = E_{p_t}[F̂·R] = 0`, since `F̂` is constant
on each cell, where `p_t` splits mass as `q` does and `R` averages to zero. (ii) Let `a_j` be the default's mass on the
level set of the `j`-th largest value `v_j`, and `π_j(t) = a_j·e^{t·v_j} / Σ_k a_k·e^{t·v_k}`. Then `E_{p_t}[F] = Σ_j
π_j(t)·m(v_j)`, and `π_1(t) → 1`, which gives the limit. By the pairwise form of the covariance in the proof of [[P19 — A monotone regression rules out overoptimization|P19]],
`Cov_{p_t}(F̂, m) = Σ_{j<k} π_j·π_k·(v_j − v_k)·(m(v_j) − m(v_k))`. As `t` grows, `π_1 → 1`, and `π_j/π_2 → 0` for `j ≥
3`, so every term other than `j = 1, k = 2` becomes negligible next to `π_1·π_2·(v_1 − v_2)·(m(v_1) − m(v_2))`, whose
sign is that of `m(v_1) − m(v_2)`.

## Notes
(i) gives a stopping rule: stop where target and evaluator become uncorrelated under the current behaviour.
Karwowski et al. derive an early-stopping rule for proxy optimization in the geometry of occupancy measures
[[References|@karwowski2024]]; whether the two rules coincide is not yet checked (`TERMS.md`, section 2). (ii) says that what decides
the end is the regression at the top of the evaluator's range, which the default may sample rarely. Before the limit, a
third value close to the second can still dominate the sign, as the check shows in log space.

## Lineage
v7.10: Prop 14 (the initial and terminal effects of optimization). New: the stationarity condition in the
regression, and the terminal rule.

## Checks
- [`checks/test_evaluator.py::test_overoptimization_starts_where_correlation_ends_and_ends_at_the_top`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_evaluator.py)

## Depends on
- [[P13 — What the start of a change gains|P13]] — What the start of a change gains
- [[P18 — Through the evaluator, only the regression counts|P18]] — Through the evaluator, only the regression counts
- [[P19 — A monotone regression rules out overoptimization|P19]] — A monotone regression rules out overoptimization

## Used by
- [[C5 — The first effect of optimization depends on the optimizer; its end, on the evaluator's top|C5]] — The first effect of optimization depends on the optimizer; its end, on the evaluator's top

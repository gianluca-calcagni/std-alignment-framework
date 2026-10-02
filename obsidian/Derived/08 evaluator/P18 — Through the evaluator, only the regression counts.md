---
kind: proposition
id: P18
aliases: ["P18"]
source: "derived/evaluator.md"
---
# P18 — Through the evaluator, only the regression counts
> [!info] Generated from [derived/evaluator.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/evaluator.md#p18--through-the-evaluator-only-the-regression-counts). Edit the source, not this note.

## Statement
Let `F̂` be an evaluator for the objective `F`, with regression `m`, residual `R` and resolution `𝒱` of
its level sets ([[D10 — Evaluator, regression and residual|D10]]).
(i) `E_q[R] = 0`, and for every behaviour `p` limited to `𝒱` ([[D4 — Resolution|D4]]), `E_p[R] = 0` and `E_p[F] = E_p[m]`.
(ii) For every full-support `p`, with `w = p/q`,
`E_p[F] − E_q[F] = Cov_q(w, m) + Cov_q(w, R)`, and `Cov_q(w, R) = E_p[R]`: the target's gain is the regression's gain
plus the residual's.
(iii) For every injective `h : ℝ → ℝ`, the evaluator `h(F̂)` has the same regression and residual as `F̂`; and if `h` is
increasing, `m` rises with `h(F̂)` exactly when it rises with `F̂`.

## In plain terms
An actor that sees outcomes only through the evaluator changes the principal's objective only
through what the evaluator tells about it: the residual, the part the evaluator does not see, averages to zero for any
such actor. For any actor at all, the objective's gain splits into the gain along the regression and the gain in the
residual. And none of this depends on the evaluator's scale, or on any relabelling of its values that keeps them
distinct.

## Proof
(i) On each cell `C` of `𝒱`, `m` equals `E_{q(·|C)}[F]`, so `E_{q(·|C)}[R] = 0`, and averaging over the cells
gives `E_q[R] = 0`. A behaviour `p` limited to `𝒱` splits each cell as `q` does, so `E_p[R] = Σ_C p(C)·E_{q(·|C)}[R] =
0`, and `E_p[F] = E_p[m] + E_p[R] = E_p[m]`; this is [[P8 — An actor that cannot tell outcomes apart|P8]](i) with `𝒜 = 𝒱`. (ii) Since `E_q[w] = 1`, `Cov_q(w, G) =
E_p[G] − E_q[G]` for every `G`; apply it to `F = m + R`, and use `E_q[R] = 0`. (iii) An injective `h` maps distinct
values to distinct values, so `h(F̂)` has the same level sets as `F̂`, hence the same `𝒱`, `m` and `R`; an increasing
`h` also keeps their order.

## Notes
(ii) is v7.10's Prop 20 (Goodhart as a covariance, for any actor) with the regression and the residual in
place of a scaled error. The second term is where an actor that sees more than the evaluator can gain or lose: through
distinctions that the evaluator does not make. By [[P12 — What interventions reveal|P12]](ii), such distinctions show in the revealed objectives of its
changes.

## Lineage
v7.10: Prop 20 and Def 13. New: the split into regression and residual, and its invariance.

## Checks
- [`checks/test_evaluator.py::test_through_the_evaluator_only_the_regression_counts`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_evaluator.py)

## Depends on
- [[D4 — Resolution|D4]] — Resolution
- [[D10 — Evaluator, regression and residual|D10]] — Evaluator, regression and residual
- [[P8 — An actor that cannot tell outcomes apart|P8]] — An actor that cannot tell outcomes apart

## Used by
- [[P19 — A monotone regression rules out overoptimization|P19]] — A monotone regression rules out overoptimization
- [[P20 — Where overoptimization starts, and how it ends|P20]] — Where overoptimization starts, and how it ends
- [[P25 — The target's curve turns no more often than the regression|P25]] — The target's curve turns no more often than the regression

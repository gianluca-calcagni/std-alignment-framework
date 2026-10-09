---
kind: proposition
id: P3
aliases: ["P3"]
source: "derived/tilts-and-paths.md"
---
# P3 — A fixed objective is visible in the changes of behaviour
> [!info] Generated from [derived/tilts-and-paths.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/tilts-and-paths.md#p3--a-fixed-objective-is-visible-in-the-changes-of-behaviour). Edit the source, not this note.

## Statement
Let `s ↦ p_s` be a continuously differentiable path in `Δ°`, over an interval containing `0`, with
revealed objective `F_s = ∂_s log p_s`, and let `F` be non-constant.
(i) There is a differentiable `τ` with `τ(0) = 0` and `p_s = tilt(p_0, τ(s)·F)` for every `s` if and only if
`F_s ∈ span{F, 1}` for every `s`. Then `F_s = τ'(s)·F + c(s)`.
(ii) The path pursues `F` ([[D2 — Pursuit of an objective|D2]]) if and only if, for every `s`, `F_s = a(s)·F + b(s)` with `a(s) ≥ 0`.

## In plain terms
Whether a changing behaviour keeps one fixed objective can be read from its changes alone: every
change must point along that objective, apart from a constant. It pursues the objective when it never moves against it.
Two changes that point in opposite directions lie on one line, but they are not one pursuit.

## Proof
(i) If `p_s = tilt(p_0, τ(s)·F)`, then `log p_s = log p_0 + τ(s)·F − log E_{p_0}[e^{τ(s)F}]`, so
`F_s = τ'(s)·F + c(s)`, with `c(s)` minus the derivative of the log-normalizer. Conversely, let `F_s = a(s)·F + b(s)`
for every `s`. Since `F` is not constant, `F` and `1` are linearly independent, so `a` and `b` are determined by `F_s`,
and they are continuous because the path is continuously differentiable. Integrating from `0` gives
`log p_s = log p_0 + τ(s)·F + B(s)`, with `τ(s) = ∫_0^s a` and `B(s) = ∫_0^s b`, and normalization gives
`p_s = tilt(p_0, τ(s)·F)`.
(ii) By (i), the path has the form of [[D2 — Pursuit of an objective|D2]] exactly when `F_s = a(s)·F + b(s)`, and then `τ' = a`. So `τ` is
non-decreasing if and only if `a` is never negative.

## Notes
The condition `F_s ∈ span{F, 1}` is the precise form of "the increments have rank 1", which [[P12 — What interventions reveal|P12]] uses for
interventions. The sign condition in (ii) is what a rank read on lines, not on rays, misses. With only two outcomes,
`span{F, 1}` contains every function, so every path keeps a fixed objective: the test has content only with three or
more outcomes. (In v7.10, this is why a two-arrangement allele-frequency series could not test the rank.) In population
genetics a fixed objective is constant selection, and a turning one is fluctuating selection; in economics the question
is whether preferences are stable.

## Lineage
New as a proposition. v7.10: ROADMAP §6 I1 (the dynamic rank), and the I1-dyn and I1-dyn2 tests, whose null
hypothesis counted opposite-pointing increments as one evaluator.

## Checks
- [`checks/test_paths.py::test_fixed_objective_iff_span`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_paths.py)
- [`checks/test_paths.py::test_two_outcomes_always_keep_a_fixed_objective`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_paths.py)

## Depends on
- [[D2 — Pursuit of an objective|D2]] — Pursuit of an objective

## Used by
- [[D10 — Evaluator, regression and residual|D10]] — Evaluator, regression and residual

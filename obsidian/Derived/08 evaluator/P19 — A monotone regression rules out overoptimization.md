---
kind: proposition
id: P19
aliases: ["P19"]
source: "derived/evaluator.md"
---
# P19 — A monotone regression rules out overoptimization
> [!info] Generated from [derived/evaluator.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/evaluator.md#p19--a-monotone-regression-rules-out-overoptimization). Edit the source, not this note.

## Statement
Let `F̂` be an evaluator whose regression `m` is non-decreasing in it: `m(x) ≤ m(y)` whenever `F̂(x) ≤
F̂(y)`. Let `s ↦ p_s`, for `s ≥ 0`, be a continuously differentiable path in `Δ°` with `p_0 = q`, whose revealed
objectives `F_s` ([[P2 — Every change of behaviour follows a replicator equation|P2]]) are, at every `s`, non-decreasing in `F̂` in the same sense. Then `s ↦ E_{p_s}[F]` is
non-decreasing.

## In plain terms
If, under the default, outcomes the evaluator scores higher are never worse on average for the
principal, then an actor that follows the evaluator, or anything that rises with it, harder and harder, never makes the
principal worse off on average. Pursuing the evaluator itself, or any increasing transformation of it, and picking
the best of more and more samples are all covered.

## Proof
Each `F_s` is constant on the level sets of `F̂`, so `log(p_s/q) = ∫_0^s F_u du` is too, and every `p_s` is
limited to `𝒱`. By [[P18 — Through the evaluator, only the regression counts|P18]](i), `E_{p_s}[F] = E_{p_s}[m]`, and by [[P13 — What the start of a change gains|P13]](i), applied to `m`, its derivative is
`Cov_{p_s}(F_s, m)`. For any behaviour `p` and two functions `f`, `g` that are both non-decreasing in `F̂`,
`Cov_p(f, g) = ½·Σ_{x,y} p(x)·p(y)·(f(x) − f(y))·(g(x) − g(y)) ≥ 0`, since the two differences never have opposite signs
(Chebyshev's association inequality). So the derivative is never negative.

## Notes
It generalizes v7.10's Prop 21, where the regression is affine, and v7.10's B §4, where target and evaluator
are jointly Gaussian. Monotonicity is a property of the default's joint law of target and evaluator, so it can be
checked before any optimization. The check shows that, without it, overoptimization is common. For an evaluator with
distinct values on distinct outcomes, `m = F` ([[D10 — Evaluator, regression and residual|D10]], Notes), and the hypothesis asks that `F̂` never score an outcome
above another that the target strictly prefers.
Best-of-`n`, the best of `n` draws from `q` by `F̂` as a path in a real `n ≥ 1`, stays in `Δ°`, and its revealed
objective is non-decreasing in `F̂`. On the level set of `v`, with `A` and `B` the default's mass of `F̂ ≤ v` and of
`F̂ < v`, it is `(A^n·log A − B^n·log B)/(A^n − B^n)`, with `0·log 0 = 0`: the average of `log u` over `[B, A]` with
weight `u^{n−1}`, plus `1/n`. Keeping only the outcomes above a threshold leaves `Δ°`, so it is not such a path, but the
conclusion holds for it directly: raising the threshold drops the level sets with the lowest regression.

## Lineage
v7.10: Prop 21 and B §4. New: the monotone case, and the proof by association.

## Checks
- [`checks/test_evaluator.py::test_a_monotone_regression_rules_out_overoptimization`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_evaluator.py)

## Depends on
- [[P2 — Every change of behaviour follows a replicator equation|P2]] — Every change of behaviour follows a replicator equation
- [[P13 — What the start of a change gains|P13]] — What the start of a change gains
- [[P18 — Through the evaluator, only the regression counts|P18]] — Through the evaluator, only the regression counts

## Used by
- [[P20 — Where overoptimization starts, and how it ends|P20]] — Where overoptimization starts, and how it ends
- [[P26 — The regression on bins governs at small intensity|P26]] — The regression on bins governs at small intensity
- [[C6 — A monotone regression forbids overoptimization|C6]] — A monotone regression forbids overoptimization

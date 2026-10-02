---
kind: proposition
id: P26
aliases: ["P26"]
source: "derived/evaluator.md"
---
# P26 — The regression on bins governs at small intensity
> [!info] Generated from [derived/evaluator.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/evaluator.md#p26--the-regression-on-bins-governs-at-small-intensity). Edit the source, not this note.

## Statement
Let `F̂` be an evaluator, and `G = h(F̂)` with `h` constant on each of finitely many disjoint intervals
that cover the values of `F̂`, and increasing from one interval to the next: `G` groups the values of `F̂` into bins.
Let `m_G` be the regression of `F` on `G` ([[D10 — Evaluator, regression and residual|D10]]), `w` the largest spread of `F̂` within a bin (its largest value there
minus its smallest), and `D` the largest spread of `F` within a bin. Along the pursuit `p_t = tilt(q, t·F̂)` of `F̂`
itself, for every `t ≥ 0`:
(i) `|E_{p_t}[F] − E_{p_t}[m_G]| ≤ t·w·D/4`.
(ii) If `m_G` is non-decreasing in `G`, then `E_{p_u}[F] ≥ E_{p_s}[F] − (s + u)·w·D/4` for all `0 ≤ s ≤ u`.
(iii) If `m_G` is single-peaked in `G`, then `t ↦ E_{p_t}[m_G]` never falls and then rises again ([[P25 — The target's curve turns no more often than the regression|P25]](iii)), and
`E_{p_t}[F]` stays within `t·w·D/4` of it.

## In plain terms
An evaluator that scores every outcome differently has a regression equal to the objective itself,
so the regression is read, in practice, from bins of scores. Pursuing the evaluator keeps the principal's average within
`t·w·D/4` of its average under that bin-wise regression, where `w` is the width of the bins in the evaluator's units
and `D` the spread of the objective inside a bin. So, while that margin is small next to the changes of the average
that matter, the bin-wise regression decides: if it rises, pursuit does not hurt beyond the margin, and if it rises and
then falls, so does the principal's average, up to the margin.

## Proof
Each bin `b` is a union of level sets of `F̂`, and `m_G = E_q[F|b]` on it, so
`E_{p_t}[F] − E_{p_t}[m_G] = Σ_b p_t(b)·(E_{p_t}[F|b] − E_q[F|b])`. Within `b`, `p_t(·|b) = tilt(q(·|b), t·F̂)`, a path
from `q(·|b)` whose revealed objective is `F̂` centred, so by [[P13 — What the start of a change gains|P13]](i)
`E_{p_t}[F|b] − E_q[F|b] = ∫_0^t Cov_{r_s}(F̂, F) ds`, with `r_s = tilt(q(·|b), s·F̂)`. By Cauchy–Schwarz,
`|Cov_r(F̂, F)| ≤ Var_r(F̂)^{1/2}·Var_r(F)^{1/2}`, and a function whose values on `b` lie in an interval of length `d`
has variance at most `d²/4` under any behaviour on `b`, the mean square distance to the interval's midpoint
(Popoviciu's inequality). So each term is at most `t·(w/2)·(D/2)`, and so is their average, which proves (i).
(ii) As a function on outcomes, `m_G` is constant on the level sets of `F̂` and non-decreasing in `F̂`, so its
regression on `F̂` is itself, and [[P19 — A monotone regression rules out overoptimization|P19]] gives `E_{p_u}[m_G] ≥ E_{p_s}[m_G]`; (i) at `s` and at `u` gives the rest.
(iii) In the same way, the regression of `m_G` on `F̂` is `m_G`, single-peaked in `F̂`, and [[P25 — The target's curve turns no more often than the regression|P25]](iii) applies; (i)
gives the margin.

## Notes
The bound is attained to first order in `t` by a bin with two equally likely outcomes at the ends of both
spreads; random instances stay well inside it. It trades resolution against reach: narrower bins make `w` smaller but
leave fewer outcomes, and fewer sampled ones ([[D11 — Sample and evidence|D11]]), in each bin, so the bin-wise regression is estimated with more
error. With one outcome per bin, `w = 0` and (i) is exact, as [[D10 — Evaluator, regression and residual|D10]]'s Notes say: the regression is then the target. The
bound covers the pursuit of `F̂`, not best-of-`n`; for best-of-`n` the natural width of a bin is in units of
`log Q(F̂)`, the log of the default's mass below a value, which is open (`NOTES.md` E8).

## Lineage
v7.10: Prop 2 (Popoviciu's bound on the variance). New (`NOTES.md` E8).

## Checks
- [`checks/test_evaluator.py::test_binned_evaluators`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_evaluator.py)

## Depends on
- [[D10 — Evaluator, regression and residual|D10]] — Evaluator, regression and residual
- [[P13 — What the start of a change gains|P13]] — What the start of a change gains
- [[P19 — A monotone regression rules out overoptimization|P19]] — A monotone regression rules out overoptimization
- [[P25 — The target's curve turns no more often than the regression|P25]] — The target's curve turns no more often than the regression

## Used by
- [[P33 — Error bounds for a known evaluator|P33]] — Error bounds for a known evaluator

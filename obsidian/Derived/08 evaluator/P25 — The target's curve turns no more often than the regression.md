---
kind: proposition
id: P25
aliases: ["P25"]
source: "derived/evaluator.md"
---
# P25 — The target's curve turns no more often than the regression
> [!info] Generated from [derived/evaluator.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/evaluator.md#p25--the-targets-curve-turns-no-more-often-than-the-regression). Edit the source, not this note.

## Statement
Let `F̂` be an evaluator with values `v_1 < … < v_k`, let `a_j` be the default's mass on the level set of
`v_j` and `m_j` the regression there ([[D10 — Evaluator, regression and residual|D10]]), and for every real `t` let `p_t = tilt(q, t·F̂)`: the pursuit of `F̂` at
intensity `t` when `t ≥ 0`, and of `−F̂` at intensity `−t` when `t < 0`.
(i) For every number `c`, the function `t ↦ E_{p_t}[F] − c` changes sign on `ℝ` at most as many times as the sequence
`m_1 − c, …, m_k − c` does, its zero terms left out. As `t → −∞` it has the sign of the first non-zero term of that
sequence, and as `t → +∞` the sign of the last.
(ii) If the regression is non-decreasing in `F̂`, then `t ↦ E_{p_t}[F]` is non-decreasing on `ℝ`.
(iii) If the regression is single-peaked, `m_1 ≤ … ≤ m_i ≥ … ≥ m_k` for some `i`, then for all `s < t < u`,
`E_{p_t}[F] ≥ min(E_{p_s}[F], E_{p_u}[F])`: once the target's average has fallen, it never rises again.

## In plain terms
Line up the evaluator's scores from lowest to highest, and write next to each the principal's
average objective over the outcomes with that score. Pursuing the evaluator harder smooths that list: the principal's
average can cross any level no more often than the list does. If the list only rises, pursuit never hurts. If it rises
and then falls, pursuit can help and then hurt, but only once: there is no recovery after the fall.

## Proof
By [[P18 — Through the evaluator, only the regression counts|P18]](i), `E_{p_t}[F] = Σ_j a_j·m_j·e^{t·v_j} / Σ_j a_j·e^{t·v_j}`, so `E_{p_t}[F] − c` has the sign of
`f(t) = Σ_j c_j·e^{t·v_j}`, with `c_j = a_j·(m_j − c)` of the sign of `m_j − c`. (i) Laguerre's rule of signs
[[References|@polya1976]], proved here: an exponential sum `Σ_j c_j·e^{t·v_j}`, with `v_1 < … < v_k` and real coefficients not all
zero, has at most as many real zeros, counted with multiplicity, as its coefficients have sign changes. By induction on
the number `s` of sign changes: if `s = 0`, all non-zero terms have one sign and there is no zero. Otherwise take `μ`
strictly between the exponents of two consecutive non-zero coefficients of opposite signs. Then `g = e^{−μt}·f` has the
zeros of `f`, and `g' = Σ_j (v_j − μ)·c_j·e^{(v_j − μ)·t}` has coefficients with `s − 1` sign changes, since the factor
`v_j − μ` flips the signs of exactly the terms before `μ`. By Rolle's theorem `g'` has at least one zero fewer than `g`,
so `g` has at most `s`. A function with at most `s` zeros changes sign at most `s` times. As `t → +∞` the non-zero term
with the largest exponent dominates, and as `t → −∞` the one with the smallest. (ii) For every `c`, the non-zero terms
of `m_j − c` are negative and then positive. By (i), `f` is either of one sign, or negative and then positive with one
simple zero; so `{t : E_{p_t}[F] > c}` is empty, `ℝ`, or a half-line `(t_0, ∞)`. If `E_{p_s}[F] > E_{p_u}[F]` for some
`s < u`, a `c` strictly between them would put `s` in that set and not `u`. (iii) Suppose `s < t < u` with
`E_{p_t}[F] < c < min(E_{p_s}[F], E_{p_u}[F])`, so that `f` takes the signs `+`, `−`, `+` at `s`, `t`, `u`. For a
single-peaked regression, the indices with `m_j > c` are consecutive, so the non-zero terms of `m_j − c` are negative,
then positive, then negative, some groups possibly empty. With two sign changes, the sequence starts and ends negative,
so by (i) `f` has at most two zeros and is negative at both ends: it is negative throughout, or negative, positive on
one interval, and negative again, and `+`, `−`, `+` is impossible. With at most one sign change, `f` changes sign at
most once, which `+`, `−`, `+` needs twice.

## Notes
(i) is the variation-diminishing property of the exponential kernel, a case of total positivity. It holds for
the pursuit of any increasing transformation of `F̂`, which has the same level sets in the same order, and so for the
pursuit of ranks. Best-of-`n`, as a path in a real `n ≥ 1`, obeys (ii) and (iii) too: with `A_j` the default's mass of
`F̂ ≤ v_j`, its average is `E_n[F] − c = (m_k − c) + Σ_{j<k} (m_j − m_{j+1})·A_j^n`, an exponential sum in `n` with
exponents `log A_1 < … < log A_k = 0`. For a single-peaked regression its coefficients are negative, then positive, then
of the sign of `m_k − c`, and the argument of (iii) applies. [[P20 — Where overoptimization starts, and how it ends|P20]](ii) gives where a single-peaked curve ends; (iii)
adds that it gets there with one turn at most. For an evaluator that scores every outcome differently, the sequence
`m_j` is the target itself in the evaluator's order, and (i) is a bound on noisy data; [[P26 — The regression on bins governs at small intensity|P26]] gives its bin-wise form.

## Lineage
New (`NOTES.md` E8). v7.10: Prop 14 (initial and terminal effects) said where the curve starts and ends;
nothing on its shape in between.

## Checks
- [`checks/test_evaluator.py::test_the_target_curve_turns_no_more_often_than_the_regression`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_evaluator.py)

## Depends on
- [[D10 — Evaluator, regression and residual|D10]] — Evaluator, regression and residual
- [[P18 — Through the evaluator, only the regression counts|P18]] — Through the evaluator, only the regression counts

## Used by
- [[P26 — The regression on bins governs at small intensity|P26]] — The regression on bins governs at small intensity
- [[C11 — No recovery after the fall|C11]] — No recovery after the fall

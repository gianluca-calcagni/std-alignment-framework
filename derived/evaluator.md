# Derived — the evaluator

What an evaluator ([D10]) does to the principal's objective when the actor pursues it. Through the evaluator, only the
regression of the target on it counts ([P18]). A regression that rises with the evaluator rules out overoptimization
([P19]). Otherwise, overoptimization starts where the evaluator stops telling anything about the target under the
current behaviour, and at high intensity it is decided by the evaluator's two highest values ([P20]).

### P18 — Through the evaluator, only the regression counts
**Statement.** Let `F̂` be an evaluator for the objective `F`, with regression `m`, residual `R` and resolution `𝒱` of
its level sets ([D10]).
(i) `E_q[R] = 0`, and for every behaviour `p` limited to `𝒱` ([D4]), `E_p[R] = 0` and `E_p[F] = E_p[m]`.
(ii) For every full-support `p`, with `w = p/q`,
`E_p[F] − E_q[F] = Cov_q(w, m) + Cov_q(w, R)`, and `Cov_q(w, R) = E_p[R]`: the target's gain is the regression's gain
plus the residual's.
(iii) For every injective `h : ℝ → ℝ`, the evaluator `h(F̂)` has the same regression and residual as `F̂`; and if `h` is
increasing, `m` rises with `h(F̂)` exactly when it rises with `F̂`.

**In plain terms.** An actor that sees outcomes only through the evaluator changes the principal's objective only
through what the evaluator tells about it: the residual, the part the evaluator does not see, averages to zero for any
such actor. For any actor at all, the objective's gain splits into the gain along the regression and the gain in the
residual. And none of this depends on the evaluator's scale, or on any relabelling of its values that keeps them
distinct.

**Proof.** (i) On each cell `C` of `𝒱`, `m` equals `E_{q(·|C)}[F]`, so `E_{q(·|C)}[R] = 0`, and averaging over the cells
gives `E_q[R] = 0`. A behaviour `p` limited to `𝒱` splits each cell as `q` does, so `E_p[R] = Σ_C p(C)·E_{q(·|C)}[R] =
0`, and `E_p[F] = E_p[m] + E_p[R] = E_p[m]`; this is [P8](i) with `𝒜 = 𝒱`. (ii) Since `E_q[w] = 1`, `Cov_q(w, G) =
E_p[G] − E_q[G]` for every `G`; apply it to `F = m + R`, and use `E_q[R] = 0`. (iii) An injective `h` maps distinct
values to distinct values, so `h(F̂)` has the same level sets as `F̂`, hence the same `𝒱`, `m` and `R`; an increasing
`h` also keeps their order.

**Checks.** checks/test_evaluator.py::test_through_the_evaluator_only_the_regression_counts

**Notes.** (ii) is main's Prop 20 (Goodhart as a covariance, for any actor) with the regression and the residual in
place of a scaled error. The second term is where an actor that sees more than the evaluator can gain or lose: through
distinctions that the evaluator does not make. By [P12](ii), such distinctions show in the revealed objectives of its
changes.

**Lineage.** main: Prop 20 and Def 13. New: the split into regression and residual, and its invariance.

### P19 — A monotone regression rules out overoptimization
**Statement.** Let `F̂` be an evaluator whose regression `m` is non-decreasing in it: `m(x) ≤ m(y)` whenever `F̂(x) ≤
F̂(y)`. Let `s ↦ p_s`, for `s ≥ 0`, be a continuously differentiable path in `Δ°` with `p_0 = q`, whose revealed
objectives `F_s` ([P2]) are, at every `s`, non-decreasing in `F̂` in the same sense. Then `s ↦ E_{p_s}[F]` is
non-decreasing.

**In plain terms.** If, under the default, outcomes the evaluator scores higher are never worse on average for the
principal, then an actor that follows the evaluator, or anything that rises with it, harder and harder, never makes the
principal worse off on average. Pursuing the evaluator itself, or any increasing transformation of it, and picking
the best of more and more samples are all covered.

**Proof.** Each `F_s` is constant on the level sets of `F̂`, so `log(p_s/q) = ∫_0^s F_u du` is too, and every `p_s` is
limited to `𝒱`. By [P18](i), `E_{p_s}[F] = E_{p_s}[m]`, and by [P13](i), applied to `m`, its derivative is
`Cov_{p_s}(F_s, m)`. For any behaviour `p` and two functions `f`, `g` that are both non-decreasing in `F̂`,
`Cov_p(f, g) = ½·Σ_{x,y} p(x)·p(y)·(f(x) − f(y))·(g(x) − g(y)) ≥ 0`, since the two differences never have opposite signs
(Chebyshev's association inequality). So the derivative is never negative.

**Checks.** checks/test_evaluator.py::test_a_monotone_regression_rules_out_overoptimization

**Notes.** It generalizes main's Prop 21, where the regression is affine, and main's B §4, where target and evaluator
are jointly Gaussian. Monotonicity is a property of the default's joint law of target and evaluator, so it can be
checked before any optimization. The check shows that, without it, overoptimization is common. For an evaluator with
distinct values on distinct outcomes, `m = F` ([D10], Notes), and the hypothesis asks that `F̂` never score an outcome
above another that the target strictly prefers.
Best-of-`n`, the best of `n` draws from `q` by `F̂` as a path in a real `n ≥ 1`, stays in `Δ°`, and its revealed
objective is non-decreasing in `F̂`. On the level set of `v`, with `A` and `B` the default's mass of `F̂ ≤ v` and of
`F̂ < v`, it is `(A^n·log A − B^n·log B)/(A^n − B^n)`, with `0·log 0 = 0`: the average of `log u` over `[B, A]` with
weight `u^{n−1}`, plus `1/n`. Keeping only the outcomes above a threshold leaves `Δ°`, so it is not such a path, but the
conclusion holds for it directly: raising the threshold drops the level sets with the lowest regression.

**Lineage.** main: Prop 21 and B §4. New: the monotone case, and the proof by association.

### P20 — Where overoptimization starts, and how it ends
**Statement.** Let `F̂` be a non-constant evaluator, with regression `m`, and let `p_t = tilt(q, t·F̂)` be its pursuit.
Write `v_1 > v_2` for the two largest values of `F̂`, and `m(v_1)`, `m(v_2)` for the regression on their level sets.
(i) `d/dt E_{p_t}[F] = Cov_{p_t}(F̂, m) = Cov_{p_t}(F̂, F)`: the target's average is stationary exactly where, under the
current behaviour, the evaluator stops correlating with the target.
(ii) As `t → ∞`, `E_{p_t}[F] → m(v_1)`. If `m(v_2) > m(v_1)`, then `E_{p_t}[F]` is decreasing for all large enough `t`;
if `m(v_2) < m(v_1)`, it is increasing for all large enough `t`.

**In plain terms.** Following the evaluator, the principal's objective stops improving exactly where, among the
outcomes the actor now favours, the evaluator no longer says anything about it. At very high effort, the objective
settles at its average over the outcomes the evaluator scores highest. If the outcomes it scores just below those are
better for the principal, pushing harder eventually does harm.

**Proof.** (i) The pursuit is limited to `𝒱`, so `E_{p_t}[F] = E_{p_t}[m]` ([P18](i)); its revealed objective is `F̂ −
E_{p_t}[F̂]`, so [P13](i) gives `Cov_{p_t}(F̂, m)`. And `Cov_{p_t}(F̂, R) = E_{p_t}[F̂·R] = 0`, since `F̂` is constant
on each cell, where `p_t` splits mass as `q` does and `R` averages to zero. (ii) Let `a_j` be the default's mass on the
level set of the `j`-th largest value `v_j`, and `π_j(t) = a_j·e^{t·v_j} / Σ_k a_k·e^{t·v_k}`. Then `E_{p_t}[F] = Σ_j
π_j(t)·m(v_j)`, and `π_1(t) → 1`, which gives the limit. By the pairwise form of the covariance in the proof of [P19],
`Cov_{p_t}(F̂, m) = Σ_{j<k} π_j·π_k·(v_j − v_k)·(m(v_j) − m(v_k))`. As `t` grows, `π_1 → 1`, and `π_j/π_2 → 0` for `j ≥
3`, so every term other than `j = 1, k = 2` becomes negligible next to `π_1·π_2·(v_1 − v_2)·(m(v_1) − m(v_2))`, whose
sign is that of `m(v_1) − m(v_2)`.

**Checks.** checks/test_evaluator.py::test_overoptimization_starts_where_correlation_ends_and_ends_at_the_top

**Notes.** (i) gives a stopping rule: stop where target and evaluator become uncorrelated under the current behaviour.
Karwowski et al. derive an early-stopping rule for proxy optimization in the geometry of occupancy measures
[@karwowski2024]; whether the two rules coincide is not yet checked (`TERMS.md`, section 2). (ii) says that what decides
the end is the regression at the top of the evaluator's range, which the default may sample rarely. Before the limit, a
third value close to the second can still dominate the sign, as the check shows in log space.

**Lineage.** main: Prop 14 (the initial and terminal effects of optimization). New: the stationarity condition in the
regression, and the terminal rule.

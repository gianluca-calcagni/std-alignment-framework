# Derived — the evaluator

What an evaluator ([D10]) does to the principal's objective when the actor pursues it. Through the evaluator, only the
regression of the target on it counts ([P18]). A regression that rises with the evaluator rules out overoptimization
([P19]). Otherwise, overoptimization starts where the evaluator stops telling anything about the target under the
current behaviour, and at high intensity it is decided by the evaluator's two highest values ([P20]). The target's curve
turns no more often than the regression does, so a single-peaked regression gives at most one fall ([P25]). For an
evaluator that scores every outcome differently, the regression on bins of its values governs the pursuit while the
intensity is small against the bins ([P26]). For an evaluator known in the target's units, pursued within a departure
budget, the target lost is at most the width of the budget along the evaluator's error, and that bound is the exact
worst case ([P29]); which of two errors is worse depends on the budget, so no bound that separates the error from the
budget can be accurate at every budget ([L1], [P30]). Computable bounds on misalignment and on the width follow from the
error's range and tails ([P33]); and when the evaluator and the target choose from the same candidates, the loss is at
most the error's spread over them, draw by draw, which is again the exact worst case ([P34]).

### P18 — Through the evaluator, only the regression counts
**Statement.** Let `F̂` be an evaluator for the objective `F`, with regression `m`, residual `R` and resolution `𝒱` of
its level sets ([D10]).
(i) `E_q[R] = 0`, and for every behaviour `p` limited to `𝒱` ([D4]), `E_p[R] = 0` and `E_p[F] = E_p[m]`.
(ii) For every full-support `p`, with `w = p/q`, `E_p[F] − E_q[F] = Cov_q(w, m) + Cov_q(w, R)`, and
`Cov_q(w, R) = E_p[R]`: the target's gain is the regression's gain plus the residual's.
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

**Notes.** (ii) is v7.10's Prop 20 (Goodhart as a covariance, for any actor) with the regression and the residual in
place of a scaled error. The second term is where an actor that sees more than the evaluator can gain or lose: through
distinctions that the evaluator does not make. By [P12](ii), such distinctions show in the revealed objectives of its
changes.

**Lineage.** v7.10: Prop 20 and Def 13. New: the split into regression and residual, and its invariance.

### P19 — A monotone regression rules out overoptimization
**Statement.** Let `F̂` be an evaluator whose regression `m` is non-decreasing in it: `m(x) ≤ m(y)` whenever `F̂(x) ≤
F̂(y)`. Let `s ↦ p_s`, for `s ≥ 0`, be a continuously differentiable path in `Δ°` with `p_0 = q`, whose revealed
objectives `F_s` ([P2]) are, at every `s`, non-decreasing in `F̂` in the same sense. Then `s ↦ E_{p_s}[F]` is
non-decreasing.

**In plain terms.** If, under the default, outcomes the evaluator scores higher are never worse on average for the
principal, then an actor that follows the evaluator, or anything that rises with it, harder and harder, never makes the
principal worse off on average. Pursuing the evaluator itself, or any increasing transformation of it, and picking the
best of more and more samples are all covered.

**Proof.** Each `F_s` is constant on the level sets of `F̂`, so `log(p_s/q) = ∫_0^s F_u du` is too, and every `p_s` is
limited to `𝒱`. By [P18](i), `E_{p_s}[F] = E_{p_s}[m]`, and by [P13](i), applied to `m`, its derivative is
`Cov_{p_s}(F_s, m)`. For any behaviour `p` and two functions `f`, `g` that are both non-decreasing in `F̂`,
`Cov_p(f, g) = ½·Σ_{x,y} p(x)·p(y)·(f(x) − f(y))·(g(x) − g(y)) ≥ 0`, since the two differences never have opposite signs
(Chebyshev's association inequality). So the derivative is never negative.

**Checks.** checks/test_evaluator.py::test_a_monotone_regression_rules_out_overoptimization

**Notes.** It generalizes v7.10's Prop 21, where the regression is affine, and v7.10's B §4, where target and evaluator
are jointly Gaussian. Monotonicity is a property of the default's joint law of target and evaluator, so it can be
checked before any optimization. The check shows that, without it, overoptimization is common. For an evaluator with
distinct values on distinct outcomes, `m = F` ([D10], Notes), and the hypothesis asks that `F̂` never score an outcome
above another that the target strictly prefers. Best-of-`n`, the best of `n` draws from `q` by `F̂` as a path in a real
`n ≥ 1`, stays in `Δ°`, and its revealed objective is non-decreasing in `F̂`. On the level set of `v`, with `A` and `B`
the default's mass of `F̂ ≤ v` and of `F̂ < v`, it is `(A^n·log A − B^n·log B)/(A^n − B^n)`, with `0·log 0 = 0`: the
average of `log u` over `[B, A]` with weight `u^{n−1}`, plus `1/n`. Keeping only the outcomes above a threshold leaves
`Δ°`, so it is not such a path, but the conclusion holds for it directly: raising the threshold drops the level sets
with the lowest regression.

**Lineage.** v7.10: Prop 21 and B §4. New: the monotone case, and the proof by association.

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

**Lineage.** v7.10: Prop 14 (the initial and terminal effects of optimization). New: the stationarity condition in the
regression, and the terminal rule.

### P25 — The target's curve turns no more often than the regression
**Statement.** Let `F̂` be an evaluator with values `v_1 < … < v_k`, let `a_j` be the default's mass on the level set of
`v_j` and `m_j` the regression there ([D10]), and for every real `t` let `p_t = tilt(q, t·F̂)`: the pursuit of `F̂` at
intensity `t` when `t ≥ 0`, and of `−F̂` at intensity `−t` when `t < 0`.
(i) For every number `c`, the function `t ↦ E_{p_t}[F] − c` changes sign on `ℝ` at most as many times as the sequence
`m_1 − c, …, m_k − c` does, its zero terms left out. As `t → −∞` it has the sign of the first non-zero term of that
sequence, and as `t → +∞` the sign of the last.
(ii) If the regression is non-decreasing in `F̂`, then `t ↦ E_{p_t}[F]` is non-decreasing on `ℝ`.
(iii) If the regression is single-peaked, `m_1 ≤ … ≤ m_i ≥ … ≥ m_k` for some `i`, then for all `s < t < u`,
`E_{p_t}[F] ≥ min(E_{p_s}[F], E_{p_u}[F])`: once the target's average has fallen, it never rises again.

**In plain terms.** Line up the evaluator's scores from lowest to highest, and write next to each the principal's
average objective over the outcomes with that score. Pursuing the evaluator harder smooths that list: the principal's
average can cross any level no more often than the list does. If the list only rises, pursuit never hurts. If it rises
and then falls, pursuit can help and then hurt, but only once: there is no recovery after the fall.

**Proof.** By [P18](i), `E_{p_t}[F] = Σ_j a_j·m_j·e^{t·v_j} / Σ_j a_j·e^{t·v_j}`, so `E_{p_t}[F] − c` has the sign of
`f(t) = Σ_j c_j·e^{t·v_j}`, with `c_j = a_j·(m_j − c)` of the sign of `m_j − c`. (i) Laguerre's rule of signs
[@polya1976]: an exponential sum `Σ_j c_j·e^{t·v_j}`, with `v_1 < … < v_k` and real coefficients not all zero, has at
most as many real zeros, counted with multiplicity, as its coefficients have sign changes. By induction on the number
`s` of sign changes: if `s = 0`, all non-zero terms have one sign and there is no zero. Otherwise take `μ` strictly
between the exponents of two consecutive non-zero coefficients of opposite signs. Then `g = e^{−μt}·f` has the zeros of
`f`, and `g' = Σ_j (v_j − μ)·c_j·e^{(v_j − μ)·t}` has coefficients with `s − 1` sign changes, since the factor `v_j − μ`
flips the signs of exactly the terms before `μ`. By Rolle's theorem `g'` has at least one zero fewer than `g`, so `g`
has at most `s`. A function with at most `s` zeros changes sign at most `s` times. As `t → +∞` the non-zero term with
the largest exponent dominates, and as `t → −∞` the one with the smallest. (ii) For every `c`, the non-zero terms of
`m_j − c` are negative and then positive. By (i), `f` is either of one sign, or negative and then positive with one
simple zero; so `{t : E_{p_t}[F] > c}` is empty, `ℝ`, or a half-line `(t_0, ∞)`. If `E_{p_s}[F] > E_{p_u}[F]` for some
`s < u`, a `c` strictly between them would put `s` in that set and not `u`. (iii) Suppose `s < t < u` with
`E_{p_t}[F] < c < min(E_{p_s}[F], E_{p_u}[F])`, so that `f` takes the signs `+`, `−`, `+` at `s`, `t`, `u`. For a
single-peaked regression, the indices with `m_j > c` are consecutive, so the non-zero terms of `m_j − c` are negative,
then positive, then negative, some groups possibly empty. With two sign changes, the sequence starts and ends negative,
so by (i) `f` has at most two zeros and is negative at both ends: it is negative throughout, or negative, positive on
one interval, and negative again, and `+`, `−`, `+` is impossible. With at most one sign change, `f` changes sign at
most once, which `+`, `−`, `+` needs twice.

**Checks.** checks/test_evaluator.py::test_the_target_curve_turns_no_more_often_than_the_regression

**Notes.** (i) is the variation-diminishing property of the exponential kernel, a case of total positivity. It holds for
the pursuit of any increasing transformation of `F̂`, which has the same level sets in the same order, and so for the
pursuit of ranks. Best-of-`n`, as a path in a real `n ≥ 1`, obeys (ii) and (iii) too: with `A_j` the default's mass of
`F̂ ≤ v_j`, its average is `E_n[F] − c = (m_k − c) + Σ_{j<k} (m_j − m_{j+1})·A_j^n`, an exponential sum in `n` with
exponents `log A_1 < … < log A_k = 0`. For a single-peaked regression its coefficients are negative, then positive, then
of the sign of `m_k − c`, and the argument of (iii) applies. [P20](ii) gives where a single-peaked curve ends; (iii)
adds that it gets there with one turn at most. For an evaluator that scores every outcome differently, the sequence
`m_j` is the target itself in the evaluator's order, and (i) is a bound on noisy data; [P26] gives its bin-wise form.

**Lineage.** New (`NOTES.md` E8). v7.10: Prop 14 (initial and terminal effects) said where the curve starts and ends;
nothing on its shape in between.

### P26 — The regression on bins governs at small intensity
**Statement.** Let `F̂` be an evaluator, and `G = h(F̂)` with `h` constant on each of finitely many disjoint intervals
that cover the values of `F̂`, and increasing from one interval to the next: `G` groups the values of `F̂` into bins.
Let `m_G` be the regression of `F` on `G` ([D10]), `w` the largest spread of `F̂` within a bin (its largest value there
minus its smallest), and `D` the largest spread of `F` within a bin. Along the pursuit `p_t = tilt(q, t·F̂)` of `F̂`
itself, for every `t ≥ 0`:
(i) `|E_{p_t}[F] − E_{p_t}[m_G]| ≤ t·w·D/4`.
(ii) If `m_G` is non-decreasing in `G`, then `E_{p_u}[F] ≥ E_{p_s}[F] − (s + u)·w·D/4` for all `0 ≤ s ≤ u`.
(iii) If `m_G` is single-peaked in `G`, then `t ↦ E_{p_t}[m_G]` never falls and then rises again ([P25](iii)), and
`E_{p_t}[F]` stays within `t·w·D/4` of it.

**In plain terms.** An evaluator that scores every outcome differently has a regression equal to the objective itself,
so the regression is read, in practice, from bins of scores. Pursuing the evaluator keeps the principal's average within
`t·w·D/4` of its average under that bin-wise regression, where `w` is the width of the bins in the evaluator's units
and `D` the spread of the objective inside a bin. So, while that margin is small next to the changes of the average
that matter, the bin-wise regression decides: if it rises, pursuit does not hurt beyond the margin, and if it rises and
then falls, so does the principal's average, up to the margin.

**Proof.** Each bin `b` is a union of level sets of `F̂`, and `m_G = E_q[F|b]` on it, so
`E_{p_t}[F] − E_{p_t}[m_G] = Σ_b p_t(b)·(E_{p_t}[F|b] − E_q[F|b])`. Within `b`, `p_t(·|b) = tilt(q(·|b), t·F̂)`, a path
from `q(·|b)` whose revealed objective is `F̂` centred, so by [P13](i)
`E_{p_t}[F|b] − E_q[F|b] = ∫_0^t Cov_{r_s}(F̂, F) ds`, with `r_s = tilt(q(·|b), s·F̂)`. By Cauchy–Schwarz,
`|Cov_r(F̂, F)| ≤ Var_r(F̂)^{1/2}·Var_r(F)^{1/2}`, and a function whose values on `b` lie in an interval of length `d`
has variance at most `d²/4` under any behaviour on `b`, the mean square distance to the interval's midpoint
(Popoviciu's inequality). So each term is at most `t·(w/2)·(D/2)`, and so is their average, which proves (i).
(ii) As a function on outcomes, `m_G` is constant on the level sets of `F̂` and non-decreasing in `F̂`, so its
regression on `F̂` is itself, and [P19] gives `E_{p_u}[m_G] ≥ E_{p_s}[m_G]`; (i) at `s` and at `u` gives the rest.
(iii) In the same way, the regression of `m_G` on `F̂` is `m_G`, single-peaked in `F̂`, and [P25](iii) applies; (i)
gives the margin.

**Checks.** checks/test_evaluator.py::test_binned_evaluators

**Notes.** The bound is attained to first order in `t` by a bin with two equally likely outcomes at the ends of both
spreads; random instances stay well inside it. It trades resolution against reach: narrower bins make `w` smaller but
leave fewer outcomes, and fewer sampled ones ([D11]), in each bin, so the bin-wise regression is estimated with more
error. With one outcome per bin, `w = 0` and (i) is exact, as [D10]'s Notes say: the regression is then the target. The
bound covers the pursuit of `F̂`, not best-of-`n`; for best-of-`n` the natural width of a bin is in units of
`log Q(F̂)`, the log of the default's mass below a value, which is open (`NOTES.md` E8).

**Lineage.** v7.10: Prop 2 (Popoviciu's bound on the variance). New (`NOTES.md` E8).

### P29 — The width is the exact worst case
**Statement.** Let `F` be the target, `F̂` an evaluator known in the units of `F` ([D10]), and `E = F̂ − F` its error,
non-constant. Let `δ > 0`, and for `G = F` and `G = F̂` let `p*_G` be a behaviour with the largest average of `G` over
the departure budget `𝓑_δ` ([P27](ii)). Let `L = E_{p*_F}[F] − E_{p*_F̂}[F]`: the target lost by pursuing the evaluator
instead of the target within the budget.
(i) `0 ≤ L ≤ E_{p*_F̂}[E] − E_{p*_F}[E] ≤ w_δ(E)`, the width of the budget along the error ([P28]).
(ii) Over all targets `F` with the same error, the supremum of `L` is `w_δ(E)`: `F = −c·E` gives `L = c·w_δ(E)`, for
every `0 < c < 1`. So no bound on `L` that depends only on the error and the budget is smaller than `w_δ(E)`.
(iii) If the budget binds for both, `δ < −log q(argmax F)` and `δ < −log q(argmax F̂)`, then `L` is the shortfall of
`p*_F̂` ([D5]).

**In plain terms.** An actor that has a fixed budget of departure and spends it on the evaluator instead of the
principal's objective loses some of it. The loss is never more than how far the budget lets the average of the error
move, up and down together; and for some objective it is that much. So the width is not a loose bound: it is the worst
case. When both pursuits use up the budget, the loss is the actor's stakes.

**Proof.** (i) `p*_F` has the largest average of `F` over the budget and `p*_F̂` is in it, so `L ≥ 0`. `p*_F̂` has the
largest average of `F̂ = F + E` and `p*_F` is in the budget, so
`E_{p*_F̂}[F] + E_{p*_F̂}[E] ≥ E_{p*_F}[F] + E_{p*_F}[E]`, which rearranges to the middle inequality. Both behaviours
are in the budget, so `E_{p*_F̂}[E] − E_q[E] ≤ σ_δ(E)` and `E_q[E] − E_{p*_F}[E] ≤ σ_δ(−E)`, whose sum is `w_δ(E)`. (ii)
With `F = −c·E`, `F̂ = (1 − c)·E`. A positive multiple of an objective has the same best behaviours in the budget, since
`λ_δ(a·G) = λ_δ(G)/a` and `p_{aG, λ/a} = p_{G,λ}` ([P27](ii)). So `p*_F̂` raises the average of `E` by `σ_δ(E)` and
`p*_F` lowers it by `σ_δ(−E)`, and `L = c·(σ_δ(E) + σ_δ(−E)) = c·w_δ(E)`. With (i), the supremum over `c < 1` is
`w_δ(E)`. (iii) When the budget binds for `F̂`, `KL(p*_F̂‖q) = δ` ([P27](ii)), so the matched intensity of `p*_F̂` is
`λ_δ(F)` and its matched pursuit is `p_{F,λ_δ(F)} = p*_F` ([D5], [P27](ii)); the shortfall is then `L`.

**Checks.** checks/test_evaluator.py::test_the_width_is_the_exact_worst_case

**Notes.** The error `E = F̂ − F` needs the evaluator's scale, which behaviour never identifies ([D10]); this result is
about evaluators known in the target's units, such as a reward model trained to predict the target. The comparison is at
an equal budget, as stakes are ([D5]); v7.10 also compared net values at a declared price, which the core does not use.
Typical losses sit well inside the width: in the check, the median of `L/w_δ(E)` is below one half.

**Lineage.** v7.10: Thm 5 (the width is the exact worst case), parts (i) and (ii) at `β = ∞`; part (iii), at a declared
price, is not imported. New: (iii) here, the loss as the shortfall of [D5].

### L1 — Separable bounds are loose when two quantities change rank
**Statement.** Let `Q(E, δ) > 0` for `E` in a pair `{E₁, E₂}` and `δ` in a set `D`, let `ρ(δ) = Q(E₁, δ)/Q(E₂, δ)`, and
`K = sup_D ρ / inf_D ρ`. If `B(E, δ) = a(E)·b(δ)` satisfies `Q ≤ B ≤ L·Q` on `{E₁, E₂} × D`, then `L ≥ √K`; and some
separable `B` attains `L = √K`.

**In plain terms.** A bound that multiplies a property of the error by a function of the budget cannot follow two errors
whose ratio changes with the budget: if the ratio moves by a factor `K`, the bound is off by at least `√K` somewhere.

**Proof.** For every `δ`, `κ = a(E₁)/a(E₂) = B(E₁, δ)/B(E₂, δ)` lies in `[ρ(δ)/L, L·ρ(δ)]`, so
`sup_D ρ/L ≤ κ ≤ L·inf_D ρ`, which gives `L² ≥ K`. For the second part, take `a(E₂) = 1`,
`a(E₁) = κ = (sup_D ρ · inf_D ρ)^{1/2}` and `b(δ) = Q(E₂, δ)·(ρ(δ)/κ)^{1/2}`: then `B/Q` is `(ρ/κ)^{1/2}` on `E₂` and
`(κ/ρ)^{1/2}` on `E₁`, both between `K^{−1/4}` and `K^{1/4}`; rescaling `b` by `K^{1/4}` gives `Q ≤ B ≤ √K·Q`.

**Checks.** checks/test_evaluator.py::test_no_separable_bound_on_the_worst_case

**Lineage.** v7.10: Lemma 8. New: that `√K` is attained.

### P30 — No separable bound on the worst case
**Statement.** Let `E₁` be non-constant and `A` a set of outcomes with `q(A) = r ∈ (0, 1)`.
(i) As `δ → 0`, `w_δ(E₁)/w_δ(1_A) → (Var_q(E₁)/(r·(1 − r)))^{1/2}`; and `w_δ(E₁)/w_δ(1_A) = max E₁ − min E₁` for every
`δ ≥ δ̄ = max{−log q(argmax E₁), −log q(argmin E₁), −log r, −log(1 − r)}`.
(ii) Hence any bound `a(E)·b(δ)` on the worst case `w_δ(E)` of [P29] that holds within a factor `L` for the pair
`{E₁, M·1_A}`, for some `M > 0`, over budgets that include arbitrarily small ones and one at least `δ̄`, has
`L ≥ (K)^{1/2}` with `K ≥ Var_q(E₁)^{1/2} / ((max E₁ − min E₁)·(r·(1 − r))^{1/2})`; and this grows without bound as
`q(A) → 0` with `Var_q(E₁)/(max E₁ − min E₁)²` bounded away from `0`.

**In plain terms.** At a small budget, the error that does more damage is the one with more spread under the default;
at a large budget, it is the one with the wider range. An error confined to a rare region has little spread but a full
range, so it is harmless at small budgets and as bad as any at large ones. No ranking of errors holds at every budget,
and no bound that scores the error once and the budget once can be accurate at every budget.

**Proof.** (i) By [P28](ii), `w_δ(E) = 2·(2δ·Var_q(E))^{1/2} + O(δ^{3/2})` for both, and `Var_q(1_A) = r·(1 − r)`. By
[P28](iii), once `δ ≥ δ̄` each width is its range: `max E₁ − min E₁`, and `1` for `1_A`, whose largest value is taken on
`A` and smallest on its complement. (ii) The width is multiplied by `M` when the function is ([P28], Notes), so the
ratio for `{E₁, M·1_A}` is that of (i) divided by `M`, and `K` does not depend on `M`. The supremum of the ratio over
the budgets is at least its limit at `0` and its value at `δ̄`, and the infimum at most either, so `K` is at least their
quotient. [L1] with `Q(E, δ) = w_δ(E)`, the worst case by [P29](ii), gives the bound on `L`.

**Checks.** checks/test_evaluator.py::test_no_separable_bound_on_the_worst_case

**Notes.** Main measured the same effect for one fixed target, not only for the worst case: a dense error and a
one-outcome spike swap ranks between small and large budgets, by a factor of about a hundred. The statement in the core
is about the worst case only.

**Lineage.** v7.10: Thm 9 (the worst-case regret is not separable), with its check V5, and §11.1 (no capacity-free
ranking of errors).

### P33 — Error bounds for a known evaluator
**Statement.** Let `F̂ = F + E` be an evaluator known in the units of `F` ([D10]), with `E` non-constant, and let
`t > 0`, `p̂ = p_{F̂,t}` and `r = p_{F,t}`. Write `Λ_r(u) = log E_r[e^{u·(E − E_r[E])}]`, and `Λ_q` the same under `q`.
(i) `M(p̂) ≤ KL(p̂‖r) = ∫_0^t s·Var_{tilt(r, s·E)}(E) ds`.
(ii) `KL(p̂‖r) ≤ t²·(max E − min E)²/8`, and the constant `1/8` cannot be lowered.
(iii) `KL(p̂‖r) ≤ Λ_r(2t) − 2Λ_r(t)`, which needs no bound on the error's range.
(iv) Within a departure budget `δ`, the target lost by pursuing `F̂` instead of `F` ([P29]) is at most
`w_δ(E) ≤ (2δ)^{1/2}·(σ₊ + σ₋) ≤ (2δ)^{1/2}·(max E − min E)`, where `σ₊² = sup_{u>0} 2Λ_q(u)/u²` and `σ₋²` is the same
for `−E`.

**In plain terms.** An actor that pursues an evaluator with an error is misaligned by at most an eighth of the square of
the error's range, measured in nats at the actor's intensity: small errors cost very little. A second bound needs no
range at all, only how the error spreads under the pursuit of the target. Within a budget of departure, the principal's
loss is at most the square root of twice the budget times the error's sub-Gaussian scales up and down.

**Proof.** (i) `r` is on the pursuit ray of `F`, so `M(p̂) ≤ KL(p̂‖r)` ([D3]). By [P1](iii), `p̂ = tilt(r, t·E)`. With
`g(s) = KL(tilt(r, s·E)‖r) = s·Λ_r'(s) − Λ_r(s)`, `g(0) = 0` and `g'(s) = s·Λ_r''(s) = s·Var_{tilt(r, s·E)}(E)`.
(ii) A function whose values lie in an interval of length `d` has variance at most `d²/4` under any behaviour (the mean
square distance to the interval's midpoint; Popoviciu's inequality, as in [P26]), so (i) gives at most `(d²/4)·t²/2`. If
`E` takes two values on sets of `r`-mass one half each, `Var_r(E) = d²/4`, so `g(t) = d²·t²/8 + O(t³)` and the ratio of
the two sides tends to `1` as `t → 0`. (iii) `Λ_r` is convex, so `Λ_r(2t) ≥ Λ_r(t) + t·Λ_r'(t)`, that is,
`g(t) = t·Λ_r'(t) − Λ_r(t) ≤ Λ_r(2t) − 2Λ_r(t)`. (iv) For `u > 0` and `p` in the budget,
`E_p[E] − E_q[E] ≤ (δ + Λ_q(u))/u ≤ δ/u + σ₊²·u/2` (the proof of [P28](i)), which is smallest at `u = (2δ/σ₊²)^{1/2}`;
so `σ_δ(E) ≤ (2δ·σ₊²)^{1/2}`, and likewise `σ_δ(−E) ≤ (2δ·σ₋²)^{1/2}`. [P29](i) bounds the loss by their sum. Finally,
`Λ_q(u) = ∫_0^u (u − s)·Var_{tilt(q, s·E)}(E) ds ≤ (max E − min E)²·u²/8` by the same variance bound, so
`σ± ≤ (max E − min E)/2`.

**Checks.** checks/test_evaluator.py::test_error_bounds_for_a_known_evaluator

**Notes.** [P10](ii) gives the linear bound `M(p̂) ≤ t·(max E − min E)`; (ii) is the smaller of the two when the error's
range in nats, `t·(max E − min E)`, is below `8`. The bound of (iv) is never looser than the range form, by the last
step of the proof. It has the separable form `a(E)·b(δ)`, which [P30] shows cannot be accurate within a fixed factor for
every error and budget; this one grows with `δ` without bound, while the width stops at the range ([P28](iii)). Main's
Prop 3 said that only the error's upper tail matters. For misalignment that holds only in a weaker form: an underrating
also costs nats, but a bounded number of them; an error confined to a set of outcomes costs at most
`max(log(1/a), log(1/(1 − a)))` nats, whatever its sign and size, with `a` the set's mass under `r` ([C3]).

**Lineage.** v7.10: Prop 2 (the sharp bound by the range), Prop 3 (only the upper tail matters, weakened: see Notes),
Prop 7 (a bound with realized travel) and Cor 1.3 (the integral form). New: the bounds as bounds on misalignment, not on
regret at a declared price.

### P34 — Choosing by the evaluator from a common candidate set
**Statement.** Let a random set `S` of candidate outcomes be drawn by any mechanism, for instance `n` independent draws
from `q`. From the same `S`, let `x*` be a candidate with the largest target `F` and `x̂` one with the largest evaluator
`F̂ = F + E`, known in the units of `F`, both breaking ties by one fixed order, and let `p*` and `p̂` be their
distributions.
(i) `0 ≤ F(x*) − F(x̂) ≤ E(x̂) − E(x*) ≤ max_S E − min_S E` for every `S`, and so
`0 ≤ E_{p*}[F] − E_{p̂}[F] ≤ E_{p̂}[E] − E_{p*}[E] ≤ E[max_S E − min_S E]`.
(ii) Over all targets `F` with the same error, the supremum of the loss is the range of the error over the candidates:
`F = −c·E` gives `F(x*) − F(x̂) = c·(max_S E − min_S E)` for every `S`, for every `0 < c < 1`. So no bound on the
average loss that depends only on the error and the way `S` is drawn is smaller than `E[max_S E − min_S E]`.

**In plain terms.** When the evaluator and the target choose among the same candidates, the target lost is at most how
much more the evaluator overrates its own pick than the target's pick, and so at most the spread of the error over the
candidates. That spread is the exact worst case: for some target it is lost. Best-of-`n` by the evaluator, compared with
best-of-`n` by the target at the same `n`, is the case in point: the worst average loss is the average spread of the
error over `n` draws.

**Proof.** `x̂ ∈ S`, so `F(x*) ≥ F(x̂)`; and `x* ∈ S`, so `F̂(x̂) ≥ F̂(x*)`, that is, `F(x̂) + E(x̂) ≥ F(x*) + E(x*)`.
Together, `0 ≤ F(x*) − F(x̂) ≤ E(x̂) − E(x*)`, and both candidates are in `S`. Taking averages over `S` gives the rest
of (i). (ii) With `F = −c·E`, `F̂ = (1 − c)·E`, so `x̂` has the largest `E` in `S` and `x*` the smallest; ties do not
matter, since tied candidates have the same `E` and `F`. Then `F(x*) − F(x̂) = c·(max_S E − min_S E)`, and with (i), the
supremum of the average loss over `0 < c < 1` is `E[max_S E − min_S E]`.

**Checks.** checks/test_evaluator.py::test_choosing_from_a_common_candidate_set

**Notes.** The middle bound of (i) is one line: the loss is `E(x̂) − E(x*)` minus the evaluator's margin
`F̂(x̂) − F̂(x*) ≥ 0`, so it is computable only when the loss is. Its use is the range form, and (ii) shows that form
cannot be improved; it is the counterpart, for selection, of [P29](ii). No width enters: the bound depends on the
candidates. It needs them to be shared. The archive found that comparing best-of-`n` by the evaluator with the pursuit
of the target at the same departure, instead of at the same `n`, breaks the inequality in some instances (v7.10: R6);
that is its measurement.

**Lineage.** v7.10: Prop 23 (argmax selectors on a common candidate set).

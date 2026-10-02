# Derived — resolution

What declared indifference forgives ([P7]), and what an actor that cannot tell outcomes apart can and cannot achieve
([P8]).

### P7 — Indifference forgives exactly what happens inside cells
**Statement.** Let `ℬ` be a resolution and `q ∈ Δ°`.
(i) If a specification is stated at resolution `ℬ`, then for every `p̂ ∈ Δ`, `M(p̂) = inf_{p ∈ 𝓘_ℬ} KL(p̂_ℬ‖p)`:
misalignment depends only on the cell masses of `p̂`.
(ii) Let `F` be non-constant and constant on the cells of `ℬ`. Let `M` be the misalignment under the standard
specification of `F`, and `M_ℬ` the misalignment under the standard specification at resolution `ℬ`. Then for every
`p̂ ∈ Δ`, `M(p̂) = M_ℬ(p̂) + W(p̂)`, where `W(p̂) = KL(p̂‖q) − KL(p̂_ℬ‖q_ℬ)` is the **within-cell departure**.

**In plain terms.** When the principal declares that it does not care how outcomes inside a cell are split,
misalignment depends only on how often each cell occurs. Compared with caring about every outcome, declaring
indifference removes exactly the part of the departure from the default that happens inside cells, and nothing else. A
maximizer that picks one of several tied best outcomes is charged when the ties are distinguished, and aligned once the
principal declares them equivalent.

**Proof.** (i) By [P4](iii), for every `p ∈ 𝓘`,
`KL(p̂‖p) = KL(p̂_ℬ‖p_ℬ) + Σ_{C : p̂(C) > 0} p̂(C)·KL(p̂(·|C)‖p(·|C))`. Membership in `𝓘` constrains only `p_ℬ`: any
full-support splits inside the cells can be combined with any `p_ℬ ∈ 𝓘_ℬ`. Choosing splits that approach `p̂(·|C)` makes
the second term tend to `0`, so the infimum over `𝓘` is the infimum over `𝓘_ℬ` of the first term.
(ii) Since `F` is constant on each cell, `p_{F,t}(·|C) = q(·|C)` for every `t` and every cell `C`, and `(p_{F,t})_ℬ` is
the
pursuit of `F`, read on the cells, from `q_ℬ`. By [P4](iii), applied with `r = p_{F,t}` and with `r = q`,
`KL(p̂‖p_{F,t}) = KL(p̂_ℬ‖(p_{F,t})_ℬ) + W(p̂)`, where `W(p̂) = Σ_{C : p̂(C) > 0} p̂(C)·KL(p̂(·|C)‖q(·|C))
= KL(p̂‖q) − KL(p̂_ℬ‖q_ℬ)` does not depend on `t`. Taking the infimum over `t ≥ 0`, and using (i) for `M_ℬ`, gives
`M(p̂) = M_ℬ(p̂) + W(p̂)`.

**Checks.** checks/test_resolution.py::test_indifference_depends_only_on_cell_masses,
checks/test_resolution.py::test_indifference_removes_the_within_cell_departure,
checks/test_resolution.py::test_ties_are_forgiven_when_merged

**Notes.** The tie case settles the charge noted in [P5]: the maximizer was charged only for a distinction the principal
had not said it cared about. Indifference is the only way the core forgives what happens inside cells. A coarse
resolution chosen to hide an exploit would be a specification error, which is why the finest resolution holds unless
another is declared.

**Lineage.** v7.10: Def 21 and R7-10 (a declared resolution removes exactly the drift inside cells, under the free
convention), Prop 32(b) and ROADMAP §6 G1 (underdetermination, here declared).

### P8 — An actor that cannot tell outcomes apart
**Statement.** Let `𝒜` be a resolution, `q ∈ Δ°` the default, `F : X → ℝ`, and `F̄ = E_q[F|𝒜]` its cell average.
(i) **Limited behaviours.** The full-support behaviours limited to `𝒜` are exactly the tilts `tilt(q, G)` with `G`
constant on the cells of `𝒜`. For every behaviour `p` limited to `𝒜`, `E_p[F] = E_p[F̄]`.
(ii) **Best effort.** For every `t > 0`, among the behaviours limited to `𝒜`, the net value `J_t` of [P4] is maximized
by
`tilt(q, t·F̄)`: the actor pursues the cell average of the objective.
(iii) **What it cannot remove.** Let `p* ∈ Δ°` and `b = log(p*/q)`. The smallest value of `KL(p‖p*)` over the behaviours
`p` limited to `𝒜` is `−log E_q[exp(E_q[b|𝒜])] ≥ 0`, reached at `tilt(q, E_q[b|𝒜])`. It is `0` if and only if `p*` is
itself limited to `𝒜`.
(iv) **Effort and misalignment.** Let `F` be non-constant, and let `M` be the misalignment under the standard
specification of `F`. If `F` is constant on the cells of `𝒜`, or `F̄` is constant, then `M(tilt(q, t·F̄)) = 0` for every
`t ≥ 0`. Otherwise `M(tilt(q, t·F̄)) > 0` for every `t > 0`, and
`M(tilt(q, t·F̄))/t² → ½·Var_q(F̄)·(1 − Var_q(F̄)/Var_q(F))` as `t → 0`. Beyond small `t` it need not grow: in some
cases it rises and then falls back toward `0`.

**In plain terms.** An actor that cannot tell the outcomes inside its cells apart can only change how often each cell
occurs. Doing its best, it pursues the objective's average over each cell. If the principal intends one behaviour that
needs finer distinctions, some misalignment cannot be removed: a Jensen gap, zero only when the intended behaviour needs
no distinction the actor lacks. Asked to pursue an objective that varies inside its cells, the actor is misaligned at
every effort, unless it can see all of the objective's variation, or none of it. At small effort, misalignment
grows with the square of the effort, at a rate set both by the part of the objective's variation the actor can see and
by the part it cannot. With more effort it need not keep growing.

**Proof.** (i) If `p ∈ Δ°` is limited to `𝒜`, then for `x` in a cell `A`, `p(x) = p(A)·q(x|A) = q(x)·p(A)/q(A)`, so
`p = tilt(q, G)` with `G = log(p(A)/q(A))` on `A`. Conversely, `tilt(q, G)` with `G` constant on cells splits each cell
in proportion to `q`. For `p` limited to `𝒜`, `E_p[F] = Σ_A p(A)·E_{q(·|A)}[F] = Σ_A p(A)·F̄(A) = E_p[F̄]`.
(ii) For `p` limited to `𝒜`, [P4](iii) with `r = q` gives `KL(p‖q) = KL(p_𝒜‖q_𝒜)`, because every within-cell term is
`0`, and (i) gives `E_p[F] = E_{p_𝒜}[F̄]`, reading `F̄` on the cells. So `J_t(p)` is the net value on the cells for the
objective `F̄`, and by [P4](i) its unique maximizer is `tilt(q_𝒜, t·F̄)` on the cells. Splitting each cell as `q` does,
that is `tilt(q, t·F̄)`.
(iii) For `p` limited to `𝒜`, write `b̄ = E_q[b|𝒜]`. As in (i), `E_p[b] = E_p[b̄]`, and `log(p/q)` is `log(p(A)/q(A))`
on
the support of `p`. So `KL(p‖p*) = E_p[log(p/q)] − E_p[b] = Σ_A p(A)·(log(p(A)/q(A)) − b̄(A))
= KL(p_𝒜‖tilt(q_𝒜, b̄)) − log E_q[e^{b̄}]`. The first term is non-negative and is `0` exactly at `p = tilt(q, b̄)`. By
Jensen's inequality for the conditional average, `E_q[e^{b̄}] ≤ E_q[e^b] = Σ_x p*(x) = 1`, so the minimum is
`−log E_q[e^{b̄}] ≥ 0`. Since `exp` is strictly convex and `q` has full support, equality holds exactly when `b` is
constant on every cell, that is, when `p*(·|A) = q(·|A)` for every cell.
(iv) If `F` is constant on cells, `F̄ = F` and `tilt(q, t·F̄) = p_{F,t}`. If `F̄` is constant, `tilt(q, t·F̄) = q`. Both
are on the pursuit ray, so `M = 0`. Otherwise, suppose `tilt(q, t·F̄) = p_{F,t'}` with `t > 0` and `t' ≥ 0`. By
[P1](ii), `t·F̄ − t'·F` is constant: if `t' = 0`, `F̄` is constant; if `t' > 0`, `F` is constant on cells. Both are
excluded, so `tilt(q, t·F̄)` is not on the ray, and since it has full support and the ray is closed in `Δ°`, [P5](ii)
gives `M > 0`.
*Small effort.* Let `φ(s) = E_{p_{F,s}}[F]` and `ψ(t) = E_{tilt(q,t·F̄)}[F]`. Both are smooth, with `φ'(0) = Var_q(F)`
and `ψ'(0) = Cov_q(F̄, F) = Var_q(F̄)`, because `E_q[F̄·F] = E_q[F̄²]`. For small `t > 0`,
`E_q[F] < ψ(t) < max F`, so by [P5](iv) `M = KL(tilt(q, t·F̄)‖p_{F,t*})` with `φ(t*) = ψ(t)`. By the inverse function
theorem, `t*` is a smooth function of `t`, with `t*(0) = 0` and `t*'(0) = ρ = Var_q(F̄)/Var_q(F)`. Expanding the
log-normalizer `Λ(c) = log E_q[e^c]` to second order gives
`KL(tilt(q, a)‖tilt(q, b)) = ½·Var_q(a − b) + O(‖a‖³ + ‖b‖³)` for small `a`, `b`. With `a = t·F̄` and `b = t*·F`,
`M = ½·t²·Var_q(F̄ − ρ·F) + O(t³)`, and `Var_q(F̄ − ρ·F) = Var_q(F̄) − 2ρ·Var_q(F̄) + ρ²·Var_q(F) = Var_q(F̄)·(1 − ρ)`.
*Not monotone.* The check exhibits a case: three outcomes, the actor's cells `{x₁}` and `{x₂, x₃}`, and `F` largest at
`x₁`. Misalignment is `0` at `t = 0`, about `0.24` at `t = 2`, and below `10⁻⁶` at `t = 10`, because the actor's best
cell holds only the best outcome.

**Checks.** checks/test_resolution.py::test_limited_behaviours_are_tilts_by_cell_functions,
checks/test_resolution.py::test_best_effort_pursues_the_cell_average,
checks/test_resolution.py::test_irreducible_misalignment_is_a_jensen_gap,
checks/test_resolution.py::test_coarse_pursuit_is_misaligned_at_every_effort,
checks/test_resolution.py::test_coarse_misalignment_starts_quadratic_and_need_not_keep_growing

**Notes.** Since `Var_q(F) = Var_q(F̄) + Var_q(F − F̄)`, the coefficient in (iv) is
`½·Var_q(F̄)·Var_q(F − F̄)/Var_q(F)`:
the product of what the actor can see and the share it cannot. Writing `θ` for the angle between `F̄` and `F` in the
Fisher metric at `q`, `cos²θ = Var_q(F̄)/Var_q(F)`, and the same expansion gives `KL(tilt(q, t·F̄)‖q) ≈ ½·t²·Var_q(F̄)`.
So at small effort `M ≈ sin²θ` times the departure: here, the misaligned share of the departure is `sin²θ`. (iii) is
the retention gap of v7.10's B1, in closed form.

**Lineage.** v7.10: B1 and NOTES §8 (retention, `G = E_q[F|ℋ]`, under the budget convention, where it rises with the
budget), ROADMAP §6 G2 (transmission and retention), and the I1 notes (the dynamic angle, `D_⊥ ≈ sin²θ·KL`, conjectured
there). New: the Jensen gap in closed form, the small-effort coefficient, and the counterexample to monotone growth:
B1's
"rises with budget" does not carry over as a law.

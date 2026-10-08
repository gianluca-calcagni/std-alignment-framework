# Derived — stakes and sensitivity

What is at stake, in the objective's own units, and its three causes ([P9]); and how much an error in the declared
default or objective can move misalignment ([P10]).

### P9 — What is at stake
**Statement.** Under the standard specification of a non-constant `F`, let `p̂ ∈ Δ`, with matched intensity `λ`, matched
pursuit `p_{F,λ}` and nearest intended behaviour `p°` ([P5](iv)).
(i) **The best use of the departure.** If `λ < ∞`, then `KL(p_{F,λ}‖q) = KL(p̂‖q)`, and `p_{F,λ}` has the largest
average of `F` among all behaviours whose departure is at most `KL(p̂‖q)`. If `λ = ∞`, then `S(p̂) = max F − E_{p̂}[F]`.
In both cases `S(p̂) ≥ 0`.
(ii) **Three causes.** If `0 < λ < ∞`, then `λ·S(p̂) = M(p̂) + KL(p°‖p_{F,λ}) + λ·[E_q[F] − E_{p̂}[F]]⁺`: misalignment,
**under-pursuit** (pursuing at a lower intensity than the departure allows), and **anti-pursuit** (moving against the
objective).
(iii) **Units.** Replacing `F` by `a·F + c`, with `a > 0`, leaves `M(p̂)` unchanged and multiplies `S(p̂)` by `a`.
(iv) **Zero stakes.** `S(p̂) = 0` if and only if `p̂` is on the pursuit ray or puts all its mass on `A`. So `M(p̂) = 0`
implies `S(p̂) = 0`, and `S(p̂) = 0 < M(p̂)` exactly when `p̂` puts all its mass on `A` but splits it differently from
`q(·|A)`.

**In plain terms.** The matched pursuit is the best use of the actor's departure from the default, so the shortfall is
never negative. Multiplied by the matched intensity, it splits into three causes: misalignment, pursuing too timidly for
the departure spent, and moving against the objective. Rescaling the objective changes the stakes but not misalignment.
No misalignment means no stakes; but stakes can be zero while misalignment is not, when the actor picks only best
outcomes and splits ties its own way.

**Proof.** (i) Let `d(t) = KL(p_{F,t}‖q) = t·E_{p_{F,t}}[F] − Λ(t)`, with `Λ(t) = log E_q[e^{tF}]`. Then `d(0) = 0` and
`d'(t) = t·Var_{p_{F,t}}(F) > 0` for `t > 0`, so `d` is continuous and strictly increasing. With `m = max F`,
`Λ(t) = t·m + log E_q[e^{t(F − m)}]`, so `d(t) = t·(E_{p_{F,t}}[F] − m) − log E_q[e^{t(F − m)}]`; the first term tends
to `0` (the mass outside `A` decays exponentially in `t`) and the second to `−log q(A)`. So `d` maps `[0, ∞)` onto
`[0, −log q(A))`, and when `KL(p̂‖q) < −log q(A)` the infimum defining `λ` is attained with equality. If `λ = 0`, then
`p̂ = q` and `S(p̂) = 0`. If `0 < λ < ∞` and `KL(p‖q) ≤ KL(p_{F,λ}‖q)`, then by [P4](i) at `t = λ`,
`E_p[F] − E_{p_{F,λ}}[F] = J_λ(p) − J_λ(p_{F,λ}) + (KL(p‖q) − KL(p_{F,λ}‖q))/λ ≤ −KL(p‖p_{F,λ})/λ ≤ 0`. If `λ = ∞`,
`E_{q(·|A)}[F] = max F`, so `S(p̂) = max F − E_{p̂}[F] ≥ 0`.
(ii) Since `KL(p̂‖q) = KL(p_{F,λ}‖q)`, [P4](i) at `t = λ` gives `λ·S(p̂) = λ·(J_λ(p_{F,λ}) − J_λ(p̂)) = KL(p̂‖p_{F,λ})`.
A finite `λ` rules out the third case of [P5](iv), because a behaviour on `A` departs by at least `−log q(A)`. In the
second case, `p° = p_{F,t*}` with `E_{p°}[F] = E_{p̂}[F]`, so
`KL(p̂‖p_{F,λ}) − KL(p̂‖p°) = E_{p̂}[log(p°/p_{F,λ})] = (t* − λ)·E_{p̂}[F] − Λ(t*) + Λ(λ) = E_{p°}[log(p°/p_{F,λ})] = KL(p°‖p_{F,λ})`,
and `E_{p̂}[F] > E_q[F]`. In the first case, `p° = q`, `M(p̂) = KL(p̂‖q)`, and
`KL(p̂‖p_{F,λ}) = KL(p̂‖q) − λ·E_{p̂}[F] + Λ(λ) = M(p̂) + KL(q‖p_{F,λ}) + λ·(E_q[F] − E_{p̂}[F])`, because
`KL(q‖p_{F,λ}) = −λ·E_q[F] + Λ(λ)`.
(iii) By [P1](ii), `tilt(q, t·(a·F + c)) = tilt(q, (t·a)·F)`, so the pursuit ray of `a·F + c` is the same set as that of
`F`, and `M(p̂)` is unchanged. The matched pursuit is the same behaviour, since it is the point of the same ray with the
same departure, so both averages are transformed by `v ↦ a·v + c`, and their difference is multiplied by `a`.
(iv) If `λ = 0`, then `p̂ = q`, on the ray. If `0 < λ < ∞`, then by (ii) `S(p̂) = KL(p̂‖p_{F,λ})/λ`, which is `0`
exactly when `p̂ = p_{F,λ}`, on the ray. If `λ = ∞`, then `S(p̂) = 0` exactly when `E_{p̂}[F] = max F`, that is, when
`p̂` puts all its mass on `A`; by [P5](iv) `M(p̂) = KL(p̂‖q(·|A))` there, which is `0` exactly when `p̂ = q(·|A)`.
Finally, the closure of the ray in `Δ` is the ray together with `q(·|A)`: a sequence on the ray either has bounded
intensities, and then a subsequence converges to a point of the ray (as in the proof of [P5](iv)), or has a subsequence
with intensities tending to `∞`, which converges to `q(·|A)`. By [P5](ii), `M(p̂) = 0` means that `p̂` is in that
closure, and in both cases `S(p̂) = 0`.

**Checks.** checks/test_stakes.py::test_matched_pursuit_gets_the_most_from_the_departure,
checks/test_stakes.py::test_stakes_split_into_three_causes,
checks/test_stakes.py::test_rescaling_moves_stakes_not_misalignment, checks/test_stakes.py::test_zero_stakes

**Notes.** (ii) is v7.10's three-term decomposition of the half-ray (transverse, axial and anti-alignment) read at the
matched intensity, with names for the causes. The matched intensity converts between the two units: `λ` nats per unit of
`F`. The checks compute KL between tilts in closed form, because at large `λ` the tilts underflow in float64.

**Lineage.** v7.10: Def 22 and Thm 17(iii) (the shortfall at the same budget), Thm 13(b) (the three terms), Prop 16 and
Thm 17(iv) (what rescaling leaves unchanged), and R8-1. New: the three cases, the zero-stakes characterization, and the
names.

### P10 — Sensitivity to the specification
**Statement.** Let `F` be non-constant, `p̂ ∈ Δ`, and write `M_{q,F}` for the misalignment under the standard
specification of `F` from the default `q`. For a function `h`, `osc(h) = max h − min h`.
(i) **The default.** For all `q, q' ∈ Δ°`, `|M_{q',F}(p̂) − M_{q,F}(p̂)| ≤ osc(log(q'/q))`.
(ii) **The objective.** For every `g : X → ℝ` with `F + g` non-constant, if the revealed intensity `t*` of `p̂` under
`F` is finite, then `M_{q,F+g}(p̂) ≤ M_{q,F}(p̂) + t*·osc(g)`.

**In plain terms.** If the declared default is wrong, misalignment moves by at most the spread, in nats, of the
log-ratio between the right default and the wrong one. If the objective is wrong, misalignment moves by at most the
spread of the error times the intensity the behaviour reveals: the harder the actor pursues, the more an error in the
objective matters.

**Proof.** First, for every `r ∈ Δ°`, `p ∈ Δ` and `h : X → ℝ`, `KL(p‖tilt(r, h)) − KL(p‖r) = log E_r[e^h] − E_p[h]`, and
both terms lie in `[min h, max h]`, so the difference lies in `[−osc(h), osc(h)]`.
(i) Let `h = log(q'/q)`. By [P1](iii), `tilt(q', t·F) = tilt(tilt(q, h), t·F) = tilt(p_{F,t}, h)`, where `p_{F,t}` is
the pursuit from `q`. By the first step, `KL(p̂‖tilt(q', t·F))` and `KL(p̂‖p_{F,t})` differ by at most `osc(h)` for
every `t ≥ 0`, and so do their infima over `t ≥ 0`, which are the two misalignments.
(ii) Let `p_{F,t*}` be the nearest intended behaviour under `F`, so `M_{q,F}(p̂) = KL(p̂‖p_{F,t*})`. The pursuit of
`F + g` at intensity `t*` is `tilt(q, t*·(F + g)) = tilt(p_{F,t*}, t*·g)`, which is on the ray of `F + g`. By the first
step, `M_{q,F+g}(p̂) ≤ KL(p̂‖tilt(p_{F,t*}, t*·g)) ≤ M_{q,F}(p̂) + t*·osc(g)`.

**Checks.** checks/test_sensitivity.py::test_default_error_moves_misalignment_by_at_most_its_spread,
checks/test_sensitivity.py::test_objective_error_matters_in_proportion_to_intensity

**Notes.** Both bounds are worst cases. The first is nearly attained (a ratio above 0.9 in the check). Exchanging the
roles of `F` and `F + g` in (ii) gives the reverse bound with the revealed intensity under `F + g`. In the third case
of [P5](iv) the revealed intensity is infinite and (ii) says nothing: at the extreme of pursuit, a small error in the
objective can change the verdict entirely.

**Lineage.** New as statements. v7.10: Prop 26 (a wrong default is measured misalignment unless it leans along the
target), and NOTES §2.3 (capacity switches the regime: errors matter more at high capacity).

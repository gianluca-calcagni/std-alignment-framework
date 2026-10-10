# Diagnostics: what misalignment is made of

Results that take a measured misalignment apart, so that a test can ask where it comes from: the intensity at which it
is judged ([P43]), the other objectives the actor may be pursuing ([P44]), the runs of one procedure that differ by
chance ([P45]), and what runs share between two conditions, such as evaluation and use ([P46]); a target known only to
lie in a family ([P48]); how training on an evaluator splits misalignment into outer and inner parts ([P49]); and how
much of a change acts on the measurement rather than on the world, and what signals, audits and re-measurements reveal
of it ([P50], [P51]). One result says what the estimates cost in samples ([P47]). Each follows from earlier results;
they were derived after the first tests on data not seen before (`NOTES.md` §6), to design the next ones.

### P43 — Misalignment at any intensity
**Statement.** Under the standard specification of a non-constant `F`, let `p̂ ∈ Δ`, with revealed intensity `t*` and
nearest intended behaviour `p°` (or its limit `q(·|A)`) ([P5](iv)).
(i) For every `t ≥ 0`, `KL(p̂‖p_{F,t}) = M(p̂) + KL(p°‖p_{F,t}) + t·[E_q[F] − E_{p̂}[F]]⁺`. The middle term, the
**intensity mismatch** at `t`, is `0` exactly when `t = t*`. At the matched intensity, `t = λ`, this is [P9](ii).
(ii) **One intensity for several conditions.** Let conditions `c` have frequencies `ρ(c) > 0`; in each, let `q_c ∈ Δ°`
be the default, `F_c` a non-constant objective, and `p_c ∈ Δ` a behaviour with misalignment `M_c`, finite revealed
intensity `t*_c` and nearest intended behaviour `p°_c`. With `a_c = [E_{q_c}[F_c] − E_{p_c}[F_c]]⁺`, the misalignment at
one shared intensity ([P24], Notes) is
`min_{t≥0} Σ_c ρ(c)·KL(p_c‖p_{c,F_c,t}) = Σ_c ρ(c)·M_c + min_{t≥0} Σ_c ρ(c)·[KL(p°_c‖p_{c,F_c,t}) + t·a_c]`, and both
minima are attained. The excess over `Σ_c ρ(c)·M_c` depends on each condition only through `q_c`, `F_c`, `t*_c` and
`a_c`, and it is `0` exactly when all the `t*_c` are equal.

**In plain terms.** Judged against a pursuit at some other strength than its own, a behaviour carries two costs beyond
its misalignment: how far its nearest pursuit is from the pursuit at that strength, and, if it did worse than the
default, that loss times the strength. So when several situations must all be pursued at one strength, the extra
misalignment depends only on how strongly each situation was pursued, never on what else the actor did there.

**Proof.** (i) Write `Λ(t) = log E_q[e^{t·F}]`, so `KL(p‖p_{F,t}) = KL(p‖q) − t·E_p[F] + Λ(t)` for every `p ∈ Δ`. In the
first case of [P5](iv), `p° = q`, `M(p̂) = KL(p̂‖q)` and `E_{p̂}[F] ≤ E_q[F]`; since `KL(q‖p_{F,t}) = −t·E_q[F] + Λ(t)`,
`KL(p̂‖p_{F,t}) = M(p̂) + KL(q‖p_{F,t}) + t·(E_q[F] − E_{p̂}[F])`. In the second, `p° = p_{F,t*}` with
`E_{p°}[F] = E_{p̂}[F] > E_q[F]`, and
`KL(p̂‖p_{F,t}) − KL(p̂‖p°) = E_{p̂}[log(p°/p_{F,t})] = (t* − t)·E_{p̂}[F] − Λ(t*) + Λ(t)`, which equals
`E_{p°}[log(p°/p_{F,t})] = KL(p°‖p_{F,t})` because the two averages of `F` agree. In the third, `p̂` puts all its mass
on `A`, `E_{p̂}[F] = max F`, and `M(p̂) = KL(p̂‖q) + log q(A)`; also `KL(q(·|A)‖p_{F,t}) = −log q(A) − t·max F + Λ(t)`,
and the two add up to `KL(p̂‖q) − t·max F + Λ(t) = KL(p̂‖p_{F,t})`. In the last two cases the last term is `0`. The
mismatch is `0` exactly when `p° = p_{F,t}`: the map `t ↦ p_{F,t}` is one to one, because `t ↦ E_{p_{F,t}}[F]` increases
strictly (proof of [P9](i)), and `q(·|A)` is not a pursuit at a finite intensity, since `A ≠ X`.
(ii) Apply (i) in each condition, weight by `ρ(c)`, and minimize over `t`. Each `KL(p°_c‖p_{c,F_c,t})` is continuous and
convex in `t`, being `Λ_c(t) − t·E_{p°_c}[F_c]` plus a constant, and it tends to infinity as `t → ∞`, because `p°_c` has
full support while the mass of `p_{c,F_c,t}` outside the outcomes where `F_c` is largest tends to `0`. So the minimum is
attained. If all the `t*_c` equal some `τ`, then at `t = τ` every mismatch is `0`, and `τ·a_c = 0`: either `τ = 0`, or
every `t*_c > 0`, so every `a_c = 0`. Conversely, if the excess is `0` at its minimizer `t`, every mismatch is `0`
there, so every `t*_c = t` by (i).

**Checks.** checks/test_diagnostics.py::test_misalignment_at_any_intensity,
checks/test_diagnostics.py::test_one_intensity_for_several_conditions

**Notes.** W1's report judged best-of-`n` in 1,000 prompts at one shared intensity and found misalignment higher by
`0.138` nats at `n = 16` than with each prompt at its own (`cases/w1-best-of-n-slope/REPORT.md`). By (ii), that excess
is set entirely by how the revealed intensities differ across prompts, and by the prompts where best-of-`n` lowered the
gold: a fixed `n` is not a fixed intensity. A principal who asks for one intensity, as KL-regularized training with one
coefficient does, should report the excess apart from the misalignment of each condition.

**Lineage.** v7.10: Thm 13(b), the three-term decomposition of the half-ray (transverse, axial and anti-alignment),
which [P9](ii) reads at the matched intensity only. New: the reading at any intensity, and across conditions at one
intensity.

### P44 — What named objectives explain
**Statement.** Under the standard specification of a non-constant `F`, let `p̂ ∈ Δ°`, whose revealed intensity `t*` is
then finite, have nearest intended behaviour `p°` ([P5](iv)). Let `G_1, …, G_k` be functions on `X`, the
**named objectives**, and let `𝓛 = {p ∈ Δ : E_p[F] = E_{p̂}[F] and E_p[G_j] = E_{p̂}[G_j] for every j}`, a linear set
([D7]) that contains `p̂`. The **named pursuit** `p̃` of `p̂` is the behaviour in `𝓛` nearest to `p°`, that is,
minimizing `KL(·‖p°)` over `𝓛` ([P15](i)).
(i) `p̃ = tilt(q, a·F + Σ_j b_j·G_j)` for some numbers `a` and `b_j`, and `p̃` has the revealed intensity `t*` and the
nearest intended behaviour `p°`.
(ii) `M(p̂) = KL(p̂‖p̃) + M(p̃)`. The first term, the **unexplained misalignment**, is `0` exactly when `p̂` is itself a
tilt of the default by some `a·F + Σ_j b_j·G_j`; the second is the **named misalignment**.
(iii) Naming more objectives moves misalignment from the first term to the second: if `p̃'` is the named pursuit for
`G_1, …, G_{k'}`, with `k' > k`, then `KL(p̂‖p̃) = KL(p̂‖p̃') + KL(p̃'‖p̃)` and `M(p̃') = M(p̃) + KL(p̃'‖p̃)`.
(iv) **At the start of a change.** Let `s ↦ p_s` be a path as in [P11], with revealed objective `H` at `s = 0` and
`Cov_q(H, F) > 0`, and let the functions `1, F, G_1, …, G_k` be linearly independent. Let `R²_F` and `R²_{F,G}` be the
squared multiple correlations, under `q`, of `H` with `F` and with `F, G_1, …, G_k`, and `p̃_s` the named pursuit of
`p_s`. As `s → 0`, `KL(p_s‖p̃_s)/KL(p_s‖q) → 1 − R²_{F,G}` and `M(p̃_s)/KL(p_s‖q) → R²_{F,G} − R²_F`.

**In plain terms.** When one suspects what else an actor pursues besides the declared objective, such as a second
reward, the length of its answers, or how typical its answers are, its misalignment splits exactly into what those named
objectives explain and what nothing named explains. Naming more objectives only moves misalignment from the unexplained
part to the named part. For small changes, the two parts are the familiar shares of variance that a regression leaves
unexplained and adds.

**Proof.** (i) `𝓛` contains `p̂`, which has full support, so [P15](i) gives one nearest behaviour, and [P15](iii) gives
`p̃ = tilt(p°, θ_0·F + Σ_j θ_j·G_j)` for some numbers `θ`. As `t*` is finite, `p° = tilt(q, t*·F)`, so
`p̃ = tilt(q, (t* + θ_0)·F + Σ_j θ_j·G_j)`, a behaviour of full support. Since `p̃ ∈ 𝓛`, `E_{p̃}[F] = E_{p̂}[F]`, and
[P5](iv) depends on a behaviour only through its average of `F` when that average is below `max F`, as it is for a
behaviour of full support: so `p̃` has the same case of [P5](iv), the same `t*` and the same `p°` as `p̂`.
(ii) [P15](v) with `𝓕 = 𝓛`, which contains `p̂`, gives `M(p̂) = KL(p̂‖p̃) + KL(p̃‖p°)`, and `KL(p̃‖p°) = M(p̃)` by (i).
If `p̂ = p̃`, it is such a tilt by (i). Conversely, if `p̂ = tilt(q, a·F + Σ_j b_j·G_j)`, then for every `p ∈ 𝓛`,
`KL(p‖p°) − KL(p‖p̂) = E_p[log(p̂/p°)]`, which depends on `p` only through its averages of `F` and the `G_j`, the same
for all of `𝓛`; so `KL(p‖p°)` and `KL(p‖p̂)` have the same minimizer over `𝓛`, which is `p̂`.
(iii) Let `𝓛'` be the linear set for `G_1, …, G_{k'}`, so `p̂ ∈ 𝓛' ⊆ 𝓛`. By [P15](iii) on `𝓛`,
`KL(p‖p°) = KL(p‖p̃) + KL(p̃‖p°)` for every `p ∈ 𝓛`, so on `𝓛'` the behaviour nearest to `p°` is the behaviour nearest
to `p̃`: `p̃'` is both. [P15](iii) on `𝓛'`, with `p̃` in the role of `r`, gives `KL(p̂‖p̃) = KL(p̂‖p̃') + KL(p̃'‖p̃)`.
With (ii) for `p̃` and for `p̃'`, `M(p̃') = M(p̂) − KL(p̂‖p̃') = M(p̃) + KL(p̃'‖p̃)`.
(iv) Write `Φ = (F, G_1, …, G_k)` and `C = Cov_q(Φ)`, which is invertible because `1, F, G_1, …, G_k` are linearly
independent. As in the proof of [P11], `p_s = tilt(q, s·H + O(s²))`, so `E_{p_s}[Φ] = E_q[Φ] + s·Cov_q(Φ, H) + O(s²)`,
and `E_{p_s}[F] > E_q[F]` for small `s > 0`, so the revealed intensity of `p_s` is positive, and finite as `p_s ∈ Δ°`.
The map `c ↦ E_{tilt(q, c·Φ)}[Φ]` has derivative `C` at `c = 0`; by the inverse function theorem and the uniqueness in
[P15](i), `p̃_s = tilt(q, c_s·Φ)` with `c_s = s·β + O(s²)`, where `β = C^{−1}·Cov_q(Φ, H)` are the coefficients of the
least-squares fit of `H` on `Φ` under `q`. By the second-order expansion in the proof of [P11],
`KL(p_s‖p̃_s) = ½·s²·Var_q(H − β·Φ) + O(s³) = ½·s²·Var_q(H)·(1 − R²_{F,G}) + O(s³)` and
`KL(p_s‖q) = ½·s²·Var_q(H) + O(s³)`, which gives the first limit. By [P11], `M(p_s)/KL(p_s‖q) → sin²θ = 1 − R²_F`, since
`cos θ` is the correlation of `H` with `F`; (ii) gives the second limit.

**Checks.** checks/test_diagnostics.py::test_named_objectives_split_misalignment,
checks/test_diagnostics.py::test_named_shares_at_the_start

**Notes.** Naming `G = log q` asks whether the actor sharpens the default: `tilt(q, a·F + b·log q)` is proportional to
`q^{1+b}·e^{a·F}`, a pursuit of `F` from the default at another temperature, sharper when `b > 0`. Other natural names
in machine learning are the length of an answer, a second reward model, or the log-probability under another model. The
increments of (iii) depend on the order in which objectives are named, as sequential sums of squares do in a regression;
the total named misalignment does not. Named misalignment is not evidence that the actor pursues the named objectives:
it says how much of the misalignment their averages account for. Whether the changes reveal one fixed objective in their
span is the question of [P3]. Outside small changes, the shares of (iv) are not regression shares: on random instances
with a median departure of `2.6` nats, the `R²` of `log(p̂/q)` on `F` misses the pursuit share by a median `0.22` under
`p̂` and `0.13` under `q`, against `0.005` at departures near `0.005` nats (`probes/diagnostics/probe_named.py`). So a
test should estimate the parts in nats, as `KL` (whose cost [P47] gives), and use a regression only where the departure
is small.

**Lineage.** New. It is [P15](v) with a linear set chosen as a diagnosis, not as a limit of the actor; (iv) extends
[P11]. v7.10: Def 21 and R7-10 (drift inside cells that the principal's resolution forgives), a different way to leave
part of a change unexplained.

### P45 — Drift: what runs share, and what they do not
**Statement.** Let `p̂_1, …, p̂_m ∈ Δ`, with `m ≥ 2`, be **runs**, such as the behaviours left by separate runs of one
training procedure, with weights `w_i > 0` that add up to `1`. Let `p̄ = Σ_i w_i·p̂_i`, and let the **drift** of the
runs be `D = Σ_i w_i·KL(p̂_i‖p̄)`. Let `(q, 𝓘)` be a specification.
(i) For every `r ∈ Δ°`, `Σ_i w_i·KL(p̂_i‖r) = KL(p̄‖r) + D`. So the **shared misalignment** of the runs,
`inf_{r∈𝓘} Σ_i w_i·KL(p̂_i‖r)`, their misalignment against one intended behaviour, is `M(p̄) + D`, and it is at least
`Σ_i w_i·M(p̂_i)`.
(ii) `0 ≤ D ≤ −Σ_i w_i·log w_i ≤ log m`. `D = 0` exactly when all the runs are equal, and `D = −Σ_i w_i·log w_i` exactly
when no two runs give positive probability to the same outcome.
(iii) **Few runs.** Let the runs be `m` independent draws, with equal weights, of a random behaviour `P` whose mean
`p̄_∞ = E[P]` has full support, and let `D_∞ = E[KL(P‖p̄_∞)]`, the drift of the procedure. Then
`E[D] = D_∞ − E[KL(p̄‖p̄_∞)]`, and `0 ≤ E[KL(p̄‖p̄_∞)] ≤ E[χ²(P‖p̄_∞)]/m`, where `χ²(p‖r) = Σ_x (p(x) − r(x))²/r(x)`. So
few runs underestimate the drift, on average.
(iv) **Small drift.** If `P = p̄_∞ + ε·V` for a bounded random function `V` with `Σ_x V(x) = 0`, `E[V] = 0`, and `V ≠ 0`
with positive probability, then `E[D]/D_∞ → 1 − 1/m` as `ε → 0`. So `m·D/(m − 1)` corrects few runs for small drift.

**In plain terms.** Train the same way several times and the runs differ. Judged against one intended behaviour, their
misalignment splits exactly into the misalignment of their average and the drift: how much an outcome tells about which
run produced it. Drift cannot exceed what the run's label can tell, at most `log m` nats for `m` runs, so a few runs see
only small drift in full. On average they see less drift than there is, about a fraction `1 − 1/m` of it when it is
small.

**Proof.** (i) Where `p̂_i(x) > 0`, `log(p̂_i(x)/r(x)) = log(p̂_i(x)/p̄(x)) + log(p̄(x)/r(x))`; averaging under `p̂_i`
and weighting by `w_i` gives the identity, since `Σ_i w_i·p̂_i = p̄`. Equivalently, it is [P39](i) for two actors, the
run label with behaviour `w` and the outcome, whose coordination is `D`. Taking the infimum over `r ∈ 𝓘` of both sides
gives `M(p̄) + D` ([D3]), and the infimum of a weighted sum is at least the weighted sum of the infima.
(ii) `D ≥ 0` as a weighted sum of divergences, and `D = 0` exactly when every `p̂_i = p̄`. Where `p̂_i(x) > 0`,
`p̄(x) ≥ w_i·p̂_i(x)`, so `log(p̂_i(x)/p̄(x)) ≤ −log w_i`, with equality exactly when no other run gives `x` positive
probability; averaging gives `D ≤ −Σ_i w_i·log w_i`, which is at most `log m` (Gibbs' inequality).
(iii) (i) with `r = p̄_∞` gives `(1/m)·Σ_i KL(p̂_i‖p̄_∞) = KL(p̄‖p̄_∞) + D`; the expectation of the left side is `D_∞`.
By Jensen's inequality, `KL(p‖r) = E_p[log(p/r)] ≤ log E_p[p/r] = log(1 + χ²(p‖r)) ≤ χ²(p‖r)`. Since the runs are
independent with mean `p̄_∞`, `E[(p̄(x) − p̄_∞(x))²] = Var(P(x))/m` for each `x`, so `E[χ²(p̄‖p̄_∞)] = E[χ²(P‖p̄_∞)]/m`.
(iv) For `p = r + δ` with `r ∈ Δ°` and `Σ_x δ(x) = 0`,
`KL(p‖r) = Σ_x (r(x) + δ(x))·log(1 + δ(x)/r(x)) = ½·Σ_x δ(x)²/r(x) + O(‖δ‖³)`. With `δ = ε·V`,
`D_∞ = ½·ε²·E[Σ_x V(x)²/p̄_∞(x)] + O(ε³)`, where the expectation is positive. The average of the runs is `p̄_∞ + ε·V̄`,
with `V̄` the average of `m` independent copies of `V`, so `E[KL(p̄‖p̄_∞)] = ½·ε²·E[Σ_x V(x)²/p̄_∞(x)]/m + O(ε³)`. By
(iii), `E[D]/D_∞ → 1 − 1/m`.

**Checks.** checks/test_diagnostics.py::test_drift_splits_shared_misalignment,
checks/test_diagnostics.py::test_drift_from_few_runs

**Notes.** Drift is the mutual information between the run and the outcome [@cover2006]. With finitely many runs,
`M(p̄)` is not purely what the runs share: the average keeps part of each run's drift, and as `m` grows it tends to
`M(p̄_∞)`, the misalignment of what the procedure does on average. When drift is large, `D` saturates near `log m` and
the average absorbs the rest, so two runs can confirm a small drift but only bound a large one from below: telling drift
of `d` nats from what runs share needs `m` of order `e^d` runs. The same split applies to any repetitions that should
not matter to the principal: random seeds, data orders, or sampling at another time.

**Lineage.** New. It is [P39](i) with the run label as a second actor; (iii) and (iv) are the information-theoretic
counterpart of the bias of the sample variance.

### P46 — What runs share between conditions, and what they do not
**Statement.** Let runs `i = 1, …, m`, with weights `w_i > 0` that add up to `1`, behave as `p_{i,e} ∈ Δ°` and
`p_{i,u} ∈ Δ` in two conditions `e` and `u` ([D8]), say evaluation and use. Let `p̄_c = Σ_i w_i·p_{i,c}` and, where
`p̄_c(x) > 0`, `ν_c(i|x) = w_i·p_{i,c}(x)/p̄_c(x)`, how strongly the outcome `x` points to run `i` in condition `c`.
(i) `Σ_i w_i·KL(p_{i,u}‖p_{i,e}) = KL(p̄_u‖p̄_e) + Σ_x p̄_u(x)·KL(ν_u(·|x)‖ν_e(·|x))`: the average difference between
the conditions is the **reproducible difference**, between the runs' averages, plus the **run-specific difference**.
(ii) If each run's response depends on the condition only through a view with `ε_i = KL(V_{i,u}‖V_{i,e})` finite ([D8],
[P16]), the average of the runs responds through a view with `KL` equal to `ε̄ = Σ_i w_i·ε_i`. So `KL(p̄_u‖p̄_e) ≤ ε̄`,
and [P17] applies to the average of the runs, with `p̄_e` observed and `ε = ε̄`.
(iii) Under one specification in both conditions, the shared misalignment of the runs ([P45]) is higher in `u` than in
`e` by `(M(p̄_u) − M(p̄_e)) + (D_u − D_e)`, with `D_c` the drift of the runs in `c`: a gap between the runs' averages,
plus a gap between the drifts.
(iv) If the runs are `m` independent draws of a random pair of behaviours `(P_e, P_u)`, with `P_e ≥ κ` everywhere for
some `κ > 0`, and means `p̄_{∞,e}`, `p̄_{∞,u}`, then `E[KL(p̄_u‖p̄_e)] ≥ KL(p̄_{∞,u}‖p̄_{∞,e})`: measured from finitely
many runs, the reproducible difference is overstated, on average.

**In plain terms.** Train an actor several times, and watch every run in two situations, say while it is evaluated and
in use. How differently the runs act in the two situations splits exactly into a part their average shows and a part
that changes from run to run. An actor that, in every run, behaves better only when evaluated shows the first part; runs
that differ at random show the second. The first part is bounded by how well the runs can tell the two situations apart.
Few runs overstate it.

**Proof.** (i) Take as outcomes the pairs `(i, x)`, and in condition `c` the behaviour `w_i·p_{i,c}(x)`, which is
`p̄_c(x)·ν_c(i|x)`. The divergence between the conditions is, on one hand, `Σ_i w_i·KL(p_{i,u}‖p_{i,e})`, because the
weights cancel in the ratio. On the other, writing each behaviour as `p̄_c(x)·ν_c(i|x)` and splitting the logarithm of
the ratio into `log(p̄_u(x)/p̄_e(x)) + log(ν_u(i|x)/ν_e(i|x))` gives the right side; every term is finite, as `p_{i,e}`
has full support.
(ii) Let the average of the runs receive the signal `(i, z)`, with `i` drawn by `w` and `z` from run `i`'s view; in
condition `c` its distribution is `w_i·V_{i,c}(z)`, and it responds to `(i, z)` as run `i` responds to `z`. Its
behaviour is `p̄_c`, and the `KL` between its views in `u` and `e` is `Σ_i w_i·KL(V_{i,u}‖V_{i,e}) = ε̄`, because the
weights cancel. [P16](ii) and [P17] apply to it as stated, with `p̄_e ∈ Δ°`.
(iii) [P45](i) in each condition.
(iv) `KL` is jointly convex, and continuous on the pairs whose second member is at least `κ` everywhere, so by Jensen's
inequality, `E[KL(p̄_u‖p̄_e)] ≥ KL(E[p̄_u]‖E[p̄_e]) = KL(p̄_{∞,u}‖p̄_{∞,e})`.

**Checks.** checks/test_diagnostics.py::test_runs_split_differences_between_conditions,
checks/test_diagnostics.py::test_average_of_runs_stays_within_the_leak

**Notes.** This is the measurable part of what is called feigned or deceptive alignment: a reproducible difference that
leaves the runs closer to the intended set when evaluated, `M(p̄_u) > M(p̄_e)`. The framework sees behaviour, not
intent: a reproducible difference is also what legitimate sensitivity to the situation produces, and the declaration
says whether the two situations should be treated alike ([D4], [D8]). [P37] gives one mechanism for a reproducible gap,
a strong incentive present only when evaluated. The order of the split matters: averaging the runs first, then comparing
the conditions, isolates what every run does differently; the chain rule in the other order splits the same total in
another way. Run-specific differences are what a single run would show and a second run would not, so a test of feigned
alignment on one run cannot tell the two apart.

**Lineage.** New. It extends [P16] and [P17] from one actor to several runs, by the chain rule of `KL` as in [P39](i).

### P47 — The cost of reweighting
**Statement.** Let `p ∈ Δ`, and `r ∈ Δ` with `r(x) = 0` wherever `p(x) = 0`; on the support of `p`, let `w = r/p`.
(i) `E_p[w] = 1` and `E_p[w²] = 1 + χ²(r‖p) ≥ e^{KL(r‖p)}`. So the average of `w` over `n` independent draws of `p`, an
estimate of the total mass of `r`, has relative variance at least `(e^{KL(r‖p)} − 1)/n`.
(ii) Under the standard specification of `F`, the average of `e^{t·F}` over `n` independent draws of `q`, an estimate of
`E_q[e^{t·F}]`, has relative variance `χ²(p_{F,t}‖q)/n`, at least `(e^{KL(p_{F,t}‖q)} − 1)/n`. At the revealed intensity
of a behaviour, `KL(p_{F,t*}‖q)` is the pursuit part of its departure ([P6]).

**In plain terms.** To learn what one behaviour would do from draws of another, by reweighting the draws, costs samples
exponentially in how far apart the two behaviours are: the variance of even the simplest such estimate grows like e to
the divergence, divided by the number of draws. The pursuit part of a departure is cheap to estimate from draws of the
default when it is small, however large the departure.

**Proof.** (i) `E_p[w] = Σ_{x: p(x)>0} r(x) = 1`, since `r` puts no mass where `p` has none.
`E_p[w²] = Σ_x r(x)²/p(x) = 1 + Σ_x (r(x) − p(x))²/p(x)`, expanding the square and using `Σ_x r(x) = Σ_x p(x) = 1`. By
Jensen's inequality, `E_p[w²] = E_r[w] ≥ exp(E_r[log w]) = e^{KL(r‖p)}`. The average of `n` independent draws of `w` has
mean `1` and variance `(E_p[w²] − 1)/n`.
(ii) (i) with `p = q` and `r = p_{F,t}`, whose ratio is `w = e^{t·F}/E_q[e^{t·F}]`; the relative variance of the average
of `e^{t·F}` is that of the average of `w`. The last sentence is [P6].

**Checks.** checks/test_diagnostics.py::test_reweighting_costs_exponentially

**Notes.** (i) is a lower bound; heavy tails make the cost larger, and the bound is attained when `r` is `p` restricted
to a set. In terms of the effective sample size `n/E_p[w²]` used in importance sampling, at most `n·e^{−KL(r‖p)}` of `n`
draws count. For a language model, whose log-probabilities are known, the departure `KL(p̂‖q)` is the average of
`log(p̂/q)` over the actor's own draws, with no reweighting; the revealed intensity and the pursuit part need averages
under pursuits of the default, from draws of the default, at the cost of (ii). So misalignment, the departure minus the
pursuit part ([P6]), needs a number of draws of the default of the order of `e` to the pursuit part. In case W3 the
pursuit part was estimated at about `0.74` nats on average, a relative variance of at least `(e^{0.74} − 1)/n ≈ 1.1/n`,
but a named pursuit that sharpens the default ([P44], Notes) may depart much further, and cost much more. From the
actor's own draws, the cost is set by `KL(p°‖p̂)`, which is not `M(p̂)` but the divergence the other way.

**Lineage.** New. The inequality is standard; the reading as the cost of the diagnostics above is new.

### P48 — Misalignment when the target is uncertain
**Statement.** Let `F_1, …, F_k` be functions on `X`, write `Φ = (F_1, …, F_k)`, and let `𝒮` be the set of non-constant
combinations `c·Φ`, the objectives a principal may hold when its target is known only to lie in their span. For
`F' ∈ 𝒮`, let `M_{F'}` be misalignment under the standard specification of `F'` from the default `q`. Let `p̂ ∈ Δ°`, and
let `p̃` be the behaviour nearest to `q` among those with `p̂`'s averages of `Φ` ([P15](i)).
(i) **The most charitable principal.** `p̃ = tilt(q, c̃·Φ)` for some `c̃`, and `M_{F'}(p̂) ≥ KL(p̂‖p̃)` for every
`F' ∈ 𝒮`. If `p̃ ≠ q`, equality holds for `F' = c̃·Φ`, the **most charitable principal**; if `p̃ = q`, every
`M_{F'}(p̂)` equals `KL(p̂‖q)`.
(ii) **The least charitable.** `M_{F'}(p̂) ≤ KL(p̂‖q)` for every `F' ∈ 𝒮`, with equality whenever
`E_{p̂}[F'] ≤ E_q[F']`, which holds for `F'` or for `−F'`.
(iii) So, for every principal whose objective lies in `𝒮`, misalignment lies in `[KL(p̂‖p̃), KL(p̂‖q)]`, and both ends
are attained. With `Φ = (F, G_1, …, G_k)`, `p̃` is the named pursuit of [P44], and the lower end is its unexplained
misalignment.

**In plain terms.** When the principal's goal is not known exactly, but is known to be some mix of given objectives,
misalignment is not one number but an interval. Its lower end is what even the most charitable principal of that kind
would find, the one whose goal the actor's change comes closest to pursuing; its upper end is the whole change, which a
principal wanting the opposite would find. An actor shown to be far from the lower end is far from every goal of that
kind.

**Proof.** (i) `𝓛 = {p ∈ Δ : E_p[Φ] = E_{p̂}[Φ]}` is linear and contains `p̂ ∈ Δ°`, so [P15](i) and (iii), with `q` in
the role of `r`, give `p̃ = tilt(q, c̃·Φ)` for some `c̃`. For every `c`, `log(p̃/tilt(q, c·Φ))` is `(c̃ − c)·Φ` plus a
constant, whose average is the same under `p̂` and `p̃`, so
`KL(p̂‖tilt(q, c·Φ)) − KL(p̂‖p̃) = E_{p̂}[log(p̃/tilt(q, c·Φ))] = KL(p̃‖tilt(q, c·Φ)) ≥ 0`. Every pursuit `p_{F',t}`
with `F' ∈ 𝒮` and `t ≥ 0` is such a tilt, with `c` a multiple of `F'`'s coefficients, so `M_{F'}(p̂) ≥ KL(p̂‖p̃)`. If
`p̃ ≠ q`, `F' = c̃·Φ` is not constant, and the mean of `F'` under `tilt(q, F')` exceeds its mean under `q`, because
tilting by a non-constant function raises its mean (the derivative of `t ↦ E_{p_{F',t}}[F']` is a positive variance); as
`E_{p̂}[F'] = E_{p̃}[F']` and `E_{p̂}[F'] < max F'` for `p̂ ∈ Δ°`, the second case of [P5](iv) applies with `t* = 1`,
and `M_{F'}(p̂) = KL(p̂‖p̃)`. If `p̃ = q`, every `F' ∈ 𝒮` has `E_{p̂}[F'] = E_q[F']`, so the first case of [P5](iv)
gives `M_{F'}(p̂) = KL(p̂‖q)`.
(ii) The bound is [P6], and the equality is the first case of [P5](iv). `E_{p̂}[F'] − E_q[F']` changes sign with `F'`,
and `−F' ∈ 𝒮`.
(iii) follows from (i) and (ii). For `Φ = (F, G_1, …, G_k)`, [P44](i) makes the named pursuit a tilt of `q` by a
combination of `Φ` with `p̂`'s averages of `Φ`; the identity in (i), applied to it and to `p̃` both ways, gives
`KL(p̃‖p_*) + KL(p_*‖p̃) = 0` for such a tilt `p_*`, so it is `p̃`.

**Checks.** checks/test_diagnostics.py::test_an_uncertain_target_gives_an_interval

**Notes.** With no restriction on the target, the lower end is `0`: if the span contains `log(p̂/q)`, then `p̃ = p̂`,
which is [P1]: every behaviour pursues its own revealed objective. So a test without a declared target can say nothing
about alignment, and a test with a declared family can bound it, as an unobserved condition is bounded by [P17]. The
interval depends only on the span of `Φ`, not on which function is called the target. In case W4
(`cases/w4-two-runs/RESULTS.md`), for every principal whose objective combines the run's reward, `log R`, the other
run's reward and the other run's revealed objective, run A is between `9.46` and `12.28` nats misaligned. A family with
signs, such as a non-negative weight on a reward, is a subset of the span, so its interval lies inside this one; its
ends then need a constrained minimization, not stated here.

**Lineage.** New, from the PI's question whether W3 and W4 had a proper target (`NOTES.md` §7). It reads [P44]'s
unexplained misalignment as the least misalignment over a family of principals; inverse reinforcement learning meets the
same ambiguity as the set of rewards consistent with behaviour (`RELATED.md`).

### P49 — Outer and inner misalignment
**Statement.** Let a principal's target `F` and a trainer's evaluator `F̂` be non-constant functions on `X`, judged from
one default `q`; write `M_P` for misalignment under the standard specification of `F`, and `M_T` under that of `F̂`,
whose intended behaviours are the optima of training on `F̂` with a KL penalty ([P4]).
(i) **Outer misalignment.** At intensity `t ≥ 0`, the **outer misalignment** is `O(t) = M_P(p_{F̂,t})`, the principal's
misalignment of the trainer's own optimum. If `F̂ = a·F + c` with `a > 0`, then `O(t) = 0` for every `t`; otherwise
`O(t) > 0` for every `t > 0`. As `t → 0`, `O(t)/KL(p_{F̂,t}‖q) → sin²θ` if `cos θ ≥ 0`, and `→ 1` otherwise, with `θ`
the angle of [P11] between `F̂` and `F`.
(ii) **Inner misalignment and the split.** The **inner misalignment** of a behaviour `p̂ ∈ Δ°` is `M_T(p̂)`. Let `p̃` be
the tilt of `q` by a combination of `F` and `F̂` with `p̂`'s averages of both ([P48]). Then `M_P(p̂) = U + M_P(p̃)` and
`M_T(p̂) = U + M_T(p̃)`, with the same **strict inner misalignment** `U = KL(p̂‖p̃)`: the least misalignment that any
principal whose target combines `F` and `F̂` finds in `p̂` ([P48]).
(iii) **The two limits.** A perfect optimizer of the training objective, `p̂ = p_{F̂,t}`, has `U = 0` and `M_T(p̂) = 0`,
and its misalignment is all outer: `M_P(p̂) = O(t)`. An evaluator that is the target up to a positive scale and a
constant, `F̂ = a·F + c` with `a > 0`, has `O = 0` and `M_T = M_P`: all misalignment is inner.

**In plain terms.** Training on an evaluator in place of the target fails in two ways. Outer misalignment is a fault of
the specification: even a perfect optimizer of the training objective is that far from what the principal wants, and it
is zero only when the evaluator is the target rescaled. Inner misalignment is a fault of the optimizer: how far the
trained actor is from anything the training objective could produce. The principal's and the trainer's misalignments
share one part exactly, the change that pursues neither the target nor the evaluator; the rest is how the actor's
pursuit, within what target and evaluator can describe, leans away from each.

**Proof.** (i) If `F̂ = a·F + c` with `a > 0`, then `p_{F̂,t} = p_{F,at}` by [P1](ii), which is on the principal's ray.
Otherwise, if `O(t) = 0` for some `t > 0`, the full-support `p_{F̂,t}` is in the closure of `F`'s ray, hence on it
([P5](ii)), so `tilt(q, t·F̂) = tilt(q, s·F)` for some `s ≥ 0`, and `t·F̂ − s·F` is constant by [P1](ii); `s > 0`
because `F̂` is not constant, a contradiction. The limit is [P11] for the path `t ↦ p_{F̂,t}`, whose revealed objective
at `t = 0` is `F̂`.
(ii) `p̂` and `p̃` have the same averages of `F` and of `F̂`, so `p̃` is the named pursuit of [P44] both for the
principal's specification with `F̂` named and for the trainer's with `F` named ([P48](iii)). [P44](ii) gives both
identities, with the same first term `KL(p̂‖p̃)`, and [P48](i) gives its reading as the least misalignment over the
principals whose target lies in the span of `F` and `F̂`.
(iii) `p_{F̂,t}` is on the trainer's ray, so `M_T(p̂) = 0`, and it is a tilt of `q` by a combination of `F` and `F̂`, so
`U = 0` by [P44](ii); `M_P(p̂) = O(t)` by definition. If `F̂ = a·F + c` with `a > 0`, the two rays are the same set by
[P1](ii), so the two specifications, and their misalignments, are the same ([P9](iii)), and `O = 0` by (i).

**Checks.** checks/test_diagnostics.py::test_outer_and_inner_misalignment

**Notes.** Outer misalignment needs the principal's target: case W1 had one, a gold reward model, and W3 and W4 had
none, so they measured inner misalignment only (`NOTES.md` §7). The growth of `O(t)` with intensity is Goodhart's law in
this framework: how the principal's objective moves along the evaluator's ray is governed by the regression of `F` on
`F̂` ([P18]–[P20], [P25]). Inner misalignment splits further by the diagnostics above: what named objectives explain
([P44]), what recurs across runs and what is drift ([P45]), what differs between evaluation and use ([P46]), and what
the actor's limits make unavoidable ([P15]). When the principal's target is uncertain, both outer misalignment and the
split become intervals over the declared family ([P48]). The split assumes one default for principal and trainer; with
two defaults, the change of default adds a term of its own.

**Lineage.** v7.10: Cor 1.5 and A16 (stacked stages, with an outer–inner cross term at second order), and H12 (the chain
rule of KL may give the archive's five gaps back as additive terms); the outer and inner alignment of Hubinger et al.
[@hubinger2019], as a two-link chain (`RELATED.md`). New: the exact split, and outer misalignment as a function of
intensity.

### P50 — Tampering: a change of the measurement, not of the world
**Statement.** Let the outcomes be pairs, `X = W × S`: a state `w` of the world, and a signal `s`, the measurement from
which an evaluator is computed. Let the default be `q(w, s) = q_W(w)·K(s|w)`, with `q_W` a full-support distribution on
`W` and `K` a **channel**: for each `w`, a full-support distribution `K(·|w)` on `S`, the honest measurement of `w`. For
`p ∈ Δ`, let `p_W` be its distribution of worlds and, where `p_W(w) > 0`, `p(·|w)` its distribution of signals given
`w`; for a distribution `r_W` on `W`, let `r_W ⊗ K` be the behaviour `r_W(w)·K(s|w)`. The **tampering** of `p` is
`T(p) = Σ_{w : p_W(w) > 0} p_W(w)·KL(p(·|w)‖K(·|w))`, and `p` is **grounded** if `T(p) = 0`, that is, if `p = p_W ⊗ K`.
A function on `W` or on `S` is read as a function on `X`.
(i) **The split.** For every `p ∈ Δ` and every distribution `r_W` on `W`, `KL(p‖r_W ⊗ K) = KL(p_W‖r_W) + T(p)`. In
particular `KL(p‖q) = KL(p_W‖q_W) + T(p)`: the departure is the change of the world plus the tampering.
(ii) **A target on the world charges all tampering.** Let `F` be a non-constant function on `W`. The intended behaviours
of the standard specification of `F` are `p_{F,t} = tilt(q_W, t·F) ⊗ K`, all grounded, and for every `p̂ ∈ Δ`,
`M_F(p̂) = M^W_F(p̂_W) + T(p̂)`, where `M^W_F` is misalignment under the standard specification of `F` on `W`, from
`q_W`.
(iii) **The trainer's optimum tampers.** Let the evaluator `F̂` be a non-constant function on `S`, and let
`m(w) = E_{K(·|w)}[F̂]` be the expected score of the world `w`. For `t > 0`, `p_{F̂,t}` has worlds `tilt(q_W, Λ_t)`,
with `Λ_t(w) = log E_{K(·|w)}[e^{t·F̂}]`, and signals `tilt(K(·|w), t·F̂)` given `w`, so `T(p_{F̂,t}) > 0`. As `t → 0`,
`T(p_{F̂,t})/KL(p_{F̂,t}‖q) → 1 − R²`, where `R² = Var_{q_W}(m)/Var_q(F̂)` is the share of the evaluator's variance
under the default that the world explains. For a target `F` on `W`, let `θ` be the angle of [P11] between `F̂` and `F`,
and `θ_W` the angle between `m` and `F` under `q_W` (with `R²·sin²θ_W` read as `0` when `m` is constant). Then
`sin²θ = (1 − R²) + R²·sin²θ_W`; the outer misalignment of [P49] splits as `O(t) = M^W_F((p_{F̂,t})_W) + T(p_{F̂,t})`;
and as `t → 0` the world's part, divided by `KL(p_{F̂,t}‖q)`, tends to `R²·sin²θ_W` if `cos θ ≥ 0` and to `R²`
otherwise, so that outer misalignment's share at the start, `sin²θ` or `1`, is the tampering share `1 − R²` plus the
world's.
(iv) **The best grounded behaviour.** The grounded behaviours form a linear feasible set ([D7]) that contains `q`. Among
them, the unique maximizer of the net value `J_t` of `F̂` ([P4]) is `p^g_t = tilt(q_W, t·m) ⊗ K`: the world pursues the
expected score at the same intensity, and the measurement is left alone. It is the best feasible behaviour for
`r = p_{F̂,t}` ([P15]), and what tampering adds to the net value is
`t·(J_t(p_{F̂,t}) − J_t(p^g_t)) = KL(p^g_t‖p_{F̂,t}) = log E_q[e^{t·F̂}] − log E_{q_W}[e^{t·m}]`.

**In plain terms.** Make the measurement part of what happens: each outcome records what the world became and what the
evaluator was shown. The default measures each world honestly, through a declared channel. Tampering is how far the
actor's measurements depart from the honest channel, given the world it produced; an actor that leaves the measurement
alone is grounded. The departure from the default is exactly the change of the world plus the tampering, and a principal
whose goal is stated on the world charges every nat of tampering as misalignment. The optimum of training on the
measured signal tampers at every intensity, because reweighting the signals of a world raises the score as surely as
changing the world does; at the start, the share of its change that is tampering is the share of the evaluator's
variance that is noise of the measurement. An actor that cannot tamper does best by pursuing each world's expected
score, at the same intensity, and the difference in net value is what tampering is worth.

**Proof.** (i) Where `p(w, s) > 0`, `log(p(w, s)/(r_W(w)·K(s|w))) = log(p_W(w)/r_W(w)) + log(p(s|w)/K(s|w))`; averaging
under `p` gives the identity, with both sides infinite when `r_W` misses a world that `p` produces. With `r_W = q_W` it
is the departure.
(ii) `tilt(q, t·F)(w, s) = q_W(w)·e^{t·F(w)}·K(s|w)/E_{q_W}[e^{t·F}] = tilt(q_W, t·F)(w)·K(s|w)`. By (i),
`KL(p̂‖p_{F,t}) = KL(p̂_W‖tilt(q_W, t·F)) + T(p̂)` for every `t ≥ 0`; the second term does not depend on `t`, so the
infimum over `t` ([D3]) gives the identity.
(iii) With `Z = E_{q_W}[e^{Λ_t}]`, `q_W(w)·K(s|w)·e^{t·F̂(s)}/Z = [q_W(w)·e^{Λ_t(w)}/Z]·[K(s|w)·e^{t·F̂(s)−Λ_t(w)}]`,
which gives the worlds and the signals. Each `tilt(K(·|w), t·F̂)` differs from `K(·|w)` when `t > 0`, by [P1](ii),
because `F̂` is not constant on `S`, the support of `K(·|w)`; and every world has positive mass, so `T > 0`. The
expansion in the proof of [P11] gives `KL(tilt(K(·|w), t·F̂)‖K(·|w)) = ½·t²·Var_{K(·|w)}(F̂) + O(t³)` and
`KL(p_{F̂,t}‖q) = ½·t²·Var_q(F̂) + O(t³)`; as the worlds tend to `q_W`, the ratio tends to
`E_{q_W}[Var_{K(·|w)}(F̂)]/Var_q(F̂)`, which is `1 − R²` by the law of total variance,
`Var_q(F̂) = Var_{q_W}(m) + E_{q_W}[Var_{K(·|w)}(F̂)]`. Since `F` depends on `w` only, `Cov_q(F̂, F) = Cov_{q_W}(m, F)`
and `Var_q(F) = Var_{q_W}(F)`, so `cos θ = R·cos θ_W`, with `R = (R²)^{1/2}`, and
`sin²θ = 1 − R²·cos²θ_W = (1 − R²) + R²·sin²θ_W`; when `m` is constant, `cos θ = 0` and `R = 0`. The split of `O(t)` is
(ii) at `p̂ = p_{F̂,t}`. Its share at the start is `sin²θ` if `cos θ ≥ 0` and `1` otherwise ([P49](i)); subtracting the
tampering share `1 − R²` leaves the world's.
(iv) The grounded set is cut out by the equations `p(w, s)·K(s'|w) = p(w, s')·K(s|w)`, for all `w`, `s`, `s'`, each of
the form `E_p[f] = 0`; they say that `p(·|w)` is `K(·|w)` wherever `p_W(w) > 0`. For grounded `p = p_W ⊗ K`, (i) gives
`KL(p‖q) = KL(p_W‖q_W)`, and `E_p[F̂] = E_{p_W}[m]`, so `J_t(p) = E_{p_W}[m] − KL(p_W‖q_W)/t`, the net value of `m` on
`W`, whose unique maximizer is `tilt(q_W, t·m)` by [P4](i). By [P15](iv) the maximizer over the feasible set is the best
feasible behaviour for `r = p_{F̂,t}`, and `t·(J_t(p_{F̂,t}) − J_t(p^g_t)) = KL(p^g_t‖p_{F̂,t})`. By the proof of
[P4](i), `t·J_t(p_{F̂,t}) = log E_q[e^{t·F̂}]` and, on `W`, `t·J_t(p^g_t) = log E_{q_W}[e^{t·m}]`.

**Checks.** checks/test_diagnostics.py::test_tampering_splits_the_departure

**Notes.** Tampering counts every influence of the actor on the measurement, given the world: a reward rewritten, a
sensor covered or replaced, a rater persuaded, or a measurement repeated until it comes out well. [P51] says what
signals, audits and re-measurements reveal of it, and separates the last kind from the others. What is world and what is
signal is declared, as the principal and the target are ([P48]), and the declaration decides what counts as tampering: a
text that persuades a rater is world if the world is the text, and a channel if the world is the facts the text reports
and the signal is the rater's verdict. The channel is declared with the default, before the behaviour is seen ([D3]); a
channel known only to lie in a family would give an interval, as a target does in [P48], not stated here. An evaluator
that is a fixed function of the outcome, as the reward models of cases W1 to W4 were of the text, is the case where
every `K(·|w)` is a point mass: the default then lacks full support and the statement does not apply, and nothing could
be tampered without leaving the default's support. There every gap between evaluator and target is in the world, and is
outer misalignment ([P49]), not tampering. The share `1 − R²` holds at the start only: in
`probes/diagnostics/probe_grounding.py`, with 4 worlds and 5 signals, the trainer's optimum at intensity 2 tampers by a
median `0.47` nats, and its tampering share differs from `1 − R²` by `−0.51` to `+0.21`. Two things stay outside: an
actor that changes what the principal wants, because the target is fixed by the declaration; and a change of the
evaluator's function `F̂`, unless the evaluator's output is taken as the signal, when changing it is tampering with the
channel.

**Lineage.** v7.10 archive, gap 3 (grounding: wireheading and reward tampering), which `IMPORT.md` §8 mapped as "partly;
needs": a tampered measurement there was only an outcome that the evaluator scores high and the target low. New: the
measurement as part of the outcome, tampering as a divergence from a declared channel, and its split from the change of
the world, from the PI's question in `NOTES.md` (Q32). The causal analyses of reward tampering [@everitt2021] and the
corrupted reward channel [@everitt2017] are the nearest work (`RELATED.md`).

### P51 — What signals, audits and re-measurements reveal of tampering
**Statement.** In the setting of [P50], let `p ∈ Δ`, with distribution of signals `p_S`. For a channel `C` from `W` to a
finite set `Z`, whose distributions `C(·|w)` need not have full support, and a distribution `μ` on `Z`, let
`L_C(μ) = min_{r_W} KL(μ‖C^⊤r_W)` over the distributions `r_W` on `W`, where `(C^⊤r_W)(z) = Σ_w r_W(w)·C(z|w)` is what
the world `r_W` produces through `C`; write `L = L_K`.
(i) **The least tampering the signals show.** The minimum is attained, and `T(p) ≥ L(p_S)`. If `r*_W` attains `L(p_S)`,
the behaviour `p*(w, s) = r*_W(w)·K(s|w)·p_S(s)/(K^⊤r*_W)(s)` has signals `p_S` and tampering `L(p_S)`, so no smaller
tampering is consistent with the signals; and `L(p_S) = 0` exactly when some distribution of worlds produces `p_S`
through `K`. For every `r_W` with `KL(μ‖C^⊤r_W)` finite, with `c(w) = Σ_{z : μ(z) > 0} C(z|w)·μ(z)/(C^⊤r_W)(z)`,
`KL(μ‖C^⊤r_W) − log max_w c(w) ≤ L_C(μ) ≤ KL(μ‖C^⊤r_W)`: a certificate for any computed `r_W`.
(ii) **The most.** The values of `T` over the behaviours with signals `p_S` form the interval `[L(p_S), Ū(p_S)]`, where
`Ū(p_S)` is the largest tampering among the behaviours in which every signal comes from a single world:
`p_a(w, s) = p_S(s)` if `w = a(s)` and `0` otherwise, for a map `a` from `S` to `W`. `Ū(p_S) ≥ max_w KL(p_S‖K(·|w))`,
and if `W` and `S` each have at least two elements, `Ū(p_S) > 0` for every `p_S`: no distribution of signals, not even
the default's, rules tampering out.
(iii) **An audit.** Let each world be measured a second time through a channel `K'` from `W` to a finite set `S'` that
the actor cannot influence, so that the actor's behaviour on `(w, s, s')` is `p(w, s)·K'(s'|w)`, and let `p_{SS'}` be
its distribution of the two signals. With `(K⊗K')(s, s'|w) = K(s|w)·K'(s'|w)`, `L(p_S) ≤ L_{K⊗K'}(p_{SS'}) ≤ T(p)`. If
the audit is exact, `S' = W` and `K'(·|w)` the point mass at `w`, then `L_{K⊗K'}(p_{SS'}) = T(p)`, and tampering is
identified ([D9]).
(iv) **A re-measurement.** If `K' = K`, a second honest measurement through the same channel, the evaluator's gain over
the default splits exactly into an **honest gain** and a **channel gain**:
`E_p[F̂] − E_q[F̂] = (E_{p_W}[m] − E_{q_W}[m]) + (E[F̂(s)] − E[F̂(s')])`, where both averages of the second term are
under the actor's behaviour on `(w, s, s')`, and `E[F̂(s')] = E_{p_W}[m]`. The channel gain, the fall of the average
score from the first measurement to the second, satisfies `|E[F̂(s)] − E[F̂(s')]| ≤ (max F̂ − min F̂)·(T(p)/2)^{1/2}`,
and `KL(p_S‖p_{S'}) ≤ T(p)`.

**In plain terms.** From the signals alone a principal sees only part of the tampering: the least that any actor would
need to produce signals like these, which is positive when the scores come out in a way no honest measurement of any
world produces. Some actor tampers exactly that much, so the signals cannot show more; and they cannot rule tampering
out, because every distribution of signals, even the default's, could come from an actor that tampers. An audit through
a measurement the actor cannot touch raises the lower end, up to the whole tampering when the audit sees the world
exactly. Measuring the same worlds again through the honest channel separates what the actor gained by changing the
world from what it gained through the measurement: the second shows as the fall of the score on re-measurement, and it
bounds the tampering from below.

**Proof.** (i) `r_W ↦ KL(μ‖C^⊤r_W)` is lower semicontinuous on the compact set of distributions on `W`, so the minimum
is attained; for `C = K` it is finite, as `K` has full support. By [P50](i), `T(p) = KL(p‖p_W ⊗ K)`, and merging the
pairs into their signals never increases KL ([P4](iv), whose proof needs only that the second behaviour be positive
wherever the first is), so `T(p) ≥ KL(p_S‖K^⊤p_W) ≥ L(p_S)`. The signals of `p*` are
`p_S(s)·(K^⊤r*_W)(s)/(K^⊤r*_W)(s) = p_S(s)`, and its worlds are `r*_W(w)·c*(w)`, with `c*` the `c` of the certificate at
`r*_W`, for `C = K` and `μ = p_S`. The function `r_W ↦ −Σ_s p_S(s)·log (K^⊤r_W)(s)` is convex, with partial derivatives
`−c(w)`, so at its minimum `c*(w) ≤ λ` for every `w`, with equality where `r*_W(w) > 0`; as
`Σ_w r*_W(w)·c*(w) = Σ_s p_S(s) = 1`, `λ = 1`. So the worlds of `p*` are `r*_W`, its signals given `w` are `K(·|w)·ρ`
with `ρ = p_S/(K^⊤r*_W)`, and `T(p*) = Σ_w r*_W(w)·Σ_s K(s|w)·ρ(s)·log ρ(s) = Σ_s p_S(s)·log ρ(s) = L(p_S)`.
`L(p_S) = 0` exactly when `p_S = K^⊤r_W` for some `r_W`, by Gibbs' inequality. For the certificate, let `r*_W` attain
`L_C(μ)`; by Jensen's inequality,
`KL(μ‖C^⊤r_W) − L_C(μ) = Σ_{z : μ(z) > 0} μ(z)·log((C^⊤r*_W)(z)/(C^⊤r_W)(z)) ≤ log Σ_w r*_W(w)·c(w) ≤ log max_w c(w)`.
(ii) The behaviours with signals `p_S` form a polytope: for each `s`, `p(·, s)` is `p_S(s)` times a distribution on `W`,
so the vertices are the `p_a`. `T(p) = KL(p‖p_W ⊗ K)` is convex in `p`, because KL is jointly convex and `p ↦ p_W ⊗ K`
is linear, and it is continuous, because `K` has full support. A convex function on a polytope attains its maximum at a
vertex, and a continuous function maps the connected polytope onto an interval, which contains `L(p_S)` by (i). The
constant map at `w` gives the behaviour with the single world `w` and signals `p_S`, whose tampering is
`KL(p_S‖K(·|w))`. That is positive unless `K(·|w) = p_S`. If every `K(·|w)` equals `p_S`, then `p_S` has full support on
`S`, which has two elements, so some signal `s₁` has `0 < p_S(s₁) < 1`; mapping `s₁` to one world and every other signal
to another gives tampering at least `p_S(s₁)·KL(δ_{s₁}‖p_S) = −p_S(s₁)·log p_S(s₁) > 0`, where `δ_{s₁}` is the point
mass at `s₁`.
(iii) Where `p(w, s)·K'(s'|w) > 0`, the ratio of the actor's behaviour on `(w, s, s')` to `p_W(w)·K(s|w)·K'(s'|w)` is
`p(s|w)/K(s|w)`, so the divergence between them is `T(p)`. Merging into `(s, s')`, as in (i), gives
`T(p) ≥ KL(p_{SS'}‖(K⊗K')^⊤p_W) ≥ L_{K⊗K'}(p_{SS'})`, and merging away `s'` gives
`KL(p_{SS'}‖(K⊗K')^⊤r_W) ≥ KL(p_S‖K^⊤r_W)` for every `r_W`, so `L_{K⊗K'}(p_{SS'}) ≥ L(p_S)`. For an exact audit,
`(K⊗K')^⊤r_W(s, w) = r_W(w)·K(s|w)` and `p_{SS'}(s, w) = p(w, s)`, so the divergence is
`KL(p‖r_W ⊗ K) = KL(p_W‖r_W) + T(p)` by [P50](i), least at `r_W = p_W`.
(iv) `E[F̂(s')] = Σ_{w,s,s'} p(w, s)·K(s'|w)·F̂(s') = E_{p_W}[m]`, and `E_q[F̂] = E_{q_W}[m]`, so the split is an
identity. `E_{p_W}[m]` is also the average of `F̂` under `p_W ⊗ K`, from which `p` departs by `T(p)` ([P50](i)); the
difference of two averages of `F̂` is at most `max F̂ − min F̂` times the total variation distance, which Pinsker's
inequality bounds by `(KL/2)^{1/2}` ([@polyanskiy2025], Theorem 7.10, read in its open draft). Finally
`p_{S'} = K^⊤p_W`, so `KL(p_S‖p_{S'}) ≤ T(p)` by (i).

**Checks.** checks/test_diagnostics.py::test_signals_and_audits_bound_tampering

**Notes.** (ii) is the identified set ([D9]) of tampering for a principal who sees signals only, and (iii) is the audit
as a designed observation that narrows it, as an intervention does for the pass-through ([D6]). `L(p_S)` is a problem of
maximum likelihood: the least divergence of the signals from the mixtures of the honest channel's distributions, as in
estimating the weights of a mixture. The check computes it by the fixed point `r_W ← r_W·c`, the EM iteration for those
weights, polished by a constrained solver; the certificate of (i) makes any computed `r_W` a bracket, whatever the
solver. In `probes/diagnostics/probe_grounding.py`, an actor that leaves the world at the default and measures each
world `n` times, keeping the signal the evaluator scores highest, has no honest gain, and all its gain is channel gain.
The signals alone reveal a median of about half its tampering (`49%`, `52%` and `46%` for `n` = 2, 4 and 16, from `0%`
to `98%` across instances), the fall on re-measurement through (iv)'s bound a median `30%` for `n = 4`, and an exact
audit all of it. (iv) needs the second measurement to be honest. If the actor's influence persists, as with a sensor
replaced, the second measurement goes through the actor's channel, and the fall can be `0` while `T > 0`: a
re-measurement through the same instrument exposes selection on the noise of measurement, not every tampering. Only a
channel the actor cannot influence, as in (iii), bounds both kinds from below.

**Lineage.** New, from the grounding brainstorm (`NOTES.md`, Q32). The optimality conditions in the proof of (i) are
those of a log-optimal portfolio [@cover2006], with the honest channel's distributions in the place of the assets; the
certificate follows from Jensen's inequality.

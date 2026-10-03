# Diagnostics: what misalignment is made of

Results that take a measured misalignment apart, so that a test can ask where it comes from: the intensity at which it
is judged, the other objectives the actor may be pursuing, the runs of one procedure that differ by chance, and the
situations an actor can tell apart. The last result says what the estimates cost in samples. Each follows from earlier
results; they were derived after the first tests on data not seen before (`NOTES.md` §6), to design the next ones.

### P43 — Misalignment at any intensity
**Statement.** Under the standard specification of a non-constant `F`, let `p̂ ∈ Δ`, with revealed intensity `t*` and
nearest intended behaviour `p°` (or its limit `q(·|A)`) ([P5](iv)).
(i) For every `t ≥ 0`, `KL(p̂‖p_{F,t}) = M(p̂) + KL(p°‖p_{F,t}) + t·[E_q[F] − E_{p̂}[F]]⁺`. The middle term, the
**intensity mismatch** at `t`, is `0` exactly when `t = t*`. At the matched intensity, `t = λ`, this is [P9](ii).
(ii) **One intensity for several conditions.** Let conditions `c` have frequencies `ρ(c) > 0`; in each, let `q_c ∈ Δ°`
be the default, `F_c` a non-constant objective, and `p_c ∈ Δ` a behaviour with misalignment `M_c`, finite revealed
intensity `t*_c` and nearest intended behaviour `p°_c`. With `a_c = [E_{q_c}[F_c] − E_{p_c}[F_c]]⁺`, the misalignment at
one shared intensity ([P24], Notes) is
`min_{t≥0} Σ_c ρ(c)·KL(p_c‖p_{c,F_c,t}) = Σ_c ρ(c)·M_c + min_{t≥0} Σ_c ρ(c)·[KL(p°_c‖p_{c,F_c,t}) + t·a_c]`,
and both minima are attained. The excess over `Σ_c ρ(c)·M_c` depends on each condition only through `q_c`, `F_c`, `t*_c`
and `a_c`, and it is `0` exactly when all the `t*_c` are equal.

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

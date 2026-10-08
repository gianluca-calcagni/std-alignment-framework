# Derived — identifiability

A single behaviour reveals an objective only relative to a default ([P1]). Changes of behaviour reveal more: their
objective needs no default ([P2]), and whether it stays fixed is testable ([P3]). This file adds how much of a change
is misaligned, read from its first step ([P11]); what interventions reveal about how an actor responds ([P12]); how
much of the objective a change gains ([P13]); and what an actor can hide in conditions that are not observed, given
what it can perceive ([P16], [P17]). Each result also says what cannot be revealed.

### P11 — The misaligned share at the start of a change
**Statement.** Let `F` be non-constant, and let `s ↦ p_s`, for `s ≥ 0`, be a twice continuously differentiable path in
`Δ°` with `p_0 = q`, whose revealed objective `G` at `s = 0` is non-constant. The **angle** `θ` between `G` and `F` is
given by `cos θ = Cov_q(G, F) / (Var_q(G)·Var_q(F))^{1/2}`. Under the standard specification of `F`, as `s → 0`,
`M(p_s)/KL(p_s‖q) → sin²θ` if `cos θ ≥ 0`, and `→ 1` if `cos θ < 0`. If `cos θ < 0`, then `M(p_s) = KL(p_s‖q)` for every
small enough `s > 0`.

**In plain terms.** Whenever a behaviour starts to move away from the default, the share of its departure that is
misaligned is set by one angle: the angle between the objective its change reveals and the declared objective, whose
cosine is the correlation of the two under the default. Moving straight along the objective is no misalignment; moving
at a right angle to it is all misalignment, and so is moving against it.

**Proof.** Since the path is twice continuously differentiable with `p_0 = q`, `p_s = tilt(q, a_s)` with
`a_s = s·G + O(s²)`. Expanding the log-normalizer `Λ(c) = log E_q[e^c]` to second order gives
`KL(tilt(q, a)‖tilt(q, b)) = ½·Var_q(a − b) + O(‖a‖³ + ‖b‖³)` for small `a`, `b`, so
`KL(p_s‖q) = ½·s²·Var_q(G) + O(s³)`, which is positive for small `s > 0`. Let
`ψ(s) = E_{p_s}[F] − E_q[F] = s·Cov_q(G, F) + O(s²)`. If `cos θ < 0`, then `ψ(s) < 0` for small `s > 0`, and the first
case of [P5](iv) gives `M(p_s) = KL(p_s‖q)`. Otherwise, whenever `ψ(s) ≤ 0` the same case gives a share of `1`. When
`ψ(s) > 0`, it is also below `max F − E_q[F]` for small `s`, so the second case applies: `M(p_s) = KL(p_s‖p_{F,t*})`
with `E_{p_{F,t*}}[F] = E_{p_s}[F]`. Since `t ↦ E_{p_{F,t}}[F]` has derivative `Var_q(F) > 0` at `t = 0`, the inverse
function theorem gives `t* = ψ(s)/Var_q(F) + O(ψ(s)²) = s·ρ + O(s²)`, with `ρ = Cov_q(G, F)/Var_q(F)`. Then
`M(p_s) = ½·Var_q(s·G − t*·F) + O(s³) = ½·s²·Var_q(G − ρ·F) + O(s³)`, and
`Var_q(G − ρ·F) = Var_q(G) − Cov_q(G, F)²/Var_q(F) = Var_q(G)·sin²θ`. Dividing by `KL(p_s‖q)` gives `sin²θ` in the
limit. If `cos θ = 0`, then `ρ = 0` and `sin²θ = 1`, which agrees with the cases where `ψ(s) ≤ 0`.

**Checks.** checks/test_identifiability.py::test_initial_share_is_sin_squared

**Notes.** The angle needs only two things, both at the default: the first change of behaviour and the declared
objective. The actor's own objective is never needed. [P8](iv)'s small-effort law is the case `G = F̄`, where
`Cov_q(F̄, F) = Var_q(F̄)`. The curvature of the path does not affect the limit, and the convergence is first order in
`s` (the check uses curved paths).

**Lineage.** v7.10: ROADMAP §6 I1 and NOTES §9 (the dynamic angle, `D_⊥ ≈ sin²θ·KL`, conjectured there), and Prop 22
(the first-order effect of any smooth path). New: the statement and its proof, including the case against the objective.

### P12 — What interventions reveal
**Statement.** (i) **Pass-through is identified from behaviour alone.** Let `p, p' ∈ Δ°` be the behaviour before and
after an intervention `u`. The actor passes it through if and only if `log(p'/p) ∈ span{u, 1}`, and then the
pass-through is the coefficient of `u`. If `log(p'/p)` is not in `span{u, 1}`, no pass-through explains the change.
(ii) **Changes certify distinctions.** Let `𝒜` be a resolution and `s ↦ p_s` a continuously differentiable path in `Δ°`,
over an interval containing `0`. Every behaviour on the path splits each cell of `𝒜` in the same proportions as `p_0` if
and only if every revealed objective `F_s` is constant on the cells of `𝒜`. So a revealed objective that separates two
outcomes of one cell shows that their ratio moved; revealed objectives that never separate them do not show that the
actor cannot tell them apart.

**In plain terms.** Whether an actor simply follows an incentive can be read from its behaviour before and after,
without knowing what it wants: the change must be a multiple of the incentive, apart from a constant, and that multiple
is the pass-through. If the change has any other shape, something more than the incentive moved it: the incentive
changed what the actor pursues or where it starts from, or something else changed at the same time. Likewise, a change
that moves two outcomes apart proves that the actor treats them differently; changes that never do prove nothing.

**Proof.** (i) If `p' = tilt(p, φ·u)`, then `log(p'/p) = φ·u − log E_p[e^{φu}]`, which is in `span{u, 1}`. Conversely,
if `log(p'/p) = φ·u + c`, then `p'` is proportional to `p·e^{φu}`, and normalization gives `p' = tilt(p, φ·u)`. Since
`u` is non-constant, `u` and `1` are linearly independent, so `φ` is determined.
(ii) If `p_s(·|A) = p_0(·|A)` for every cell `A` and every `s`, then for `x ∈ A`,
`log p_s(x) = log p_s(A) + log p_0(x|A)`, so `F_s(x) = ∂_s log p_s(A)` is the same for every `x ∈ A`. Conversely, if
every `F_s` is constant on each cell, then for `x` and `y` in one cell, `∂_s log(p_s(x)/p_s(y)) = F_s(x) − F_s(y) = 0`,
so every ratio inside a cell keeps its value at `s = 0`, and so does the split. For the last sentence: the constant path
`p_s = p_0` has `F_s = 0` for every actor, including one that tells every outcome apart.

**Checks.** checks/test_identifiability.py::test_pass_through_is_identified_from_behaviour_alone,
checks/test_identifiability.py::test_revealed_objectives_certify_distinctions

**Notes.** (i) has no power with two outcomes: then `span{u, 1}` is every function, so every change passes the
intervention through, and an intervention that changed what the actor pursues shows only as a negative or a surprising
pass-through. Telling the two apart needs at least three outcomes, or several interventions. With estimated behaviours
the distance of `log(p'/p)` from `span{u, 1}` is never exactly zero; testing it needs an estimation item, which the core
does not have yet. (ii) bounds an actor's resolution from one side only. Observed changes show which distinctions its
behaviour makes; identifying its resolution needs interventions varied enough to move every distinction it could make.
Together with [P1], this is the ladder v7.10 proposed: a snapshot identifies an objective only given a declared default,
changes identify it up to a constant without one, and interventions identify how the actor responds.

**Lineage.** v7.10: ROADMAP §6 I1 (the identifiability ladder: declare, measure, identify through interventions), B1
(identifying an actor's partition), and T7-2d. New: both statements.

### P13 — What the start of a change gains
**Statement.** Let `F` be non-constant, and let `s ↦ p_s`, for `s ≥ 0`, be a continuously differentiable path in `Δ°`
with revealed objectives `F_s`.
(i) **The average moves at the covariance rate.** For every `s`, `d/ds E_{p_s}[F] = Cov_{p_s}(F_s, F)`.
(ii) **At the start, the gain is set by the angle.** Let the path be as in [P11], with angle `θ`, and let
`σ_q(F) = Var_q(F)^{1/2}`. As `s → 0`, `(E_{p_s}[F] − E_q[F]) / (2·KL(p_s‖q))^{1/2} → cos θ·σ_q(F)` and
`S(p_s) / (2·KL(p_s‖q))^{1/2} → (1 − cos θ)·σ_q(F)`, where `S` is the shortfall of [D5].

**In plain terms.** As behaviour changes, the average of any objective moves at a rate equal to the covariance, under
the current behaviour, between that objective and the objective the change reveals. At the start of a change away from
the default, each unit of departure gains the objective's spread times the cosine of the angle of [P11]. Pursuing the
objective itself, with the same departure, gains the full spread, so the shortfall is the rest: one minus the cosine,
times the spread. No change gains more per unit of departure at the start than pursuit of the objective, and a change
against the objective loses.

**Proof.** (i) By [P2], `∂_s p_s(x) = p_s(x)·F_s(x)`, so `d/ds E_{p_s}[F] = Σ_x p_s(x)·F_s(x)·F(x) = E_{p_s}[F_s·F]`.
Since `Σ_x p_s(x) = 1` for every `s`, `E_{p_s}[F_s] = Σ_x ∂_s p_s(x) = 0`, so `E_{p_s}[F_s·F] = Cov_{p_s}(F_s, F)`.
(ii) Write `G = F_0` and `ε(s) = (2·KL(p_s‖q))^{1/2}`. The proof of [P11] gives `KL(p_s‖q) = ½·s²·Var_q(G) + O(s³)`, so
`ε(s) = s·σ_q(G)·(1 + O(s))`. By (i) and Taylor's theorem, `E_{p_s}[F] − E_q[F] = s·Cov_q(G, F) + O(s²)`. Dividing, the
first ratio tends to `Cov_q(G, F)/σ_q(G) = cos θ·σ_q(F)`. For the shortfall, let `A` be the set where `F` is largest.
Along the ray, `d(t) = KL(p_{F,t}‖q) = t·E_{p_{F,t}}[F] − log E_q[e^{tF}]` is continuous and `0` at `t = 0`. The ray's
revealed objective is `F − E_{p_{F,t}}[F]`, so (i) gives `d/dt E_{p_{F,t}}[F] = Var_{p_{F,t}}(F)`, and
`d'(t) = t·Var_{p_{F,t}}(F) > 0` for `t > 0`: `d` is increasing. Its limit as `t → ∞` is `KL(q(·|A)‖q) = −log q(A) > 0`,
since `F` is non-constant. So for small `s`, the matched intensity `λ` of [D5] is finite, `d(λ) = KL(p_s‖q)`, and
`λ → 0` as `s → 0`. The same second-order expansion applied to the ray gives `d(λ) = ½·λ²·Var_q(F) + O(λ³)`, so
`λ·σ_q(F) = ε(s)·(1 + O(λ))`, and `λ = O(s)`. By (i) on the ray,
`E_{p_{F,λ}}[F] − E_q[F] = λ·Var_q(F) + O(λ²) = ε(s)·σ_q(F) + O(s²)`. Subtracting the actual gain,
`S(p_s) = ε(s)·σ_q(F)·(1 − cos θ) + O(s²)`, and dividing by `ε(s)` gives the second limit.

**Checks.** checks/test_identifiability.py::test_average_moves_at_the_covariance_rate,
checks/test_identifiability.py::test_start_gains_cos_theta_of_the_spread

**Notes.** (i) is the Price equation [@price1970] in continuous time without its transmission term, with `F_s` in the
role of Malthusian fitness: it holds at every `s`, for any path, with no default. Along any path, the average of `F` is
stationary exactly where `Cov_{p_s}(F_s, F) = 0`. So when an actor pursues a proxy, the average of the objective peaks
only where the proxy and the objective are uncorrelated under the actor's current behaviour. (ii) is a law in the
square root of the departure, with a finite slope at zero departure, bounded by `σ_q(F)` for every smooth path, since
`|cos θ| ≤ 1`. Together with [P11]: at the start of a change, `sin²θ` of the departure is misaligned, and `1 − cos θ` of
the attainable gain is lost.

**Lineage.** v7.10: B §4 (for a jointly Gaussian target and evaluator, the gold gain along the Gibbs path is exactly
`√2·ρ_q(F, F̂)·sd_q(F)` times `√KL`, which (ii) generalizes to the first order of any smooth path), Prop 14 and Prop 22
(the initial effect has the sign of the covariance), ROADMAP §6 I1 (the dynamic angle) and Def 22 (the value shortfall).
New: (i) as a statement about any path, and the shortfall in (ii). The v9 restart first credited none of the first
three, which `NOTES.md` §1 records as a failure mode.

### P16 — An actor cannot behave more differently than it can tell conditions apart
**Statement.** Let the actor's response depend on the condition only through a view `(Z, V)` ([D8]), and let `c` and
`c'` be conditions.
(i) If `V_c = V_{c'}`, then `p_c = p_{c'}`.
(ii) `KL(p_c‖p_{c'}) ≤ KL(V_c‖V_{c'})`.
(iii) If the view depends on the condition only through an input, that is, there are finitely many inputs `w`, with
distribution `W_c` in condition `c`, and distributions `K_w` on `Z` with `V_c = Σ_w W_c(w)·K_w`, then
`KL(V_c‖V_{c'}) ≤ KL(W_c‖W_{c'})`.

**In plain terms.** An actor that perceives two situations alike acts alike in them. More generally, how differently it
can act in two situations is bounded by how well it can tell them apart, and it cannot tell them apart better than what
it receives in them differs.

**Proof.** (i) `p_c = Σ_z V_c(z)·π_z` depends on `c` only through `V_c`. (ii) If some `z` has `V_c(z) > 0 = V_{c'}(z)`,
the right side is infinite. Otherwise, for each outcome `x`, the log-sum inequality applied to the numbers
`V_c(z)·π_z(x)` and `V_{c'}(z)·π_z(x)` gives `p_c(x)·log(p_c(x)/p_{c'}(x)) ≤ Σ_z V_c(z)·π_z(x)·log(V_c(z)/V_{c'}(z))`,
with the terms where `V_c(z)·π_z(x) = 0` left out. Summing over `x`, and using `Σ_x π_z(x) = 1`, gives (ii). (iii) is
(ii) with the inputs in the place of the signals and the distributions `K_w` in the place of the behaviours `π_z`.

**Checks.** checks/test_identifiability.py::test_identical_views_give_identical_behaviour,
checks/test_identifiability.py::test_behaviour_differs_no_more_than_views

**Notes.** (ii) and (iii) are the data-processing inequality [@cover2006]. (iii) matters in practice: the principal can
bound how well the actor tells two conditions apart from what the actor receives in them, without knowing anything
about the actor. The bound holds only for a view that includes everything the actor uses. Memory across episodes,
timestamps and side channels are inputs too, and an input left out of `W` can make the bound false.

**Lineage.** New. v7.10: ROADMAP §6 I1 (identification through interventions).

### P17 — What an unobserved condition can hide
**Statement.** Let the actor's response depend on the condition only through a view ([D8]). Let `a` be an observed
condition ([D9]) with `p_a ∈ Δ°`, let `d` be a condition that is not observed, and let `ε = KL(V_d‖V_a)` be finite. Let
`F` be non-constant, with `A₊` and `A₋` the sets of outcomes where it is largest and smallest.
(i) `KL(p_d‖p_a) ≤ ε`.
(ii) `E_{p_d}[F] ≤ E_{tilt(p_a, λ₊·F)}[F]`, where `λ₊ ≥ 0` is the intensity at which `tilt(p_a, λ·F)` departs from `p_a`
by exactly `ε`; when `ε ≥ −log p_a(A₊)` the bound is `max F`. Likewise `E_{p_d}[F] ≥ E_{tilt(p_a, −λ₋·F)}[F]`, or
`min F` when `ε ≥ −log p_a(A₋)`.
(iii) The lower bound of (ii) is attained: for every `p_a ∈ Δ°` and `λ ≥ 0`, some view and some response through it
have the observed behaviour `p_a`, `ε = KL(tilt(p_a, −λ·F)‖p_a)`, and `E_{p_d}[F] = E_{tilt(p_a, −λ·F)}[F]`. So, from
`ε` alone, (ii) cannot be improved.
(iv) If `ε = 0`, then `p_d = p_a`: the behaviour in `d`, and every quantity defined from it, such as its misalignment
and its shortfall, is identified ([D9]).

**In plain terms.** An actor watched in one situation and not in another can behave differently in the second only as
far as it can tell the two apart. How much of the objective it can lose there is at most what the most direct move
against the objective loses, at that distance from its watched behaviour, and some actor loses exactly that much. An
actor that cannot tell the two situations apart behaves the same in both, so what was watched is what happens.

**Proof.** (i) is [P16](ii). (ii) Take `p_a` in the role of the default, and write `p_λ = tilt(p_a, λ·F)`. By [P4](i),
for every `p` and every `λ > 0`, `E_p[F] − E_{p_λ}[F] = (KL(p‖p_a) − KL(p_λ‖p_a))/λ − KL(p‖p_λ)/λ`. As in the proof of
[P9](i), the departure `KL(p_λ‖p_a)` increases continuously from `0` toward `−log p_a(A₊)` as `λ` grows. If `ε` is below
that limit, `λ₊` exists, and for `p = p_d`, (i) gives `KL(p_d‖p_a) ≤ ε = KL(p_{λ₊}‖p_a)`, so
`E_{p_d}[F] ≤ E_{p_{λ₊}}[F]`. Otherwise the bound `max F` holds for every behaviour. The lower bound is the same
argument for `−F`. (iii) Take `Z = X`, `V_a = p_a`, `V_d = tilt(p_a, −λ·F)`, and `π_z` the behaviour that puts all its
mass on `z`. Then `p_c = V_c` in both conditions, so `ε = KL(V_d‖V_a)` is the departure of `tilt(p_a, −λ·F)`, whose
average of `F` is the lower bound with `λ₋ = λ`. (iv) `ε = 0` means `V_d = V_a`, and [P16](i) applies.

**Checks.** checks/test_identifiability.py::test_what_an_unobserved_condition_can_hide

**Notes.** In the core's terms, an actor is deceptively aligned when its misalignment in conditions that are not
observed exceeds its misalignment in those that are. This result says what that needs and what it can cost. It needs a
view that separates the conditions ((iv) and [P16](i)). And what it can cost in the objective is bounded, sharply given
`ε`, by the matched pursuit of `−F` from the observed behaviour: [P9]'s comparison, with the observed behaviour as the
default. With [P16](iii), it gives the principal a design rule: observe in conditions whose inputs the actor cannot tell
from those of the unobserved ones, such as audits drawn from real use and indistinguishable from it, and the behaviour
in the unobserved conditions is identified. The bound uses KL only. Every other `f`-divergence obeys the same
data-processing inequality, so the identified set can be narrower than (ii) states; (ii) is an outer bound that some
actor attains. The misalignment in `d` is at most the largest misalignment within `ε` of `p_a`, a maximization that has
no closed form in general.

**Lineage.** New, on the PI's request to make deceptive alignment measurable. v7.10: none.

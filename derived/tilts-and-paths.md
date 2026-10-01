# Derived — tilts and paths

Every full-support behaviour is a tilt of any other, so describing behaviour as a reweighted default loses
nothing ([P1]). Every change of behaviour follows a replicator equation, which is the steepest climb of [A2] ([P2]).
Whether a change keeps one objective can be read from the change alone ([P3]).

### P1 — Every behaviour is a tilt of any other
**Statement.** Let `r ∈ Δ°`.
(i) For every `p ∈ Δ°`, `p = tilt(r, log(p/r))`.
(ii) `tilt(r, F) = tilt(r, G)` if and only if `F − G` is constant.
(iii) `tilt(tilt(r, F), G) = tilt(r, F + G)`, and `tilt(r, 0) = r`.

**In plain terms.** Any full-support behaviour can be written as any other full-support behaviour reweighted by some
function, and that function is fixed except for adding a constant. Reweightings add up. So describing a behaviour as
"the default, reweighted toward an objective" is always possible, and loses nothing.

**Proof.** (i) `r·e^{log(p/r)} = p`, which already sums to 1. (ii) If `F − G = c`, the factor `e^c` cancels in the
normalization. Conversely, if the tilts are equal, then `F − log E_r[e^F] = G − log E_r[e^G]` at every outcome, so
`F − G` is constant. (iii) `tilt(tilt(r, F), G)` is proportional to `r·e^F·e^G`, and both sides are normalized;
`e^0 = 1`.

**Checks.** checks/test_tilts.py::test_every_behaviour_is_a_tilt,
checks/test_tilts.py::test_tilt_objective_unique_up_to_constant,
checks/test_tilts.py::test_tilts_compose

**Notes.** `log(p/r)` is the log-likelihood ratio of `p` to `r`. Recovering an objective from behaviour is the problem
of
inverse reinforcement learning, which is known to be ill-posed [@ng2000]; (ii) is the form the ambiguity takes here:
given the default, a behaviour reveals its objective up to a constant. Written with an intensity, `tilt(r, t·F)`, it
reveals only the product `t·F`.

**Lineage.** New as a statement. main used the tilt as the form of intended behaviour (Def 1), and recorded "everything
is a tilt" as an insight (NOTES §2.1) without stating it. The freedom in (ii) is main's Prop 16 (g2), and the product
`t·F` is main's Prop 12.

### P2 — Every change of behaviour follows a replicator equation
**Statement.** Let `s ↦ p_s` be a continuously differentiable path in `Δ°`, over an interval containing `0`, and let
`F_s = ∂_s log p_s`, the **revealed objective** at time `s`.
(i) **Replicator form.** `ṗ_s = p_s·(F_s − E_{p_s}[F_s])`. A function `G` satisfies `ṗ_s = p_s·(G − E_{p_s}[G])` if
and only if `G − F_s` is constant.
(ii) **Steepest climb.** Give `Δ°` the Fisher metric `g_p(u, v) = Σ_x u(x)·v(x)/p(x)` on tangent vectors, those with
`Σ_x u(x) = 0`. For every `F : X → ℝ`, the field `p·(F − E_p[F])` is the gradient of `p ↦ E_p[F]`. If `F` is not
constant, then among tangent directions of unit length it is the one along which `E_p[F]` rises fastest.
(iii) **The flow of a fixed objective.** For every `r ∈ Δ°` and `F : X → ℝ`, the path `s ↦ tilt(r, s·F)`, for `s ∈ ℝ`,
is the unique solution of `ṗ = p·(F − E_p[F])` with `p_0 = r`.

**In plain terms.** Any change of behaviour over time can be described as climbing an objective that may itself change
over time, and that objective can be read off the change, except for a constant. When distances between behaviours are
measured the way statistics measures them, this form of change is the steepest possible climb of the objective's
average. Climbing a fixed objective this way from a starting behaviour is exactly reweighting that behaviour by the
objective, more and more strongly.

**Proof.** (i) Differentiating `Σ_x p_s(x) = 1` gives `E_{p_s}[F_s] = Σ_x ṗ_s(x) = 0`, so
`p_s·(F_s − E_{p_s}[F_s]) = p_s·∂_s log p_s = ṗ_s`. If `G` satisfies the equation, then
`G − E_{p_s}[G] = ṗ_s/p_s = F_s`, so `G − F_s` is constant. Conversely, a constant cancels in `G − E_{p_s}[G]`.
(ii) The derivative of `f(p) = E_p[F]` along a tangent vector `u` is `Σ_x F(x)·u(x)`. The field `v = p·(F − E_p[F])`
is tangent, because it sums to `0`, and `g_p(v, u) = Σ_x (F(x) − E_p[F])·u(x) = Σ_x F(x)·u(x)` for every tangent `u`.
So `v` is the gradient of `f`. If `F` is not constant, then `v ≠ 0`, and for `g_p(u, u) = 1` Cauchy–Schwarz gives
`Σ_x F(x)·u(x) = g_p(v, u) ≤ g_p(v, v)^{1/2}`, with equality at `u = v / g_p(v, v)^{1/2}`.
(iii) `log tilt(r, s·F) = log r + s·F − log E_r[e^{sF}]`, so `∂_s log tilt(r, s·F) = F − c(s)` for a number `c(s)`, and
by (i) the path satisfies the equation; it starts at `r`. The field `p·(F − E_p[F])` is a polynomial in `p`, hence
locally Lipschitz on `Δ°`, so the solution through `r` is unique.

**Checks.** checks/test_paths.py::test_replicator_form_of_any_path,
checks/test_paths.py::test_replicator_is_fisher_gradient,
checks/test_paths.py::test_pursuit_ray_solves_the_replicator_flow

**Notes.** "Revealed" is meant as in revealed preference: read from behaviour, not assumed about the actor. In
population genetics the revealed objective is the Malthusian fitness of each type (its per-capita growth rate), up to a
constant, and the replicator equation is the gradient of mean fitness in this metric, known there as the Shahshahani
metric [@shahshahani1979].

**Lineage.** New as a proposition. main: NOTES §2.1 ("everything is a tilt") and ROADMAP §6 I1 (dynamics: increments
cancel the default).

### P3 — A fixed objective is visible in the changes of behaviour
**Statement.** Let `s ↦ p_s` be a continuously differentiable path in `Δ°`, over an interval containing `0`, with
revealed objective `F_s = ∂_s log p_s`, and let `F` be non-constant.
(i) There is a differentiable `τ` with `τ(0) = 0` and `p_s = tilt(p_0, τ(s)·F)` for every `s` if and only if
`F_s ∈ span{F, 1}` for every `s`. Then `F_s = τ'(s)·F + c(s)`.
(ii) The path pursues `F` ([D2]) if and only if, for every `s`, `F_s = a(s)·F + b(s)` with `a(s) ≥ 0`.

**In plain terms.** Whether a changing behaviour keeps one fixed objective can be read from its changes alone: every
change must point along that objective, apart from a constant. It pursues the objective when it never moves against it.
Two changes that point in opposite directions lie on one line, but they are not one pursuit.

**Proof.** (i) If `p_s = tilt(p_0, τ(s)·F)`, then `log p_s = log p_0 + τ(s)·F − log E_{p_0}[e^{τ(s)F}]`, so
`F_s = τ'(s)·F + c(s)`, with `c(s)` minus the derivative of the log-normalizer. Conversely, let `F_s = a(s)·F + b(s)`
for
every `s`. Since `F` is not constant, `F` and `1` are linearly independent, so `a` and `b` are determined by `F_s`, and
they are continuous because the path is continuously differentiable. Integrating from `0` gives
`log p_s = log p_0 + τ(s)·F + B(s)`, with `τ(s) = ∫_0^s a` and `B(s) = ∫_0^s b`, and normalization gives
`p_s = tilt(p_0, τ(s)·F)`.
(ii) By (i), the path has the form of [D2] exactly when `F_s = a(s)·F + b(s)`, and then `τ' = a`. So `τ` is
non-decreasing if and only if `a` is never negative.

**Checks.** checks/test_paths.py::test_fixed_objective_iff_span,
checks/test_paths.py::test_two_outcomes_always_keep_a_fixed_objective

**Notes.** The condition `F_s ∈ span{F, 1}` is the precise form of "the increments have rank 1", which [P12] uses for
interventions. The sign condition in (ii) is what a rank read on lines, not on rays, misses. With only two
outcomes, `span{F, 1}` contains every function, so every path keeps a fixed objective: the test has content only with
three or more outcomes. (On main, this is why a two-arrangement allele-frequency series could not test the rank.) In
population genetics a fixed objective is constant selection, and a turning one is fluctuating selection; in economics
the question is whether preferences are stable.

**Lineage.** New as a proposition. main: ROADMAP §6 I1 (the dynamic rank), and the I1-dyn and I1-dyn2 tests, whose null
hypothesis counted opposite-pointing increments as one evaluator.

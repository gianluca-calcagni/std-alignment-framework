# The core

> **Status: v8, in progress.** Sections 1–3: behaviours, pursuit, and the declaration. Each item carries a formal
> statement and a plain-terms twin. A definition says why this choice; a result carries a proof and checks that run in
> CI. Every item gives its lineage from the archive on `main`. The format is in `README.md`.

**How to read.** Items are numbered by kind: D for definitions, P for propositions. A statement, justification or proof uses only items above it.
`[P2](iii)` means part (iii) of P2. Logarithms are natural, so divergences are in nats.

## 1. Behaviours and tilts

### D1 — Outcomes, behaviours, divergence and tilt
**Statement.** `X` is a finite set of **outcomes**, with at least two elements. A **behaviour** is a probability
distribution `p` on `X`. `Δ` is the set of behaviours, and `Δ°` the set of **full-support** behaviours, those with
`p(x) > 0` for every `x`. For `p ∈ Δ` and `r ∈ Δ°`, the **Kullback–Leibler divergence** is
`KL(p‖r) = Σ_x p(x)·log(p(x)/r(x))`, with `0·log 0 = 0`. The **tilt** of `r ∈ Δ°` by a function `F : X → ℝ` is the
behaviour `tilt(r, F) = r·e^F / E_r[e^F]`.

**In plain terms.** Outcomes are the things that can happen, and a behaviour says how often each one happens; full
support means that nothing is ruled out entirely. KL measures how different one behaviour is from another. Tilting
reweights a behaviour toward the outcomes that a function scores higher.

**Why this choice.**
- *Finite outcomes.* Every statement can then be proved with finite sums and checked exactly on random instances.
  General outcome spaces change the statements only by conditions of absolute continuity. They come back when an item
  needs them.
- *Full support.* It keeps every logarithm finite. A behaviour that rules an outcome out is a limit of full-support
  ones, and is allowed as the first argument of KL.
- *Behaviour is any distribution.* No model of how an actor produces its behaviour is assumed. The core measures
  behaviour; explanations are not part of it.
- *KL and the tilt are notation here.* The items that use them argue that they are the right tools.

**Lineage.** main: Def 1 (the objects), and R7-1's rule that the actual behaviour is any distribution (Def 13). main's
R7-8 (measurable spaces) stays deferred, as it was there.

### P1 — Every behaviour is a tilt of any other
**Statement.** Let `r ∈ Δ°`.
(i) For every `p ∈ Δ°`, `p = tilt(r, log(p/r))`.
(ii) `tilt(r, F) = tilt(r, G)` if and only if `F − G` is constant.
(iii) `tilt(tilt(r, F), G) = tilt(r, F + G)`, and `tilt(r, 0) = r`.

**In plain terms.** Any full-support behaviour can be written as any other full-support behaviour reweighted by some
function, and that function is fixed except for adding a constant. Reweightings add up. So describing a behaviour as
"the default, tilted by an objective" is always possible, and loses nothing.

**Proof.** (i) `r·e^{log(p/r)} = p`, which already sums to 1. (ii) If `F − G = c`, the factor `e^c` cancels in the
normalization. Conversely, if the tilts are equal, then `F − log E_r[e^F] = G − log E_r[e^G]` at every outcome, so
`F − G` is constant. (iii) `tilt(tilt(r, F), G)` is proportional to `r·e^F·e^G`, and both sides are normalized;
`e^0 = 1`.

**Checks.** checks/test_tilts.py::test_every_behaviour_is_a_tilt, checks/test_tilts.py::test_tilt_objective_unique_up_to_constant,
checks/test_tilts.py::test_tilts_compose

**Lineage.** New as a statement. main used the tilt as the form of intended behaviour (Def 1), and recorded "everything
is a tilt" as an insight (NOTES §2.1) without stating it. The freedom in (ii) is main's Prop 16 (g2).

### P2 — Every change of behaviour is a pursuit with a moving objective
**Statement.** Let `t ↦ p_t` be a continuously differentiable path in `Δ°` over an interval containing `0`, and let
`F_t = ∂_t log p_t`.
(i) **Replicator form.** `ṗ_t = p_t·(F_t − E_{p_t}[F_t])`. A function `G` satisfies `ṗ_t = p_t·(G − E_{p_t}[G])` if
and only if `G − F_t` is constant.
(ii) **Fixed objective.** Let `F` be non-constant. There is a differentiable `τ` with `τ(0) = 0` and
`p_t = tilt(p_0, τ(t)·F)` for every `t` if and only if `F_t ∈ span{F, 1}` for every `t`. Then `F_t = τ'(t)·F + c(t)`,
so `τ` is non-decreasing (the path **pursues** `F`) if and only if the coefficient of `F` in `F_t` is never negative.
(iii) **Steepest climb.** Give `Δ°` the Fisher metric `g_p(u, v) = Σ_x u(x)·v(x)/p(x)` on tangent vectors
(`Σ_x u(x) = Σ_x v(x) = 0`). For a fixed `F`, the field `p·(F − E_p[F])` is the gradient of `p ↦ E_p[F]`. Among
tangent directions of unit length, it is the one along which `E_p[F]` rises fastest.

**In plain terms.** Any change of behaviour over time can be described as pursuing an objective that may itself change
over time, and that objective can be read off the change, except for a constant. The objective stays the same exactly
when every change points along one fixed direction, apart from constants, and the path pursues it when it never moves
against it. Pursuing a fixed objective in this way is the steepest possible climb of its average, when distances
between behaviours are measured the way statistics measures them.

**Proof.** (i) Differentiating `Σ_x p_t(x) = 1` gives `E_{p_t}[F_t] = Σ_x ṗ_t(x) = 0`, so
`p_t·(F_t − E_{p_t}[F_t]) = p_t·∂_t log p_t = ṗ_t`. If `G` satisfies the equation, then `G − E_{p_t}[G] = ṗ_t/p_t = F_t`,
so `G − F_t` is constant. Conversely, a constant cancels in `G − E_{p_t}[G]`.
(ii) If `p_t = tilt(p_0, τ(t)·F)`, then `log p_t = log p_0 + τ(t)·F − log E_{p_0}[e^{τ(t)F}]`, so `F_t = τ'(t)·F + c(t)`,
with `c(t)` minus the derivative of the log-normalizer. Conversely, let `F_t = a(t)·F + b(t)` for every `t`. Since `F` is
non-constant, `F` and `1` are linearly independent, so `a` and `b` are determined by `F_t`, and they are continuous
because the path is continuously differentiable. Integrating from `0` gives `log p_t = log p_0 + τ(t)·F + B(t)`, with
`τ(t) = ∫_0^t a` and `B(t) = ∫_0^t b`. Normalization then gives `p_t = tilt(p_0, τ(t)·F)`. Since `τ' = a`, `τ` is
non-decreasing if and only if `a` is never negative.
(iii) The derivative of `f(p) = E_p[F]` along a tangent vector `u` is `Σ_x F(x)·u(x)`. The field
`v = p·(F − E_p[F])` is tangent, because it sums to `0`, and `g_p(v, u) = Σ_x (F(x) − E_p[F])·u(x) = Σ_x F(x)·u(x)` for
every tangent `u`. So `v` is the gradient of `f`. For `g_p(u, u) = 1`, Cauchy–Schwarz gives
`Σ_x F(x)·u(x) = g_p(v, u) ≤ g_p(v, v)^{1/2}`, with equality at `u = v / g_p(v, v)^{1/2}`.

**Checks.** checks/test_paths.py::test_replicator_form_of_any_path, checks/test_paths.py::test_fixed_objective_iff_span,
checks/test_paths.py::test_replicator_is_fisher_gradient

**Notes.** In population genetics the replicator equation is the gradient of mean fitness in this metric, known there as
the Shahshahani metric [@shahshahani1979]. The condition `F_t ∈ span{F, 1}` in (ii) is the precise form of "the
increments have rank 1", which later items use for identifiability. The sign condition says what a line-based rank
misses: two opposite-pointing increments lie on one line, but they are not one pursuit.

**Lineage.** New as a proposition. main: ROADMAP §6 I1 (dynamics: increments cancel the reference; the dynamic rank),
and the I1-dyn and I1-dyn2 tests, whose null hypothesis counted opposite-pointing increments as one evaluator.

## 2. Pursuit, and what KL measures

### D2 — Pursuit of an objective
**Statement.** Let `q ∈ Δ°`, the **reference**, and let `F : X → ℝ` be a function, an **objective**. The **pursuit** of
`F` from `q` at **intensity** `t ≥ 0` is `p_{F,t} = tilt(q, t·F)`. The **pursuit ray** of `F` from `q` is
`R_F = {p_{F,t} : t ≥ 0}`. For a constant `F`, the ray is the single point `q`.

**In plain terms.** Pursuing an objective means reweighting the default behaviour toward the outcomes that the objective
scores higher, and the intensity says how strongly. Intensity zero is the default itself, and the pursuit ray collects
every intensity.

**Why this choice.**
- *It loses no generality.* Every full-support behaviour `p` lies on the pursuit ray of some objective from any
  reference: `p = p_{F,1}` with `F = log(p/q)` ([P1](i)). Every path of behaviours is a pursuit with a moving objective
  ([P2](i)). What the definition adds is a claim that can fail, namely that the objective stays fixed, and [P2](ii) makes
  that claim testable. Other ways of reweighting a behaviour (mixing it with another, keeping the best of `n` samples,
  cutting off below a threshold) are paths too, and [P2](ii) says whether they keep a fixed objective.
- *It is canonical.* The ray is the steepest climb of `E_p[F]` in the Fisher metric, started at `q`: by [P2](iii) that
  climb follows `ṗ = p·(F − E_p[F])`, and by [P2](ii) its solution is `tilt(q, t·F)`. Up to a constant factor, the
  Fisher metric is the only choice of metric, across outcome spaces of every size, that is unchanged when outcomes are
  split into sub-outcomes in fixed proportions (Čencov's theorem [@cencov1982]; [@campbell1986]). So a notion of
  pursuit that must not depend on how finely the outcomes are described is led to this ray.
- *The reference is part of it.* The same objective pursued from two references gives two different rays. Who fixes the
  reference, and when, is settled by the declaration below.

**Lineage.** main: Def 1 (the Gibbs tilt `p_{G,t}`), Def 2 (the bounded actor, whose optimum is the tilt: here a
property, [P3](i)), Prop 15 (the carrier), and Prop 16 (g4) (the half-ray). The ray defines intended pursuit; it is not a
model of the actor. main's rows 67–68 and 76–78 filed results by the intended actor's model instead of by what their
proofs need, and the core keeps the two apart by construction.

### P3 — What KL measures
**Statement.** Let `q ∈ Δ°`, `F : X → ℝ` and `t > 0`, and let `J_t(p) = E_p[F] − KL(p‖q)/t` for `p ∈ Δ`.
(i) **Value.** For every `p ∈ Δ`, `J_t(p_{F,t}) − J_t(p) = KL(p‖p_{F,t})/t`. So `p_{F,t}` is the unique maximizer of
`J_t`.
(ii) **Every behaviour is an optimum.** For every `r ∈ Δ°`, `r = p_{F_r,t}` with `F_r = log(r/q)/t`. So `r` is the unique
maximizer of `J_t` for the objective `F_r`, and `KL(p‖r)` is `t` times the value that any `p ∈ Δ` loses against it.
(iii) **Chain rule.** For every partition `𝒢` of `X`, every `p ∈ Δ` and every `r ∈ Δ°`,
`KL(p‖r) = KL(p_𝒢‖r_𝒢) + Σ_{C ∈ 𝒢, p(C) > 0} p(C)·KL(p(·|C)‖r(·|C))`, where `p_𝒢` is the distribution of the cell
masses `p(C)`.
(iv) **Merging never increases it.** `KL(p_𝒢‖r_𝒢) ≤ KL(p‖r)`, with equality if and only if `p/r` is constant on every
cell `C` with `p(C) > 0`.

**In plain terms.** KL from an actual behaviour to an intended one is exactly the value the actual behaviour gives up,
in the objective the intended behaviour optimizes, multiplied by its intensity. Every full-support intended behaviour
optimizes some objective, so this reading always applies. KL splits into a part between groups and a part within
groups when outcomes are grouped, and grouping outcomes can only hide differences, never create them.

**Proof.** (i) With `Z = E_q[e^{tF}]`, `log p_{F,t} = log q + t·F − log Z`, so for every `p ∈ Δ`,
`KL(p‖p_{F,t}) = KL(p‖q) − t·E_p[F] + log Z = log Z − t·J_t(p)`. Hence `J_t(p) = (log Z − KL(p‖p_{F,t}))/t`. Taking the
difference at `p_{F,t}`, where the KL is `0`, and at `p` gives the identity. KL is non-negative, and zero only between
equal behaviours (Gibbs' inequality), so the maximizer is unique.
(ii) `tilt(q, t·F_r) = tilt(q, log(r/q)) = r` by [P1](i). Then apply (i).
(iii) For `x ∈ C` with `p(x) > 0`, `log(p(x)/r(x)) = log(p(C)/r(C)) + log(p(x|C)/r(x|C))`. Averaging over `p` gives the
identity.
(iv) By (iii), the difference is `Σ_C p(C)·KL(p(·|C)‖r(·|C)) ≥ 0`. It is zero if and only if `p(·|C) = r(·|C)` on every
cell with `p(C) > 0`, that is, if and only if `p/r` is constant there.

**Checks.** checks/test_value.py::test_value_identity, checks/test_value.py::test_every_behaviour_is_an_optimum,
checks/test_value.py::test_chain_rule, checks/test_value.py::test_merging_never_increases,
checks/test_value.py::test_other_divergences_break_the_chain_rule

**Notes.** (i) is the Gibbs variational principle. The chain rule and Gibbs' inequality are standard [@cover2006]. Hobson
characterized KL, up to a positive factor, by a small set of conditions that includes the chain rule (iii)
[@hobson1969]. The last check confirms that three common alternatives (χ², squared Hellinger, total variation) break
it.

**Lineage.** main: Thm 1 (regret is a divergence) for (i); Def 21 (the within-cell divergence) for (iii) and (iv). New:
(ii), which follows from [P1] and removes the need to assume that intended behaviour is "Gibbs", since every
full-support behaviour is. main's Prop 15 (other regularizers) is not carried: the score is KL.

## 3. The declaration and misalignment

### D3 — Declaration and misalignment
**Statement.** A **declaration** is a pair `(q, 𝓘)`, fixed before, and without using, the behaviour it will judge: a
reference `q ∈ Δ°`, and a non-empty set `𝓘 ⊆ Δ°` of **intended behaviours**, closed in `Δ°`. The **misalignment** of a
behaviour `p̂ ∈ Δ°` is `M(p̂) = inf_{p ∈ 𝓘} KL(p̂‖p)`. The **standard declaration** of an objective `F` is `(q, R_F)`:
pursuit of `F` from `q` at every intensity, including none.

**In plain terms.** Before looking at what the actor does, the principal states a default behaviour and the set of
behaviours it would accept. Misalignment is how far the actual behaviour is from the nearest acceptable one, in nats.
When the request is "pursue this objective", every intensity of pursuing it is acceptable, including doing nothing.

**Why this choice.**
- *Declared before, not fitted after.* A reference or an intended set fitted from the behaviour being judged removes
  exactly the differences the judgement needs. On main, I1-dyn fitted a Hardy–Weinberg reference from the counts it
  judged, and its test could not fail.
- *A set, not a point.* A principal who asks for `F` without naming an intensity would otherwise charge the actor for an
  intensity it never asked about (main: row 74, the price measure is a regret, not misalignment). A single intended
  behaviour is the case `𝓘 = {p*}`.
- *KL, with the actual behaviour first.* By [P3](ii), each intended behaviour is the optimum of its own objective, and
  `KL(p̂‖p)` is exactly the value `p̂` loses against `p`, multiplied by the intensity. So `M(p̂)` is the smallest value
  lost against any acceptable behaviour, each judged by its own objective, and that identity fixes the order of the
  arguments. By [P3](iii) and (iv), the score splits along groupings of outcomes, and grouping can only hide
  misalignment. Later items use this for resolutions.
- *The standard declaration is the pursuit ray,* because "pursue `F`" states a fixed objective ([D2]) at an unstated
  intensity. It includes doing nothing. A principal for whom doing nothing is a failure declares a smaller set (main:
  the floor, Def 20).
- *Slim on purpose.* main's declaration (Def 23) had nine slots. Only four changed the measure, and all four are ways
  of generating `𝓘`. Rules, instruments, feasibility and the environment did not enter the measure, so they are not
  declared here; instruments return with identifiability, as interventions. A later item adds a slot only with a case
  where the slot changes a verdict, and with its default.

**Lineage.** main: Def 19 and Prop 34 (the declared intended set), Def 17 (the free convention's half-ray), Def 23 (the
declaration, slimmed; its timing slot becomes the condition "fixed before, and without using"), and row 74.

### P4 — Misalignment is attained, and zero exactly on the intended set
**Statement.** Let `(q, 𝓘)` be a declaration and `p̂ ∈ Δ°`.
(i) The infimum in `M(p̂)` is attained: some `p ∈ 𝓘` has `KL(p̂‖p) = M(p̂)`.
(ii) `M(p̂) = 0` if and only if `p̂ ∈ 𝓘`.
(iii) If `q ∈ 𝓘`, then `M(p̂) ≤ KL(p̂‖q)`.
(iv) Let `F` be non-constant. The pursuit ray `R_F` is closed in `Δ°`, so `(q, R_F)` is a declaration. Under it,
`M(p̂) = KL(p̂‖p_{F,t*})`, where `t* = 0` if `E_{p̂}[F] ≤ E_q[F]`, and otherwise `t*` is the unique `t > 0` with
`E_{p_{F,t}}[F] = E_{p̂}[F]`.

**In plain terms.** There is always a nearest acceptable behaviour, and misalignment is zero only when the actual
behaviour is itself acceptable. When the default is acceptable, misalignment is never more than the actual behaviour's
departure from the default. The pursuit ray is a valid set of intended behaviours, and for "pursue `F`" the nearest
acceptable behaviour is the pursuit that reaches the same average of `F` as the actual behaviour, or the default itself
when the actual behaviour reaches less than the default.

**Proof.** (i) Pick `p₀ ∈ 𝓘` and let `c = KL(p̂‖p₀)` and `H(p̂) = −Σ_x p̂(x)·log p̂(x)`. For any `p ∈ Δ°`,
`KL(p̂‖p) = −H(p̂) − Σ_y p̂(y)·log p(y)`, and every term `−p̂(y)·log p(y)` is non-negative. So `KL(p̂‖p) ≤ c` implies
`p(x) ≥ exp(−(c + H(p̂))/p̂(x)) > 0` for every `x`. The set `K = {p ∈ Δ : KL(p̂‖p) ≤ c}` is closed in `Δ`, because
`KL(p̂‖·)` is lower semicontinuous on `Δ` (with value `+∞` where some `p(x) = 0`). So `K` is compact, and by the bound it
lies in `Δ°`. Since `𝓘` is closed in `Δ°`, the set `𝓘 ∩ K` is closed in `K`, hence compact, and it contains `p₀`. The
continuous function `KL(p̂‖·)` attains its minimum on `𝓘 ∩ K`, and that minimum is `M(p̂)`, because every point of `𝓘`
outside `K` has `KL(p̂‖p) > c`.
(ii) If `p̂ ∈ 𝓘`, then `M(p̂) ≤ KL(p̂‖p̂) = 0`. If `M(p̂) = 0`, then by (i) some `p ∈ 𝓘` has `KL(p̂‖p) = 0`, so `p = p̂`.
(iii) `q` is one of the candidates in the infimum.
(iv) *Closed.* Let `x₋` and `x₊` be outcomes where `F` is smallest and largest, and `osc F = F(x₊) − F(x₋) > 0`. Then
`p_{F,t}(x₋) = q(x₋)·e^{t·F(x₋)} / E_q[e^{tF}] ≤ (q(x₋)/q(x₊))·e^{−t·osc F}`. If `p_{F,t_k} → p ∈ Δ°`, then
`p(x₋) > 0`, so the `t_k` are bounded. A subsequence converges to some `t ≥ 0`, and by continuity `p = p_{F,t} ∈ R_F`.
*Minimum.* Let `g(t) = KL(p̂‖p_{F,t}) = KL(p̂‖q) − t·E_{p̂}[F] + log E_q[e^{tF}]`. Then `g'(t) = E_{p_{F,t}}[F] − E_{p̂}[F]`
and `g''(t) = Var_{p_{F,t}}(F) > 0`, because `F` is non-constant and `p_{F,t}` has full support. So `g` is strictly
convex. If `E_{p̂}[F] ≤ E_q[F]`, then `g'(0) ≥ 0`, and the minimum over `t ≥ 0` is at `0`. Otherwise `g'(0) < 0`. As
`t → ∞`, `E_{p_{F,t}}[F]` increases continuously toward `max F`, and `E_{p̂}[F] < max F` because `p̂` has full support
and `F` is not constant. So `g'` has a unique root `t* > 0`, and `g` is minimal there.

**Checks.** checks/test_misalignment.py::test_minimum_on_the_ray_is_attained_at_the_closed_form,
checks/test_misalignment.py::test_zero_exactly_on_the_intended_set,
checks/test_misalignment.py::test_bounded_by_departure_from_reference,
checks/test_misalignment.py::test_the_ray_leaves_every_compact_set

**Notes.** The checks exercise the standard declaration. Parts (i)–(iii) for a general closed `𝓘` rest on the proof
alone. (iv) is maximum likelihood in the family `{p_{F,t}}`, restricted to `t ≥ 0`: it matches the mean of `F`.

**Lineage.** main: Prop 34(b) for (i) and (ii); Thm 13 and Thm 17(i) for (iv) (the transverse error `D_⊥`, attained at
`t̂⁺`).

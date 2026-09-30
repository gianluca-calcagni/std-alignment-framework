# The core

> **Status: v8, in progress.** Sections 1–3: behaviours, pursuit, and the declaration. Each item carries a formal
> statement and a plain-terms twin. A definition says why this choice; a result carries a proof and checks that run in
> CI. Every item gives its lineage from the archive on `main`. The format is in `README.md`.

## 0. What the core does

Alignment compares what an actor does with what a principal intended. The core makes that comparison precise in three
steps.
1. **Behaviour** (section 1). What happens is described by how often each outcome occurs: a probability distribution.
   Any behaviour, and any change of behaviour over time, can be written as a default reweighted toward some objective,
   so this description loses nothing.
2. **Pursuit** (section 2). Pursuing an objective means reweighting a default toward it, at some intensity, along the
   steepest route. KL divergence measures the value lost against such a pursuit, when value includes the cost of
   departing from the default.
3. **Declaration and score** (section 3). Before judging, the principal declares a default and the set of behaviours it
   would accept. Misalignment is the KL divergence from the actual behaviour to the nearest acceptable one, in nats.

The core assumes nothing about how the actor produces its behaviour.

**How to read.** Items are numbered by kind: D for definitions, P for propositions. A statement, justification or proof
uses only items above it. `[P2](iii)` means part (iii) of P2. Logarithms are natural, so divergences are in nats.
Operations on functions (`p/r`, `log`, `e^F`) act outcome by outcome.

| Symbol | Meaning | Introduced in |
|---|---|---|
| `X` | the outcomes | [D1] |
| `Δ`, `Δ°` | all behaviours; the full-support ones | [D1] |
| `E_p[F]`, `Var_p(F)` | average and variance of `F` under `p` | [D1] |
| `KL(p‖r)` | the Kullback–Leibler divergence, in nats | [D1] |
| `tilt(r, F)` | `r` reweighted by `e^F` | [D1] |
| `s` | time along a path of behaviours | [P2] |
| `q`, `F`, `t` | the reference (the default), an objective, an intensity | [D2] |
| `p_{F,t}`, `R_F` | pursuit of `F` at intensity `t`; the pursuit ray | [D2] |
| `(q, 𝓘)` | a declaration: the reference and the intended behaviours | [D3] |
| `M(p̂)` | the misalignment of the actual behaviour `p̂` | [D3] |

## 1. Behaviours and tilts

### D1 — Outcomes, behaviours, divergence and tilt
**Statement.** `X` is a finite set of **outcomes**, with at least two elements. A **behaviour** is a probability
distribution `p` on `X`. `Δ` is the set of behaviours, and `Δ°` the set of **full-support** behaviours, those with
`p(x) > 0` for every `x`. For `p ∈ Δ` and `F : X → ℝ`, `E_p[F] = Σ_x p(x)·F(x)` and
`Var_p(F) = E_p[F²] − E_p[F]²`; for a set `C ⊆ X` with `p(C) > 0`, `p(·|C)` is `p` conditioned on `C`. For `p, r ∈ Δ`, the
**Kullback–Leibler divergence** is `KL(p‖r) = Σ_{x : p(x) > 0} p(x)·log(p(x)/r(x))`, which is finite when `r(x) > 0`
wherever `p(x) > 0`, and `+∞` otherwise. The **tilt** of `r ∈ Δ°` by `F : X → ℝ` is the behaviour
`tilt(r, F) = r·e^F / E_r[e^F]`.

**In plain terms.** Outcomes are the things that can happen, and a behaviour says how often each one happens; full
support means that nothing is ruled out entirely. KL measures how far one behaviour is from another; it is not
symmetric, so the order matters. Tilting reweights a behaviour toward the outcomes that a function scores higher.

**Why this choice.**
- *Finite outcomes.* Every statement can then be proved with finite sums, and checked exactly on random instances.
  General outcome spaces add conditions (absolute continuity, integrability of `e^F`, and compactness in the existence
  arguments). They come back when an item needs them.
- *Full support, where it is needed.* It keeps every logarithm finite. A behaviour that rules an outcome out, such as a
  deterministic one, is still a behaviour: it is allowed as the first argument of KL, and it is a limit of full-support
  behaviours.
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
"the default, reweighted toward an objective" is always possible, and loses nothing.

**Proof.** (i) `r·e^{log(p/r)} = p`, which already sums to 1. (ii) If `F − G = c`, the factor `e^c` cancels in the
normalization. Conversely, if the tilts are equal, then `F − log E_r[e^F] = G − log E_r[e^G]` at every outcome, so
`F − G` is constant. (iii) `tilt(tilt(r, F), G)` is proportional to `r·e^F·e^G`, and both sides are normalized;
`e^0 = 1`.

**Checks.** checks/test_tilts.py::test_every_behaviour_is_a_tilt, checks/test_tilts.py::test_tilt_objective_unique_up_to_constant,
checks/test_tilts.py::test_tilts_compose

**Lineage.** New as a statement. main used the tilt as the form of intended behaviour (Def 1), and recorded "everything
is a tilt" as an insight (NOTES §2.1) without stating it. The freedom in (ii) is main's Prop 16 (g2).

### P2 — Every change of behaviour follows a replicator equation
**Statement.** Let `s ↦ p_s` be a continuously differentiable path in `Δ°`, over an interval containing `0`, and let
`F_s = ∂_s log p_s`.
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

**Checks.** checks/test_paths.py::test_replicator_form_of_any_path, checks/test_paths.py::test_replicator_is_fisher_gradient,
checks/test_paths.py::test_pursuit_ray_solves_the_replicator_flow

**Notes.** In population genetics the replicator equation is the gradient of mean fitness in this metric, known there as
the Shahshahani metric [@shahshahani1979].

**Lineage.** New as a proposition. main: NOTES §2.1 ("everything is a tilt") and ROADMAP §6 I1 (dynamics: increments
cancel the reference).

## 2. Pursuit, and what KL measures

### D2 — Pursuit of an objective
**Statement.** Let `q ∈ Δ°`, the **reference**, and let `F : X → ℝ` be a function, an **objective**. The **pursuit** of
`F` from `q` at **intensity** `t ≥ 0` is `p_{F,t} = tilt(q, t·F)`. The **pursuit ray** of `F` from `q` is
`R_F = {p_{F,t} : t ≥ 0}`; for a constant `F` it is the single point `q`. A continuously differentiable path
`s ↦ p_s` in `Δ°`, over an interval containing `0`, **pursues** `F` if `p_s = tilt(p_0, τ(s)·F)` for a
differentiable, non-decreasing `τ` with `τ(0) = 0`.

**In plain terms.** Pursuing an objective means reweighting the default behaviour toward the outcomes that the objective
scores higher, and the intensity says how strongly. Intensity zero is the default itself, and the pursuit ray collects
every intensity. A path of behaviours pursues an objective when it keeps reweighting toward that same objective, never
away from it, from wherever it starts.

**Why this choice.**
- *It loses no generality.* Every full-support behaviour `p` lies on the pursuit ray of some objective, from any
  reference: `p = p_{F,1}` with `F = log(p/q)` ([P1](i)). Every path of behaviours follows the replicator equation of an
  objective that may move over time ([P2](i)). What the definition adds is a claim that can fail: that the objective
  stays fixed, which the next item makes testable. Mixing a behaviour with another, for example, generally gives a path
  whose objective turns, as the next item's check shows; cut-offs that exclude outcomes leave `Δ°` altogether.
- *It is canonical, given one premise.* Suppose pursuing `F` means climbing `E_p[F]` as steeply as possible, in some
  Riemannian geometry on behaviours. Up to a constant factor, the Fisher metric is the only such geometry, across
  outcome spaces of every size, that is unchanged when outcomes are split into sub-outcomes in fixed proportions
  (Čencov's theorem [@cencov1982]; [@campbell1986]). In the Fisher metric the steepest climb is the replicator field
  ([P2](ii)), and its flow from `q` is `tilt(q, s·F)` ([P2](iii)). A constant factor in the metric only rescales time,
  so the ray is the same. A notion of pursuit that must not depend on how finely outcomes are described is therefore
  led to this ray.
- *The ray needs a reference; the path does not.* The same objective pursued from two references gives two different
  rays, so the declaration below fixes the reference. Whether a path pursues `F` needs no reference at all, which is
  why later items can read pursuit from changes of behaviour without declaring a default.

**Lineage.** main: Def 1 (the Gibbs tilt `p_{G,t}`), Def 2 (the bounded actor, whose optimum is the tilt: here a
property, [P4](i)), Prop 15 (the carrier), and Prop 16 (g4) (the half-ray). The ray defines intended pursuit; it is not a
model of the actor. main's rows 67–68 and 76–78 filed results by the intended actor's model instead of by what their
proofs need, and the core keeps the two apart by construction.

### P3 — A fixed objective is visible in the changes of behaviour
**Statement.** Let `s ↦ p_s` be a continuously differentiable path in `Δ°`, over an interval containing `0`, with
`F_s = ∂_s log p_s`, and let `F` be non-constant.
(i) There is a differentiable `τ` with `τ(0) = 0` and `p_s = tilt(p_0, τ(s)·F)` for every `s` if and only if
`F_s ∈ span{F, 1}` for every `s`. Then `F_s = τ'(s)·F + c(s)`.
(ii) The path pursues `F` ([D2]) if and only if, for every `s`, `F_s = a(s)·F + b(s)` with `a(s) ≥ 0`.

**In plain terms.** Whether a changing behaviour keeps one fixed objective can be read from its changes alone: every
change must point along that objective, apart from a constant. It pursues the objective when it never moves against it.
Two changes that point in opposite directions lie on one line, but they are not one pursuit.

**Proof.** (i) If `p_s = tilt(p_0, τ(s)·F)`, then `log p_s = log p_0 + τ(s)·F − log E_{p_0}[e^{τ(s)F}]`, so
`F_s = τ'(s)·F + c(s)`, with `c(s)` minus the derivative of the log-normalizer. Conversely, let `F_s = a(s)·F + b(s)` for
every `s`. Since `F` is not constant, `F` and `1` are linearly independent, so `a` and `b` are determined by `F_s`, and
they are continuous because the path is continuously differentiable. Integrating from `0` gives
`log p_s = log p_0 + τ(s)·F + B(s)`, with `τ(s) = ∫_0^s a` and `B(s) = ∫_0^s b`, and normalization gives
`p_s = tilt(p_0, τ(s)·F)`.
(ii) By (i), the path has the form of [D2] exactly when `F_s = a(s)·F + b(s)`, and then `τ' = a`. So `τ` is
non-decreasing if and only if `a` is never negative.

**Checks.** checks/test_paths.py::test_fixed_objective_iff_span,
checks/test_paths.py::test_two_outcomes_always_keep_a_fixed_objective

**Notes.** The condition `F_s ∈ span{F, 1}` is the precise form of "the increments have rank 1", which later items use
for identifiability. The sign condition in (ii) is what a rank read on lines, not on rays, misses. With only two
outcomes, `span{F, 1}` contains every function, so every path keeps a fixed objective: the test has content only with
three or more outcomes. (On main, this is why a two-arrangement allele-frequency series could not test the rank.)

**Lineage.** New as a proposition. main: ROADMAP §6 I1 (the dynamic rank), and the I1-dyn and I1-dyn2 tests, whose null
hypothesis counted opposite-pointing increments as one evaluator.

### P4 — What KL measures
**Statement.** Let `q ∈ Δ°`, `F : X → ℝ` and `t > 0`, and let `J_t(p) = E_p[F] − KL(p‖q)/t` for `p ∈ Δ`: the average of
the objective, minus the cost of departing from the reference, priced at `1/t`.
(i) **Value.** For every `p ∈ Δ`, `J_t(p_{F,t}) − J_t(p) = KL(p‖p_{F,t})/t`. So `p_{F,t}` is the unique maximizer of
`J_t`.
(ii) **Every behaviour is an optimum.** For every `r ∈ Δ°`, `r = p_{G,1}` with `G = log(r/q)`. So `r` is the unique
maximizer of `J_1` for the objective `G`, and for every `p ∈ Δ` the value `p` loses against `r` in that objective is
exactly `KL(p‖r)`.
(iii) **Chain rule.** For every partition `𝒢` of `X` into non-empty cells, every `p ∈ Δ` and every `r ∈ Δ°`,
`KL(p‖r) = KL(p_𝒢‖r_𝒢) + Σ_{C ∈ 𝒢, p(C) > 0} p(C)·KL(p(·|C)‖r(·|C))`, where `p_𝒢` is the distribution of the cell
masses `p(C)`.
(iv) **Merging never increases it.** `KL(p_𝒢‖r_𝒢) ≤ KL(p‖r)`, with equality if and only if `p/r` is constant on every
cell `C` with `p(C) > 0`.

**In plain terms.** Count the value of a behaviour as the average of an objective minus the cost of moving away from
the default. Then the best behaviour is the pursuit of the objective, at the intensity set by the price of moving
away, and the KL from any behaviour to it is exactly the value given up. Every full-support behaviour is the best one for some objective, so
this reading always applies. KL also splits into a part between groups and a part within groups when outcomes are
grouped, and grouping outcomes can only hide differences, never create them.

**Proof.** (i) With `Z = E_q[e^{tF}]`, `log p_{F,t} = log q + t·F − log Z`, so for every `p ∈ Δ`,
`KL(p‖p_{F,t}) = KL(p‖q) − t·E_p[F] + log Z = log Z − t·J_t(p)`. Hence `J_t(p) = (log Z − KL(p‖p_{F,t}))/t`. Taking the
difference at `p_{F,t}`, where the KL is `0`, and at `p` gives the identity. KL is non-negative, and zero only between
equal behaviours (Gibbs' inequality), so the maximizer is unique.
(ii) `p_{G,1} = tilt(q, log(r/q)) = r` by [P1](i). Then apply (i) with `t = 1`.
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
**Statement.** A **declaration** is a pair `(q, 𝓘)`: a reference `q ∈ Δ°`, and a non-empty set `𝓘 ⊆ Δ°` of
**intended behaviours**, closed in `Δ°`. The **misalignment** of a behaviour `p̂ ∈ Δ` is
`M(p̂) = inf_{p ∈ 𝓘} KL(p̂‖p)`. The **standard declaration** of an objective `F` is `(q, R_F)`: pursuit of `F` from
`q` at every intensity, including none.
*Rule of use* (a condition on how a declaration is made, not a mathematical property): a declaration is fixed before,
and without using, the behaviour it will judge.

**In plain terms.** Before looking at what the actor does, the principal states a default behaviour and the set of
behaviours it would accept. Misalignment is how far the actual behaviour is from the nearest acceptable one, in nats.
When the request is "pursue this objective", every intensity of pursuing it is acceptable, including none: an actor
that stays at the default is not misaligned, though it may be useless, which is a different failure.

**Why this choice.**
- *KL, with the actual behaviour first.* Count value as in [P4]: the average of an objective, minus the cost of
  departing from the reference. Then each intended behaviour is the best one for its own objective ([P4](ii)), and
  `KL(p̂‖p)` is exactly the value `p̂` loses against `p`. So `M(p̂)` is the smallest value lost against any acceptable
  behaviour, each judged by its own objective, and that identity fixes the order of the arguments. The cost term is
  what makes the reading general: without it, the only fully intended behaviours of an objective would be
  those on its best outcomes, and every behaviour that puts any mass elsewhere would be charged.
- *The nearest acceptable behaviour.* Taking the minimum gives the actor the benefit of the doubt: it is charged only
  for what no acceptable behaviour explains.
- *Grouping only hides.* By [P4](iii) and (iv), the score splits along groupings of outcomes, and grouping can only hide
  misalignment. Later items use this for resolutions.
- *A set, not a point.* A principal who asks for `F` without naming an intensity would otherwise charge the actor for an
  intensity it never asked about (main: row 74, the price measure is a regret, not misalignment). A single intended
  behaviour is the case `𝓘 = {p*}`.
- *The standard declaration is the pursuit ray,* because "pursue `F`" states a fixed objective ([D2]) at an unstated
  intensity. It includes doing nothing. A principal for whom doing nothing is a failure declares a smaller set (main:
  the floor, Def 20).
- *The actual behaviour may rule outcomes out; the intended ones may not.* A deterministic actor still gets a score.
  Intended behaviours keep full support so that the score is finite.
- *Declared before, not fitted after.* A reference or an intended set fitted from the behaviour being judged removes
  exactly the differences the judgement needs. On main, I1-dyn fitted a Hardy–Weinberg reference from the counts it
  judged, and its test could not fail.
- *Slim on purpose.* main's declaration (Def 23) had nine slots. Only four changed the measure, and all four are ways of
  generating `𝓘`. Rules, instruments, feasibility and the environment did not enter the measure, so they are not
  declared here; instruments return with identifiability, as interventions. The reference enters the measure through
  `𝓘` (the pursuit ray starts at `q`), and later items use it directly. A later item adds a slot only with a case where
  the slot changes a verdict, and with its default.

**Lineage.** main: Def 19 and Prop 34 (the declared intended set), Def 17 (the free convention's half-ray), Def 23 (the
declaration, slimmed; its timing slot becomes the rule of use), and row 74. New: behaviours that rule outcomes out are
scored.

### P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits
**Statement.** Let `(q, 𝓘)` be a declaration and `p̂ ∈ Δ`.
(i) If `p̂ ∈ Δ°`, the infimum in `M(p̂)` is attained: some `p ∈ 𝓘` has `KL(p̂‖p) = M(p̂)`.
(ii) `M(p̂) = 0` if and only if `p̂` is in the closure of `𝓘` in `Δ`. For `p̂ ∈ Δ°`, this means `p̂ ∈ 𝓘`.
(iii) If `q ∈ 𝓘`, then `M(p̂) ≤ KL(p̂‖q)`.
(iv) Let `F` be non-constant, and `A` the set of outcomes where `F` is largest. The pursuit ray `R_F` is closed in `Δ°`,
so `(q, R_F)` is a declaration. Under it:
- if `E_{p̂}[F] ≤ E_q[F]`, then `M(p̂) = KL(p̂‖q)`;
- if `E_q[F] < E_{p̂}[F] < max F`, then `M(p̂) = KL(p̂‖p_{F,t*})`, where `t* > 0` is the unique intensity with
  `E_{p_{F,t*}}[F] = E_{p̂}[F]`;
- if `E_{p̂}[F] = max F`, that is, `p̂` puts all its mass on `A`, then `M(p̂) = KL(p̂‖q(·|A))`, approached as `t → ∞`
  and not attained. It is `0` exactly when `p̂ = q(·|A)`.

**In plain terms.** For a full-support behaviour there is always a nearest acceptable behaviour. Misalignment is zero
only for acceptable behaviours and their limits. When the default is acceptable, misalignment is never more than the
actual behaviour's departure from the default. For "pursue `F`": a behaviour that does no better than the default is
charged its whole departure from it; one that does better is compared with the pursuit that reaches the same average
of `F`; and one that only ever picks the best outcomes is aligned exactly when it splits its choices among tied best
outcomes as the default would. In particular, a maximizer with a single best outcome is aligned.

**Proof.** (i) Pick `p₀ ∈ 𝓘` and let `c = KL(p̂‖p₀)` and `H(p̂) = −Σ_x p̂(x)·log p̂(x)`. For any `p ∈ Δ°`,
`KL(p̂‖p) = −H(p̂) − Σ_y p̂(y)·log p(y)`, and every term `−p̂(y)·log p(y)` is non-negative. So `KL(p̂‖p) ≤ c` implies
`p(x) ≥ exp(−(c + H(p̂))/p̂(x)) > 0` for every `x`, since `p̂(x) > 0`. The set `K = {p ∈ Δ : KL(p̂‖p) ≤ c}` is closed in
`Δ`, because `KL(p̂‖·)` is lower semicontinuous on `Δ` (with value `+∞` where some `p(x) = 0`). So `K` is compact, and by
the bound it lies in `Δ°`. Since `𝓘` is closed in `Δ°`, the set `𝓘 ∩ K` is closed in `K`, hence compact, and it contains
`p₀`. The continuous function `KL(p̂‖·)` attains its minimum on `𝓘 ∩ K`, and that minimum is `M(p̂)`, because every
point of `𝓘` outside `K` has `KL(p̂‖p) > c`.
(ii) If `M(p̂) = 0`, there are `p_k ∈ 𝓘` with `KL(p̂‖p_k) → 0`, and by Pinsker's inequality
`Σ_x |p̂(x) − p_k(x)| ≤ (2·KL(p̂‖p_k))^{1/2} → 0`, so `p̂` is in the closure of `𝓘`. Conversely, if `p_k ∈ 𝓘` and
`p_k → p̂`, then `KL(p̂‖p_k) = Σ_{p̂(x) > 0} p̂(x)·log(p̂(x)/p_k(x)) → 0`, because `p_k(x) → p̂(x) > 0` on every term.
For `p̂ ∈ Δ°`, the closure of `𝓘` in `Δ` meets `Δ°` exactly in `𝓘`, because `𝓘` is closed in `Δ°`.
(iii) `q` is one of the candidates in the infimum.
(iv) *Closed.* Let `x₋` and `x₊` be outcomes where `F` is smallest and largest, and `osc F = F(x₊) − F(x₋) > 0`. Then
`p_{F,t}(x₋) = q(x₋)·e^{t·F(x₋)} / E_q[e^{tF}] ≤ (q(x₋)/q(x₊))·e^{−t·osc F}`. If `p_{F,t_k} → p ∈ Δ°`, then
`p(x₋) > 0`, so the `t_k` are bounded. A subsequence converges to some `t ≥ 0`, and by continuity `p = p_{F,t} ∈ R_F`.
*Minimum.* Let `g(t) = KL(p̂‖p_{F,t}) = KL(p̂‖q) − t·E_{p̂}[F] + log E_q[e^{tF}]`, finite for every `t ≥ 0`. Then
`g'(t) = E_{p_{F,t}}[F] − E_{p̂}[F]` and `g''(t) = Var_{p_{F,t}}(F) > 0`, because `F` is non-constant and `p_{F,t}` has
full support; so `g` is strictly convex. As `t → ∞`, `E_{p_{F,t}}[F]` increases continuously toward `max F`. If
`E_{p̂}[F] ≤ E_q[F]`, then `g'(0) ≥ 0`, and the minimum over `t ≥ 0` is at `0`. If `E_q[F] < E_{p̂}[F] < max F`, then
`g'` has a unique root `t* > 0`, where `g` is minimal. If `E_{p̂}[F] = max F`, then `g' < 0` everywhere, so `g`
decreases toward its limit, which is not attained: with `m = max F`,
`g(t) = KL(p̂‖q) − t·m + log E_q[e^{tF}] = KL(p̂‖q) + log E_q[e^{t(F − m)}] → KL(p̂‖q) + log q(A) = KL(p̂‖q(·|A))`, using
that `p̂` puts all its mass on `A`. That limit is `0` exactly when `p̂ = q(·|A)`.

**Checks.** checks/test_misalignment.py::test_minimum_on_the_ray_is_attained_at_the_closed_form,
checks/test_misalignment.py::test_best_outcomes_case, checks/test_misalignment.py::test_zero_exactly_on_the_intended_set,
checks/test_misalignment.py::test_bounded_by_departure_from_reference,
checks/test_misalignment.py::test_the_ray_leaves_every_compact_set

**Notes.** The checks exercise the standard declaration; parts (i)–(iii) for a general closed `𝓘` rest on the proof
alone. Pinsker's inequality is standard [@cover2006]. The second case of (iv) is maximum likelihood in the family
`{p_{F,t}}`, restricted to `t ≥ 0`: it matches the mean of `F`. In the third case a maximizer that breaks ties among the
best outcomes differently from the reference is charged; a principal who is indifferent among tied outcomes says so
with a resolution, which a later item introduces.

**Lineage.** main: Prop 34(b) for (i) and (ii); Thm 13 and Thm 17(i) for the first two cases of (iv) (the transverse error
`D_⊥`, attained at `t̂⁺`). New: behaviours that rule outcomes out, including the deterministic maximizer (the third case).

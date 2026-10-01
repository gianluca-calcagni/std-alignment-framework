# The core

> **Status: v8, in progress.** Sections 1–6: behaviours, pursuit, the specification, resolution, stakes, and
> identifiability. Each item carries a formal
> statement and a plain-terms twin. A definition says why this choice; a result carries a proof and checks that run in
> CI. Every item gives its lineage from the archive on `main`. The format is in `README.md`.

## 0. What the core does

Alignment compares what an actor does with what a principal intended. The core makes that comparison precise in six
steps.
1. **Behaviour** (section 1). What happens is described by how often each outcome occurs: a probability distribution.
   Any behaviour, and any change of behaviour over time, can be written as a default reweighted toward some objective,
   so this description loses nothing.
2. **Pursuit** (section 2). Pursuing an objective means reweighting the default toward it, at some intensity, along
   the steepest route. KL divergence measures the value lost against such a pursuit, when value includes the cost of
   departing from the default.
3. **Specification and score** (section 3). Before judging, the principal declares a specification: a default, and the
   set of behaviours it would accept. Misalignment is the KL divergence from the actual behaviour to the nearest acceptable one, in nats of
   evidence per decision. How far the actor departs from the default splits exactly into pursuit and misalignment.
4. **Resolution** (section 4). The principal may declare that it does not care about some distinctions between
   outcomes, and the actor may be unable to see some. Each changes misalignment in a way the core computes exactly.
5. **Stakes and sensitivity** (section 5). Misalignment is in nats; the shortfall says how much of the objective is
   lost, in its own units. Both come with bounds on how much a slightly wrong default or objective can move them.
6. **Identifiability** (section 6). What a change of behaviour or an intervention reveals about the actor without
   knowing what it wants: how much of the change is misaligned, how much of the objective it gains, and how the actor
   responds to incentives.

The core assumes nothing about how the actor produces its behaviour.

**How to read.** Items are numbered by kind: D for definitions, P for propositions. A statement, justification or proof
uses only items above it. `[P2](iii)` means part (iii) of P2. Logarithms are natural, so divergences are in nats.
Operations on functions (`p/r`, `log`, `e^F`) act outcome by outcome. The Notes of each item give the names its objects
carry in other fields.

| Symbol | Meaning | Introduced in |
|---|---|---|
| `X` | the outcomes | [D1] |
| `Δ`, `Δ°` | all behaviours; the full-support ones | [D1] |
| `E_p[F]`, `Var_p(F)`, `Cov_p(F, G)` | average, variance and covariance under `p` | [D1] |
| `KL(p‖r)` | the Kullback–Leibler divergence, in nats | [D1] |
| `tilt(r, F)` | `r` reweighted by `e^F` | [D1] |
| `s`, `F_s` | time along a path of behaviours; the objective the change reveals | [P2] |
| `q`, `F`, `t` | the default, an objective, an intensity | [D2] |
| `p_{F,t}`, `R_F` | pursuit of `F` at intensity `t`; the pursuit ray | [D2] |
| `J_t` | net value: the objective's average minus the cost of departing from the default | [P4] |
| `(q, 𝓘)` | a specification, declared by the principal: the default and the intended behaviours | [D3] |
| `M(p̂)` | the misalignment of the actual behaviour `p̂` | [D3] |
| `t*`, `p°` | the revealed intensity; the nearest intended behaviour | [P5] |
| `KL(p̂‖q)` | the departure of the actual behaviour from the default | [P6] |
| `ℬ`, `𝒜` | the principal's resolution; the actor's resolution | [D4] |
| `E_q[F\|𝒜]`, `F̄` | the cell average of `F` under the default | [D4] |
| `λ`, `S(p̂)` | the matched intensity; the shortfall, in the units of `F` | [D5] |
| `θ` | the angle between a revealed objective and the declared one | [P11] |
| `u`, `φ` | an intervention; the pass-through | [D6] |
| `σ_q(F)` | the spread of `F` under the default: `Var_q(F)^{1/2}` | [P13] |

## 1. Behaviours and tilts

### D1 — Outcomes, behaviours, divergence and tilt
**Statement.** `X` is a finite set of **outcomes**, with at least two elements. A **behaviour** is a probability
distribution `p` on `X`. `Δ` is the set of behaviours, and `Δ°` the set of **full-support** behaviours, those with
`p(x) > 0` for every `x`. For `p ∈ Δ` and `F : X → ℝ`, `E_p[F] = Σ_x p(x)·F(x)` and
`Var_p(F) = E_p[F²] − E_p[F]²`, and `Cov_p(F, G) = E_p[F·G] − E_p[F]·E_p[G]`; for a set `C ⊆ X` with `p(C) > 0`, `p(·|C)` is `p` conditioned on `C`. For `p, r ∈ Δ`,
the **Kullback–Leibler divergence** is `KL(p‖r) = Σ_{x : p(x) > 0} p(x)·log(p(x)/r(x))`, which is finite when
`r(x) > 0` wherever `p(x) > 0`, and `+∞` otherwise. The **tilt** of `r ∈ Δ°` by `F : X → ℝ` is the behaviour
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

**Notes.** A behaviour is a policy in reinforcement learning, a mixed strategy in game theory, a distribution of choices
in economics, and a distribution of types in a population in biology. The tilt is exponential tilting in statistics.

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

**Notes.** `log(p/r)` is the log-likelihood ratio of `p` to `r`. Recovering an objective from behaviour is the problem of
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

**Checks.** checks/test_paths.py::test_replicator_form_of_any_path, checks/test_paths.py::test_replicator_is_fisher_gradient,
checks/test_paths.py::test_pursuit_ray_solves_the_replicator_flow

**Notes.** "Revealed" is meant as in revealed preference: read from behaviour, not assumed about the actor. In
population genetics the revealed objective is the Malthusian fitness of each type (its per-capita growth rate), up to a
constant, and the replicator equation is the gradient of mean fitness in this metric, known there as the Shahshahani
metric [@shahshahani1979].

**Lineage.** New as a proposition. main: NOTES §2.1 ("everything is a tilt") and ROADMAP §6 I1 (dynamics: increments
cancel the default).

## 2. Pursuit, and what KL measures

### D2 — Pursuit of an objective
**Statement.** Let `q ∈ Δ°`, the **default**, and let `F : X → ℝ` be a function, an **objective**. The **pursuit** of
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
  default: `p = p_{F,1}` with `F = log(p/q)` ([P1](i)). Every path of behaviours follows the replicator equation of an
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
- *The ray needs a default; the path does not.* The same objective pursued from two defaults gives two different rays,
  so the specification below fixes the default. Whether a path pursues `F` needs no default at all, which is why later
  items can read pursuit from changes of behaviour without declaring one.

**Notes.** Names in other fields. The default is the reference policy of RL fine-tuning, the prior of KL control, the
base measure of an exponential family, the status quo of behavioural economics, and the population before selection
in biology. The objective is a reward, a utility, or a log-fitness. The pursuit `p_{F,t}` is the optimum of KL-regularized
reward maximization with coefficient `1/t` in RL fine-tuning; with a uniform default it is the logit choice rule, or
quantal response, with rationality `t` [@mckelvey1995]; and it is the result of `t` generations of constant selection
with fitness `e^F`. The intensity is an inverse temperature in physics, and "optimization pressure" in AI safety.

**Lineage.** main: Def 1 (the Gibbs tilt `p_{G,t}`, with `q` there called the reference), Def 2 (the bounded actor,
whose optimum is the tilt: here a property, [P4](i)), Prop 15 (the carrier), and Prop 16 (g4) (the half-ray). The ray
defines intended pursuit; it is not a model of the actor. main's rows 67–68 and 76–78 filed results by the intended
actor's model instead of by what their proofs need, and the core keeps the two apart by construction.

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
three or more outcomes. (On main, this is why a two-arrangement allele-frequency series could not test the rank.) In
population genetics a fixed objective is constant selection, and a turning one is fluctuating selection; in economics
the question is whether preferences are stable.

**Lineage.** New as a proposition. main: ROADMAP §6 I1 (the dynamic rank), and the I1-dyn and I1-dyn2 tests, whose null
hypothesis counted opposite-pointing increments as one evaluator.

### P4 — What KL measures
**Statement.** Let `q ∈ Δ°`, `F : X → ℝ` and `t > 0`. The **net value** of `p ∈ Δ` is `J_t(p) = E_p[F] − KL(p‖q)/t`:
the average of the objective, minus the cost of departing from the default, priced at `1/t`.
(i) **Value.** For every `p ∈ Δ`, `J_t(p_{F,t}) − J_t(p) = KL(p‖p_{F,t})/t`. So `p_{F,t}` is the unique maximizer of
`J_t`.
(ii) **Every behaviour is an optimum.** For every `r ∈ Δ°`, `r = p_{G,1}` with `G = log(r/q)`. So `r` is the unique
maximizer of `J_1` for the objective `G`, and for every `p ∈ Δ` the net value `p` loses against `r` in that objective is
exactly `KL(p‖r)`.
(iii) **Chain rule.** For every partition `𝒢` of `X` into non-empty cells, every `p ∈ Δ` and every `r ∈ Δ°`,
`KL(p‖r) = KL(p_𝒢‖r_𝒢) + Σ_{C ∈ 𝒢, p(C) > 0} p(C)·KL(p(·|C)‖r(·|C))`, where `p_𝒢` is the distribution of the cell
masses `p(C)`.
(iv) **Merging never increases it.** `KL(p_𝒢‖r_𝒢) ≤ KL(p‖r)`, with equality if and only if `p/r` is constant on every
cell `C` with `p(C) > 0`.

**In plain terms.** Count the net value of a behaviour as the average of an objective minus the cost of moving away from
the default. Then the best behaviour is the pursuit of the objective, at the intensity set by the price of moving away,
and the KL from any behaviour to it is exactly the net value given up. Every full-support behaviour is the best one for
some objective, so this reading always applies. KL also splits into a part between groups and a part within groups when
outcomes are grouped, and grouping outcomes can only hide differences, never create them.

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

**Notes.** (i) is the Gibbs variational principle. The net value is the objective of KL-regularized RL fine-tuning, and a
free energy in the literature on bounded rationality [@ortega2013]. The same ray therefore arises twice: as the steepest
climb of [D2] and as the set of best behaviours at every price in (i). The chain rule and Gibbs' inequality are standard
[@cover2006]. Hobson characterized KL, up to a positive factor, by a small set of conditions that includes the chain rule
(iii) [@hobson1969]. The last check confirms that three common alternatives (χ², squared Hellinger, total variation)
break it.

**Lineage.** main: Thm 1 (regret is a divergence) for (i); Def 21 (the within-cell divergence) for (iii) and (iv). New:
(ii), which follows from [P1] and removes the need to assume that intended behaviour is "Gibbs", since every
full-support behaviour is. main's Prop 15 (other regularizers) is not carried: the score is KL.

## 3. The specification and misalignment

### D3 — Specification, declaration and misalignment
**Statement.** A **specification** is a pair `(q, 𝓘)`: a default `q ∈ Δ°`, and a non-empty set `𝓘 ⊆ Δ°` of
**intended behaviours**, closed in `Δ°`. The **misalignment** of a behaviour `p̂ ∈ Δ` is
`M(p̂) = inf_{p ∈ 𝓘} KL(p̂‖p)`. The **standard specification** of an objective `F` is `(q, R_F)`: pursuit of `F` from
`q` at every intensity, including none.
*Rule of use* (a condition on how a specification is made, not a mathematical property): a specification is
**declared**, that is, fixed before, and without using, the behaviour it will judge.

**In plain terms.** Before looking at what the actor does, the principal states a default behaviour and the set of
behaviours it would accept. Misalignment is how far the actual behaviour is from the nearest acceptable one, in nats.
When the request is "pursue this objective", every intensity of pursuing it is acceptable, including none: an actor
that stays at the default is not misaligned, though it may be useless, which is a different failure.

**Why this choice.**
- *KL, with the actual behaviour first.* Count value as the net value of [P4]: the average of an objective, minus the
  cost of departing from the default. Then each intended behaviour is the best one for its own objective ([P4](ii)),
  and `KL(p̂‖p)` is exactly the net value `p̂` loses against `p`. So `M(p̂)` is the smallest loss against any acceptable
  behaviour, each judged by its own objective, and that identity fixes the order of the arguments. The cost term is
  what makes the reading general: without it, the only fully intended behaviours of an objective would be those on its
  best outcomes, and every behaviour that puts any mass elsewhere would be charged.
- *What the number means.* If the actor behaves as `p̂` and `p` is intended, each independent decision adds on average
  `KL(p̂‖p)` nats to the log-likelihood ratio in favour of `p̂` over `p`. So `M(p̂)` is the slowest rate at which an
  observer gathers evidence that the actor is not behaving as intended: about `1/M(p̂)` decisions give one nat, odds of
  about `e` to 1.
- *The direction charges the unintended.* `KL(p̂‖p)` is large when the actor often does what `p` rarely does, and
  comparatively small when the actor merely does less of what `p` does. Doing the unintended costs more than leaving the intended undone.
- *The nearest acceptable behaviour.* Taking the minimum gives the actor the benefit of the doubt: it is charged only
  for what no acceptable behaviour explains.
- *Grouping only hides.* By [P4](iii) and (iv), the score splits along groupings of outcomes, and grouping can only hide
  misalignment. Later items use this for resolutions.
- *A set, not a point.* A principal who asks for `F` without naming an intensity would otherwise charge the actor for an
  intensity it never asked about (main: row 74, the price measure is a regret, not misalignment). A single intended
  behaviour is the case `𝓘 = {p*}`.
- *The standard specification is the pursuit ray,* because "pursue `F`" states a fixed objective ([D2]) at an unstated
  intensity. It includes doing nothing. A principal for whom doing nothing is a failure declares a smaller set (main:
  the floor, Def 20).
- *The actual behaviour may rule outcomes out; the intended ones may not.* A deterministic actor still gets a score.
  Intended behaviours keep full support so that the score is finite.
- *Declared before, not fitted after.* A default or an intended set fitted from the behaviour being judged removes
  exactly the differences the judgement needs. On main, I1-dyn fitted its default (a Hardy–Weinberg expectation) from
  the counts it judged, and its test could not fail.
- *Stakes are reported separately.* Misalignment in nats says nothing about how much of `F` is at stake. A later item
  reports the shortfall in `F`'s own units (main: Def 22 and R8-1, where this lesson was learned).
- *Slim on purpose.* main's declaration (Def 23, the same object under its old name) had nine slots. Only four changed the measure, and all four are ways of
  generating `𝓘`. Rules, instruments, feasibility and the environment did not enter the measure, so they are not
  declared here; instruments return with identifiability, as interventions. The default enters the measure through `𝓘`
  (the pursuit ray starts at `q`), and later items use it directly. A later item adds a slot only with a case where the
  slot changes a verdict, and with the value it takes when nothing is declared.

**Notes.** The principal declares; what it declares is the specification, the word AI safety and formal verification use
for the set of acceptable behaviours. Misalignment is then a quantitative distance from the specification. The direction of KL used here is the
one called zero-forcing in variational inference.

**Lineage.** main: Def 19 and Prop 34 (the declared intended set), Def 17 (the free convention's half-ray), Def 23 (the
declaration, slimmed; its timing slot becomes the rule of use), and row 74. New: behaviours that rule outcomes out are
scored.

### P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits
**Statement.** Let `(q, 𝓘)` be a specification and `p̂ ∈ Δ`.
(i) If `p̂ ∈ Δ°`, the infimum in `M(p̂)` is attained: some `p ∈ 𝓘` has `KL(p̂‖p) = M(p̂)`.
(ii) `M(p̂) = 0` if and only if `p̂` is in the closure of `𝓘` in `Δ`. For `p̂ ∈ Δ°`, this means `p̂ ∈ 𝓘`.
(iii) If `q ∈ 𝓘`, then `M(p̂) ≤ KL(p̂‖q)`.
(iv) Let `F` be non-constant, and `A` the set of outcomes where `F` is largest. The pursuit ray `R_F` is closed in `Δ°`,
so `(q, R_F)` is a specification. Under it, with `p°` the **nearest intended behaviour** (or its limit):
- if `E_{p̂}[F] ≤ E_q[F]`, then `p° = q` and `M(p̂) = KL(p̂‖q)`;
- if `E_q[F] < E_{p̂}[F] < max F`, then `p° = p_{F,t*}` and `M(p̂) = KL(p̂‖p°)`, where the **revealed intensity**
  `t* > 0` is the unique intensity with `E_{p_{F,t*}}[F] = E_{p̂}[F]`;
- if `E_{p̂}[F] = max F`, that is, `p̂` puts all its mass on `A`, then `p° = q(·|A)` and `M(p̂) = KL(p̂‖q(·|A))`,
  approached as `t → ∞` and not attained. It is `0` exactly when `p̂ = q(·|A)`.

**In plain terms.** For a full-support behaviour there is always a nearest acceptable behaviour. Misalignment is zero
only for acceptable behaviours and their limits. When the default is acceptable, misalignment is never more than the
actual behaviour's departure from the default. For "pursue `F`": a behaviour that does no better than the default is
charged its whole departure from it; one that does better is compared with the pursuit that reaches the same average
of `F`, whose intensity is the one the behaviour reveals; and one that only ever picks the best outcomes is aligned
exactly when it splits its choices among tied best outcomes as the default would. In particular, a maximizer with a
single best outcome is aligned.

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
checks/test_misalignment.py::test_bounded_by_departure_from_default,
checks/test_misalignment.py::test_the_ray_leaves_every_compact_set, checks/test_misalignment.py::test_deviance_identity

**Notes.** The checks exercise the standard specification; parts (i)–(iii) for a general closed `𝓘` rest on the proof
alone. Pinsker's inequality is standard [@cover2006]. The revealed intensity is the weight that maximum-entropy inverse
reinforcement learning, in its one-step form, fits for the single feature `F` [@ziebart2008]; in the first case that
fit is zero or negative, and in the third it is infinite. For `n` independent decisions with observed frequencies `p̂`, the log-likelihood ratio of an unrestricted
model against the best pursuit of `F` is `n·M(p̂)`, so `2n·M(p̂)` is the deviance of the model "the actor pursues `F`
from the default" (checked in the second and first cases). In the third case, a maximizer that breaks ties among the
best outcomes differently from the default is charged; a principal who is indifferent among tied outcomes says so with
a resolution, which a later item introduces.

**Lineage.** main: Prop 34(b) for (i) and (ii); Thm 13 and Thm 17(i) for the first two cases of (iv) (the transverse error
`D_⊥`, attained at `t̂⁺`). New: behaviours that rule outcomes out, including the deterministic maximizer (the third case),
and the name "revealed intensity".

### P6 — The departure from the default splits into pursuit and misalignment
**Statement.** Under the standard specification of a non-constant `F`, let `p̂ ∈ Δ` and let `p°` be as in [P5](iv). The
**departure** of `p̂` from the default is `KL(p̂‖q)`, and
`KL(p̂‖q) = KL(p°‖q) + M(p̂)`.
So `0 ≤ M(p̂) ≤ KL(p̂‖q)`, and `M(p̂) = KL(p̂‖q)` when `E_{p̂}[F] ≤ E_q[F]`.

**In plain terms.** How far the actor moved away from the default splits exactly into two parts: the movement explained
by pursuing the objective, and the misalignment. An actor that does no better than the default has all of its movement
counted as misalignment.

**Proof.** In the first case of [P5](iv), `p° = q` and `KL(q‖q) = 0`. In the second, `log(p°/q) = t*·F − log E_q[e^{t*F}]`,
so `KL(p̂‖q) − KL(p̂‖p°) = E_{p̂}[log(p°/q)] = t*·E_{p̂}[F] − log E_q[e^{t*F}]`. Since `E_{p̂}[F] = E_{p°}[F]`, this equals
`t*·E_{p°}[F] − log E_q[e^{t*F}] = E_{p°}[log(p°/q)] = KL(p°‖q)`. In the third, `p̂` and `q(·|A)` put all their mass on
`A`, so `KL(p̂‖q) − KL(p̂‖q(·|A)) = −log q(A) = KL(q(·|A)‖q)`. The bounds follow because KL is non-negative, and the last
claim is the first case.

**Checks.** checks/test_misalignment.py::test_departure_splits_into_pursuit_and_misalignment

**Notes.** The identity is a Pythagorean relation for KL along the pursuit ray. In RL fine-tuning the departure is the
KL from the reference policy, often treated as a budget; the identity splits that budget into the part spent on the
objective and the misaligned part. Whenever the actor departs from the default, `M(p̂)/KL(p̂‖q)` is the misaligned share
of its departure, between 0 and 1.

**Lineage.** main: Thm 13 (the intent-ray decomposition) and NOTES §2.5 (the intent ray). New: the third case, and the
reading as a split of the departure.

## 4. Resolution: what each side distinguishes

### D4 — Resolution
**Statement.** A **resolution** is a partition `𝒢` of `X` into non-empty **cells**. A function is constant on cells if it
takes one value on each cell. For `p ∈ Δ`, `p_𝒢` is the distribution of the cell masses `p(C)`. For `q ∈ Δ°` and
`F : X → ℝ`, the **cell average** `E_q[F|𝒢]` is the function equal, on each cell `C`, to `E_{q(·|C)}[F]`. Resolutions
are used in two positions.
- A specification `(q, 𝓘)` is **stated at resolution** `ℬ` if `𝓘 = {p ∈ Δ° : p_ℬ ∈ 𝓘_ℬ}` for a non-empty set `𝓘_ℬ`
  of full-support distributions on the cells, closed in the set of all full-support distributions on the cells. The
  principal is then **indifferent** inside the cells of `ℬ`. For an objective `F` constant on the cells of `ℬ`, the **standard specification at resolution** `ℬ` takes
  `𝓘_ℬ` to be the pursuit ray of `F`, read on the cells, from `q_ℬ`.
- A behaviour `p` is **limited to** a resolution `𝒜` if it splits every cell as the default does: `p(·|A) = q(·|A)` for
  every cell `A` of `𝒜` with `p(A) > 0`. An actor **has resolution** `𝒜` if every behaviour it can produce is limited
  to `𝒜`.

When nothing is declared or known, the resolution is the finest one, with one outcome per cell, in both positions.

**In plain terms.** A resolution groups outcomes into cells that are treated as one. A principal who states its
specification on cells declares that it does not care how outcomes inside a cell are split, only how often each cell
occurs. An actor with a resolution cannot tell the outcomes inside a cell apart: it can change how often each cell
occurs, but inside a cell the outcomes keep the proportions they have by default.

**Why this choice.**
- *One object, two positions.* The same kind of object describes what the principal cares to distinguish and what the
  actor can distinguish. Gaps between the two cover two familiar failures: a principal who cares about distinctions the
  actor cannot see (main's transmission gap, G2), and an actor that acts on distinctions the principal never mentioned
  (underdetermination, G1).
- *Partitions are the general case here.* On a finite set, a σ-algebra is the same thing as a partition into cells.
- *Inside an actor's cells, the default decides.* An actor that cannot tell two outcomes apart cannot change how often
  one occurs relative to the other, so that ratio stays where it is without the actor's choice: at the default ([D2]).
  This needs no object beyond the specification.
- *The finest resolution unless declared.* A principal who declares a coarse resolution cannot see what happens inside
  its cells; on main, a style exploit lived almost entirely inside cells in toy tests (B1). So indifference has to be
  declared, never assumed. An actor's resolution, in contrast, is a fact about the actor, to be identified from its
  behaviour rather than declared.
- *Not the meet.* The finest partition coarser than both resolutions (their meet) holds the events both sides can
  describe, which are common knowledge in Aumann's sense [@aumann1976]. Misalignment computed there is a lower bound both
  can verify ([P4](iv)), but it is blind to every gap between the two resolutions, so it is not the score.

**Notes.** In reinforcement learning, an actor's resolution is a state abstraction, and outcomes it cannot tell apart
are aliased. A principal's resolution is a coarse-graining of the outcomes.

**Lineage.** main: Def 21 (the declared resolution: the principal's position), B1 and NOTES H14 (one object in several
positions; retention), and ROADMAP §6 G1, G2 and G4. New: the actor's position as a definition, with the default deciding
inside cells.

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
(ii) Since `F` is constant on each cell, `p_{F,t}(·|C) = q(·|C)` for every `t` and every cell `C`, and `(p_{F,t})_ℬ` is the
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

**Lineage.** main: Def 21 and R7-10 (a declared resolution removes exactly the drift inside cells, under the free
convention), Prop 32(b) and ROADMAP §6 G1 (underdetermination, here declared).

### P8 — An actor that cannot tell outcomes apart
**Statement.** Let `𝒜` be a resolution, `q ∈ Δ°` the default, `F : X → ℝ`, and `F̄ = E_q[F|𝒜]` its cell average.
(i) **Limited behaviours.** The full-support behaviours limited to `𝒜` are exactly the tilts `tilt(q, G)` with `G`
constant on the cells of `𝒜`. For every behaviour `p` limited to `𝒜`, `E_p[F] = E_p[F̄]`.
(ii) **Best effort.** For every `t > 0`, among the behaviours limited to `𝒜`, the net value `J_t` of [P4] is maximized by
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
(iii) For `p` limited to `𝒜`, write `b̄ = E_q[b|𝒜]`. As in (i), `E_p[b] = E_p[b̄]`, and `log(p/q)` is `log(p(A)/q(A))` on
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

**Notes.** Since `Var_q(F) = Var_q(F̄) + Var_q(F − F̄)`, the coefficient in (iv) is `½·Var_q(F̄)·Var_q(F − F̄)/Var_q(F)`:
the product of what the actor can see and the share it cannot. Writing `θ` for the angle between `F̄` and `F` in the
Fisher metric at `q`, `cos²θ = Var_q(F̄)/Var_q(F)`, and the same expansion gives `KL(tilt(q, t·F̄)‖q) ≈ ½·t²·Var_q(F̄)`.
So at small effort `M ≈ sin²θ` times the departure: here, the misaligned share of the departure is `sin²θ`. (iii) is
the retention gap of main's B1, in closed form.

**Lineage.** main: B1 and NOTES §8 (retention, `G = E_q[F|ℋ]`, under the budget convention, where it rises with the
budget), ROADMAP §6 G2 (transmission and retention), and the I1 notes (the dynamic angle, `D_⊥ ≈ sin²θ·KL`, conjectured
there). New: the Jensen gap in closed form, the small-effort coefficient, and the counterexample to monotone growth: B1's
"rises with budget" does not carry over as a law.

## 5. Stakes and sensitivity

### D5 — Stakes
**Statement.** Under the standard specification of a non-constant objective `F`, let `p̂ ∈ Δ` and let `A` be the set of
outcomes where `F` is largest. The **matched intensity** of `p̂` is `λ = inf{t ≥ 0 : KL(p_{F,t}‖q) ≥ KL(p̂‖q)}`, with
`λ = ∞` when the set is empty; the **matched pursuit** is `p_{F,λ}`, with `p_{F,∞} = q(·|A)`. The **shortfall** of `p̂`
is `S(p̂) = E_{p_{F,λ}}[F] − E_{p̂}[F]`, in the units of `F`.

**In plain terms.** Stakes ask how much of the objective was actually lost. The actor is compared with the pursuit that
departs from the default by the same amount, and the shortfall is how much more of the objective that pursuit gets, in
the objective's own units.

**Why this choice.**
- *Misalignment is silent about stakes.* Misalignment does not change when the objective is rescaled (shown below), so it
  cannot say how much of the objective is lost; a principal needs that in its own units. On main this was learned the
  hard way (R8-1).
- *Compare at the same departure.* The departure is what the actor spent, and the matched pursuit is the most of `F`
  that departure can buy (shown below). Comparing with the nearest intended behaviour would say nothing: in the second
  case of [P5](iv) it reaches the same average of `F` by construction.
- *Not the best outcome.* Comparing with `max F` would charge every cautious actor for not being reckless, although the
  specification ([D3]) counts departing from the default as a cost.
- *Defined by an infimum,* so that the definition needs no result: the next item shows that the departure is matched
  exactly whenever `λ` is finite.

**Lineage.** main: Def 22 (the value shortfall `ΔV`), Thm 17(iii) (the same-budget counterfactual), and R8-1.

### P9 — What is at stake
**Statement.** Under the standard specification of a non-constant `F`, let `p̂ ∈ Δ`, with matched intensity `λ`, matched
pursuit `p_{F,λ}` and nearest intended behaviour `p°` ([P5](iv)).
(i) **The best use of the departure.** If `λ < ∞`, then `KL(p_{F,λ}‖q) = KL(p̂‖q)`, and `p_{F,λ}` has the largest
average of `F` among all behaviours whose departure is at most `KL(p̂‖q)`. If `λ = ∞`, then `S(p̂) = max F − E_{p̂}[F]`.
In both cases `S(p̂) ≥ 0`.
(ii) **Three causes.** If `0 < λ < ∞`, then
`λ·S(p̂) = M(p̂) + KL(p°‖p_{F,λ}) + λ·[E_q[F] − E_{p̂}[F]]⁺`:
misalignment, **under-pursuit** (pursuing at a lower intensity than the departure allows), and **anti-pursuit** (moving
against the objective).
(iii) **Units.** Replacing `F` by `a·F + c`, with `a > 0`, leaves `M(p̂)` unchanged and multiplies `S(p̂)` by `a`.
(iv) **Zero stakes.** `S(p̂) = 0` if and only if `p̂` is on the pursuit ray or puts all its mass on `A`. So
`M(p̂) = 0` implies `S(p̂) = 0`, and `S(p̂) = 0 < M(p̂)` exactly when `p̂` puts all its mass on `A` but splits it
differently from `q(·|A)`.

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
`KL(p̂‖p_{F,λ}) − KL(p̂‖p°) = E_{p̂}[log(p°/p_{F,λ})] = (t* − λ)·E_{p̂}[F] − Λ(t*) + Λ(λ) = E_{p°}[log(p°/p_{F,λ})]
= KL(p°‖p_{F,λ})`, and `E_{p̂}[F] > E_q[F]`. In the first case, `p° = q`, `M(p̂) = KL(p̂‖q)`, and
`KL(p̂‖p_{F,λ}) = KL(p̂‖q) − λ·E_{p̂}[F] + Λ(λ) = M(p̂) + KL(q‖p_{F,λ}) + λ·(E_q[F] − E_{p̂}[F])`, because
`KL(q‖p_{F,λ}) = −λ·E_q[F] + Λ(λ)`.
(iii) By [P1](ii), `tilt(q, t·(a·F + c)) = tilt(q, (t·a)·F)`, so the pursuit ray of `a·F + c` is the same set as that
of `F`, and `M(p̂)` is unchanged. The matched pursuit is the same behaviour, since it is the point of the same ray with the
same departure, so both averages are transformed by `v ↦ a·v + c`, and their difference is multiplied by `a`.
(iv) If `λ = 0`, then `p̂ = q`, on the ray. If `0 < λ < ∞`, then by (ii) `S(p̂) = KL(p̂‖p_{F,λ})/λ`, which is `0` exactly
when `p̂ = p_{F,λ}`, on the ray. If `λ = ∞`, then `S(p̂) = 0` exactly when `E_{p̂}[F] = max F`, that is, when `p̂` puts
all its mass on `A`; by [P5](iv) `M(p̂) = KL(p̂‖q(·|A))` there, which is `0` exactly when `p̂ = q(·|A)`. Finally, the closure of the ray in `Δ` is the ray together with `q(·|A)`: a sequence
on the ray either has bounded intensities, and then a subsequence converges to a point of the ray (as in the proof
of [P5](iv)), or has a subsequence with intensities tending to `∞`, which converges to `q(·|A)`. By [P5](ii),
`M(p̂) = 0` means that `p̂` is in that closure, and in both cases `S(p̂) = 0`.

**Checks.** checks/test_stakes.py::test_matched_pursuit_gets_the_most_from_the_departure,
checks/test_stakes.py::test_stakes_split_into_three_causes,
checks/test_stakes.py::test_rescaling_moves_stakes_not_misalignment, checks/test_stakes.py::test_zero_stakes

**Notes.** (ii) is main's three-term decomposition of the half-ray (transverse, axial and anti-alignment) read at the
matched intensity, with names for the causes. The matched intensity converts between the two units: `λ` nats per unit of
`F`. The checks compute KL between tilts in closed form, because at large `λ` the tilts underflow in float64.

**Lineage.** main: Def 22 and Thm 17(iii) (the shortfall at the same budget), Thm 13(b) (the three terms), Prop 16 and
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

**Proof.** First, for every `r ∈ Δ°`, `p ∈ Δ` and `h : X → ℝ`,
`KL(p‖tilt(r, h)) − KL(p‖r) = log E_r[e^h] − E_p[h]`, and both terms lie in `[min h, max h]`, so the difference lies in
`[−osc(h), osc(h)]`.
(i) Let `h = log(q'/q)`. By [P1](iii), `tilt(q', t·F) = tilt(tilt(q, h), t·F) = tilt(p_{F,t}, h)`, where `p_{F,t}` is the
pursuit from `q`. By the first step, `KL(p̂‖tilt(q', t·F))` and `KL(p̂‖p_{F,t})` differ by at most `osc(h)` for every
`t ≥ 0`, and so do their infima over `t ≥ 0`, which are the two misalignments.
(ii) Let `p_{F,t*}` be the nearest intended behaviour under `F`, so `M_{q,F}(p̂) = KL(p̂‖p_{F,t*})`. The pursuit of
`F + g` at intensity `t*` is `tilt(q, t*·(F + g)) = tilt(p_{F,t*}, t*·g)`, which is on the ray of `F + g`. By the first
step, `M_{q,F+g}(p̂) ≤ KL(p̂‖tilt(p_{F,t*}, t*·g)) ≤ M_{q,F}(p̂) + t*·osc(g)`.

**Checks.** checks/test_sensitivity.py::test_default_error_moves_misalignment_by_at_most_its_spread,
checks/test_sensitivity.py::test_objective_error_matters_in_proportion_to_intensity

**Notes.** Both bounds are worst cases. The first is nearly attained (a ratio above 0.9 in the check). Exchanging the
roles of `F` and `F + g` in (ii) gives the reverse bound with the revealed intensity under `F + g`. In the third case
of [P5](iv) the revealed intensity is infinite and (ii) says nothing: at the extreme of pursuit, a small error in the
objective can change the verdict entirely.

**Lineage.** New as statements. main: Prop 26 (a wrong default is measured misalignment unless it leans along the
target), and NOTES §2.3 (capacity switches the regime: errors matter more at high capacity).

## 6. Identifiability: what changes of behaviour reveal

A single behaviour reveals an objective only relative to a default ([P1]). Changes of behaviour reveal more: their
objective needs no default ([P2]), and whether it stays fixed is testable ([P3]). This section adds how much of a change
is misaligned, read from its first step ([P11]), what interventions reveal about how an actor responds ([P12]), and
how much of the objective a change gains ([P13]). Each item also says what cannot be revealed.

### P11 — The misaligned share at the start of a change
**Statement.** Let `F` be non-constant, and let `s ↦ p_s`, for `s ≥ 0`, be a twice continuously differentiable path in
`Δ°` with `p_0 = q`, whose revealed objective `G` at `s = 0` is non-constant. The **angle** `θ` between `G` and `F`
is given by `cos θ = Cov_q(G, F) / (Var_q(G)·Var_q(F))^{1/2}`. Under the standard specification of `F`, as `s → 0`,
`M(p_s)/KL(p_s‖q) → sin²θ` if `cos θ ≥ 0`, and `→ 1` if `cos θ < 0`. If `cos θ < 0`, then `M(p_s) = KL(p_s‖q)` for
every small enough `s > 0`.

**In plain terms.** Whenever a behaviour starts to move away from the default, the share of its departure that is
misaligned is set by one angle: the angle between the objective its change reveals and the declared objective, whose
cosine is the correlation of the two under the default. Moving straight along the objective is no misalignment; moving
at a right angle to it is all misalignment, and so is moving against it.

**Proof.** Since the path is twice continuously differentiable with `p_0 = q`, `p_s = tilt(q, a_s)` with
`a_s = s·G + O(s²)`. Expanding the log-normalizer `Λ(c) = log E_q[e^c]` to second order gives
`KL(tilt(q, a)‖tilt(q, b)) = ½·Var_q(a − b) + O(‖a‖³ + ‖b‖³)` for small `a`, `b`, so
`KL(p_s‖q) = ½·s²·Var_q(G) + O(s³)`, which is positive for small `s > 0`. Let
`ψ(s) = E_{p_s}[F] − E_q[F] = s·Cov_q(G, F) + O(s²)`.
If `cos θ < 0`, then `ψ(s) < 0` for small `s > 0`, and the first case of [P5](iv) gives `M(p_s) = KL(p_s‖q)`.
Otherwise, whenever `ψ(s) ≤ 0` the same case gives a share of `1`. When `ψ(s) > 0`, it is also below `max F − E_q[F]`
for small `s`, so the second case applies: `M(p_s) = KL(p_s‖p_{F,t*})` with `E_{p_{F,t*}}[F] = E_{p_s}[F]`. Since
`t ↦ E_{p_{F,t}}[F]` has derivative `Var_q(F) > 0` at `t = 0`, the inverse function theorem gives
`t* = ψ(s)/Var_q(F) + O(ψ(s)²) = s·ρ + O(s²)`, with `ρ = Cov_q(G, F)/Var_q(F)`. Then
`M(p_s) = ½·Var_q(s·G − t*·F) + O(s³) = ½·s²·Var_q(G − ρ·F) + O(s³)`, and
`Var_q(G − ρ·F) = Var_q(G) − Cov_q(G, F)²/Var_q(F) = Var_q(G)·sin²θ`. Dividing by `KL(p_s‖q)` gives `sin²θ` in the
limit. If `cos θ = 0`, then `ρ = 0` and `sin²θ = 1`, which agrees with the cases where `ψ(s) ≤ 0`.

**Checks.** checks/test_identifiability.py::test_initial_share_is_sin_squared

**Notes.** The angle needs only two things, both at the default: the first change of behaviour and the declared
objective. The actor's own objective is never needed. [P8](iv)'s small-effort law is the case `G = F̄`, where
`Cov_q(F̄, F) = Var_q(F̄)`. The curvature of the path does not affect the limit, and the convergence is first order in
`s` (the check uses curved paths).

**Lineage.** main: ROADMAP §6 I1 and NOTES §9 (the dynamic angle, `D_⊥ ≈ sin²θ·KL`, conjectured there), and Prop 22 (the
first-order effect of any smooth path). New: the statement and its proof, including the case against the objective.

### D6 — Intervention and pass-through
**Statement.** An **intervention** changes what the actor faces by a known non-constant function `u : X → ℝ`: an
incentive, a fine, or a change of the default option. With `p ∈ Δ°` the actor's behaviour before it and `p' ∈ Δ°` after,
the actor passes the intervention through, with **pass-through** `φ ∈ ℝ`, if `p' = tilt(p, φ·u)`.

**In plain terms.** An intervention is a known nudge added to the situation: a bonus for some outcomes, a fine for
others, or a different default option. The actor passes it through when its behaviour changes exactly by reweighting
with that nudge. The pass-through says how strongly it responds: zero ignores the nudge, a positive value follows it, and
a negative value means the nudge backfires.

**Why this choice.**
- *The simplest response that can fail.* Any change of behaviour is a reweighting by some function ([P1](i)). The claim
  that this function is a multiple of the intervention is testable, and the next item tests it. When it fails, more
  happened between the two behaviours than adding `u`: the intervention also changed what the actor pursues or where
  it starts from, or something else changed at the same time.
- *It needs no model of the actor.* The pass-through is defined from behaviour before and after; the actor's objective,
  default and intensity never appear. An actor that pursues `F̂` at intensity `t` from its own default (every behaviour
  can be written so, by [P1]), and adds `w·u` to `F̂`, has pass-through `φ = t·w` by [P1](iii); only that product is
  identified.
- *A change of default is an intervention too.* If the actor's own default is shifted by a known tilt `h` and its
  objective is unchanged, its behaviour moves to `tilt(p, h)` by [P1](iii): pass-through `1` for `u = h`.

**Lineage.** main: ROADMAP §6 I1 (instrument pass-through: regress the increments on the fine), Def 23's instruments slot,
made measurable, and T7-2d (a change of default that moved the evaluator).

### P12 — What interventions reveal
**Statement.** (i) **Pass-through is identified from behaviour alone.** Let `p, p' ∈ Δ°` be the behaviour before and
after an intervention `u`. The actor passes it through if and only if `log(p'/p) ∈ span{u, 1}`, and then the
pass-through is the coefficient of `u`. If `log(p'/p)` is not in `span{u, 1}`, no pass-through explains the change.
(ii) **Changes certify distinctions.** Let `𝒜` be a resolution and `s ↦ p_s` a continuously differentiable path in `Δ°`.
Every behaviour on the path splits each cell of `𝒜` in the same proportions as `p_0` if and only if every revealed
objective `F_s` is constant on the cells of `𝒜`. So a revealed objective that separates two outcomes of one cell shows
that their ratio moved; revealed objectives that never separate them do not show that the actor cannot tell them apart.

**In plain terms.** Whether an actor simply follows an incentive can be read from its behaviour before and after, without
knowing what it wants: the change must be a multiple of the incentive, apart from a constant, and that multiple is the
pass-through. If the change has any other shape, something more than the incentive moved it: the incentive changed what
the actor pursues or where it starts from, or something else changed at the same time. Likewise, a change that moves two
outcomes apart proves that the actor treats them differently; changes that never do prove nothing.

**Proof.** (i) If `p' = tilt(p, φ·u)`, then `log(p'/p) = φ·u − log E_p[e^{φu}]`, which is in `span{u, 1}`. Conversely,
if `log(p'/p) = φ·u + c`, then `p'` is proportional to `p·e^{φu}`, and normalization gives `p' = tilt(p, φ·u)`. Since `u`
is non-constant, `u` and `1` are linearly independent, so `φ` is determined.
(ii) If `p_s(·|A) = p_0(·|A)` for every cell `A` and every `s`, then for `x ∈ A`,
`log p_s(x) = log p_s(A) + log p_0(x|A)`, so `F_s(x) = ∂_s log p_s(A)` is the same for every `x ∈ A`. Conversely, if
every `F_s` is constant on each cell, then for `x` and `y` in one cell,
`∂_s log(p_s(x)/p_s(y)) = F_s(x) − F_s(y) = 0`, so every ratio inside a cell keeps its value at `s = 0`, and so does the
split. For the last sentence: the constant path `p_s = p_0` has `F_s = 0` for every actor, including one that tells
every outcome apart.

**Checks.** checks/test_identifiability.py::test_pass_through_is_identified_from_behaviour_alone,
checks/test_identifiability.py::test_revealed_objectives_certify_distinctions

**Notes.** (i) has no power with two outcomes: then `span{u, 1}` is every function, so every change passes the
intervention through, and an intervention that changed what the actor pursues shows only as a negative or a surprising
pass-through. Telling the two apart needs at least three outcomes, or several interventions. With estimated behaviours
the distance of `log(p'/p)` from `span{u, 1}` is never exactly zero; testing it needs an estimation item, which the
core does not have yet. (ii) bounds an actor's resolution from one side only. Observed changes show which distinctions its behaviour
makes; identifying its resolution needs interventions varied enough to move every distinction it could make. Together
with [P1], this is the ladder main proposed: a snapshot identifies an objective only given a declared default, changes
identify it up to a constant without one, and interventions identify how the actor responds.

**Lineage.** main: ROADMAP §6 I1 (the identifiability ladder: declare, measure, identify through interventions), B1
(identifying an actor's partition), and T7-2d. New: both statements.

### P13 — What the start of a change gains
**Statement.** Let `F` be non-constant, and let `s ↦ p_s`, for `s ≥ 0`, be a continuously differentiable path in `Δ°`
with revealed objectives `F_s`.
(i) **The average moves at the covariance rate.** For every `s`, `d/ds E_{p_s}[F] = Cov_{p_s}(F_s, F)`.
(ii) **At the start, the gain is set by the angle.** Let the path be as in [P11], with angle `θ`, and let
`σ_q(F) = Var_q(F)^{1/2}`. As `s → 0`,
`(E_{p_s}[F] − E_q[F]) / (2·KL(p_s‖q))^{1/2} → cos θ·σ_q(F)` and `S(p_s) / (2·KL(p_s‖q))^{1/2} → (1 − cos θ)·σ_q(F)`,
where `S` is the shortfall of [D5].

**In plain terms.** As behaviour changes, the average of any objective moves at a rate equal to the covariance, under
the current behaviour, between that objective and the objective the change reveals. At the start of a change away from
the default, each unit of departure gains the objective's spread times the cosine of the angle of [P11]. Pursuing the
objective itself, with the same departure, gains the full spread, so the shortfall is the rest: one minus the cosine,
times the spread. No change gains more per unit of departure at the start than pursuit of the objective, and a change
against the objective loses.

**Proof.** (i) By [P2], `∂_s p_s(x) = p_s(x)·F_s(x)`, so `d/ds E_{p_s}[F] = Σ_x p_s(x)·F_s(x)·F(x) = E_{p_s}[F_s·F]`.
Since `Σ_x p_s(x) = 1` for every `s`, `E_{p_s}[F_s] = Σ_x ∂_s p_s(x) = 0`, so `E_{p_s}[F_s·F] = Cov_{p_s}(F_s, F)`.
(ii) Write `G = F_0` and `ε(s) = (2·KL(p_s‖q))^{1/2}`. The proof of [P11] gives `KL(p_s‖q) = ½·s²·Var_q(G) + O(s³)`, so
`ε(s) = s·σ_q(G)·(1 + O(s))`. By (i) and Taylor's theorem, `E_{p_s}[F] − E_q[F] = s·Cov_q(G, F) + O(s²)`. Dividing,
the first ratio tends to `Cov_q(G, F)/σ_q(G) = cos θ·σ_q(F)`.
For the shortfall, let `A` be the set where `F` is largest. Along the ray, `d(t) = KL(p_{F,t}‖q)
= t·E_{p_{F,t}}[F] − log E_q[e^{tF}]` is continuous and `0` at `t = 0`. The ray's revealed objective is
`F − E_{p_{F,t}}[F]`, so (i) gives `d/dt E_{p_{F,t}}[F] = Var_{p_{F,t}}(F)`, and `d'(t) = t·Var_{p_{F,t}}(F) > 0` for
`t > 0`: `d` is increasing. Its limit as
`t → ∞` is `KL(q(·|A)‖q) = −log q(A) > 0`, since `F` is non-constant. So for small `s`, the matched intensity `λ` of
[D5] is finite, `d(λ) = KL(p_s‖q)`, and `λ → 0` as `s → 0`. The same second-order expansion applied to the ray gives
`d(λ) = ½·λ²·Var_q(F) + O(λ³)`, so `λ·σ_q(F) = ε(s)·(1 + O(λ))`, and `λ = O(s)`. By (i) on the ray,
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

**Lineage.** main: ROADMAP §6 I1 (the dynamic angle) and Def 22 (the value shortfall). New: both statements.

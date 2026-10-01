# The core

> **Status: v8, in progress.** Sections 1–4: behaviours, pursuit, the specification, and resolution. Each item carries a formal
> statement and a plain-terms twin. A definition says why this choice; a result carries a proof and checks that run in
> CI. Every item gives its lineage from the archive on `main`. The format is in `README.md`.

## 0. What the core does

Alignment compares what an actor does with what a principal intended. The core makes that comparison precise in four
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

The core assumes nothing about how the actor produces its behaviour.

**How to read.** Items are numbered by kind: D for definitions, P for propositions. A statement, justification or proof
uses only items above it. `[P2](iii)` means part (iii) of P2. Logarithms are natural, so divergences are in nats.
Operations on functions (`p/r`, `log`, `e^F`) act outcome by outcome. The Notes of each item give the names its objects
carry in other fields.

| Symbol | Meaning | Introduced in |
|---|---|---|
| `X` | the outcomes | [D1] |
| `Δ`, `Δ°` | all behaviours; the full-support ones | [D1] |
| `E_p[F]`, `Var_p(F)` | average and variance of `F` under `p` | [D1] |
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

## 1. Behaviours and tilts

### D1 — Outcomes, behaviours, divergence and tilt
**Statement.** `X` is a finite set of **outcomes**, with at least two elements. A **behaviour** is a probability
distribution `p` on `X`. `Δ` is the set of behaviours, and `Δ°` the set of **full-support** behaviours, those with
`p(x) > 0` for every `x`. For `p ∈ Δ` and `F : X → ℝ`, `E_p[F] = Σ_x p(x)·F(x)` and
`Var_p(F) = E_p[F²] − E_p[F]²`; for a set `C ⊆ X` with `p(C) > 0`, `p(·|C)` is `p` conditioned on `C`. For `p, r ∈ Δ`,
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

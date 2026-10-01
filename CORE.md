# The core

> **Status: v9, in progress.** The core holds what cannot be derived: five premises, and the definitions that the whole
> framework uses. Everything that follows from them is in `derived/`, with proofs and checks that run in CI. Each item
> carries a formal statement and a plain-terms twin, and gives its lineage from the archive on `main`. The format is in
> `README.md`.

## 0. What the core is

Alignment compares what an actor does with what a principal intended. The core fixes the terms of that comparison and
the few premises it rests on. Section 1 states the premises. Sections 2–8 give the definitions, each with the reasons
for it. The results, which follow from these by proofs, are in `derived/`, whose `README.md` gives their reading order.
A definition may cite a result to justify itself, provided that no chain of dependencies leads back to it.

The framework in eight steps:
1. **Premises** (section 1). Alignment is judged from behaviour in every condition; pursuit is the steepest climb, and
   the best trade-off; misalignment is value lost; specifications are declared before they judge.
2. **Behaviour and pursuit** (section 2). Behaviour is a distribution over outcomes. Pursuing an objective reweights a
   default toward it. Derived: nothing is lost by this description, pursuit is the steepest climb, and the cost of
   departing from the default can only be the KL divergence (`derived/tilts-and-paths.md`, `derived/value.md`).
3. **Specification and misalignment** (section 3). The principal declares a default and the behaviours it accepts.
   Misalignment is the KL divergence from the actual behaviour to the nearest acceptable one. Derived: when it is zero,
   its closed forms for "pursue `F`", and the split of the departure (`derived/misalignment.md`).
4. **Resolution** (section 4). Distinctions the principal does not care about, and distinctions the actor cannot make
   (`derived/resolution.md`).
5. **Stakes** (section 5). How much of the objective is lost, in its own units (`derived/stakes.md`).
6. **Interventions** (section 6). Known changes of what the actor faces, and how strongly the actor follows them
   (`derived/identifiability.md`).
7. **Feasibility** (section 7). What the actor can do. Derived: misalignment splits into what the actor could have
   avoided and what it could not (`derived/feasibility.md`).
8. **Conditions, views and identification** (section 8). The situations the actor faces, what it can perceive of them,
   and what observation determines. Derived: an actor cannot behave more differently in two situations than it can tell
   them apart, which bounds what it can hide when it is not observed (`derived/identifiability.md`).

**In scope.** One principal and one actor; finitely many outcomes; behaviour in each of finitely many conditions; any
declared set of acceptable behaviours, with closed forms for "pursue `F`"; what the actor cannot distinguish, cannot do,
or cannot perceive; and what observation identifies, including misalignment that an actor shows only when it is not
observed.

**Out of scope**, stated so that no result is read as covering it:
- *Internal states.* The core judges behaviour ([A1]). Two actors that behave alike in every condition are the same
  actor for the core, whatever their internal goals. An actor that behaves differently when it is not observed is in
  scope: its misalignment in unobserved conditions is a quantity with an identified set ([D9]).
- *Several actors*, and actors that respond to the measurement itself in ways not captured by a stated view and fixed
  interventions.
- *Aggregating several principals.* The core takes one specification at a time; unions and intersections of intended
  sets are specifications too, but weighing principals against each other is not defined.
- *Continuous outcomes.* Deferred. The results are expected to carry over with integrability conditions; none is
  claimed.
- *Estimation from finite samples.* Not yet in the framework (`NOTES.md`).
- *Which objective is right.* The principal declares it; the core does not choose it.
- *Explanations.* Why an actor behaves as it does is not measured.

**How to read.** Items are numbered by kind: A for premises and D for definitions, in this file; P for propositions, in
`derived/`. `[P2](iii)` means part (iii) of P2. Logarithms are natural, so divergences are in nats. Operations on
functions (`p/r`, `log`, `e^F`) act outcome by outcome. The Notes of each item give the names its objects carry in other
fields.

| Symbol | Meaning | Introduced in |
|---|---|---|
| `X` | the outcomes | [D1] |
| `Δ`, `Δ°` | all behaviours; the full-support ones | [D1] |
| `E_p[F]`, `Var_p(F)`, `Cov_p(F, G)` | average, variance and covariance under `p` | [D1] |
| `KL(p‖r)` | the Kullback–Leibler divergence, in nats | [D1] |
| `tilt(r, F)` | `r` reweighted by `e^F` | [D1] |
| `q`, `F`, `t` | the default, an objective, an intensity | [D2] |
| `p_{F,t}`, `R_F` | pursuit of `F` at intensity `t`; the pursuit ray | [D2] |
| `(q, 𝓘)` | a specification, declared by the principal: the default and the intended behaviours | [D3] |
| `M(p̂)` | the misalignment of the actual behaviour `p̂` | [D3] |
| `ℬ`, `𝒜` | the principal's resolution; the actor's resolution | [D4] |
| `E_q[F\|𝒜]`, `F̄` | the cell average of `F` under the default | [D4] |
| `λ`, `S(p̂)` | the matched intensity; the shortfall, in the units of `F` | [D5] |
| `u`, `φ` | an intervention; the pass-through | [D6] |
| `𝓕` | the actor's feasible set | [D7] |
| `𝒞`, `(p_c)` | the conditions; the actor's response | [D8] |
| `Z`, `V_c` | the actor's view: its signals, and their distribution in condition `c` | [D8] |
| `O` | the observed conditions | [D9] |
| `s`, `F_s` | time along a path of behaviours; the objective the change reveals | [P2] |
| `J_t` | net value: the objective's average minus the cost of departing from the default | [P4] |
| `t*`, `p°` | the revealed intensity; the nearest intended behaviour | [P5] |
| `KL(p̂‖q)` | the departure of the actual behaviour from the default | [P6] |
| `θ` | the angle between a revealed objective and the declared one | [P11] |
| `σ_q(F)` | the spread of `F` under the default: `Var_q(F)^{1/2}` | [P13] |
| `p*` | the best feasible behaviour | [P15] |

## 1. Premises

### A1 — Behaviour suffices
**Statement.** What an actor does is described by how often each of finitely many outcomes occurs, in each condition it
may face. Alignment is judged from that description alone, never from how the behaviour is produced.

**In plain terms.** We judge what the actor does, in every situation it may meet, and not what goes on inside it.

**Why this choice.**
- *It can be observed.* Behaviour can be counted. Internal goals and mechanisms differ across AI systems, people,
  institutions and organisms, and are often out of reach. A premise about behaviour applies to all four.
- *In every condition, not in one.* Judging a single behaviour would miss an actor that behaves well when it is
  observed and badly otherwise. Requiring behaviour in every condition keeps such deceptive alignment inside the
  framework, as misalignment in conditions that are not observed (section 8).
- *Finitely many outcomes.* Every statement can then be proved with finite sums and checked exactly on random
  instances. General outcome spaces are out of scope for now.
- *What it costs.* Two actors that behave alike in every condition are the same actor for the core, whatever their
  internal goals. That is deliberate: a difference that shows in no condition has no consequence a principal could
  suffer.

**Lineage.** main: R7-1 (the actual behaviour is any distribution, Def 13). v8: [D1]'s "why", where this was an
argument.
New: behaviour in every condition, so that deceptive alignment is in scope.

### A2 — Pursuit is the steepest climb
**Statement.** To pursue an objective is to raise its average as steeply as possible, with steepness measured in a
geometry on behaviours that does not change when outcomes are split into finer outcomes in fixed proportions.

**In plain terms.** Wanting more of something means moving toward it by the most direct route, and what counts as most
direct must not depend on how finely we describe what happens.

**Why this choice.**
- *Description-independence is the least we can ask.* Two observers who describe the same events at different
  granularity must agree on what pursuing an objective means.
- *It is enough.* By Čencov's theorem [@cencov1982] it fixes the geometry, up to a constant factor, and with it the form
  of pursuit,
  a reweighting of the default (section 2 and `derived/tilts-and-paths.md`).

**Lineage.** main: Def 1 (the Gibbs tilt as the form of intended behaviour, assumed there). v8: [D2]'s "why", where this
was the one premise.

### A3 — Pursuit is the best trade-off
**Statement.** To pursue an objective at an intensity is to choose the behaviour with the largest average of the
objective minus a cost of departing from the default, priced at the reciprocal of the intensity. With the default
fixed, the cost depends only on the behaviour, and is differentiable.

**In plain terms.** Pursuing harder means accepting more cost of change for more of what is pursued. The cost of change
depends only on how the behaviour changes, not on what is pursued.

**Why this choice.**
- *It says what intensity means.* The reciprocal of the intensity is the price of one nat of departure, in the
  objective's units: an actor that pursues intensely treats departure as cheap.
- *Together with A2 it fixes the cost.* The steepest climb is also the best trade-off for exactly one cost: the KL
  divergence from the default (`derived/value.md`). A2 is a geometric premise and A3 an economic one; they agree in one
  way only.

**Lineage.** main: Def 2 (the bounded actor, with the KL cost assumed) and Thm 1. New: the cost is derived, not assumed.

### A4 — Misalignment is value lost
**Statement.** The misalignment of a behaviour is the least value it loses against a behaviour the principal accepts,
each accepted behaviour judged by its own objective at its own intensity, with value counted in nats: the objective's
units times the intensity.

**In plain terms.** Misalignment is how much worse the actor did than the closest acceptable way of acting, judged by
the standard of that acceptable way.

**Why this choice.**
- *The benefit of the doubt.* The least loss over the acceptable behaviours charges the actor only for what no
  acceptable behaviour explains.
- *Each by its own objective.* Every full-support behaviour is the best trade-off for some objective, so judging an
  accepted behaviour by its own objective needs no further choice.
- *In nats.* A behaviour can be written with an objective and an intensity in many ways; only their product is fixed.
  Value times intensity does not depend on the choice.

**Lineage.** v8: [D3]'s "why" (KL, with the actual behaviour first), where this was an argument. main: Thm 1 (regret is
a divergence).

### A5 — Declared before
**Statement.** The default and the acceptable behaviours are fixed before, and without using, the behaviour they will
judge.

**In plain terms.** Decide what counts as acceptable before looking at what the actor did.

**Why this choice.** A default or an acceptable set fitted to the behaviour being judged removes exactly the
differences the judgement needs. On main, I1-dyn fitted its default (a Hardy–Weinberg expectation) from the counts it
judged, and its test could not fail. Pre-registration in science makes the same demand.

**Lineage.** main: Def 23's timing slot. v8: [D3]'s rule of use.

## 2. Behaviour and pursuit

### D1 — Outcomes, behaviours, divergence and tilt
**Statement.** `X` is a finite set of **outcomes**, with at least two elements. A **behaviour** is a probability
distribution `p` on `X`. `Δ` is the set of behaviours, and `Δ°` the set of **full-support** behaviours, those with
`p(x) > 0` for every `x`. For `p ∈ Δ` and `F : X → ℝ`, `E_p[F] = Σ_x p(x)·F(x)` and
`Var_p(F) = E_p[F²] − E_p[F]²`, and `Cov_p(F, G) = E_p[F·G] − E_p[F]·E_p[G]`; for a set `C ⊆ X` with `p(C) > 0`,
`p(·|C)` is `p` conditioned on `C`. For `p, r ∈ Δ`,
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
- *Behaviour is any distribution* ([A1]). No model of how an actor produces its behaviour is assumed. The core measures
  behaviour; explanations are not part of it.
- *KL and the tilt are notation here.* The items that use them argue that they are the right tools.

**Notes.** A behaviour is a policy in reinforcement learning, a mixed strategy in game theory, a distribution of choices
in economics, and a distribution of types in a population in biology. The tilt is exponential tilting in statistics.

**Lineage.** main: Def 1 (the objects), and R7-1's rule that the actual behaviour is any distribution (Def 13). main's
R7-8 (measurable spaces) stays deferred, as it was there.

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
  stays fixed, which a derived result makes testable (`derived/tilts-and-paths.md`). Mixing a behaviour with another,
  for example, generally gives a path whose objective turns, as that result's check shows; cut-offs that exclude
  outcomes leave `Δ°` altogether.
- *It is canonical, given [A2].* Pursuing `F` means climbing `E_p[F]` as steeply as possible, in a Riemannian geometry
  on behaviours that is unchanged when outcomes are split into sub-outcomes in fixed proportions. Up to a constant
  factor, the Fisher metric is the only such geometry, across outcome spaces of every size (Čencov's theorem
  [@cencov1982]; [@campbell1986]). In the Fisher metric the steepest climb is the replicator field
  ([P2](ii)), and its flow from `q` is `tilt(q, s·F)` ([P2](iii)). A constant factor in the metric only rescales time,
  so the ray is the same. A notion of pursuit that must not depend on how finely outcomes are described is therefore
  led to this ray.
- *The ray needs a default; the path does not.* The same objective pursued from two defaults gives two different rays,
  so the specification of section 3 fixes the default. Whether a path pursues `F` needs no default at all, which is why
  derived results can read pursuit from changes of behaviour without declaring one.

**Notes.** Names in other fields. The default is the reference policy of RL fine-tuning, the prior of KL control, the
base measure of an exponential family, the status quo of behavioural economics, and the population before selection
in biology. The objective is a reward, a utility, or a log-fitness. The pursuit `p_{F,t}` is the optimum of
KL-regularized
reward maximization with coefficient `1/t` in RL fine-tuning, for one prompt (across prompts, which the policy does
not choose, the optimum reweights each prompt's responses separately, which is not a pursuit on prompt–response pairs);
with a uniform default it is the logit choice rule, or quantal response, with rationality `t` [@mckelvey1995]; and it
is the result of `t` generations of constant selection with fitness `e^F`, for types that are passed on intact, as in
clonal reproduction. The intensity is an inverse temperature in physics, and "optimization pressure" in AI safety.

**Lineage.** main: Def 1 (the Gibbs tilt `p_{G,t}`, with `q` there called the reference), Def 2 (the bounded actor,
whose optimum is the tilt: here a property, [P4](i)), Prop 15 (the carrier), and Prop 16 (g4) (the half-ray). The ray
defines intended pursuit; it is not a model of the actor. main's rows 67–68 and 76–78 filed results by the intended
actor's model instead of by what their proofs need, and the core keeps the two apart by construction.

## 3. The specification and misalignment

### D3 — Specification, declaration and misalignment
**Statement.** A **specification** is a pair `(q, 𝓘)`: a default `q ∈ Δ°`, and a non-empty set `𝓘 ⊆ Δ°` of
**intended behaviours**, closed in `Δ°`. The **misalignment** of a behaviour `p̂ ∈ Δ` is
`M(p̂) = inf_{p ∈ 𝓘} KL(p̂‖p)`. The **standard specification** of an objective `F` is `(q, R_F)`: pursuit of `F` from
`q` at every intensity, including none.
A specification is **declared** when it is fixed as [A5] requires: before, and without using, the behaviour it will
judge.

**In plain terms.** Before looking at what the actor does, the principal states a default behaviour and the set of
behaviours it would accept. Misalignment is how far the actual behaviour is from the nearest acceptable one, in nats.
When the request is "pursue this objective", every intensity of pursuing it is acceptable, including none: an actor
that stays at the default is not misaligned, though it may be useless, which is a different failure.

**Why this choice.**
- *The formula is forced.* By [A3], pursuit is the best trade-off between an objective and a cost of departing from
  the default, and by [P14] that cost can only be KL. Each intended behaviour `p` is then the best trade-off for its own
  objective, `log(p/q)` at intensity 1 ([P4](ii)), and `KL(p̂‖p)` is exactly the net value, in nats, that `p̂` loses
  against it. [A4] takes the least such loss over the acceptable behaviours: that is `M(p̂)`, including the order of
  the arguments. The cost term is
  what makes the reading general: without it, the only fully intended behaviours of an objective would be those on its
  best outcomes, and every behaviour that puts any mass elsewhere would be charged.
- *What the number means.* If the actor behaves as `p̂` and `p` is intended, each independent decision adds on average
  `KL(p̂‖p)` nats to the log-likelihood ratio in favour of `p̂` over `p`. So `M(p̂)` is the slowest rate at which an
  observer gathers evidence that the actor is not behaving as intended: about `1/M(p̂)` decisions give one nat, odds of
  about `e` to 1.
- *The direction charges the unintended.* `KL(p̂‖p)` is large when the actor often does what `p` rarely does, and
  comparatively small when the actor merely does less of what `p` does. Doing the unintended costs more than leaving the
  intended undone.
- *The nearest acceptable behaviour.* Taking the minimum gives the actor the benefit of the doubt: it is charged only
  for what no acceptable behaviour explains.
- *Grouping only hides.* By [P4](iii) and (iv), the score splits along groupings of outcomes, and grouping can only hide
  misalignment. Section 4 uses this for resolutions.
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
- *Stakes are reported separately.* Misalignment in nats says nothing about how much of `F` is at stake. Section 5
  reports the shortfall in `F`'s own units (main: Def 22 and R8-1, where this lesson was learned).
- *Slim on purpose.* main's declaration (Def 23, the same object under its old name) had nine slots. Only four changed
  the measure, and all four are ways of
  generating `𝓘`. Rules, instruments, feasibility and the environment did not enter the measure, so they are not
  part of the specification. Instruments return as interventions (section 6), and feasibility as a property of the
  actor (section 7), where it splits misalignment instead of changing it. The default enters the measure through `𝓘`
  (the pursuit ray starts at `q`), and other definitions use it directly. A slot is added only with a case where it
  changes a verdict, and with the value it takes when nothing is declared.

**Notes.** The principal declares; what it declares is the specification, the word AI safety and formal verification use
for the set of acceptable behaviours. Misalignment is then a quantitative distance from the specification. The direction
of KL used here is the one called zero-forcing in variational inference. That the standard specification is a
specification, that is, that the pursuit ray is closed in `Δ°`, is shown in [P5](iv); for a constant `F` the ray is the
single point `q`, which is closed.

**Lineage.** main: Def 19 and Prop 34 (the declared intended set), Def 17 (the free convention's half-ray), Def 23 (the
declaration, slimmed; its timing slot becomes the rule of use), and row 74. New: behaviours that rule outcomes out are
scored.

## 4. Resolution: what each side distinguishes

### D4 — Resolution
**Statement.** A **resolution** is a partition `𝒢` of `X` into non-empty **cells**. A function is constant on cells if
it
takes one value on each cell. For `p ∈ Δ`, `p_𝒢` is the distribution of the cell masses `p(C)`. For `q ∈ Δ°` and
`F : X → ℝ`, the **cell average** `E_q[F|𝒢]` is the function equal, on each cell `C`, to `E_{q(·|C)}[F]`. Resolutions
are used in two positions.
- A specification `(q, 𝓘)` is **stated at resolution** `ℬ` if `𝓘 = {p ∈ Δ° : p_ℬ ∈ 𝓘_ℬ}` for a non-empty set `𝓘_ℬ`
  of full-support distributions on the cells, closed in the set of all full-support distributions on the cells. The
  principal is then **indifferent** inside the cells of `ℬ`. For an objective `F` constant on the cells of `ℬ`,
  the **standard specification at resolution** `ℬ` takes
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
  describe, which are common knowledge in Aumann's sense [@aumann1976]. Misalignment computed there is a lower bound
  both
  can verify ([P4](iv)), but it is blind to every gap between the two resolutions, so it is not the score.

**Notes.** The actor's position is a case of feasibility: the behaviours limited to `𝒜` form a linear feasible set
([D7]). In reinforcement learning, an actor's resolution is a state abstraction, and outcomes it cannot tell apart
are aliased. A principal's resolution is a coarse-graining of the outcomes.

**Lineage.** main: Def 21 (the declared resolution: the principal's position), B1 and NOTES H14 (one object in several
positions; retention), and ROADMAP §6 G1, G2 and G4. New: the actor's position as a definition, with the default
deciding
inside cells.

## 5. Stakes

### D5 — Stakes
**Statement.** Under the standard specification of a non-constant objective `F`, let `p̂ ∈ Δ` and let `A` be the set of
outcomes where `F` is largest. The **matched intensity** of `p̂` is `λ = inf{t ≥ 0 : KL(p_{F,t}‖q) ≥ KL(p̂‖q)}`, with
`λ = ∞` when the set is empty; the **matched pursuit** is `p_{F,λ}`, with `p_{F,∞} = q(·|A)`. The **shortfall** of `p̂`
is `S(p̂) = E_{p_{F,λ}}[F] − E_{p̂}[F]`, in the units of `F`.

**In plain terms.** Stakes ask how much of the objective was actually lost. The actor is compared with the pursuit that
departs from the default by the same amount, and the shortfall is how much more of the objective that pursuit gets, in
the objective's own units.

**Why this choice.**
- *Misalignment is silent about stakes.* Misalignment does not change when the objective is rescaled
  (`derived/stakes.md`), so it
  cannot say how much of the objective is lost; a principal needs that in its own units. On main this was learned the
  hard way (R8-1).
- *Compare at the same departure.* The departure is what the actor spent, and the matched pursuit is the most of `F`
  that departure can buy (`derived/stakes.md`). Comparing with the nearest intended behaviour would say nothing: in the
  second
  case of [P5](iv) it reaches the same average of `F` by construction.
- *Not the best outcome.* Comparing with `max F` would charge every cautious actor for not being reckless, although the
  specification ([D3]) counts departing from the default as a cost.
- *Defined by an infimum,* so that the definition needs no result: a derived result shows that the departure is matched
  exactly whenever `λ` is finite.

**Lineage.** main: Def 22 (the value shortfall `ΔV`), Thm 17(iii) (the same-budget counterfactual), and R8-1.

## 6. Interventions

### D6 — Intervention and pass-through
**Statement.** An **intervention** changes what the actor faces by a known non-constant function `u : X → ℝ`: an
incentive, a fine, or a known shift of the actor's own default. With `p ∈ Δ°` the actor's behaviour before it and
`p' ∈ Δ°` after,
the actor passes the intervention through, with **pass-through** `φ ∈ ℝ`, if `p' = tilt(p, φ·u)`.

**In plain terms.** An intervention is a known nudge added to the situation: a bonus for some outcomes, a fine for
others, or a shift in what the actor would do by default. The actor passes it through when its behaviour changes exactly
by reweighting
with that nudge. The pass-through says how strongly it responds: zero ignores the nudge, a positive value follows it,
and
a negative value means the nudge backfires.

**Why this choice.**
- *The simplest response that can fail.* Any change of behaviour is a reweighting by some function ([P1](i)). The claim
  that this function is a multiple of the intervention is testable, and a derived result tests it
  (`derived/identifiability.md`). When it fails, more
  happened between the two behaviours than adding `u`: the intervention also changed what the actor pursues or where
  it starts from, or something else changed at the same time.
- *It needs no model of the actor.* The pass-through is defined from behaviour before and after; the actor's objective,
  default and intensity never appear. An actor that pursues `F̂` at intensity `t` from its own default (every behaviour
  can be written so, by [P1]), and adds `w·u` to `F̂`, has pass-through `φ = t·w` by [P1](iii); only that product is
  identified.
- *A change of default is an intervention too.* If the actor's own default is shifted by a known tilt `h` and its
  objective is unchanged, its behaviour moves to `tilt(p, h)` by [P1](iii): pass-through `1` for `u = h`.

**Lineage.** main: ROADMAP §6 I1 (instrument pass-through: regress the increments on the fine), Def 23's instruments
slot,
made measurable, and T7-2d (a change of default that moved the evaluator).

## 7. Feasibility

### D7 — Feasibility
**Statement.** The actor's **feasible set** is a non-empty closed set `𝓕 ⊆ Δ`: the behaviours it can produce. It is
**linear** if it is the set of behaviours whose averages of given functions take given values,
`𝓕 = {p ∈ Δ : E_p[f_i] = a_i for i = 1, …, m}`, for functions `f_i : X → ℝ` and numbers `a_i`. When nothing is known
about what the actor can do, `𝓕 = Δ`.

**In plain terms.** The feasible set is what the actor can do. It is linear when the actor's limits take the form "these
averages cannot change": how often each situation arises, how the actor splits outcomes it cannot tell apart, how the
environment responds to what the actor does.

**Why this choice.**
- *It separates "cannot" from "will not".* Misalignment ([D3]) judges what the actor did; the feasible set says what it
  could have done. Without it, an actor is charged alike for what it chose and for what no behaviour in its reach could
  avoid.
- *Linear limits are the natural class.* Three limits met in practice are linear: situations whose frequencies the actor
  does not choose (fixed masses of groups of outcomes), outcomes the actor cannot tell apart ([D4]: fixed ratios inside
  cells), and acting in an environment whose responses are fixed (fixed transition probabilities). For linear limits the
  split of misalignment into an avoidable and an unavoidable part is exact, and it is at once Csiszár's Pythagorean
  theorem and an exact accounting of net value (`derived/feasibility.md`). Convex limits give only an inequality, and
  limits of capacity, such as a parametric family, give none.
- *Closed,* so that a best feasible behaviour exists.
- *Everything, when nothing is known.* Then no misalignment is excused as unavoidable, as the finest resolution is the
  default in [D4]. Excusing requires a stated limit.

**Notes.** In reinforcement learning the feasible set of a policy acting in a fixed environment is the set of trajectory
distributions it can induce; in economics, a budget or technology set; in biology, the genotypes and frequencies that
inheritance allows. In control theory the question "which behaviours can the actor reach" is controllability.

**Lineage.** main: Def 23's feasibility slot, dropped in v8 because it did not change the measure; it returns because it
splits the measure. main: B1 and ROADMAP §6 G2 (retention). New: the definition, and linearity as the class for which
the split is exact.

## 8. Conditions, views and identification

### D8 — Conditions, responses and views
**Statement.** A **condition** is a situation in which the actor may act; `𝒞` is a finite set of conditions. The
actor's **response** is the family `(p_c)_{c ∈ 𝒞}` of its behaviours, one in each condition. A **view** is a finite set
`Z` of signals and, for each condition `c`, a distribution `V_c` on `Z`: what the actor perceives in condition `c`. The
response **depends on the condition only through the view** if there are behaviours `π_z`, for `z ∈ Z`, with
`p_c = Σ_z V_c(z)·π_z` for every condition `c`. When nothing is known about the actor's perception, the view is exact:
`Z = 𝒞`, and each condition is perceived as itself.

**In plain terms.** Conditions are the situations the actor may face: a prompt, a client, a test, or real use. The
response collects what the actor does in each. The view describes what the actor can perceive of its situation. An actor
whose response depends only on its view must act alike in situations it perceives alike, and can act differently only
where it perceives a difference.

**Why this choice.**
- *[A1] judges behaviour in every condition.* A single behaviour is the case of one condition. Situations whose
  frequencies the actor does not choose, such as prompts or arriving patients, are conditions: a response weighted by
  those frequencies is a behaviour on condition–outcome pairs with fixed condition masses, a linear feasible set
  ([D7]).
- *The view makes "cannot tell apart" a quantity.* [D4]'s actor resolution limits what the actor can do with outcomes;
  a view limits what it can perceive of conditions. A view that gives each condition a single signal is a partition of
  the conditions; a random view says by how much two conditions can be told apart.
- *Deceptive alignment needs a view.* An actor that behaves well when it is observed and badly otherwise must perceive
  whether it is observed. A derived result bounds what it can hide by how well its view separates the two
  (`derived/identifiability.md`).
- *The exact view, when nothing is known,* assumes nothing about the actor's perception, and excuses nothing.

**Notes.** In control theory the response is an input–output map and the view is the actor's observation of its input;
here observability runs from the condition to the actor. In reinforcement learning the conditions are states or prompts
and the response is the policy. In statistics, a response that depends on the condition only through a view is a
Markov kernel composed with a channel.

**Lineage.** New. main: ROADMAP §6 I1 (identification through interventions) and the brainstorm's point on
identifiability dynamics. The ontologies' "contexts" (v8, `NOTES.md`) are conditions with fixed frequencies.

### D9 — Observation and identification
**Statement.** The principal observes the response in a set `O ⊆ 𝒞` of **observed conditions**. Let `𝓡` be the set of
responses that satisfy stated assumptions, such as a feasible set in each condition ([D7]) or a view ([D8]). A quantity
defined from the response is **identified** if every response in `𝓡` that agrees with the observed behaviours `p_c`,
for `c ∈ O`, gives it the same value. Otherwise the set of values that those responses give is its **identified set**.

**In plain terms.** The principal watches the actor only in some situations. A quantity is identified when everything
that fits what was watched, and what is assumed, gives it one value. Otherwise the honest report is the range of values
it could take.

**Why this choice.**
- *It reports what the evidence and the assumptions determine, and no more.* This is partial identification
  [@manski2003]. A report that gives one number for a quantity that is not identified hides an assumption.
- *It makes deceptive alignment measurable.* Misalignment in a condition that is not observed has an identified set.
  With no assumption it can be anything; a view narrows it, and an exact view of indistinguishable conditions makes it
  identified (`derived/identifiability.md`).
- *It is why interventions belong to the core.* An intervention ([D6]) is a designed change of condition. It adds
  observed conditions, chosen so that what the principal needs, such as the pass-through, is identified.
- *Every report states it.* The reporting standard (`STANDARD.md`) asks, for each reported quantity, whether it is
  identified, and under which assumptions.

**Notes.** In econometrics this is identification, and partial identification when only a set is determined; in control
theory, identifiability of a system from input–output data, which needs inputs varied enough (persistent excitation).

**Lineage.** New. main: ROADMAP §6 I1 (the ladder: declare, measure, identify through interventions).

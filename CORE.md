# The core

> **Status: v13, on branch `claude/core-reframe`, approved by the PI (Q52); `main` holds v12 until it is merged.** The
> core holds what the framework takes from outside and what it cannot derive: three imported axioms of probability,
> four background conditions assumed without loss of generality, three premises, and the definitions the whole
> framework uses, each with the interpretation it declares. Everything that follows from them is in `derived/`, with
> proofs and checks that run in CI. The format is in `README.md`.

## 0. What the core is

Alignment compares what an actor does with what a principal intended. The core fixes the terms of that comparison, and
says of each starting point what kind of starting point it is.

**How the core is built.** It follows the method of reverse physics [@carcassi2022], [@carcassi2026]: separate what a
theory takes from mathematics from what it assumes about the world, say of each assumption what kind it is, and map
every mathematical object to what it stands for, declaring the map and justifying it, so that only objects with a
meaning in the world enter. The core has four kinds of item, and a table of the conventions they use.
- **Imported axioms** (M): mathematics taken as it is, from probability theory. They assume nothing about actors or
  principals.
- **Background conditions** (B): choices of representation assumed without loss of generality, each with the reason
  that no case is lost, and the qualifier where something is.
- **Premises** (A): what the framework assumes about judging alignment. Each says its status in the terms of reverse
  physics: a *principle*, taken to be true, or an *assumption*, which may fail; *conceptual*, a logical necessity or a
  consequence of definitions, or *phenomenological*, justified by observation [@carcassi2022].
- **Definitions** (D): each declares its **interpretation**, what its object is in the world and how a record verifies
  it, and justifies it. A statement about behaviour is *verifiable* when a test exists that ends in finite time if it is
  true, and *refutable* when its negation is verifiable [@carcassi2021]. Most statements about a behaviour are
  verifiable only in the statistical sense, with error rates that vanish as the record grows, and the statements so
  verifiable are exactly the open sets of behaviours [@genin2017]; the interpretations say which, and by what test.
- **Conventions**: choices that an equally reasonable principal could make otherwise. They are listed in one table at
  the start of section 1, each justified as forced by a stated requirement, by mathematical convenience, or by the
  literature whose results it lets the framework import, and marked by whether it changes a verdict.
No result in `derived/` cites a premise in its Statement or its Proof, and the one premise a definition's Statement
cites, [A5] in [D3], defines a word, "declared", that no proof uses: the results are facts about finite distributions,
given the definitions. The premises and the interpretations carry the meaning, the bridge from those facts to judging
an actor (`NOTES.md` §17). Ids of retired items are not reused: v12's premises A2 and A3, on what pursuit is, are now
reasons of [D2], and the draft's A6 was not adopted (`NOTES.md` §16).

The framework in ten steps:
1. **Foundations** (section 1). Probability on finitely many outcomes, and independent repetition, as mathematics gives
   them; finitely many outcomes, episodes and conditions as outcomes, objectives up to scale, one actor and one
   principal, as background conditions; and three premises: alignment is judged from behaviour in every condition,
   misalignment is the rate of evidence against what was intended, and specifications are declared before they judge;
   with a table of the conventions, each justified.
2. **Behaviour and pursuit** (section 2). Behaviour is a distribution over outcomes. Pursuing an objective reweights a
   default toward it. Derived: nothing is lost by this description, pursuit is the steepest climb, and the cost of
   departing from the default for which it is the best trade-off can only be the KL divergence
   (`derived/tilts-and-paths.md`, `derived/value.md`).
3. **Specification and misalignment** (section 3). The principal declares a default and the behaviours it accepts, often
   as a family of targets: for "pursue `F`", every strength of pursuing `F`, or of any objective that respects the order
   of `F`, or of any mix of candidate targets. Misalignment is the KL divergence from the actual behaviour to the
   nearest acceptable one, the rate of evidence against the specification. Derived: when it is zero, its closed forms,
   and that it is the departure spent beyond the cheapest behaviour that does at least as well as the actor on every
   target of the family (`derived/misalignment.md`).
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
9. **The evaluator** (section 9). What the actor actually pursues, and what it tells about the principal's objective.
   Derived: through the evaluator, only the regression counts; a monotone regression rules out overoptimization, and a
   single-peaked one allows at most one fall (`derived/evaluator.md`).
10. **Records, samples and evidence** (section 10). The record that every claim reaches the world through. Derived: the
    expected evidence per decision is misalignment; detection, estimation and the evaluation gap; what dependence and
    drift between decisions add; and a test of acceptance from counts, exact at every size (`derived/estimation.md`).

Specifications defined by a structure rather than by an objective need no definition of their own: several actors meant
to act independently, behaviour meant to ignore the situation, a process meant to look the same run backward, and
several principals with declared weights (`derived/structure.md`). What the core rules out, the statements that data
could contradict, is collected in `derived/forbids.md`.

**In scope.** One principal and one actor, where the actor may be a group acting on joint outcomes ([P39]) and the
principal several principals with declared weights ([P42]); finitely many outcomes; behaviour in each of finitely many
conditions, which may be the measurement rules the actor faces; any declared set of acceptable behaviours, and any
declared family of targets, with closed forms for "pursue `F`" and for the structural specifications of
`derived/structure.md`; what the actor cannot distinguish, cannot do, or cannot perceive; what observation identifies,
including misalignment that an actor shows only when it is not observed; the evaluator an actor pursues, and what
pursuing it does to the principal's objective; and what records reveal: by their counts, whatever the actor, and with
intervals when they are samples, where one decision may be a whole episode of dependent decisions.

**Out of scope**, stated so that no result is read as covering it:
- *Internal states.* The core judges behaviour ([A1]). Two actors that behave alike in every condition are the same
  actor for the core, whatever their internal goals. An actor that behaves differently when it is not observed is in
  scope: its misalignment in unobserved conditions is a quantity with an identified set ([D9]).
- *Why a group behaves as it does.* A group is one actor on joint outcomes, and its coordination is measured ([P39]);
  how it reaches its joint behaviour, its equilibria and which of them it selects, is not modelled. An actor that
  responds to the measurement is in scope when the rules it may face are conditions ([D8]); a principal that changes its
  rule in response to the actor without having declared how breaks [A5].
- *Choosing the weights of several principals.* Several principals with declared weights are in scope ([P42]); deriving
  the weights, by aggregating preferences, is not.
- *Outcomes that are not finite.* Drafted separately in `CORE-GENERAL.md`, with its results, expected and probed, in
  `general/`. Nothing there is claimed here.
- *Intervals from one long record of dependent decisions.* The misalignment of a record's counts needs no independence
  of the actor ([A4]), what dependence and drift add is measured ([D11], Notes), and decisions that depend on each
  other within an episode are one outcome. An interval for the actor's behaviour from one long record without episodes
  needs rates of mixing, which the core does not model (`CORE-GENERAL.md`).
- *Which objective is right.* The principal declares it; the core does not choose it.
- *Explanations beyond the evaluator.* Why an actor pursues the evaluator it does, and by what mechanism, is not
  measured. The evaluator itself is in scope, as a hypothesis about behaviour that samples can test ([D10], [D11]).

**How to read.** Items are numbered by kind: M for imported axioms, B for background conditions, A for premises and D
for definitions, in this file; P for propositions, in `derived/`. `[P2](iii)` means part (iii) of P2. Logarithms are
natural, so divergences are in nats. Operations on functions (`p/r`, `log`, `e^F`) act outcome by outcome. The Notes of
each item give the names its objects carry in other fields.

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
| `C_F` | the intended behaviours of the ordinal specification of `F` | [D3] |
| `M(p̂)` | the misalignment of the actual behaviour `p̂` | [D3] |
| `𝓚`, `𝓘_𝓚` | a family of targets; its intended behaviours, the pursuits of its targets | [D3] |
| `ℬ`, `𝒜` | the principal's resolution; the actor's resolution | [D4] |
| `E_q[F\|𝒜]`, `F̄` | the cell average of `F` under the default | [D4] |
| `λ`, `S(p̂)` | the matched intensity; the shortfall, in the units of `F` | [D5] |
| `u`, `φ` | an intervention; the pass-through | [D6] |
| `𝓕` | the actor's feasible set | [D7] |
| `𝒞`, `(p_c)` | the conditions; the actor's response | [D8] |
| `Z`, `V_c` | the actor's view: its signals, and their distribution in condition `c` | [D8] |
| `O` | the observed conditions | [D9] |
| `F̂`, `m`, `R` | an evaluator; the regression of the target on it; the residual | [D10] |
| `n`, `p̂_n` | the size of a record; its empirical behaviour | [D11] |
| `s`, `F_s` | time along a path of behaviours; the objective the change reveals | [P2] |
| `J_t` | net value: the objective's average minus the cost of departing from the default | [P4] |
| `t*`, `p°` | the revealed intensity; the nearest intended behaviour | [P5] |
| `KL(p̂‖q)` | the departure of the actual behaviour from the default | [P6] |
| `θ` | the angle between a revealed objective and the declared one | [P11] |
| `σ_q(F)` | the spread of `F` under the default: `Var_q(F)^{1/2}` | [P13] |
| `p*` | the best feasible behaviour | [P15] |

## 1. Foundations

What the framework takes from mathematics, the representation it assumes without loss of generality, and what it
assumes about judging alignment, in that order; first, the conventions they and the definitions use.

**Conventions.** Each is forced by a stated requirement, chosen for mathematical convenience, or taken from the
literature so that its results import; often more than one. The last column but one says whether a principal who chose
otherwise would reach another verdict.

| Convention | Declared in | Justified by | Changes a verdict | Why |
|---|---|---|---|---|
| natural logarithms: divergences and evidence in nats | [D1], [D11] | convenience, literature | no: another base rescales every number alike | derivatives of `e^F` and of the tilt carry no constant; statistics and large deviations count in nats, coding theory in bits, a factor `log 2` apart |
| evidence on a logarithmic scale, per decision | [A4], [D11] | forced, literature | no: only the unit is chosen | the evidence of independent decisions must add up, and the only continuous functions that turn products of probabilities into sums are multiples of the logarithm (Cauchy's functional equation); Good's weight of evidence, Wald's sequential test and the Neyman–Pearson lemma all count it so |
| the accepted behaviour most favourable to the record | [A4], [D3] | literature, convenience | yes: an average over the accepted behaviours, or the least favourable, would charge more | the generalized likelihood ratio test judges a set of hypotheses by its member most favourable to the data ([@polyanskiy2025], §16.4); the minimum is attained ([P5](i)), at one behaviour for every family of targets ([P53](i)) |
| accepted behaviours decide independently | [A4], [B2], [D11] | convenience, literature | yes: an actor whose decisions depend on each other is accused by the test from counts more often than its level, and one whose shares never settle is charged for that; a principal who intends dependence declares episodes instead ([B2]) | a test of a distribution takes independent draws from it as the hypothesis; the counts are then all the record says about it, and the method of types applies ([P55]) |
| the shares of the record measured against the accepted behaviour, `KL(p̂‖p)`, in this order | [A4], [D3] | forced, literature | yes: the other order is another number, with another nearest behaviour | forced by [A4]: shares `s` become improbable under `p` at the rate `KL(s‖p)` ([P55](i)); maximum likelihood minimizes the same order, so the deviance and Wilks's theorem import ([P23]) |
| intended behaviours of full support, the set closed in `Δ°` | [D3] | convenience | no: their limits count as intended ([P5](ii)) | every divergence from a full-support actor to an intended behaviour is finite, and its least value is attained |
| doing nothing is intended: the default is in every family's specification | [D3] | convenience, literature | yes: an actor that stays at the default is not charged, though it may be useless | misalignment is then at most the departure ([P5](iii)); KL-regularized training keeps the reference policy admissible; a principal who wants something done declares a floor ([P35]) |
| families of targets hold the constants and the positive mixes of their targets | [D3] | forced, convenience | only for a family that is not convex, judged as the union of its convex parts | constants change no aim ([B3]); a principal who accepts each of two targets, with weights not fixed, accepts their weighted pursuit ([P42](ii)); convexity gives one nearest behaviour and the credited reading ([P53]) |
| objectives up to a positive factor and a constant | [B3] | forced | no | a pursuit reveals its objective only up to them ([P1](ii)) |
| pursuit is a tilt of the default | [D2] | forced, literature | yes: another model of pursuit gives another standard specification | forced by the steepest climb in a geometry that ignores how finely outcomes are described, and by the best trade-off at a KL price ([P2], [P4](i), [P14]); it is the optimum of KL-regularized training, the logit choice rule and selection |
| stakes in the objective's own units | [D5] | convenience | no: misalignment is in nats either way | the principal reads losses in the units it declared |

### M1 — Probability on finitely many outcomes
**Statement.** On a finite set, a probability gives each element a non-negative mass, and the masses add up to one. The
probability of a subset is the sum of the masses of its elements; given a subset of positive probability, the
probability of another is the probability of their intersection divided by that of the first. The average of a function
is the sum of its values, each weighted by its mass.

**In plain terms.** Shares of a whole: each thing that can happen gets a share, the shares add up to one, and an
average weighs each value by its share.

**Status.** Imported from probability theory as it is: Kolmogorov's axioms in their finite case, where additivity over
countably many sets reduces to finite sums. It assumes nothing about actors or principals.

**Why this choice.**
- *It is the mathematics of ensembles.* Decisions can be mixed: an actor that acts one way on a share `a` of occasions
  and another way on the rest acts as their mixture with weights `a` and `1 − a`. With finitely many outcomes that
  exclude each other, every ensemble is one such mixture of the outcomes, in one way only, so the ensembles are the
  points of a simplex, as classical ensembles are, and an average is an affine function of the ensemble, as statistical
  quantities are [@carcassi2026e].
- *Nothing more is needed.* Every result of the finite core uses finite sums. The general core replaces the sums by
  integrals against a measure, and ratios of masses by densities (`CORE-GENERAL.md`).

**Lineage.** New in v13: used silently before, in [D1].

### M2 — Independent repetition
**Statement.** Decisions drawn independently from one probability have, jointly, the product of their probabilities.
The share of an outcome `x` among `n` such decisions has average `p(x)` and variance `p(x)·(1 − p(x))/n`, so it lies
within `ε > 0` of `p(x)` with probability at least `1 − p(x)·(1 − p(x))/(n·ε²)`.

**In plain terms.** When decisions do not influence each other, the shares in a long record come as close as one likes
to the actor's behaviour, with a known chance of missing.

**Status.** Imported from probability theory: independence as the product of probabilities. The bound is Chebyshev's
inequality, shown below; nothing else is imported.

**Why this choice.**
- *It is the bridge from records to behaviours.* A behaviour is never observed; the shares in a record are. This is what
  lets a record verify a behaviour to any precision, in the statistical sense, and why section 2 reads a behaviour as
  the shares over unboundedly many decisions.
- *The bound, in one line.* The share is the average of `n` independent indicators, each of average `p(x)` and variance
  `p(x)·(1 − p(x))`, so its variance is `p(x)·(1 − p(x))/n`, and Chebyshev's inequality bounds the chance of a
  deviation of at least `ε` by that variance over `ε²`.

**Lineage.** New in v13: before, part of [D11]'s reasons.

### M3 — Imported theorems
**Statement.** Besides finite sums and [M2], the results of `derived/` use these theorems: Gibbs' and Pinsker's
inequalities; the Neyman–Pearson lemma; the central limit theorem and the delta method; Wilks's theorem; Chernoff's
theorem; Huber's limit law for estimates that solve an equation; and Čencov's theorem, which gives one reason for the
definition of pursuit (section 2) and nothing a result rests on.

**In plain terms.** The framework borrows a short list of standard theorems, each checked in a text anyone can read,
and assumes nothing else from outside.

**Status.** Imported, each with its hypotheses quoted where a result uses it, and read in a text anyone can read without
paying, or derived where it is used; `REFERENCES.md` says where each is read.

**Why this choice.** Proving classical theorems again adds nothing a reader can check better in their source. Quoting
their hypotheses where they are used keeps each result honest about what it needs, and listing them here makes the
boundary between what the framework assumes and what it borrows visible at once.

**Lineage.** New in v13: the list was implicit in the results and in `REFERENCES.md`.

### B1 — Finitely many outcomes
**Statement.** The outcomes of a decision are finitely many.

**In plain terms.** Whatever happens is sorted into one of finitely many results that a record can tell apart.

**Status.** A background condition, assumed without loss of generality for every quantity that finite descriptions
determine.

**Why this choice.**
- *A record decides finitely many events.* A record of finitely many decisions, each read at finite precision, settles
  which of finitely many results occurred, and nothing finer. The outcomes are the possibilities of a domain in which
  every statement about one decision is decidable, and such a domain is discrete [@carcassi2021]: finitely many outcomes
  are the general case of what a finite record can tell apart.
- *Nothing a record measures is lost.* On outcomes that are not finite, the divergence is the supremum of its values
  over finite descriptions, so each misalignment the framework reports there is a limit of misalignments on finitely
  many outcomes (`CORE-GENERAL.md`, GA1 and GD3; `general/dictionary.md`). What does not carry over, the existence of
  nearest behaviours, heavy tails and atoms, is listed there, and is the qualifier of this condition.
- *Exactness.* Every statement can be proved with finite sums and checked exactly on random instances.

**Lineage.** v12: [A1]'s "finitely many outcomes" and [D1]'s first reason; new as a condition in v13.

### B2 — Episodes and conditions as outcomes
**Statement.** Decisions that depend on each other within an episode count as one outcome, the episode; and a situation
the actor does not choose counts as part of the outcome, with its frequency fixed.

**In plain terms.** A whole conversation, game or treatment can be one outcome, and the situation it happened in can be
part of it.

**Status.** A background condition, assumed without loss of generality: episodes, and pairs of a situation and an
outcome, are again finitely many outcomes ([B1]), with a behaviour on them. It is how a principal who intends decisions
to depend on each other says so: within an episode they may; between episodes, the accepted behaviours decide
independently, a convention of the declaration (the table of conventions above).

**Why this choice.** A record of dependent decisions grouped into episodes, or of situations with their frequencies, is
again a record of outcomes on a finite set, so every result applies to it unchanged; results about several situations
are stated on pairs of a situation and an outcome (`derived/estimation.md`). One long record with no episodes is not
covered (section 0, out of scope).

**Lineage.** v12: §0's scope ("the episode being one outcome") and the contexts of the ontologies; new as a condition in
v13.

### B3 — An objective up to scale and constant
**Statement.** An objective `F` and `a·F + c`, for numbers `a > 0` and `c`, state the same aim; the units of `F` matter
only to the stakes.

**In plain terms.** Doubling every score, or adding the same amount to all of them, does not change what is asked for.

**Status.** A background condition, assumed without loss of generality: pursuit, every specification built from `F`,
and misalignment are unchanged by the change; the stakes are reported in the declared units, and scale with `a`.

**Why this choice.** A pursuit reveals its objective only up to a positive factor and a constant ([P1](ii)), so no
behaviour can tell the two statements apart. Fixing one of them loses nothing a record could show; the units return
where the principal needs them, in the stakes (section 5).

**Lineage.** v7.10: Prop 16's gauge; new as a condition in v13.

### B4 — One actor and one principal
**Statement.** Several actors acting on joint outcomes count as one actor, and several principals with declared weights
count as one principal.

**In plain terms.** A team is judged as one player on what the team does, and a committee with agreed weights as one
judge.

**Status.** A background condition, assumed without loss of generality once the joint outcomes and the weights are
declared. How a group reaches its joint behaviour, and how the weights are chosen, are out of scope (section 0).

**Why this choice.** On joint outcomes, the coordination of a group is a measured quantity rather than an assumption
([P39]), and several principals with declared weights pool exactly into one ([P42]).

**Lineage.** v11: the scope widened to groups and to several principals (Q24, Q25); new as a condition in v13.

### A1 — Behaviour suffices
**Statement.** What an actor does is described by how often each outcome occurs, in each condition it may face.
Alignment is judged from that description alone, never from how the behaviour is produced.

**In plain terms.** We judge what the actor does, in every situation it may meet, and not what goes on inside it.

**Status.** A principle, conceptual. A judgement that a principal can check rests on what a record can verify, and a
record verifies what the actor does, not how it does it: the principle that science is universal, non-contradictory and
evidence based [@carcassi2021], applied to judging an actor. "In every condition" makes it a principle about all the
situations the actor may meet, not only those recorded.

**Why this choice.**
- *It can be observed.* Behaviour can be counted. Internal goals and mechanisms differ across AI systems, people,
  institutions and organisms, and are often out of reach. A premise about behaviour applies to all four.
- *In every condition, not in one.* Judging a single behaviour would miss an actor that behaves well when it is
  observed and badly otherwise. Requiring behaviour in every condition keeps such deceptive alignment inside the
  framework, as misalignment in conditions that are not observed (section 8).
- *What it costs.* Two actors that behave alike in every condition are the same actor for the core, whatever their
  internal goals. That is deliberate: a difference that shows in no condition has no consequence a principal could
  suffer.

**Lineage.** v7.10: R7-1 (the actual behaviour is any distribution, Def 13). v8: [D1]'s "why", where this was an
argument. New: behaviour in every condition, so that deceptive alignment is in scope. v13: "finitely many outcomes"
moved to [B1].

### A4 — Misalignment is evidence
**Statement.** The misalignment of the shares that a record of decisions shows, against the behaviours a principal
accepts, is the rate per decision at which, as records with those shares grow, the highest probability that accepted
behaviours give them, a supremum, falls, each accepted behaviour deciding independently. The misalignment of a behaviour
is that of the shares that approach it.

**In plain terms.** Watch the actor decide, and count what it does. Misalignment is how fast those counts become
improbable for every acceptable way of acting, judged by the acceptable way that makes them most probable. It needs no
model of how the actor decides.

**Status.** A principle, conceptual: it says what a record of counts shows against acceptance, which is all that [A1]
lets a judgement rest on, and it assumes nothing about how the actor decides: independently, alike over time, or
neither. Three conventions give it its form, each justified in the table of conventions above: probability counted on a
logarithmic scale, per decision; the accepted behaviour most favourable to the record; and accepted behaviours that
decide independently, unless the principal declares episodes ([B2]).

**Why this choice.**
- *It needs nothing about the actor.* The probabilities are computed under the accepted behaviours, which the principal
  declares, so the measure applies to any actor, any record and any declared set, with no model of how the actor
  decides and no price of departing from the default.
- *Improbability under acceptance is evidence against it.* Counts that are improbable under every accepted behaviour
  are evidence that the actor acts in no accepted way. Judging a set of hypotheses by its member most favourable to the
  data is the generalized likelihood ratio test ([@polyanskiy2025], §16.4), which gives the actor the benefit of the
  doubt and charges it only for what no accepted behaviour explains.
- *The measure follows.* The highest probability that accepted behaviours give the shares `s` falls at the rate
  `inf_{p∈𝓘} KL(s‖p)` (Notes): that is the measure, its form and the order of its arguments.
- *For an actor that decides independently, it is the rate of likelihood-ratio evidence.* Each independent decision
  drawn from `p̂` adds on average `KL(p̂‖p)` nats to the evidence for `p̂` against `p` (the Neyman–Pearson lemma makes
  that evidence canonical, [@polyanskiy2025], Theorem 14.11), so misalignment is also the least expected evidence per
  decision. For an actor whose decisions depend on each other, or drift, that evidence is larger, by exactly two terms
  that are reported beside it (Notes).
- *Value lost, as a reading.* Every full-support behaviour is the best trade-off for its own objective at a KL price
  ([P4](ii)), so the same number is the least net value lost against an accepted behaviour, judged by that behaviour's
  own objective. Until v12 that reading was the premise, and it needed two premises on pursuit to make the price KL
  ([P14]); here it is a consequence, and the measure rests on evidence alone.

**Notes.** The rate is the method of types, [P55](i); the test it gives, exact at every size of record, is [P55](ii);
what dependence and drift add to the likelihood-ratio evidence is [P54]. That "misaligned" is verifiable in chance, and
"exactly aligned" only refutable, is [P55], Notes, after Genin and Kelly [@genin2017].

**Lineage.** v7.10: Thm 1 (regret is a divergence) and Prop 18 (detection). v8: [D3]'s "what the number means". v12:
"misalignment is value lost", which this premise replaces, its reading kept as a consequence (`NOTES.md` §16, §17). The
idea is the hunch H4 of `NOTES.md` §5.4. v13, at the PI's question whether independence could be dropped (Q53): the
rate at which the record's shares become improbable under acceptance, which needs no independence of the actor, in
place of the rate of likelihood-ratio evidence of an actor that decides independently, now a reading ([P54]).

### A5 — Declared before
**Statement.** The default and the acceptable behaviours are fixed before, and without using, the behaviour they will
judge.

**In plain terms.** Decide what counts as acceptable before looking at what the actor did.

**Status.** A principle, conceptual: a standard fitted to the behaviour it judges cannot be refuted by that behaviour,
so fixing it first is what makes the judgement a test. It is a logical necessity of testing, not an observation.

**Why this choice.** A default or an acceptable set fitted to the behaviour being judged removes exactly the
differences the judgement needs. In v7.10, I1-dyn fitted its default (a Hardy–Weinberg expectation) from the counts it
judged, and its test could not fail. Pre-registration in science makes the same demand.

**Lineage.** v7.10: Def 23's timing slot. v8: [D3]'s rule of use.

## 2. Behaviour and pursuit

### D1 — Outcomes, behaviours, divergence and tilt
**Statement.** `X` is a finite set of **outcomes**, with at least two elements. A **behaviour** is a probability
distribution `p` on `X`. `Δ` is the set of behaviours, and `Δ°` the set of **full-support** behaviours, those with
`p(x) > 0` for every `x`. For `p ∈ Δ` and `F : X → ℝ`, `E_p[F] = Σ_x p(x)·F(x)` and `Var_p(F) = E_p[F²] − E_p[F]²`, and
`Cov_p(F, G) = E_p[F·G] − E_p[F]·E_p[G]`; for a set `C ⊆ X` with `p(C) > 0`, `p(·|C)` is `p` conditioned on `C`. For
`p, r ∈ Δ`, the **Kullback–Leibler divergence** is `KL(p‖r) = Σ_{x : p(x) > 0} p(x)·log(p(x)/r(x))`, which is finite
when `r(x) > 0` wherever `p(x) > 0`, and `+∞` otherwise. The **tilt** of `r ∈ Δ°` by `F : X → ℝ` is the behaviour
`tilt(r, F) = r·e^F / E_r[e^F]`.

**In plain terms.** Outcomes are the things that can happen, and a behaviour says how often each one happens; full
support means that nothing is ruled out entirely. KL measures how far one behaviour is from another; it is not
symmetric, so the order matters. Tilting reweights a behaviour toward the outcomes that a function scores higher.

**Interpretation.** *Declared.* An outcome is the narrowest result that a record of one decision tells apart from the
others, such as the answer an assistant gave or whether a patient was seen within four hours. A behaviour is the actor's
ensemble in one condition: the shares its outcomes take over unboundedly many independent decisions ([M2]). `E_p[F]` is
the average score of those decisions. `KL(p‖r)` is the rate per decision at which shares `p` become improbable for an
actor that decides as `r` ([A4]); for an actor that decides independently as `p`, it is also the evidence one decision
gives, on average, against `r`. `tilt(r, F)` is what remains of the ensemble `r` when each decision is kept with a
probability proportional to `e^F`: a selection a principal could carry out, by accepting or rejecting decisions.
*Verified.* Which outcome occurred is decided by the record of one decision. A behaviour is approached by the shares in
a record, never reached ([M2]): `p(x) > 0` is verified by a single occurrence of `x`, while `p(x) = 0` can only be
refuted, and no record verifies an exact mass. *Justified.* Outcomes exclude each other and are decidable, and ensembles
of decisions mix, so the behaviours are the points of a simplex, and averages are affine in them ([M1]). Masses that are
exactly zero, or irrational, are idealizations no record verifies; the definitions that follow ask for full support
where a divergence must stay finite.

**Why this choice.**
- *Finite outcomes.* Every statement can then be proved with finite sums, and checked exactly on random instances.
  General outcome spaces add conditions (absolute continuity, integrability of `e^F`, and compactness in the existence
  arguments). They come back when an item needs them.
- *Full support, where it is needed.* It keeps every logarithm finite. A behaviour that rules an outcome out, such as a
  deterministic one, is still a behaviour: it is allowed as the first argument of KL, and it is a limit of full-support
  behaviours.
- *Behaviour is any distribution* ([A1]). No model of how an actor produces its behaviour is assumed. The core measures
  behaviour; how it is produced is not part of it.
- *KL and the tilt are notation here.* The items that use them argue that they are the right tools.

**Notes.** A behaviour is a policy in reinforcement learning, a mixed strategy in game theory, a distribution of choices
in economics, and a distribution of types in a population in biology. The tilt is exponential tilting in statistics.

**Lineage.** v7.10: Def 1 (the objects), and R7-1's rule that the actual behaviour is any distribution (Def 13). v7.10's
R7-8 (measurable spaces) stays deferred, as it was there.

### D2 — Pursuit of an objective
**Statement.** Let `q ∈ Δ°`, the **default**, and let `F : X → ℝ` be a function, an **objective**. The **pursuit** of
`F` from `q` at **intensity** `t ≥ 0` is `p_{F,t} = tilt(q, t·F)`. The **pursuit ray** of `F` from `q` is
`R_F = {p_{F,t} : t ≥ 0}`; for a constant `F` it is the single point `q`. A continuously differentiable path `s ↦ p_s`
in `Δ°`, over an interval containing `0`, **pursues** `F` if `p_s = tilt(p_0, τ(s)·F)` for a differentiable,
non-decreasing `τ` with `τ(0) = 0`.

**In plain terms.** Pursuing an objective means reweighting the default behaviour toward the outcomes that the objective
scores higher, and the intensity says how strongly. Intensity zero is the default itself, and the pursuit ray collects
every intensity. A path of behaviours pursues an objective when it keeps reweighting toward that same objective, never
away from it, from wherever it starts.

**Interpretation.** *Declared.* The default is what the actor does when it pursues nothing in particular: the base
policy before tuning, the status quo, the population before selection, measured apart from the behaviour to be judged.
An objective is a score of outcomes. To pursue it at intensity `t` is to keep the default's decisions in proportion to
`e^{t·F}`: selection with fitness `e^F` for `t` generations, the logit choice of an actor whose rationality is `t`, or
the optimum of training on `F` with a penalty of `1/t` on the departure from the default. A path pursues `F` when every
change along it reweights toward that one score. *Verified.* That an actor pursues `F` from `q` can be refuted from
records: its revealed objective `log(p/q)` must be an affine function of `F`, with a slope that is not negative, in
every condition (`derived/tilts-and-paths.md`). Only the product `t·F` is identified ([B3]). *Justified.* below: the
reasons for the ray are geometric and economic, and the two agree on it.

**Why this choice.**
- *It loses no generality.* Every full-support behaviour `p` lies on the pursuit ray of some objective, from any
  default: `p = p_{F,1}` with `F = log(p/q)` ([P1](i)). Every path of behaviours follows the replicator equation of an
  objective that may move over time ([P2](i)). What the definition adds is a claim that can fail: that the objective
  stays fixed, which a derived result makes testable (`derived/tilts-and-paths.md`). Mixing a behaviour with another,
  for example, generally gives a path whose objective turns, as that result's check shows; cut-offs that exclude
  outcomes leave `Δ°` altogether.
- *The steepest climb.* To pursue an objective is to raise its average as steeply as possible, with steepness measured
  in a Riemannian geometry on behaviours that does not change when outcomes are split into finer outcomes in fixed
  proportions: two observers who describe the same events at different granularity must agree on what pursuing means.
  Up to a constant factor, the Fisher metric is the only such geometry, across outcome spaces of every size (Čencov's
  theorem [@cencov1982], extended by [@campbell1986]; read in the open texts [@le2016], Proposition 6.1, and [@ay2015],
  Corollary 3.20). In the Fisher metric the steepest climb is the replicator field ([P2](ii)), and its flow from `q` is
  `tilt(q, s·F)` ([P2](iii)). A constant factor in the metric only rescales time, so the ray is the same. A geometry
  whose lengths come from a norm that is not an inner product would need a uniqueness theorem of its own; none is known
  here, and this reason does not cover it.
- *The best trade-off.* To pursue at intensity `t` is also to choose the behaviour with the largest average of `F` minus
  a cost of departing from the default, priced at `1/t` in the units of `F`, the cost depending only on the behaviour:
  an actor that pursues intensely treats departure as cheap. The ray is that choice for exactly one differentiable cost,
  up to a constant, the KL divergence from the default, so the geometric reason and the economic one agree in one way
  only (Notes).
- *Reasons, not premises.* Until v12 the two reasons above were the premises A2 and A3. No result uses them: the
  results hold of the ray as defined. They carry its interpretation, that the ray is what pursuing means; a reader who
  rejects both keeps every result, and loses that reading (`NOTES.md` §17).
- *The ray needs a default; the path does not.* The same objective pursued from two defaults gives two different rays,
  so the specification of section 3 fixes the default. Whether a path pursues `F` needs no default at all, which is why
  derived results can read pursuit from changes of behaviour without declaring one.

**Notes.** Names in other fields. The default is the reference policy of RL fine-tuning, the prior of KL control, the
base measure of an exponential family, the status quo of behavioural economics, and the population before selection in
biology. The objective is a reward, a utility, or a log-fitness. The pursuit `p_{F,t}` is the optimum of KL-regularized
reward maximization with coefficient `1/t` in RL fine-tuning, for one prompt (across prompts, which the policy does not
choose, the optimum reweights each prompt's responses separately, which is not a pursuit on prompt–response pairs); with
a uniform default it is the logit choice rule, or quantal response, with rationality `t` [@mckelvey1995]; and it is the
result of `t` generations of constant selection with fitness `e^F`, for types that are passed on intact, as in clonal
reproduction. The intensity is an inverse temperature in physics, and "optimization pressure" in AI safety. That the
ray is the best trade-off for the KL cost is [P4](i); that KL is the only cost for which the steepest climb is the best
trade-off is [P14], and if the best trade-offs are only asked to lie somewhere on the ray, any increasing function of KL
passes ([P14], Notes).

**Lineage.** v7.10: Def 1 (the Gibbs tilt `p_{G,t}`, with `q` there called the reference), Def 2 (the bounded actor,
whose optimum is the tilt: here a property, [P4](i)), Prop 15 (the carrier), and Prop 16 (g4) (the half-ray). The ray
defines intended pursuit; it is not a model of the actor. v7.10's rows 67–68 and 76–78 filed results by the intended
actor's model instead of by what their proofs need, and the core keeps the two apart by construction. v13: v12's
premises A2 (pursuit is the steepest climb) and A3 (pursuit is the best trade-off) became the first two reasons above,
as no result used them (Q52).

## 3. The specification and misalignment

### D3 — Specification, declaration and misalignment
**Statement.** A **specification** is a pair `(q, 𝓘)`: a default `q ∈ Δ°`, and a non-empty set `𝓘 ⊆ Δ°` of
**intended behaviours**, closed in `Δ°`. The **misalignment** of a behaviour `p̂ ∈ Δ` is `M(p̂) = inf_{p ∈ 𝓘} KL(p̂‖p)`.
A **family of targets** is a closed set `𝓚` of objectives that contains the constants and `a·G + b·G'` whenever it
contains `G` and `G'`, for all numbers `a, b ≥ 0`; its specification is `(q, 𝓘_𝓚)`, with `𝓘_𝓚 = {tilt(q, G) : G ∈ 𝓚}`,
the pursuits of its targets from `q`. For an objective `F`, the **standard specification** is that of the family
`{t·F + c : t ≥ 0, c real}`, so that `𝓘_𝓚 = R_F`: pursuit of `F` from `q` at every intensity, including none; the
**ordinal specification** is that of the family of non-decreasing functions of `F`, so that
`𝓘_𝓚 = C_F = {p ∈ Δ° : p/q is a non-decreasing function of F}`. A specification is **declared** when it is fixed as [A5]
requires: before, and without using, the behaviour it will judge.

**In plain terms.** Before looking at what the actor does, the principal states a default behaviour and the set of
behaviours it would accept. Misalignment is how far the actual behaviour is from the nearest acceptable one, in nats:
how fast a record of it builds a case that it is not acceptable. For the request "pursue this objective", two sets are
natural. For an actor that pursues, weighing outcomes by how much better they are, every intensity of pursuing the
objective is acceptable, including none. For an actor that only ranks outcomes, or whose method is unknown, every
behaviour that favours better outcomes at least as much as worse ones, relative to the default, is acceptable. Under
either, an actor that stays at the default is not misaligned, though it may be useless, which is a different failure.

**Interpretation.** *Declared.* A specification is the principal's standard, written down and dated before the record it
judges is read ([A5]): a default, and the ensembles the principal accepts. A family of targets is the set of aims the
principal accepts being pursued: each at every strength, and every positive mix of them; "pursue `F`" is the smallest
family that holds `F`, and "favour what `F` ranks higher" the family of its order. Misalignment is the rate, in nats per
decision, at which a record's counts become improbable under every accepted behaviour ([A4]): about `1/M` decisions make
them `e` times less probable. *Verified.* "Misaligned", `M > 0`, is verifiable in the statistical sense, by a test whose
rate of false accusation is bounded at every size of record and whose power tends to one, with no model of how the actor
decides beyond what acceptance asks: an intended actor decides independently, and one that does not may be accused for
that alone (Notes). "Aligned within `ε`", `M < ε`, is verifiable in the same sense for an actor that decides
independently. "Exactly aligned", `M = 0`, can only be refuted: an actor can be shown to be misaligned, or aligned
within a stated margin, never exactly aligned, unless the specification accepts every behaviour. *Justified.* Counts are
what a record supplies ([A4]); fixing the standard first is what makes the judgement a test ([A5]); and the statements
above are verifiable or refutable because of their shape, open or closed in the behaviours, as the statistical form of
reverse physics requires (Notes).

**Why this choice.**
- *The formula is [A4] made exact.* If the actor behaves as `p̂` and `p` is intended, each independent decision adds on
  average `KL(p̂‖p)` nats to the log-likelihood ratio in favour of `p̂` over `p`; the least such rate over the intended
  behaviours is `M(p̂)`, including the order of the arguments. Each intended behaviour is also the best trade-off for
  its own objective at a KL price ([P4](ii)), so `M(p̂)` is as well the least net value lost, in nats; for a pursuit
  that is both the steepest climb and the best trade-off ([D2]), that price is the only one ([P14]).
- *What the number means.* About `1/M(p̂)` decisions give one nat of evidence that the actor is not behaving as
  intended, odds of about `e` to 1.
- *The direction charges the unintended.* `KL(p̂‖p)` is large when the actor often does what `p` rarely does, and
  comparatively small when the actor merely does less of what `p` does. Doing the unintended costs more than leaving the
  intended undone.
- *The nearest acceptable behaviour.* Taking the minimum gives the actor the benefit of the doubt: it is charged only
  for what no acceptable behaviour explains.
- *Grouping only hides.* By [P4](iii) and (iv), the score splits along groupings of outcomes, and grouping can only hide
  misalignment. Section 4 uses this for resolutions.
- *A set, not a point.* A principal who asks for `F` without naming an intensity would otherwise charge the actor for an
  intensity it never asked about (v7.10: row 74, the price measure is a regret, not misalignment). A single intended
  behaviour is the case `𝓘 = {p*}`.
- *The standard specification is the pursuit ray,* because "pursue `F`" states a fixed objective ([D2]) at an unstated
  intensity, for an actor that weighs outcomes by their values ([D2], its reasons). It includes doing nothing; a
  principal for whom doing nothing is a failure declares a smaller set (v7.10: the floor, Def 20). The cost of departing
  is what makes it a set of compromises: without it, the only fully intended behaviours would be those on the best
  outcomes of `F`.
- *A family of targets, not one.* A principal often knows its target only up to a family: its order, a span of
  candidate rewards, the objectives of several principals whose weights are not agreed. Declaring the family keeps one
  definition for all of them; the single objective is the smallest family. The family holds the constants, since they
  change no aim ([B3]), and positive mixes of its targets, since a principal who accepts each of two targets with
  weights it has not fixed accepts their weighted pursuit; a family that is not convex is the union of the
  specifications of its convex parts, and its misalignment is the least of theirs.
- *Misalignment is excess departure.* Every family credits the actor with what it achieves on the family's targets, and
  `M(p̂)` is the departure spent beyond the cheapest behaviour that does at least as well on every target (Notes). The
  standard specification credits the average of `F`, only when the actor does better than the default; the ordinal one
  credits reaching every threshold of `F` at least as often. What is charged is departure that buys nothing the family
  credits, whether from a wrong goal or from a way of acting that cannot reach the cheapest behaviour.
- *The ordinal specification, for actors that rank.* An actor that picks by rank, such as best-of-`n`, behaves alike
  for every increasing transformation of `F`, and keeps the default's proportions within each level set of `F`. Its
  specification is the order of `F`, which accepts every pursuit of an increasing transformation of `F` and every
  best-of-`n` by `F` (Notes). Under it, misalignment charges only what contradicts the order; the standard
  specification charges, besides, the shape of the reweighting.
- *Both, side by side.* The declaration names the specification that judges. No premise chooses it for the principal: a
  rule that tied the choice to how the actor is declared to act would move a judgement about the actor into the
  standard. A report under the standard specification gives the ordinal misalignment beside it, so that the part charged
  for the shape of the reweighting is visible (Notes; `STANDARD.md`).
- *The actual behaviour may rule outcomes out; the intended ones may not.* A deterministic actor still gets a score.
  Intended behaviours keep full support so that the score is finite.
- *Declared before, not fitted after.* A default or an intended set fitted from the behaviour being judged removes
  exactly the differences the judgement needs. In v7.10, I1-dyn fitted its default (a Hardy–Weinberg expectation) from
  the counts it judged, and its test could not fail.
- *Stakes are reported separately.* Misalignment in nats says nothing about how much of `F` is at stake. Section 5
  reports the shortfall in `F`'s own units (v7.10: Def 22 and R8-1, where this lesson was learned).
- *Slim on purpose.* v7.10's declaration (Def 23, the same object under its old name) had nine slots. Only four changed
  the measure, and all four are ways of generating `𝓘`. Rules, instruments, feasibility and the environment did not
  enter the measure, so they are not part of the specification. Instruments return as interventions (section 6), and
  feasibility as a property of the actor (section 7), where it splits misalignment instead of changing it. The default
  enters the measure through `𝓘` (the pursuit ray starts at `q`), and other definitions use it directly. A slot is added
  only with a case where it changes a verdict, and with the value it takes when nothing is declared.

**Notes.** The principal declares; what it declares is the specification, the word AI safety and formal verification use
for the set of acceptable behaviours. Misalignment is then a quantitative distance from the specification. The direction
of KL used here is the one called zero-forcing in variational inference. That the standard specification is a
specification, that is, that the pursuit ray is closed in `Δ°`, is shown in [P5](iv); for a constant `F` the ray is the
single point `q`, which is closed. That the ordinal specification is one, that it contains every best-of-`n` by `F`, and
that its misalignment and the shape's add up to at most the standard one are [P36](i) and (iv). That the nearest
intended behaviour of a pursuer has the least departure among those with the actor's average of `F` is [P6](ii), and
that, for every family of targets, the specification is closed, its nearest intended behaviour unique, and misalignment
the departure beyond the cheapest behaviour that does at least as well on every target, is [P53]. The test that makes
"misaligned" verifiable at every size, and the interval that makes "aligned within `ε`" verifiable, are [P55]; its level
holds for intended behaviours deciding independently, and for independent decisions that drift, but an actor whose
decisions depend on each other may be accused for its dependence alone ([P55], Notes); that the statements so verifiable
are the open sets of behaviours, and the refutable ones the closed sets, is Genin and Kelly's theorem [@genin2017], the
statistical form of the verifiable and refutable statements of reverse physics [@carcassi2021] ([P55], Notes). In
statistics, the standard specification is a one-parameter exponential family and the ordinal one a cone of monotone
likelihood ratios, and misalignment is the divergence from the actual behaviour to either.

**Lineage.** v7.10: Def 19 and Prop 34 (the declared intended set), Def 17 (the free convention's half-ray), Def 23 (the
declaration, slimmed; its timing slot becomes the rule of use), row 74, and the target sets of R7-7, cardinal or
ordinal by the principal's declaration. New: behaviours that rule outcomes out are scored. v13: the ordinal
specification moved here from [P36]; misalignment read first as evidence ([A4]); the draft's rule of a matched
specification (its A6) replaced by the paired report (Q52); families of targets, of which the standard and the ordinal
specification are cases, at the PI's question whether a family is more general than one target (Q53).

## 4. Resolution: what each side distinguishes

### D4 — Resolution
**Statement.** A **resolution** is a partition `𝒢` of `X` into non-empty **cells**. A function is constant on cells if
it takes one value on each cell. For `p ∈ Δ`, `p_𝒢` is the distribution of the cell masses `p(C)`. For `q ∈ Δ°` and
`F : X → ℝ`, the **cell average** `E_q[F|𝒢]` is the function equal, on each cell `C`, to `E_{q(·|C)}[F]`. Resolutions
are used in two positions.
- A specification `(q, 𝓘)` is **stated at resolution** `ℬ` if `𝓘 = {p ∈ Δ° : p_ℬ ∈ 𝓘_ℬ}` for a non-empty set `𝓘_ℬ` of
  full-support distributions on the cells, closed in the set of all full-support distributions on the cells. The
  principal is then **indifferent** inside the cells of `ℬ`. For an objective `F` constant on the cells of `ℬ`, the
  **standard specification at resolution** `ℬ` takes `𝓘_ℬ` to be the pursuit ray of `F`, read on the cells, from `q_ℬ`.
- A behaviour `p` is **limited to** a resolution `𝒜` if it splits every cell as the default does: `p(·|A) = q(·|A)` for
  every cell `A` of `𝒜` with `p(A) > 0`. An actor **has resolution** `𝒜` if every behaviour it can produce is limited
  to `𝒜`.

When nothing is declared or known, the resolution is the finest one, with one outcome per cell, in both positions.

**In plain terms.** A resolution groups outcomes into cells that are treated as one. A principal who states its
specification on cells declares that it does not care how outcomes inside a cell are split, only how often each cell
occurs. An actor with a resolution cannot tell the outcomes inside a cell apart: it can change how often each cell
occurs, but inside a cell the outcomes keep the proportions they have by default.

**Interpretation.** *Declared.* The principal's resolution groups outcomes it declares equally acceptable, such as
answers that differ only in wording. The actor's resolution groups outcomes it cannot act on separately: inside a cell,
its decisions keep the default's proportions, as a selection that cannot see inside the cell must. *Verified.* The
principal's resolution is declared, not measured. The actor's can be refuted from records: if the ratio of two outcomes
in one cell moves away from the default's, the actor tells them apart (`derived/identifiability.md`). *Justified.* On
finitely many outcomes, the events a description can decide are the unions of the cells of one partition ([B1]), so a
partition is the general form of what either side can tell apart.

**Why this choice.**
- *One object, two positions.* The same kind of object describes what the principal cares to distinguish and what the
  actor can distinguish. Gaps between the two cover two familiar failures: a principal who cares about distinctions the
  actor cannot see (v7.10's transmission gap, G2), and an actor that acts on distinctions the principal never mentioned
  (underdetermination, G1).
- *Partitions are the general case here.* On a finite set, a σ-algebra is the same thing as a partition into cells.
- *Inside an actor's cells, the default decides.* An actor that cannot tell two outcomes apart cannot change how often
  one occurs relative to the other, so that ratio stays where it is without the actor's choice: at the default ([D2]).
  This needs no object beyond the specification.
- *The finest resolution unless declared.* A principal who declares a coarse resolution cannot see what happens inside
  its cells; in v7.10, a style exploit lived almost entirely inside cells in toy tests (B1). So indifference has to be
  declared, never assumed. An actor's resolution, in contrast, is a fact about the actor, to be identified from its
  behaviour rather than declared.
- *Not the meet.* The finest partition coarser than both resolutions (their meet) holds the events both sides can
  describe, which are common knowledge in Aumann's sense [@aumann1976]. Misalignment computed there is a lower bound
  both can verify ([P4](iv)), but it is blind to every gap between the two resolutions, so it is not the score.

**Notes.** The actor's position is a case of feasibility: the behaviours limited to `𝒜` form a linear feasible set
([D7]). In reinforcement learning, an actor's resolution is a state abstraction, and outcomes it cannot tell apart are
aliased. A principal's resolution is a coarse-graining of the outcomes.

**Lineage.** v7.10: Def 21 (the declared resolution: the principal's position), B1 and NOTES H14 (one object in several
positions; retention), and ROADMAP §6 G1, G2 and G4. New: the actor's position as a definition, with the default
deciding inside cells.

## 5. Stakes

### D5 — Stakes
**Statement.** Under the standard specification of a non-constant objective `F`, let `p̂ ∈ Δ` and let `A` be the set of
outcomes where `F` is largest. The **matched intensity** of `p̂` is `λ = inf{t ≥ 0 : KL(p_{F,t}‖q) ≥ KL(p̂‖q)}`, with
`λ = ∞` when the set is empty; the **matched pursuit** is `p_{F,λ}`, with `p_{F,∞} = q(·|A)`. The **shortfall** of `p̂`
is `S(p̂) = E_{p_{F,λ}}[F] − E_{p̂}[F]`, in the units of `F`.

**In plain terms.** Stakes ask how much of the objective was actually lost. The actor is compared with the pursuit that
departs from the default by the same amount, and the shortfall is how much more of the objective that pursuit gets, in
the objective's own units.

**Interpretation.** *Declared.* The shortfall is what the principal loses in the objective's own units, such as euros,
points of accuracy or hours of delay, against the pursuit that departs from the default as much as the actor did.
*Verified.* Estimated from a record and the declared objective, with its interval. The departure is matched, not the
intensity, because the departure is what a record measures, while the intensity is a property of a pursuit.
*Justified.* Misalignment does not change when the objective is rescaled ([B3]), so it cannot carry the units; the
shortfall carries them.

**Why this choice.**
- *Misalignment is silent about stakes.* Misalignment does not change when the objective is rescaled
  (`derived/stakes.md`), so it cannot say how much of the objective is lost; a principal needs that in its own units. In
  v7.10 this was learned the hard way (R8-1).
- *Compare at the same departure.* The departure is what the actor spent, and the matched pursuit is the most of `F`
  that departure can buy (`derived/stakes.md`). Comparing with the nearest intended behaviour would say nothing: in the
  second case of [P5](iv) it reaches the same average of `F` by construction.
- *Not the best outcome.* Comparing with `max F` would charge every cautious actor for not being reckless, although the
  specification ([D3]) counts departing from the default as a cost.
- *Defined by an infimum,* so that the definition needs no result: a derived result shows that the departure is matched
  exactly whenever `λ` is finite.

**Lineage.** v7.10: Def 22 (the value shortfall `ΔV`), Thm 17(iii) (the same-budget counterfactual), and R8-1.

## 6. Interventions

### D6 — Intervention and pass-through
**Statement.** An **intervention** changes what the actor faces by a known non-constant function `u : X → ℝ`: an
incentive, a fine, or a known shift of the actor's own default. With `p ∈ Δ°` the actor's behaviour before it and
`p' ∈ Δ°` after, the actor passes the intervention through, with **pass-through** `φ ∈ ℝ`, if `p' = tilt(p, φ·u)`.

**In plain terms.** An intervention is a known nudge added to the situation: a bonus for some outcomes, a fine for
others, or a shift in what the actor would do by default. The actor passes it through when its behaviour changes exactly
by reweighting with that nudge. The pass-through says how strongly it responds: zero ignores the nudge, a positive value
follows it, and a negative value means the nudge backfires.

**Interpretation.** *Declared.* An intervention is a change the principal makes and knows, such as a bonus, a fine or a
new default option, written as a score `u` of outcomes. The pass-through is how strongly the actor's behaviour follows
it: `0` ignores it, a positive value follows it, and a negative value means it backfires. *Verified.* From records
before and after: the change of `log p` must lie in `span{u, 1}`, which a record can refute, and the coefficient on `u`
is the pass-through. *Justified.* Any change of behaviour is a reweighting by some function
(`derived/tilts-and-paths.md`), so "it follows the intervention" means that this function is a multiple of `u`.

**Why this choice.**
- *The simplest response that can fail.* Any change of behaviour is a reweighting by some function ([P1](i)). The claim
  that this function is a multiple of the intervention is testable, and a derived result tests it
  (`derived/identifiability.md`). When it fails, more happened between the two behaviours than adding `u`: the
  intervention also changed what the actor pursues or where it starts from, or something else changed at the same time.
- *It needs no model of the actor.* The pass-through is defined from behaviour before and after; the actor's objective,
  default and intensity never appear. An actor that pursues `F̂` at intensity `t` from its own default (every behaviour
  can be written so, by [P1]), and adds `w·u` to `F̂`, has pass-through `φ = t·w` by [P1](iii); only that product is
  identified.
- *A change of default is an intervention too.* If the actor's own default is shifted by a known tilt `h` and its
  objective is unchanged, its behaviour moves to `tilt(p, h)` by [P1](iii): pass-through `1` for `u = h`.

**Lineage.** v7.10: ROADMAP §6 I1 (instrument pass-through: regress the increments on the fine), Def 23's instruments
slot, made measurable, and T7-2d (a change of default that moved the evaluator).

## 7. Feasibility

### D7 — Feasibility
**Statement.** The actor's **feasible set** is a non-empty closed set `𝓕 ⊆ Δ`: the behaviours it can produce. It is
**linear** if it is the set of behaviours whose averages of given functions take given values,
`𝓕 = {p ∈ Δ : E_p[f_i] = a_i for i = 1, …, m}`, for functions `f_i : X → ℝ` and numbers `a_i`. When nothing is known
about what the actor can do, `𝓕 = Δ`.

**In plain terms.** The feasible set is what the actor can do. It is linear when the actor's limits take the form "these
averages cannot change": how often each situation arises, how the actor splits outcomes it cannot tell apart, how the
environment responds to what the actor does.

**Interpretation.** *Declared.* The feasible set is what the actor can produce: given by its design, such as a class of
policies or a budget; by the world, such as how often situations arise and how the environment responds; or by its
resolution. *Verified.* Declared from knowledge of the actor and the world. A behaviour seen in a record is feasible, so
records can refute a declared feasible set, but never confirm it. *Justified.* A principal charges what the actor chose,
not what no behaviour in its reach could avoid; the split between the two is exact for linear limits
(`derived/feasibility.md`).

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

**Lineage.** v7.10: Def 23's feasibility slot, dropped in v8 because it did not change the measure; it returns because
it splits the measure. v7.10: B1 and ROADMAP §6 G2 (retention). New: the definition, and linearity as the class for
which the split is exact.

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

**Interpretation.** *Declared.* A condition is a situation the actor faces and does not choose, such as a prompt, a
client, a test or real use. The response is its behaviour in each condition, and a view is what it perceives of the
condition: a channel from conditions to the signals it receives. *Verified.* Responses are recorded condition by
condition; that a response depends on the condition only through a declared view can be refuted from them
(`derived/identifiability.md`). *Justified.* [A1] judges behaviour in every condition, and a situation the actor does
not choose is part of the outcome without loss of generality ([B2]).

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
and the response is the policy. In statistics, a response that depends on the condition only through a view is a Markov
kernel composed with a channel.

**Lineage.** New. v7.10: ROADMAP §6 I1 (identification through interventions) and the brainstorm's point on
identifiability dynamics. The ontologies' "contexts" (v8, `NOTES.md`) are conditions with fixed frequencies.

### D9 — Observation and identification
**Statement.** The principal observes the response in a set `O ⊆ 𝒞` of **observed conditions**. Let `𝓡` be the set of
responses that satisfy stated assumptions, such as a feasible set in each condition ([D7]) or a view ([D8]). A quantity
defined from the response is **identified** if every response in `𝓡` that agrees with the observed behaviours `p_c`,
for `c ∈ O`, gives it the same value. Otherwise the set of values that those responses give is its **identified set**.

**In plain terms.** The principal watches the actor only in some situations. A quantity is identified when everything
that fits what was watched, and what is assumed, gives it one value. Otherwise the honest report is the range of values
it could take.

**Interpretation.** *Declared.* The observed conditions are those for which a record exists. A quantity is identified
when every response that agrees with the records and with the declared assumptions gives it one value; its identified
set is the range of values they give otherwise. *Verified.* Identification is a property of the records and the
declaration together, checked by computing the identified set. *Justified.* A report that gives one number for what the
records and the assumptions leave open hides an assumption [@manski2003]; what no record can verify enters only as a
declared assumption, and the report says which.

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

**Lineage.** New. v7.10: ROADMAP §6 I1 (the ladder: declare, measure, identify through interventions).

## 9. The evaluator

### D10 — Evaluator, regression and residual
**Statement.** Let `F` be the principal's objective, which this section calls the target. An **evaluator** is an
objective `F̂ : X → ℝ` put forward as the one the actor pursues: known, when it is a function the actor is rewarded on,
or revealed, when it is read from a full-support actual behaviour `p̂` as `F̂ = log(p̂/q)`; as the objective of a
pursuit at some intensity, a revealed evaluator is fixed only up to a positive factor and an added constant. Let `𝒱` be
the resolution whose cells are the level sets of `F̂` ([D4]). The **regression** of the target on the evaluator is the
cell average `m = E_q[F|𝒱]`, and the **residual** is `R = F − m`.

**In plain terms.** The evaluator is what the actor actually works toward: a reward it is paid on, a measure it is
judged by, or, when nothing else is known, the objective its own behaviour reveals. The regression is what the
evaluator tells, on average under the default, about the principal's objective; the residual is the part of the
principal's objective that the evaluator does not see.

**Interpretation.** *Declared.* An evaluator is the score the actor is trained, paid or selected on, such as a reward
model, a performance measure or a fitness; or, when none is known, the objective its own behaviour reveals. The
regression is what the evaluator says, on average under the default, about the principal's objective, and the residual
is what it misses. *Verified.* From outcomes drawn from the default and scored by both the principal and the evaluator;
that the actor pursues a known evaluator can be refuted as any pursuit can ([D2]). *Justified.* The regression depends
on the evaluator only through the outcomes it scores alike, which is all that a ranking or a selection by the evaluator
can use.

**Why this choice.**
- *It adds no assumption.* By [P4](ii) and [P1], every full-support behaviour is the best trade-off for one objective,
  `log(p̂/q)` at intensity 1, fixed up to a constant ([P1](ii)): every actor has a revealed evaluator. A known evaluator
  is a hypothesis about the actor, which behaviour can test ([P1], [P3]).
- *It is the actor's counterpart of the principal's objective.* The principal declares a pursuit of `F` from `q`; the
  actor reveals a pursuit of `F̂` from the same `q`. Misalignment compares two pursuits from one default, in one
  currency.
- *It is universal.* A reward model in fine-tuning, selection through one sex, a fine, a report card, a measured bonus:
  each ontology has one.
- *The residual, not the difference.* The difference `F̂ − F`, v7.10's evaluator error, depends on the scale of `F̂`,
  which behaviour never identifies. The regression and the residual depend on `F̂` only through its level sets, and
  whether the regression rises with `F̂` only through their order: neither changes under an increasing transformation
  of `F̂`. The residual averages to zero in every cell of `𝒱` under the default, so an actor that sees outcomes only
  through the evaluator can neither gain nor lose through it (`derived/evaluator.md`).
- *Regression in the statistical sense.* `m` is the best predictor of `F` from `F̂` in mean square under the default.

**Notes.** The evaluator is a proxy or reward model in machine learning, a performance measure in the economics of
incentives, and the fitness of a selection regime in biology. Goodhart's law is about the gap between an evaluator and a
target; the residual separates the part of that gap that an actor seeing only the evaluator cannot exploit. When `F̂`
gives distinct outcomes distinct values, every cell of `𝒱` is a single outcome, so `m = F` and `R = 0`. The regression
says more than the target itself only when the evaluator is coarser than the outcomes, as a test passed or failed, a
grade, a count or an indicator is.

**Lineage.** v7.10: Def 13 (`F̂ = F + E`, an evaluator and its error `E`) and Def 12's note (an explanation adds an
evaluator). New: the revealed evaluator, and the regression and residual in place of the error, which needed a scale.

## 10. Records, samples and evidence

### D11 — Record, sample and evidence
**Statement.** A **record** of size `n` is the sequence `x_1, …, x_n` of the outcomes of `n` decisions, and its
**empirical behaviour** `p̂_n` gives each outcome its share in the record. A record is a **sample** from a behaviour
`p` when its outcomes are drawn independently from `p`. For full-support behaviours `r` and `r'`, the **evidence** that
a record gives for `r` against `r'` is `Σ_{i=1}^n log(r(x_i)/r'(x_i))`, in nats.

**In plain terms.** A record is what the actor did on successive occasions, in order. Counting gives the empirical
behaviour. A sample is a record whose occasions are independent draws from one behaviour: a model of the actor, which a
case can test. The evidence for one behaviour against another is how much more likely the record is under the first
than under the second, on a logarithmic scale.

**Interpretation.** *Declared.* A record is the log of the actor's decisions; its empirical behaviour is the shares in
it; a sample is a record whose decisions are independent draws from one behaviour; the evidence for one behaviour
against another is how much more likely the record is under the first, in nats. *Verified.* The record is what is
verified, decision by decision; every claim about behaviour reaches the world through it. That a record is a sample is
a claim about the actor, which the order of the record can refute (Notes). *Justified.* Shares are what [A1] judges and
[A4] measures, whatever the actor; independence is what makes them approach one behaviour ([M2]) and the evidence add
up decision by decision, and decisions that depend on each other within an episode are one outcome ([B2]).

**Why this choice.**
- *Behaviours are never observed; records are.* This is the act of measurement that [A1] presumes when it says that
  behaviour can be counted, and that [D9]'s observed conditions stand for.
- *It is universal.* Counted choices, sampled genotypes, sampled responses, case records and logged units of work are
  all samples.
- *Evidence is the canonical statistic.* Between two behaviours, the most powerful test thresholds the likelihood ratio
  (the Neyman–Pearson lemma [@cover2006], read in the open draft of [@polyanskiy2025], Theorem 14.11).
- *It makes [A4] exact.* For a sample, the expected evidence per decision, under the actual behaviour, for it against
  the nearest intended behaviour is the misalignment (`derived/estimation.md`). Evidence gained ([A4]) and value lost
  ([P4](ii)) agree, in the same direction of KL, as the steepest climb and the best trade-off, the reasons of [D2],
  agree on the cost.
- *It compares explanations in the same unit.* Two evaluators proposed for one actor are compared by the evidence a
  sample gives for one pursuit against the other, in nats, the unit of misalignment and of value.
- *Records first, samples as a model.* What a record shows against acceptance needs no model of the actor ([A4]); a
  sample is the model under which shares estimate one behaviour, with an interval. An actor whose decisions depend on
  each other, or drift, is judged by its average behaviour, and what dependence and drift add is measured beside it
  (Notes).

**Notes.** The evidence is the log-likelihood ratio; I. J. Good called it the weight of evidence. In statistics a sample
from a finite set is multinomial, and the empirical behaviour is the type of the sequence [@cover2006]. For a record
that is not a sample, [P54] gives what dependence and drift add to the evidence; [P55] gives the test of acceptance from
counts, exact at every size, and the interval for a sample. Independence between episodes can be tested from the order
of a record, for instance by comparing the shares of pairs of successive episodes with the products of their shares.

**Lineage.** v7.10: Prop 18 (detection) and the deviance of v8's [P5] Notes, which used samples without defining them.
New: the definition, and evidence as the second meaning of misalignment. v13: the record, of which the sample is the
case of independent decisions (Q53).

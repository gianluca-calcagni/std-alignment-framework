# The core

> **Status: v13, approved by the PI (Q52) and merged into `main` with pull request #33 (Q55).** The core holds what the
> framework takes from outside and what it cannot derive: three imported axioms of probability, four background
> conditions assumed without loss of generality, three premises, and the definitions the whole framework uses, each with
> the interpretation it declares. Everything that follows from them is in `derived/`, with proofs and checks that run in
> CI. The format is in `README.md`.

## 0. What the core is

Alignment compares what an actor does with what a principal intended. The core fixes the terms of that comparison, and
says of each starting point what kind of starting point it is.

**How the core is built.** It follows the method of reverse physics [[References|@carcassi2022]], [[References|@carcassi2026]]: separate what a
theory takes from mathematics from what it assumes about the world, say of each assumption what kind it is, and map
every mathematical object to what it stands for, declaring the map and justifying it, so that only objects with a
meaning in the world enter. The core has four kinds of item, and a table of the conventions they use.
- **Imported axioms** (M): mathematics taken as it is, from probability theory. They assume nothing about actors or
  principals.
- **Background conditions** (B): choices of representation assumed without loss of generality, each with the reason
  that no case is lost, and the qualifier where something is.
- **Premises** (A): what the framework assumes about judging alignment. Each says its status in the terms of reverse
  physics: a *principle*, taken to be true, or an *assumption*, which may fail; *conceptual*, a logical necessity or a
  consequence of definitions, or *phenomenological*, justified by observation [[References|@carcassi2022]].
- **Definitions** (D): each declares its **interpretation**, what its object is in the world and how a record verifies
  it, and justifies it. A statement about behaviour is *verifiable* when a test exists that ends in finite time if it is
  true, and *refutable* when its negation is verifiable [[References|@carcassi2021]]. Most statements about a behaviour are
  verifiable only in the statistical sense, with error rates that vanish as the record grows, and the statements so
  verifiable are exactly the open sets of behaviours [[References|@genin2017]]; the interpretations say which, and by what test.
- **Conventions**: choices that an equally reasonable principal could make otherwise. They are listed in one table at
  the start of section 1, each justified as forced by a stated requirement, by mathematical convenience, or by the
  literature whose results it lets the framework import, and marked by whether it changes a verdict.
No result in `derived/` cites a premise in its Statement or its Proof, and the one premise a definition's Statement
cites, [[A5 — Declared before|A5]] in [[D3 — Specification, declaration and misalignment|D3]], defines a word, "declared", that no proof uses: the results are facts about finite distributions,
given the definitions. The premises and the interpretations carry the meaning, the bridge from those facts to judging
an actor (`NOTES.md` §17). Ids of retired items are not reused: v12's premises A2 and A3, on what pursuit is, are now
reasons of [[D2 — Pursuit of an objective|D2]], and the draft's A6 was not adopted (`NOTES.md` §16).

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

**In scope.** One principal and one actor, where the actor may be a group acting on joint outcomes ([[P39 — Several actors: coordination plus individual misalignment|P39]]) and the
principal several principals with declared weights ([[P42 — Several principals: gridlock, and the pooled pursuit|P42]]); finitely many outcomes; behaviour in each of finitely many
conditions, which may be the measurement rules the actor faces; any declared set of acceptable behaviours, and any
declared family of targets, with closed forms for "pursue `F`" and for the structural specifications of
`derived/structure.md`; what the actor cannot distinguish, cannot do, or cannot perceive; what observation identifies,
including misalignment that an actor shows only when it is not observed; the evaluator an actor pursues, and what
pursuing it does to the principal's objective; and what records reveal: by their counts, whatever the actor, and with
intervals when they are samples, where one decision may be a whole episode of dependent decisions.

**Out of scope**, stated so that no result is read as covering it:
- *Internal states.* The core judges behaviour ([[A1 — Behaviour suffices|A1]]). Two actors that behave alike in every condition are the same
  actor for the core, whatever their internal goals. An actor that behaves differently when it is not observed is in
  scope: its misalignment in unobserved conditions is a quantity with an identified set ([[D9 — Observation and identification|D9]]).
- *Why a group behaves as it does.* A group is one actor on joint outcomes, and its coordination is measured ([[P39 — Several actors: coordination plus individual misalignment|P39]]);
  how it reaches its joint behaviour, its equilibria and which of them it selects, is not modelled. An actor that
  responds to the measurement is in scope when the rules it may face are conditions ([[D8 — Conditions, responses and views|D8]]); a principal that changes its
  rule in response to the actor without having declared how breaks [[A5 — Declared before|A5]].
- *Choosing the weights of several principals.* Several principals with declared weights are in scope ([[P42 — Several principals: gridlock, and the pooled pursuit|P42]]); deriving
  the weights, by aggregating preferences, is not.
- *Outcomes that are not finite.* Drafted separately in `CORE-GENERAL.md`, with its results, expected and probed, in
  `general/`. Nothing there is claimed here.
- *Intervals from one long record of dependent decisions.* The misalignment of a record's counts needs no independence
  of the actor ([[A4 — Misalignment is evidence|A4]]), what dependence and drift add is measured ([[D11 — Record, sample and evidence|D11]], Notes), and decisions that depend on each
  other within an episode are one outcome. An interval for the actor's behaviour from one long record without episodes
  needs rates of mixing, which the core does not model (`CORE-GENERAL.md`).
- *Which objective is right.* The principal declares it; the core does not choose it.
- *Explanations beyond the evaluator.* Why an actor pursues the evaluator it does, and by what mechanism, is not
  measured. The evaluator itself is in scope, as a hypothesis about behaviour that samples can test ([[D10 — Evaluator, regression and residual|D10]], [[D11 — Record, sample and evidence|D11]]).

**How to read.** Items are numbered by kind: M for imported axioms, B for background conditions, A for premises and D
for definitions, in this file; P for propositions, in `derived/`. `[[P2 — Every change of behaviour follows a replicator equation|P2]](iii)` means part (iii) of P2. Logarithms are
natural, so divergences are in nats. Operations on functions (`p/r`, `log`, `e^F`) act outcome by outcome. The Notes of
each item give the names its objects carry in other fields.

| Symbol | Meaning | Introduced in |
|---|---|---|
| `X` | the outcomes | [[D1 — Outcomes, behaviours, divergence and tilt\|D1]] |
| `Δ`, `Δ°` | all behaviours; the full-support ones | [[D1 — Outcomes, behaviours, divergence and tilt\|D1]] |
| `E_p[F]`, `Var_p(F)`, `Cov_p(F, G)` | average, variance and covariance under `p` | [[D1 — Outcomes, behaviours, divergence and tilt\|D1]] |
| `KL(p‖r)` | the Kullback–Leibler divergence, in nats | [[D1 — Outcomes, behaviours, divergence and tilt\|D1]] |
| `tilt(r, F)` | `r` reweighted by `e^F` | [[D1 — Outcomes, behaviours, divergence and tilt\|D1]] |
| `q`, `F`, `t` | the default, an objective, an intensity | [[D2 — Pursuit of an objective\|D2]] |
| `p_{F,t}`, `R_F` | pursuit of `F` at intensity `t`; the pursuit ray | [[D2 — Pursuit of an objective\|D2]] |
| `(q, 𝓘)` | a specification, declared by the principal: the default and the intended behaviours | [[D3 — Specification, declaration and misalignment\|D3]] |
| `C_F` | the intended behaviours of the ordinal specification of `F` | [[D3 — Specification, declaration and misalignment\|D3]] |
| `M(p̂)` | the misalignment of the actual behaviour `p̂` | [[D3 — Specification, declaration and misalignment\|D3]] |
| `𝓚`, `𝓘_𝓚` | a family of targets; its intended behaviours, the pursuits of its targets | [[D3 — Specification, declaration and misalignment\|D3]] |
| `ℬ`, `𝒜` | the principal's resolution; the actor's resolution | [[D4 — Resolution\|D4]] |
| `E_q[F\|𝒜]`, `F̄` | the cell average of `F` under the default | [[D4 — Resolution\|D4]] |
| `λ`, `S(p̂)` | the matched intensity; the shortfall, in the units of `F` | [[D5 — Stakes\|D5]] |
| `u`, `φ` | an intervention; the pass-through | [[D6 — Intervention and pass-through\|D6]] |
| `𝓕` | the actor's feasible set | [[D7 — Feasibility\|D7]] |
| `𝒞`, `(p_c)` | the conditions; the actor's response | [[D8 — Conditions, responses and views\|D8]] |
| `Z`, `V_c` | the actor's view: its signals, and their distribution in condition `c` | [[D8 — Conditions, responses and views\|D8]] |
| `O` | the observed conditions | [[D9 — Observation and identification\|D9]] |
| `F̂`, `m`, `R` | an evaluator; the regression of the target on it; the residual | [[D10 — Evaluator, regression and residual\|D10]] |
| `n`, `p̂_n` | the size of a record; its empirical behaviour | [[D11 — Record, sample and evidence\|D11]] |
| `s`, `F_s` | time along a path of behaviours; the objective the change reveals | [[P2 — Every change of behaviour follows a replicator equation\|P2]] |
| `J_t` | net value: the objective's average minus the cost of departing from the default | [[P4 — What KL measures\|P4]] |
| `t*`, `p°` | the revealed intensity; the nearest intended behaviour | [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits\|P5]] |
| `KL(p̂‖q)` | the departure of the actual behaviour from the default | [[P6 — The departure from the default splits into pursuit and misalignment\|P6]] |
| `θ` | the angle between a revealed objective and the declared one | [[P11 — The misaligned share at the start of a change\|P11]] |
| `σ_q(F)` | the spread of `F` under the default: `Var_q(F)^{1/2}` | [[P13 — What the start of a change gains\|P13]] |
| `p*` | the best feasible behaviour | [[P15 — Misalignment splits into what the actor could avoid and what it could not\|P15]] |

## 1. Foundations

What the framework takes from mathematics, the representation it assumes without loss of generality, and what it
assumes about judging alignment, in that order; first, the conventions they and the definitions use.

**Conventions.** Each is forced by a stated requirement, chosen for mathematical convenience, or taken from the
literature so that its results import; often more than one. The last column but one says whether a principal who chose
otherwise would reach another verdict.

| Convention | Declared in | Justified by | Changes a verdict | Why |
|---|---|---|---|---|
| natural logarithms: divergences and evidence in nats | [[D1 — Outcomes, behaviours, divergence and tilt\|D1]], [[D11 — Record, sample and evidence\|D11]] | convenience, literature | no: another base rescales every number alike | derivatives of `e^F` and of the tilt carry no constant; statistics and large deviations count in nats, coding theory in bits, a factor `log 2` apart |
| evidence on a logarithmic scale, per decision | [[A4 — Misalignment is evidence\|A4]], [[D11 — Record, sample and evidence\|D11]] | forced, literature | no: only the unit is chosen | the evidence of independent decisions must add up, and the only continuous functions that turn products of probabilities into sums are multiples of the logarithm (Cauchy's functional equation); Good's weight of evidence, Wald's sequential test and the Neyman–Pearson lemma all count it so |
| the accepted behaviour most favourable to the record | [[A4 — Misalignment is evidence\|A4]], [[D3 — Specification, declaration and misalignment\|D3]] | literature, convenience | yes: an average over the accepted behaviours, or the least favourable, would charge more | the generalized likelihood ratio test judges a set of hypotheses by its member most favourable to the data ([[References\|@polyanskiy2025]], §16.4); the minimum is attained ([[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits\|P5]](i)), at one behaviour for every family of targets ([[P53 — Misalignment is the departure beyond what the family of targets credits\|P53]](i)) |
| accepted behaviours decide independently | [[A4 — Misalignment is evidence\|A4]], [[B2 — Episodes and conditions as outcomes\|B2]], [[D11 — Record, sample and evidence\|D11]] | convenience, literature | yes: an actor whose decisions depend on each other is accused by the test from counts more often than its level, and one whose shares never settle is charged for that; a principal who intends dependence declares episodes instead ([[B2 — Episodes and conditions as outcomes\|B2]]) | a test of a distribution takes independent draws from it as the hypothesis; the counts are then all the record says about it, and the method of types applies ([[P55 — What a record of counts certifies, at every size\|P55]]) |
| the shares of the record measured against the accepted behaviour, `KL(p̂‖p)`, in this order | [[A4 — Misalignment is evidence\|A4]], [[D3 — Specification, declaration and misalignment\|D3]] | forced, literature | yes: the other order is another number, with another nearest behaviour | forced by [[A4 — Misalignment is evidence\|A4]]: shares `s` become improbable under `p` at the rate `KL(s‖p)` ([[P55 — What a record of counts certifies, at every size\|P55]](i)); maximum likelihood minimizes the same order, so the deviance and Wilks's theorem import ([[P23 — The estimated misalignment of an actor that pursues the objective\|P23]]) |
| intended behaviours of full support, the set closed in `Δ°` | [[D3 — Specification, declaration and misalignment\|D3]] | convenience | no: their limits count as intended ([[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits\|P5]](ii)) | every divergence from a full-support actor to an intended behaviour is finite, and its least value is attained |
| doing nothing is intended: the default is in every family's specification | [[D3 — Specification, declaration and misalignment\|D3]] | convenience, literature | yes: an actor that stays at the default is not charged, though it may be useless | misalignment is then at most the departure ([[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits\|P5]](iii)); KL-regularized training keeps the reference policy admissible; a principal who wants something done declares a floor ([[P35 — Floors and caps\|P35]]) |
| families of targets hold the constants and the positive mixes of their targets | [[D3 — Specification, declaration and misalignment\|D3]] | forced, convenience | only for a family that is not convex, judged as the union of its convex parts | constants change no aim ([[B3 — An objective up to scale and constant\|B3]]); a principal who accepts each of two targets, with weights not fixed, accepts their weighted pursuit ([[P42 — Several principals: gridlock, and the pooled pursuit\|P42]](ii)); convexity gives one nearest behaviour and the credited reading ([[P53 — Misalignment is the departure beyond what the family of targets credits\|P53]]) |
| objectives up to a positive factor and a constant | [[B3 — An objective up to scale and constant\|B3]] | forced | no | a pursuit reveals its objective only up to them ([[P1 — Every behaviour is a tilt of any other\|P1]](ii)) |
| pursuit is a tilt of the default | [[D2 — Pursuit of an objective\|D2]] | forced, literature | yes: another model of pursuit gives another standard specification | forced by the steepest climb in a geometry that ignores how finely outcomes are described, and by the best trade-off at a KL price ([[P2 — Every change of behaviour follows a replicator equation\|P2]], [[P4 — What KL measures\|P4]](i), [[P14 — The cost of departing from the default is forced\|P14]]); it is the optimum of KL-regularized training, the logit choice rule and selection |
| stakes in the objective's own units | [[D5 — Stakes\|D5]] | convenience | no: misalignment is in nats either way | the principal reads losses in the units it declared |

## Items, in order
- [[M1 — Probability on finitely many outcomes|M1]] — Probability on finitely many outcomes
- [[M2 — Independent repetition|M2]] — Independent repetition
- [[M3 — Imported theorems|M3]] — Imported theorems
- [[B1 — Finitely many outcomes|B1]] — Finitely many outcomes
- [[B2 — Episodes and conditions as outcomes|B2]] — Episodes and conditions as outcomes
- [[B3 — An objective up to scale and constant|B3]] — An objective up to scale and constant
- [[B4 — One actor and one principal|B4]] — One actor and one principal
- [[A1 — Behaviour suffices|A1]] — Behaviour suffices
- [[A4 — Misalignment is evidence|A4]] — Misalignment is evidence
- [[A5 — Declared before|A5]] — Declared before
- [[D1 — Outcomes, behaviours, divergence and tilt|D1]] — Outcomes, behaviours, divergence and tilt
- [[D2 — Pursuit of an objective|D2]] — Pursuit of an objective
- [[D3 — Specification, declaration and misalignment|D3]] — Specification, declaration and misalignment
- [[D4 — Resolution|D4]] — Resolution
- [[D5 — Stakes|D5]] — Stakes
- [[D6 — Intervention and pass-through|D6]] — Intervention and pass-through
- [[D7 — Feasibility|D7]] — Feasibility
- [[D8 — Conditions, responses and views|D8]] — Conditions, responses and views
- [[D9 — Observation and identification|D9]] — Observation and identification
- [[D10 — Evaluator, regression and residual|D10]] — Evaluator, regression and residual
- [[D11 — Record, sample and evidence|D11]] — Record, sample and evidence

# The core

> **Status: v11, in progress.** The core holds what cannot be derived: five premises, and the definitions that the whole
> framework uses. Everything that follows from them is in `derived/`, with proofs and checks that run in CI. Each item
> carries a formal statement and a plain-terms twin, and gives its lineage from the archive, tagged `v7.10`. The format
> is in `README.md`.

## 0. What the core is

Alignment compares what an actor does with what a principal intended. The core fixes the terms of that comparison and
the few premises it rests on. Section 1 states the premises. Sections 2–10 give the definitions, each with the reasons
for it. The results, which follow from these by proofs, are in `derived/`, whose `README.md` gives their reading order.
A definition may cite a result to justify itself, provided that no chain of dependencies leads back to it.

The framework in ten steps:
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
9. **The evaluator** (section 9). What the actor actually pursues, and what it tells about the principal's objective.
   Derived: through the evaluator, only the regression counts; a monotone regression rules out overoptimization, and a
   single-peaked one allows at most one fall (`derived/evaluator.md`).
10. **Samples and evidence** (section 10). The act of measurement. Derived: misalignment is the rate of evidence
    against the specification; detection, estimation and the evaluation gap (`derived/estimation.md`).

Specifications defined by a structure rather than by an objective need no definition of their own: several actors
meant to act independently, behaviour meant to ignore the situation, a process meant to look the same run backward, and
several principals with declared weights (`derived/structure.md`). What the core rules out, the statements that data
could contradict, is collected in `derived/forbids.md`.

**In scope.** One principal and one actor, where the actor may be a group acting on joint outcomes ([[P39 — Several actors: coordination plus individual misalignment|P39]]) and the
principal several principals with declared weights ([[P42 — Several principals: gridlock, and the pooled pursuit|P42]]); finitely many outcomes; behaviour in each of finitely many
conditions, which may be the measurement rules the actor faces; any declared set of acceptable behaviours, with closed
forms for "pursue `F`" and for the structural specifications of `derived/structure.md`; what the actor cannot
distinguish, cannot do, or cannot perceive; what observation identifies, including misalignment that an actor shows
only when it is not observed; the evaluator an actor pursues, and what pursuing it does to the principal's objective;
and what independent samples reveal, where one sample may be a whole episode of dependent decisions.

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
- *One long record of dependent decisions.* Samples are independent draws ([[D11 — Sample and evidence|D11]]). Decisions that depend on each other
  within an episode are in scope, the episode being one outcome; one long record without episodes needs rates on
  trajectories, which are not finite (`CORE-GENERAL.md`).
- *Which objective is right.* The principal declares it; the core does not choose it.
- *Explanations beyond the evaluator.* Why an actor pursues the evaluator it does, and by what mechanism, is not
  measured. The evaluator itself is in scope, as a hypothesis about behaviour that samples can test ([[D10 — Evaluator, regression and residual|D10]], [[D11 — Sample and evidence|D11]]).

**How to read.** Items are numbered by kind: A for premises and D for definitions, in this file; P for propositions, in
`derived/`. `[[P2 — Every change of behaviour follows a replicator equation|P2]](iii)` means part (iii) of P2. Logarithms are natural, so divergences are in nats. Operations on
functions (`p/r`, `log`, `e^F`) act outcome by outcome. The Notes of each item give the names its objects carry in other
fields.

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
| `M(p̂)` | the misalignment of the actual behaviour `p̂` | [[D3 — Specification, declaration and misalignment\|D3]] |
| `ℬ`, `𝒜` | the principal's resolution; the actor's resolution | [[D4 — Resolution\|D4]] |
| `E_q[F\|𝒜]`, `F̄` | the cell average of `F` under the default | [[D4 — Resolution\|D4]] |
| `λ`, `S(p̂)` | the matched intensity; the shortfall, in the units of `F` | [[D5 — Stakes\|D5]] |
| `u`, `φ` | an intervention; the pass-through | [[D6 — Intervention and pass-through\|D6]] |
| `𝓕` | the actor's feasible set | [[D7 — Feasibility\|D7]] |
| `𝒞`, `(p_c)` | the conditions; the actor's response | [[D8 — Conditions, responses and views\|D8]] |
| `Z`, `V_c` | the actor's view: its signals, and their distribution in condition `c` | [[D8 — Conditions, responses and views\|D8]] |
| `O` | the observed conditions | [[D9 — Observation and identification\|D9]] |
| `F̂`, `m`, `R` | an evaluator; the regression of the target on it; the residual | [[D10 — Evaluator, regression and residual\|D10]] |
| `n`, `p̂_n` | the size of a sample; its empirical behaviour | [[D11 — Sample and evidence\|D11]] |
| `s`, `F_s` | time along a path of behaviours; the objective the change reveals | [[P2 — Every change of behaviour follows a replicator equation\|P2]] |
| `J_t` | net value: the objective's average minus the cost of departing from the default | [[P4 — What KL measures\|P4]] |
| `t*`, `p°` | the revealed intensity; the nearest intended behaviour | [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits\|P5]] |
| `KL(p̂‖q)` | the departure of the actual behaviour from the default | [[P6 — The departure from the default splits into pursuit and misalignment\|P6]] |
| `θ` | the angle between a revealed objective and the declared one | [[P11 — The misaligned share at the start of a change\|P11]] |
| `σ_q(F)` | the spread of `F` under the default: `Var_q(F)^{1/2}` | [[P13 — What the start of a change gains\|P13]] |
| `p*` | the best feasible behaviour | [[P15 — Misalignment splits into what the actor could avoid and what it could not\|P15]] |

## 1. Premises

## Items, in order
- [[A1 — Behaviour suffices|A1]] — Behaviour suffices
- [[A2 — Pursuit is the steepest climb|A2]] — Pursuit is the steepest climb
- [[A3 — Pursuit is the best trade-off|A3]] — Pursuit is the best trade-off
- [[A4 — Misalignment is value lost|A4]] — Misalignment is value lost
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
- [[D11 — Sample and evidence|D11]] — Sample and evidence

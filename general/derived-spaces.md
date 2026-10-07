# General results — derived spaces

`CORE.md` §0 once left out several actors, actors that respond to the measurement, several principals and dependent
samples. Each can become a standard scenario, one principal and one actor, on a derived outcome space. When that space
is finite, the finite core covers the scenario, and its results are proved in `derived/structure.md` ([P39]–[P42]). This
file is about derived spaces that are not finite, which are most of them: long records, the shares of a large
population, continuous measurement rules, models. It also holds the evidence gathered before the finite results were
proved.

## 1. When a lift is honest

Any group of actors has a joint behaviour, so a lift is always possible. It gives a standard scenario only if, on the
derived space, a default can be declared before the behaviour is seen (GA5), the principal's intended behaviours are a
declared specification there (GD3), and records are independent draws, or one long record has a single rate. Where a
condition fails, the failure is what is strategic about the scenario, and most often it can be measured.

| Scenario | Derived outcome space | Derived default | Standard when | What stays strategic |
|---|---|---|---|---|
| dependent decisions | episodes, finite (`CORE.md` §0); trajectories, where infinitely many steps of finitely many outcomes already form a continuum | the process with no pursuit | episodes are independent, or one long record has one rate: the divergence per step | lock-in: each run has a rate, but early chance fixes it (section 5) |
| several actors | joint actions, finite ([P39]); with many actors, the share of each action | the actors acting independently, each from its own default | the principal declares the joint behaviour it intends: independent pursuit, or a pursuit of a potential | coordination ([P39]); learning that goes round in circles, measured by its irreversibility ([P41]) |
| actors that respond to the measurement | the measurement rules, as conditions (GD8); finite rules are conditions of the finite core | the principal's declared randomization over rules | rules are randomized as declared; the response to a change of rule is then bounded by how differently the actor perceives the two rules, where performative prediction assumes such a bound [@perdomo2020] | a principal that changes its rule in response to the actor without having declared how: GA5 fails at every level |
| several principals | the principals, with declared weights ([P42]) | — | the weights are declared | the weights: who counts how much |
| actors that learn | the models a learner can end with | the distribution of models at the start | training is a pursuit of its objective over models | the gap between actual training and a pursuit |

## 2. Structural specifications

Five specifications are defined by a structure rather than by an objective. Misalignment against each is a divergence
with a name, so the framework measures all five in the unit it measures everything in.

| Intended structure | Misalignment against it | On finite outcomes | On spaces that are not finite |
|---|---|---|---|
| independence: each actor pursues its own objective on its own | coordination, plus the actors' own misalignments | proved: [P39] | expected: a rate in time on trajectories. Tested (T3): two tit-for-tat players with 5% errors show `0` in every round and `0.231` nats per round over long records |
| ignoring the situation: the same behaviour in every condition | attention, the mutual information between condition and outcome | proved: [P40] | expected to carry; the identity tested (B7) |
| reversibility: the record looks the same run backward | the Jensen–Shannon divergence from the reversal: at most half the entropy production, a quarter of it at low asymmetry | proved: [P41], for transitions and for Markov chains | tested on learning in games (T4, B1, B2); continuous time expected |
| regularity: smooth ratios to the default | grows like `(D − d)·log(1/w)` with the record's width `w` | — (finite outcomes are regular) | tested (T1) |
| a fixed objective: pursuit | a pursuer of a threshold evaluator never piles behaviour at the threshold | immediate: a tilt by an indicator has a ratio with two values | tested (T2), for a pursuer acting step by step through time |

**Going round in circles.** In log-linear learning, players revise one at a time by a logit rule. In a potential game
its long-run behaviour is the Gibbs law of the potential, a pursuit of the potential on joint actions [@blume1993], and
the process is reversible: its entropy production is `0` (T4: below `10⁻²⁴` in 120 cases). In other games it is not, and
the game's harmonic part [@candogan2011] drives the circulation. On a single cycle, the entropy production is the
cycle's flux times its affinity [@schnakenberg1976]; for log-linear learning in a two-by-two game the affinity is
exactly `t·C`, with `C` the payoff gained around the cycle of single-player deviations, at every intensity (B2: ratio
`1.000000000000`). At low intensity the flux is the affinity divided by the cycle's resistance, the sum of the inverse
edge fluxes, so the entropy production is `(t·C)²` divided by that resistance: `1/64` when each player revises with
probability `½`, a constant probe T4 found before it was derived, and `0.013125` with revision probabilities `0.7` and
`0.3`, predicted before it was computed (B2). So the game sets how hard learners are pushed round the cycle, and the
learning rule only how easily they move: how much a game makes its players go round in circles is its harmonic
circulation, times the intensity, squared, times the conductance of the way they learn.

## 3. Two sources of piles

A pile is an exact value chosen with positive probability, where the default chooses it with probability zero. No
pursuit from a fixed default makes one (section 2), so a pile always says something the evaluator does not explain. Two
mechanisms make them, and where the piles sit tells them apart.
- *Gaming*, at the evaluator's thresholds: an actor that sets outcomes precisely, facing an evaluator with a jump, puts
  mass just on the passing side. The four-hour target, the proficiency cut-offs of the New York Regents exams [@dee2019]
  and round marathon times [@allen2017] are of this kind. The pile is where the principal's measure jumps.
- *An optimized default*, at the actor's own points: an actor with an information cost that chooses its own default, as
  in rational inattention [@matejka2015], ends with a discrete default even when everything else is continuous. In each
  condition its behaviour is still a pursuit of its objective from that default ([P40], Notes). With a uniform situation
  on `[0, 1]` and squared loss at intensity `β` (B3, B3b): one atom below `β_c = 1/(2·Var) = 6` and two just above it,
  the critical point that deterministic annealing predicts for squared loss (Rose; *to verify*); between `√(β/6)` and
  `2·√(β/6)` atoms beyond. The piles sit at the actor's own points, spread over the range: categories, routines, rules
  of thumb.

The atom count of B3 and its dimension slope failed as registered: `3`, `6` and `11` atoms against `2.2`, `4.1` and
`7.1 ± 1`, and a slope of `0.751` against more than `0.9`. The slope failed because the algorithm converges slowly: the
atoms narrow like the inverse square root of the iterations, and the slope rises toward `1` (`0.54`, `0.75`, `0.81`,
`0.84`). The range of atoms, registered after B3 and before its own run, held at new intensities (B3b: `4` atoms at
`β = 50`, `10` at `200`), and so did the critical intensity (between `5.85` and `6.15`).

## 4. Several principals

Under standard specifications from one default, the default is intended by every principal, so it is always a best
compromise: gridlock ([P42](i)). With declared intensities the compromise is the pursuit of the weights times
intensities times objectives, added up ([P42](ii)). With floors ([P35]) a probe found the compromise to be the same kind
of pursuit, with each principal's intensity that of its nearest intended behaviour (T5), often at the floors but not
always: in 11 of 20 random instances, against a predicted 15 at least (T5b, failed). The weights stay a declaration.

## 5. Lock-in

A record of a process that locks in, such as a Pólya urn, has a rate in every run, but early chance fixes it. Against
independent fair draws, each run's rate is the divergence of its final share from one half, within `3.5·10⁻⁴`, and over
400 runs the rates have mean `0.199` and standard deviation `0.185` (T6). What fails is that one rate describes the
actor, not that a rate exists.

## 6. What does not lift

Internal states and beliefs about beliefs. A space for them exists, the universal type space, but no default on it can
be observed, so no lift can be declared (GA5), and they stay out of scope by GA1.

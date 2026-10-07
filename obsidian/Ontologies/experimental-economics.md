# Ontology — experimental economics: learning in games

In a laboratory game, the experimenter declares the game and a hypothesis about how the players learn; a population of
subjects plays it. The experimenter is the principal and the population, taken together, is the actor: its outcome is
the mix of strategies in play ([[P39 — Several actors: coordination plus individual misalignment|P39]]). A game whose payoffs follow one potential can be learned by pursuing that
potential, and such learning looks the same run backward ([[P41 — Reversibility: the Jensen–Shannon divergence from the reversal|P41]], Notes). A game with a cycle of best responses, such as
Rock–Paper–Scissors, has no potential, and its learning goes round in circles. Experiments record the population mix
moment by moment, so the difference is a number: the Jensen–Shannon divergence between the record of transitions and its
reversal. One known result is reframed: cycles in a Rock–Paper–Scissors population game played in continuous time.

## 1. Slots

| Slot | Core | In this discipline | Observed as | Fit |
|---|---|---|---|---|
| **outcomes** | [[D1 — Outcomes, behaviours, divergence and tilt\|D1]] | the population mix, the number of the group's players using each strategy: 45 mixes for 8 players and 3 strategies; for [[P41 — Reversibility: the Jensen–Shannon divergence from the reversal\|P41]], a transition, the pair of mixes at two successive moments of a declared step | the players' strategies, recorded moment by moment | exact for the mix; approximate for transitions, since the step is declared |
| **contexts** | [[D8 — Conditions, responses and views\|D8]] | the treatment, its payoff matrix; the session and the group | the design | exact |
| **behaviour** | [[D1 — Outcomes, behaviours, divergence and tilt\|D1]] | the frequencies of the transitions between mixes over a session, per treatment | the recorded strategies | exact as frequencies |
| **sample** | [[D11 — Sample and evidence\|D11]] | one transition | the recorded strategies | approximate: successive transitions form a chain, and a session's transitions depend on each other; error bars are computed by group |
| **default** | [[D2 — Pursuit of an objective\|D2]] | play with no regard to payoffs: each player's strategy uniform and independent of the others' | none: a design choice, declared before the experiment | assumed |
| **objective** | [[D2 — Pursuit of an objective\|D2]] | each player's payoff, given the mix it faces; for a game with a potential, the potential, which every player's payoff change follows | the payoff matrix | exact for payoffs; the potential exists only for some games |
| **evaluator** | [[D10 — Evaluator, regression and residual\|D10]] | the payoffs the subjects receive, a known function of their strategy and of the mix | the payoff matrix | exact |
| **intensity** | [[D2 — Pursuit of an objective\|D2]] | how sharply players respond to payoff differences | estimated from the choices, as a logit precision | approximate |
| **specification** | [[D3 — Specification, declaration and misalignment\|D3]] | the experimenter's hypothesis that the population learns by pursuing one fixed objective on joint play, which the core tests through what such learning implies: a reversible record of transitions ([[P41 — Reversibility: the Jensen–Shannon divergence from the reversal\|P41]]), and a path whose revealed objective does not turn ([[P3 — A fixed objective is visible in the changes of behaviour\|P3]]) | the pre-registered hypothesis | assumed: the hypothesis is the experimenter's |
| **principal's resolution** | [[D4 — Resolution\|D4]] | the mix, not which player plays what: players are interchangeable by design | the design | exact |
| **actor's resolution** | [[D4 — Resolution\|D4]] | players see the current mix, or the payoff of each strategy against it, on their screens | the software | approximate: what a player attends to is not recorded |
| **change** | [[P2 — Every change of behaviour follows a replicator equation\|P2]] | the path of the mix over a session; around a cycle, its revealed objective turns | the recorded strategies | approximate: the path is sampled at the declared step |
| **intervention** | [[D6 — Intervention and pass-through\|D6]] | a change of the payoff matrix between treatments: a known change of every payoff | the design | exact |
| **stakes** | [[D5 — Stakes\|D5]] | the payoff points, converted to money | the payment records | exact |

## 2. Known result

Cason, Friedman and Hopkins ran Rock–Paper–Scissors population games in continuous time: groups of eight subjects, each
matched against the whole group, could change strategy at any moment, and a heat map showed each strategy's current
payoff [[References|@cason2014]]. Evolutionary game theory predicts cycles in the population mix for such games, and the experiment
found them. Blume showed that log-linear learning, in which players revise one at a time by a logit rule, has the Gibbs
law of the potential as its long-run behaviour in games that have one [[References|@blume1993]]: a pursuit of the potential, which is
reversible.

**Data.** The experiments record every subject's strategy moment by moment, so the mix and its transitions can be
counted at any declared step. Whether Cason et al.'s records are public has not been checked; the paper's figures and
summaries are seen. New sessions under the same protocol are cheap to run, and the potential-game arm of the prediction
below is new.

## 3. What the core says

- **Consequence** of [[P41 — Reversibility: the Jensen–Shannon divergence from the reversal|P41]]: the irreversibility of a group's learning is a number, the Jensen–Shannon divergence between
  its record of transitions between mixes and the reversal of that record. It is zero exactly when the record looks the
  same run backward, and at most half the entropy production.
- **Consequence** of [[P3 — A fixed objective is visible in the changes of behaviour|P3]]: read as shares of the strategies in play, a population that pursues one fixed objective moves
  along a path whose revealed objective keeps one direction, with an intensity that never falls. A path that moves and
  comes back to where it started would need its intensity to rise and fall again, so play that cycles pursues no fixed
  objective, whatever the players intend.
- **Prediction** (empirical) from [[P41 — Reversibility: the Jensen–Shannon divergence from the reversal|P41]]: under the same continuous-time protocol, in a game with an exact potential,
  such as a pure coordination game, the Jensen–Shannon divergence of the record of transitions from its reversal is zero
  within its sampling error, while in a Rock–Paper–Scissors game it is positive. *Refuted if* the potential game's
  record is irreversible beyond sampling error, computed by group, or the Rock–Paper–Scissors record is not. A
  refutation in the potential game would mean that the subjects do not learn by pursuing the potential, for instance
  because they hold on to strategies or chase patterns. The Rock–Paper–Scissors arm is seen in summary; the potential
  arm is new.
- **Reading** with [[D6 — Intervention and pass-through|D6]]: a treatment that changes the payoff matrix is an intervention with a known effect on every
  payoff; how much it changes the irreversibility of play measures how the game's cycle, not the players, drives the
  circulation.

## 4. Limits

- Eight players give 45 mixes, and the transitions between them are counted at a declared step: a longer step loses
  moves, a shorter one leaves most transitions empty. The step is declared before the data are read.
- Subjects learn the game during a session, so the chain of transitions is not stationary; [[P41 — Reversibility: the Jensen–Shannon divergence from the reversal|P41]](iv) assumes a
  stationary chain, and the early part of a session may have to be set aside, as declared in advance.
- Reversibility follows from pursuing a potential for log-linear learning; other learning rules, such as best responses
  with inertia, may break it in a potential game without any departure from pursuit.
- Transitions within one session depend on each other, and the core's estimation assumes independent samples ([[D11 — Sample and evidence|D11]]):
  one session is one long record, outside the scope (`CORE.md` §0). The groups are the independent samples, and error
  bars are computed by group.

## 5. Open questions

- Does irreversibility grow with the game's circulation, its payoff gained around the cycle of best responses, as the
  law found for learning by logit responses suggests (`general/derived-spaces.md`)?
- Can the game's harmonic part, computed from the payoff matrix before any session, predict how strongly a group will
  cycle?
- Is the coordination of players' strategies within a group ([[P39 — Several actors: coordination plus individual misalignment|P39]]) zero in Rock–Paper–Scissors, with all the structure
  in time?

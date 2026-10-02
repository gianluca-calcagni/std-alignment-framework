# Related theories

Theories that share objects or aims with this framework. The word "competitor" is used loosely: overlap is welcome,
because it validates the approach and gives results to import. For each theory: what it shares with us and with which
items, what differs, what we should import, what it could take from us, and the state of its sources. A source cited
with a key in brackets is verified and listed in `REFERENCES.md`; one marked *(to verify)* is from memory and must be
checked before an item cites it. Lint rule R12 checks that this file names only existing items and cites only listed
sources.

**Import priority.** *Now*: needed by the next items of the core. *Later*: useful once a later item needs it.
*Never*: outside the framework's scope, recorded so the question is not reopened. *Done*: imported, with the items
that carry it.

## Overview

| Theory | Shares with us | The main difference | Import |
|---|---|---|---|
| KL control and control as inference | pursuit, net value, the maximum-entropy policy | it optimizes; we measure | later: soft dynamic programming for sequential feasibility |
| Information geometry | the Fisher metric, I-projections, Pythagorean identities | no principal, no specification | now: the geometry of two objectives (the alignment plane) |
| The Price equation and selection theory | the replicator equation, the covariance form of change | descriptive; no specification | now: selection gradients as evaluators |
| Bounded rationality and discrete choice | the logit rule as a pursuit; a KL cost | the default is chosen by the agent | later: an endogenous default |
| Inverse RL and reward identifiability | objectives revealed up to a constant; identification | recovers rewards, does not score misalignment | now: identification across environments |
| Goodhart's law and reward hacking | evaluator and target; overoptimization | rankings and worst cases, not a divergence | done: the evaluator ([[D10 — Evaluator, regression and residual\|D10]], [[P18 — Through the evaluator, only the regression counts\|P18]]–[[P20 — Where overoptimization starts, and how it ends\|P20]]); later: early stopping compared, hackability over a feasible set |
| Principal–agent theory | delegation, performance measures, pass-through | equilibrium contracts, risk and payments | later: the angle of a performance measure |
| Identification and causal inference | identified sets, interventions | no notion of misalignment | now: sharp identified sets |
| Hypothesis testing and sequential analysis | KL as a rate of evidence | a theory of tests, not of alignment | done: sampling, evidence, detection and estimation ([[D11 — Sample and evidence\|D11]], [[P21 — The expected evidence is misalignment\|P21]]–[[P23 — The estimated misalignment of an actor that pursues the objective\|P23]]); later: Stein's exponent, the boundary case |
| Deceptive alignment and AI evaluation | behaviour that differs when unobserved | intent-based definitions | later: audit protocols |
| Distribution shift | bounds across conditions | prediction error, not misalignment | later: divergence-based transfer bounds |
| Active inference | a KL from predicted to preferred outcomes | a process theory of brains | never, beyond the correspondence |
| Formal specification | specifications as sets, fixed in advance | deterministic traces | later: quantitative semantics |
| Social choice | several principals | aggregation of preferences | never, while several principals are out of scope |
| Metrology and reporting standards | a standard for reports | not about alignment | now: how to report uncertainty |

## KL control and control as inference

- *Sources.* Rafailov et al. [[References|@rafailov2023]]; Ziebart et al. [[References|@ziebart2008]]; Todorov's linearly solvable control and
  Levine's review of control as inference *(to verify)*.
- *Shared.* Pursuit is the KL-regularized optimum ([[D2 — Pursuit of an objective|D2]], [[P4 — What KL measures|P4]](i)). The maximum-entropy policy is the best feasible
  behaviour in a random environment ([[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]], Notes).
- *Different.* These theories compute optimal behaviour. We judge actual behaviour against declared behaviour, and
  report stakes and identification.
- *Import, later.* Soft dynamic programming, to state [[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]]'s sequential case as an item of its own.
- *What it could take from us.* The split of the KL "budget" into pursuit and misalignment ([[P6 — The departure from the default splits into pursuit and misalignment|P6]]), and of misalignment
  into avoidable and unavoidable parts ([[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]]).

## Information geometry

- *Sources.* Čencov [[References|@cencov1982]]; Campbell [[References|@campbell1986]]; Csiszár [[References|@csiszar1975]]; Amari's monographs *(to verify)*.
- *Shared.* The Fisher metric and its uniqueness ([[A2 — Pursuit is the steepest climb|A2]], [[P2 — Every change of behaviour follows a replicator equation|P2]]); I-projections and the Pythagorean theorem ([[P6 — The departure from the default splits into pursuit and misalignment|P6]], [[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]]);
  the second-order expansion of KL ([[P11 — The misaligned share at the start of a change|P11]], [[P13 — What the start of a change gains|P13]]).
- *Different.* No principal and no specification: the geometry is the same, the question is not.
- *Import, now.* The dual (mixture and exponential) flat structures, for the two-parameter family spanned by a target
  and an evaluator through the default (`NOTES.md` §5, H6).
- *What it could take from us.* An interpretation of its projections as value lost, avoidable and unavoidable.

## The Price equation and selection theory

- *Sources.* Price [[References|@price1970]]; Shahshahani [[References|@shahshahani1979]]; Frank's Price equation programme [[References|@frank2018]];
  Robertson's secondary theorem and Lande and Arnold's selection gradients *(to verify)*.
- *Shared.* The revealed objective as Malthusian fitness and the replicator equation as a Fisher gradient ([[P2 — Every change of behaviour follows a replicator equation|P2]]); the
  covariance form of change ([[P13 — What the start of a change gains|P13]](i)). Frank argues that these invariances unify selection, thermodynamics and
  inference, an ambition close to ours.
- *Different.* Descriptive: it says how a population changes, not whether the change is what someone intended.
- *Import, now.* Selection gradients as evaluators, and the breeder's setting (a trait against fitness) as the model
  case of a target against an evaluator. *Later:* Frank's separation of forces, for paths that are not pursuits.
- *What it could take from us.* Specification, misalignment and the stakes of selection that is not aligned with a
  declared trait (the evolutionary-biology ontology's shortfall of ordinary selection).

## Bounded rationality and discrete choice

- *Sources.* McKelvey and Palfrey [[References|@mckelvey1995]]; Ortega and Braun [[References|@ortega2013]]; Matějka and McKay [[References|@matejka2015]];
  Sims's rational inattention *(to verify)*.
- *Shared.* The logit rule and quantal response are pursuits ([[D2 — Pursuit of an objective|D2]]); free energy is the net value ([[P4 — What KL measures|P4]]). Matějka and
  McKay derive the multinomial logit from a cost of information, an independent route to the KL cost of [[P14 — The cost of departing from the default is forced|P14]].
- *Different.* In rational inattention the default (the prior over choices) is chosen optimally and the cost is a
  mutual information; here the default is declared ([[A5 — Declared before|A5]]).
- *Import, later.* An endogenous default, as a derived case: when the default is itself optimal, which quantities
  change?
- *What it could take from us.* A measure of how far observed choices are from a declared intention, with its stakes.

## Inverse reinforcement learning and reward identifiability

- *Sources.* Ng and Russell [[References|@ng2000]]; Ziebart et al. [[References|@ziebart2008]]; work on partial identifiability of rewards by
  Skalse and coauthors, and by Cao, Cohen and Szpruch *(to verify)*.
- *Shared.* A behaviour reveals its objective only up to a constant, and with an intensity only the product
  ([[P1 — Every behaviour is a tilt of any other|P1]]); the revealed intensity is the maximum-entropy fit ([[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]]); identification needs variation in conditions
  ([[D9 — Observation and identification|D9]], [[P12 — What interventions reveal|P12]]).
- *Different.* These theories aim to recover rewards. We take the principal's objective as declared and measure the
  distance to it; we need the actor's objective only as the evaluator.
- *Import, now.* Identification of an objective across several environments, which in our terms are conditions
  ([[D8 — Conditions, responses and views|D8]]) or interventions ([[D6 — Intervention and pass-through|D6]]); the invariance classes of rewards that leave optimal behaviour unchanged.
- *What it could take from us.* A measure of how much an unidentified part of the reward matters: its effect on
  misalignment and stakes.

## Goodhart's law and reward hacking

- *Sources.* Gao et al. [[References|@gao2023]]; Skalse et al. [[References|@skalse2022]]; Karwowski et al. [[References|@karwowski2024]]; Laidlaw et al.
  [[References|@laidlaw2025]], who define a proxy by its correlation with the target under a reference policy and propose `χ²`
  regularization of occupancy measures, the `χ²` row of [[P31 — Budgets of other shapes|P31]] with the correlation of [[P13 — What the start of a change gains|P13]] (unlike KL, a `χ²` cost can
  rule outcomes out at the optimum: [[P38 — Any convex cost|P38]](ii)); Manheim and
  Garrabrant's taxonomy, Zhuang and Hadfield-Menell on unmentioned attributes, El-Mhamdi and Hoang on weak and strong
  Goodhart *(to verify)*.
- *Shared.* An evaluator that differs from the target, and what pursuing it does to the target ([[D10 — Evaluator, regression and residual|D10]]). Karwowski et al.
  explain Goodhart by angles between reward vectors in the polytope of occupancy measures: a linear feasible set ([[D7 — Feasibility|D7]])
  and the angle of [[P11 — The misaligned share at the start of a change|P11]]. Skalse et al. show that over all stochastic policies only trivial pairs are unhackable.
- *Different.* Rankings, worst cases and orderings over policy sets, rather than a divergence with stakes and
  identification.
- *Import, done.* The evaluator, with the decomposition of the target into its regression on the evaluator and a
  residual ([[D10 — Evaluator, regression and residual|D10]], [[P18 — Through the evaluator, only the regression counts|P18]]); a stopping rule, where the target and the evaluator become uncorrelated under the current
  behaviour ([[P20 — Where overoptimization starts, and how it ends|P20]](i)).
- *Import, later.* Whether Karwowski et al.'s early stopping is the rule of [[P20 — Where overoptimization starts, and how it ends|P20]](i) (`TERMS.md`, section 2, level B);
  hackability as a property of a target and an evaluator over a feasible set; Manheim and Garrabrant's
  four variants, once their definitions are checked against [[P8 — An actor that cannot tell outcomes apart|P8]], [[P20 — Where overoptimization starts, and how it ends|P20]](ii), [[P12 — What interventions reveal|P12]] and [[P17 — What an unobserved condition can hide|P17]] (`NOTES.md` §5, H3).
- *What it could take from us.* Exact results for actors that see only the evaluator: a monotone regression rules out
  overoptimization ([[P19 — A monotone regression rules out overoptimization|P19]]), so a proxy that only averages the target over what it can tell apart cannot lower it, and
  neither can a pass-or-fail verifier whose passing outcomes are better on average (`ontologies/machine-learning/`);
  the terminal rule of [[P20 — Where overoptimization starts, and how it ends|P20]](ii); and the shape law of [[P25 — The target's curve turns no more often than the regression|P25]]: the target's curve turns no more often than the
  regression, so a single-peaked regression gives at most one overoptimization peak, for pursuit and for best-of-`n`
  alike. Whether Manheim and Garrabrant's regressional variant (proxy equals target plus
  noise) has a monotone regression depends on the noise, which is a question for their definitions. For an evaluator
  known in the target's units, the exact worst cases of the target lost, within a departure budget ([[P29 — The width is the exact worst case|P29]]) and among
  shared candidates such as best-of-`n` ([[P34 — Choosing by the evaluator from a common candidate set|P34]]); and no ranking of errors that holds at every budget ([[C1 — No ranking of errors holds at every budget|C1]]).

## Principal–agent theory

- *Sources.* Holmström [[References|@holmstrom1979]]; Holmström and Milgrom [[References|@holmstrom1991]]; Kerr [[References|@kerr1975]]; Frey and Jegen
  [[References|@frey2001]]; Gneezy and Rustichini [[References|@gneezy2000]]; Baker's distortion of performance measures *(to verify)*.
- *Shared.* Delegation, a performance measure that differs from value, and the response to incentives
  ([[D6 — Intervention and pass-through|D6]], [[P12 — What interventions reveal|P12]]); the medical-sciences ontology, where the measures are written rules.
- *Different.* These theories solve for optimal contracts, with risk, participation and the cost of pay. We measure,
  and do not model the principal's optimization.
- *Import, later.* Baker's alignment of a performance measure as an angle between marginal effects, if it is the angle
  of [[P11 — The misaligned share at the start of a change|P11]] (`NOTES.md` §5, H8); the informativeness principle as a statement about the principal's observation.
- *What it could take from us.* A measure of misalignment that needs no model of the agent's preferences.

## Identification and causal inference

- *Sources.* Manski [[References|@manski2003]]; Pearl's causal models, and causal analyses of agent incentives by Everitt, Carey and
  coauthors *(to verify)*.
- *Shared.* Identified and identified sets ([[D9 — Observation and identification|D9]]); interventions as designed changes of condition ([[D6 — Intervention and pass-through|D6]]); bounds from
  assumptions rather than point estimates ([[P17 — What an unobserved condition can hide|P17]]).
- *Different.* No notion of misalignment or of a specification.
- *Import, now.* Sharp identified sets; instrumental variables as a model for interventions that change only one
  thing.
- *What it could take from us.* Misalignment and stakes as targets of identification.

## Hypothesis testing and sequential analysis

- *Sources.* Cover and Thomas [[References|@cover2006]] (Stein's lemma, Chernoff information); Wald [[References|@wald1945]]; Chernoff
  [[References|@chernoff1952]]; Wilks [[References|@wilks1938]].
- *Shared.* KL is the expected evidence per observation under the true behaviour ([[D11 — Sample and evidence|D11]], [[P21 — The expected evidence is misalignment|P21]]); `2n·M(p̂)` is a
  likelihood-ratio statistic ([[P23 — The estimated misalignment of an actor that pursues the objective|P23]]).
- *Different.* A theory of tests; it does not define alignment.
- *Import, done.* Sampling, as the act of measurement that connects behaviours to data ([[D11 — Sample and evidence|D11]]), with evidence ([[P21 — The expected evidence is misalignment|P21]],
  Wald in its Notes), detection ([[P22 — No test detects misalignment faster than misalignment|P22]], Chernoff) and estimation ([[P23 — The estimated misalignment of an actor that pursues the objective|P23]], Wilks) as derived results.
- *Import, later.* Stein's exponent, for a test that fixes the error of one kind; the chi-bar-square limit at the
  boundary `t* = 0`; confidence sets for the other quantities of the standard.
- *What it could take from us.* Misalignment as the quantity a test of "the actor behaves as intended" is about.

## Deceptive alignment and AI evaluation

- *Sources.* Hubinger et al. on risks from learned optimization, the sleeper agents study, studies of evaluation
  awareness, and Ward et al.'s causal definition of deception *(to verify)*.
- *Shared.* An actor that behaves differently when it is observed ([[D8 — Conditions, responses and views|D8]], [[D9 — Observation and identification|D9]], [[P16 — An actor cannot behave more differently than it can tell conditions apart|P16]], [[P17 — What an unobserved condition can hide|P17]]).
- *Different.* Several of these define deception by beliefs or intent, internal states that the core does not judge
  ([[A1 — Behaviour suffices|A1]]). We bound what an unobserved condition can hide from what the actor can perceive.
- *Import, later.* Audit protocols, trigger studies and measured evaluation awareness, as estimates of the divergence
  between views.
- *What it could take from us.* Identified bounds, and the design rule of [[P17 — What an unobserved condition can hide|P17]](iv): audits that the actor cannot tell
  from real use identify real use. A behavioural form of faked alignment, with no model of intent: an incentive met
  only in evaluation, pointing where the target does, drives the misalignment seen in evaluation to zero, and two
  actors that pass it through alike become indistinguishable at an exponential rate ([[P37 — A strong incentive masks the actor, and can fake alignment|P37]]).

## Distribution shift

- *Sources.* Domain adaptation bounds (Ben-David and coauthors) and covariate shift *(to verify)*.
- *Shared.* Behaviour in one condition bounded by behaviour in another and a divergence between them ([[P17 — What an unobserved condition can hide|P17]]); v7.10's
  evaluation gap (Prop 19), which shifts the weights of conditions.
- *Different.* Bounds on prediction error, not on misalignment.
- *Import, later.* Divergences other than KL for transfer bounds, which may narrow [[P17 — What an unobserved condition can hide|P17]]'s identified set.

## Active inference

- *Sources.* Friston and coauthors *(to verify)*.
- *Shared.* Its "risk" term is a KL from predicted to preferred outcomes, the direction of misalignment ([[D3 — Specification, declaration and misalignment|D3]]).
- *Different.* A process theory of brains, with commitments the framework does not need.
- *Import, never* beyond recording the correspondence (`NOTES.md` §5, H7).

## Formal specification

- *Sources.* Quantitative semantics of temporal logics *(to verify)*.
- *Shared.* A specification as a set of acceptable behaviours, fixed in advance ([[D3 — Specification, declaration and misalignment|D3]], [[A5 — Declared before|A5]]).
- *Different.* Deterministic traces and satisfaction degrees, not distributions.
- *Import, later.* A case in which a robustness degree and misalignment order behaviours alike (`TERMS.md` §2).

## Social choice

- *Shared.* The question of several principals.
- *Different.* It aggregates preferences, which the core declares out of scope.
- *Import, never*, while several principals are out of scope; unions and intersections of intended sets need no import.

## Metrology and reporting standards

- *Sources.* The Guide to the Expression of Uncertainty in Measurement, and reporting checklists for trials *(to
  verify)*.
- *Shared.* A standard says what a report must declare and contain (`STANDARD.md`).
- *Different.* Not about alignment.
- *Import, now.* How to state uncertainty, now that sampling is in the framework ([[D11 — Sample and evidence|D11]]): the uncertainty of each
  estimated result in `STANDARD.md` should follow a recognized convention.

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
| KL control and control as inference | pursuit, net value, the maximum-entropy policy | it optimizes; we measure | tested on unseen data: is a PPO-tuned model the pursuit of its reward (W3, in part); later: soft dynamic programming for sequential feasibility |
| Information geometry | the Fisher metric, I-projections, Pythagorean identities | no principal, no specification | done: total correlation and the Jensen–Shannon divergence as misalignments ([[P39 — Several actors: coordination plus individual misalignment\|P39]], [[P41 — Reversibility: the Jensen–Shannon divergence from the reversal\|P41]]); nested I-projections split misalignment into named and unexplained parts ([[P44 — What named objectives explain\|P44]]); now: the alignment plane, exact for a Gaussian default (`general/`) |
| The Price equation and selection theory | the replicator equation, the covariance form of change | descriptive; no specification | now: selection gradients as evaluators |
| Bounded rationality and discrete choice | the logit rule as a pursuit; a KL cost | the default is chosen by the agent | done: attention as mutual information ([[P40 — Attention: misalignment against ignoring the situation\|P40]]); tested in part: an endogenous default (`general/`) |
| Inverse RL and reward identifiability | objectives revealed up to a constant; identification | recovers rewards, does not score misalignment | now: identification across environments |
| Goodhart's law and reward hacking | evaluator and target; overoptimization | rankings and worst cases, not a divergence | done: the evaluator ([[D10 — Evaluator, regression and residual\|D10]], [[P18 — Through the evaluator, only the regression counts\|P18]]–[[P20 — Where overoptimization starts, and how it ends\|P20]]); tested on unseen data: the best-of-`n` form against [[P13 — What the start of a change gains\|P13]] (W1, refuted); probed: heavy tails and the χ² angle law (`general/`); later: early stopping compared, hackability over a feasible set |
| Principal–agent theory | delegation, performance measures, pass-through | equilibrium contracts, risk and payments | later: the angle of a performance measure |
| Identification and causal inference | identified sets, interventions | no notion of misalignment | now: sharp identified sets |
| Hypothesis testing and sequential analysis | KL as a rate of evidence | a theory of tests, not of alignment | done: sampling, evidence, detection and estimation ([[D11 — Sample and evidence\|D11]], [[P21 — The expected evidence is misalignment\|P21]]–[[P23 — The estimated misalignment of an actor that pursues the objective\|P23]]); the cost of reweighting ([[P47 — The cost of reweighting\|P47]]); later: Stein's exponent, the boundary case |
| Deceptive alignment and AI evaluation | behaviour that differs when unobserved | intent-based definitions | done: across runs, differences between evaluation and use split into reproducible and run-specific parts ([[P46 — What runs share between conditions, and what they do not\|P46]]); later: audit protocols |
| Distribution shift | bounds across conditions | prediction error, not misalignment | later: divergence-based transfer bounds |
| Active inference | a KL from predicted to preferred outcomes | a process theory of brains | never, beyond the correspondence |
| Formal specification | specifications as sets, fixed in advance | deterministic traces | tested: a robustness degree that orders as misalignment does (`general/`); later: quantitative semantics |
| Learning in games and algorithmic collusion | several actors, potential games, learning dynamics | equilibria and their selection | done: a group as one actor ([[P39 — Several actors: coordination plus individual misalignment\|P39]]), reversible learning in potential games ([[P41 — Reversibility: the Jensen–Shannon divergence from the reversal\|P41]], Notes) |
| Network theory of irreversible processes | entropy production, cycle fluxes and affinities | thermodynamics of Markov chains, no principal | done: entropy production bounds the Jensen–Shannon divergence ([[P41 — Reversibility: the Jensen–Shannon divergence from the reversal\|P41]]) |
| Social choice | several principals | aggregation of preferences | never for the weights; several principals with declared weights are in scope ([[P42 — Several principals: gridlock, and the pooled pursuit\|P42]]) |
| Metrology and reporting standards | a standard for reports | not about alignment | now: how to report uncertainty |

## KL control and control as inference

- *Sources.* Rafailov et al. [[References|@rafailov2023]]; Ziebart et al. [[References|@ziebart2008]]; Todorov's linearly solvable control and
  Levine's review of control as inference *(to verify)*.
- *Shared.* Pursuit is the KL-regularized optimum ([[D2 — Pursuit of an objective|D2]], [[P4 — What KL measures|P4]](i)). The maximum-entropy policy is the best feasible
  behaviour in a random environment ([[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]], Notes).
- *Different.* These theories compute optimal behaviour. We judge actual behaviour against declared behaviour, and
  report stakes and identification.
- *Tested on unseen data* (case W3, `cases/w3-ppo-pursuit/`): whether a policy tuned by PPO with a KL penalty, a public
  GPT-2 tuned on a sentiment reward by von Werra et al.'s library [[References|@vonwerra2020]], is the KL-regularized optimum that
  these theories compute. In part: the change follows the reward in the reward's own scale, with a slope near `1/β`, but
  within prompts the reward explains only a third of the change, and about a tenth within each model's own outputs. The
  optimum is what a run aims at, not what it delivers; the framework measures the gap.
- *Import, later.* Soft dynamic programming, to state [[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]]'s sequential case as an item of its own.
- *What it could take from us.* The split of the KL "budget" into pursuit and misalignment ([[P6 — The departure from the default splits into pursuit and misalignment|P6]]), and of misalignment
  into avoidable and unavoidable parts ([[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]]).

## Information geometry

- *Sources.* Čencov [[References|@cencov1982]]; Campbell [[References|@campbell1986]]; Csiszár [[References|@csiszar1975]]; Amari's monographs *(to verify)*.
- *Shared.* The Fisher metric and its uniqueness ([[A2 — Pursuit is the steepest climb|A2]], [[P2 — Every change of behaviour follows a replicator equation|P2]]); I-projections and the Pythagorean theorem ([[P6 — The departure from the default splits into pursuit and misalignment|P6]], [[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]]);
  the second-order expansion of KL ([[P11 — The misaligned share at the start of a change|P11]], [[P13 — What the start of a change gains|P13]]); total correlation, the misalignment of several actors against
  independent pursuit ([[P39 — Several actors: coordination plus individual misalignment|P39]]); the Jensen–Shannon divergence, the misalignment of a record of transitions against
  reversibility, where the nearest reversible record is the midpoint of the record and its reversal ([[P41 — Reversibility: the Jensen–Shannon divergence from the reversal|P41]]).
- *Different.* No principal and no specification: the geometry is the same, the question is not.
- *Import, done.* Total correlation ([[P39 — Several actors: coordination plus individual misalignment|P39]]) and the Jensen–Shannon divergence ([[P41 — Reversibility: the Jensen–Shannon divergence from the reversal|P41]]); the bound of the latter by half
  the entropy production is Jeffreys' divergence bound. Probe B1 found the midpoint to be the nearest reversible record
  before [[P41 — Reversibility: the Jensen–Shannon divergence from the reversal|P41]] proved it.
- *Import, now.* The dual (mixture and exponential) flat structures, for the two-parameter family spanned by a target
  and an evaluator through the default (`NOTES.md` §5, H6). For a Gaussian default and linear objectives the plane is
  exact: the departure splits like a right triangle, `cos²θ` into the target and `sin²θ` into misalignment, at every
  intensity (probe B5, `general/transfer.md`). With other defaults the law is local only, and B5's registered
  exponential case failed as posed, at an intensity where pursuit does not exist. Whether [[P41 — Reversibility: the Jensen–Shannon divergence from the reversal|P41]](iv) is the mixture
  projection of the information geometry of Markov chains has not been searched for.
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
- *Import, done.* The information cost: misalignment against ignoring the situation is the mutual information between
  the condition and the response, and the average response is the nearest default to all conditions at once ([[P40 — Attention: misalignment against ignoring the situation|P40]]).
- *Import, tested in part.* An endogenous default (probes B3, B3b; `general/derived-spaces.md`). On a continuum, the
  optimized default is discrete: for a state uniform on `[0, 1]` and squared loss, one atom until the precision `β`
  reaches `1/(2·Var) = 6`, where it splits, and between `√(β/6)` and `2·√(β/6)` atoms after that (B3b, held). B3's
  registered atom counts failed (3, 6 and 11 against 2.2, 4.1 and 7.1 ± 1), and its dimension slope did too, from the
  algorithm's slow convergence; both failures are recorded. Not claimed until proved.
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

- *Sources.* Gao et al. [[References|@gao2023]]; Coste et al. [[References|@coste2024]], whose released answers W1 used; Skalse et al.
  [[References|@skalse2022]]; Karwowski et al. [[References|@karwowski2024]]; Laidlaw et al. [[References|@laidlaw2025]], who define a proxy by its correlation
  with the target under a reference policy and propose `χ²` regularization of occupancy measures, the `χ²` row of [[P31 — Budgets of other shapes|P31]]
  with the correlation of [[P13 — What the start of a change gains|P13]] (unlike KL, a `χ²` cost can rule outcomes out at the optimum: [[P38 — Any convex cost|P38]](ii)); Manheim and
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
- *Tested on unseen data* (case W1, `cases/w1-best-of-n-slope/`): Gao et al.'s best-of-`n` form `d·(a − b·d)`,
  fitted over the usual range, overstates the initial slope that [[P13 — What the start of a change gains|P13]] computes from the initial policy, by 22%, on
  12.6 million of Coste et al.'s answers with a proxy built here. The curve keeps [[P13 — What the start of a change gains|P13]]'s slope up to `n = 16` and then
  saturates (exploratory), so the form's two numbers misstate both the start and the shape.
- *Import, tested* (probes B4, B5; `general/transfer.md`). Under a default with a power-law upper tail, a KL budget
  buys unbounded gain, the case of Kwa et al. [[References|@kwa2024]], while a χ² budget `B` buys exactly `√(B·Var)`. Under χ²,
  Laidlaw et al.'s correlated proxy gains `√B·ρ·sd` in the target for every default; under KL the same law is exact
  only for Gaussian defaults. These are statements about outcomes that are not finite, and claimed nowhere yet.
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
- *Import, tested* (probe B6, `general/transfer.md`). The case in which a robustness degree and misalignment order
  behaviours alike (`TERMS.md` §2): an actor that aims deterministically at a margin `r` inside a threshold, blurred by
  noise of size `σ`, judged by "pass with probability at least `1 − α`", has misalignment that depends on `r/σ` alone,
  never increases with `r`, and vanishes from `r = σ·Φ⁻¹(1 − α)`. Robustness counts in units of the actor's noise.
- *Import, later.* Quantitative semantics for temporal properties of whole episodes, each episode one outcome.

## Learning in games and algorithmic collusion

- *Sources.* Blume [[References|@blume1993]]; Candogan et al. [[References|@candogan2011]]; Calvano et al. [[References|@calvano2020]]; Cason et al.
  [[References|@cason2014]]; Assad et al. [[References|@assad2024]].
- *Shared.* Several actors, read as one actor on joint outcomes ([[P39 — Several actors: coordination plus individual misalignment|P39]]). Log-linear learning in a potential game is a
  pursuit of the potential and is reversible; in a game with a harmonic part, learning circulates ([[P41 — Reversibility: the Jensen–Shannon divergence from the reversal|P41]], Notes).
  Algorithms that learn to sustain high prices coordinate over rounds, the case of [[P39 — Several actors: coordination plus individual misalignment|P39]](iii).
- *Different.* These theories solve for equilibria and ask which one is selected. The core does not model how a group
  reaches its joint behaviour (`CORE.md` §0); it measures the coordination, against independent pursuit, and the
  irreversibility, against a reversible record.
- *Import, done.* The structural specifications of [[P39 — Several actors: coordination plus individual misalignment|P39]] and [[P41 — Reversibility: the Jensen–Shannon divergence from the reversal|P41]], with the ontologies `industrial-organization/` and
  `experimental-economics/`.
- *Import, later.* Whether the harmonic part of a game, computed from its payoffs, predicts how irreversible play will
  be (`ontologies/experimental-economics/`, open questions).
- *What it could take from us.* A number for collusion that needs no model of the firms' profits, and that charges
  every departure from independence, agreed or not.

## Network theory of irreversible processes

- *Sources.* Schnakenberg [[References|@schnakenberg1976]].
- *Shared.* The entropy production of a Markov chain, `KL` of its record of transitions from the reversal; on a single
  cycle, the cycle's flux times its affinity.
- *Different.* Thermodynamics, with no principal and no specification.
- *Import, done.* The entropy production bounds the misalignment against reversibility, the Jensen–Shannon divergence,
  by half, and their ratio tends to a quarter when the asymmetry is small ([[P41 — Reversibility: the Jensen–Shannon divergence from the reversal|P41]]). For log-linear learning in a
  two-by-two game, the affinity is the intensity times the payoff gained around the cycle of single-player deviations
  (probe B2; `general/derived-spaces.md`).
- *What it could take from us.* Irreversibility measured against a declared reversible model, with its stakes.

## Social choice

- *Shared.* The question of several principals.
- *Different.* It aggregates preferences into weights, which the core does not choose.
- *Import, never* for the weights. Several principals with declared weights are in scope: their best compromise is a
  logarithmic pool of their intended behaviours, a single pursuit when each names an intensity, and with no intensity
  named every principal is satisfied by doing nothing ([[P42 — Several principals: gridlock, and the pooled pursuit|P42]]). Unions and intersections of intended sets need no
  import.

## Metrology and reporting standards

- *Sources.* The Guide to the Expression of Uncertainty in Measurement, and reporting checklists for trials *(to
  verify)*.
- *Shared.* A standard says what a report must declare and contain (`STANDARD.md`).
- *Different.* Not about alignment.
- *Import, now.* How to state uncertainty, now that sampling is in the framework ([[D11 — Sample and evidence|D11]]): the uncertainty of each
  estimated result in `STANDARD.md` should follow a recognized convention.

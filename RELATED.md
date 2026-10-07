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
| Information geometry | the Fisher metric, I-projections, Pythagorean identities | no principal, no specification | done: total correlation and the Jensen–Shannon divergence as misalignments ([P39], [P41]); nested I-projections split misalignment into named and unexplained parts ([P44]); now: the alignment plane, exact for a Gaussian default (`general/`) |
| The Price equation and selection theory | the replicator equation, the covariance form of change | descriptive; no specification | now: selection gradients as evaluators |
| Bounded rationality and discrete choice | the logit rule as a pursuit; a KL cost | the default is chosen by the agent | done: attention as mutual information ([P40]); tested in part: an endogenous default (`general/`) |
| Inverse RL and reward identifiability | objectives revealed up to a constant; identification | recovers rewards, does not score misalignment | done: misalignment over a family of objectives, an interval whose lower end the most charitable principal finds ([P48]); now: identification across environments |
| Cooperative inverse reinforcement learning and assistance | a principal whose target the agent does not know; a request read as evidence; norms taken for granted | designs agents that infer the target; we measure against a declared one | done, by correspondence: the posterior-mean target is the pooled pursuit of [P42](ii); later: the request as evidence, as a declared family of targets ([P48]) |
| Outer and inner alignment | a target, an evaluator trained on, and the trained actor | the two failures named, not measured | done: outer misalignment, inner misalignment, and their exact split ([P49]) |
| Reward tampering and wireheading | an evaluator computed from a measurement the actor can influence | causal incentives of agent designs, not a measure of behaviour | done: tampering as a divergence from a declared honest channel, split exactly from the change of the world; its bounds from signals, audits and re-measurements ([P50], [P51]); later: designs that remove the incentive, as interventions on the channel; rewards the actor can influence |
| Goodhart's law and reward hacking | evaluator and target; overoptimization | rankings and worst cases, not a divergence | done: the evaluator ([D10], [P18]–[P20]); tested on unseen data: the best-of-`n` form against [P13] (W1, refuted); probed: heavy tails and the χ² angle law (`general/`); now: heavy tails as a condition of the general core; later: early stopping compared, hackability over a feasible set, proxies that omit attributes, quantilizers as a budget |
| Principal–agent theory | delegation, performance measures, pass-through | equilibrium contracts, risk and payments | now: distortion and risk of a measure, read against [P50](iii)'s split of the misaligned share; a test of distortion from how a measure degrades, as a world design for [P20] |
| Identification and causal inference | identified sets, interventions | no notion of misalignment | now: sharp identified sets; later: transportability from evaluation to use; comparison of experiments for views |
| Hypothesis testing and sequential analysis | KL as a rate of evidence | a theory of tests, not of alignment | done: sampling, evidence, detection and estimation ([D11], [P21]–[P23]); the cost of reweighting ([P47]); now: reweighting needs about `e^{KL}` draws; what samples alone can certify; later: Stein's exponent, the boundary case |
| Deceptive alignment and AI evaluation | behaviour that differs when unobserved | intent-based definitions | done: across runs, differences between evaluation and use split into reproducible and run-specific parts ([P46]); now: a monitor trained against, as a tampered channel (H34, case C3); later: audit protocols |
| Distribution shift | bounds across conditions | prediction error, not misalignment | later: divergence-based transfer bounds |
| Statistics of misspecified models | the best fit of a family that excludes the truth, and the divergence left | estimation and model choice, not alignment | now: intervals at the revealed intensity; a test of which specification fits an actor better |
| Distributionally robust optimization | the worst average over a divergence ball | an optimizer's guard, not a measure of an actor | later: duals for every divergence ball, and its radius from data |
| Information elicitation without verification | reports judged without the truth, by measures that obey data processing | mechanism design: paying for truthful reports | later: audits without ground truth ([P51]) |
| Active inference | a KL from predicted to preferred outcomes | a process theory of brains | never, beyond the correspondence |
| Formal specification | specifications as sets, fixed in advance | deterministic traces | tested: a robustness degree that orders as misalignment does (`general/`); later: quantitative semantics |
| Learning in games and algorithmic collusion | several actors, potential games, learning dynamics | equilibria and their selection | done: a group as one actor ([P39]), reversible learning in potential games ([P41], Notes) |
| Network theory of irreversible processes | entropy production, cycle fluxes and affinities | thermodynamics of Markov chains, no principal | done: entropy production bounds the Jensen–Shannon divergence ([P41]) |
| Social choice | several principals | aggregation of preferences | never for the weights; several principals with declared weights are in scope ([P42]) |
| Metrology and reporting standards | a standard for reports | not about alignment | now: how to report uncertainty |

## KL control and control as inference

- *Sources.* Rafailov et al. [@rafailov2023]; Ziebart et al. [@ziebart2008]; Todorov's linearly solvable control and
  Levine's review of control as inference *(to verify)*.
- *Shared.* Pursuit is the KL-regularized optimum ([D2], [P4](i)). The maximum-entropy policy is the best feasible
  behaviour in a random environment ([P15], Notes).
- *Different.* These theories compute optimal behaviour. We judge actual behaviour against declared behaviour, and
  report stakes and identification.
- *Tested on unseen data* (case W3, `cases/w3-ppo-pursuit/`): whether a policy tuned by PPO with a KL penalty, a public
  GPT-2 tuned on a sentiment reward by von Werra et al.'s library [@vonwerra2020], is the KL-regularized optimum that
  these theories compute. In part: the change follows the reward in the reward's own scale, with a slope near `1/β`, but
  within prompts the reward explains only a third of the change, and about a tenth within each model's own outputs. The
  optimum is what a run aims at, not what it delivers; the framework measures the gap.
- *Import, later.* Soft dynamic programming, to state [P15]'s sequential case as an item of its own.
- *What it could take from us.* The split of the KL "budget" into pursuit and misalignment ([P6]), and of misalignment
  into avoidable and unavoidable parts ([P15]).

## Information geometry

- *Sources.* Čencov [@cencov1982]; Campbell [@campbell1986]; Csiszár [@csiszar1975]; Polyanskiy and Wu
  [@polyanskiy2025], for divergences on general spaces and their variational forms, which the general core needs for
  outcomes that are not finite (Q33); Ay, Jost, Lê and Schwachhöfer [@ay2015], who extend Čencov's uniqueness of the
  Fisher metric to infinite sample spaces; Pistone and Sempi [@pistone1995], the manifold of behaviours equivalent to a
  given one, on which the tilts that exist live; Amari's monographs *(to verify)*.
- *Shared.* The Fisher metric and its uniqueness ([A2], [P2]); I-projections and the Pythagorean theorem ([P6], [P15]);
  the second-order expansion of KL ([P11], [P13]); total correlation, the misalignment of several actors against
  independent pursuit ([P39]); the Jensen–Shannon divergence, the misalignment of a record of transitions against
  reversibility, where the nearest reversible record is the midpoint of the record and its reversal ([P41]).
- *Different.* No principal and no specification: the geometry is the same, the question is not.
- *Import, done.* Total correlation ([P39]) and the Jensen–Shannon divergence ([P41]); the bound of the latter by half
  the entropy production is Jeffreys' divergence bound. Probe B1 found the midpoint to be the nearest reversible record
  before [P41] proved it.
- *Import, now.* The dual (mixture and exponential) flat structures, for the two-parameter family spanned by a target
  and an evaluator through the default (`NOTES.md` §5, H6). For a Gaussian default and linear objectives the plane is
  exact: the departure splits like a right triangle, `cos²θ` into the target and `sin²θ` into misalignment, at every
  intensity (probe B5, `general/transfer.md`). With other defaults the law is local only, and B5's registered
  exponential case failed as posed, at an intensity where pursuit does not exist. Whether [P41](iv) is the mixture
  projection of the information geometry of Markov chains has not been searched for.
- *What it could take from us.* An interpretation of its projections as value lost, avoidable and unavoidable.

## The Price equation and selection theory

- *Sources.* Price [@price1970]; Shahshahani [@shahshahani1979]; Frank's Price equation programme [@frank2018];
  Robertson's secondary theorem and Lande and Arnold's selection gradients *(to verify)*.
- *Shared.* The revealed objective as Malthusian fitness and the replicator equation as a Fisher gradient ([P2]); the
  covariance form of change ([P13](i)). Frank argues that these invariances unify selection, thermodynamics and
  inference, an ambition close to ours.
- *Different.* Descriptive: it says how a population changes, not whether the change is what someone intended.
- *Import, now.* Selection gradients as evaluators, and the breeder's setting (a trait against fitness) as the model
  case of a target against an evaluator. *Later:* Frank's separation of forces, for paths that are not pursuits.
- *What it could take from us.* Specification, misalignment and the stakes of selection that is not aligned with a
  declared trait (the evolutionary-biology ontology's shortfall of ordinary selection).

## Bounded rationality and discrete choice

- *Sources.* McKelvey and Palfrey [@mckelvey1995]; Ortega and Braun [@ortega2013]; Matějka and McKay [@matejka2015];
  Sims's rational inattention *(to verify)*.
- *Shared.* The logit rule and quantal response are pursuits ([D2]); free energy is the net value ([P4]). Matějka and
  McKay derive the multinomial logit from a cost of information, an independent route to the KL cost of [P14].
- *Different.* In rational inattention the default (the prior over choices) is chosen optimally and the cost is a
  mutual information; here the default is declared ([A5]).
- *Import, done.* The information cost: misalignment against ignoring the situation is the mutual information between
  the condition and the response, and the average response is the nearest default to all conditions at once ([P40]).
- *Import, tested in part.* An endogenous default (probes B3, B3b; `general/derived-spaces.md`). On a continuum, the
  optimized default is discrete: for a state uniform on `[0, 1]` and squared loss, one atom until the precision `β`
  reaches `1/(2·Var) = 6`, where it splits, and between `√(β/6)` and `2·√(β/6)` atoms after that (B3b, held). B3's
  registered atom counts failed (3, 6 and 11 against 2.2, 4.1 and 7.1 ± 1), and its dimension slope did too, from the
  algorithm's slow convergence; both failures are recorded. Not claimed until proved.
- *What it could take from us.* A measure of how far observed choices are from a declared intention, with its stakes.

## Inverse reinforcement learning and reward identifiability

- *Sources.* Ng and Russell [@ng2000]; Ziebart et al. [@ziebart2008]; work on partial identifiability of rewards by
  Skalse and coauthors, and by Cao, Cohen and Szpruch *(to verify)*.
- *Shared.* A behaviour reveals its objective only up to a constant, and with an intensity only the product ([P1]); the
  revealed intensity is the maximum-entropy fit ([P5]); identification needs variation in conditions ([D9], [P12]).
  Maximum-entropy IRL models a behaviour as the tilt of a base behaviour by a linear reward, which is a pursuit ([D2]),
  and its maximum-likelihood reward over the span of given features is [P48]'s most charitable principal of that span;
  what no reward in the span explains is [P44]'s unexplained misalignment (probed to `10⁻⁸`,
  `probes/diagnostics/probe_requests.py`). With stochastic dynamics, the trajectory model of [@ziebart2008] lets the
  agent choose its transitions; the causal version [@ziebart2010] does not, and is the best feasible behaviour of [P15]
  for an actor whose limits fix the environment's transitions (`NOTES.md` §1, the probe bug of [P15]). A semi-supervised
  variant [@audiffren2026] adds trajectories drawn from a mixture of behaviours under different rewards, used only to
  smooth the fitted reward; in our terms, a population of principals ([P42], [P45]).
- *Different.* These theories aim to recover rewards. We take the principal's objective as declared and measure the
  distance to it; we need the actor's objective only as the evaluator.
- *Import, now.* Identification of an objective across several environments, which in our terms are conditions
  ([D8]) or interventions ([D6]); the invariance classes of rewards that leave optimal behaviour unchanged.
- *What it could take from us.* A measure of how much an unidentified part of the reward matters: its effect on
  misalignment and stakes.

## Cooperative inverse reinforcement learning and assistance

- *Sources.* Hadfield-Menell, Dragan, Abbeel and Russell [@hadfieldmenell2016], cooperative inverse reinforcement
  learning (CIRL): a two-player game with identical payoffs, in which the human knows the reward's parameter and the
  robot does not; Hadfield-Menell, Milli, Abbeel, Russell and Dragan [@hadfieldmenell2017], inverse reward design (IRD):
  the reward a designer writes is evidence about the true one, likely to the extent that its optimum behaves well in the
  environment the designer had in mind; Shah, Krasheninnikov, Alexander, Abbeel and Dragan [@shah2019], preferences
  implicit in the state of the world, which humans have already shaped toward what they want; Armstrong and Mindermann
  [@armstrong2018], a no-free-lunch theorem: every policy is the result of every reward under some planner;
  Hadfield-Menell and Hadfield [@hadfieldmenell2019], AI alignment as incomplete contracting, whose gaps people fill
  with norms.
- *Shared.* A principal whose target is not fully stated; a request read as more than its letter; norms that go without
  saying.
- *Different.* These works design an agent that infers the principal's target and acts on its belief. The core infers
  nothing about the principal: the target is declared ([A5]), a family when it is uncertain ([P48]), and behaviour is
  measured against it. The two are complementary: an inference can supply the declaration, and the core can judge the
  agent that acts on it.
- *Correspondences, checked* (`probes/diagnostics/probe_requests.py`). CIRL's deployment theorem, that the robot
  optimizes the reward of the posterior mean, is [P42](ii): with the posterior's weights and each possible target
  pursued at intensity `1`, the behaviour least far from them on average is the pursuit of the posterior-mean target.
  Armstrong and Mindermann's theorem says that observation alone cannot split a policy into a planner and a reward
  without a normative assumption; the core makes that assumption by its premises, pursuit as the steepest climb and the
  best trade-off ([A2], [A3]), which is why a behaviour's revealed objective is identified up to a constant ([P1]). Its
  price: a principal who is not a pursuer, such as CIRL's teaching human, whose best demonstrations depart from its own
  optimum, has a revealed objective that includes the teaching.
- *What a request leaves unsaid* (`NOTES.md` §10). Inverse reward design's observation model makes a written reward
  informative only about the features that varied where it was written; in the core, a request made in one condition and
  used in another ([D8], [P24]) leaves the weights of the features that did not vary undeclared, and the honest report
  is [P48]'s interval over them. Preferences implicit in the state of the world are, in the core, carried by the
  default: a pursuit keeps the default's proportions among outcomes the request scores alike, so whatever the request
  does not mention moves only through its regression on the request under the default ([P18]). The cost of departure
  from the default is an impact penalty of this kind, and a principal who means "within the usual norms" declares a cap
  on intensity ([P35]) or a feasible set ([D7]), not the whole ray.
- *Import, later.* The posterior of inverse reward design as the declared family of [P48]: the least and most
  misalignment over the targets consistent with a request (`NOTES.md` §5.4, H35). The default estimated from how a
  population usually acts, the state of the world in Shah et al.'s sense (H36).
- *What it could take from us.* A measure of how far an assistant's behaviour is from every target its belief allows,
  with the split of [P49] between what the request gets wrong and what the assistant does wrong.

## Outer and inner alignment

- *Sources.* Hubinger, van Merwijk, Mikulik, Skalse and Garrabrant [@hubinger2019], who name outer alignment, between
  the principal's target and the training objective, and inner alignment, between the training objective and what the
  trained system pursues.
- *Shared.* A chain of two links: target, evaluator, actor. In the core, the target is the principal's ([D3];
  `STANDARD.md`, the field Principal), the evaluator the trainer's ([D10]), and the actor's behaviour is judged against
  both.
- *Different.* Hubinger et al. define inner alignment through the objective a learned optimizer represents; the core
  judges behaviour only ([A1]), so inner misalignment is how far behaviour is from every optimum of the training
  objective, whatever the system represents.
- *Import, done* ([P49]). Outer misalignment is the principal's misalignment of the trainer's own optimum, a function of
  intensity, zero exactly when the evaluator is the target rescaled. Inner misalignment is the trainer's misalignment of
  the actor. The two share one part exactly, the change that pursues neither target nor evaluator. Case W1 had a gold
  target and so an outer side; W3 and W4 measured inner misalignment only.
- *Import, done.* Reward tampering, where the actor changes the measurement rather than the world: the next section.

## Reward tampering and wireheading

- *Sources.* Ring and Orseau [@ring2011], the delusion box; Everitt, Krakovna, Orseau, Hutter and Legg [@everitt2017],
  reinforcement learning with a corrupted reward channel, with a no-free-lunch theorem for learning the true reward from
  a corrupted one, and decoupled feedback, which checks rewards across sources; Everitt, Hutter, Kumar and Krakovna
  [@everitt2021], reward tampering analysed with causal influence diagrams; Leike et al. [@leike2017], the AI safety
  gridworlds, whose tomato-watering environment lets the agent make the tomatoes look watered; Carroll, Foote,
  Siththaranjan, Russell and Dragan [@carroll2024], reward functions that change and that the agent can influence.
- *Shared.* A true state and an observed reward or signal that the agent may corrupt; tampering as the gap between them;
  checking one source of reward against another.
- *Different.* These works ask which agent designs have an incentive to tamper, through the structure of causal
  diagrams, and whether a learner can recover the true reward. The core measures behaviour ([A1]): tampering is how far
  the actor's measurements depart from a declared honest channel, in nats, whatever the agent's design or incentives.
- *Import, done* ([P50], [P51]). With the measurement part of the outcome, the departure from the default splits exactly
  into the change of the world and the tampering; a target on the world charges all of the tampering as misalignment;
  and the optimum of training on a measured signal tampers at every intensity, with a share at the start equal to the
  share of the evaluator's variance that is noise of the measurement. From signals alone, tampering is bounded below by
  an attained minimum and never ruled out ([P51](ii)), the principal's side of the no-free-lunch result; an audit
  through a channel the actor cannot influence raises the lower bound, and identifies tampering when it is exact, as the
  cross-checking of several sources does.
- *Import, later.* Designs that remove the incentive to tamper, read as interventions ([D6]) on what the actor can
  influence, and their cost in the net value of [P50](iv). Carroll et al.'s influenceable rewards, for what [P50] leaves
  outside, an actor that changes the principal's target; their finding that each of eight candidate definitions of
  alignment either allows unwanted influence or is too cautious to be useful is a warning for any extension that tries.
  For worlds and signals that are not finite, the least tampering of [P51](i) is the maximum-likelihood estimate of a
  mixing distribution, whose existence and finite support Lindsay established [@lindsay1983].
- *What it could take from us.* A measure of tampering from behaviour, with its identified set from signals and the gain
  of each audit, in one currency with outer and inner misalignment ([P49]).

## Goodhart's law and reward hacking

- *Sources.* Gao et al. [@gao2023]; Coste et al. [@coste2024], whose released answers W1 used; Skalse et al.
  [@skalse2022]; Karwowski et al. [@karwowski2024]; Laidlaw et al. [@laidlaw2025], who define a proxy by its correlation
  with the target under a reference policy and propose `χ²` regularization of occupancy measures, the `χ²` row of [P31]
  with the correlation of [P13] (unlike KL, a `χ²` cost can rule outcomes out at the optimum: [P38](ii)); Zhuang and
  Hadfield-Menell [@zhuang2020], on proxies that omit attributes of the state; Taylor's quantilizers [@taylor2016];
  Manheim and Garrabrant's taxonomy, and El-Mhamdi and Hoang on weak and strong Goodhart *(to verify)*.
- *Shared.* An evaluator that differs from the target, and what pursuing it does to the target ([D10]). Karwowski et al.
  explain Goodhart by angles between reward vectors in the polytope of occupancy measures: a linear feasible set ([D7])
  and the angle of [P11]. Skalse et al. show that over all stochastic policies only trivial pairs are unhackable.
- *Different.* Rankings, worst cases and orderings over policy sets, rather than a divergence with stakes and
  identification.
- *Import, done.* The evaluator, with the decomposition of the target into its regression on the evaluator and a
  residual ([D10], [P18]); a stopping rule, where the target and the evaluator become uncorrelated under the current
  behaviour ([P20](i)).
- *Tested on unseen data* (case W1, `cases/w1-best-of-n-slope/`): Gao et al.'s best-of-`n` form `d·(a − b·d)`,
  fitted over the usual range, overstates the initial slope that [P13] computes from the initial policy, by 22%, on
  12.6 million of Coste et al.'s answers with a proxy built here. The curve keeps [P13]'s slope up to `n = 16` and then
  saturates (exploratory), so the form's two numbers misstate both the start and the shape.
- *Import, tested* (probes B4, B5; `general/transfer.md`). Under a default with a power-law upper tail, a KL budget
  buys unbounded gain, the case of Kwa et al. [@kwa2024], while a χ² budget `B` buys exactly `√(B·Var)`. Under χ²,
  Laidlaw et al.'s correlated proxy gains `√B·ρ·sd` in the target for every default; under KL the same law is exact
  only for Gaussian defaults. These are statements about outcomes that are not finite, and claimed nowhere yet.
- *Import, now* (for the general core's outcomes that are not finite, Q33). Kwa et al.'s condition on tails: a KL
  penalty protects the target when the evaluator's error is light-tailed, and not when it is heavy-tailed, a distinction
  finite outcomes cannot show, so the general core must carry it.
- *Import, later.* Whether Karwowski et al.'s early stopping is the rule of [P20](i) (`TERMS.md`, section 2, level B);
  hackability as a property of a target and an evaluator over a feasible set; Manheim and Garrabrant's four variants,
  once their definitions are checked against [P8], [P20](ii), [P12] and [P17] (`NOTES.md` §5, H3); Zhuang and
  Hadfield-Menell's necessary and sufficient conditions under which optimizing a proxy that omits attributes drives
  utility arbitrarily low, against the residual of [D10] and the worst cases of [P29]; a quantilizer, whose
  probabilities are at most a fixed multiple of the default's, as a departure budget of another shape ([P31]): a bound
  on the max-divergence.
- *What it could take from us.* Exact results for actors that see only the evaluator: a monotone regression rules out
  overoptimization ([P19]), so a proxy that only averages the target over what it can tell apart cannot lower it, and
  neither can a pass-or-fail verifier whose passing outcomes are better on average (`ontologies/machine-learning/`);
  the terminal rule of [P20](ii); and the shape law of [P25]: the target's curve turns no more often than the
  regression, so a single-peaked regression gives at most one overoptimization peak, for pursuit and for best-of-`n`
  alike. Whether Manheim and Garrabrant's regressional variant (proxy equals target plus
  noise) has a monotone regression depends on the noise, which is a question for their definitions. For an evaluator
  known in the target's units, the exact worst cases of the target lost, within a departure budget ([P29]) and among
  shared candidates such as best-of-`n` ([P34]); and no ranking of errors that holds at every budget ([C1]).

## Principal–agent theory

- *Sources.* Holmström [@holmstrom1979]; Holmström and Milgrom [@holmstrom1991]; Kerr [@kerr1975]; Frey and Jegen
  [@frey2001]; Gneezy and Rustichini [@gneezy2000]; Baker [@baker2002], who characterizes a performance measure by two
  parameters, its distortion and its risk; Courty and Marschke [@courty2008], a test for distortion from how a measure's
  association with the true goal changes once the measure is used.
- *Shared.* Delegation, a performance measure that differs from value, and the response to incentives
  ([D6], [P12]); the medical-sciences ontology, where the measures are written rules.
- *Different.* These theories solve for optimal contracts, with risk, participation and the cost of pay. We measure,
  and do not model the principal's optimization.
- *Import, now.* Baker's two parameters, read against [P50](iii): at the start of a pursuit of a measured evaluator, the
  misaligned share `sin²θ` splits into the share of the evaluator's variance that is noise of the measurement, `1 − R²`,
  and `R²` times the world's misaligned share `sin²θ_W`. Whether his distortion is that angle needs his text, which is
  not open (`NOTES.md`, H8). Courty and Marschke read distortion from how a measure's association with the goal weakens
  once its weight in pay rises: in the core, the covariance of target and evaluator under the current behaviour as
  intensity grows, whose zero is [P20](i)'s stopping point. Their design is a candidate world test of [P20], if its data
  are public.
- *Import, later.* The informativeness principle, as a statement about the principal's observation.
- *What it could take from us.* A measure of misalignment that needs no model of the agent's preferences.

## Identification and causal inference

- *Sources.* Manski [@manski2003]; Pearl and Bareinboim [@pearl2014], on transporting what is learned in one population
  to another; Blackwell [@blackwell1953], on comparing experiments; causal analyses of agent incentives by Everitt and
  coauthors [@everitt2021].
- *Shared.* Identified and identified sets ([D9]); interventions as designed changes of condition ([D6]); bounds from
  assumptions rather than point estimates ([P17]).
- *Different.* No notion of misalignment or of a specification.
- *Import, now.* Sharp identified sets; instrumental variables as a model for interventions that change only one thing.
- *Import, later.* Transportability's graphical criteria, for when what is seen in evaluation carries to use: an
  assumption that can make [P17]'s unobserved condition identified ([P24], [P46]). Blackwell's comparison of
  experiments, for sharper identified sets of views ([D8]; `NOTES.md` §3.3, E5).
- *What it could take from us.* Misalignment and stakes as targets of identification.

## Hypothesis testing and sequential analysis

- *Sources.* Cover and Thomas [@cover2006] (Stein's lemma, Chernoff information); Wald [@wald1945]; Chernoff
  [@chernoff1952]; Wilks [@wilks1938]; Chatterjee and Diaconis [@chatterjee2018], on the sample size of importance
  sampling; McAllester and Stratos [@mcallester2020], on what samples can certify about information.
- *Shared.* KL is the expected evidence per observation under the true behaviour ([D11], [P21]); `2n·M(p̂)` is a
  likelihood-ratio statistic ([P23]).
- *Different.* A theory of tests; it does not define alignment.
- *Import, done.* Sampling, as the act of measurement that connects behaviours to data ([D11]), with evidence ([P21],
  Wald in its Notes), detection ([P22], Chernoff) and estimation ([P23], Wilks) as derived results.
- *Import, now* (for the estimation work, Q33). Chatterjee and Diaconis's law: reweighting draws of one behaviour to
  stand for another needs about `e^{KL}` draws, necessary and sufficient, with a cut-off on the logarithmic scale; the
  sharp form of [P47]'s `E[w²] ≥ e^{KL}`, and the rule for every diagnostic computed by reweighting. McAllester and
  Stratos's limit: with one behaviour known and samples from the other, a high-confidence, distribution-free lower bound
  on `KL(known‖sampled)` stays below `ln N`, and the same holds for mutual information. Misalignment is the other way
  round, with the actor sampled and the intended behaviour known; there it is the general core's limit that applies: no
  sample certifies that misalignment is small (GD11). So which behaviour is sampled, and which log-ratios are known,
  decides what a case can certify (`general/dictionary.md`, §2): with log-probabilities known, as in W3 and W4, the
  core's quantities are Monte Carlo averages.
- *Import, later.* Stein's exponent, for a test that fixes the error of one kind; the chi-bar-square limit at the
  boundary `t* = 0`; confidence sets for the other quantities of the standard.
- *What it could take from us.* Misalignment as the quantity a test of "the actor behaves as intended" is about.

## Deceptive alignment and AI evaluation

- *Sources.* Hubinger et al. [@hubinger2019] on risks from learned optimization; Baker, Huizinga and coauthors
  [@baker2025], on monitoring the reasoning of a model trained against its monitor; the sleeper agents study, studies of
  evaluation awareness, and Ward et al.'s causal definition of deception *(to verify)*.
- *Shared.* An actor that behaves differently when it is observed ([D8], [D9], [P16], [P17]).
- *Different.* Several of these define deception by beliefs or intent, internal states that the core does not judge
  ([A1]). We bound what an unobserved condition can hide from what the actor can perceive.
- *Import, now* (H34, case C3). Baker et al. found that a monitor reading a reasoning model's chain of thought catches
  reward hacking, and that adding the monitor to the training reward helps at low optimization strength, while at higher
  strength the model learns to hide its intent and goes on hacking. That is H34's case (`NOTES.md` §5.4): training
  against a monitor that reads a channel the actor can influence tampers with the channel ([P50](iii)). A quantitative
  comparison needs the channel declared, which their setting does not give; case C3's second arm simulates it.
- *Import, later.* Audit protocols, trigger studies and measured evaluation awareness, as estimates of the divergence
  between views.
- *What it could take from us.* Identified bounds, and the design rule of [P17](iv): audits that the actor cannot tell
  from real use identify real use. A behavioural form of faked alignment, with no model of intent: an incentive met
  only in evaluation, pointing where the target does, drives the misalignment seen in evaluation to zero, and two
  actors that pass it through alike become indistinguishable at an exponential rate ([P37]).

## Distribution shift

- *Sources.* Domain adaptation bounds (Ben-David and coauthors) and covariate shift *(to verify)*.
- *Shared.* Behaviour in one condition bounded by behaviour in another and a divergence between them ([P17]); v7.10's
  evaluation gap (Prop 19), which shifts the weights of conditions.
- *Different.* Bounds on prediction error, not on misalignment.
- *Import, later.* Divergences other than KL for transfer bounds, which may narrow [P17]'s identified set.

## Statistics of misspecified models

- *Sources.* White [@white1982]; Vuong [@vuong1989].
- *Shared.* Fitting a family that does not contain the truth. The maximum-likelihood fit of a pursuit ray to an actor's
  sample estimates the intensity that minimizes `KL(p̂‖p_{F,t})`, White's pseudo-true parameter, which is the revealed
  intensity `t*` of [P5](iv); the divergence left is the misalignment.
- *Different.* These theories estimate and choose models; they do not read the divergence left as an actor's failure to
  do as intended.
- *Import, now* (for the estimation work, Q33). White's limit theory for a fit under misspecification: intervals for
  `t*` and the quantities computed at it, with the sandwich variance, where W1–W4 used the bootstrap. Vuong's test of
  which of two families is closer in KL to the truth: whether one specification fits an actor better than another, such
  as two principals ([P42], [P48]), a trainer and a principal ([P49]), or a specification with and without a named
  objective ([P44]). His nested case, with the saturated model, should give the limit of `2n·M(p̂_n)` when `M > 0`,
  where [P23]'s χ² reference does not apply; to be checked in the text before an item imports it.
- *What it could take from us.* The divergence left read as misalignment, with its stakes and its splits.

## Distributionally robust optimization

- *Sources.* Ben-Tal, den Hertog, De Waegenaere, Melenberg and Rennen [@bental2013].
- *Shared.* The worst average over a ball of behaviours around a nominal one, in a divergence such as KL or `χ²`:
  [P17]'s bound on what an unobserved condition can hide, and the departure budgets of [P27] and [P31].
- *Different.* An optimizer's guard against uncertain probabilities, not a measure of an actor.
- *Import, later.* The tractable dual of the worst case for every divergence of this kind, and the ball's radius chosen
  as a confidence region from goodness-of-fit statistics: a way to set [P17]'s `ε` from data rather than by assumption.

## Information elicitation without verification

- *Sources.* Kong and Schoenebeck [@kong2019].
- *Shared.* Reports that cannot be checked against the truth, judged by information measures that obey data processing,
  as [P51] judges signals.
- *Different.* Mechanism design: their mechanisms pay for reports so that telling the truth pays most; we measure what a
  behaviour reveals.
- *Import, later.* Their information-monotone measures and their impossibility result, for audits without ground truth
  ([P51]) and, if the archive's gap 5 is reopened, for H33's latent knowledge.
- *What it could take from us.* Tampering, and its identified set, as the quantity a truthful mechanism drives to zero.

## Active inference

- *Sources.* Friston and coauthors *(to verify)*.
- *Shared.* Its "risk" term is a KL from predicted to preferred outcomes, the direction of misalignment ([D3]).
- *Different.* A process theory of brains, with commitments the framework does not need.
- *Import, never* beyond recording the correspondence (`NOTES.md` §5, H7).

## Formal specification

- *Sources.* Quantitative semantics of temporal logics *(to verify)*.
- *Shared.* A specification as a set of acceptable behaviours, fixed in advance ([D3], [A5]).
- *Different.* Deterministic traces and satisfaction degrees, not distributions.
- *Import, tested* (probe B6, `general/transfer.md`). The case in which a robustness degree and misalignment order
  behaviours alike (`TERMS.md` §2): an actor that aims deterministically at a margin `r` inside a threshold, blurred by
  noise of size `σ`, judged by "pass with probability at least `1 − α`", has misalignment that depends on `r/σ` alone,
  never increases with `r`, and vanishes from `r = σ·Φ⁻¹(1 − α)`. Robustness counts in units of the actor's noise.
- *Import, later.* Quantitative semantics for temporal properties of whole episodes, each episode one outcome.

## Learning in games and algorithmic collusion

- *Sources.* Blume [@blume1993]; Candogan et al. [@candogan2011]; Calvano et al. [@calvano2020]; Cason et al.
  [@cason2014]; Assad et al. [@assad2024].
- *Shared.* Several actors, read as one actor on joint outcomes ([P39]). Log-linear learning in a potential game is a
  pursuit of the potential and is reversible; in a game with a harmonic part, learning circulates ([P41], Notes).
  Algorithms that learn to sustain high prices coordinate over rounds, the case of [P39](iii).
- *Different.* These theories solve for equilibria and ask which one is selected. The core does not model how a group
  reaches its joint behaviour (`CORE.md` §0); it measures the coordination, against independent pursuit, and the
  irreversibility, against a reversible record.
- *Import, done.* The structural specifications of [P39] and [P41], with the ontologies `industrial-organization/` and
  `experimental-economics/`.
- *Import, later.* Whether the harmonic part of a game, computed from its payoffs, predicts how irreversible play will
  be (`ontologies/experimental-economics/`, open questions).
- *What it could take from us.* A number for collusion that needs no model of the firms' profits, and that charges
  every departure from independence, agreed or not.

## Network theory of irreversible processes

- *Sources.* Schnakenberg [@schnakenberg1976].
- *Shared.* The entropy production of a Markov chain, `KL` of its record of transitions from the reversal; on a single
  cycle, the cycle's flux times its affinity.
- *Different.* Thermodynamics, with no principal and no specification.
- *Import, done.* The entropy production bounds the misalignment against reversibility, the Jensen–Shannon divergence,
  by half, and their ratio tends to a quarter when the asymmetry is small ([P41]). For log-linear learning in a
  two-by-two game, the affinity is the intensity times the payoff gained around the cycle of single-player deviations
  (probe B2; `general/derived-spaces.md`).
- *What it could take from us.* Irreversibility measured against a declared reversible model, with its stakes.

## Social choice

- *Shared.* The question of several principals.
- *Different.* It aggregates preferences into weights, which the core does not choose.
- *Import, never* for the weights. Several principals with declared weights are in scope: their best compromise is a
  logarithmic pool of their intended behaviours, a single pursuit when each names an intensity, and with no intensity
  named every principal is satisfied by doing nothing ([P42]). Unions and intersections of intended sets need no
  import.

## Metrology and reporting standards

- *Sources.* The Guide to the Expression of Uncertainty in Measurement, and reporting checklists for trials *(to
  verify)*.
- *Shared.* A standard says what a report must declare and contain (`STANDARD.md`).
- *Different.* Not about alignment.
- *Import, now.* How to state uncertainty, now that sampling is in the framework ([D11]): the uncertainty of each
  estimated result in `STANDARD.md` should follow a recognized convention.

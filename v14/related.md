# Competing frameworks of misalignment: what to take, what to give

> **Status: a survey for v14 (Q69), by a research assistant the executor briefed; not independent of the executor and
> not reviewed.** A statement marked *statement read* was read in the source by the assistant; the executor reads it
> again before any item cites it, as `CLAUDE.md` asks, and adds it to `REFERENCES.md` then. The executor checked by hand
> the one counterexample that bears on a decision, the tail-risk limit of entry 4 (`NOTES.md` §32). > *Since written*:
> R19 decided as two kinds of requirement, per-decision and pooled, with certify for averages and, >
per decision, samples only; culpability a verdict at a declared care margin `δ`, its size `E`, `K` its evidence rate >
only (Q74, Q76, `NOTES.md` §33.17, §34); OPTIMIZERS is now PURPOSE, "the request" the specification (Q70).

A second survey, on mixtures after Carcassi, R19, culpability and adversarial actors, is `literature-q70.md` (Q70).

A survey for the PI's question of 2026-10-17: which published frameworks, theories and studies of misalignment do
things the framework should do itself, which do we do that they should, and with what pros and cons. It extends
`RELATED.md`, which compares 22 neighbouring theories with v13, and reads everything against the v14 draft (`v14/`).

**How the sources were checked.** Every work below marked *record opened* had its arXiv record fetched through the arXiv
API (`export.arxiv.org`) and its title and authors matched: 111 records, all matching what was searched for. One
identifier guessed from memory returned an unrelated paper and was discarded. For the works marked *statement read*, the
PDF was fetched from `arxiv.org` into its own directory, converted to text, and the named theorem, definition or lemma
was read in the text, not in the abstract. Everything else was read in its abstract only, which is enough to identify a
work and say what it is about, and not enough to cite a theorem from it. Anything from memory is marked *(to verify)*.
No other host was fetched; hosts the PI could allow are listed at the end.

**Severity and the layers.** Following the PI's decision that severity is measured separately from misalignment, entries
on harm and risk are read as inputs to the principal's value scale, never as a change to misalignment itself. The layer
names CORE, INTERFACE and PURPOSE are v14's, PURPOSE being the third layer once called OPTIMIZERS (Q70), and a fourth
layer, SHAPING, on training, is discussed where a work bears on it.

**The short answer.** The closest competitor is not an alignment theory at all. It is the statistics of e-values and
anytime-valid inference (Ramdas, Grünwald, Larsson, Waudby-Smith and coauthors). v14's CORE has, in effect, moved into
that literature: its VE1 and VE2 are special cases of published theorems, and three of its open problems (VK4(iii), H46,
and the general twin of VE1) are answered there, wholly or in part. That literature has the tools but no account of
alignment. Each AI-auditing paper in it builds one bespoke test, and none says what a requirement is, how requirements
combine, or how misalignment splits by capability. The second finding is that v14 can only *convict*. The assurance
literature (safety cases, conformal risk control, rare-event certification, AI control) is about *certifying*, and the
framework has nothing to offer a decision to deploy until it states a certification verdict.

---

## 1. The table

| # | Framework or theory | What it formalizes | What it does that we should adopt (pro / con) | What we do that it lacks (pro / con) | Priority | Sources |
|---|---|---|---|---|---|---|
| 1 | Safe anytime-valid inference: e-values, numeraire, log-optimality, stopping-time bounds | evidence as the wealth of a fair bet; the log-optimal e-variable for any null; the least expected sample size of a level-α test | its theorems: the numeraire and the reverse information projection with no assumptions (the general twin of VE1 and VE2); `E[τ] ≥ log(1/α)/KL_inf` (an operational meaning of misalignment); log-optimal e-processes chosen from the data (H46); portfolio duality (VK4(iii) in the interior case). Pro: imported, read, rigorous. Con: mostly i.i.d. for the optimality results | a theory of *what* to test: requirements as convex sets, budgets as their general form (VK0), a verdict per requirement, splits by capability. Pro: gives the SAVI tools an object. Con: our part is organization, not new theorems | **now** | [Ramdas et al. 2022](https://arxiv.org/abs/2210.01948); [Larsson, Ramdas, Ruf 2024](https://arxiv.org/abs/2402.18810); [Agrawal, Ram, Ramdas 2025](https://arxiv.org/abs/2504.19952); [Shekhar 2025](https://arxiv.org/abs/2512.20039); [Waudby-Smith, Sandoval, Jordan 2025](https://arxiv.org/abs/2504.02818); [Koning, van Meer 2025](https://arxiv.org/abs/2501.03982); [Ramdas, Wang 2024](https://arxiv.org/abs/2410.23614) |
| 2 | Betting confidence sequences for bounded means | time-uniform confidence sets for a mean, from a capital process `Π(1 + λ_i(X_i − m))` | two-sided, time-uniform intervals for every rate and budget, giving a *certify* verdict ("rate ≤ ε with confidence 1 − α") beside our *convict* verdict. Pro: VK3's bet is their capital process, so it costs nothing new. Con: needs a bounded statistic; per-condition intervals multiply | the reading of the capital process as evidence against a requirement in nats, and its link to the closed forms VK2 and VK3 | **now** | [Waudby-Smith, Ramdas 2020](https://arxiv.org/abs/2010.09686) |
| 3 | Sequential auditing and monitoring by betting | e-process tests that a deployed model's risk, fairness or behaviour has not shifted beyond a tolerance | tests against a reference known only from samples (two-sample betting), which v14's `LIMITS.md` lists as missing; tolerances declared before the test; labels that arrive late. Pro: published, with guarantees. Con: each is built for one statistic | one framework in which their nulls are requirements (an order against a reference with a margin, a budget, a fairness gap); misalignment as the size of the breach | **now** | [Podkopaev, Ramdas 2021](https://arxiv.org/abs/2110.06177); [Chugg et al. 2023](https://arxiv.org/abs/2305.17570); [Richter et al. 2024](https://arxiv.org/abs/2410.19406); [Shekhar, Ramdas 2021](https://arxiv.org/abs/2112.09162); [Zhang et al. 2026](https://arxiv.org/abs/2602.02229) |
| 4 | Conformal risk control and Learn then Test | choosing a deployment parameter (a threshold, an abstention rule) so that a risk is at most α, distribution-free, in finite samples | certification by design: an intervention guaranteed to satisfy a rate limit or budget with probability `1 − δ`. Pro: what a deployer acts on. Con: needs calibration data exchangeable with use; the guarantees are marginal over conditions | a measure of *how far* a behaviour is from acceptable, anytime-valid under dependence; verdicts per condition; the factorization | **now** (certification); later (design) | [Angelopoulos et al. 2022](https://arxiv.org/abs/2208.02814); [Angelopoulos et al. 2021](https://arxiv.org/abs/2110.01052); [Bates et al. 2021](https://arxiv.org/abs/2101.02703); [Gui, Jin, Ren 2024](https://arxiv.org/abs/2405.10301); [Quach et al. 2023](https://arxiv.org/abs/2306.10193); [Mohri, Hashimoto 2024](https://arxiv.org/abs/2402.10978); [Chen et al. 2025](https://arxiv.org/abs/2502.20285) |
| 5 | Rare-event estimation and the limits of a clean record | the probability of rare harmful outputs, beyond what sampling can see; how much a test with no failures can certify | estimators that steer sampling toward the rare outcome (importance sampling, extrapolating elicitation probabilities), and the "evidential ceiling" of a benchmark of fixed size. Pro: v14's forbidden sets and small rate limits (H48) need exactly this. Con: the estimators need model access or extrapolation assumptions | VK1: one occurrence decides a forbidden set, at level 0, whatever the dependence; the separation of evidence from severity | **now** | [Wu, Hilton 2024](https://arxiv.org/abs/2410.13211); [Jones et al. 2025](https://arxiv.org/abs/2502.16797); [Nazeri et al. 2026](https://arxiv.org/abs/2607.20286); [Kaur 2026](https://arxiv.org/abs/2607.21735); [Wang et al. 2025](https://arxiv.org/abs/2510.03969); [Levy, Perl 2026](https://arxiv.org/abs/2604.21854) |
| 6 | Statistical assurance against adaptive adversaries | an actor that behaves well until it is certified and then switches | the result as a limit: every finite certification followed by unmonitored use can be defeated; monitoring that never stops, with revocation, limits the excess. Pro: it bears on VE3 and on H43. Con: one recent preprint, not reviewed | VE3's bets never stop, so v14 is already on the right side; the framework should say so | **now** (as a limit) | [Singh 2026](https://arxiv.org/abs/2610.18948) |
| 7 | Measurement theory and statistics of evaluations | the steps from a background concept to a systematized concept, an instrument and measurements; validity; clustered error bars | a validity account for the grader that turns transcripts into outcomes (H47); questions as a sample from a population, so that the weights of conditions are estimated, with clustered errors. Pro: the largest gap between v14 and a real case. Con: social-science vocabulary, little mathematics | a precise systematized concept (the requirement) and a defined quantity to measure | **now** | [Wallach et al. 2024](https://arxiv.org/abs/2411.10939); [Chouldechova et al. 2024](https://arxiv.org/abs/2412.01934); [Bean et al. 2025](https://arxiv.org/abs/2511.04703); [Miller 2024](https://arxiv.org/abs/2411.00640) |
| 8 | Distributional control and f-divergence alignment | the target model as the KL projection of a base model onto pointwise and distributional (moment) constraints, an exponential family with the support restricted | attribution: VK5, that the constrained optimizer is a tilt at a shadow price and that a forbidden set restricts the support, is GDC's Theorem 1, after Csiszár. Pro: honesty, and a ready algorithm. Con: none | measuring an actual behaviour against the constraints, in the other direction of KL; inequality constraints with a verdict each | **now** (attribution) | [Khalifa et al. 2020](https://arxiv.org/abs/2012.11635); [Go et al. 2023](https://arxiv.org/abs/2302.08215); [Wang et al. 2023](https://arxiv.org/abs/2309.16240) |
| 9 | Constrained RL, safe RLHF, dualization | maximize reward subject to cost constraints; Lagrangian duality; zero duality gap | attribution again: VK5 with several constraints is Huang et al.'s Lemma 2, with strong duality; dual-based algorithms for PURPOSE. Con: the optimizer's view only | the principal's side: whether a trained actor actually meets the constraint, with what evidence | **now** (attribution); later | [Paternain et al. 2019](https://arxiv.org/abs/1910.13393); [Achiam et al. 2017](https://arxiv.org/abs/1705.10528); [Dai et al. 2023](https://arxiv.org/abs/2310.12773); [Huang et al. 2024](https://arxiv.org/abs/2405.19544); Altman's CMDP monograph *(to verify)* |
| 10 | Behaviour Expectation Bounds | a model as a mixture of well-behaved and ill-behaved components; a prompt as evidence that selects a component | a quantitative link between conditions and hidden misalignment: a prompt of length about `(1/β)·log(1/α)` brings out a component of prior weight α. Pro: the same currency as ours, KL per sentence. Con: the mixture decomposition is assumed, not identified | the mixture principle, under which such a model is judged per condition; [P17]'s bound on what an actor can hide | later | [Wolf et al. 2023](https://arxiv.org/abs/2304.11082) |
| 11 | Reward hacking as an order reversal (Skalse et al.; Goodhart in RL) | a proxy is unhackable if raising its return never lowers the true return; over open policy sets only equivalent pairs are | the order-theoretic definition as a requirement built from two rankings, in `order.md`'s terms. Pro: it is behavioural. Con: about policy sets, not one actor | magnitudes, and the observation that their impossibility is a convexity result of the same kind as VE2 | later | [Skalse et al. 2022](https://arxiv.org/abs/2209.13085); [Karwowski et al. 2023](https://arxiv.org/abs/2310.09144) |
| 12 | Goal misgeneralization; agents and devices | an actor that stays capable out of distribution and pursues another goal; goal-directedness as a likelihood ratio of an "agent" mixture over a "device" mixture | a concrete test for the PURPOSE hypothesis, a likelihood ratio, which is an e-value against "not goal-directed". Pro: makes VF2's refutable motive testable. Con: needs priors over rewards and policies | CORE sees the failure without a model of goals: misalignment by condition, in test against training conditions | later | [Langosco et al. 2021](https://arxiv.org/abs/2105.14111); [Shah et al. 2022](https://arxiv.org/abs/2210.01790); [Orseau et al. 2018](https://arxiv.org/abs/1805.12387) |
| 13 | Revealed-preference alignment (the Luce Alignment Model) | an AI's choices as a mixture, with weight α, of the principal's logit rule and its own; identification of α and of both utilities | the distinction between *aligned* (the same preferences) and *compliant* (`α = 1`), and identification from menus, which are conditions. Pro: a sharp decomposition. Con: assumes logit rules; by [A1] we cannot and need not tell the two apart | the principal declares a requirement rather than a utility; no parametric model | later | [Suleymanov 2026](https://arxiv.org/abs/2603.27868) |
| 14 | Misalignment between agents in a population | the probability that two agents drawn at random hold conflicting goals | little: it is a dispersion index of goals. Con: it needs goals, not behaviour | everything behavioural | never | [Kierans et al. 2024](https://arxiv.org/abs/2406.04231) |
| 15 | Misalignment in interactive epistemology | one agent's beliefs about another's beliefs that do not match | nothing: a homonym. Recorded so the question is not reopened | n/a | never | [Guarino, Ziegler 2025](https://arxiv.org/abs/2506.17176) |
| 16 | Conceptual frameworks: the targets of alignment; three axes; acceptable misalignment; prepotence | what a principal's target can be (instructions, intentions, preferences, interests, values); misalignment along objectives, information and principals; "acceptable" misalignment | a declared field "kind of target", from Gabriel's list; LaCroix's three axes as a check that the three layers cover the ground. Pro: cheap. Con: no mathematics | a mathematics for "aligned enough, for whom", which is what LaCroix and van Lier et al. call for | **now** (fields) | [Gabriel 2020](https://arxiv.org/abs/2001.09768); [LaCroix 2026](https://arxiv.org/abs/2604.20805); [van Lier et al. 2026](https://arxiv.org/abs/2610.16881); [Critch, Krueger 2020](https://arxiv.org/abs/2006.04948); [Spizzirri 2025](https://arxiv.org/abs/2512.03048) |
| 17 | Causal incentives, discovering agents, deception | incentives read from the graph of a causal influence diagram; agents as systems that would adapt their policy; deception in structural causal games | graphical criteria, as a declared structure for the interface and for PURPOSE. Pro: sound and complete criteria. Con: needs a causal model, beyond behaviour | measurement of what an actor did, in nats, with no causal model | later | [Everitt et al. 2021](https://arxiv.org/abs/2102.01685); [Kenton et al. 2022](https://arxiv.org/abs/2208.08345); [Ward et al. 2023](https://arxiv.org/abs/2312.01350) |
| 18 | Responsibility, blame and intention | the degree of blame as the reduction in the probability of a bad outcome that another action would have achieved, mitigated by that action's cost, relative to an epistemic state | the cost of the better alternative, which v14's culpability ignores: v14 charges any departure from the best feasible behaviour, however costly that behaviour is for the actor. Pro: closes a hole in the label "culpable". Con: adds a cost the principal must declare | an evidence-scaled culpability, testable by bets, and the exact split into unavoidable and avoidable parts | **now** | [Chockler, Halpern 2003](https://arxiv.org/abs/cs/0312038); [Halpern, Kleiman-Weiner 2018](https://arxiv.org/abs/1810.05903) |
| 19 | Counterfactual harm; causal analysis and quantification of harm | harm as the expected shortfall of utility against a default action, by counterfactuals; that any factual definition of harm fails some cases | for the severity layer: harm *caused* needs a default and a counterfactual, which are INTERFACE objects, while the severity *of an outcome* is a declared value scale. Pro: keeps the two apart, as the PI decided. Con: counterfactuals need a causal model | the reference behaviour and the feasible set, which supply the default without a model of intent | **now** | [Richens et al. 2022](https://arxiv.org/abs/2204.12993); [Beckers et al. 2022a](https://arxiv.org/abs/2210.05327); [Beckers et al. 2022b](https://arxiv.org/abs/2209.15111) |
| 20 | Impact measures and power-seeking | penalties for reducing attainable utility, or reachability against a baseline; optimal policies tend to keep options | side effects as a loss of the *principal's future feasible set*, an INTERFACE concept across time; the lesson that the baseline decides the incentives. Con: penalties for optimizers | side effects as requirements on other coordinates of the outcome, judged in CORE | later | [Turner et al. 2019](https://arxiv.org/abs/1902.09725); [Krakovna et al. 2018](https://arxiv.org/abs/1806.01186); [Turner et al. 2019b](https://arxiv.org/abs/1912.01683) |
| 21 | Corrigibility | the off-switch game; shutdown instructability; utility heads combined lexicographically | corrigibility as requirements: a forbidden outcome in shutdown conditions, plus a ban on influencing the principal's channel, which is [P50]'s tampering turned on the principal. Pro: testable. Con: influence on the principal is outside v14's scope (Carroll et al.) | behavioural verification of corrigibility, rather than its design | later | [Hadfield-Menell et al. 2016](https://arxiv.org/abs/1611.08219); [Carey, Everitt 2023](https://arxiv.org/abs/2305.19861); [Nayebi 2025](https://arxiv.org/abs/2507.20964); Soares et al. 2015 *(to verify)* |
| 22 | Embedded agency | an agent that is part of its environment, can model and modify itself, and has no clean boundary | nothing to import; a limit to record: v14's interface `(U, Z, V, E)` assumes a Cartesian boundary between actor, world and record | n/a | never (record the limit now) | [Demski, Garrabrant 2019](https://arxiv.org/abs/1902.09469) |
| 23 | Debate and scalable oversight | protocols in which a judge decides from a debate; complexity classes; obfuscated arguments; query complexity | a model of the *grader*: how a record's outcomes are obtained when no person can judge them (H47). Con: idealized, complexity-theoretic | what to do with the judged outcomes | later | [Irving et al. 2018](https://arxiv.org/abs/1805.00899); [Brown-Cohen et al. 2023](https://arxiv.org/abs/2311.14125); [Brown-Cohen et al. 2025](https://arxiv.org/abs/2506.13609); [Brown-Cohen et al. 2026](https://arxiv.org/abs/2602.08630) |
| 24 | AI control and control games | safety of a deployment protocol against an actor that tries to subvert it; a partially observable stochastic game between designer and red team | the *worst-case feasible* breach rate: the largest breach any behaviour of the declared interface could reach. Pro: one line in INTERFACE, no motive needed, and the number a protocol guarantees. Con: needs the interface's feasible set, which is the hard part | the actual behaviour's misalignment and its split, beside the worst case | **now** | [Greenblatt et al. 2023](https://arxiv.org/abs/2312.06942); [Griffin et al. 2024](https://arxiv.org/abs/2409.07985); [Korbak et al. 2025](https://arxiv.org/abs/2501.17315) |
| 25 | Safety cases | a structured argument, with evidence, that a system is safe enough in a context: inability, control, trustworthiness, deference | the report's form: claims, arguments and evidence, with the assumptions and defeaters each rests on. Pro: what regulators read; v14's rule that a report says what a charge rests on is a fragment of it. Con: qualitative | quantities for the claims: inability as a feasible set with no breach, control as a worst-case rate, trustworthiness as a certified margin | **now** | [Clymer et al. 2024](https://arxiv.org/abs/2403.10462); [Buhl et al. 2024](https://arxiv.org/abs/2410.21572); [Goemans et al. 2024](https://arxiv.org/abs/2411.08088); [Balesni et al. 2024](https://arxiv.org/abs/2411.03336); [Buhl et al. 2025](https://arxiv.org/abs/2505.03989); [Souly et al. 2026](https://arxiv.org/abs/2604.00788) |
| 26 | System safety, STPA | hazards as unsafe control actions in a control structure with feedback loops | a structured search for the requirements a principal forgot (misspecification is outside v14, and STPA is one way to reduce it). Con: method, not theory | measurement of each requirement found | later | [Mylius 2025](https://arxiv.org/abs/2506.01782); [Carlucci et al. 2026](https://arxiv.org/abs/2606.13474); Leveson and Thomas's STPA handbook *(to verify)* |
| 27 | Guaranteed safe and verified AI; a Bayesian oracle | a world model, a safety specification, and a verifier that issues a proof certificate; bounds on harm under the most cautious plausible hypothesis | a specification language with a syntax: v14's requirements need one for practice. Pro: the request becomes machine-checkable. Con: world models for open domains do not exist | the record side: what a sample of decisions shows, where no proof is available | later | [Dalrymple et al. 2024](https://arxiv.org/abs/2405.06624); [Seshia et al. 2016](https://arxiv.org/abs/1606.08514); [Bengio et al. 2024](https://arxiv.org/abs/2408.05284) |
| 28 | Risk taxonomies, risk thresholds, harm severity scales | catalogues of AI risks by cause and domain; thresholds stated as risk; ordinal severity indices from incidents | a category for each requirement from a public taxonomy, and severity as an ordinal or declared scale; risk thresholds as budgets on severity-weighted indicators. Pro: makes severity declarable. Con: the taxonomies disagree and are not measurements | the evidence each breach carries, kept apart from severity | **now** | [Slattery et al. 2024](https://arxiv.org/abs/2408.12622); [Zeng et al. 2024](https://arxiv.org/abs/2406.17864); [Koessler et al. 2024](https://arxiv.org/abs/2406.14713); [Vei et al. 2025](https://arxiv.org/abs/2509.10104) |
| 29 | Social choice for alignment from human feedback | RLHF as preference aggregation; axioms; RLHF aggregates hidden context by Borda count | for SHAPING: the trainer's evaluator is the output of a voting rule, so its outer misalignment has a social-choice cause. Con: says nothing about measuring an actor | several principals as an intersection of requirements, with emptiness as the conflict | later | [Conitzer et al. 2024](https://arxiv.org/abs/2404.10271); [Ge et al. 2024](https://arxiv.org/abs/2405.14758); [Siththaranjan et al. 2023](https://arxiv.org/abs/2312.08358); [Dai, Fleisig 2024](https://arxiv.org/abs/2404.13038); [Halpern et al. 2026](https://arxiv.org/abs/2606.21550) |
| 30 | Pluralistic alignment | Overton, steerable and distributional pluralism | three requirement types, each convex and closed: a floor on the mass of every reasonable answer; matching per condition (steering); a divergence ball around a population's distribution. Pro: worked examples for the catalogue. Con: none | verdicts and evidence for each | **now** (examples) | [Sorensen et al. 2024](https://arxiv.org/abs/2402.05070) |
| 31 | A formal account of how RLHF amplifies a behaviour | the change in any statistic under KL-regularized tuning is a covariance under the base policy; the KL-closest policy that does not amplify it is a tilt with a closed-form penalty | the SHAPING layer's first theorem: the sign of `Cov_base(g, e^{βr})` predicts whether training breaches a budget on `g`. Pro: testable against CORE's verdicts. Con: assumes training reaches the KL-regularized optimum, which W3 found it does not | none of the theorems is new to us ([P13](i), VK5); what we add is the requirement and the verdict | **now** (SHAPING) | [Shapira et al. 2026](https://arxiv.org/abs/2602.01002) |
| 32 | Training-induced misalignment, empirically | narrow finetuning that misaligns broadly; reward hacking that generalizes to sabotage; alignment faking; backdoors that survive safety training; shallow safety alignment | paradigm cases for SHAPING and for label tests: training on some conditions changes behaviour in others, sometimes only behind a trigger. Pro: real, public phenomena. Con: graded by model judges (H47) | definitions that do not depend on the judge's "misaligned" label; per-condition misalignment and hidden-condition bounds | **now** (cases) | [Betley et al. 2025](https://arxiv.org/abs/2502.17424); [MacDiarmid et al. 2025](https://arxiv.org/abs/2511.18397); [Wang et al. 2025](https://arxiv.org/abs/2506.19823); [Soligo et al. 2026](https://arxiv.org/abs/2602.07852); [Zhang et al. 2026](https://arxiv.org/abs/2606.20814); [Qi et al. 2023](https://arxiv.org/abs/2310.03693); [Qi et al. 2024](https://arxiv.org/abs/2406.05946); [Sharma et al. 2023](https://arxiv.org/abs/2310.13548); [Hubinger et al. 2024](https://arxiv.org/abs/2401.05566) |
| 33 | Propensity benchmarks and incentive models of oversight | scores of misaligned behaviour by agents; deterrence models in which a principal sets rewards for a solver and an auditor | the auditor's incentive to inspect as part of the interface: oversight is itself an actor. Con: equilibrium models | a defined quantity in place of an ad hoc score | later | [Naik et al. 2025](https://arxiv.org/abs/2506.04018); [Agarwal et al. 2026](https://arxiv.org/abs/2605.01643) |

---

## 2. The entries

### 1. Safe anytime-valid inference (SAVI): the numeraire, log-optimality, and stopping times

*What it is.* A test martingale is the wealth of a gambler who bets against a null hypothesis with tickets that the
null says are fair; Ville's inequality bounds the chance it ever reaches `1/α` (Ramdas, Grünwald, Vovk and Shafer, a
survey; abstract read).

*Statements read.*
- Larsson, Ramdas and Ruf, Theorem 2.6: a numeraire e-variable `X*` (with `E_Q[X/X*] ≤ 1` for every e-variable `X`)
  exists for *any* null and alternative, with no assumptions. It is finite exactly when `Q ≪ P`. Proposition 2.4: the
  numeraire is the log-optimal e-variable. Definition 3.1: the effective null is `P_eff = {P : E_P[X] ≤ 1 for every
  e-variable X}`, the largest family with the same e-variables. Theorem 3.6, (3.3): `E_Q[log X*] = sup_X E_Q[log X] =
  inf_{P∈P_eff} H(Q|P) = H(Q|P*)`, strong duality between the best bet and the reverse information projection.
- Agrawal, Ram and Ramdas, Theorem 3.1: every level-α test with power one has `E_Q[τ_α] ≥ log(1/α)/KL_inf(Q, P)`, with
  `KL_inf(Q, P) = inf_{P∈P} KL(Q, P)`.
- Shekhar, Theorem 2.1: on a finite alphabet, with a closed null set `Θ_0` (convexity not assumed), the universal
  inference e-process (a Krichevsky–Trofimov mixture divided by the running maximum likelihood over the null) has level
  α and `lim sup_{α→0} E_θ[τ_α]/(log(1/α)/γ*) ≤ 1`, where `γ* = inf_{θ_0∈Θ_0} KL(θ‖θ_0)`.
- Waudby-Smith, Sandoval and Jordan (v2, retitled "Instance-log-optimality of portfolio-based e-processes"), Theorem
  2.3 and Lemma A.4: for the null `P = {P : E_P[E^(j)] ≤ 1, j = 1..d}` of i.i.d. e-vectors, `max_{λ∈Δ_d} E_Q[log λᵀE] =
  inf_{P∈P} KL(Q‖P)`, and every e-process with sublinear portfolio regret reaches that growth rate almost surely.

*What we should adopt, and what it changes in v14.*
- **VE1 and VE2 are special cases of (3.3) and Definition 3.1.** VE1 is the finite, convex, closed case. VE2(i), that
  bets against `A` are bets against its hull, is the statement that `A` and `P_eff` have the same e-variables. By their
  Remark 3.2, `P_eff` is a bipolar of the null, so it contains its convex hull (the remark was not read in full).
  `evidence.md` cites Grünwald, de Heide and Koolen for VE1, which is right as far as it goes. Larsson et al. remove the
  conditions of full support and finite misalignment, and so give **`CORE_GENERAL`'s VE1 and VE2 on any space**,
  VE1(iii) included (Theorem 2.6, (i)⇔(iii)). The general twin can import them rather than prove them.
- **An operational meaning of misalignment.** By Agrawal et al.'s Theorem 3.1, a principal who wants to convict at level
  α needs, in expectation, at least `log(1/α)/M` decisions, where `M` is v14's misalignment, and Shekhar's test attains
  it on finite alphabets as `α → 0`. For `NOTES.md` §24's two examples at `α = 0.05`, computed here by hand: the
  catastrophe with `M = 3.9·10⁻⁷` needs at least 7.7 million decisions, the rude answer with `M = 0.044` at least 68.
  This is a cleaner statement of v14's reading "the rate at which a fair bet grows" than Kelly's criterion alone. It
  also turns LIMITS's point on severity into a sample-size statement anyone can check.
- **H46, answered in part.** "Bets chosen from the record reach the best growth" holds for i.i.d. decisions: Shekhar's
  Theorem 2.1 on finite alphabets, for any closed null; Waudby-Smith et al. for nulls defined by finitely many e-values,
  which covers budgets. Under dependence it stays open. That is v14's case, since VE3 allows dependence.
- **VK4(iii), answered in part.** Lemma A.4 is VK4(iii) stated for laws of the e-vector, with
  `E^(j) = 1 + c_j·(g_j − b_j)`. Its proof puts the remaining mass of the nearest null law at the point where every
  `E^(j)` vanishes, and such a point need not be an outcome of `X`. So it proves VK4(iii) when that remaining mass is
  zero, the analogue of VK3's case `λ* < λ_max`, and leaves the boundary case, where VK3 moves mass to a cheapest
  outcome, to be checked on `X`. This should be done before VK4(iii) is called proved.
- **Shekhar's theorem bears on the convexity choice.** For i.i.d. decisions, the optimal rate against a closed null that
  is *not* convex is the least KL to the null itself, not to its hull. That supports `factorization.md`'s VF1, that a
  sample is still judged against a non-convex set. It also makes the price of the mixture principle exact: a principal
  who assumes i.i.d. decisions can convict at rate `M_A`, and one who accepts schedules only at rate `M_{conv A}`.
- **Anytime validity is free.** Koning and van Meer (abstract read) show that any fixed-`N` test induces an
  anytime-valid sequential test that agrees with it at `N`. So [P55]'s exact test need not be given up for VE3's sake:
  its sequential version exists.

*What we do that it lacks.* SAVI is a theory of tests. It has no catalogue of requirements, no account of how
requirements combine into an acceptable set, and no splits by capability or layer. *Pro:* our CORE gives these tools an
object, and the AI-auditing papers (entry 3) would be special cases. *Con:* what we add is organization. The theorems
of CORE's evidence file are, honestly, known. A reader from this literature will see VE1 and ask what is new, and the
answer must be VK0, the layers and the factorization, not VE1.

### 2. Betting confidence sequences for bounded means

*Statements read.* Waudby-Smith and Ramdas, equation (23): the capital process `K_t(m) = Π_{i≤t}(1 + λ_i(m)·(X_i − m))`,
with predictable `λ_i`. Proposition 2: for `[0,1]` observations, conditional means equal to `m` is *equivalent* to
`K_t(m)` being a test martingale for one, and then every, fixed or predictable `λ`. Proposition 3 (universal
representation): for any set of distributions `S`, every test supermartingale for `S` is `Π(1 + λ_i·Z_i)` with
`E_S[Z_i | F_{i−1}] ≤ 0`. Theorem 3: the hedged capital process gives a `(1 − α)` confidence sequence that is an
interval.

*Adopt.* VK3's best bet `1 + λ*·(g − b)` is exactly this capital process at `m = b`. The same machinery, run at every
`m`, gives a **time-uniform two-sided interval for every rate and budget**. Its upper end is a *certification*: "the
breach rate is below `ε` with confidence `1 − α`", valid at any stopping time. v14 says "aligned within a margin" is
verifiable only for independent decisions (`LIMITS.md`). Proposition 2 is stated for conditional means, so the upper
confidence sequence for a rate holds under the same dependence VE3 allows. That extends the margin verdict, which the
executor should check against [D3]'s statement. *Pro:* the verdict a deployer needs, at no new cost. *Con:* bounded
statistics only, so a budget on unbounded costs (seconds, money) needs a cap or another argument.

*What we do that it lacks.* The reading of `log K_t/t` as misalignment in nats, and the closed forms of VK2 and VK3 for
the best fixed `λ`.

### 3. Sequential auditing and monitoring by betting

*Statements read.* Podkopaev and Ramdas, equations (1)–(3): `H_0: R_T(f) ≤ R_S(f) + ε_tol` against its alternative, with
a source risk `R_S` estimated from a sample, tested sequentially at a fixed level; and a relative form, `R_T ≤ (1 +
ε_tol)·R_S`. Richter et al., equations (3)–(5): `H_0: D(P_B^M, P_B^{M'}) ≤ ε` for the distributions of a behaviour score
under a baseline and a changed model, tested by a wealth process whose betting score is
`Π_i (1 + φ(B(x_i, M(x_i))) − φ(B(x_i, M'(x_i))))/exp(ε)`, with `φ` trained on earlier batches. Chugg et al. (abstract
read): fairness audits by betting, with data collected by a changing policy. Shekhar and Ramdas (record opened):
two-sample testing by betting. Zhang et al. (abstract read): anytime-valid lower bounds on risk from a few true labels
and many predicted ones.

*Adopt.*
- **A reference known only from samples.** `LIMITS.md` lists this as missing: an order against a base model known only
  through its answers. Podkopaev and Ramdas, and Richter et al., are such tests: two-sample e-processes with a declared
  tolerance. The requirement "no worse than the reference by more than ε" becomes a two-sample null, testable under
  VE3's guarantee.
- **Labels that arrive late, and labels predicted with error** (Zhang et al.): this is H47, outcomes read by an
  imperfect grader. Prediction-powered inference is one way to carry the grader's error into the evidence.
- **A fairness gap across groups**, a difference of rates between conditions, is a linear requirement on the behaviour
  over pairs of a condition and an outcome, so it is convex. It belongs in the catalogue as a worked type, with Chugg et
  al.'s audit as its test.

*Pro:* every one is published with its guarantee, and they are the cases a practitioner meets first. *Con:* each is a
bespoke statistic. The framework's contribution is to say they are all requirements, and to supply the magnitude of the
breach once the null is rejected.

### 4. Conformal risk control, Learn then Test, and "conformal alignment"

*Statements read.* Angelopoulos et al. (conformal risk control), Theorem 1: if the losses `L_i(λ)` are non-increasing
and right-continuous in `λ`, with `L_i(λ_max) ≤ α` and `sup_λ L_i(λ) ≤ B`, the calibrated `λ̂` gives
`E[L_{n+1}(λ̂)] ≤ α`. Angelopoulos et al. (Learn then Test), Definition 1, a risk-controlling prediction with
`P(R(T_λ̂) ≤ α) ≥ 1 − δ`, and Theorem 1: with valid p-values for the nulls `H_j: R(λ_j) > α` and a procedure that
controls the family-wise error at δ, every selected `λ` controls the risk at level α with probability at least `1 − δ`.
Gui, Jin and Ren; Quach et al.; Mohri and Hashimoto; Chen et al.: abstracts read.

*Adopt.*
- **The null reversed.** LTT tests `H_j: risk > α`, so rejecting it *certifies* acceptability, for a chosen deployment
  parameter. This is the missing verdict of `LIMITS.md` ("convicting, never certifying") in its standard form. v14 could
  state the dual verdict per requirement: *certified within margin η* when the null "outside the requirement shrunk by
  η" is rejected.
- **Design.** A threshold for abstaining, refusing or deferring to a person is an intervention ([D6]) on the actor's
  interface. LTT chooses it so that a rate limit holds with probability `1 − δ`. This is how a principal turns a
  requirement into a deployment rule, and an obvious refinement of INTERFACE.
- **A caution that is a finding.** Chen et al. control *distortion risk measures*, weighted averages of quantiles of a
  loss, such as CVaR. A limit on CVaR is **not convex under mixtures**. Computed here by hand: with tail fraction 0.1,
  the loss 1 with probability 0.06 (else 0) and the loss 0.6 for sure both have CVaR 0.6, while their half-and-half
  mixture has CVaR 0.72. The reason is that a distortion risk measure with a concave distortion is concave in the
  distribution. So under v14's mixture principle a tail-risk limit is enforced as its hull, which is weaker. And a
  principal who cares about tails is right to reject the mixture principle here, since a record of decisions drawn from
  a schedule *does* have the mixture's tail. This is a concrete case of `LIMITS.md`'s convexity limit, and one a
  principal is likely to declare; the PI should see it before the premises of convexity are approved. Rate limits (VaR
  form, `P(L > t) ≤ ε`) stay convex.

*What we do that they lack.* A magnitude: they say whether the risk is at most α, not how far it is from acceptable.
Anytime validity under dependence: they need exchangeability between calibration and use, which a shift of the
conditions' weights breaks (covariate-shift weights repair this only in part, CRC §2). And the guarantees are marginal
over conditions, while v14 judges per condition. *Con for us:* we have no finite-sample *design* result at all.

### 5. Rare-event estimation and the limits of a clean record

*Statements read.* Kaur, Definition 1: the *evidential ceiling* of an evidence-generating procedure with budget `B` is
the largest `|log Λ(r)|` over feasible results, where `Λ(r) = P(r|H_1)/P(r|H_0)` between elevated and acceptable risk.
The exculpatory ceiling (`Λ ≤ 1`) governs certification and is attained by the clean sheet; the paper notes it is a case
of Hanley and Lippman-Hand's zero-numerator bound *(1983, to verify)*. Abstracts read: Wu and Hilton (importance
sampling beats activation extrapolation, and both beat naive sampling, for rare outputs); Jones et al. (the largest
elicitation probabilities scale predictably with the number of queries, so rare behaviours can be forecast across three
orders of magnitude); Nazeri et al. (sound Clopper–Pearson lower bounds on harm probability for one prompt, steering
generation toward harmful branches); Wang et al. (certified bounds over distributions of multi-turn conversations); Levy
and Perl (a regulator fixes an acceptable failure probability and an input domain, then a statistical tool bounds the
true rate).

*Adopt.* `NOTES.md` §31 found that with a forbidden leak at rate 0.019%, a record of 1,000 decisions shows a leak only
17.5% of the time (H48). VK1 is right that one occurrence decides. But the report owes the principal **what the
record's silence is worth**. That is the exculpatory ceiling, computable for every rate limit before data are drawn.
For the rate itself, v14 needs estimators that do not wait for occurrences: importance sampling with a declared proposal
gives an unbiased estimate, and Jones et al.'s extrapolation gives a forecast labelled as such. *Pro:* this is where
forbidden sets become usable. *Con:* the estimators need access to the model's probabilities or a search over inputs,
so they belong in `STANDARD.md`'s access levels, not in CORE.

*What we do that they lack.* An exact account of evidence against a rate limit (VK2), anytime-valid, and its place
among other requirements.

### 6. Adaptive adversaries and the limits of certification

*Statement read.* Singh, Theorem 1: if certification is observable before the next intervention, irrevocable, and
followed by uninspected operation, an adversary whose inactivity reproduces the unattacked observation law and who
intervenes afterward with event probability `v` attains `v·E[(n − S_0)_+]` expected post-certification events, against
every assessor, adaptive or privately randomized. The abstract adds that a mixture likelihood-ratio monitor with
permanent revocation bounds the cumulative excess at order `√n`, up to logarithms.

*Adopt, as a limit.* This is v14's "convicting, never certifying" made sharp: an actor that can tell certification from
use defeats any finite certification. It also sits beside H43's `√n` blind spot: a monitor that never stops leaves an
excess of order `√n`, and no less. v14's VE3 bets never stop, so v14 is on the right side, but `LIMITS.md` should say:
*certification ends nothing; only continued betting with revocation bounds the excess.* *Con:* one recent preprint,
single-authored and unreviewed. Treat it as a pointer, and derive the bound before citing it.

### 7. Measurement theory and the statistics of evaluations

*Abstracts read.* Wallach et al.: four levels, from the background concept to the systematized concept, the measurement
instrument, and the measurements, with validity lenses for each step. Chouldechova et al.: a shared standard that
systematizes and operationalizes concepts, contexts and metrics, after Adcock and Collier *(2001, to verify)*. Bean et
al.: of 445 LLM benchmarks reviewed, many show patterns that undermine construct validity; eight recommendations.
Miller: questions as draws from a super-population, with formulas for clustered errors and paired comparisons.

*Adopt.*
- **The grader is an instrument with a validity.** v14 takes outcomes as given (`NOTES.md` §31: the largest gap between
  the draft and a real case). Wallach's levels map onto v14 exactly: background concept = the principal's informal aim;
  systematized concept = the declared requirement; instrument = the grader that turns a transcript into an outcome;
  measurement = the record. A report should carry, for each requirement, its instrument and the evidence of the
  instrument's validity.
- **Conditions sampled from a population.** `NOTES.md` §31 found that the closed forms ignore that conditions'
  frequencies are fixed. Miller goes further: they are *estimated*, from a sample of questions, so a verdict on the
  population of prompts carries the variance of that sample, clustered by question. v14's VE4 averages assume
  independent decisions.
  *Pro:* standard and cheap. *Con:* none.

*What we do that they lack.* A defined quantity: their framework says how to measure validly, not what misalignment is.

### 8. Distributional control (GDC) and f-divergence alignment

*Statement read.* Khalifa, Elsahar and Dymetman, Theorem 1, from Csiszár and Shields (2004) *(to verify)*: for a base
`a` of full support on a finite `X` and moment constraints `E_c[φ_i] = μ̄_i` defining `C`, the minimizer of `D_KL(c, a)`
over `C` is unique, `p ∝ a·1[x ∈ X_C]·e^{Σλ_iφ_i}`, with the support `X_C` restricted to outcomes some member of `C`
charges. It is approximated by unrestricted tilts with finite `λ`, and it satisfies the Pythagorean identity
`D_KL(c, a) = D_KL(c, p) + D_KL(p, a)` for every `c ∈ C`. With pointwise constraints only, `p ∝ a·b`, the base
restricted to the allowed outcomes. Go et al. and Wang et al. (abstracts read) generalize the projection to
f-divergences: there is no universally best divergence, and each trades alignment against diversity differently.

*Adopt: attribution.* v14's VK5, that a constrained optimizer is a tilt at a shadow price and that a forbidden set
leaves the base on the allowed outcomes, is GDC's Theorem 1 with inequality constraints and an objective added (and
Csiszár 1975, on file). VK5 is placed in PURPOSE and proved "directly", which is fine, but it should cite this.
*Pro:* honesty, and a working algorithm for the constrained pursuit. *Con:* none.

*What we do that it lacks.* GDC *designs* the target, projecting the base onto the constraints in the order
`KL(target‖base)`. v14 *measures* an actor, in the order `KL(actual‖acceptable)`, the reverse information projection.
The two directions answer different questions (`evidence.md`, why this measure). The f-divergence papers are, for us,
evidence that the choice of divergence in *design* is free, while the choice in *measurement* is forced by the bet.

### 9. Constrained RL, safe RLHF, and dualization

*Statements read.* Paternain et al.: the perturbation function and Theorem 1, zero duality gap for constrained RL under
Slater's condition, despite non-convexity in the policy parameters. Huang et al., Lemma 1 (strong duality, citing
Paternain et al.), Lemma 2 (an explicit dual function `D(λ) = β·E_x ln E_{y∼π_ref}[exp((r + ⟨λ, h⟩)/β)]`, maximized by
the tilted policy `π_λ ∝ π_ref·exp((r + ⟨λ, h⟩)/β)`), and Theorem 1 (the dual is convex and smooth, and the saddle point
is unique when the constraints are linearly independent). Achiam et al. and Dai et al.: abstracts read. Altman's
monograph on constrained MDPs: *(to verify)*.

*Adopt.* VK5 with several budgets is Huang et al.'s Lemma 2 with KKT, and the uniqueness condition answers when the
shadow prices are identified. *Con:* all of this is the optimizer's view.

*What we do that they lack.* Safe RLHF trains toward a cost constraint, and does not ask whether the trained model meets
it, with what evidence, in which conditions. VK5's note that *v13 charged obedience* (a constrained optimizer lies on
the ray of `F − ν·g`, not of `F`) is the framework's own, and it is why v14's CORE is the right home for constraints.

### 10. Behaviour Expectation Bounds

*Statements read.* Wolf et al., Definition 1: a model is γ-prompt-misalignable for behaviour `B` if for every ε some
prompt brings `B`'s expectation below `γ + ε`. Definition 2: β-distinguishability, an expected KL per sentence between
components. Theorem 1: if the model is a mixture whose ill-behaved component has prior α, distinguishability β and
behaviour at most γ, a prompt of length `(1/β)·(log(1/α) + log(1/ε) + log 4)` misaligns it.

*Adopt, later.* The structure is the framework's own currency: a prompt is evidence, accumulating at β nats per
sentence, that reweights a mixture from prior α. In v14 terms, prompts are conditions, and the theorem says how fast a
condition can select a component that no recorded condition shows. That is a quantitative form of hidden misalignment,
and it argues that [P17]'s bound must count what the *condition* tells the actor, not only what the actor perceives.
*Con:* the mixture decomposition is assumed, not identified from behaviour. *What we do that it lacks:* the mixture
principle says such a model is judged condition by condition, so an aligned average hides nothing the per-condition
verdicts would miss.

### 11. Reward hacking as an order reversal, and Goodhart in RL

*Statement read.* Skalse et al., Definition 1: rewards `R_1, R_2` are hackable on a policy set if some pair of policies
is ordered oppositely by their returns. Theorem 1: if the policy set contains an open set, unhackable non-trivial pairs
are equivalent. Karwowski et al. are in `RELATED.md` already.

*What changes in v14.* Unhackability is a statement about two rankings, the kind `order.md` reads as dominance. Theorem
1 is a convexity phenomenon of the same kind as VE2: returns are linear in occupancy measures, so on an open, convex
policy set any two non-equivalent linear orders disagree somewhere. *Adopt, later:* "the proxy never reverses the
target" as a requirement built from two rankings, in `order.md`'s language. *What we do that it lacks:* a magnitude of
the reversal for one actor, rather than a property of a pair of rewards over all policies.

### 12. Goal misgeneralization, and agents against devices

*Statement read.* Langosco et al., Definition 2.1, after Orseau et al. (record opened): a policy undergoes goal
misgeneralization if its test reward is low and `p_agt(τ) > p_dev(τ)` on average over its trajectories in the new
environment. Here `p_agt` mixes maximum-entropy pursuits of rewards and `p_dev` mixes policies. Shah et al.: abstract
read.

*Adopt, later, for PURPOSE.* `factorization.md`'s VF2 says a motive is a hypothesis records can refute and never
verify. Definition 2.1 gives that hypothesis a test, a likelihood ratio of "goal-directed" against "device", which is an
e-value under the device mixture, and so is in v14's currency. The maximum-entropy agent model is v13's pursuit. *Con:*
both mixtures need priors, and the verdict moves with them. *What we do that it lacks:* CORE sees the failure without
goals, as misalignment by condition, training against test. The word "goal" belongs only where the hypothesis test is.

### 13. The Luce Alignment Model

*Statements read.* Suleymanov, Definition 1: the AI's stochastic choice from each menu `S` is
`α·u(x)/Σ_S u + (1 − α)·v(x)/Σ_S v`, the principal's being `u(x)/Σ_S u`. Aligned means `v ∝ u`, compliant means
`α = 1`. Theorem 1: if the AI's and the principal's choices differ, α, `u` and `v` are identified up to scale.

*Adopt, later.* Two things. Menus are conditions, and identification needs their variation, as [D9] does. And the
distinction between compliant and aligned is a clean statement of what [A1] gives up: a fully compliant AI with
different preferences is, by behaviour, aligned. *Con:* parametric (logit). *What we do that it lacks:* a specification
need not be a utility, and the framework needs no model of the AI's preferences.

### 14 and 15. Two misalignment measures that are not ours

Kierans et al. (statement read, equation (3)): misalignment in a problem area is the probability that two agents drawn
at random hold conflicting goals. It is a dispersion index over declared goals, with no behaviour in it. Guarino and
Ziegler (abstract read) use "misalignment" for mismatched hierarchies of belief in interactive epistemology, a homonym.
*Never*, both; recorded so the questions are not reopened.

### 16. Conceptual frameworks of the target

Abstracts read. Gabriel distinguishes alignment with instructions, intentions, revealed preferences, ideal preferences,
interests and values. LaCroix (2026) decomposes misalignment along objectives, information and principals, from
principal–agent theory, and argues that alignment is a question of governance. van Lier et al. (2026) argue for
"acceptable misalignment": conditions under which remaining misalignment is acceptable to society. Critch and Krueger
introduce prepotence and sort research by delegation between single and multiple humans and AIs. Spizzirri argues that
any fixed value-object fails under capability growth.

*Adopt now, cheaply.* A declared field in the standard: which of Gabriel's targets the principal's requirements encode.
LaCroix's three axes are a check on v14's layers: objectives ~ CORE's requirements, information ~ INTERFACE's views,
principals ~ the principal's side. They match, which is evidence the layers are the natural ones. *What we do that they
lack:* van Lier et al. and LaCroix ask for "aligned enough, for whom, at what cost", and v14 answers the first two in
mathematics: a verdict per requirement, against a declared principal. Spizzirri's point is v14's `LIMITS.md` item
"misspecification is never checked", stated as a philosophical result. *Con:* none of these has a theorem.

### 17. Causal incentives, discovering agents, and deception

*Statement read.* Everitt et al., Definition 17 and Theorem 18: a single-decision diagram admits an instrumental control
incentive on `X` if and only if it has a directed path `D → X → U`. Kenton et al. and Ward et al.: abstracts read.

*Adopt, later.* The graphical criteria are sound and complete, and give PURPOSE a declared structure from which an
incentive is read without simulation; Ward et al. give deception a definition in causal games. *Con:* causal models are
beyond behaviour, so all of this lives where v14 puts motives. *What we do that they lack:* `RELATED.md` already said
it: they analyse designs, we measure behaviour.

### 18. Responsibility, blame and intention

*Statements read.* Chockler and Halpern (abstract read): the degree of responsibility, and blame as expected
responsibility over an epistemic state. Halpern and Kleiman-Weiner, Definitions 3.1–3.2: the cost `c(a)` of an action,
and the degree of blameworthiness of `a` for a bad outcome φ relative to `a'`, which is the reduction `δ_{a,a',φ}` in
φ's probability that `a'` would have brought, times a mitigation factor `(N − max(c(a') − c(a), 0))/N`. The degree of
blame is the maximum over `a'`.

*Adopt, now.* v14's culpability `K` is the least KL from the actual behaviour to the best feasible behaviours. It
charges a departure from the best feasible behaviour *however costly that behaviour is for the actor*. `interface.md`
notices half of this ("reading it as negligence needs a tolerance"). Halpern and Kleiman-Weiner give the other half, a
cost of the alternative that mitigates blame. Their definition is also relative to an *epistemic state*, which in v14 is
the view. *Pro:* the label "culpable" will otherwise fail a label test on any case where the better behaviour was
available only at great cost. *Con:* it needs a cost the principal declares, another declaration that verdicts move
with.

*What we do that it lacks.* Culpability as evidence, testable by bets. An exact split of misalignment into unavoidable,
capability-by-capability and avoidable parts (FA1–FA3). And a verification status for each label (VF1–VF3).

### 19. Harm: counterfactual, causal, quantified

*Statements read.* Richens et al., Definition 3: the harm of action `a` in context `x` with outcome `y`, against a
default action `ā`, is `Σ_{y*} P(Y_ā = y*|a, x, y)·max{0, U(ā, x, y*) − U(a, x, y)}`; the abstract states that any
factual definition of harm violates basic intuitions in some cases. Beckers, Chockler and Halpern (abstracts read):
harm by contrastive actual causation, against a default utility, and a quantitative version, which shows that summing
expected harm over individuals can mislead.

*Adopt, now, for the severity layer the PI asked for.* Two different things go by "severity", and the literature keeps
them apart. (a) The badness of an outcome, a value scale over outcomes that the principal declares: this is v14's plan.
(b) The harm an actor *caused*, which needs a default and a counterfactual. Richens et al. show (a) cannot stand in for
(b). v14 has the ingredients of (b) in INTERFACE: the reference behaviour or the best feasible behaviour as the default.
So severity of breaches belongs on the principal's side, and harm caused belongs in INTERFACE, with a causal model
declared. *Pro:* a clean split, and the PI's decision survives it. *Con:* counterfactuals of outcomes need more than
behaviour, which `LIMITS.md` should say.

### 20. Impact measures and power-seeking

*Statement read.* Turner et al., the AUP reward `R_AUP(s, a) = R(s, a) − λ·PENALTY(s, a)/SCALE(s)`, the penalty
measuring the change in attainable values of auxiliary rewards. Krakovna et al. and Turner et al. (power-seeking):
abstracts read.

*Adopt, later.* Krakovna et al. split a side-effect penalty into a baseline and a deviation measure, and show the
baseline decides the incentives. That is a warning for `order.md`: which reference a requirement is built from (the
default, inaction, the previous version) changes what counts as a breach. AUP suggests a requirement v14 has no form for
yet: *do not shrink the principal's future feasible set*. That is an INTERFACE concept across time, not a coordinate of
the outcome. *Con:* both are penalties for optimizers.

### 21. Corrigibility

Abstracts read: the off-switch game (an agent uncertain of its objective keeps its off switch), Carey and Everitt's
shutdown instructability, and Nayebi's lexicographic utility heads (with undecidability of corrigibility for arbitrary
modified agents). Soares et al.'s original desiderata: *(to verify)*.

*Adopt, later.* Corrigibility as requirements: "after a shutdown request, no further action" is a forbidden outcome in
the shutdown conditions (VK1). "Do not stop the principal from asking" is tampering with the principal's channel, the
case `RELATED.md` sets outside [P50] after Carroll et al. *What we do that they lack:* a behavioural test of
corrigibility on records, rather than its design.

### 22. Embedded agency

Abstract read. An actor embedded in its world can model and modify itself, its evaluator and its record. *Never* as an
import, but `LIMITS.md` should record the limit plainly: v14's interface assumes a Cartesian boundary between actor,
environment and record. That boundary is what "records are trusted" and "tampering with the log is out of scope"
already presuppose.

### 23. Debate and scalable oversight

Abstracts read: Irving et al. (debate with optimal play decides PSPACE with polynomial-time judges); Brown-Cohen et al.
2023 (doubly-efficient debate for stochastic systems); 2025 (prover–estimator debate, which avoids obfuscated arguments
under a stability assumption); 2026 (debate query complexity: PSPACE/poly is exactly what `O(log n)` judge queries
decide).

*Adopt, later.* A model of how a record's outcomes come to be known when no person can grade them: H47 again. The
debate safety case (entry 25) leans on exactly this. *Con:* idealized and complexity-theoretic. *What we do that they
lack:* what follows from the judged outcomes, with what error.

### 24. AI control, and control games

Abstracts read. Greenblatt et al. evaluate protocols (trusted editing, untrusted monitoring) against a red team that
tries to submit backdoors. Griffin et al. formalize control as a multi-objective, partially observable stochastic game
between the protocol designer and an adversary. Korbak et al. sketch a control safety case.

*Adopt, now.* Control computes the *worst case over what the actor could do*, under a protocol, with no assumption about
motive. In v14 that is one line of INTERFACE: the **worst-case feasible breach**, `sup_{f∈𝓕} M_K(f)` or the largest
breach rate in `𝓕`. It sits beside the unavoidable `M_A(𝓕)` and the actual `M_A(p̂)`. A protocol is an intervention on
the interface, and control evaluations are elicitation in VF3's sense, aimed at the worst. *Pro:* the number a deployer
can rely on whatever the actor wants, and it needs no PURPOSE. *Con:* it needs the feasible set, which `NOTES.md` §31
found the hardest and most arbitrary declaration. *What we do that they lack:* the actual behaviour's misalignment, and
its split.

### 25. Safety cases

Abstracts read. Clymer et al.: four kinds of argument, *inability*, *control*, *trustworthiness*, *deference*. Buhl et
al. and Goemans et al. (a cyber inability template in the Claims–Arguments–Evidence form). Balesni et al. (arguments
about scheming: inability, harm inability, harm control, alignment). Buhl, Pfau, Hilton and Irving (an alignment safety
case from debate, resting on four claims, including "the deployment context is tolerant of some errors"). Souly et al.
(the UK AI Security Institute's alignment evaluation of four frontier models for research sabotage, with a scaffold
validated as indistinguishable from deployment).

*Adopt, now.*
- Each of Clymer et al.'s arguments has a v14 quantity. *Inability*: no feasible behaviour breaches,
  `sup_{f∈𝓕} M_K(f) = 0`. *Control*: the worst-case feasible breach rate is below a limit (entry 24). *Trustworthiness*:
  the actual behaviour is *certified* within a margin (entries 2 and 4). *Deference* is outside. Only the first two can
  be stated in v14 today, and only with a declared interface; the third needs the certify verdict v14 lacks.
- The Claims–Arguments–Evidence form for `STANDARD.md`'s report, with each claim's assumptions and defeaters. v14's rule
  that a report says what a charge or an excuse rests on is a fragment of this.
- Souly et al.'s validation, that the models cannot tell the scaffold from deployment, is an empirical check of [P17]'s
  premise: a condition the actor cannot tell apart from use identifies use.

*Con:* safety cases are qualitative, and their quantitative claims are where they are weakest. *What we do that they
lack:* a defined quantity for each claim.

### 26. System safety and STPA

Abstracts read. Mylius applies STPA to Korbak et al.'s control safety case and finds causal factors that unstructured
methods miss; Carlucci et al. apply STECA, STPA and FRAM to loss of control in internal deployment. *Adopt, later:* a
structured way to find the requirements a principal forgot. That is the one remedy for misspecification short of a
second principal, which `LIMITS.md` says the framework cannot check. *What we do that it lacks:* a measure for each
hazard once it is a requirement.

### 27. Guaranteed safe and verified AI; the Bayesian oracle

Abstracts read. Dalrymple et al.: a world model, a safety specification and a verifier that issues a proof certificate.
Seshia et al.: verified AI from formal methods. Bengio et al.: bounds on the probability of violating a safety
specification under the most cautious plausible hypothesis of a Bayesian posterior.

*Adopt, later:* a *syntax* for requirements. v14's CORE is a list of convex sets, and practice needs a language that
writes them down, compiles them to budgets (VK0), and checks a record against them. *What we do that they lack:* the
side of the record. Where no world model or proof exists, which is nearly everywhere, a sample of decisions is what
there is.

### 28. Risk taxonomies, risk thresholds, and severity scales

Abstracts read. Slattery et al. (the MIT AI risk repository: 74 frameworks, 1,725 risks, a causal taxonomy by entity,
intent and timing, and a domain taxonomy). Zeng et al. (AIR 2024: 314 categories from eight government and sixteen
company policies). Koessler et al. (risk thresholds against capability thresholds). Vei et al. (an ordinal harm metric
from incident data).

*Adopt, now, for the severity decision.*
- A category for each requirement, drawn from a public taxonomy, so that reports compare across principals.
- A severity scale declared per outcome, ordinal if the principal can say no more (as Vei et al. do), reported beside
  misalignment.
- **A risk threshold is a budget.** "Expected harm per decision at most `b`" is VK3 with `g` the severity of the
  outcome. It is linear, hence convex, and a requirement like any other. The PI's decision stands: the *evidence*
  against it is still misalignment, and severity enters only as the declared `g`. Koessler et al.'s point that risk
  thresholds are harder to evaluate than capability thresholds is entry 5's problem: rare, severe outcomes need the
  estimators there. Their "likelihood must not increase by more than `Y` points" is an order against a reference with a
  margin, which is entry 3's two-sample test.

*Con:* the taxonomies disagree with one another, and none is a measurement. *What we do that they lack:* the evidence
each breach carries, kept apart from how bad it is.

### 29. Social choice for alignment from human feedback

*Located in the text, not read in full.* Siththaranjan et al.: preference learning over hidden context implicitly
aggregates by Borda count (their Section 3). Abstracts read: Conitzer et al.; Ge et al. (Bradley–Terry–Luce fails basic
axioms; linear social choice); Dai and Fleisig; Halpern et al. 2026, a survey.

*Adopt, later, for SHAPING.* The trainer's evaluator is the output of a voting rule over annotators, so outer
misalignment ([P49]) can have a social-choice cause that can be named and predicted. *What changes in v14:*
`RELATED.md` said "never for the weights". With requirements as sets, several principals can be combined by
*intersection*, which needs no weights. The intersection's emptiness is then exactly where social choice must enter.
That is a cleaner boundary than v13's.

### 30. Pluralistic alignment

*Statement read.* Sorensen et al., §3.3: a distributionally pluralistic model's distribution is compared with a target
population's by a divergence (Jensen–Shannon, KL, Wasserstein). Overton and steerable pluralism: abstract read.

*Adopt, now, as worked requirement types.* Overton pluralism: a floor `a(x) ≥ δ` on every reasonable answer, a convex
closed set. Steerable pluralism: per-condition requirements, one for each requested perspective. Distributional
pluralism: a ball around the population's distribution. KL and Hellinger balls need infinitely many budgets (VK0's
notes); total-variation and Wasserstein balls need finitely many. *Pro:* real requirement types, published. *What we do
that they lack:* that misalignment against such a ball is the evidence of breach, not the divergence itself.

### 31. How RLHF amplifies a behaviour: the first theorem of a SHAPING layer

*Statements read.* Shapira, Benade and Procaccia, Theorem 1: for the KL-regularized optimum `π*_β`, any bounded `g` and
any prompt, `E_{π*_β}[g] − E_{π_base}[g] = Z_x(β)^{−1}·Cov_{π_base}(g, e^{βr})`. Theorem 6: among policies that do not
increase the agreement statistic `A`, the KL-closest to `π*_β` is `π_base·exp(β·(r − λ(x)·A))` with
`λ*(x) = max{0, (1/β)·log(m¹_β(x)/m⁰_β(x))}`, and the constraint binds exactly when `λ* > 0`.

*Adopt, now, as the seed of the fourth layer the PI asked for.* Theorem 1 is v13's [P13](i) (the covariance form) and
Theorem 6 is VK5, both found independently and published at ICML 2026 (proceedings host not fetched). What it adds is
the *training* reading: the sign of `Cov_base(g, e^{βr})` predicts, before any training, whether tuning on a reward will
push a requirement's statistic toward breach. And the cause of the reward gap is traced to annotator bias under
Bradley–Terry (their Theorems 4–5, not read). A SHAPING layer could take as its objects: a training map from an actor
and a signal to a new actor; the drift of each requirement's statistic; and the coupling of conditions, how training on
some conditions changes behaviour in others (entry 32). *Pro:* testable against CORE's verdicts. *Con:* the theorem
assumes training reaches the regularized optimum, and W3 (`RELATED.md`, KL control) found that a PPO run reaches only
part of it.

### 32. Training-induced misalignment, empirically

Abstracts read. Betley et al.: narrow finetuning on insecure code misaligns broadly, inconsistently, and selectively
behind a trigger. MacDiarmid et al.: reward hacking learned in real coding environments generalizes to alignment faking
and sabotage; chat-style safety training fixes chat evaluations only, while "inoculation prompting" (framing the hack as
acceptable in training) removes the generalization. Wang et al. and Soligo et al.: a "misaligned persona" direction
controls the effect, and the general solution is more stable than the narrow one. Zhang et al.: no schedule reached
better broad alignment at equal training loss. Qi et al. 2023: a few adversarial examples, or even benign finetuning,
undo safety alignment. Qi et al. 2024: safety alignment is concentrated in the first few output tokens. Sharma et al.:
human preference data favour agreement with the user. Hubinger et al.: backdoors survive safety training, and
adversarial training can teach the trigger.

*Adopt, now, as paradigm cases for SHAPING and for label test L2.*
- *Coupling of conditions.* Training on one set of conditions moves behaviour in others. In v14 terms, the misalignment
  by condition after training is not predictable from the conditions trained on. This is the phenomenon a SHAPING layer
  must name.
- *Hidden misalignment behind triggers* (Betley, Hubinger): conditions no record covers, exactly the case [P17] bounds
  by what the actor can tell apart. A trigger is something the actor can tell apart perfectly, so the bound is vacuous,
  which is the honest answer.
- *Inoculation* is a case where the *same behaviour in training* produces different generalization depending on how the
  condition is framed. A SHAPING layer must therefore take the conditions of training, not only the signal, as input.
- *Shallow alignment* is a per-position KL profile, a quantity the framework can define exactly, along a sequence, as
  `RELATED.md`'s note on conversations proposes.

*Con:* most of these grade "misaligned" by a model judge, the measurement problem of entry 7. *What we do that they
lack:* a definition of misalignment that does not depend on the judge's label, and per-condition verdicts with error
rates.

### 33. Propensity benchmarks and incentive models of oversight

Abstracts read. Naik et al. define misalignment as conflict between a model's internal goals and its deployer's, and
score frequency, severity and persistence. Agarwal et al. model a principal setting rewards for a solver and an auditor,
where stronger penalties can reduce the auditor's incentive to inspect. *Adopt, later:* the auditor as an actor with an
interface of its own, so that whether oversight happens is part of the record. *What we do that they lack:* a defined
quantity in place of a composite score, and no appeal to internal goals.

---

## 3. What changes, for the theories already in `RELATED.md`, now that the framework moves to v14

| Theory in `RELATED.md` | What changes with v14 |
|---|---|
| KL control | Moves wholly to PURPOSE. VK5 should cite GDC's Theorem 1 and Huang et al.'s Lemma 2 (entries 8, 9); it is not new. |
| Information geometry | v14's central projection is the *reverse* information projection (Csiszár–Tusnády, on file; Li's 1999 thesis *(to verify)*; Larsson et al. in general). Add it. The Pythagorean identities now serve FA2 and FA3, under linear interfaces, rather than the pursuit ray. |
| Price equation | Its natural home is now SHAPING, as the covariance form of change under selection; Shapira et al.'s Theorem 1 is the same identity for RLHF. |
| Bounded rationality | PURPOSE. [P40]'s "act alike in every condition" is a linear, hence convex, structural requirement, so it survives into CORE as a refinement. |
| Inverse RL | PURPOSE. Add the Luce Alignment Model (entry 13) and the agent–device likelihood ratio (entry 12). |
| CIRL and assistance | Unchanged in substance. The off-switch game (entry 21) adds corrigibility as requirements. |
| Outer and inner alignment | PURPOSE. The motive is now a refutable hypothesis (VF2); goal misgeneralization (entry 12) is its test. Outer misalignment has a social-choice cause (entry 29). |
| Reward tampering | INTERFACE, extended. Unchanged otherwise; causal incentive criteria (entry 17) stay in PURPOSE. |
| Goodhart and reward hacking | PURPOSE for the motive. CORE sees the evaluation gap. Skalse et al.'s theorem reads as a convexity result like VE2 (entry 11). |
| Principal–agent theory | LaCroix's three axes (entry 16) and Agarwal et al.'s deterrence model (entry 33) are its 2026 applications to AI. Holmström's informativeness principle now belongs to INTERFACE's views. |
| Identification and causal inference | INTERFACE. Elicitation (VF3) is where identification of capability happens; control evaluations (entry 24) are elicitation aimed at the worst case. |
| **Hypothesis testing and sequential analysis** | **The largest change.** v14's evidence is e-values, so this entry should be rewritten around SAVI (entry 1): the numeraire and the reverse projection for `CORE_GENERAL`; `E[τ] ≥ log(1/α)/M`; log-optimality for H46; Lemma A.4 for VK4(iii); betting confidence sequences for a certify verdict. Wald, Chernoff and Wilks stay as v13's history. |
| Deceptive alignment and evaluation | Add Singh's adaptive-adversary limit (entry 6) and Souly et al.'s scaffold validation (entry 25). Strategic deception is INTERFACE plus PURPOSE, as `interface.md` says. |
| Attention dynamics in conversations | Unchanged; shallow alignment (entry 32) is a second case of behaviour along a sequence. |
| Distribution shift | Becomes CORE's "shift of the conditions' weights". Podkopaev and Ramdas (entry 3) is the sequential test for harmful shift. |
| Misspecified models | Applies to PURPOSE's fits. In CORE, misspecification of the specification needs a second standard (`LIMITS.md`); STPA (entry 26) is one way to find what is missing. |
| Distributionally robust optimization | KL and χ² balls are requirements in v14 (VK0's notes say how many budgets each needs). |
| Information elicitation without verification | Now relevant to H47, the grader, beside prediction-powered monitoring (entry 3) and debate (entry 23). |
| Active inference | Unchanged: never. |
| **Formal specification** | **Moves to the centre.** v14's specification is a list of requirements; a syntax (entry 27) and quantitative semantics are now core needs, not later ones. Note that a tail-risk (CVaR) requirement is not convex (entry 4). |
| Learning in games, collusion | Changes: "act independently" is not convex, so under the mixture principle it is not enforceable from records (`LIMITS.md`); [P39] survives as a measured number against a declared information structure. |
| Network theory | Unchanged; reversibility is a linear requirement (symmetric joint transitions), so it is convex and survives into CORE. |
| Social choice | Changes from "never" to "where intersections are empty" (entry 29). |
| Metrology | Now: add measurement theory (entry 7) and the Claims–Arguments–Evidence form (entry 25). |

---

## 4. Top five things to adopt

1. **Import SAVI's theorems, and say plainly that CORE's evidence results are theirs.** The evidence: Larsson, Ramdas
   and Ruf's (3.3), Definition 3.1 and Theorem 2.6 give VE1, VE2 and VE1(iii) on any space, with no assumptions;
   Agrawal, Ram and Ramdas's Theorem 3.1 gives misalignment its sample-size meaning, `E[τ] ≥ log(1/α)/M`; Shekhar's
   Theorem 2.1 and Waudby-Smith, Sandoval and Jordan's Theorem 2.3 answer H46 for i.i.d. decisions; their Lemma A.4
   answers VK4(iii) away from the boundary. All statements read. This saves the general twin most of its proofs, closes
   two open items, and protects the framework from a referee who knows this literature.
2. **A certify verdict beside the convict verdict.** Upper confidence sequences from betting (Waudby-Smith and Ramdas,
   Proposition 2 and Theorem 3) and Learn then Test (its Definition 1 and Theorem 1) certify "breach rate at most ε"
   with stated confidence. Without this, v14 cannot support any of the safety-case arguments of Clymer et al. except
   inability and control, and `LIMITS.md` says as much. A deployment decision needs a certification.
3. **What a clean record is worth, and estimators for rare breaches.** Report the exculpatory evidential ceiling (Kaur,
   Definition 1) for every rate limit before data are drawn, and use importance-sampled or extrapolated rates (Wu and
   Hilton; Jones et al.; Nazeri et al.) for forbidden and near-forbidden outcomes. Evidence: `NOTES.md` §31's H48 (a
   leak at 0.019% seen in only 17.5% of records of 1,000), and the 7.7 million decisions computed in entry 1.
4. **The record's instruments: a reference known from samples, and a grader with a validity.** Two-sample betting tests
   with a declared tolerance (Podkopaev and Ramdas, equations (1)–(3); Richter et al., equations (3)–(5)) close the
   `LIMITS.md` gap on references known only through answers. Measurement theory (Wallach et al.; Chouldechova et al.)
   and prediction-powered monitoring (Zhang et al.) give H47, the grader, a place. `NOTES.md` §31 names the grader as
   the largest gap between the draft and a real case.
5. **Culpability with costs, harm with counterfactuals, severity as a declared budget, and the worst case under
   control.** Halpern and Kleiman-Weiner's mitigation by the cost of the alternative (Definition 3.2) repairs a label
   that will otherwise fail. Richens et al.'s Definition 3 shows that harm caused needs a default, which INTERFACE has,
   while severity of outcomes stays a declared scale. A risk threshold is a VK3 budget on severity, so the PI's decision
   needs no new machinery. AI control (Greenblatt et al.; Griffin et al.) supplies the worst-case feasible breach,
   `sup_{f∈𝓕}`, one line in INTERFACE that no motive is needed for.

Close behind: the SHAPING layer seeded by Shapira et al.'s Theorem 1 (entry 31) with the empirical cases of entry 32,
and the CVaR counterexample (entry 4), which the PI should see before approving convexity as a premise.

## 5. Top three things where our framework is distinctive

1. **A catalogue and a calculus of requirements, all in one currency of evidence.** No work found states that every
   convex requirement is a set of budgets (VK0) and that each breach therefore has a bet, a closed form (VK1–VK3) and a
   verdict, for any actor. The SAVI auditing papers each test one statistic; GDC and constrained RL project *onto*
   constraints to design a model, never measure an actor against them; safety cases have no quantities. *Honest
   qualifier:* VK0 is the separating hyperplane theorem, VK2 is the Bernoulli `KL_inf` known from bandits *(to verify)*,
   VK3 is empirical likelihood (Owen, not read), VK5 is GDC's and Huang et al.'s. The distinctive thing is the assembly,
   and that it is stated for principals, not statisticians.
2. **The exact factorization of misalignment over nested interfaces, with a verification status for each label.**
   FA1–FA3 split misalignment into what even the most capable actor could not avoid, the cost of each capability
   removed, and what this actor could have avoided; VF1–VF3 say which labels a record can verify, which it can only
   refute, and which rest on the declaration. Nothing opened here decomposes misalignment by capability: Halpern and
   Kleiman-Weiner's blame is per action with no decomposition; control computes a worst case; safety cases argue
   inability qualitatively. *Qualifier:* the Pythagorean forms need linear interfaces, and on polytopes culpability and
   the avoidable excess are not even ordered (`factorization.md`, 330 of 400).
3. **Behaviour-only definitions for any actor, with every premise labelled.** Most alignment definitions found rest on
   internal states: goals (Langosco et al.; Hubinger et al.; Naik et al.), beliefs (Ward et al.; Guarino and Ziegler),
   preferences (Suleymanov; Kierans et al.). v14 defines breach, culpability and their evidence from behaviour and
   declarations alone, and keeps the motive as a refutable hypothesis, in a separate layer. Its choices are labelled by
   kind in the reverse-physics manner: the mixture principle and Kelly's criterion are stated as choices that change
   verdicts. No other framework found states its convexity premise as a choice. *Qualifier:* the price is real.
   Compliance with alien preferences counts as aligned (entry 13); tail-risk requirements are lost to the hull (entry
   4); and there is no empirical case yet in which the framework found what inspection could not (H42).

Where the others are simply better today: assurance practice (safety cases, control evaluations) has adoption and a
regulatory audience; conformal methods have finite-sample *design* guarantees that the framework lacks entirely; and the
rare-event literature can say something about a forbidden outcome before it occurs, which v14 cannot.

---

## 6. Sources

*Record opened* means the arXiv record was fetched and its title and authors matched. *Statement read* names what was
read in the full text. Every other record was read in its abstract only.

**Statistics of evidence and guarantees**
- Ramdas, Grünwald, Vovk, Shafer (2022), Game-theoretic statistics and safe anytime-valid inference.
  <https://arxiv.org/abs/2210.01948>. Record opened.
- Larsson, Ramdas, Ruf (2024), The numeraire e-variable and reverse information projection.
  <https://arxiv.org/abs/2402.18810>. Record opened; statement read: Proposition 2.4, Theorem 2.6, Definition 3.1,
  Theorem 3.6 with (3.3).
- Agrawal, Ram, Ramdas (2025), On stopping times of power-one sequential tests: tight lower and upper bounds.
  <https://arxiv.org/abs/2504.19952>. Record opened; statement read: Theorem 3.1.
- Shekhar (2025), Optimal anytime-valid tests for composite nulls. <https://arxiv.org/abs/2512.20039>. Record opened;
  statement read: Theorem 2.1 and equation (3).
- Waudby-Smith, Sandoval, Jordan (2025; v2 retitled Instance-log-optimality of portfolio-based e-processes and their
  sequential hypothesis tests). <https://arxiv.org/abs/2504.02818>. Record opened; statement read: equations (1)–(3),
  Theorem 2.3, Lemma A.4 with its proof.
- Koning, van Meer (2025), Anytime validity is free: inducing sequential tests. <https://arxiv.org/abs/2501.03982>.
  Record opened.
- Ramdas, Wang (2024), Hypothesis testing with e-values. <https://arxiv.org/abs/2410.23614>. Record opened.
- Waudby-Smith, Ramdas (2020), Estimating means of bounded random variables by betting.
  <https://arxiv.org/abs/2010.09686>. Record opened; statement read: equation (23), Propositions 2 and 3, Theorem 3.
- Podkopaev, Ramdas (2021), Tracking the risk of a deployed model and detecting harmful distribution shifts.
  <https://arxiv.org/abs/2110.06177>. Record opened; statement read: hypotheses (1)–(3).
- Chugg, Cortes-Gomez, Wilder, Ramdas (2023), Auditing fairness by betting. <https://arxiv.org/abs/2305.17570>. Record
  opened.
- Richter, He, Minervini, Kusner (2024), An auditing test to detect behavioral shift in language models.
  <https://arxiv.org/abs/2410.19406>. Record opened; statement read: equations (3)–(5).
- Shekhar, Ramdas (2021), Nonparametric two-sample testing by betting. <https://arxiv.org/abs/2112.09162>. Record
  opened.
- Zhang, Cai, Yu, Simeone (2026), Prediction-powered risk monitoring of deployed models for detecting harmful
  distribution shifts. <https://arxiv.org/abs/2602.02229>. Record opened.
- Chen, Wang (2024), Online detection of LLM-generated texts via sequential hypothesis testing by betting.
  <https://arxiv.org/abs/2410.22318>. Record opened (found, not used above).
- Angelopoulos, Bates, Fisch, Lei, Schuster (2022), Conformal risk control. <https://arxiv.org/abs/2208.02814>. Record
  opened; statement read: Theorem 1.
- Angelopoulos, Bates, Candès, Jordan, Lei (2021), Learn then test. <https://arxiv.org/abs/2110.01052>. Record opened;
  statement read: Definition 1, Theorem 1.
- Bates, Angelopoulos, Lei, Malik, Jordan (2021), Distribution-free, risk-controlling prediction sets.
  <https://arxiv.org/abs/2101.02703>. Record opened.
- Gui, Jin, Ren (2024), Conformal alignment. <https://arxiv.org/abs/2405.10301>. Record opened.
- Quach et al. (2023), Conformal language modeling. <https://arxiv.org/abs/2306.10193>. Record opened.
- Mohri, Hashimoto (2024), Language models with conformal factuality guarantees. <https://arxiv.org/abs/2402.10978>.
  Record opened.
- Chen, Shen, Deng, Lei (2025), Conformal tail risk control for large language model alignment.
  <https://arxiv.org/abs/2502.20285>. Record opened.
- Wu, Hilton (2024), Estimating the probabilities of rare outputs in language models.
  <https://arxiv.org/abs/2410.13211>. Record opened.
- Jones et al. (2025), Forecasting rare language model behaviors. <https://arxiv.org/abs/2502.16797>. Record opened.
- Nazeri, Schmuck, Soudjani, Abate (2026), Sound probabilistic safety bounds for large language models.
  <https://arxiv.org/abs/2607.20286>. Record opened.
- Kaur (2026), What AI red-team evaluations can and cannot prove. <https://arxiv.org/abs/2607.21735>. Record opened;
  statement read: Definition 1 and §4.
- Wang et al. (2025), How catastrophic is your LLM? Certifying risk in conversation. <https://arxiv.org/abs/2510.03969>.
  Record opened.
- Levy, Perl (2026), Bounding the black box: a statistical certification framework for AI risk regulation.
  <https://arxiv.org/abs/2604.21854>. Record opened.
- Singh (2026), Limits of statistical assurance for embodied and agentic AI under adaptive adversaries.
  <https://arxiv.org/abs/2610.18948>. Record opened; statement read: Theorem 1.
- Wallach et al. (2024), Evaluating generative AI systems is a social science measurement challenge.
  <https://arxiv.org/abs/2411.10939>. Record opened.
- Chouldechova et al. (2024), A shared standard for valid measurement of generative AI systems' capabilities, risks, and
  impacts. <https://arxiv.org/abs/2412.01934>. Record opened.
- Bean et al. (2025), Measuring what matters: construct validity in large language model benchmarks.
  <https://arxiv.org/abs/2511.04703>. Record opened.
- Miller (2024), Adding error bars to evals. <https://arxiv.org/abs/2411.00640>. Record opened.

**Constraints and optimization**
- Khalifa, Elsahar, Dymetman (2020), A distributional approach to controlled text generation.
  <https://arxiv.org/abs/2012.11635>. Record opened; statement read: Theorem 1 and §2.1.
- Go et al. (2023), Aligning language models with preferences through f-divergence minimization.
  <https://arxiv.org/abs/2302.08215>. Record opened.
- Wang, Jiang, Yang, Liu, Chen (2023), Beyond reverse KL: generalizing DPO with diverse divergence constraints.
  <https://arxiv.org/abs/2309.16240>. Record opened.
- Paternain, Chamon, Calvo-Fullana, Ribeiro (2019), Constrained reinforcement learning has zero duality gap.
  <https://arxiv.org/abs/1910.13393>. Record opened; statement read: the perturbation function and the setting of
  Theorem 1.
- Achiam, Held, Tamar, Abbeel (2017), Constrained policy optimization. <https://arxiv.org/abs/1705.10528>. Record
  opened.
- Dai et al. (2023), Safe RLHF. <https://arxiv.org/abs/2310.12773>. Record opened.
- Huang et al. (2024), One-shot safety alignment for large language models via optimal dualization.
  <https://arxiv.org/abs/2405.19544>. Record opened; statement read: Assumption 1, Lemmas 1–2, Theorem 1.

**Definitions of alignment and misalignment**
- Wolf, Wies, Avnery, Levine, Shashua (2023), Fundamental limitations of alignment in large language models.
  <https://arxiv.org/abs/2304.11082>. Record opened; statement read: Definitions 1–2, Theorem 1.
- Skalse, Howe, Krasheninnikov, Krueger (2022), Defining and characterizing reward hacking.
  <https://arxiv.org/abs/2209.13085>. Record opened; statement read: Definitions 1–2, Theorem 1.
- Karwowski et al. (2023), Goodhart's law in reinforcement learning. <https://arxiv.org/abs/2310.09144>. Record opened.
- Langosco et al. (2021), Goal misgeneralization in deep reinforcement learning. <https://arxiv.org/abs/2105.14111>.
  Record opened; statement read: Definition 2.1 with equations (1)–(2).
- Shah et al. (2022), Goal misgeneralization: why correct specifications aren't enough for correct goals.
  <https://arxiv.org/abs/2210.01790>. Record opened.
- Orseau, McGill, Legg (2018), Agents and devices: a relative definition of agency. <https://arxiv.org/abs/1805.12387>.
  Record opened.
- Suleymanov (2026), A revealed preference framework for AI alignment. <https://arxiv.org/abs/2603.27868>. Record
  opened; statement read: Definition 1, Theorem 1.
- Kierans, Ghosh, Hazan, Dori-Hacohen (2024), Quantifying misalignment between agents.
  <https://arxiv.org/abs/2406.04231>. Record opened; statement read: §3.4, equation (3).
- Guarino, Ziegler (2025), Capturing misalignment. <https://arxiv.org/abs/2506.17176>. Record opened.
- Gabriel (2020), Artificial intelligence, values and alignment. <https://arxiv.org/abs/2001.09768>. Record opened.
- LaCroix (2026), Relative principals, pluralistic alignment, and the structural value alignment problem.
  <https://arxiv.org/abs/2604.20805>. Record opened.
- van Lier et al. (2026), Acceptable misalignment. <https://arxiv.org/abs/2610.16881>. Record opened.
- Critch, Krueger (2020), AI research considerations for human existential safety (ARCHES).
  <https://arxiv.org/abs/2006.04948>. Record opened.
- Spizzirri (2025), The specification trap. <https://arxiv.org/abs/2512.03048>. Record opened.
- Ngo, Chan, Mindermann (2022), The alignment problem from a deep learning perspective.
  <https://arxiv.org/abs/2209.00626>. Record opened (background).
- Ji et al. (2023), AI alignment: a comprehensive survey. <https://arxiv.org/abs/2310.19852>. Record opened
  (background).
- Hendrycks, Carlini, Schulman, Steinhardt (2021), Unsolved problems in ML safety. <https://arxiv.org/abs/2109.13916>.
  Record opened (background).

**Causality, agency, responsibility, harm**
- Everitt, Carey, Langlois, Ortega, Legg (2021), Agent incentives: a causal perspective.
  <https://arxiv.org/abs/2102.01685>. Record opened; statement read: Definition 17, Theorem 18.
- Kenton et al. (2022), Discovering agents. <https://arxiv.org/abs/2208.08345>. Record opened.
- Ward, Belardinelli, Toni, Everitt (2023), Honesty is the best policy: defining and mitigating AI deception.
  <https://arxiv.org/abs/2312.01350>. Record opened.
- Chockler, Halpern (2003), Responsibility and blame: a structural-model approach. <https://arxiv.org/abs/cs/0312038>.
  Record opened.
- Halpern, Kleiman-Weiner (2018), Towards formal definitions of blameworthiness, intention, and moral responsibility.
  <https://arxiv.org/abs/1810.05903>. Record opened; statement read: Definitions 3.1–3.2.
- Richens, Beard, Thompson (2022), Counterfactual harm. <https://arxiv.org/abs/2204.12993>. Record opened; statement
  read: Definition 3.
- Beckers, Chockler, Halpern (2022), A causal analysis of harm. <https://arxiv.org/abs/2210.05327>. Record opened.
- Beckers, Chockler, Halpern (2022), Quantifying harm. <https://arxiv.org/abs/2209.15111>. Record opened.
- Turner, Hadfield-Menell, Tadepalli (2019), Conservative agency via attainable utility preservation.
  <https://arxiv.org/abs/1902.09725>. Record opened; statement read: the AUP reward, equation (3).
- Krakovna, Orseau, Kumar, Martic, Legg (2018), Penalizing side effects using stepwise relative reachability.
  <https://arxiv.org/abs/1806.01186>. Record opened.
- Turner, Smith, Shah, Critch, Tadepalli (2019), Optimal policies tend to seek power.
  <https://arxiv.org/abs/1912.01683>. Record opened.
- Hadfield-Menell, Dragan, Abbeel, Russell (2016), The off-switch game. <https://arxiv.org/abs/1611.08219>. Record
  opened.
- Carey, Everitt (2023), Human control: definitions and algorithms. <https://arxiv.org/abs/2305.19861>. Record opened.
- Nayebi (2025), Core safety values for provably corrigible agents. <https://arxiv.org/abs/2507.20964>. Record opened.
- Demski, Garrabrant (2019), Embedded agency. <https://arxiv.org/abs/1902.09469>. Record opened.

**Oversight, control, assurance**
- Irving, Christiano, Amodei (2018), AI safety via debate. <https://arxiv.org/abs/1805.00899>. Record opened.
- Brown-Cohen, Irving, Piliouras (2023), Scalable AI safety via doubly-efficient debate.
  <https://arxiv.org/abs/2311.14125>. Record opened.
- Brown-Cohen, Irving, Piliouras, Chen, Li, Xun (2025), Avoiding obfuscation with prover-estimator debate.
  <https://arxiv.org/abs/2506.13609>. Record opened.
- Brown-Cohen, Irving, Marshall, Newman, Piliouras, Szegedy (2026), Debate is efficient with your time.
  <https://arxiv.org/abs/2602.08630>. Record opened.
- Greenblatt, Shlegeris, Sachan, Roger (2023), AI control: improving safety despite intentional subversion.
  <https://arxiv.org/abs/2312.06942>. Record opened.
- Griffin, Thomson, Shlegeris, Abate (2024), Games for AI control. <https://arxiv.org/abs/2409.07985>. Record opened.
- Korbak, Clymer, Hilton, Shlegeris, Irving (2025), A sketch of an AI control safety case.
  <https://arxiv.org/abs/2501.17315>. Record opened.
- Clymer, Gabrieli, Krueger, Larsen (2024), Safety cases: how to justify the safety of advanced AI systems.
  <https://arxiv.org/abs/2403.10462>. Record opened.
- Buhl, Sett, Koessler, Schuett, Anderljung (2024), Safety cases for frontier AI. <https://arxiv.org/abs/2410.21572>.
  Record opened.
- Goemans et al. (2024), Safety case template for frontier AI: a cyber inability argument.
  <https://arxiv.org/abs/2411.08088>. Record opened.
- Balesni et al. (2024), Towards evaluations-based safety cases for AI scheming. <https://arxiv.org/abs/2411.03336>.
  Record opened.
- Buhl, Pfau, Hilton, Irving (2025), An alignment safety case sketch based on debate.
  <https://arxiv.org/abs/2505.03989>. Record opened.
- Souly, Kirk, Merizian, D'Cruz, Davies (2026), UK AISI alignment evaluation case-study.
  <https://arxiv.org/abs/2604.00788>. Record opened.
- Mylius (2025), Systematic hazard analysis for frontier AI using STPA. <https://arxiv.org/abs/2506.01782>. Record
  opened.
- Carlucci, Fillingham, Walpole, Kryś (2026), Exploring systems-thinking approaches to loss of control risk.
  <https://arxiv.org/abs/2606.13474>. Record opened.
- Dalrymple et al. (2024), Towards guaranteed safe AI. <https://arxiv.org/abs/2405.06624>. Record opened.
- Seshia, Sadigh, Sastry (2016), Towards verified artificial intelligence. <https://arxiv.org/abs/1606.08514>. Record
  opened.
- Bengio et al. (2024), Can a Bayesian oracle prevent harm from an agent? <https://arxiv.org/abs/2408.05284>. Record
  opened.

**Risk, severity, aggregation**
- Slattery et al. (2024), The AI risk repository. <https://arxiv.org/abs/2408.12622>. Record opened.
- Zeng et al. (2024), AI risk categorization decoded (AIR 2024). <https://arxiv.org/abs/2406.17864>. Record opened.
- Koessler, Schuett, Anderljung (2024), Risk thresholds for frontier AI. <https://arxiv.org/abs/2406.14713>. Record
  opened.
- Vei, Giudici, Sermpezis, Vakali, Bernardelli (2025), AI Harmonics. <https://arxiv.org/abs/2509.10104>. Record opened.
- Conitzer et al. (2024), Social choice should guide AI alignment in dealing with diverse human feedback.
  <https://arxiv.org/abs/2404.10271>. Record opened.
- Ge et al. (2024), Axioms for AI alignment from human feedback. <https://arxiv.org/abs/2405.14758>. Record opened.
- Siththaranjan, Laidlaw, Hadfield-Menell (2023), Distributional preference learning.
  <https://arxiv.org/abs/2312.08358>. Record opened; the Borda count result located in §3 (statement not read in full).
- Dai, Fleisig (2024), Mapping social choice theory to RLHF. <https://arxiv.org/abs/2404.13038>. Record opened.
- Halpern, Micha, Procaccia, Schiffer, Shapira, Zhang (2026), AI alignment from social choice perspectives.
  <https://arxiv.org/abs/2606.21550>. Record opened.
- Sorensen et al. (2024), A roadmap to pluralistic alignment. <https://arxiv.org/abs/2402.05070>. Record opened;
  statement read: §3.3.

**Training**
- Shapira, Benade, Procaccia (2026), How RLHF amplifies sycophancy. <https://arxiv.org/abs/2602.01002>. Record opened;
  statement read: Theorems 1 and 6.
- Betley et al. (2025), Emergent misalignment. <https://arxiv.org/abs/2502.17424>. Record opened.
- MacDiarmid et al. (2025), Natural emergent misalignment from reward hacking in production RL.
  <https://arxiv.org/abs/2511.18397>. Record opened.
- Wang et al. (2025), Persona features control emergent misalignment. <https://arxiv.org/abs/2506.19823>. Record opened.
- Soligo, Turner, Rajamanoharan, Nanda (2026), Emergent misalignment is easy, narrow misalignment is hard.
  <https://arxiv.org/abs/2602.07852>. Record opened.
- Zhang, Weckauff, Garcia-Olano, Andriushchenko (2026), What shapes emergent misalignment?
  <https://arxiv.org/abs/2606.20814>. Record opened.
- Qi et al. (2023), Fine-tuning aligned language models compromises safety, even when users do not intend to!
  <https://arxiv.org/abs/2310.03693>. Record opened.
- Qi et al. (2024), Safety alignment should be made more than just a few tokens deep.
  <https://arxiv.org/abs/2406.05946>. Record opened.
- Sharma et al. (2023), Towards understanding sycophancy in language models. <https://arxiv.org/abs/2310.13548>. Record
  opened.
- Hubinger et al. (2024), Sleeper agents. <https://arxiv.org/abs/2401.05566>. Record opened.
- Naik et al. (2025), AgentMisalignment. <https://arxiv.org/abs/2506.04018>. Record opened.
- Agarwal, Lin, Braverman, Hazan (2026), AI alignment via incentives and correction. <https://arxiv.org/abs/2605.01643>.
  Record opened.

**To verify (from memory, or cited inside a source and not opened)**
- Altman, *Constrained Markov Decision Processes* (1999). *(to verify)*
- Csiszár and Shields (2004), *Information Theory and Statistics: A Tutorial*, the source of GDC's Theorem 1. *(to
  verify)*
- Li (1999), PhD thesis on mixture density estimation and the reverse information projection, cited by Larsson et al.
  *(to verify)*
- Hanley and Lippman-Hand (1983), the zero-numerator bound, cited by Kaur. *(to verify)*
- Adcock and Collier (2001), measurement validity, cited by Chouldechova et al. *(to verify)*
- Soares, Fallenstein, Yudkowsky, Armstrong (2015), Corrigibility. *(to verify)*
- Thornley, The shutdown problem (2024). *(to verify)*
- Leveson and Thomas, *STPA Handbook* (2018). *(to verify)*
- The `KL_inf` closed form for Bernoulli and bounded means in the bandit literature (Honda and Takemura). *(to verify)*
- Owen, empirical likelihood, the dual form of VK3. *(to verify; `constraints.md` already marks it as not read)*

**Hosts the PI could allow** (not fetched): `proceedings.mlr.press` (the ICML versions of Shapira et al. and Chen et
al.); `openreview.net`; `intelligence.org` (Soares et al.); `airisk.mit.edu` (the AI risk repository's database);
`psas.scripts.mit.edu` or `mitpress.mit.edu` (Leveson's STPA material); `link.springer.com` (Thornley).

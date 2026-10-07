# NOTES — the executor's working notes

Not part of the core, and not checked by lint. Blunt on purpose. A hunch is not a claim: nothing moves into `CORE.md` or
`derived/`
without a proof and a check. Names, and correspondences with the literature, with their confidence levels, live in
`TERMS.md`.

## 1. Failure modes

Every one of these was caught by a check or by someone else, not by re-reading: more checks, fewer re-reads. The first
part is v7.10's table (`70 Project/NOTES_claude.md` §1 in the tag), condensed: rows about objects the core dropped
(tiers, conventions, the vault) are left out or stated in general form. The second part is from building this core.

**From v7.10.**

| Failure mode | Evidence (v7.10) | Countermeasure |
|---|---|---|
| **Naming elegant things before checking the edge case** | row 50: `D_⊥` called "misalignment proper", though a sign flip gives 0 | check every new name and example against the definition, and against the sign and degenerate cases, before writing it down |
| **Bounding what has a closed form** | rows 31–35: five versions bounded a regret that equals a KL divergence | before bounding anything, ask whether there is an identity |
| **Stating a prediction in the form that sounds right** | row 51: "matched variances cross"; the limits say they tie | derive a prediction's conditions from the theorem's limits first |
| **Grading my own framework generously** | T1: my routing was the outlier (κ 0.04 against a blind rater) | assume my own coverage judgements are inflated; get a blind second rater for anything quoted |
| **Stating a result for the case it was found in, not for what its proof needs** | rows 67–68, 76, 77, 78: the same error five times, results filed under a narrower actor class than their proofs needed | read the quantifier in the proof: the hypothesis is the weakest one the proof uses |
| **Plain language that drops the qualifiers** | row 62: "cheap ⇒ hard to detect" lost "in nats" and the actor class | every plain sentence must survive the theorem's hypotheses |
| **A check that overstates its coverage** | Prop 14's note cited V8, which checked part (ii) only; part (i) was never checked | name the part a check covers |
| **Testing an asymptotic claim on a fixed grid** | R7-4: a fixed grid mixed asymptotic and pre-asymptotic instances, and naive arithmetic hit `10⁻¹⁵` | scale the test window to the instance, compute in log space, and say which regime is tested |
| **A property claimed from intent, not from a scan** | v7.0: "every table link is escaped"; the escaping function was never called, and 41 tables were malformed | a property is claimed only if a check enforces it |
| **Printing noise as a result** | V25, V33, F1, F3 printed round-off; the first CI run on another CPU failed on exactly those lines | assert the claim, print diagnostics apart, and run every check on a second SIMD path |
| **Generalizing a shape from one instance** | R7-2: "the cost of a wrong default rises, then vanishes", from one probe; 200 random instances showed a peak in 67 | a claim about the shape of a curve needs a random sample before it is said |
| **Snapshotting a derived field** | v7.0 froze each note's tier at migration, so editing the tier table would have left every note stale | derive every derivable field from the live source, never from a snapshot |
| **Allow-listing a cycle instead of fixing it** | v6.6 allow-listed a citation as "attribution only"; it closed a real cycle | a citation that is only attribution goes in Notes, not in a proof |
| **Measuring after the answer has converged** | three rounds of census routing | when a measurement stops changing what will be built, stop measuring |
| **A headline that claims more than the scope** | row 52: "a formalization of alignment" | put the scope in the headline |
| **Judging a dropped idea from its retraction line alone** | ROADMAP §6's first draft misfiled grounding from row 4; the source said otherwise | before restoring or judging a retracted idea, read its source |
| **Correcting the ledger, not the prose that repeats it** | the v7.3.3 review found prose three versions behind the ledger | a status change is a retraction for search purposes: search the old wording everywhere |
| **Calling a pattern derived when a definition builds it in** | Prop 27(c): "complies when rewarded … derived"; Def 16 built the switch in | before writing "derived", check whether the conclusion is already in a definition |
| **Internal refinement over external contact** | after R6 named diagnostics as underserved, the next five steps were refactors | after two internal steps, the next makes external contact, unless the PI says otherwise |
| **Registering what is already proved, or a threshold without a scale** | R8-1: a "new" identity was Thm 17(iii); R7-7, R7-9, R7-10, R8-2: tolerances below the solver's precision or the sum's rounding | search for the quantity first; derive every threshold from a stated scale; state existence claims as existence |
| **A pass rate as a reliability rule** | R7-7: starts agreed in 98.7% of instances; the failure that mattered was where they disagreed | reliability is per instance: flag each value |
| **A reference fitted from the data being judged** | I1-dyn: a Hardy–Weinberg reference from the same counts left the test nothing to reject | count the degrees of freedom the reference removes; use an independent reference |
| **A prediction the design makes unfalsifiable** | T7-1: a within-cell share on a two-cell space is 1 by construction | compute every registered share or ratio on the design's degenerate cases first |
| **A data column or a design parameter not checked before registering** | T7-1b: a column with 18 values; T7-2b: a test needing 3 bins below a default that left 2 | count non-missing values and read the design parameters before registering |
| **A mask that blacklists leaks** | I1-dyn2: masking digits missed OCR's look-alikes, and two values showed through | mask by whitelist |
| **Killing processes by pattern** | `pkill -f` matched its own shell, twice; and a third time while deriving the diagnostics (Q28), killing the edit it was chained with | stop processes by PID; nothing enforces it yet (`cases/README.md`, lessons as defaults) |

**From this core.**

| Failure mode | Evidence | Countermeasure |
|---|---|---|
| **A check that omits the constraint it tests** | the ray-minimizer check never required `t* ≥ 0`; a mutant that pursued `−F` passed | mutation-test every new check before recording it: break the mathematics on purpose and watch it fail |
| **A tolerance without its scale, again** | the ray-closedness check compared a tight bound with no rounding margin (1.79134602e-43 against itself) | every comparison gets the relative margin of `EXACT`, including the "obvious" ones |
| **A justification leaning on a later result** | D3 cited P5 while P5 came after it; lint rule R5 caught it | keep R5; write the "why" from what is above |
| **A check helper that misclassifies at the edge of float64** | at intensity 40, the coarse actor's mass off the best outcome (about `1e-34`) vanished from its mean of `F`; the helper took the "all mass on the best outcomes" case and returned `+∞`; again in W1's report, where the matched pursuit at an intensity near `10³` underflowed to zeros and the under-pursuit of 9 prompts read infinite; and in [[P50 — Tampering: a change of the measurement, not of the world\|P50]]'s check, whose small-intensity ratio of two divergences near `10⁻⁹`, each a sum that cancels to that size, erred by `10⁻⁷` at intensity `10⁻³` and by `2.5·10⁻⁵` at `10⁻⁴` | keep check instances where float64 represents every mass; test limits by their own formula; compute a divergence to a tilt in closed form, with `log E_q[e^{tF}]` by log-sum-exp |
| **A familiar formula that hides a typing error** | "the KL-regularized optimum is `tilt(π_ref, r/β)`" is true prompt by prompt, and false on prompt–response pairs: the pursuit ray of [[D2 — Pursuit of an objective\|D2]] would also reweight the prompts, which no policy can do. Found only when the ontologies had to say what an outcome is | typed slots in every ontology, including **contexts**; a formula from the literature enters only with its outcome space stated |
| **A probe bug read as a refutation** | the first probe of [[P15 — Misalignment splits into what the actor could avoid and what it could not\|P15]] for policies used `log E[e^V]` over the environment (the optimistic recursion of control as inference) and found the split off by 5 nats; the derivation said the projection averages over the environment, and with that the split was exact. The same slip, from the other side, in the grounding probe (Q32): the best grounded behaviour was first written with `log E_K[e^{t·F̂}|w]`, the trainer's optimum's own weights of worlds, where an actor that cannot touch the channel faces its average, `E_K[F̂|w]`; the numerical projection disagreed by `0.37`, and the derivation was redone | when a probe contradicts a derivation, check each against the other before concluding anything; what the actor cannot control enters by its average, not by its log-mean-exp; the slip is now a mutation in [[P50 — Tampering: a change of the measurement, not of the world\|P50]]'s check |
| **A rule test passing because another rule fired** | the lint tests for "numbers increase" and "a core Statement may not use a result" passed only because a duplicate id and a cycle fired too; both mutants survived | each rule test isolates its rule, or asserts its rule's own message; mutation-test the linter as well as the checks |
| **A degenerate random instance hiding the property** | the first check of [[P16 — An actor cannot behave more differently than it can tell conditions apart\|P16]](i) moved mass between two inputs, one of which had almost none, so the two conditions barely differed (KL 1e-5) | build the instance so the property has something to show (here KL > 0.3), and assert that it does |
| **A plain-terms twin that claims more than the statement** | [[P19 — A monotone regression rules out overoptimization\|P19]]'s plain terms listed threshold selection among the covered paths; a threshold leaves `Δ°`, so the statement does not cover it (the conclusion holds there by a direct argument). Found in the review before the v10 commit | read each "In plain terms" against the Statement's hypotheses, one named example at a time |
| **A rate copied from a sketch** | [[P22 — No test detects misalignment faster than misalignment\|P22]]'s Notes said the Chernoff bound is approached like `1/log(1/ε)`; a computation across seven decades of `ε` showed `log log(1/ε)/log(1/ε)` | a rate in a Note is computed across several decades before it is written |
| **A check whose instance generator kills the case it tests** | the first single-peaked regressions of [[P26 — The regression on bins governs at small intensity\|P26]]'s check capped the falling part at the peak, so every "falling" part was flat; a mutant claiming monotone curves survived until the counts were printed | assert that the hypothesis is visible in the instances (here: some curves do fall), as the failure mode on degenerate instances already asks |
| **A concept that is trivial in the typical case** | the regression of [[D10 — Evaluator, regression and residual\|D10]] is the target itself whenever the evaluator gives distinct outcomes distinct values, the usual case for reward models and fitness; noticed only when filling the ontologies' evaluator slots, after [[P18 — Through the evaluator, only the regression counts\|P18]]–[[P20 — Where overoptimization starts, and how it ends\|P20]] were proved and checked on instances built with ties | build check instances from the typical case as well as the interesting one, and fill one ontology before a new definition is final |
| **A result silent on its specification** | [[P24 — The evaluation gap\|P24]] said "the misalignment in deployment" without naming the specification on condition–outcome pairs; under one shared intensity its formula fails in 173 of 200 instances | every result over several conditions names the specification on pairs |
| **Lineage amnesia after a restart** | [[P13 — What the start of a change gains\|P13]](ii) re-derived v7.10's B §4 (the gold slope `√2·ρ·sd` per `√KL`) and Prop 14 without crediting them; found only in the retrospective after v9 | before adding a result, search v7.10 (`git grep -i <idea> v7.10`) for its counterpart, and cite it in the Lineage |
| **A data claim written from memory** | the industrial-organization ontology gave the German price archive the licence CC BY 4.0, the live feed's; by secondary sources the archive is CC BY-NC-SA 4.0, for non-commercial use. Found only when the PI asked which specification the public data can test | a Data paragraph says where each claim about licence and access comes from, and says so when the primary source was not reached |
| **An intervention dated with the quantity it tests** | the known result dates adoption partly by the speed of a station's response to its rival, a dependence between the stations; a test of coordination before and after those dates would have been partly true by construction. Caught before registration | before registering, list how every intervention or group is defined, and drop any marker that measures the outcome tested |
| **A threshold without its scale, in a registration** | case C2's verification required a recovery of `0.999` on a grid of step `0.05`, while a third of the peaks came before `t = 0.5`; and S1 scored the rule against the best of 32 noisy training runs, so its threshold measured luck. All three predictions failed; the exact pursuit on S1's own grid would have reached only 79% | before registering, compute every threshold on the design's noise-free case, with seeds the test will not use, and score against what the design can reach, not against the luckiest run |
| **A run lost at its last step** | W1's report computed 35 minutes of per-prompt results and crashed in its final aggregation, a bootstrap indexing all 1,000 prompts over a list of 994; nothing had been saved | save per-item results (outside the repository) before aggregating, and aggregate in a function that can be rerun on them |
| **A speed never measured** | W3's first launch was estimated at seconds per context and took about 50: the sampler recomputed every sequence at every token, and a second heavy job shared the processors. It was stopped before any context finished; a cached sampler in double precision, checked against the scorer, replaced it | before launching, time one context of the registered size on a made-up input, alone on the machine |
| **A registered statistic that the design's mixture inflates** | W3 pooled, within each prompt, 32 continuations of the reference and 32 of the tuned model, and registered the `R²` of the revealed objective on the reward over all 64. The two sets differ by 16.5 nats on the objective and also on the reward, so most of the registered `0.358` comes from that difference; within either model's own continuations it is `0.10` to `0.12`. The verdict (refuted) stands, but the registered number understates the refutation, and a model whose change were pure pursuit of something correlated with the reward across the two sets could have passed S1 | before registering a statistic on a sample that mixes sources, compute it on each source alone in the calibration, and register the one that answers the question |
| **A tie-breaking order charged as departure** | W1's report broke ties in the proxy's score by one fixed random order, as `run.py` does for the gold curve, where it changes nothing in expectation. A divergence is convex, so a fixed order adds itself to the departure and to misalignment: on a synthetic prompt with a tied block near the top, `KL` at `n = 16` was `1.84` instead of `1.40` nats. Caught on re-reading the report's declaration ("it scores nothing else alike", which was also false), halfway through the third computation | compute a divergence on the behaviour averaged over its tie-breaking, which by symmetry is uniform within each tie; check it against a simulation of the selector |
| **Saving the estimates, not the data behind them** | W4 saved, outside the repository, each context's estimates but not the per-draw log-probabilities and rewards, so an analysis needing no reweighting, how far one run's draws move along the other's revealed objective, needed a second run of 2.2 hours | save every per-draw value before aggregating; the template now asks for it |
| **A specification with no named principal** | W3 and W4 declared as the target the reward the policy was trained on, the evaluator itself, while the machine-learning ontology's specification asks for a gold objective distinct from it; the executor declared it, for no principal in particular. What they measured is misalignment against the trainer's formal objective, and their texts said "misalignment" without saying whose. Caught by the PI | name the principal in the declaration; when the target is uncertain, declare the family of targets and report the interval it gives (§7) |
| **An optimum taken from a solver's word** | the first check of [[P51 — What signals, audits and re-measurements reveal of tampering\|P51]](i) ran the EM iteration a fixed number of steps and compared its value with the bound: 20,000 steps left gaps near `3·10⁻⁸`, and 50,000 left `10⁻⁶` where the minimum is `0` with more worlds than signals | certify a computed optimum by a bound that holds at any point, here `log max_w c(w)`, and test claims against the bracket, not the point |
| **An abstract read as the theorem** | the import survey (§9) read McAllester and Stratos from their abstract, as a limit of `log N` on what samples certify about information, and inferred what it says of misalignment; their Theorem 3.1 holds with one behaviour known and the other sampled, a lower bound on `KL(known‖sampled)`, which is the reverse of misalignment's sampling. Caught on reading the text, once arXiv was reachable (Q34) | quote a theorem's hypotheses, not its abstract, before inferring from it; D12's rule, applied to readings as well as to imports |

**One that worked.** "Misalignment of a coarse actor grows with effort" was the natural claim from v7.10's B1 ("rises
with budget"). A 400-instance probe before writing it found 123 non-monotone cases, so [[P8 — An actor that cannot tell outcomes apart|P8]] claims only the small-effort
law and exhibits a counterexample. The rule "a shape claim needs a random sample before it is said" (v7.10, §1) paid
off.

**Another.** In draft 2's tests of the general core (`probes/general/`), T5 found the compromise of three principals
meeting each principal's floor exactly, and that read like a law ("a committee delivers each member's minimum"). A
20-instance test registered before running it found it in 11 of 20 instances, against a predicted 15, so it is recorded
as failed, and draft 2 says "often, not always".

**Two from the second batch.** B5 registered a prediction at intensity 2 for a default whose pursuit stops at 1: the
object did not exist there. Countermeasure: compute the domain (`t_max`) of every registered quantity before
registering. And the first run of a diagnosis of B3 contradicted B3 itself; checking the probe first, as the failure
mode "a probe bug read as a refutation" says, found an operator-precedence bug (`pa * (rho / z) @ K`).

**One that worked, in a case.** Before the industrial-organization prediction met German prices, case C1 tested its
instrument in simulation, where the truth is known (`cases/c1-collusion-simulation/`). Coordination over episodes did
not separate algorithms that learned to collude from players that only adapt (S1 failed, `p = 0.019`), and, outside the
registration, not from learning algorithms that barely collude either. The prediction was revised before any data were
read. Countermeasure, now a habit: test an instrument where the truth is known before spending data on it.

**One that worked, before a registration.** W1's procedure was first run on synthetic prompts, as the C2 lesson asks:
without noise it recovered the slope to 0.7%, with noise it held 6 times in 6 with intervals of about ±0.02, and in a
world whose gold falls at the top it was refuted. An earlier run on 200 prompts had shown a 17% gap that looked like a
flaw of the prediction; it was sampling noise, and the noise-free case showed it. The registration could then say what
a refutation would mean. After the verdict, the executor's first explanation, the ties, was tested and failed (`D` moved
from `+0.060` to `+0.062`); the shape of the curve was the explanation.

**One that worked, in a rehearsal.** W4's rehearsal (`cases/w4-two-runs/rehearsal.json`), run before its registration as
design rule 4 asks, failed on a degenerate case the real data could produce: a named objective with extreme values, the
other run's log-probability of a draw it would almost never make, made Newton's method overflow. Named objectives are
now scaled before matching. The same rehearsal measured each estimator's bias on synthetic runs at the real departures,
and the registration's two thresholds are that bias plus two standard errors, not round numbers; it also showed that one
of the two tests is the weaker, which the registration says.

**Two from the consolidation.** The first check of [[P41 — Reversibility: the Jensen–Shannon divergence from the reversal|P41]](iv) drew some 2-state chains, which are always reversible; its
assertion that the target is visible (the countermeasure of the degenerate-instance row) fired, so the check could not
pass vacuously. Instances now have 3 to 5 states. And the first check of [[P41 — Reversibility: the Jensen–Shannon divergence from the reversal|P41]](iii)'s quarter law used an asymmetry of
`10⁻³`, scaled by the smallest stationary weight: the divergences were near `10⁻¹¹`, rounding outweighed the `h²`
correction, and the asymmetry was tiny almost everywhere. The fix came from the expansion of the ratio,
`1/4·(1 − h²·S4/(6·S2))`: normalize the asymmetry by its largest relative size and choose `h` so that the `h²` term
dominates rounding. A tolerance without its scale, a third time.

## 2. Is the core a compelling standard yet?

Closer, not yet. v9 applied the PI's decisions: the core held five premises and nine definitions; every result is
derived; the cost of departing from the default is derived ([[P14 — The cost of departing from the default is forced|P14]]), not assumed; feasibility separates "cannot" from
"will not" ([[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]]); conditions, views and identification make deceptive alignment a measurable quantity ([[P16 — An actor cannot behave more differently than it can tell conditions apart|P16]],
[[P17 — What an unobserved condition can hide|P17]]); and a reporting standard names every definition (`STANDARD.md`, lint R11).

v10 added the two concepts approved after the retrospective (§5): the evaluator ([[D10 — Evaluator, regression and residual|D10]]), from which the Goodhart results
of v7.10 are derived ([[P18 — Through the evaluator, only the regression counts|P18]]–[[P20 — Where overoptimization starts, and how it ends|P20]]), and sampling ([[D11 — Sample and evidence|D11]]), which gives misalignment its second meaning as a rate of
evidence and brings detection, estimation and the evaluation gap ([[P21 — The expected evidence is misalignment|P21]]–[[P24 — The evaluation gap|P24]]). The core holds five premises and eleven
definitions. Since then the import of v7.10 added [[P27 — The best use of a departure budget|P27]]–[[P38 — Any convex cost|P38]], [[L1 — Separable bounds are loose when two quantities change rank|L1]] and the forbidden statements ([[C1 — No ranking of errors holds at every budget|C1]]–[[C12 — No misalignment, no stakes|C12]]).

v11 widened the scope to groups and several principals with declared weights ([[P39 — Several actors: coordination plus individual misalignment|P39]]–[[P42 — Several principals: gridlock, and the pooled pursuit|P42]]), and the framework met
data for the first time: W1 tested the machine-learning prediction from [[P13 — What the start of a change gains|P13]] on answers no one had scored, and
refuted it (`cases/w1-best-of-n-slope/`); W3 tested the bet itself, on a public model tuned by PPO, and it held in
part: the model pursues its reward in the reward's own scale, but most of what the tuning changed is not that pursuit
(`cases/w3-ppo-pursuit/`). One of three predictions held. The finish line's prediction row is met; the row for a worked
case run by an outside reader is not: W1 is reported to `STANDARD.md`, and outside reviews wait (Q27). Where the
framework stands, and what comes next, is kept in `ROADMAP.md`; this table keeps the gaps the core has closed.

| Gap | State |
|---|---|
| sensitivity, resolution, stakes, the gain of a change | closed in v8: [[P7 — Indifference forgives exactly what happens inside cells\|P7]]–[[P10 — Sensitivity to the specification\|P10]], [[P13 — What the start of a change gains\|P13]] |
| the KL cost was assumed | **closed by [[P14 — The cost of departing from the default is forced\|P14]]**: forced by [[A2 — Pursuit is the steepest climb\|A2]] and [[A3 — Pursuit is the best trade-off\|A3]] together |
| "cannot" versus "will not" | **closed by [[P15 — Misalignment splits into what the actor could avoid and what it could not\|P15]]** for linear and convex limits; for capacity limits only a lower bound |
| contexts (v8 design question Q1) | **closed by [[P15 — Misalignment splits into what the actor could avoid and what it could not\|P15]]**: the shared intensity across contexts is derived, not chosen |
| deceptive alignment | **opened as a measurable quantity**: [[D8 — Conditions, responses and views\|D8]], [[D9 — Observation and identification\|D9]], [[P16 — An actor cannot behave more differently than it can tell conditions apart\|P16]], [[P17 — What an unobserved condition can hide\|P17]]; bounds on the objective's average in an unobserved condition, sharp given `ε` |
| a standard for reports | **closed by `STANDARD.md`** (lint R11) |
| no estimation layer | **closed in part by [[P23 — The estimated misalignment of an actor that pursues the objective\|P23]]**: the estimated misalignment under the standard specification, at a positive intensity; the boundary `t* = 0` and confidence sets for the other quantities are open |
| no theory of what optimizing a proxy does | **opened by [[D10 — Evaluator, regression and residual\|D10]]**: [[P18 — Through the evaluator, only the regression counts\|P18]] (only the regression counts), [[P19 — A monotone regression rules out overoptimization\|P19]] (a monotone regression rules out overoptimization), [[P20 — Where overoptimization starts, and how it ends\|P20]] (where it starts, how it ends) |
| detection, and the gap between evaluation and use | **closed by [[P22 — No test detects misalignment faster than misalignment\|P22]] and [[P24 — The evaluation gap\|P24]]** |
| the regression of a real-valued evaluator | **closed in part by [[P26 — The regression on bins governs at small intensity\|P26]]**: on finitely many outcomes it is the target itself; the regression on bins governs the pursuit up to `t·w·D/4`. Best-of-`n` with bins is open (E8) |
| the shape of the overoptimization curve | **closed by [[P25 — The target's curve turns no more often than the regression\|P25]]**: the target's curve turns no more often than the regression; a single-peaked regression gives at most one fall, for pursuit and best-of-`n` |
| several actors, several principals | **in scope since v11**: a group as one actor ([[P39 — Several actors: coordination plus individual misalignment\|P39]]), several principals with declared weights ([[P42 — Several principals: gridlock, and the pooled pursuit\|P42]]) |
| worked cases | **opened**: W1 and W3 on unseen data (one prediction held of three), W1 reported to `STANDARD.md`; C1 and C2 in simulation (`cases/`); no outside reader yet |

**Deferred from identifiability.** The "dynamic rank" generalizes [[P3 — A fixed objective is visible in the changes of behaviour|P3]] beyond rank one. No ontology needed it.

## 3. Open requests and recommendations

Everything waiting on the PI or deferred by agreement, in one place.

### 3.1 Decisions taken (v9–v11)

| # | Decision | By | Applied as |
|---|---|---|---|
| Q1 | contexts: one shared intensity or a free one per context | derived, not decided | [[P15 — Misalignment splits into what the actor could avoid and what it could not\|P15]](v) and its Notes |
| Q2 | no merging for its own sake; the core holds what cannot be derived and the universal definitions; derivations in their own folder | PI | `CORE.md`, `derived/`, lint R1 and R5 |
| Q3 | C1 (the cost is forced), C4 (feasibility), C9 (a standard), the scope, premises as items, ontologies in folders | PI | [[P14 — The cost of departing from the default is forced\|P14]]; [[D7 — Feasibility\|D7]], [[P15 — Misalignment splits into what the actor could avoid and what it could not\|P15]]; `STANDARD.md`; `CORE.md` §0; A1–A5; `ontologies/<name>/` |
| Q4 | identifiability into the core, so that deceptive alignment can be measured; interventions and stakes stay in the core | PI | [[D8 — Conditions, responses and views\|D8]], [[D9 — Observation and identification\|D9]], [[P16 — An actor cannot behave more differently than it can tell conditions apart\|P16]], [[P17 — What an unobserved condition can hide\|P17]]; [[D5 — Stakes\|D5]], [[D6 — Intervention and pass-through\|D6]] |
| Q5 | C2 and C3 (merge P11 with P13; move the Price equation into P2) | PI: declined, merging only to have fewer items | not applied |
| Q6 | the evaluator as the one strong concept to import, with the residual `R = F − E_q[F \| F̂]` as the canonical error | PI: approved | [[D10 — Evaluator, regression and residual\|D10]]; [[P18 — Through the evaluator, only the regression counts\|P18]]–[[P20 — Where overoptimization starts, and how it ends\|P20]] |
| Q7 | sampling in the core | PI: inclined to yes, as a universal act of measurement that the framework must interpret and can use for explanations; executor: yes, as definitions only (§5.6); PI: approved | [[D11 — Sample and evidence\|D11]]; [[P21 — The expected evidence is misalignment\|P21]]–[[P24 — The evaluation gap\|P24]] |
| Q8 | a file on related theories | PI | `RELATED.md`, lint R12 |
| Q9 | derived results whose proof is a classical theorem | PI: approved, with a light simulation unless a discrepancy shows | [[P22 — No test detects misalignment faster than misalignment\|P22]] (Chernoff), [[P23 — The estimated misalignment of an actor that pursues the objective\|P23]] (Wilks): the theorem quoted with its hypotheses, and a check |
| Q10 | [[P25 — The target's curve turns no more often than the regression\|P25]] (shape law, by Laguerre's rule of signs) and [[P26 — The regression on bins governs at small intensity\|P26]] (binned evaluators, E8) | executor, in a turn the PI left free; PI: worth merging | `derived/evaluator.md`; checks mutation-tested (eight mutants, all caught after two check fixes) |
| Q11 | v7.10's bounds on `F̂ − F` stated for known evaluators only, with the error as notation | PI: approved | `IMPORT.md` §2 |
| Q12 | v7.10's capacity imported as a feasible set, the **departure budget** | PI: approved | [[P27 — The best use of a departure budget\|P27]], [[P28 — The width of a departure budget\|P28]] |
| Q13 | the import plan of `IMPORT.md`, every recommendation, and its roadmap | PI: approved | `IMPORT.md` §6; phase R1 done |
| Q14 | `derived/feasibility.md` moved after `identifiability.md` in the reading order, since [[P27 — The best use of a departure budget\|P27]] uses [[P9 — What is at stake\|P9]] and [[P13 — What the start of a change gains\|P13]] and no earlier file cites [[P15 — Misalignment splits into what the actor could avoid and what it could not\|P15]] | executor, caught by lint R5 | `derived/README.md` |
| Q15 | v7.10's Thm 5 imported at an equal budget only, with the loss as the shortfall of [[D5 — Stakes\|D5]]; its part at a declared price dropped with the price convention. Lemma 8 kept as a lemma ([[L1 — Separable bounds are loose when two quantities change rank\|L1]]), since it is about bounds, not about alignment | executor, under Q13 | [[P29 — The width is the exact worst case\|P29]], [[L1 — Separable bounds are loose when two quantities change rank\|L1]], [[P30 — No separable bound on the worst case\|P30]] |
| Q16 | v7.10's Prop 11 imported in its form on finite outcomes ([[P31 — Budgets of other shapes\|P31]](vi)): a KL budget reaches a rare outcome at a cost `log(1/r)`, a `χ²` budget at `1/r − 1`; the statement on a continuum stays out of scope | executor, under Q13 | [[P31 — Budgets of other shapes\|P31]] |
| Q17 | `derived/forbids.md` as corollaries C1–C12: v7.10's §11.1–8 kept, §11.9 (price convention) dropped, four statements added from the core's own results; v7.10's Prop 4 imported there as [[C3 — An error confined to one region costs bounded nats\|C3]] instead of in N7 | executor, under Q13 | `derived/forbids.md` |
| Q18 | R5 imported as [[P33 — Error bounds for a known evaluator\|P33]]–[[P36 — Ordinal objectives\|P36]]: v7.10's error bounds as bounds on misalignment (not on regret at a price); floors and caps, and the ordinal specification, as specifications of [[D3 — Specification, declaration and misalignment\|D3]], with v7.10's budget and contract parts dropped | executor, under Q13 | `derived/evaluator.md`, `derived/misalignment.md` |
| Q19 | R6 imported as [[P37 — A strong incentive masks the actor, and can fake alignment\|P37]] and [[P38 — Any convex cost\|P38]]: v7.10's incentive results from the pass-through of [[D6 — Intervention and pass-through\|D6]] alone, without its reward coupling (which stays out of scope); v7.10's Bregman identity as a result about actors with other costs, the measure staying KL | executor, under Q13 | `derived/estimation.md`, `derived/value.md` |
| Q20 | the compatibility review of every imported item, asked by the PI: all compatible and kept; [[P29 — The width is the exact worst case\|P29]], [[P33 — Error bounds for a known evaluator\|P33]], [[P34 — Choosing by the evaluator from a common candidate set\|P34]], [[P37 — A strong incentive masks the actor, and can fake alignment\|P37]] changed (a supremum, an overclaim on the upper tail withdrawn, the selection bound strengthened to an attained worst case, the pass-through written as in [[D6 — Intervention and pass-through\|D6]]); [[P32 — Regulation costs departure\|P32]] and [[P38 — Any convex cost\|P38]] flagged as the first candidates to drop | PI asked; executor | `IMPORT.md` §7 |
| Q21 | the rest of v7.10, after the analysis of the archive: keep its record, not its files. An item survives only if it constrains what the core does now, for a reason stated in the framework's own goals; a result about the world that bears on a surviving claim is never dropped. Adopted: `RECORD.md` (lint R13), the rules of evidence (a)–(f), the finish line, the version rule, a generated Obsidian view. Dropped: the standing decisions that duplicate the scope or concern another project, the toy-example debt, T8, the dropped-ideas backlog, the retraction table as a file (`IMPORT.md` §5) | PI approved | `IMPORT.md` §5–§6, `README.md`, `RECORD.md` |
| Q22 | the disciplines: an ontology needs a principal and an actor, behaviour reported in numbers, data that can be read, and to be inside the scope (`ontologies/README.md`). Kept: machine learning. Renamed: humans to behavioural economics, biology to evolutionary biology. Reworked: institutions to medical sciences, with the four-hour target as a second known result. Dropped: job delegation, which had no numbers; its prediction is withdrawn untested (`RECORD.md`). Declined: ethics and philosophy, normative sciences, game theory, network science, complexity theory, with reasons. Every ontology now states its data, checked by lint R10 | PI asked; executor | `ontologies/` |
| Q23 | outcomes that are not finite: a separate draft, `CORE-GENERAL.md`, built as the core was, by canonicity, with a plain-terms twin for every item and a reading in the four disciplines. The framework commits to no topology on outcomes: the principal and the actor supply one where it matters. Executor: three tests (reduction, invariance, finite determination) and one new premise, GA6 | PI (route and topology); executor (the tests, GA6) | `CORE-GENERAL.md`, from draft 1; open decisions now in its §12 |
| Q24 | consolidation. The finite and the general parts are kept apart, in definitions and in results: `CORE.md` with `derived/` (v10, claims what it proves) and `CORE-GENERAL.md` with `general/` (draft 3, claims nothing). The results of draft 2 that hold on finite outcomes became [[P39 — Several actors: coordination plus individual misalignment\|P39]]–[[P42 — Several principals: gridlock, and the pooled pursuit\|P42]] in `derived/structure.md`, proved and checked. Scope revised (`CORE.md` §0): in, a group as one actor on joint outcomes, several principals with declared weights, rules as conditions, an episode as one outcome; out, why a group behaves as it does, choosing the weights, outcomes that are not finite, one long record of dependent decisions. Ontologies: condition 4 revised, and two added, industrial organization and experimental economics, each with a prediction (`RECORD.md`). The executor kept v10, since the scope is not the Statement of a premise or a definition; the PI overruled it (Q25) | PI (consolidate, keep the two parts apart, more disciplines, revisit the scope); executor (how to separate, which disciplines, the scope's wording) | `CORE.md` §0, `derived/structure.md`, `general/`, `ontologies/`, `RECORD.md` |
| Q25 | a new version, v11, for Q24's change of scope: the version rule now counts the scope, and so does the finish line's stability criterion, which is not met again until three steps pass without a change. The specification of `ontologies/industrial-organization/` is the one that papers and public data can test: independent pursuit, within contexts, over declared episodes. The alternative, independence given the rival's past prices, fits the law better but needs a declared model of what each station observes, and is blind by construction to the known result's algorithms, which set prices from the last round's prices alone. Checking the data corrected the archive's licence and found that one of the known result's adoption markers measures a dependence between the stations; the prediction dates adoption without it | PI (a new version; the testable specification); executor (the stability criterion; which specification is testable) | `README.md` (versions, finish line), `ontologies/industrial-organization/`, `RECORD.md` |
| Q26 | a freeze, after the executor's review: the framework had grown in theory, scope and disciplines while none of its predictions met data not seen before. Frozen until one does: the general core at draft 3, new disciplines, and any widening of the scope. Work goes to tests registered before they are computed, judged by the executor (`cases/`), and to a worked scenario in three registers (`SCENARIO.md`) | PI | `CORE-GENERAL.md`, `general/`, `ontologies/README.md`, `cases/`, `SCENARIO.md` |
| Q27 | after W1: the freeze is kept, to build more confidence first, although Q26's condition is met; no external reviews yet; the W1 report may be written, without breaking any licence, and in doubt the safer way; consolidate; then design, choose public data for, and run one more test, on machine learning. Applied: the repository keeps no third-party data, weights, or item-by-item derivatives (README, working agreements); W1's proxy weights and per-prompt statistics were removed. They remain in two earlier commits (`f7a2665`, `899c721`); removing them from history needs a force-push, which waits for the PI. The test chosen: W3, whether a public PPO-tuned model is the pursuit of its reward, the framework's bet itself | PI; executor (the licence rule and its application; the choice of test) | `README.md`, `cases/w1-best-of-n-slope/`, `cases/w3-ppo-pursuit/`, `.gitignore` |
| Q28 | after the retrospective of W1 and W3 (§6): every recommendation approved, that is, the retrospective recorded, the five design rules for cases (`cases/README.md`), and a registered follow-up to W3. And: derive more tools from the core for targeted diagnostics, such as telling drift apart from feigned alignment, even though the failures were not in the mathematics. New results in `derived/` serve that, as diagnostics; the freeze otherwise stands (no change of scope, premise or definition) | PI | `cases/README.md`, `derived/`, `NOTES.md` §6 |
| Q29 | test W4; and how can future designs include the lessons by default? Applied: a lesson becomes a default only when a template asks for it, a tool does it, or a check refuses work without it. So: `cases/TEMPLATE.md`; lint R15, which holds every registration made after the design rules to the template; `tools/casekit.py`, the fixes of W1's and W3's failures as tested helpers; and a map in `cases/README.md` from each lesson to what holds it, including the one nothing holds yet. W4 is the first case under them, of a new kind, diagnostic | PI; executor (the mechanisms) | `cases/TEMPLATE.md`, `tools/lint.py`, `tools/casekit.py`, `cases/README.md`, `cases/w4-two-runs/` |
| Q30 | after the question "whose target?" (§7): approved. The interval of misalignment over a family of targets becomes a result, [[P48 — Misalignment when the target is uncertain\|P48]]; every declaration names its principal, and a declaration whose target is uncertain declares the family and registers the interval (`STANDARD.md`, the field Principal; `cases/TEMPLATE.md`; lint R15, from which W4 is exempt for that field only, having been registered before it) | PI; executor (the statement and its wiring) | `derived/diagnostics.md`, `STANDARD.md`, `cases/TEMPLATE.md`, `tools/lint.py` |
| Q31 | how does the framework now relate to outer and inner alignment, Goodhart and the archive's five gaps? Outer alignment needed a definition the tools now give. Applied: [[P49 — Outer and inner misalignment\|P49]], outer misalignment as a function of intensity, inner misalignment, and their exact split; the five gaps mapped in `IMPORT.md`, section 8, where grounding (reward tampering) is only partly covered. Next, by the PI's request: a brainstorm on grounding, its definition and its diagnosis | PI; executor (the statement) | `derived/diagnostics.md`, `IMPORT.md`, `RELATED.md`, `STANDARD.md` |
| Q32 | grounding: can the framework define wireheading and diagnose it? Approved: [[P50 — Tampering: a change of the measurement, not of the world\|P50]], tampering as a divergence from a declared honest channel, with no new definition, and [[P51 — What signals, audits and re-measurements reveal of tampering\|P51]], what signals, audits and re-measurements reveal of it; a simulation case before any world case. With it, the two tests of framework predictions pending since W1, [[P41 — Reversibility: the Jensen–Shannon divergence from the reversal\|P41]]'s Rock–Paper–Scissors arm and [[P20 — Where overoptimization starts, and how it ends\|P20]]'s stopping rule on gold-labelled data not used before, become the next work items. The PI also asked whether logs of a black box could make the unobservable observable (H33), and whether the framework's new tools are real or a biased perception (§8) | PI; executor (the statements, checks and wiring) | `derived/diagnostics.md`, `STANDARD.md`, `IMPORT.md`, `RELATED.md`, `ROADMAP.md` |
| Q33 | after pull request #29 was merged, with its history, and the other branches deleted: the executor's recommendations approved. (i) The hold on external review is lifted narrowly: one mathematical reader of `CORE.md` and `derived/`, and the literature checked, done for D10 and D11 from records and abstracts. (ii) H34 becomes the second arm of case C3. (iii) The general core is unfrozen for outcomes that are not finite and for estimation guarantees, and for nothing else; the stability row's count restarts when its definitions change. (iv) No history rewrite: the files removed under Q27 stay in the history. (v) Novelty was never the point; the question is which theories the framework can import from (§9) | PI; executor (the survey) | `ROADMAP.md`, `RELATED.md`, `REFERENCES.md`, `NOTES.md` §9 |
| Q34 | with arXiv allowed: collect how the imports treat the continuous case, and a table mapping each term, concept and definition to its finite and its continuous formal form. Applied: `general/dictionary.md`, from the texts of eleven sources on arXiv and the records of the rest; its findings: alignment theory mostly stays finite on purpose; one function, the log-normalizer, decides most of the continuous case; atoms are the hinge; existence becomes conditional; some finite bounds become infinite; estimation depends on which log-ratios are known more than on the space | PI; executor (the reading and the table) | `general/dictionary.md`, `REFERENCES.md`, `RELATED.md`, `CORE-GENERAL.md` |

### 3.2 Papers and data the PI could supply

| # | For | What is needed | Why | Note |
|---|---|---|---|---|
| D1 | behavioural economics (fine) | Gneezy and Rustichini (2000), weekly counts of late parents per centre | the pair test (fine, removal) of `ontologies/behavioural-economics/` | a copy of the data appears to be public (`users.stat.ufl.edu/~winner/data/fineprice.txt`, seen in a search result, not opened) |
| D2 | behavioural economics (defaults) | the distribution of contribution rates under two defaults, in a company not used before | a confirmatory pass-through ratio test | v7.10 already read Madrian and Shea (2001), Choi et al. (2004) and Beshears et al. (w12009) from their figures and tables (T7-2, 2b, 2d), so tests on them are exploratory; the result is in `ontologies/behavioural-economics/`, section 3 |
| D3 | machine learning | samples from an initial policy, scored by a gold and a proxy reward model | the best-of-`n` slope and the covariance-at-the-peak predictions | found: Coste et al. [[References\|@coste2024]], answers of a 1.4B Pythia policy, gold-scored, at `huggingface.co/datasets/tlc4418/gold_labelled_gens`. The paper, read in full (supplied by the PI), says its best-of-`n` used at least 12,500 answers per prompt for 1,000 prompts of AlpacaFarm's validation split, at temperature 1, top-p 0.9, up to 256 new tokens; the gold is AlpacaFarm's 7B human-preference reward model; their proxies (7M to 1.3B, trained on 46,000 gold-labelled pairs) are not released. The dataset is described as 12,600 generations; whether that is per prompt is to be read from its card. The answers are not read. Access: `huggingface.co` is refused by this environment's network policy; `pip install datasets` works. A proxy must be added: on this machine's CPUs only the smallest of their sizes can be trained, and only a subset of the answers scored. **Used in W1**, with a linear proxy that scored all 12.6 million answers (`cases/w1-best-of-n-slope/`) |
| D4 | evolutionary biology | Chippindale et al. (2001), the hemiclone fitness values per sex | the angle and the shortfall of ordinary selection | supplementary data, if any |
| D5 | medical sciences (report cards) | Dranove et al. (2003): treatment by severity class, before and after the cards | the log-odds prediction | Medicare data are not public; the published cards give hospital-level deaths, not treatment by severity. Low priority |
| D6 | medical sciences (four-hour target) | Mason et al. (2012): the shares of the three time intervals by year, trust and admission; or the same intervals in a system whose data have not been read | the ratio test and the within-cell misalignment | the paper's tables (not reachable from here); a House of Commons Library briefing charts the minute at which patients leave, from national records; England's data are seen in summary |
| D7 | industrial organization | the German price archive, 2016 to 2018, with the station list; Assad et al. (2024) and its replication package; their method paper (2022) | W2 (`ROADMAP.md`) | the archive needs credentials from Tankerkönig (`creativecommons.tankerkoenig.de`); the package is `doi.org/10.7910/DVN/X4MSWW`; the papers are at `discovery.ucl.ac.uk/10187765/1/draft_v15_JPE_main.pdf` and `discovery.ucl.ac.uk/10187769/1/ACEX_PP_2022.pdf`. Not read |
| D8 | deceptive alignment (H27) | Needham et al. (2025), and their evaluation-awareness dataset | a world test of [[P17 — What an unobserved condition can hide\|P17]]'s reach | arXiv 2505.23836; `huggingface.co/datasets/jjpn2/eval_awareness`. Not read |
| D9 | experimental economics | Cason, Friedman and Hopkins (2014), and its data, if published with it | the Rock–Paper–Scissors arm of the ontology's prediction | `doi.org/10.1093/restud/rdt023`. Low priority: the potential-game arm needs new sessions in a laboratory |
| D10 | outer and inner alignment ([[P49 — Outer and inner misalignment\|P49]]) | Hubinger, van Merwijk, Mikulik, Skalse and Garrabrant (2019), arXiv:1906.01820 | verified from its record and abstract (2026-10-07), and listed in `REFERENCES.md` | recorded in v7.10; found by web search, as arXiv is not reachable from this environment |
| D11 | reward tampering ([[P50 — Tampering: a change of the measurement, not of the world\|P50]], [[P51 — What signals, audits and re-measurements reveal of tampering\|P51]]) | Ring and Orseau (2011), the delusion box; Everitt, Krakovna, Orseau, Hutter and Legg (2017), the corrupted reward channel; Everitt, Hutter, Kumar and Krakovna (2021), reward tampering in causal influence diagrams; Leike et al. (2017), the AI safety gridworlds, arXiv:1711.09883 | verified from their records and abstracts (2026-10-07), and listed in `REFERENCES.md`; the gridworlds' code is reported under the Apache 2.0 licence, to be confirmed from the repository before case C3 borrows a layout | from memory, then found by web search |
| D12 | the imports of §9 marked "now" | the full texts of White (1982), Vuong (1989), Baker (2002), Courty and Marschke (2008), Ben-Tal et al. (2013), Blackwell (1953), Lindsay (1983), Pistone and Sempi (1995) and Polyanskiy and Wu (2025); those on arXiv were read once the PI allowed it (Q34) | a theorem enters `derived/` only after its statement is read in the source, not in an abstract | their records and abstracts were found by web search; arXiv is reachable since Q34, the publishers are not |

Every test is pre-registered and pushed before any computation (README rules).

**Handing sources over.** This repository is public, so papers and third-party data go into a private repository that
the session can read, not into this one. Papers are read at once. A data file is listed, its documentation and codebook
read, and its rows left unopened until the registration of the test that uses it has been pushed; then only that test's
script opens it, and the result says when the file arrived and what of it had been seen.

### 3.3 Open proposals

| # | Proposal | Kind | Evidence so far |
|---|---|---|---|
| E1 | **Estimation.** For `n` decisions from an actor that does pursue `F` at an interior intensity, `2n·M(p̂_n)` is asymptotically χ² with `|X| − 2` degrees of freedom (Wilks); at the boundary `t* = 0`, a chi-bar-square mixture. With [[D9 — Observation and identification\|D9]], estimated quantities get confidence sets, which the standard already asks for | **applied as [[P23 — The estimated misalignment of an actor that pursues the objective\|P23]]** for `t* > 0`; the boundary `t* = 0` is open | probe: means 1.08, 2.98, 6.09, variances 2.15, 5.97, 11.5 for `|X|` = 3, 5, 8 |
| E2 | **A floor.** `{p_{F,t} : t ≥ t_min}` for a principal for whom doing nothing fails; the nearest intensity is `max(t*, t_min)` | a remark in `derived/misalignment.md` | done: [[P35 — Floors and caps\|P35]] (floors and caps, imported in R5) |
| E3 | **Ordinal objectives.** The tilts of `q` by every function non-decreasing in `F`: closed, contains the ray, misalignment a convex program. Best-of-`n` on a proxy is aligned with its ranking but not its values | a definition and a result | done: [[P36 — Ordinal objectives\|P36]] (the ordinal specification, imported in R5) |
| E4 | **Several principals.** Unions and intersections of intended sets; conflict as an angle at the default | a remark | done in part: gridlock and the pooled pursuit ([[P42 — Several principals: gridlock, and the pooled pursuit\|P42]]); chains of delegation open |
| E5 | **Sharper identified sets.** [[P17 — What an unobserved condition can hide\|P17]] uses KL alone. Every `f`-divergence obeys data processing, and for two conditions the exact condition for a pair of behaviours to come from a pair of views is a comparison of experiments (Blackwell) | a result | citation to verify before use |
| E6 | **Misalignment in an unobserved condition.** [[P17 — What an unobserved condition can hide\|P17]] bounds the objective's average. The largest misalignment within `ε` of the observed behaviour has no closed form; a small-`ε` expansion, as in [[P11 — The misaligned share at the start of a change\|P11]], may give one | a result | open |
| E7 | **Identifying a view.** Which interventions identify what the actor perceives: the control-theory question of observability, from the principal's side | a result | open |
| E8 | **Binned evaluators.** An evaluator with distinct values on distinct outcomes has `m = F` and `R = 0` ([[D10 — Evaluator, regression and residual\|D10]], Notes), so [[P19 — A monotone regression rules out overoptimization\|P19]]'s hypothesis becomes "the evaluator never misorders two outcomes", which a learned reward model is not expected to meet. In practice the regression is estimated on bins of the evaluator, a coarser evaluator `h(F̂)`. Pursuing `F̂` and pursuing `h(F̂)` differ by at most `t·w` in log-probability, for bins of width `w` and `h` the bin's centre, so [[P19 — A monotone regression rules out overoptimization\|P19]] for the binned evaluator holds for `F̂` up to an error that grows with `t·w`. Wanted: the bound, and whether it is tight enough to say anything at the intensities where overoptimization is seen | **applied as [[P26 — The regression on bins governs at small intensity\|P26]]** for the pursuit, with the margin `t·w·D/4` (Popoviciu); open for best-of-`n`, where the natural bin width is in units of `log Q(F̂)` and the lowest bin needs separate care | found in the double-check of the v10 ontologies. This cell said that outcomes that are not finite would make the regression non-trivial without binning: wrong, since a one-to-one evaluator has `m = F` on any outcome space (`CORE-GENERAL.md`, GD10); only an evaluator that merges outcomes makes it informative. For best-of-`n` with an evaluator without atoms, the bins are not needed (`general/transfer.md`, the row for best-of-`n`) |

**Verified.** [[D2 — Pursuit of an objective|D2]]'s justification says that the check of [[P3 — A fixed objective is visible in the changes of behaviour|P3]] exercises mixture paths. It does:
`checks/test_paths.py::test_fixed_objective_iff_span` asserts that a mixture of two behaviours leaves the span of the
fixed-objective test by more than `10⁻³`.

### 3.4 Contexts (history)

Resolved in v9 by [[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]]: see §3.1, Q1. The v8 analysis is kept below for the record.


**What was found.** In four of the five ontologies, part of an outcome is fixed before the actor acts: the prompt a
model answers, the patient who arrives, the request a manager sends, a person's circumstances. The actor chooses only
what happens within each context. The core's pursuit ray reweights whole outcomes, contexts included, which the actor
cannot do. So within one context every item applies as stated, but "pursue `F`" across contexts is not yet defined by
the core.

**What the ontologies do meanwhile.** They apply every item context by context. Across contexts they use the
specification "pursue `F` in every context, at any intensity in each", which is a specification by [[D3 — Specification, declaration and misalignment|D3]]; when the
actual behaviour has the default's context masses, its misalignment is the average of the per-context misalignments,
by [[P4 — What KL measures|P4]](iii). [[P13 — What the start of a change gains|P13]](i), and the first limit of [[P13 — What the start of a change gains|P13]](ii), hold across contexts as stated.

**Options.**
- **A (recommended): one shared intensity.** A definition: a resolution of *contexts* is one whose cell masses every
  behaviour of the actor shares with the default; the standard specification in contexts is pursuit of `F` within every
  context at one shared intensity. Then a proposition, to be proved and checked: (i) it is the unique maximizer of net
  value among behaviours with the default's context masses (the per-context form of [[P4 — What KL measures|P4]](i)); (ii) its misalignment is
  the average of the per-context misalignments plus an inconsistency term, never negative, which is zero when one
  intensity is nearest in every context. Why one intensity: "pursue `F`" names one objective on all outcomes, and
  pursuing it at different intensities in different contexts is pursuing a different objective, `t(C)·F`, which [[P1 — Every behaviour is a tilt of any other|P1]](ii)
  tells apart from `F`. KL-regularized fine-tuning, with one `β` for all prompts, is exactly this specification. The
  report-card prediction (`ontologies/institutions/`) needs it; the delegation ontology asks for it.
- **B: free intensity per context.** Keep what the ontologies do now. It needs no new item, but it forgives an actor
  that pursues hard in some contexts and not at all in others.

Either way the change is an addition (one definition, one proposition, a new section), not a refactoring: no existing
item changes.

(End of the v8 record.)

## 4. Order next

The order of work, its blockers and the checks against drift are in `ROADMAP.md`, the one place they are kept. This
section keeps the history of what was done.

**Done before v11:** the merge (`IMPORT.md` §6). The defects found in the archive were fixed (M1), the record and the
rules of evidence written (M2), the Obsidian view built (O1); the tag `v7.10` marks the vault, and the core replaced it
on `main` (R7). The ontologies were then reworked around disciplines with numbers (Q22). Since v10: evaluator and
sample slots in the ontologies, with the claims they allow; [[P25 — The target's curve turns no more often than the regression|P25]], the shape law; [[P26 — The regression on bins governs at small intensity|P26]], binned evaluators for the
pursuit; the import of v7.10 (R1–R6: [[P27 — The best use of a departure budget|P27]]–[[P38 — Any convex cost|P38]], [[L1 — Separable bounds are loose when two quantities change rank|L1]], [[C1 — No ranking of errors holds at every budget|C1]]–[[C12 — No misalignment, no stakes|C12]]) and its review (`IMPORT.md` §7). The general core,
drafts 1 to 3 (Q23, Q24).

**Done in v11:** the scope widened to groups and several principals with declared weights ([[P39 — Several actors: coordination plus individual misalignment|P39]]–[[P42 — Several principals: gridlock, and the pooled pursuit|P42]], Q24, Q25);
the freeze (Q26); `cases/` with lint R14, and cases C1 and C2, each revising a prediction before its data were read;
`SCENARIO.md`; `ROADMAP.md`; W1, the first prediction tested on data not seen before: refuted.

**Kept from the earlier list, not scheduled** (`ROADMAP.md`, "Not now"): E8 for best-of-`n` ([[P26 — The regression on bins governs at small intensity|P26]] covers the pursuit
only); the alignment plane (H6); porting v7.10's F2, an exact check of [[P22 — No test detects misalignment faster than misalignment|P22]](i), and F4, edge cases in log space for the
checks' helpers.

## 5. Retrospective after v9, and hunches for v10

### 5.1 What v9 is

v9 is a measurement standard: a small set of premises, forced choices, exact decompositions (departure, stakes,
avoidable and unavoidable misalignment), identification-aware reporting, and mechanical checks. It is not yet a theory
of what optimizing a proxy does. v7.10 was both: it measured the departure and explained it by what the agent optimizes
("target" against "evaluator"). The predictive content, the Goodhart theory and the detection results, lived in the
explanatory half, which v9 left out with "explanations". The PI's plan is to bring it back slowly, as one or two strong
concepts from which the rest is derived, each with a canonicity argument, so that the design space stays confined.

### 5.2 What v7.10 had that v9 lacks, and whether v9 can derive it

| v7.10 | Content | Derivable in v9? |
|---|---|---|
| Prop 20 | Goodhart as a covariance, for any optimizer: `E_pF − E_qF = Cov_q(w, F̂) − Cov_q(w, E)`, `w = p/q` | yes, once the evaluator has a name: the finite form of [[P13 — What the start of a change gains\|P13]](i) (the Price equation) |
| Prop 21 | an affine regression of target on evaluator rules out overoptimization, for actors that see only the evaluator | yes, from [[P8 — An actor that cannot tell outcomes apart\|P8]](i) and [[P13 — What the start of a change gains\|P13]](i); and it generalizes to any monotone regression (H1 below) |
| B §4 | Gaussian target and evaluator: gold gain `√2·ρ·sd·√KL` exactly | yes: [[P13 — What the start of a change gains\|P13]](ii) to first order; now credited in its Lineage |
| Thm 9 | no ranking of evaluator errors holds at every budget: variance governs small budgets, oscillation large ones | yes, once the error is an object: the worst case at departure `δ` is a pursuit of the error ([[P9 — What is at stake\|P9]](i), as in [[P17 — What an unobserved condition can hide\|P17]](ii)); the small-`δ` limit is [[P13 — What the start of a change gains\|P13]](ii)'s expansion, the large-`δ` limit [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits\|P5]](iv)'s third case |
| Prop 11 | a KL limit cannot contain heavy-tailed errors; a χ² limit can | not in finite outcomes (heavy tails need infinitely many); its finite shadow is a χ² budget as a convex feasible set ([[D7 — Feasibility\|D7]], [[P15 — Misalignment splits into what the actor could avoid and what it could not\|P15]](ii)). Needs "the actor's own cost", distinct from the measure (v7.10's Prop 15) |
| Prop 18 | misalignment caps the detection exponent of any test (Chernoff `≤` KL) | yes, by importing Chernoff's theorem, once sampling is a concept |
| Prop 19 | the evaluation gap `Γ = Σ_c (ρ_dep − ρ_ev)·KL_c` | yes, in one line from [[D8 — Conditions, responses and views\|D8]] with frequencies; it complements [[P17 — What an unobserved condition can hide\|P17]] (shift of conditions, against shift of behaviour) |
| §11 | "what the core forbids": nine falsifiable statements, some tested in R5 and R6 | a section, not a result: return it as `derived/forbids.md`, each statement with its test |
| A3 tiers | results for any actor, and for an assumed entropic actor | v9 can test the actor model instead of assuming it ([[P3 — A fixed objective is visible in the changes of behaviour\|P3]], [[P12 — What interventions reveal\|P12]]): tier-E results return as results conditional on "the actor pursues `F̂`" |

So most of what was lost is derivable from v9 plus one concept, the evaluator; the detection results need a second,
sampling.

**Applied in v10.** Prop 20 as [[P18 — Through the evaluator, only the regression counts|P18]](ii); Prop 21 and B §4 as special cases of [[P19 — A monotone regression rules out overoptimization|P19]]; Prop 14 as [[P20 — Where overoptimization starts, and how it ends|P20]]; Prop 18 as
[[P22 — No test detects misalignment faster than misalignment|P22]]; Prop 19 as [[P24 — The evaluation gap|P24]]. Still open: Thm 9, Prop 11, §11, the A3 tiers.

### 5.3 The strong concept: candidates

**Candidate 1, recommended: the evaluator.** The objective the actor pursues, `F̂`: declared, as a reward model, a
performance measure, a fine or a selection regime, or revealed, as `log(p̂/q)` up to scale and constant ([[P1 — Every behaviour is a tilt of any other|P1]]).
- *Why it is canonical.* (a) It adds no assumption: by [[P1 — Every behaviour is a tilt of any other|P1]] and [[A3 — Pursuit is the best trade-off|A3]], every full-support behaviour is the best trade-off
  for exactly one objective direction, its revealed evaluator. (b) It is the actor's counterpart of the principal's
  objective, in the same currency: the principal declares `(q, F)`, the actor reveals `(q, t̂·F̂)`. (c) It is universal:
  each of the five ontologies has one (the reward model; selection through males; the fine; the report card; the
  measured bonus). (d) Its scale-free invariants are objects v9 already uses: the angle `θ` under `q` ([[P11 — The misaligned share at the start of a change|P11]]), the
  regression `m = E_q[F | F̂]` (the cell average of [[P8 — An actor that cannot tell outcomes apart|P8]] for the resolution that `F̂` generates), and that resolution.
- *What it would re-derive.* Prop 20, Prop 21 and more (H1), B §4, Thm 9, the overoptimization peak, and Manheim and
  Garrabrant's four Goodhart variants (H3).
- *The geometry.* Target and evaluator span a two-parameter family `{tilt(q, a·F + b·F̂)}` through the default: the
  alignment plane (H6). Every Goodhart quantity lives in it.
- *Where to look for it in existing theory.* The angle between a performance measure and value in the economics of
  incentives (Baker's "distortion" of performance measures, 2002); the angle between true and proxy rewards
  in occupancy space (Karwowski et al., ICLR 2024); hackability of reward pairs (Skalse et al., NeurIPS 2022); selection
  gradients and the secondary theorem of selection in biology (Lande and Arnold; Robertson; Price); Manheim and
  Garrabrant's taxonomy.

**Candidate 2, a possible second: sampling.** Observation through `n` independent decisions.
- *Why it is canonical.* It gives misalignment a second, independent meaning that agrees with the first (H4): the
  expected log-likelihood ratio per decision, under the actual behaviour, of the actual against the nearest intended
  behaviour is `M`, so in a sequential test (Wald) about `log(1/α)/M` decisions reject the intended behaviour. Value
  lost ([[A4 — Misalignment is value lost|A4]]) and evidence gained agree, in the same direction of KL: the same pattern as [[A2 — Pursuit is the steepest climb|A2]] and [[A3 — Pursuit is the best trade-off|A3]] agreeing on the
  cost.
- *What it would re-derive.* Prop 18 (with Chernoff's theorem), the estimation layer (E1: Wilks), and the standard's
  error bars, as results instead of instructions.

**Why not other candidates.** v7.10's "capacity" is the intensity or the departure, already in v9. v7.10's conventions
are roles already assigned (misalignment = free, stakes = budget, a fixed price = a single intended behaviour). Actor
models are hypotheses that [[P3 — A fixed objective is visible in the changes of behaviour|P3]] and [[P12 — What interventions reveal|P12]] test.

### 5.4 Hunches

| # | Hunch | Status |
|---|---|---|
| H1 | **Monotone regression rules out overoptimization.** If every revealed objective of a path is a non-decreasing function of `F̂` (pursuit of `F̂`, best-of-`n`, threshold selection, any monotone transform), and `m = E_q[F | F̂]` is non-decreasing, then `E_{p_s}[F]` never decreases. Proof sketch: the behaviours are tilts by functions of `F̂`, so `E_p[F] = E_p[m(F̂)]` ([[P8 — An actor that cannot tell outcomes apart\|P8]](i)); by [[P13 — What the start of a change gains\|P13]](i) the rate is `Cov_{p_s}(F_s, m(F̂))`, the covariance of two non-decreasing functions of `F̂`, which is never negative (Chebyshev's association inequality). It generalizes v7.10's Prop 21 (affine) and B §4 (Gaussian) | **proved as [[P19 — A monotone regression rules out overoptimization\|P19]]**; probe: 0 decreasing curves in 111 monotone instances; among 1889 non-monotone ones, 1474 decrease somewhere |
| H2 | **Extremal Goodhart.** Along the pursuit of `F̂`, at large intensity the target decreases exactly when `m` is lower at the largest evaluator value than at the second largest; the peak, when there is one, is where `Cov_{p_t}(F̂, m(F̂)) = 0` | **proved as [[P20 — Where overoptimization starts, and how it ends\|P20]]**; probe: 1889 of 1889 in the limit (log-space); at moderate intensity, a third value close to the second can still dominate |
| H3 | **Goodhart's four variants are four objects of v9.** Regressional: the cell average and its Jensen gap ([[P8 — An actor that cannot tell outcomes apart\|P8]]); extremal: H2; causal: an intervention that changes more than it adds ([[D6 — Intervention and pass-through\|D6]], [[P12 — What interventions reveal\|P12]]); adversarial: an actor whose view separates observed from unobserved conditions ([[D8 — Conditions, responses and views\|D8]], [[P17 — What an unobserved condition can hide\|P17]]) | C: a mapping, to be checked against Manheim and Garrabrant's definitions |
| H4 | **Value and evidence agree.** Misalignment is both the least value lost ([[A4 — Misalignment is value lost\|A4]]) and the evidence rate against the nearest intended behaviour under the actual one (Wald). Could justify the direction of KL independently of [[A3 — Pursuit is the best trade-off\|A3]] | **stated as [[P21 — The expected evidence is misalignment\|P21]]**: with the log-likelihood ratio as evidence ([[D11 — Sample and evidence\|D11]]) and samples drawn from the actual behaviour, the rate is `KL(p̂‖·)`, form and direction, without [[A3 — Pursuit is the best trade-off\|A3]]; it rests on the choice of evidence (Neyman–Pearson) instead. [[D3 — Specification, declaration and misalignment\|D3]]'s Why gives the reading, and argues from value |
| H5 | **The measure is not the actor's cost.** [[P14 — The cost of departing from the default is forced\|P14]] forces the measure to be KL; v7.10's Prop 11 says an actor regularized by KL is exposed to heavy-tailed evaluator errors, and one regularized by χ² is not. Not a contradiction: the actor's cost belongs to its feasibility or its mechanism, never to the measure | B: keep the two apart in every future item |
| H6 | **The alignment plane.** Target and evaluator span a two-parameter exponential family through `q`; the gold curve, the actor's misalignment along its own pursuit and the stakes may have closed forms in it | D: explore; **Gaussian closed form probed** (B5): gain per √departure = √2·sd·cos θ and M = departure·sin²θ, exact to 4e-15; not exact beyond (an exponential × normal default departs) |
| H7 | **Active inference reached the same direction.** Its "risk" term is a KL from predicted to preferred outcomes, the direction of `M` | D: verify before citing |
| H8 | **Baker's distortion is our angle.** The alignment of a performance measure with value, as a cosine of marginal effects, would be [[P11 — The misaligned share at the start of a change\|P11]]'s `cos θ` in the incentive literature | C: the paper exists (Baker 2002, verified from its record); whether its distortion is this angle needs its text, which is not open. [[P50 — Tampering: a change of the measurement, not of the world\|P50]](iii) suggests a sharper reading: his two parameters, distortion and risk, as the world's misaligned share and the noise share (`RELATED.md`, principal–agent theory) |
| H9 | **The dimension law.** Against a fixed smooth behaviour, misalignment at a record of width `w` grows like `(D − d)·log(1/w)`, `d` the information dimension (Rényi): "digits decided" made exact | **tested** (T1): four cases, including the Cantor measure, which no count of atoms explains |
| H10 | **No pursuit makes a pile.** A pile at a threshold is evidence that the actor does not pursue the evaluator | **tested** (T2); a theorem by the chain rule, to be written |
| H11 | **Collusion is coordination, often in time.** Under independent pursuit, misalignment on joint actions = total correlation + individual misalignments, exactly | **proved as [[P39 — Several actors: coordination plus individual misalignment\|P39]]**; **tested** (T3): tit-for-tat shows `0` per round and `0.231` nats per round over time |
| H12 | **Strategic residue is irreversibility.** Learning that pursues a potential is reversible; misalignment against reversible processes ≤ EP/2, ≈ EP/4 at low intensity | **proved as [[P41 — Reversibility: the Jensen–Shannon divergence from the reversal\|P41]]**: the Jensen–Shannon form, the bound and the quarter law; EP = flux × affinity is Schnakenberg's, in its Notes. **tested** (T4); found `EP = (t·C/8)²` in 2×2 games at low intensity, not predicted; to derive; **explained** (B1, B2): misalignment against reversibility is the Jensen–Shannon divergence between forward and backward flux (to 2e-12), and EP = cycle flux × cycle affinity with affinity t·C, the 1/64 being the cycle's series conductance (out of sample: 0.013125) |
| H13 | **Gridlock and pooling.** The default satisfies every standard specification; with floors the compromise pursues `Σ w_k·t_k·F_k` | gridlock, and pooling with declared intensities, **proved as [[P42 — Several principals: gridlock, and the pooled pursuit\|P42]]**; the form with floors **tested** (T5), not claimed |
| H14 | **The compromise meets every floor exactly** | **failed** (T5b): 11 of 20 against 15 predicted |
| H15 | **Lock-in has a rate, fixed by early chance** (corrects "no single rate") | **tested** (T6) |
| H16 | **Information for the principal, geometry for the actor.** Gaming is cheap transport under a threshold evaluator; an actor's reach could enter as feasibility (GD7) | D: explore; the fudging probe only (2.3 against 15.6 patient-minutes) |
| H17 | **Strategic scenarios lift to standard ones on derived spaces** (`general/derived-spaces.md`) | C: a mapping, with T3–T6 as its first tests |
| H18 | **Model space.** Training as a Gibbs posterior over models; PAC-Bayes's complexity term is the departure, which bounds the evaluation gap | D: explore |
| H19 | **Schrödinger bridge.** An actor moving outcomes by noisy short steps, conditioned on its target, is a Schrödinger bridge: Sanov on trajectories | D: a guess |
| H20 | **Piles from an optimized default.** An actor with an information cost that chooses its own default (rational inattention) has a discrete default: one atom below beta_c = 1/(2·Var), splitting near it, with between √(β/6) and 2√(β/6) atoms; each condition's behaviour is still a tilt of that default. So piles have two sources: gaming, at the evaluator's thresholds, and inattention, at the actor's own atoms | **probed** (B3, B3b): split and range held; the first count prediction failed |
| H21 | **Attention is mutual information.** Misalignment against "ignoring the situation" (one behaviour in every condition) is the mutual information between condition and action: a fifth structural specification, the cost of rational inattention | **proved as [[P40 — Attention: misalignment against ignoring the situation\|P40]]**; identity (B7) |
| H22 | **The angle is exact under χ², local under KL.** Under a χ² budget the target gains √B·ρ·sd for any default (Cauchy–Schwarz), ρ the correlation under the default: Laidlaw et al.'s correlated proxy is the angle of [[P11 — The misaligned share at the start of a change\|P11]]. Under KL it is exact only for Gaussians | **probed** (B4c, B5) |
| H23 | **Heavy tails: an infinite frontier at every budget.** With a power-law upper tail, `t_max = 0`, and any positive KL budget buys unbounded gain (like `L/log L`); a χ² budget buys `√(B·Var)` | **probed** (B4a, B4b) |
| H24 | **Collusion is a question about the revealed objective, not about dependence.** Case C1: coordination tracks firms reacting to each other, colluding or not. What separates collusion is that the joint moves pursue joint profit rather than each firm's own: each firm's revealed objective ([[P1 — Every behaviour is a tilt of any other\|P1]], [[D10 — Evaluator, regression and residual\|D10]]), given the rival's last price, correlates with joint profit beyond its own. That needs the profit of every joint move, so a demand model: known in C1's simulation, estimated in industrial organization, absent from the German record, which has no volumes | D: not scheduled (`ROADMAP.md`, "Not now"); a case on C1's sessions only if W2 needs it |
| H25 | **The width bounds the scatter of a training run.** A trained policy within `δ` nats of its optimum has a target average within the width of that KL ball along `F` ([[P29 — The width is the exact worst case\|P29]]), about `√(2δ)·σ(F)` for small `δ`. No stopping rule resolves gains closer than that. C2: median `KL` to the optimum `0.010` nats gives about `0.14·σ`, against a median observed scatter of `0.016`: a loose bound, as worst cases are | D: exploratory on C2's output, only if a world test needs a stopping rule |
| H26 | **Single-peakedness can be checked before trusting the stopping rule.** The regression on bins of the evaluator, estimated from labelled outputs ([[D10 — Evaluator, regression and residual\|D10]], [[P26 — The regression on bins governs at small intensity\|P26]]), says whether the first zero of the covariance is the highest peak ([[P25 — The target's curve turns no more often than the regression\|P25]](iii)); `STANDARD.md`'s evaluator row already asks for it. Open: the sample size at which bins judge single-peakedness correctly, given [[P26 — The regression on bins governs at small intensity\|P26]]'s margin | C: follows from [[P25 — The target's curve turns no more often than the regression\|P25]] and [[P26 — The regression on bins governs at small intensity\|P26]]; the sample size is to be worked out |
| H27 | **Evaluation awareness bounds the leak from below, not from above.** [[P16 — An actor cannot behave more differently than it can tell conditions apart\|P16]](iii) and [[P17 — What an unobserved condition can hide\|P17]] need an upper bound on how far an actor can tell evaluation from use. Studies of evaluation awareness give lower bounds: on 1,000 transcripts from 61 datasets, humans tell evaluation from deployment with an AUC of 0.92 and the best model 0.83 (Needham et al. 2025, arXiv 2505.23836, read in a search summary only). Any score's AUC satisfies `AUC − ½ = ∫(F_Q − F_P) dF_P ≤ TV`, so by data processing and Pinsker the inputs differ by at least `2·(AUC − ½)²` nats: 0.35 for an AUC of 0.92 (derived here, not checked; a first guess, `TV ≥ 2·AUC − 1`, was false: uniform inputs on `[0.5, 1.5]` and `[0, 1]` give an AUC of 0.875 and a TV of 0.5). That is more than the 0.10 nats that already made `SCENARIO.md`'s bounds span −€4.80 to €5.64, so for typical suites [[P17 — What an unobserved condition can hide\|P17]]'s bounds say little, and only [[P17 — What an unobserved condition can hide\|P17]](iv), audits indistinguishable from use, helps. Their dataset is public and unread | D: a candidate world test of a negative prediction, after W1 |
| H28 | **The best-of-`n` prediction needs no training.** Coste et al. released 12,600 outputs of their initial policy, each with a gold score (`NOTES.md` §3.2, D3). With a proxy reward model fixed in the registration, the best-of-`n` curve of the gold, and the slope of [[P13 — What the start of a change gains\|P13]], follow from resampling the outputs within each prompt | **tested** as W1 (`cases/w1-best-of-n-slope/`): run on 12.6 million unseen answers with a proxy trained here; the prediction from [[P13 — What the start of a change gains\|P13]] was refuted |
| H29 | **The executor's simulations test the executor as much as the framework.** C1 and C2 were designed, run and judged by the model family that wrote the predictions, and four of their seven predictions failed on the executor's own thresholds or design. A registration read by the PI, or by an outside reader, before it is pushed would catch some of this (rule (f)) | proposal to the PI |
| H30 | **Saturation, not decline, and the shape is the finding.** In W1 the gold curve under best-of-`n` keeps the framework's initial slope up to `n = 16` and then saturates, with almost no fall; the literature's two numbers, `a` and `b`, hide that shape and misstate the slope. A report of overoptimization should give the curve's local slopes in `d` against the initial slope of [[P13 — What the start of a change gains\|P13]], not a fitted form. Whether a neural proxy gives the same shape is open | D: a candidate field for `STANDARD.md`'s evaluator row, not scheduled |
| H31 | **Unconverged reinforcement learning changes more than it pursues.** In W3, the part of `log(π/π_ref)` along the reward has a slope near `1/β` (`4.27` against `5` at the starting KL coefficient), as [[P4 — What KL measures\|P4]] says, yet within each model's own continuations the reward explains only a tenth of it. The rest may be the drift a noisy policy gradient accumulates, which the KL penalty slows but does not aim. If so, along one run the reward's share of the revealed objective, within the tuned model's own continuations, should rise towards 1 as the run converges; a share that stays low at convergence would mean the rest is not drift but a systematic pull, of the value estimate or the adaptive coefficient, which the framework would then have to name. Test: checkpoints of one run, or runs at several `β`, with their reward model, all public | open: needs public checkpoints. W4 (`ROADMAP.md`, step 1) asks the part two public runs can answer: whether the off-reward change recurs in another run |
| H32 | **The most charitable principal.** When the principal's objective is known only to lie in the span of given functions, the least misalignment any such principal finds is the unexplained misalignment of [[P44 — What named objectives explain\|P44]], attained by the principal whose objective is the named pursuit's exponent, and the largest is the departure. So an uncertain target turns misalignment into an interval, as an unobserved condition does in [[P17 — What an unobserved condition can hide\|P17]]. Proof sketch: over the span, `inf_{c, t ≥ 0} KL(p̂‖tilt(q, t·c·Φ))` is the infimum over the whole exponential family, attained at the moment-matching tilt, which is the named pursuit ([[P44 — What named objectives explain\|P44]](i)); one of `±F'` never beats the default, so [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits\|P5]](iv) gives the departure | **applied as [[P48 — Misalignment when the target is uncertain\|P48]]**, with a direct proof and a check (Q30); first probed in `probes/diagnostics/probe_charitable.py` |
| H33 | **Logs as outcomes.** Activations logged from a black box are observations, so making them part of the declared outcome keeps [[A1 — Behaviour suffices\|A1]]: the core would judge their distribution, not their meaning, the move [[P50 — Tampering: a change of the measurement, not of the world\|P50]] made for measurements. Three consequences, none yet a result. (a) If the outputs are computed from the logged activations, these are a view of the condition ([[D8 — Conditions, responses and views\|D8]]), so by [[P16 — An actor cannot behave more differently than it can tell conditions apart\|P16]] the divergence of activations between evaluation and use bounds from above how differently the actor can act there: the `ε` that [[P17 — What an unobserved condition can hide\|P17]] needs and that studies of evaluation awareness cannot give (H27). But an upper bound on a divergence between high-dimensional distributions cannot be estimated from samples without a model, so the bound inherits the model's error. (b) A surrogate, a white-box model trained on the logs, transfers its findings to the black box only within its fidelity, a divergence measurable where the surrogate was fitted and bounded elsewhere only by [[P17 — What an unobserved condition can hide\|P17]] again. (c) What the black box "knows" is identified from logs only under stated assumptions ([[D9 — Observation and identification\|D9]]): where the labels come from a fallible observer, a reporter that says the truth and one that says what the observer would believe fit the same data, and logs narrow the identified set only through assumptions such as consistency or sparsity. This is the programme of probing and dictionary learning in interpretability, not new; the framework would add its accounting: fidelity in nats, identified sets, the view bound | E: outside the scope (`IMPORT.md` §8, gap 5, "drop"); reopening it is the PI's decision under the freeze. A narrow test, if reopened: a small network whose internals are known, where the view bound and the surrogate's transfer are checked against the truth |
| H34 | **A monitor trained against is tampered with.** A monitor whose verdict is computed from a channel the actor can influence, such as a probe on activations, is a signal in [[P50 — Tampering: a change of the measurement, not of the world\|P50]]'s sense, and training against it is the trainer's optimum of [[P50 — Tampering: a change of the measurement, not of the world\|P50]](iii): it tampers at every positive intensity, with a share at the start equal to the share of the monitor's variance not explained by what it is meant to detect. So optimizing against an imperfect monitor buys, from the first step, a change of what the monitor reads as well as of what it monitors. The reading needs the channel declared (the activations each behaviour would produce, before any training against the monitor), and the trainer's optimum idealizes training | D: a candidate simulation, after the tampering case; no world test named |

### 5.5 Process

- Lineage amnesia (§1): search v7.10 before adding a result.
- Three restructurings without data: the next phase has to touch data (§3.2).
- Most of what was "lost" is derivable: the archive is a source of statements to re-derive and check, not of text to
  copy.

### 5.6 Drafts for v10 (applied as [[D10 — Evaluator, regression and residual|D10]] and [[D11 — Sample and evidence|D11]]; kept for the record)

**What changed from the drafts.** "Declared" and "revealed" became "known" and "revealed", since [[D3 — Specification, declaration and misalignment|D3]] uses "declared"
for specifications. The target is named in [[D10 — Evaluator, regression and residual|D10]]'s statement. Wald's sequential test is a Note of [[P21 — The expected evidence is misalignment|P21]], not an item;
Stein's exponent is not imported. [[P24 — The evaluation gap|P24]] names the specification on condition–outcome pairs, and its Notes give the
shared-intensity case, where its formula fails. Thm 9 is not yet re-derived.

**D10 — Evaluator (draft).**
*Statement.* Let `F` be the principal's objective. An **evaluator** is an objective `F̂ : X → ℝ` proposed as the one
the actor pursues: **declared** when it is a known function the actor is rewarded on, **revealed** when
`F̂ = log(p̂/q)` for a full-support behaviour `p̂`, which fixes it up to a positive factor and a constant. The
**regression** of the target on the evaluator is `m = E_q[F | F̂]`, the cell average of `F` over the resolution whose
cells are the level sets of `F̂`; the **residual** is `R = F − m`.
*Why, in outline.* (a) No new assumption: by [[P1 — Every behaviour is a tilt of any other|P1]] and [[A3 — Pursuit is the best trade-off|A3]] every full-support behaviour reveals one evaluator, up to
scale. (b) The actor's counterpart of the principal's objective, in the same currency. (c) Universal: each ontology has
one. (d) Scale-free: `m` and `R` depend on `F̂` only through its level sets, and the monotonicity of `m` only through
their order, so neither changes under an increasing transformation of `F̂`; the difference `F̂ − F` depends on a scale
that behaviour never identifies. (e) Whether the actor does pursue a declared evaluator is testable ([[P1 — Every behaviour is a tilt of any other|P1]], [[P3 — A fixed objective is visible in the changes of behaviour|P3]]).
*Results it would carry, in a new `derived/evaluator.md`.* (i) For a behaviour that sees outcomes only through `F̂`,
the target's gain is the regression's gain, and the residual's gain is `0` ([[P8 — An actor that cannot tell outcomes apart|P8]](i)). (ii) H1: a non-decreasing
regression rules out overoptimization along any path whose revealed objectives are non-decreasing functions of `F̂`.
(iii) H2: the extremal rule at large intensity, and the peak where `Cov_{p_t}(F̂, m(F̂)) = 0`. (iv) v7.10's Prop 20 as
the integrated covariance form, split into regression and residual. (v) Later: v7.10's Thm 9 (variance at small
departures, oscillation at large ones) as the matched pursuit of the residual.

**D11 — Sample and evidence (draft).**
*Statement.* A **sample** of size `n` from a behaviour `p` is a sequence of `n` outcomes drawn independently from `p`;
its **empirical behaviour** `p̂_n` gives each outcome its frequency in the sample. The **evidence** that a sample gives
for a behaviour `r` against a behaviour `r'` is `Σ_i log(r(x_i)/r'(x_i))`, in nats.
*Why, in outline.* (a) Behaviours are never observed, samples are: this is the act of measurement that [[A1 — Behaviour suffices|A1]] presumes,
and [[D9 — Observation and identification|D9]]'s "observed" is informal without it. (b) Universal: counted choices, genotypes, sampled responses, case
records, logged units of work. (c) The likelihood ratio is the most powerful statistic for two behaviours
(Neyman–Pearson). (d) The expected evidence per decision, under `p`, for `p` against `r` is `KL(p‖r)`: misalignment is
also the slowest rate at which evidence against the specification accumulates (H4), a second meaning, in the same
direction, as the value lost of [[A4 — Misalignment is value lost|A4]]. (e) Explanations can be compared in the same unit: evidence in nats for one
evaluator against another. (f) Independence is the default model; dependent samples are out of scope until an item
needs them.
*Results it would carry, in a new `derived/estimation.md`.* the expected evidence identity; Wald's expected sample size
to reject the specification; Chernoff and Stein exponents for detection (v7.10's Prop 18); Wilks for the estimated
misalignment (E1); the evaluation gap (v7.10's Prop 19) with [[D8 — Conditions, responses and views|D8]].
*A policy question.* Wald, Chernoff, Stein and Wilks are classical theorems. Do derived results whose proof is a
citation, checked by simulation, meet the standard of the derived folder? Executor's view: yes, with the theorem
quoted with its hypotheses, and a check that would fail if a hypothesis did not hold.

## 6. Retrospective after W1 and W3

Two of the three predictions tested on data not seen before failed. The PI asked where the problem lies: in the
framework, or in how it was read.

**Four layers.** A failed prediction can come from the mathematics (the theorems and their checks), the instrument (the
definitions and `STANDARD.md` applied to data), the bridge (what an ontology asserts about real systems), or the design
(which statistic, which threshold, compared with what). Both failures sit in the bridge and the design. On real data the
identities held to `10⁻¹⁰`.
- **W1.** The framework's initial slope, `0.278` (`0.263` to `0.294`), was compared with the literature's coefficient
  `a`, fitted over every `n` up to 12,500: `0.338`. Fitted over `n ≤ 16`, `a` is `0.290`, inside the framework's
  interval. What failed is an auxiliary assumption the ontology had made, that the literature's form holds from the
  start; the framework's own quantity looks right, in exploratory analysis only.
- **W3, S1.** [[P4 — What KL measures|P4]] is a theorem about the optimum of KL-regularized training. S1 claimed that one trained model is near
  that optimum, explaining "at least half": a guess about PPO with a round threshold. The training notebook itself says
  the run had not converged, which was read before registering and not treated as fatal. The part of the change that
  follows the reward has a slope near `1/β`, as [[P4 — What KL measures|P4]] says; it is small. Candidate explanations, all formed after the
  data and each needing its own registered test: drift that a noisy gradient leaves and the KL penalty pulls back
  slowly; sharpening, a second systematic objective `log π_ref`; the policy's capacity, which [[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]] would make
  unavoidable misalignment, while the ontology declared the feasible set "everything"; and generalization from training
  prompts.
- **S2 held**, but it is the weakest of the three tests: a change that follows the reward at all tends to follow its
  logit better than a squashed transform of it. Within each model's own outputs the margin is `+0.01`.

**One conceptual gap.** Misalignment does not tell drift that would not recur in another run from the systematic pursuit
of something else. For a principal both are "not what I asked for"; for a diagnosis they must be separated. The tools
derived in response are in `derived/diagnostics.md`.

**The revisions.** No registered analysis changed after its data were seen. The rest had four causes:

| Cause | Instances | Caught by |
|---|---|---|
| engineering | W3's first sampler too slow; W1's report lost at its last step | a rehearsal, timed (design rule 4) |
| degenerate cases in code | a reward that did not vary within a prompt; infinite intensities; a matched pursuit that underflowed | a rehearsal with the degenerate cases built in (rule 4); the core names each of them: [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits\|P5]](iv), [[P9 — What is at stake\|P9]], [[D10 — Evaluator, regression and residual\|D10]] |
| decisions never made | W3 pooled two models' outputs; S1's round threshold; best-of-`n` under ties; one intensity per prompt or one shared | the declaration of `STANDARD.md` in the registration (rule 1), which asks both of the last two; rules 3 and 5 |
| one family of models designs, runs and judges | all of the above | no internal fix; an outside reader, on hold (Q27) |

## 7. Whose target? After W4

The PI asked whether W3 and W4 had a proper target for the principal. They had one for one principal and none for
another.
- **The trainer** declared, in code, a formal objective: the reward minus `β` times the KL from the reference. Its
  optima, at every `β`, are the pursuit ray of the reward, which is the specification W3 and W4 used. Against it, their
  misalignment is well defined: how far PPO's result is from anything its own objective could produce at convergence.
  That is the fidelity of the optimizer, the bet of the framework, not alignment with what anyone wanted.
- **The user**, someone who wants positive and readable reviews, declared nothing, and no gold stands in for them; the
  machine-learning ontology's specification asks for one, and W1 had one. So W3's and W4's "`0.90` of the change is
  misaligned" says that the change is mostly not what the training objective asks; it says nothing on whether the change
  is good or bad for anyone.

**What the framework can still say without the user's target.**
1. *Nothing about alignment, with no target at all*: by [[P1 — Every behaviour is a tilt of any other|P1]] every behaviour pursues its own revealed objective, so some
   principal always finds it perfectly aligned.
2. *Everything that needs no target*: the departure; whether one fixed objective explains the changes across contexts
   ([[P3 — A fixed objective is visible in the changes of behaviour|P3]]); drift and what runs share ([[P45 — Drift: what runs share, and what they do not|P45]], [[P46 — What runs share between conditions, and what they do not|P46]]). Most of W4 is of this kind: the named pursuit depends only on the
   span of the functions named, not on which one is called the target, so S1 and S2, and the finding that the two runs
   are 15 nats apart and nearly always tell themselves apart, hold for any principal.
3. *An interval, when the target is uncertain but confined to a declared family* (H32, now [[P48 — Misalignment when the target is uncertain|P48]]); and outer and inner
   misalignment, with their exact split ([[P49 — Outer and inner misalignment|P49]], Q31): the least misalignment over the family is [[P44 — What named objectives explain|P44]]'s unexplained
   part, the largest the departure. In W4, any principal whose objective combines the reward, typicality (`log R`), the
   other run's reward and the other run's change finds A at least `9.46` (`9.24` to `9.67`) nats misaligned of a
   `12.28`-nat departure, and B at least `6.94` of `10.77`: most of each change pursues nothing in that family. Families
   with signs, such as "more positive is better", would narrow the upper end; [[P36 — Ordinal objectives|P36]] covers an order without a scale.
4. *What survives the principal's indifference*: a declared resolution forgives what happens inside cells ([[D4 — Resolution|D4]], [[P7 — Indifference forgives exactly what happens inside cells|P7]]),
   and grouping never shows more misalignment ([[C9 — Grouping outcomes never shows more misalignment|C9]]). Whether W4's unexplained change survives grouping by what a user
   could see (sentiment, fluency, length, repetition) would tell style drift from visible change; it needs the per-draw
   values W4 did not save.
5. *Stand-in targets*: independent evaluators of what a user wants (another sentiment model, a fluency score from a
   larger model, a toxicity classifier), each a declared target, or together a family for item 3.
6. *Two principals at once*: the trainer and the user, with declared weights ([[P42 — Several principals: gridlock, and the pooled pursuit|P42]]), when both targets exist.

For the confidence the PI wants (`ROADMAP.md`, row 4), tests should either have a declared gold, as W1 did, or declare a
family of targets and register the interval.

## 8. What the new tools are worth, after P51

The PI asked whether the framework is gaining tools for free, or the perception is biased; whether it is near the
frontier; and how far it can be pushed, on the theoretical side as well as on the engineering side.

**The theoretical side.** The gain is real, and its cause is identifiable. One identity, the chain rule of KL with its
Pythagorean form for I-projections ([[P4 — What KL measures|P4]](iii), [[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]]), gives every exact split the framework has: pursuit and
misalignment ([[P6 — The departure from the default splits into pursuit and misalignment|P6]]), avoidable and unavoidable ([[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]]), named and unexplained ([[P44 — What named objectives explain|P44]]), shared and drift ([[P45 — Drift: what runs share, and what they do not|P45]]),
reproducible and run-specific ([[P46 — What runs share between conditions, and what they do not|P46]]), outer and strict inner ([[P49 — Outer and inner misalignment|P49]]), world and tampering ([[P50 — Tampering: a change of the measurement, not of the world|P50]]). Partial
identification ([[D9 — Observation and identification|D9]]) gives every interval: an unobserved condition ([[P17 — What an unobserved condition can hide|P17]]), an uncertain target ([[P48 — Misalignment when the target is uncertain|P48]]), tampering from
signals ([[P51 — What signals, audits and re-measurements reveal of tampering|P51]]). The core did not grow to give them: five premises and eleven definitions since v11. That is the
expressiveness a minimal, compelling core should have, and alignment's usual vocabulary, where reward hacking, goal
misgeneralization, deceptive alignment and wireheading are each defined on their own and informally, does not have it.
Three cautions keep the claim honest. The mathematics is classical, so the novelty, if any, is in the choice of objects
and the readings, not in the theorems. Each new tool moves difficulty into a declaration (a target, a family, a channel,
named objectives, runs) that the framework requires and cannot supply. And whether the synthesis is new is unverified:
the literature cannot be searched from here (D10, D11), and no mathematician other than the executor has read the
proofs, while grading one's own framework generously is a recorded failure (§1). So: a strong candidate for a unifying
formal language of alignment evaluation, to be called frontier only after a literature check and an outside reading. The
theory's open edges are continuous outcomes, estimation guarantees in outcome spaces too large to count, actors that
respond to the measurement itself (H34), and tampering over time.

**The engineering side.** One of three framework predictions held on data not seen before (`RECORD.md`). Of the nine
diagnostics, five were used in a case, all in W4: [[P43 — Misalignment at any intensity|P43]], [[P44 — What named objectives explain|P44]], [[P45 — Drift: what runs share, and what they do not|P45]] and [[P47 — The cost of reweighting|P47]] in its registration, and [[P48 — Misalignment when the target is uncertain|P48]] after its
verdicts; [[P46 — What runs share between conditions, and what they do not|P46]], [[P49 — Outer and inner misalignment|P49]], [[P50 — Tampering: a change of the measurement, not of the world|P50]] and [[P51 — What signals, audits and re-measurements reveal of tampering|P51]] in none; tampering was zero by construction in W1–W4, whose evaluators were
fixed functions of the text. The roadmap's rule, new results only when a test needs one, has been set aside, with the
PI's approval, for four results in a row ([[P48 — Misalignment when the target is uncertain|P48]]–[[P51 — What signals, audits and re-measurements reveal of tampering|P51]]); that would be the recorded failure "internal refinement over
external contact" (§1) if the next steps were not external. They are: the two tests of Q32, then the tampering
simulation.

## 9. What the framework can import, after the survey of 2026-10-07 (Q33)

The PI asked which frameworks or theories the framework can import from. A web search found the sources below; their
records and abstracts were read, not their full texts, since arXiv and the publishers are not reachable from here (D12).
Each is filed in `RELATED.md` under its theory, with what it shares with the core and what it would add. Ranked by what
each would add to the steps now open:

| # | Source | What it gives the framework | Into | Kind | When |
|---|---|---|---|---|---|
| 1 | White (1982); Vuong (1989): misspecified models | the revealed intensity is White's pseudo-true parameter, so his limit theory gives intervals for `t*` and the quantities at it; Vuong's test says which of two specifications fits an actor better, and should give the limit of `2n·M(p̂_n)` when `M > 0`, which [[P23 — The estimated misalignment of an actor that pursues the objective\|P23]] lacks | [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits\|P5]], [[P23 — The estimated misalignment of an actor that pursues the objective\|P23]], [[P44 — What named objectives explain\|P44]], [[P48 — Misalignment when the target is uncertain\|P48]], [[P49 — Outer and inner misalignment\|P49]]; the estimation work | theorems and a test | now |
| 2 | Chatterjee and Diaconis (2018) | reweighting needs about `e^{KL}` draws, necessary and sufficient | [[P47 — The cost of reweighting\|P47]], every diagnostic computed by reweighting | theorem | now |
| 3 | McAllester and Stratos (2020) | with one behaviour known and the other sampled, no distribution-free lower bound on the divergence above `ln N`; the same for mutual information (read in full, Q34) | the estimation work; the limit of H33 | theorem | now |
| 4 | Kwa et al. (2024) | a KL penalty protects the target against a light-tailed evaluator error and not against a heavy-tailed one | the general core, for outcomes that are not finite | theorem | now |
| 5 | Baker (2002); Courty and Marschke (2008) | a measure's distortion and risk, against [[P50 — Tampering: a change of the measurement, not of the world\|P50]](iii)'s split of the misaligned share into world and noise; a test of distortion from how a measure degrades once it is paid on, a candidate world design for [[P20 — Where overoptimization starts, and how it ends\|P20]] | [[P11 — The misaligned share at the start of a change\|P11]], [[P50 — Tampering: a change of the measurement, not of the world\|P50]]; step 2 | correspondence and a design | now, if the texts and data are open |
| 6 | Baker et al. (2025) | a monitor trained against hides the intent it was meant to catch, at high optimization strength | H34; case C3's second arm | evidence | now |
| 7 | Polyanskiy and Wu (2025) | divergences on general spaces, and their variational forms | the general core | textbook | now |
| 8 | Ben-Tal et al. (2013): robust optimization over divergence balls | the dual of the worst case for every divergence ball, and its radius from data | [[P17 — What an unobserved condition can hide\|P17]], [[P27 — The best use of a departure budget\|P27]], [[P31 — Budgets of other shapes\|P31]] | method | later |
| 9 | Pearl and Bareinboim (2014): transportability | when what is seen in evaluation carries to use | [[P17 — What an unobserved condition can hide\|P17]], [[P24 — The evaluation gap\|P24]], [[P46 — What runs share between conditions, and what they do not\|P46]] | assumptions with criteria | later |
| 10 | Blackwell (1953): comparison of experiments | sharper identified sets for views | [[D8 — Conditions, responses and views\|D8]], E5 | theorem | later |
| 11 | Kong and Schoenebeck (2019): elicitation without verification | information measures that obey data processing, for reports with no ground truth | [[P51 — What signals, audits and re-measurements reveal of tampering\|P51]]; H33 if gap 5 reopens | theory | later |
| 12 | Zhuang and Hadfield-Menell (2020) | when optimizing a proxy that omits attributes drives utility arbitrarily low | [[D10 — Evaluator, regression and residual\|D10]]'s residual, [[P29 — The width is the exact worst case\|P29]] | theorem | later |
| 13 | Carroll et al. (2024): influenceable rewards | an actor that changes the principal's target, outside [[P50 — Tampering: a change of the measurement, not of the world\|P50]] | a scope question | theory and a warning | later, if the scope widens |

Two readings of the list. The imports with most weight are statistical, not about alignment: the core's quantities are
divergences from a misspecified family, and the statistics of such fits, of reweighting and of what samples can certify
is mature, so the estimation work is mostly import. And several alignment results map onto existing items rather than
adding new ones (Baker on [[P11 — The misaligned share at the start of a change|P11]] and [[P50 — Tampering: a change of the measurement, not of the world|P50]], Baker et al. on H34, Everitt et al. on [[P50 — Tampering: a change of the measurement, not of the world|P50]] and [[P51 — What signals, audits and re-measurements reveal of tampering|P51]]), which is what a
framework meant to be imported into should find.


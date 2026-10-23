# NOTES — the executor's working notes

Not part of the core, and not checked by lint. Blunt on purpose. A hunch is not a claim: nothing moves into `CORE.md` or
`derived/` without a proof and a check. Names, and correspondences with the literature, with their confidence levels,
live in `TERMS.md`.

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
| **Correcting the ledger, not the prose that repeats it** | the v7.3.3 review found prose three versions behind the ledger; again after the merge of pull request #33 (2026-10-11): the first bullet of `ROADMAP.md`'s "Where we are" was changed to say that v13 is on `main`, and the next bullet, which said that `main` holds v12, was left; found in the next turn | a status change is a retraction for search purposes: search the old wording everywhere |
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
| **A check that omits the constraint it tests** | the ray-minimizer check never required `t* ≥ 0`; a mutant that pursued `−F` passed. Again in [[P55 — What a record of counts certifies, at every size\|P55]]'s first check (2026-10-11): the ordinal level was checked only through the final bound, loose at those sizes, so a mutant that judged the ordinal specification by the standard misalignment passed; the check now asserts the step of the proof, that every intended behaviour is at least as far from every count vector as its misalignment | mutation-test every new check before recording it: break the mathematics on purpose and watch it fail |
| **A mutant caught by a crash** | the first mutant list of [[P53 — Misalignment is the departure beyond what the family of targets credits\|P53]] (2026-10-11) restricted a minimization to one direction with a gradient of the wrong shape; the check failed with a `ValueError`, counted as "caught", though no assertion had judged the mathematics. Again the same day, in lint R17's list: a mutant that added a string to a set raised a `TypeError`; rewritten, an assertion catches it | read why each mutant is caught: an error raised by the mutated code itself tests nothing, so rewrite the mutant until an assertion fails |
| **A push without the steps before every push** | C5's registration (2026-10-11) was committed and pushed with lint run but without regenerating `OVERVIEW.md` and `obsidian/`, which the NOTES and ROADMAP edits had made stale; CI run 241 failed on their freshness, and run 242, with them regenerated, passed. The registration's hash did not change | the block of `CLAUDE.md`, "Before every push", runs whole even for a push that only registers a case: a push meant to fix a moment in time is still a push |
| **A tolerance without its scale, again** | the ray-closedness check compared a tight bound with no rounding margin (1.79134602e-43 against itself) | every comparison gets the relative margin of `EXACT`, including the "obvious" ones |
| **A justification leaning on a later result** | D3 cited P5 while P5 came after it; lint rule R5 caught it. Again in the draft v13 (2026-10-10, §16): [[A4 — Misalignment is evidence\|A4]] and [A6] were first argued from [[D11 — Record, sample and evidence\|D11]], [[P21 — The expected evidence is misalignment\|P21]], [[P24 — The evaluation gap\|P24]] and [[P36 — Ordinal objectives\|P36]], built on [[D3 — Specification, declaration and misalignment\|D3]], which cites [A6]; R5 found seven cycles. Again in v13 as built (2026-10-11, §17): [[D1 — Outcomes, behaviours, divergence and tilt\|D1]]'s Interpretation cites
[[M2 — Independent repetition|M2]], and [[M2 — Independent repetition|M2]]'s reason cited [[D1 — Outcomes, behaviours, divergence and tilt|D1]]; R5 found the cycle | keep R5; write the "why" from what is above; evidence that uses
later results goes in Notes |
| **A check helper that misclassifies at the edge of float64** | at intensity 40, the coarse actor's mass off the best outcome (about `1e-34`) vanished from its mean of `F`; the helper took the "all mass on the best outcomes" case and returned `+∞`; again in W1's report, where the matched pursuit at an intensity near `10³` underflowed to zeros and the under-pursuit of 9 prompts read infinite; and in [[P50 — Tampering: a change of the measurement, not of the world\|P50]]'s check, whose small-intensity ratio of two divergences near `10⁻⁹`, each a sum that cancels to that size, erred by `10⁻⁷` at intensity `10⁻³` and by `2.5·10⁻⁵` at `10⁻⁴`; and in the library itself, whose revealed intensity takes the best-outcomes case within `10⁻¹²` of `max F` and returns `M = ∞` for an actor of full support, in the regime that the checks of [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits\|P5]] and [[P9 — What is at stake\|P9]] skip (§15, point 3) | keep check instances where float64 represents every mass; test limits by their own formula; compute a divergence to a tilt in closed form, with `log E_q[e^{tF}]` by log-sum-exp; a regime that a check skips is one the library either refuses with an error or computes another way, with a test there |
| **A familiar formula that hides a typing error** | "the KL-regularized optimum is `tilt(π_ref, r/β)`" is true prompt by prompt, and false on prompt–response pairs: the pursuit ray of [[D2 — Pursuit of an objective\|D2]] would also reweight the prompts, which no policy can do. Found only when the ontologies had to say what an outcome is | typed slots in every ontology, including **contexts**; a formula from the literature enters only with its outcome space stated |
| **A probe bug read as a refutation** | the first probe of [[P15 — Misalignment splits into what the actor could avoid and what it could not\|P15]] for policies used `log E[e^V]` over the environment (the optimistic recursion of control as inference) and found the split off by 5 nats; the derivation said the projection averages over the environment, and with that the split was exact. The same slip, from the other side, in the grounding probe (Q32): the best grounded behaviour was first written with `log E_K[e^{t·F̂}|w]`, the trainer's optimum's own weights of worlds, where an actor that cannot touch the channel faces its average, `E_K[F̂|w]`; the numerical projection disagreed by `0.37`, and the derivation was redone | when a probe contradicts a derivation, check each against the other before concluding anything; what the actor cannot control enters by its average, not by its log-mean-exp; the slip is now a mutation in [[P50 — Tampering: a change of the measurement, not of the world\|P50]]'s check |
| **A rule test passing because another rule fired** | the lint tests for "numbers increase" and "a core Statement may not use a result" passed only because a duplicate id and a cycle fired too; both mutants survived | each rule test isolates its rule, or asserts its rule's own message; mutation-test the linter as well as the checks |
| **A degenerate random instance hiding the property** | the first check of [[P16 — An actor cannot behave more differently than it can tell conditions apart\|P16]](i) moved mass between two inputs, one of which had almost none, so the two conditions barely differed (KL 1e-5). Again in [[P53 — Misalignment is the departure beyond what the family of targets credits\|P53]]'s first check (2026-10-11): with `d` statistics on `d + 1` outcomes, the behaviours with given averages are a single point, so "another behaviour with the same averages" was not one; its own assertion caught it | build the instance so the property has something to show (here KL > 0.3), and assert that it does |
| **A plain-terms twin that claims more than the statement** | [[P19 — A monotone regression rules out overoptimization\|P19]]'s plain terms listed threshold selection among the covered paths; a threshold leaves `Δ°`, so the statement does not cover it (the conclusion holds there by a direct argument). Found in the review before the v10 commit. Again in v13 (2026-10-11): [[P55 — What a record of counts certifies, at every size\|P55]]'s plain terms said its test needs no model of how the actor decides, though its level needs independence, and that exact alignment can never be shown, false when every behaviour is accepted; [[P54 — Dependence and drift only add evidence\|P54]]'s compared the evidence with what the counts show rather than with the misalignment of the average behaviour | read each "In plain terms" against the Statement's hypotheses, one named example at a time |
| **A rate copied from a sketch** | [[P22 — No test detects misalignment faster than misalignment\|P22]]'s Notes said the Chernoff bound is approached like `1/log(1/ε)`; a computation across seven decades of `ε` showed `log log(1/ε)/log(1/ε)` | a rate in a Note is computed across several decades before it is written |
| **A check whose instance generator kills the case it tests** | the first single-peaked regressions of [[P26 — The regression on bins governs at small intensity\|P26]]'s check capped the falling part at the peak, so every "falling" part was flat; a mutant claiming monotone curves survived until the counts were printed | assert that the hypothesis is visible in the instances (here: some curves do fall), as the failure mode on degenerate instances already asks |
| **A concept that is trivial in the typical case** | the regression of [[D10 — Evaluator, regression and residual\|D10]] is the target itself whenever the evaluator gives distinct outcomes distinct values, the usual case for reward models and fitness; noticed only when filling the ontologies' evaluator slots, after [[P18 — Through the evaluator, only the regression counts\|P18]]–[[P20 — Where overoptimization starts, and how it ends\|P20]] were proved and checked on instances built with ties | build check instances from the typical case as well as the interesting one, and fill one ontology before a new definition is final |
| **A result silent on its specification** | [[P24 — The evaluation gap\|P24]] said "the misalignment in deployment" without naming the specification on condition–outcome pairs; under one shared intensity its formula fails in 173 of 200 instances | every result over several conditions names the specification on pairs |
| **Lineage amnesia after a restart** | [[P13 — What the start of a change gains\|P13]](ii) re-derived v7.10's B §4 (the gold slope `√2·ρ·sd` per `√KL`) and Prop 14 without crediting them; found only in the retrospective after v9. Again in the review of 2026-10-10 (§15, point 1): its finding that misalignment charges an optimizer's route re-found v7.10's H8, item 2 of its review of v7.3.3 and the identification rule of its brainstorm B1, none of which the restart had carried over; found when the PI asked for the hunches of past executors to be read | before adding a result, search v7.10 (`git grep -i <idea> v7.10`) for its counterpart, and cite it in the Lineage; before a finding of a review, too |
| **A data claim written from memory** | the industrial-organization ontology gave the German price archive the licence CC BY 4.0, the live feed's; by secondary sources the archive is CC BY-NC-SA 4.0, for non-commercial use. Found only when the PI asked which specification the public data can test | a Data paragraph says where each claim about licence and access comes from, and says so when the primary source was not reached |
| **An intervention dated with the quantity it tests** | the known result dates adoption partly by the speed of a station's response to its rival, a dependence between the stations; a test of coordination before and after those dates would have been partly true by construction. Caught before registration | before registering, list how every intervention or group is defined, and drop any marker that measures the outcome tested |
| **A threshold without its scale, in a registration** | case C2's verification required a recovery of `0.999` on a grid of step `0.05`, while a third of the peaks came before `t = 0.5`; and S1 scored the rule against the best of 32 noisy training runs, so its threshold measured luck. All three predictions failed; the exact pursuit on S1's own grid would have reached only 79%; again in L1 (2026-10-14, §21): the outer misalignment of an order-preserving evaluator at intensity `1` was registered against an absolute threshold of `10⁻⁶`, and came out `2.9·10⁻⁷`, since at that intensity the trainer's optimum is almost wholly on the best outcome; positive as [[P49 — Outer and inner misalignment\|P49]](i) proves, but unresolved by the registration, so a failed prediction | before registering, compute every threshold on the design's noise-free case, with seeds the test will not use, and score against what the design can reach, not against the luckiest run |
| **A run lost at its last step** | W1's report computed 35 minutes of per-prompt results and crashed in its final aggregation, a bootstrap indexing all 1,000 prompts over a list of 994; nothing had been saved | save per-item results (outside the repository) before aggregating, and aggregate in a function that can be rerun on them |
| **A speed never measured** | W3's first launch was estimated at seconds per context and took about 50: the sampler recomputed every sequence at every token, and a second heavy job shared the processors. It was stopped before any context finished; a cached sampler in double precision, checked against the scorer, replaced it | before launching, time one context of the registered size on a made-up input, alone on the machine |
| **A registered statistic that the design's mixture inflates** | W3 pooled, within each prompt, 32 continuations of the reference and 32 of the tuned model, and registered the `R²` of the revealed objective on the reward over all 64. The two sets differ by 16.5 nats on the objective and also on the reward, so most of the registered `0.358` comes from that difference; within either model's own continuations it is `0.10` to `0.12`. The verdict (refuted) stands, but the registered number understates the refutation, and a model whose change were pure pursuit of something correlated with the reward across the two sets could have passed S1 | before registering a statistic on a sample that mixes sources, compute it on each source alone in the calibration, and register the one that answers the question |
| **A tie-breaking order charged as departure** | W1's report broke ties in the proxy's score by one fixed random order, as `run.py` does for the gold curve, where it changes nothing in expectation. A divergence is convex, so a fixed order adds itself to the departure and to misalignment: on a synthetic prompt with a tied block near the top, `KL` at `n = 16` was `1.84` instead of `1.40` nats. Caught on re-reading the report's declaration ("it scores nothing else alike", which was also false), halfway through the third computation | compute a divergence on the behaviour averaged over its tie-breaking, which by symmetry is uniform within each tie; check it against a simulation of the selector |
| **Saving the estimates, not the data behind them** | W4 saved, outside the repository, each context's estimates but not the per-draw log-probabilities and rewards, so an analysis needing no reweighting, how far one run's draws move along the other's revealed objective, needed a second run of 2.2 hours | save every per-draw value before aggregating; the template now asks for it |
| **A specification with no named principal** | W3 and W4 declared as the target the reward the policy was trained on, the evaluator itself, while the machine-learning ontology's specification asks for a gold objective distinct from it; the executor declared it, for no principal in particular. What they measured is misalignment against the trainer's formal objective, and their texts said "misalignment" without saying whose. Caught by the PI | name the principal in the declaration; when the target is uncertain, declare the family of targets and report the interval it gives (§7) |
| **An optimum taken from a solver's word** | the first check of [[P51 — What signals, audits and re-measurements reveal of tampering\|P51]](i) ran the EM iteration a fixed number of steps and compared its value with the bound: 20,000 steps left gaps near `3·10⁻⁸`, and 50,000 left `10⁻⁶` where the minimum is `0` with more worlds than signals | certify a computed optimum by a bound that holds at any point, here `log max_w c(w)`, and test claims against the bracket, not the point |
| **An abstract read as the theorem** | the import survey (§9) read McAllester and Stratos from their abstract, as a limit of `log N` on what samples certify about information, and inferred what it says of misalignment; their Theorem 3.1 holds with one behaviour known and the other sampled, a lower bound on `KL(known‖sampled)`, which is the reverse of misalignment's sampling. Caught on reading the text, once arXiv was reachable (Q34) | quote a theorem's hypotheses, not its abstract, before inferring from it; D12's rule, applied to readings as well as to imports |
| **A search result's record taken for the paper** | asked for Vuong's working paper 605, the executor gave the PI the link of a Caltech record found by search, which was Lien and Vuong's working paper 606; the title showed only once the record was fetched (2026-10-08). Again on 2026-10-10: the answer on the licence's aim (Q50) passed on nine links found by web search, on licences and on copyright in AI-written text, without opening them; when they were then fetched for these notes, their hosts were not allowed, so §11 says that those facts come from search results and that the primary pages were not read | open a record and match its title and authors before citing or passing on its link; when the host is not reachable, say so with the link, or ask the PI to allow it |
| **A rule about sources applied forward only** | Q36 (an imported theorem is read in a text anyone can read without paying) was applied to the citations made after it. [A2] and [[D2 — Pursuit of an objective\|D2]] still rested on Čencov's theorem, cited only from a monograph behind a paywall that was never read here, and the review of 2026-10-08 (§12), which read `CORE.md` in full, did not catch it. Found on 2026-10-09 while writing the overview (H1): the statement is now read in Lê's and Ay et al.'s open texts, and Gibbs' and Pinsker's inequalities ([[P4 — What KL measures\|P4]], [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits\|P5]]) in Polyanskiy and Wu's draft. A sweep by script then found seven more sources, cited in the Statement, Proof or reason of nine items, that no record says were read (`ROADMAP.md`, step 8, done the same day, Q44) | a new rule about sources comes with a sweep, the same day, of every existing citation in a Statement, a Proof or a reason, by script, and a row for each one it leaves open |
| **A result's hypothesis dropped in the code that applies it** | [[P23 — The estimated misalignment of an actor that pursues the objective\|P23]]'s χ² law holds at an interior intensity, and its Notes and proposal E1 (§3.3) name the χ̄² law at `t = 0`; `stdalign`'s `from_counts` returns the interior law's p-value at every intensity, so an actor at the default, which the standard specification intends, is rejected at a nominal 5% in up to `10.3%` of samples. The library's checks passed, since they test the law where it holds. Found by the review of 2026-10-10 (§15, point 4) | a function that applies a result checks the result's hypotheses on its input, and switches law or says so where they fail; its tests include an input where a hypothesis fails |
| **A hypothesis dropped in the Notes** | [[P55 — What a record of counts certifies, at every size\|P55]]'s Notes (2026-10-11) said that for an actor whose decisions depend on each other the counts estimate `M(p̄)`, and [[P54 — Dependence and drift only add evidence\|P54]]'s that [[P55 — What a record of counts certifies, at every size\|P55]] certifies `M(p̄)` with no assumption on how the actor decides; [[P54 — Dependence and drift only add evidence\|P54]](iii) gives only that the counts estimate `p̄` without bias, and [[P55 — What a record of counts certifies, at every size\|P55]]'s level needs independence: a Markov chain whose average is intended is accused in `17.9%` of records at `α = 0.05` (`probes/review/p55_dependence.py`). The same Notes quoted Sanov's theorem for every closed convex set, though the source, read that day, asks for a non-empty interior, and [[P53 — Misalignment is the departure beyond what the family of targets credits\|P53]]'s Notes built a reading on it that fails for a span. The proofs and the checks were right; the sentences around them were not. Found by a subagent of the executor's, asked to read [[P53 — Misalignment is the departure beyond what the family of targets credits\|P53]]–[[P55 — What a record of counts certifies, at every size\|P55]] before the pull request, not independent (rule (f)). Again in the general core's new results (2026-10-11, §20): the dimension law's hypotheses dropped where GD3 and GD11 cite it, and its grid stated so that it did not cover the space; the τ-topology named where a nearness gives weak convergence; "aligned within `ε`" said never to be verifiable, without the finite case. Found by a subagent's reading of the proofs, the second time this check has found what the executor's own reading missed. Again in v14's draft (2026-10-15, §23), before its push: a set cut out by non-strict inequalities called open (VO3(iii)), so that a shortfall by a margin was called verifiable when it is not, and that shortfall read as a case of "worse"; VO3(ii) without the hypothesis its proof uses; a probe's example cited for dependence that showed only the ray's lack of convexity; and instance counts printed as planned rather than as checked (19 of 30 for VK4). Found by a subagent's adversarial reading of the proofs, the third time. Again in `v14/factorization.md` and `v14/LIMITS.md` (2026-10-16, §26), before the push: VF3 stated for every record what holds for samples; "culpable" called verifiable without the interface taken as known; a limits file, whose header promised only proved limits, stating hunches and a brainstorm as proved; the fourth time. Again in v14's claims of generality (2026-10-16, §28): VK0 matched a budget the definition excludes, a ball claimed to need infinitely many budgets that does not, and "forced" said where four choices were hidden; the fifth time | a sentence of the Notes that draws a consequence names the hypothesis its proof uses, and is read against the Statement and the source as the proof is; a new result's Notes are reviewed with its proof, not after it |
| **A label that claims a minimum its split does not prove** | [[P15 — Misalignment splits into what the actor could avoid and what it could not\|P15]](v) splits misalignment exactly into `KL(p̂‖p*°) + KL(p*°‖p°)` and calls the second term the unavoidable misalignment; it is unavoidable only toward `p°`, the intended behaviour nearest to the actor's, at its revealed intensity, and a feasible behaviour aimed at another intensity can do better: on 109 random instances with one fixed average, the term exceeded the least misalignment of any feasible behaviour in 107, by up to `0.86` nats (`probes/v14/factorization.py`, 2026-10-16). The split, its proof and its checks were right; the word said more. Found by the executor while proving v14's factorization at the PI's request (Q62), two versions after the item was written | a label that says "unavoidable", "least" or "best" names the set it is least over, and a check compares it with a search over that set |
| **A long job started with `&`** | twice the executor started a long job with a shell `&` instead of the harness's background run, against `CLAUDE.md`: once in the work of Q56, when the job was stopped by its PID and relaunched, and again on 2026-10-16, for the probe of `v14/factorization.py`, which was left to finish and its output read from its file; a third time on 2026-10-21 (Q71), the gated test run and push of §33.13, started with `&` inside a compound command; it completed and pushed, and was waited on by its completion | a long job is started only as a background run of the harness, and waited on by its completion |
| **Editing the tree during a gated test run** | on 2026-10-16 the executor edited `v14/constraints.md` while the tests that gate a push were running on the working tree; the check that every Markdown source is wrapped read the half-edited file and failed, and the push did not happen. The commit itself was wrapped | while a gated run is in progress, the working tree is not touched; edits wait for its result |
| **A result applied outside its hypothesis** | on 2026-10-17 (Q69) the draft of `v14/severity.md` and `v14/training.md` read VK7, which holds the actor fixed, as saying how a trainer's budget moves the evidence against the actor it trains, which changes with the budget, and called the trainer's and the bettor's prices "two prices of one budget", which are never both positive for one actor and one budget; RS5(iii) said that coarsening a resolution shrinks the feasible set, which needs the environment's splits to be consistent. Caught by the adversarial review of §32 before any push | before a result is used in a proposal or a gloss, write its hypotheses beside the use, and check that the use keeps every one |
| **A gloss written from the intended meaning, not from the formula** | the same day: SH1's middle term glossed as "what the feedback costs by rewarding behaviours the principal does not accept", where it is positive exactly when the feedback leaves out every best feasible behaviour; VK6's plain terms "more where it breaches more", false once the nearest rate passes ½; VK4's Notes "no exact attribution exists", where one exists along a chosen order. Caught by the same review | derive each gloss from the formula, with one instance that would make it false, before writing it; the fifth row of this table's kind, after "A plain-terms twin that claims more than the statement" |
| **A formula checked, its source not read** | on 2026-10-18 (Q70) the executor checked the research assistant's formula for Carcassi and Aidala's fraction capacity, `sup_{a∈A} exp(−D_∞(a‖p))`, for one acceptable behaviour, and wrote in §33.10 and H58 that it "needs no convexity", without reading the book's definition, which takes the hull (Definition 4.173); the reading of the book the same day found it | before a formula is attributed to a source, read the source's definition, not only the formula's proof; the third row of this table about reading the source, after "An abstract read as the theorem" |
| **A PI's question answered in the notes, never carried into the files** | the PI asked on 2026-10-17 (Q70) whether conditions and outcomes could be one distribution; §33.2 answered, H53 recorded it, and Q74 decided it (§33.17, item 5), but `v14/` and the slides kept conditions as a type until Q76, and the PI, reading the files, could not find the answer. The same for "declare" defined in one line (§33.8), never written into `v14/`. Found by the PI (Q76); an audit of all 44 of the PI's prompts found no other ask lost, and two left waiting without the PI being told (§34) | an answer to a PI's question ends in the file the PI reads for that subject, or the turn's answer says where it waits; at each handover, read the PI's prompts against the tree |
| **A verdict assumed for every kind of requirement** | §33.15, §33.17 and H51 put a certify verdict beside the convict verdict for per-decision requirements, the obstacle named as dependence; it is not dependence: two actors that differ at one decision, fixed in advance and independent of everything, cannot be told apart well enough to certify that every decision was acceptable, so only an average is certifiable (`v14/LIMITS.md`, Q76). Found by the executor when an external review asked for H51 to be proved | before claiming a verdict exists for a class of requirements, try the actor that changes one decision |
| **A strict change claimed where the result gives a weak one** | in `v14/junctures.md` (Q77) the executor wrote that refining the record makes visible misalignment rise and hidden fall, that refining the principal makes misalignment rise, and that new actions make unavoidable misalignment fall, where RS1, RS6 and the definition as an infimum give only "does not fall" or "does not rise", and the principal's case needs the finer acceptable set inside the coarser; and cited H55, about honeypots, for the worst case. Found by a reviewing subagent (Q78) | a monotone result is written with its weak inequality, and with the inclusion it needs |
| **A closed form proved for a case it does not cover** | v14's VK6, an overall rate limit with the conditions' law fixed, solved for each condition's breach rate as if it could take any value in `[0, 1]`; a condition all of whose outcomes lie in `C` forces it to `1`, and then the closed form gives a finite number where no acceptable behaviour exists. Found when the MVP's library, solving the same problem by linear programming, disagreed on a random instance (Q80, 2026-10-23); the hypothesis added to VK6 and to the MVP's R10 | test a closed form against a general solver on random instances that include the degenerate ones, not only the generic |

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
"will not" ([[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]]); conditions, views and identification make deceptive alignment a measurable quantity ([[P16 — An actor cannot behave more differently than it can tell conditions apart|P16]], [[P17 — What an unobserved condition can hide|P17]]);
and a reporting standard names every definition (`STANDARD.md`, lint R11).

v10 added the two concepts approved after the retrospective (§5): the evaluator ([[D10 — Evaluator, regression and residual|D10]]), from which the Goodhart results
of v7.10 are derived ([[P18 — Through the evaluator, only the regression counts|P18]]–[[P20 — Where overoptimization starts, and how it ends|P20]]), and sampling ([[D11 — Record, sample and evidence|D11]]), which gives misalignment its second meaning as a rate of
evidence and brings detection, estimation and the evaluation gap ([[P21 — The expected evidence is misalignment|P21]]–[[P24 — The evaluation gap|P24]]). The core holds five premises and eleven
definitions. Since then the import of v7.10 added [[P27 — The best use of a departure budget|P27]]–[[P38 — Any convex cost|P38]], [[L1 — Separable bounds are loose when two quantities change rank|L1]] and the forbidden statements ([[C1 — No ranking of errors holds at every budget|C1]]–[[C12 — No misalignment, no stakes|C12]]).

v11 widened the scope to groups and several principals with declared weights ([[P39 — Several actors: coordination plus individual misalignment|P39]]–[[P42 — Several principals: gridlock, and the pooled pursuit|P42]]), and the framework met data
for the first time: W1 tested the machine-learning prediction from [[P13 — What the start of a change gains|P13]] on answers no one had scored, and refuted it
(`cases/w1-best-of-n-slope/`); W3 tested the bet itself, on a public model tuned by PPO, and it held in part: the model
pursues its reward in the reward's own scale, but most of what the tuning changed is not that pursuit
(`cases/w3-ppo-pursuit/`). One of three predictions held. The finish line's prediction row is met; the row for a worked
case run by an outside reader is not: W1 is reported to `STANDARD.md`, and the readers are requested (`REQUESTS.md`,
R1), the hold on review having been lifted for one mathematical reader (Q33). Since then: nine diagnostics
([[P43 — Misalignment at any intensity|P43]]–[[P51 — What signals, audits and re-measurements reveal of tampering|P51]]), the law of estimated misalignment by access ([[P52 — What a sample certifies about misalignment, by access|P52]]), a diagnostic case (W4), a library (Q37), and a
reader package (Q41). v12 made [A2]'s geometry Riemannian, as Čencov's theorem requires (Q44). Where the framework
stands, and what comes next, is kept in `ROADMAP.md`; this table keeps the gaps the core has closed.

| Gap | State |
|---|---|
| sensitivity, resolution, stakes, the gain of a change | closed in v8: [[P7 — Indifference forgives exactly what happens inside cells\|P7]]–[[P10 — Sensitivity to the specification\|P10]], [[P13 — What the start of a change gains\|P13]] |
| the KL cost was assumed | **closed by [[P14 — The cost of departing from the default is forced\|P14]]**: forced by [A2] and [A3] together |
| "cannot" versus "will not" | **closed by [[P15 — Misalignment splits into what the actor could avoid and what it could not\|P15]]** for linear and convex limits; for capacity limits only a lower bound |
| contexts (v8 design question Q1) | **closed by [[P15 — Misalignment splits into what the actor could avoid and what it could not\|P15]]**: the shared intensity across contexts is derived, not chosen |
| deceptive alignment | **opened as a measurable quantity**: [[D8 — Conditions, responses and views\|D8]], [[D9 — Observation and identification\|D9]], [[P16 — An actor cannot behave more differently than it can tell conditions apart\|P16]], [[P17 — What an unobserved condition can hide\|P17]]; bounds on the objective's average in an unobserved condition, sharp given `ε` |
| a standard for reports | **closed by `STANDARD.md`** (lint R11) |
| no estimation layer | **closed in part by [[P23 — The estimated misalignment of an actor that pursues the objective\|P23]] and [[P52 — What a sample certifies about misalignment, by access\|P52]]**: the law of estimated misalignment on the ray ([[P23 — The estimated misalignment of an actor that pursues the objective\|P23]]) and off it, by what is known of each draw ([[P52 — What a sample certifies about misalignment, by access\|P52]]), with the revealed intensity's; the boundary `t* = 0` and confidence sets for the other quantities (the pursuit part, named misalignment, [[P48 — Misalignment when the target is uncertain\|P48]]'s interval) are open, and bootstrap intervals for them under-cover near zero (`probes/examples/`) |
| no theory of what optimizing a proxy does | **opened by [[D10 — Evaluator, regression and residual\|D10]]**: [[P18 — Through the evaluator, only the regression counts\|P18]] (only the regression counts), [[P19 — A monotone regression rules out overoptimization\|P19]] (a monotone regression rules out overoptimization), [[P20 — Where overoptimization starts, and how it ends\|P20]] (where it starts, how it ends) |
| detection, and the gap between evaluation and use | **closed by [[P22 — No test detects misalignment faster than misalignment\|P22]] and [[P24 — The evaluation gap\|P24]]** |
| the regression of a real-valued evaluator | **closed in part by [[P26 — The regression on bins governs at small intensity\|P26]]**: on finitely many outcomes it is the target itself; the regression on bins governs the pursuit up to `t·w·D/4`. Best-of-`n` with bins is open (E8) |
| the shape of the overoptimization curve | **closed by [[P25 — The target's curve turns no more often than the regression\|P25]]**: the target's curve turns no more often than the regression; a single-peaked regression gives at most one fall, for pursuit and best-of-`n` |
| several actors, several principals | **in scope since v11**: a group as one actor ([[P39 — Several actors: coordination plus individual misalignment\|P39]]), several principals with declared weights ([[P42 — Several principals: gridlock, and the pooled pursuit\|P42]]) |
| what a measured misalignment is made of | **opened by the diagnostics** [[P43 — Misalignment at any intensity\|P43]]–[[P51 — What signals, audits and re-measurements reveal of tampering\|P51]]: the intensity at which it is judged, named objectives, drift between runs, the cost of reweighting, a family of targets, outer and inner misalignment, tampering |
| worked cases | **opened**: W1 and W3 on unseen data (one prediction held of three), W4 a diagnostic case, W1 reported to `STANDARD.md` and as data; C1 and C2 in simulation (`cases/`); a case on simulated data any reader can rerun (`examples/quickstart.py`); no outside reader yet |
| a library for the standard's quantities | **opened** (Q37, Q41): `stdalign` 0.2, misalignment, its split, its estimates by access and the diagnostics [[P43 — Misalignment at any intensity\|P43]]–[[P51 — What signals, audits and re-measurements reveal of tampering\|P51]], on which their checks run, and the validator of reports as data; stakes, the evaluator's results and feasibility to follow (`ROADMAP.md`, E1(c)) |
| imported theorems read in open texts (Q36) | **closed** (Q44): every theorem a Statement, Proof or reason imports is read in an open text or derived where it is used; `REFERENCES.md` says which |

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
| Q7 | sampling in the core | PI: inclined to yes, as a universal act of measurement that the framework must interpret and can use for explanations; executor: yes, as definitions only (§5.6); PI: approved | [[D11 — Record, sample and evidence\|D11]]; [[P21 — The expected evidence is misalignment\|P21]]–[[P24 — The evaluation gap\|P24]] |
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
| Q35 | how does the framework relate to cooperative inverse reinforcement learning and its variants, and is a request made with poor consideration ("get rich", ethically taken for granted) a coarse resolution of the principal? Answered in §10: not a resolution, which would forgive what it merges; a request that is an evaluator coarser than the target, norms carried by the default, and weights the request never fixed, a family of targets. With it: consolidate, rework the roadmap, archive what is done, re-prioritize, and say which papers are needed | PI; executor (the analysis, the roadmap) | `NOTES.md` §10, `RELATED.md`, `ROADMAP.md` |
| Q36 | the PI has no academic access, so papers behind paywalls are out of reach; hosts are allowed on request. Applied: an imported theorem is read in a text anyone can read without paying, or derived here with a proof and a check, or not imported (`README.md`, working agreements); the limit laws White and Vuong were to supply derived for finite outcomes as [[P52 — What a sample certifies about misalignment, by access\|P52]], with Huber's open paper read for the general case of (i); the field Access in `STANDARD.md`; the requests to the PI now name hosts to allow and data to ask for, not papers (`ROADMAP.md`) | PI; executor (the rule, [[P52 — What a sample certifies about misalignment, by access\|P52]], the field) | `README.md`; [[P52 — What a sample certifies about misalignment, by access\|P52]]; `STANDARD.md`; §3.2, D12; §9; `ROADMAP.md` |
| Q37 | consolidate what the executor needs from the PI in one file, and make the framework's engineering side more solid before some steps are actioned. Applied: `REQUESTS.md`, with the hosts allowed; the engineering steps E1–E5 first in `ROADMAP.md`; `stdalign` 0.1, the library, with misalignment, its split and its estimates by access, the checks of those items pointed at it, tests of its interface, and its functions mutation-tested; `pyproject.toml` | PI; executor (the plan, the library) | `REQUESTS.md`; `ROADMAP.md`; `stdalign/`; `README.md` |
| Q38 | the licence of the library and of the framework: the GNU Affero GPL is kept, since the framework is a work in progress the PI hopes the community will support rather than copy; it is to be revisited if the framework gains predictive or diagnostic power, which is not taken for granted. Applied: §11, with what the licence does not cover (the ideas) and what a later change needs (every copyright holder's consent) | PI | §11; `ROADMAP.md` |
| Q39 | a file for contributors, a review of the whole framework with doc hygiene, then a merge into `main`, and advice for the project. Applied: `CONTRIBUTING.md`, its terms proposed for the PI's approval; the review and its advice in §12; the fixes it lists | PI; executor (the review) | `CONTRIBUTING.md`; §12; `README.md`; `RECORD.md`; `ROADMAP.md` |
| Q40 | close up and hand over, in the order the executor proposed: a close-out (the executor's tools and working rules into the repository, a handover note), then a reader package with a defined end, then the handover, to readers and to a fresh session. Applied: `tools/mdwrap.py`, `tools/mutate.py` and `tools/mutants/`, with tests; `CLAUDE.md`; §13; steps H1 and H2 | PI; executor (the plan) | `CLAUDE.md`; `tools/`; §13; `ROADMAP.md` |
| Q41 | continue until every step of the handover is done, then open one pull request into `main`. Applied: E1(b), the diagnostics in `stdalign` 0.2; E2, the report as data, with its validator and lint R16, and W1's report migrated; E3, `examples/quickstart.py`, run by CI, and every case's environment pinned, which lint R14 now requires; H1, `OVERVIEW.md`, generated from the items; H2, §13 and the requests updated; and the pull request | PI; executor (the package) | §13; `ROADMAP.md`; `REQUESTS.md`; `OVERVIEW.md`; `stdalign/`; `examples/` |
| Q42 | a general doc hygiene before the handover's pull request is updated. Applied: the scripted sweep of §12 run again, statements the handover made stale fixed (`ROADMAP.md`, §2, §13, `REQUESTS.md`, `README.md`, `cases/README.md`), and pull request #31 updated | PI | `ROADMAP.md`; §2; §13 |
| Q43 | review Johnson and Huo (2026), and put in the roadmap, with a priority of the executor's choosing, anything compelling for the framework. Applied: §14; the paper is in `RELATED.md`; nothing in it becomes a step: its theory is a mechanism ([[A1 — Behaviour suffices\|A1]]) and its evidence too thin to build a prediction on; the behavioural question it raises is H37, after E4 and below W5 and C3 (`ROADMAP.md`, not now) | PI; executor (the review and the priority) | §14; `RELATED.md`; `ROADMAP.md` |
| Q44 | [A2]'s Statement says "a Riemannian geometry", as the executor recommended (`REQUESTS.md`, R6). Applied: [A2] with a reason on what "Riemannian" excludes and a Lineage line; GA2 follows it; the core is v12; `OVERVIEW.md`'s point of pressure restated. With it, step 8 done: every imported theorem read in an open text or derived where it is used (`REFERENCES.md`) | PI; executor (step 8) | `CORE.md`; `CORE-GENERAL.md`; `OVERVIEW.md`; `derived/`; `REFERENCES.md`; `ROADMAP.md` |
| Q45 | the contribution terms of `CONTRIBUTING.md` approved as drafted (R4): AGPL in and out, with a grant to relicense under another licence approved by the Open Source Initiative, recorded by a `Signed-off-by:` line | PI | `CONTRIBUTING.md` |
| Q46 | a step, for the finish line's row "stable", is a merged pull request (R5); the count starts with the first pull request merged after the one that made v12 | PI | `README.md`; `ROADMAP.md`, step 7 |
| Q47 | no release tag for the handover (R7): readers review `main` as it is when they start | PI | `REQUESTS.md` |
| Q48 | hand over: the PI relays to an independent reviewer a starting message the executor prepared (R1), and the executor may finish what it chooses first. Applied: the message, pointing to `OVERVIEW.md`, its points of pressure, the checks and the record, given to the PI, not kept in the repository; the pull request that brings v12 and step 8 into `main`, so that the reviewer reads them | PI; executor (the message, the choice) | `REQUESTS.md`, R1 |
| Q49 | review the framework in general: get familiar with its files, methodology and ethos, plan an exhaustive list of focus areas, then review them in turn, with challenges and constructive criticism. Applied: §15, with twelve focus areas, eleven findings and seven pieces of advice; `probes/review/`; `OVERVIEW.md`'s count of predictions and an orientation for a mathematician; Korbak, Perez and Buckley in `RELATED.md`; a row of §1 extended and one added; the order of the commands before a push fixed; three decisions asked (`REQUESTS.md`, R8–R10) | PI; executor (the review) | §15; `probes/review/`; `tools/overview_template.md`; `ROADMAP.md`; `REQUESTS.md` |
| Q50 | the licence's aim during research: progress on the framework, by people or by models working on copies of it, is shared with everyone; the GNU Affero GPL, version 3 or later, is kept for the code and the text, and the adoption it costs is accepted; it is to be relaxed once research gives way to use. So R9 is declined, and the executor withdraws the recommendation behind it (§15, advice 6). Applied: §11, what a copyleft licence reaches and what it does not, and what gets closer; proposed and awaiting the PI: additional terms under the licence's section 7, a request to AI agents that work on copies, and a citation file with a DOI per release (`REQUESTS.md`, R11) | PI; executor (the analysis) | §11; §15; `REQUESTS.md`; `ROADMAP.md` |
| Q51 | draft on a new branch the core the review's advice would give, and review whether it is more compelling and more solid than v12. Applied: branch `claude/core-reframe`, a draft v13: [[A4 — Misalignment is evidence\|A4]] misalignment is evidence, [A6] declared no finer than identified, [[D3 — Specification, declaration and misalignment\|D3]] with the ordinal and the matched specification, [[P6 — The departure from the default splits into pursuit and misalignment\|P6]](ii) the excess departure with its check and mutants (5 of 5 caught), `GA4`, `STANDARD.md`, `TERMS.md`, `README.md`, `RECORD.md` and the overview; §16 the review: adopt [[A4 — Misalignment is evidence\|A4]], [[P6 — The departure from the default splits into pursuit and misalignment\|P6]](ii), the ordinal specification as an option and the paired report, not [A6] (R12) | PI; executor (the draft and the review) | §16; the branch |
| Q52 | v13 approved, in the lean form the executor proposed after Q51's review: three premises, [[A1 — Behaviour suffices\|A1]] behaviour suffices, [[A4 — Misalignment is evidence\|A4]] misalignment is evidence and [[A5 — Declared before\|A5]] declared before; v12's A2 and A3 made reasons of [[D2 — Pursuit of an objective\|D2]], since no result used them; A6 not adopted; the identity that misalignment is the departure beyond what a specification credits, as a result with its check and mutants; the paired report in `STANDARD.md`; the dependencies measured again; the estimation and diagnostics of the ordinal specification as steps. Applied on the existing branch, not a new one, and built by the method of Carcassi's reverse physics: what is imported from probability theory (M), what is assumed without loss of generality (B) and what is assumed (A) named apart, each with a Status saying what kind of starting point it is, and every definition with a physical or behavioural interpretation, declared and justified | PI; executor (the structure, the interpretations, [[P53 — Misalignment is the departure beyond what the family of targets credits\|P53]]) | `CORE.md` v13; [[P53 — Misalignment is the departure beyond what the family of targets credits\|P53]]; `STANDARD.md`; lint R1, R3–R5; `ROADMAP.md` O1, O2 and step 3; §17 |
| Q53 | seven requests: justify every declared convention by mathematical convenience or the literature; drop the independence of decisions between episodes, if nothing important is lost; compare against a family of targets rather than one target, with Sanov; rework the continuous case, with the dictionary and the mapping; say how the ontologies and their declarations change; give the verifications statistical tests in a meaningful way; and say whether observing activations helps verification. Applied on `claude/core-reframe`: the table of conventions in `CORE.md` §1, with lint R17; [[A4 — Misalignment is evidence\|A4]] restated on the record's counts, which needs no independence of the actor, with [[P54 — Dependence and drift only add evidence\|P54]] (dependence and drift only add evidence); families of targets in [[D3 — Specification, declaration and misalignment\|D3]], and [[P53 — Misalignment is the departure beyond what the family of targets credits\|P53]] for every family; [[P55 — What a record of counts certifies, at every size\|P55]] (exact tests and intervals from counts, Sanov, Genin and Kelly's verifiability); [[D11 — Record, sample and evidence\|D11]] with records; `CORE-GENERAL.md` draft 4 on the kinds of v13, with misalignment as the supremum over the finite descriptions a record can decide, and `general/dictionary.md` and `general/transfer.md` brought to it; the ontologies' slots and declarations; H38 on activations; §18 | PI; executor (the derivations, the general core's design) | §18; `CORE.md`; `derived/misalignment.md`, `derived/estimation.md`; `CORE-GENERAL.md`; `ontologies/` |
| Q54 | all accepted: misalignment on a continuum as the supremum over the finite descriptions a record can decide (`CORE-GENERAL.md` draft 4, open decision 1); H33 and H38, activations as observations, reopened under the freeze, starting with the narrow case H38 proposes; and the convention that doing nothing is intended, flagged as changing a verdict, kept as it stands. Then doc hygiene. Applied: `REQUESTS.md` R13 done; `CORE-GENERAL.md` §12; case C5 (`cases/c5-activations/`); §19 | PI | `CORE-GENERAL.md`; `cases/c5-activations/`; §19 |
| Q55 | pull request #33 merged into `main` with its history (2026-10-11): v13, the review of Q49, the licence's aim (Q50), the seven requests (Q53), C5, doc hygiene, and the reread's fixes. Applied: the records that said v13 was not yet merged (`CORE.md`'s status, `README.md`, `ROADMAP.md`, §19's handover); the count for "stable" restarts at 0 of 3 (Q46) | PI | `CORE.md`; `README.md`; `ROADMAP.md`; §19 |
| Q56 | the branch `claude/core-reframe` may be deleted; the executor agrees, since everything on it is in `main`. Priorities: the mathematics first, and `CORE-GENERAL.md` now, made correct and coherent rather than split or restructured; read the missing sources, asking for a host when one is needed; then a real-life simple case where the framework gives true insight, diagnosis or prediction, for which the engineering must be rethought or updated. A rewrite of the framework into a more digestible structure, most files ignorable without losing anything important and deep knowledge reachable when needed, is the PI's hunch, not a decision (H39). The executor keeps its own insights, hypotheses and hunches in these notes. Applied: §20; `general/transfer.md` TR1–TR8; the corrections of `CORE-GENERAL.md`; `REQUESTS.md` R14 | PI | §20; `CORE-GENERAL.md`; `general/` |
| Q57 | `www.math.mcgill.ca` allowed (R14). Then: since the framework calls mathematical objects by words such as "misalignment", "outer alignment" or "tampering", and since theory and practice must agree through verification (Carcassi), verify every definition in the sense that its label corresponds to what its word means, with concrete arguments; a definition labelled wrongly gives a false sense of understanding, and accuracy here is worth its cost. Applied: R14 closed; a label verification, L1, registered and pushed before anything was computed (`probes/labels/REGISTRATION.md`), then run; §21 | PI | `probes/labels/`; §21 |
| Q58 | open to a major revamp of the core, if it brings the terminology closer to common sense; no quick fixes or workarounds; the framework must be trustworthy, mathematically formal and general. A brainstorm first. Applied: §22, a proposal for the PI | PI | §22 |
| Q59 | open a pull request to `main` with the latest changes; then start reworking the core as the executor recommends, on a branch of its own, from everything discussed so far. Constraints become a concept of the core: outcomes the principal finds unacceptable, whose breach is plainly a form of misalignment; how to include that misalignment, in its most fitting form, and the concepts that follow from it, is to be discussed; where optimization is treated, constraints are enforced too, perhaps through the Karush–Kuhn–Tucker conditions and Lagrange multipliers. The PI's decisions on R15 and R16 are postponed until the rework has absorbed constraints and the other recommended changes. Applied: the pull request; the branch `claude/core-v14`; R15 and R16 marked postponed | PI | `REQUESTS.md`; the branch `claude/core-v14` |
| Q60 | back to the drawing board for a turn: constraints are declared explicitly, as a general concept, since some are not available in the principal's family of targets (a bound on an average, a resolution); a fee or cost against a misaligned event is not a concept of the core, since each target carries it implicitly in the event's probability, and it is to be derived where optimization needs it; which other concepts can move from the core to refinements? Applied: §24, a discussion; nothing changed in `v14/` yet | PI | §24 |
| Q61 | separate files built on their cores: `CORE`, `CORE_GENERAL`, `OPTIMIZERS`, `OPTIMIZERS_GENERAL`; culpability to be defined formally; the full list of forms of misalignment (unavoidable breaches, coarse understanding, cheating, and others), which `CORE` alone can factor, and the least additional concepts each of the others needs. Applied: §25, a discussion; nothing changed in `v14/` yet | PI | §25 |
| Q62 | three layers, each with its twin: `CORE`, `CORE_GENERAL`, `INTERFACE`, `INTERFACE_GENERAL`, `OPTIMIZERS`, `OPTIMIZERS_GENERAL`; a file of the framework's limits and what it leaves out; prove that the factorization is exactly additive, as the earlier splits were by Pythagoras, looking for the factors those splits found; prove that Carcassi's methodology of verification can justify the factors' labels; report any issue, and anything the PI is forgetting. Applied: `v14/factorization.md`, `v14/LIMITS.md`, `v14/README.md`'s plan of files; §26; a failure mode of [[P15 — Misalignment splits into what the actor could avoid and what it could not\|P15]](v)'s label | PI | §26; `v14/` |
| Q63 | prepend the executor's recommendations to the roadmap, to be worked on together; and say how much of the previous work the new core and files can save, and what is incompatible whatever the fix. Applied: `ROADMAP.md`'s recommendations; `v14/MIGRATION.md`; §27 | PI | `ROADMAP.md`; `v14/MIGRATION.md`; §27 |
| Q64 | consolidate the findings in the appropriate files; find again the work that made the core compelling, every convention and definition without loss of generality and mathematically canonical, understand its method, and say whether the new core and files keep to it, explaining so in the files, as a defence against challenges that would weaken the framework if acknowledged without further thought. Applied: `v14/README.md` rewritten to the current design, with the claims of generality and their qualifiers, the conventions justified, and the challenges answered; `v14/interface.md`, the INTERFACE layer and the forms of misalignment; VK0 and IN1; the canonicity sections of `evidence.md` and `order.md`; §28 | PI | `v14/`; §28 |
| Q65 | pull request #34 merged into `main`; [[P15 — Misalignment splits into what the actor could avoid and what it could not\|P15]](v)'s overclaim left on `main` for now, to be corrected in v14's migration (R18 closed); a turn of documentation hygiene and consistency across the files. Applied: `main` merged into `claude/core-v14`; `ROADMAP.md`, `README.md`, `REQUESTS.md`, `CLAUDE.md` and the v14 files swept; §29 | PI | §29 |
| Q66 | a presentation of about thirty slides, in whatever format suits slides that change often, presenting the framework and how to use it on one simple example, kept in the repository where it fits best. Applied: `slides/framework.md` (32 slides, Marp Markdown) with `slides/README.md` and `slides/.marprc.yml`; the example's numbers from `probes/slides/support_bot.py`; §30 | PI | `slides/`; `probes/slides/`; §30 |
| Q67 | what drafting the slides and running the example taught: lessons of formalization, methodology and applicability, and gaps in theory or practice. Applied: §31; H47, H48; `ROADMAP.md`, recommendation 10 | PI | §31 |
| Q68 | merge the v14 draft to `main`, then delete the branches no longer needed, after an analysis of which. Applied: the files that placed v14 on its branch made true on `main`; a pull request from `claude/core-v14`; the analysis of the branches in the pull request and the turn's answer | PI | `README.md`, `ROADMAP.md`, `CLAUDE.md`, `slides/`, `v14/README.md` |
| Q69 | after reviewing the slides, ten requests: (0) which of the slides' lessons to include now; (1) a second, independent deck of about thirty slides for mathematicians who know probability but not alignment, explaining σ-algebras and factoring their effect on misalignment, families of targets with Sanov, and every factorization result named and its label verified by Carcassi's methodology; (2) a better name than OPTIMIZERS, which suggests machine-learning training and is, in practice, about mesa-optimizers; (3) a fourth file and twin for training, with ontology-neutral terms, as a draft for a brainstorm; (4) severity, agreed to be independent of misalignment, measured and played against it in training; (5) how constraints are declared, where they are implicit, where explicit, the interface's role, and whether to call them a specification; (6) whether the principal is the only one who grades, and in what form; (7) formal elegance and reverse-physics methodology to adopt; (8) what the framework includes that the rest already gives; (9) a survey of competing frameworks, both ways. Applied: §32; `v14/resolution.md`, `v14/targets.md`, VK6 and VK7 and the section on declaring in `v14/constraints.md`, `v14/severity.md`, `v14/training.md`, `v14/related.md`; `slides/mathematicians.md`, `slides/specification.md`; `probes/v14/resolution.py`, `probes/slides/qa_model.py`; R20 | PI | §32 |
| Q70 | after reading §32: record every analysis, the survey of competitors with its pros and cons included, where it belongs; say which of the lessons, elegances, redundancies and gaps were already applied to the tree, and brainstorm the rest; brainstorm whether conditions and outcomes need to stay split, or can be one distribution; a clearer method, after Carcassi, that justifies pairing each label with its formalization; a measure of what an actor does with distinctions finer than the principal's ("deviance" or "miscalibration", a better name welcome), beside the factor for distinctions it lacks; whether "adversarial" can be defined and measured. Decisions: R19, the mixture principle, to be solved from the literature, statistical or Carcassi's, where mixtures are founding; culpability to be redefined, with the literature's help; R20 approved (PURPOSE, SHAPING, specification), the PI liking "aligning" too and asking the executor to defend "declaration" and "specification" against common usage or to brainstorm better names; a turn of documentation hygiene, then the brainstorm. Applied: §33 | PI | §33 |
| Q71 | the point of σ-algebras, made explicit by the PI: in general the actor and the principal do not know each other's σ-algebras; they know mismatches are possible but cannot point to where they are, which is why confusion occurs and why perplexity can be measured; the PI expects this to change how mismatches are treated and factored, not to prevent measuring them; and Carcassi and Aidala's book supplied (R21). Applied: RS8 in `v14/resolution.md`; §33.11, §33.12 | PI | §33.11, §33.12 |
| Q72 | after the executor proposed R19 and certification as the next brainstorm: above the PI's expertise; consolidate it in the notes with the decision pending the PI, the answer perhaps forced once the framework's desiderata are clear; the PI still wants more clarity on latitude available and confusion on a continuum, good enough for now. Applied: §33.15, R19 updated | PI | §33.15 |
| Q73 | the PI wants more time on the desiderata: they shape the project so much that they need much consideration; the framework is to be formally well-defined, coherent and general, import known results (from its ontologies above all), make testable predictions and serve as a diagnostic, and guide a person or a model to say what alignment means in a context and how the declarations shape the analysis; desiderata should be few, general, informal but not too much, and filtering, and §33.15's looked oddly specific. Applied: §33.16, a draft of six; §33.15's D1–D6 restated as design rules that follow from them; R22 | PI | §33.16 |
| Q74 | the PI likes the six desiderata and how they interplay, sometimes against one another, drawing a border, an interface; promote them, and revisit them from time to time; if the list forces a pending decision, decide it directly; then a turn of documentation hygiene. Applied: the desiderata in `README.md`, with a drift check in `ROADMAP.md` and a rule in `CLAUDE.md`; §33.17, the decisions they force, taken by the executor under this row: R19 by two kinds of requirement and two verdicts, an order's requirement as dominance with declared margins, a reference that may break a constraint, culpability at a declared care margin with `E` as its size, one space with an exogenous σ-algebra, the entropy imports, the redundancies, and three working agreements; R19, R22 and R16 closed, R15 trimmed; the hygiene of `v14/` and `slides/` | PI; executor (the decisions forced) | §33.17 |
| Q75 | once Q74's work is done and CI is green, bring it to `main`. Applied: a pull request from `claude/peaceful-ritchie-cnu5r3`, merged with a merge commit, as `CLAUDE.md` asks rather than a push to `main` | PI | `ROADMAP.md` |
| Q76 | the PI deleted the merged branch; an external review by another model family, to be weighed and not imported; the question of Q70 on conditions and outcomes seemed unanswered: read all the PI's prompts, judge each actioned or lost, then fix the docs and the slides. Applied: §34, the audit and the review weighed; conditions and outcomes as one distribution with a declared exogenous σ-algebra, in `v14/` and the three decks; "declare" defined; certification corrected to averages; two rules for v14's report; H62, H63 | PI; executor (the audit, the review weighed) | §34 |
| Q77 | a brainstorm: misalignment as a sum weighted by severity, to be rid of infinities without losing the factorization; a simpler CORE, with no reference, targets as a closed convex set of desired distributions with severity scores, and a specification as a signature with an algorithm deciding records in finite time; an exhaustive list of junctures, where the framework's parts meet, with how to treat them and the measures they inspire, from other disciplines too; challenge everything. Applied: §35, `v14/junctures.md`, `probes/v14/contamination.py`, H64–H68, R24 | PI | §35 |
| Q78 | a thorough turn of documentation hygiene. Applied: §36; the stale passages of `v14/`, the slides and the top-level files fixed; the row "stable" recorded as met by the letter, with R25 | PI | §36 |
| Q79 | a step back: how the executor values the framework, its pros and cons, and its gaps, given the recent changes, the goals, the desiderata, the mathematics and the method. Applied: §37 | PI | §37 |
| Q80 | make a new plan that fills the minimal gaps for publishing the framework as an MVP, taking priority over the roadmap and backlog, and carry it out until done; the PI will later publish the MVP from a second repository, cleaned for readers. Applied: `mvp/PLAN.md` | PI; executor (the plan) | `mvp/PLAN.md` |

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
| D12 | the imports of §9 marked "now" | the full texts of White (1982), Vuong (1989), Baker (2002), Courty and Marschke (2008), Ben-Tal et al. (2013) and Polyanskiy and Wu (2025); those on arXiv were read once the PI allowed it (Q34), and Blackwell (1953), Csiszár (1975), Lindsay (1983) and Pistone and Sempi (1995) in their scans on Project Euclid | a theorem enters `derived/` only after its statement is read in the source, not in an abstract | their records and abstracts were found by web search; arXiv and Project Euclid are reachable since Q34, the other publishers are not. Since Q36 no paywalled text is sought: White's limit theory, and Vuong's case with the saturated model, are not needed for finite outcomes, where [[P52 — What a sample certifies about misalignment, by access\|P52]] derives the laws, and Huber (1967), open on Project Euclid, was read for the general case; Vuong's working paper (Caltech Social Science Working Paper 605) and Ben-Tal et al.'s preprint (CentER Discussion Paper 2011-061) are on file since their hosts were allowed (2026-10-08), not yet read; Polyanskiy and Wu's draft is reachable since 2026-10-08, and was read on 2026-10-09 for Gibbs' and Pinsker's inequalities (Theorems 2.3 and 7.10), not yet for divergences on general spaces; no open text of Baker (2002) or of Courty and Marschke (2008) was found |
| D13 | experimental economics ([[P41 — Reversibility: the Jensen–Shannon divergence from the reversal\|P41]], `ROADMAP.md` step 5) | the session records of Oprea, Henwood and Friedman (2011), hawk–dove in continuous time with one-population matching, a symmetric game with two strategies and so a potential game; and of Cason, Friedman and Hopkins (2014), Rock–Paper–Scissors under the same lab's continuous-time protocol | the potential arm of step 5, under a protocol comparable with the Rock–Paper–Scissors arm | no public copy found (2026-10-07); the authors, at the LEEPS laboratory of UC Santa Cruz, are the source. The Rock–Paper–Scissors arm alone has public records, Wang, Xu and Zhou (2014), in discrete time, in the R package stratEst under GPL-3, but their cycles are already reported, so a test on them alone risks little |

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
specification "pursue `F` in every context, at any intensity in each", which is a specification by [[D3 — Specification, declaration and misalignment|D3]]; when the actual
behaviour has the default's context masses, its misalignment is the average of the per-context misalignments, by
[[P4 — What KL measures|P4]](iii). [[P13 — What the start of a change gains|P13]](i), and the first limit of [[P13 — What the start of a change gains|P13]](ii), hold across contexts as stated.

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

**Done in v11:** the scope widened to groups and several principals with declared weights ([[P39 — Several actors: coordination plus individual misalignment|P39]]–[[P42 — Several principals: gridlock, and the pooled pursuit|P42]], Q24, Q25); the
freeze (Q26); `cases/` with lint R14, and cases C1 and C2, each revising a prediction before its data were read;
`SCENARIO.md`; `ROADMAP.md`; W1, the first prediction tested on data not seen before: refuted.

**Kept from the earlier list, not scheduled** (`ROADMAP.md`, "Not now"): E8 for best-of-`n` ([[P26 — The regression on bins governs at small intensity|P26]] covers the pursuit
only); the alignment plane (H6); porting v7.10's F2, an exact check of [[P22 — No test detects misalignment faster than misalignment|P22]](i), and F4, edge cases in log space for the
checks' helpers.

**Done since W1** (2026-10-03 to 2026-10-07; archived from `ROADMAP.md`'s "Where we are" on 2026-10-07, Q35). The
licence rule (Q27). W3 (`cases/w3-ppo-pursuit/`), the first test of the bet that an optimizer pursues what it is
rewarded on: a public GPT-2 tuned by PPO pursues its reward in the reward's own scale, with a slope near `1/β` (S2
held), but within prompts the reward explains only `0.358` of what the tuning changed (S1 refuted at the registered
half). W1's report to `STANDARD.md`, exploratory: about three quarters of best-of-`n`'s departure is misalignment
against the gold, at every `n`; the literature's coefficient overstates the initial slope by 22%. The retrospective of
W1 and W3 (§6) and five diagnostics, [[P43 — Misalignment at any intensity|P43]]–[[P47 — The cost of reweighting|P47]] (Q28). Lessons as defaults: `cases/TEMPLATE.md`, lint R15,
`tools/casekit.py` (Q29). W4 (`cases/w4-two-runs/`), the first diagnostic case: what PPO changed beyond its reward is
not a sharpening (S1 refuted) and part of it recurs in a second public run (S2 held), but naming sharpening, the other
reward and the other run's change explains `0.14` of the misalignment. Whose target (§7, Q30): W3 and W4 measured the
trainer's objective, every declaration now names its principal, and an uncertain target is a family ([[P48 — Misalignment when the target is uncertain|P48]]). Outer and
inner misalignment ([[P49 — Outer and inner misalignment|P49]], Q31). Grounding ([[P50 — Tampering: a change of the measurement, not of the world|P50]], [[P51 — What signals, audits and re-measurements reveal of tampering|P51]], Q32): tampering, zero by construction in W1–W4. The cases C1
and C2, and `SCENARIO.md`. Pull request #29 merged (Q33); the survey of imports (§9, Q33); the dictionary from finite to
continuous outcomes (Q34); steps 1 and 2 of that roadmap checked against public data (no record of a potential game,
D13; no public sweep) and the sweep timed.

### 4.1 The roadmap's log, to 2026-10-07

Archived from `ROADMAP.md` on 2026-10-07 (Q35); the step numbers are those of the roadmap at the time.

| Date | Change | Row |
|---|---|---|
| 2026-10-03 | consolidation; v11; the freeze; `cases/` and R14; cases C1 and C2, both revising a prediction before data; `SCENARIO.md`; this roadmap | 4 (instruments checked); 5 (scenario) |
| 2026-10-03 | the PI supplied Coste et al.'s paper; read; W1's data located, and its access blocked on one network domain | 4 (step 1) |
| 2026-10-03 | W1: proxy trained and frozen; procedure calibrated on synthetic prompts; registered; run once on 12.6 million unseen answers; refuted. The framework's first test on unseen data | 4: met, by a refutation |
| 2026-10-03 | licence rule applied (Q27); W1 reported to `STANDARD.md`; W3 designed, calibrated, registered and run once on a public PPO model: the bet held in part; consolidation | 4 (the bet tested); 5 (the report) |
| 2026-10-03 | retrospective of W1 and W3 (`NOTES.md` §6); five design rules for cases; five diagnostic results derived from the core, P43–P47 (Q28); W4 designed, its second run's provenance traced | 4 (W4); 5 (diagnostics) |
| 2026-10-03 | lessons as defaults: `cases/TEMPLATE.md`, lint R15, `tools/casekit.py` (Q29); W4 rehearsed, registered and run: no sharpening; a small shared change beyond the reward | 5 (W4, a diagnostic) |
| 2026-10-04 | whose target? W3 and W4 measured the trainer's objective; [[P48 — Misalignment when the target is uncertain\|P48]], the interval of misalignment over a family of targets; the field Principal in the standard, the template and lint R15 (Q30) | 5 (diagnostics) |
| 2026-10-04 | [[P49 — Outer and inner misalignment\|P49]], outer and inner misalignment and their exact split; the archive's five gaps mapped (`IMPORT.md`, section 8), grounding only partly covered (Q31) | 5 (diagnostics) |
| 2026-10-07 | [[P50 — Tampering: a change of the measurement, not of the world\|P50]], tampering, and [[P51 — What signals, audits and re-measurements reveal of tampering\|P51]], what signals, audits and re-measurements reveal of it, with checks and mutation tests; the grounding gap mapped as in the core for a declared channel; the two pending framework tests, [[P41 — Reversibility: the Jensen–Shannon divergence from the reversal\|P41]] and [[P20 — Where overoptimization starts, and how it ends\|P20]], made steps 1 and 2, and the tampering simulation step 3 (Q32) | 4 (steps 1–3 set); 5 (diagnostics) |
| 2026-10-07 | pull request #29 merged with its history; the PI approved: one mathematical reader, H34 as C3's second arm, the general core unfrozen for outcomes that are not finite and estimation (step 4), the history kept (Q33). A survey of what the framework can import: twenty sources verified from their records, filed in `RELATED.md`, ranked in `NOTES.md` §9 | 5 (imports for the estimation work); 2 (the count restarts with step 4) |
| 2026-10-07 | with arXiv allowed, eleven imported sources read in their text; `general/dictionary.md`, each object of the framework in its finite and its continuous form, with what the imports say about the continuum (Q34); McAllester and Stratos's limit corrected after reading its theorem | 5 (step 4 prepared) |
| 2026-10-07 | four sources read in their scans on Project Euclid (Blackwell, Csiszár, Lindsay, Pistone and Sempi), the dictionary updated; steps 1 and 2 checked: no public record of a potential game (requested, D13), no public sweep; a sweep's cost measured on this machine (`probes/cases/`) | 4 (steps 1 and 2 checked) |

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
- *Why it is canonical.* (a) It adds no assumption: by [[P1 — Every behaviour is a tilt of any other|P1]] and [A3], every full-support behaviour is the best trade-off
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
  incentives (Baker's "distortion" of performance measures, 2002); the angle between true and proxy rewards in occupancy
  space (Karwowski et al., ICLR 2024); hackability of reward pairs (Skalse et al., NeurIPS 2022); selection gradients
  and the secondary theorem of selection in biology (Lande and Arnold; Robertson; Price); Manheim and Garrabrant's
  taxonomy.

**Candidate 2, a possible second: sampling.** Observation through `n` independent decisions.
- *Why it is canonical.* It gives misalignment a second, independent meaning that agrees with the first (H4): the
  expected log-likelihood ratio per decision, under the actual behaviour, of the actual against the nearest intended
  behaviour is `M`, so in a sequential test (Wald) about `log(1/α)/M` decisions reject the intended behaviour. Value
  lost ([[A4 — Misalignment is evidence|A4]]) and evidence gained agree, in the same direction of KL: the same pattern as [A2] and [A3] agreeing on the
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
| H4 | **Value and evidence agree.** Misalignment is both the least value lost ([[A4 — Misalignment is evidence\|A4]]) and the evidence rate against the nearest intended behaviour under the actual one (Wald). Could justify the direction of KL independently of [A3] | **stated as [[P21 — The expected evidence is misalignment\|P21]]**: with the log-likelihood ratio as evidence ([[D11 — Record, sample and evidence\|D11]]) and samples drawn from the actual behaviour, the rate is `KL(p̂‖·)`, form and direction, without [A3]; it rests on the choice of evidence (Neyman–Pearson) instead. [[D3 — Specification, declaration and misalignment\|D3]]'s Why gives the reading, and argues from value |
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
| H31 | **Unconverged reinforcement learning changes more than it pursues.** In W3, the part of `log(π/π_ref)` along the reward has a slope near `1/β` (`4.27` against `5` at the starting KL coefficient), as [[P4 — What KL measures\|P4]] says, yet within each model's own continuations the reward explains only a tenth of it. The rest may be the drift a noisy policy gradient accumulates, which the KL penalty slows but does not aim. If so, along one run the reward's share of the revealed objective, within the tuned model's own continuations, should rise towards 1 as the run converges; a share that stays low at convergence would mean the rest is not drift but a systematic pull, of the value estimate or the adaptive coefficient, which the framework would then have to name. Test: checkpoints of one run, or runs at several `β`, with their reward model, all public | open: needs public checkpoints. W4 (`cases/w4-two-runs/`) asks the part two public runs can answer: whether the off-reward change recurs in another run |
| H32 | **The most charitable principal.** When the principal's objective is known only to lie in the span of given functions, the least misalignment any such principal finds is the unexplained misalignment of [[P44 — What named objectives explain\|P44]], attained by the principal whose objective is the named pursuit's exponent, and the largest is the departure. So an uncertain target turns misalignment into an interval, as an unobserved condition does in [[P17 — What an unobserved condition can hide\|P17]]. Proof sketch: over the span, `inf_{c, t ≥ 0} KL(p̂‖tilt(q, t·c·Φ))` is the infimum over the whole exponential family, attained at the moment-matching tilt, which is the named pursuit ([[P44 — What named objectives explain\|P44]](i)); one of `±F'` never beats the default, so [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits\|P5]](iv) gives the departure | **applied as [[P48 — Misalignment when the target is uncertain\|P48]]**, with a direct proof and a check (Q30); first probed in `probes/diagnostics/probe_charitable.py` |
| H33 | **Logs as outcomes.** Activations logged from a black box are observations, so making them part of the declared outcome keeps [[A1 — Behaviour suffices\|A1]]: the core would judge their distribution, not their meaning, the move [[P50 — Tampering: a change of the measurement, not of the world\|P50]] made for measurements. Three consequences, none yet a result. (a) If the outputs are computed from the logged activations, these are a view of the condition ([[D8 — Conditions, responses and views\|D8]]), so by [[P16 — An actor cannot behave more differently than it can tell conditions apart\|P16]] the divergence of activations between evaluation and use bounds from above how differently the actor can act there: the `ε` that [[P17 — What an unobserved condition can hide\|P17]] needs and that studies of evaluation awareness cannot give (H27). But an upper bound on a divergence between high-dimensional distributions cannot be estimated from samples without a model, so the bound inherits the model's error. (b) A surrogate, a white-box model trained on the logs, transfers its findings to the black box only within its fidelity, a divergence measurable where the surrogate was fitted and bounded elsewhere only by [[P17 — What an unobserved condition can hide\|P17]] again. (c) What the black box "knows" is identified from logs only under stated assumptions ([[D9 — Observation and identification\|D9]]): where the labels come from a fallible observer, a reporter that says the truth and one that says what the observer would believe fit the same data, and logs narrow the identified set only through assumptions such as consistency or sparsity. This is the programme of probing and dictionary learning in interpretability, not new; the framework would add its accounting: fidelity in nats, identified sets, the view bound | E: outside the scope (`IMPORT.md` §8, gap 5, "drop"); reopening it is the PI's decision under the freeze. A narrow test, if reopened: a small network whose internals are known, where the view bound and the surrogate's transfer are checked against the truth; reopened by the PI with H38 (Q54): case C5 |
| H34 | **A monitor trained against is tampered with.** A monitor whose verdict is computed from a channel the actor can influence, such as a probe on activations, is a signal in [[P50 — Tampering: a change of the measurement, not of the world\|P50]]'s sense, and training against it is the trainer's optimum of [[P50 — Tampering: a change of the measurement, not of the world\|P50]](iii): it tampers at every positive intensity, with a share at the start equal to the share of the monitor's variance not explained by what it is meant to detect. So optimizing against an imperfect monitor buys, from the first step, a change of what the monitor reads as well as of what it monitors. The reading needs the channel declared (the activations each behaviour would produce, before any training against the monitor), and the trainer's optimum idealizes training | D: a candidate simulation, after the tampering case; no world test named |
| H35 | **The request as evidence, as a declared family.** Inverse reward design's posterior over true rewards, given a written one and the environment it was written for [[References\|@hadfieldmenell2017]], could be the family of [[P48 — Misalignment when the target is uncertain\|P48]] that a principal declares when the request is all there is: the least misalignment over it is the most charitable reading of the request, and the largest is the departure. Features that did not vary where the request was written get the prior's spread, so the interval widens exactly where the request was silent | D: a derived result only if a test needs it |
| H36 | **The default from how people usually act.** Preferences implicit in the state of the world [[References\|@shah2019]] suggest estimating the default from a population's ordinary behaviour, so that the norms nobody states are carried by the cost of departure. Since a pursuit keeps the default's proportions among outcomes the request scores alike, an unstated norm then moves only through its regression on the request ([[P18 — Through the evaluator, only the regression counts\|P18]]) | D: a declaration practice for `STANDARD.md`, to try in a case |
| H37 | **Misalignment along a conversation.** Each prefix of a conversation is a condition ([[D8 — Conditions, responses and views\|D8]]), so a model's next-turn behaviour over declared classes of outcome, good, bad and other (a resolution, [[D4 — Resolution\|D4]]), can be judged at each position against the standard specification of `F = 1_good − 1_bad`, and the path of behaviours tested for a fixed objective ([[P3 — A fixed objective is visible in the changes of behaviour\|P3]]). Evaluations that sample first turns and use that runs long meet these conditions in different proportions, so [[P24 — The evaluation gap\|P24]]'s gap applies, and [[P17 — What an unobserved condition can hide\|P17]] says first-turn alignment certifies nothing about later turns without a bound on how far the model tells them apart. Johnson and Huo's good-to-bad tipping [[References\|@johnson2026]] would be the case where the revealed objective turns from good to bad at a definite position (§14) | D: a diagnostic case, after E4, below W5 and C3 |
| H38 | **Activations verify that an actor can tell situations apart, never that it cannot.** The PI asked whether observing activations helps verification (Q53). H33 and H34 already said most of it: logged activations are observations, so judging their distribution keeps [[A1 — Behaviour suffices\|A1]]; if the outputs are computed from them they are a view ([[D8 — Conditions, responses and views\|D8]]), and by [[P16 — An actor cannot behave more differently than it can tell conditions apart\|P16]] their divergence between evaluation and use bounds from above how differently the actor can act, the `ε` that [[P17 — What an unobserved condition can hide\|P17]] needs; and a monitor on activations that the actor is trained against is tampered with. What the topology of verifiability adds is exact: a probe, any statistic of the activations, gives a lower bound on the divergence of the view by data processing (the Donsker–Varadhan formula, [[References\|@polyanskiy2025]], Theorem 4.6, is a supremum over such statistics), so "the actor tells evaluation from use" is verifiable from activations, an open statement, while "it cannot", the upper bound that [[P17 — What an unobserved condition can hide\|P17]] needs, is closed, refutable and never verifiable without a model ([[P55 — What a record of counts certifies, at every size\|P55]], Notes, after [[References\|@genin2017]]). So activations can refute the identification of unobserved behaviour, a warning, but cannot establish it. Where they do help: as side information that sharpens estimates, as log-probabilities, which are internals too, already do in [[P52 — What a sample certifies about misalignment, by access\|P52]]; as an audit channel in [[P51 — What signals, audits and re-measurements reveal of tampering\|P51]](iii)'s sense, only while nothing is trained against it (H34); and by letting a white-box model be run on constructed situations, which then become observed conditions ([[D9 — Observation and identification\|D9]]) rather than inferred ones | reopened (Q54); case C5 done, all held: a linear probe was silent on an XOR-read cue of `0.339` nats, and [[P17 — What an unobserved condition can hide\|P17]]'s bound fed that silence failed in 200 of 200 instances (`cases/c5-activations/`). The narrow case as proposed: a small network whose internals are known, where probes' lower bounds on the view's divergence, [[P16 — An actor cannot behave more differently than it can tell conditions apart\|P16]]'s bound and [[P17 — What an unobserved condition can hide\|P17]]'s hidden misalignment are compared with the truth |
| H39 | **One core, with compactness as its hinge.** The PI's hunch (Q56) is a rewrite into a structure most of which can be ignored. TR3 suggests what the centre could be. On a finite set every closure of intended behaviours is compact, so TR3 there says that misalignment is the least divergence over that closure, attained: [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits\|P5]](i) and (ii). The general core would then not be a parallel document but the core itself, with finite outcomes as the case where compactness is free, and every phenomenon that finite outcomes hide (piles, near misses, the on-target controller, the end of pursuit) is a way compactness fails. A reader who never leaves finite outcomes would lose nothing by ignoring the rest | D: for the PI's rewrite, if it comes; nothing to build before |
| H40 | **A test from counts that tolerates dependence it is told about.** [[P55 — What a record of counts certifies, at every size\|P55]]'s test accuses an actor whose decisions depend on each other, for that alone (§19). For an actor whose decisions more than `b` apart are independent, the counts of every other block of `b` decisions are independent, so [[P55 — What a record of counts certifies, at every size\|P55]] on blocks, as episodes of length `b` ([[B2 — Episodes and conditions as outcomes\|B2]]), would keep its level with the order of the record as the only extra information; a declared `b` is a resolution of time, declared before the data like any other | D: a derived result if a case needs it; a question for the PI first, since it touches the convention that acceptance means independence |
| H41 | **Verifiability without compactness.** TR5 makes "misaligned" verifiable in chance when the closure of the intended behaviours is compact. Without compactness and with no nearness, misalignment may be witnessed only by descriptions outside any countable family fixed in advance, so it may fail to be verifiable; whether it can fail is open, and a counterexample would say exactly what a principal must add (a nearness, a resolution, or a compact family) for a verdict of misalignment to be reachable | D: mathematics, after the PI's priorities |
| H42 | **The real-life case should live where compactness is free.** The PI wants a simple real case with true insight (Q56). Finite outcomes make every result of the core exact and every closure compact, and the ordinal specification needs only a ranking: a public record of choices among a few options, under a known incentive and a known default, judged against a declared ranking, with the paired report of `STANDARD.md` and [[P55 — What a record of counts certifies, at every size\|P55]]'s test, would use only what is proved and checked. What it needs from the engineering is E1(d): the ordinal misalignment and [[P55 — What a record of counts certifies, at every size\|P55]] in the library | D: for the case after the general core, with the PI |
| H43 | **An undetectable loss of order `√n`.** Over `n` decisions, a shift of about `1/√(n·I)` per decision escapes every test of the record, yet loses about `√(n/I)` in `F` in all (`I` the shift's Fisher information). No resolution, bin or distribution function closes it; a guarantee from records should state it | U: a local-asymptotic sketch, not proved (`NOTES.md` §22) |
| H44 | **A ranking certifies three verdicts, not two.** With a ranking and a reference only, an actor is better for every reading of the ranking (its rank under the reference dominates the uniform law), worse for every reading, or neither; a greedy decoder at the 0.9 quantile is neither, and the ordinal specification calls it misaligned. "Misaligned" in its everyday sense needs a value scale, a floor or forbidden outcomes | U: to be registered as a case of L2 before it is computed (`NOTES.md` §22) |
| H45 | **Join the order and the constraints by intersection, with a reference that keeps the constraints.** The acceptable set is the constraints' set intersected with the order's requirement against the reference; a reference that breaches a constraint is replaced by its nearest behaviour that does not, or else "better than the reference" can require a breach | U: a design hunch (`NOTES.md` §23); decided otherwise (Q74, §33.17): the reference may break a constraint, and an empty intersection is reported as an inconsistent specification |
| H46 | **Bets chosen from the record approach the best bet at a rate set by the bets allowed.** On a continuum, bets refitted before each decision from the earlier ones reach the best growth rate at a rate that depends only on the class of bets the principal allows, and H43's `√n` is that rate's floor | U: not proved (`NOTES.md` §23) |
| H47 | **Outcomes are measured, not given.** In practice an outcome such as "a wrong answer" is read by a grader, a person or a model, with errors; v14 treats the record as giving outcomes exactly (`v14/LIMITS.md`). A measurement channel from the true outcome to the graded one, declared and audited, belongs at the base of CORE, not only in INTERFACE's tampering ([[P50 — Tampering: a change of the measurement, not of the world\|P50]]); misalignment of the true behaviour is then partially identified from graded records and audits, as [[P51 — What signals, audits and re-measurements reveal of tampering\|P51]] does for tampering | U: the most important gap in practice (`NOTES.md` §31) |
| H48 | **A forbidden set needs a rate and a plan.** Its misalignment is infinite at any positive rate, so it ranks nothing; and a record shows a breach of rate `r` only after about `1/r` decisions. What a principal can use is a verified lower bound on the rate when a breach is seen, an upper confidence bound when none is (about `3/n` after `n` clean decisions, for a sample), and the number of decisions needed to see one at a rate that matters | U: from the example (`NOTES.md` §31) |
| H49 | **Every factorization is a telescoping along a chain in a lattice, and Pythagorean exactly on linear families.** FA1 telescopes along feasible sets ordered by inclusion, RS1 along σ-algebras ordered by refinement, [[P54 — Dependence and drift only add evidence\|P54]] along the filtration of a record; each term is non-negative because misalignment is monotone along the lattice, and each is an evidence rate between named behaviours when the chain consists of linear families, Csiszár's Pythagorean case. A rule for new splits: name the lattice and the chain, and say whether its members are linear (§32) | D: a pattern seen in every split of `factorization.md` and `resolution.md`, not a theorem |
| H50 | **The trainer's shadow price and the bettor's stake, across two budgets.** A trainer at a KL price under its own severity budget acts on its objective minus `ν` times the severity (VK5), and keeps that budget, so against the same budget the trained actor has no misalignment and `λ* = 0`. When the principal's budget differs from the trainer's, in conditions, grader or cost, the trained actor can break it, and for that actor held fixed the evidence moves with the principal's tolerance at `−λ*` (VK7). How `ν` and `λ*` relate across the two budgets is open (`v14/severity.md`); an earlier form of this hunch, "two prices of one budget", was wrong, as the review of §32 showed | D: a guess, restated after review |
| H51 | **A certify verdict, from the same bets.** VK3's bet is the capital process of a betting confidence sequence for a mean, so an upper confidence sequence for a rate or a budget comes from the bets v14 already builds, giving "breach rate at most `ε`, with confidence `1 − α`" beside the convict verdict, valid under dependence if the literature's martingale argument carries over (`v14/related.md`, entry 2; not read by the executor) | D: from the survey; corrected (Q76, §34): only the average breach rate is certifiable, a pooled verdict, and per decision only for a sample |
| H52 | **Report culpability's size by `E`.** `K = M_{𝓕*}(p̂)` is infinite exactly when the actor produces an outcome that no best feasible behaviour produces, which is the common case: the best behaviours of a convex program over a polytope sit on its boundary, often deterministic in some condition. So `K` is `0` or `∞` for most actors and ranks nothing; and with `M_A(𝓕)` finite, `K > 0`, `E > 0` and `p̂ ∉ 𝓕*` are one verdict. The avoidable excess `E = M_A(p̂) − M_A(𝓕)` is finite whenever `M_A(p̂)` is, and is the size to report; a smoothed `K`, against the best behaviours within a declared margin, is a third candidate for L2 (§32) | D: from the example of `slides/mathematicians.md` |
| H53 | **Conditions are an exogenous σ-algebra, not a type.** One space `Ω` and one distribution; the conditions are a sub-σ-algebra `ℰ` whose law the world fixes, which carries no evidence about the actor, may arrive in any order, and makes pooled requirements state their weights (§33.2) | D: a proposal; decided (Q74, §33.17) |
| H54 | **Latitude.** What the actor does inside the principal's cells, against a declared reference, `KL(p̂‖r) − KL(p̂_ℬ‖r_ℬ)`: never a verdict, a signal that the specification is silent where the principal may not be (RS7, §33.4) | D: a proposal, its identities proved |
| H55 | **Evaluation gaming is measurable with honeypots.** Conditions the principal records and the actor's view merges with unobserved use stand for use; acting differently in evaluations and honeypots is verifiable, and the sign of the misalignment gap says whether it flatters the actor (§33.5) | D: a proposal |
| H56 | **Per-decision and pooled requirements dissolve R19.** Per-decision requirements are convex by meaning and judged by bets; pooled requirements, on the average of the conditional behaviours over a horizon, may be any closed set, CVaR included, judged by a confidence set valid under any dependence (§33.6) | D: a proposal, its key theorem read (§33.10); decided (Q74, §33.17) |
| H57 | **Culpability at a care margin.** `K_δ`, the evidence that the actor is not within a declared `δ` of its best, finite for `δ > 0` in the usual case; the size by `E`, and a Hand-style gap where severity and costs are declared (§33.7) | D: a proposal; decided in its shape (Q74, §33.17), the word left to L2 |
| H58 | **The fraction capacity as a bounded companion of misalignment.** `1 − fcap_p̂(A)`, the least share of decisions that must be unacceptable to explain the behaviour, where Carcassi and Aidala's `fcap` takes the hull of `A` (Definition 4.173): for convex `A`, `fcap_p̂(A) = sup_{a∈A} exp(−D_∞(a‖p̂))`. Bounded, finite at forbidden outcomes, continuous on finite outcomes for compact `A`, so both of its directions are verifiable; it convexifies as the mixture principle does, so it is no way around R19. An earlier form of this row claimed it needed no convexity, which was wrong (§33.11) | D: a proposal, its formula checked for convex `A` |
| H59 | **Perplexity and confusion between σ-algebras.** Under a declared distribution, `H(ℬ|𝒜)` (its exponential the perplexity, the effective number of the principal's cells per cell of the actor) measures what the actor cannot resolve of what the principal cares about, `H(𝒜|ℬ)` the latitude available, and their sum, the variation of information, the confusion; potentials beside the realized missing-resolution factor and latitude (§33.12) | D: a proposal |
| H60 | **Factors that need an unknown σ-algebra are families of exact splits.** One split per σ-algebra consistent with the record; the actor's view revealed from below only (RS8), so the cost of missing resolution is bounded above by records and shown positive only by elicitation (§33.12) | D: RS8 proved; the rest a proposal |
| H61 | **A declared reference is the framework's count of states, and a declared precision its minimal cell.** After Carcassi and Aidala (§4.4, §4.7), entropy-based diagnostics on a continuum are taken relative to a declared distribution, which fixes their zero, sign and coordinates; those that measure the actor's own spread, latitude available and confusion, need besides a declared precision, the smallest cell the actor can act on, the role physics gives a minimal cell of phase space (§33.14) | D: a proposal; adopted (Q74, §33.17) |
| H62 | **Evidence for a motive is relative.** A hypothesis of PURPOSE is never verified (VF2), but two hypotheses that each predict a behaviour can be compared by bets, the likelihood ratio of their predictions growing as evidence for one against the other; a motive gains evidence only against named rivals, and a report says which (from an external review, Q76) | D: a proposal |
| H63 | **A real record where v13 and v14 disagree.** One arm of the real case (H42): an actor that mixes acceptable behaviours, such as decoding at a temperature chosen per prompt, judged by v13's ray and by v14's hull; the verdicts should differ as VE2 says, a prediction that can fail (from an external review, Q76) | D: a proposal for H42's registration |
| H64 | **Zero tolerances reported lexicographically.** A forbidden set is reported as a decisive verdict with its breach rate and interval as the size, beside the finite misalignment of the rest, never summed; this removes every infinity from what a report ranks (§35.1) | D: a proposal |
| H65 | **A declared contamination tolerance.** `A_η = (1 − η)·A + η·Δ` bounds misalignment by `log(1/η)`, keeps convexity, bets and Sanov, and returns to `M_A` as `η → 0`; for a rate limit it loosens the limit to `(1 − η)·ε + η`; for a forbidden outcome the number is dominated by `η`, so it suits a tolerance the principal truly holds (§35.1, `probes/v14/contamination.py`) | D: proved in §35.1, a proposal for CORE |
| H66 | **"Criteria" for v13's targets.** The PI read "target" as a desired distribution, which is what CORE's acceptable behaviours are; v13's targets are scores on outcomes; renaming them criteria removes the clash (§35.2) | D: a proposal |
| H67 | **The record's signature as a declared object.** The outcomes, the world's part `ℰ`, the record's σ-algebra and the horizon, declared together as the contract between a specification and its records; the algorithm supplied by the framework from the acceptable set, not declared (§35.2) | D: a proposal |
| H68 | **Capability and evaluability pull against each other.** A finer view lowers unavoidable misalignment and weakens excuses, and lets the actor tell evaluation from use, weakening honeypots ([[P16 — An actor cannot behave more differently than it can tell conditions apart\|P16]], [[P17 — What an unobserved condition can hide\|P17]]); a report on a more capable actor needs evaluation that the actor's view cannot separate from use, or monitoring in use (`v14/junctures.md`) | D: a proposal |

### 5.5 Process

- Lineage amnesia (§1): search v7.10 before adding a result.
- Three restructurings without data: the next phase has to touch data (§3.2).
- Most of what was "lost" is derivable: the archive is a source of statements to re-derive and check, not of text to
  copy.

### 5.6 Drafts for v10 (applied as [[D10 — Evaluator, regression and residual|D10]] and [[D11 — Record, sample and evidence|D11]]; kept for the record)

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
*Why, in outline.* (a) No new assumption: by [[P1 — Every behaviour is a tilt of any other|P1]] and [A3] every full-support behaviour reveals one evaluator, up to
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
direction, as the value lost of [[A4 — Misalignment is evidence|A4]]. (e) Explanations can be compared in the same unit: evidence in nats for one
evaluator against another. (f) Independence is the default model; dependent samples are out of scope until an item
needs them.
*Results it would carry, in a new `derived/estimation.md`.* the expected evidence identity; Wald's expected sample size
to reject the specification; Chernoff and Stein exponents for detection (v7.10's Prop 18); Wilks for the estimated
misalignment (E1); the evaluation gap (v7.10's Prop 19) with [[D8 — Conditions, responses and views|D8]].
*A policy question.* Wald, Chernoff, Stein and Wilks are classical theorems. Do derived results whose proof is a
citation, checked by simulation, meet the standard of the derived folder? Executor's view: yes, with the theorem quoted
with its hypotheses, and a check that would fail if a hypothesis did not hold.

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
| 1 | White (1982); Vuong (1989): misspecified models | the revealed intensity is White's pseudo-true parameter, so his limit theory gives intervals for `t*` and the quantities at it; Vuong's test says which of two specifications fits an actor better, and should give the limit of `2n·M(p̂_n)` when `M > 0`, which [[P23 — The estimated misalignment of an actor that pursues the objective\|P23]] lacks | [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits\|P5]], [[P23 — The estimated misalignment of an actor that pursues the objective\|P23]], [[P44 — What named objectives explain\|P44]], [[P48 — Misalignment when the target is uncertain\|P48]], [[P49 — Outer and inner misalignment\|P49]]; the estimation work | theorems and a test | finite outcomes: derived as [[P52 — What a sample certifies about misalignment, by access\|P52]], with Huber's open paper (Q36); the test between two specifications later |
| 2 | Chatterjee and Diaconis (2018) | reweighting needs about `e^{KL}` draws, necessary and sufficient | [[P47 — The cost of reweighting\|P47]], every diagnostic computed by reweighting | theorem | now |
| 3 | McAllester and Stratos (2020) | with one behaviour known and the other sampled, no distribution-free lower bound on the divergence above `ln N`; the same for mutual information (read in full, Q34) | the estimation work; the limit of H33 | theorem | now |
| 4 | Kwa et al. (2024) | a KL penalty protects the target against a light-tailed evaluator error and not against a heavy-tailed one | the general core, for outcomes that are not finite | theorem | now |
| 5 | Baker (2002); Courty and Marschke (2008) | a measure's distortion and risk, against [[P50 — Tampering: a change of the measurement, not of the world\|P50]](iii)'s split of the misaligned share into world and noise; a test of distortion from how a measure degrades once it is paid on, a candidate world design for [[P20 — Where overoptimization starts, and how it ends\|P20]] | [[P11 — The misaligned share at the start of a change\|P11]], [[P50 — Tampering: a change of the measurement, not of the world\|P50]]; step 1 | correspondence and a design | no open text found (Q36); W5's design does not wait on it |
| 6 | Baker et al. (2025) | a monitor trained against hides the intent it was meant to catch, at high optimization strength | H34; case C3's second arm | evidence | now |
| 7 | Polyanskiy and Wu (2025) | divergences on general spaces, and their variational forms | the general core | textbook | now: the authors' draft is reachable (Q36) |
| 8 | Ben-Tal et al. (2013): robust optimization over divergence balls | the dual of the worst case for every divergence ball, and its radius from data | [[P17 — What an unobserved condition can hide\|P17]], [[P27 — The best use of a departure budget\|P27]], [[P31 — Budgets of other shapes\|P31]] | method | later; its preprint is on file |
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

**After Q36 (2026-10-08).** With paywalled texts out of reach, the first import of the list was derived instead of read:
on finite outcomes, the limit laws of the revealed intensity and of misalignment off the ray are a few lines of the
central limit theorem and the delta method, since the pursuit ray is an exponential family, and they are [[P52 — What a sample certifies about misalignment, by access|P52]], with
Huber's corollary, open on Project Euclid, as their general form. The derivation found more than the import promised:
what a sample certifies depends on what is known of each draw, and with log-ratios known the estimate is never negative,
exactly zero on the ray, and near the ray of the order of `M²` in variance rather than `M`, while far from the ray
counting does better. The rule that follows, to read imported theorems only in open texts or derive them, suits a
standard: an outside reader without an affiliation can then check every theorem the framework rests on.

## 10. Requests made without full consideration, and cooperative inverse reinforcement learning (Q35)

The PI's example: someone asks to get rich, without saying "ethically", because it goes without saying. Is that a coarse
resolution of the principal? It is not, and the difference matters.

**Why not a resolution.** In the core a principal's resolution is a declaration of indifference ([[D4 — Resolution|D4]]): outcomes in one
cell are equally acceptable, and [[P7 — Indifference forgives exactly what happens inside cells|P7]] shows that such a declaration forgives exactly the departure inside the cells.
Read as a resolution, "get rich" would make ethical and unethical wealth equally acceptable, and an actor that got rich
dishonestly would be aligned by the principal's own declaration. The requester is not indifferent; they did not say.
What is coarse is the request, not the requester's indifference.

**What it is, in the core's objects.** Three things, which combine.
1. *A request that is an evaluator coarser than the target* ([[D10 — Evaluator, regression and residual|D10]]). The request scores outcomes by wealth; the target
   distinguishes outcomes the request scores alike, and what the request does not see is the residual. Along the pursuit
   of the request, the default's proportions among outcomes of equal wealth are kept, so anything the request does not
   mention, honesty included, moves only through its regression on wealth under the default ([[P18 — Through the evaluator, only the regression counts|P18]]; checked in
   `probes/diagnostics/probe_requests.py`). Where the dishonest ways are also the richer ones, pursuing wealth buys
   dishonesty: in the probe's toy, where the dishonest way is a tenth as common under the default and 1.5 richer, the
   dishonest share rises from `9%` at the default to `31%` at intensity `1` and `67%` at intensity `2`. Against the
   requester's real target, wealth minus 3 for each dishonest outcome, the outer misalignment of [[P49 — Outer and inner misalignment|P49]] is `0.11`, `0.52`
   and `2.23` nats at intensities `0.5`, `1` and `2`, of departures `0.27`, `1.10` and `3.02`.
2. *Norms carried by the default.* What goes without saying is how things are usually done: the default. The cost of
   departing from it is what keeps a pursuit near the usual norms, and the standard specification, which accepts every
   intensity, is where the request overreaches. "Get rich, within the usual norms" is a cap on intensity ([[P35 — Floors and caps|P35]]), or a
   feasible set that excludes some outcomes ([[D7 — Feasibility|D7]]); "get rich" alone accepts the end of the ray.
3. *Weights the request never fixed* ([[P48 — Misalignment when the target is uncertain|P48]]). A request formed where honesty never varied fixes nothing about honesty's
   weight. When the actor meets a condition where it varies ([[D8 — Conditions, responses and views|D8]], [[P24 — The evaluation gap|P24]]), the honest report is the interval of
   misalignment over targets "wealth plus some non-negative weight on honesty": its lower end, the most charitable
   reading, can be zero while its upper end is the whole departure.

*Wrong perception altogether*, a requester who misjudges what outcomes are like, is different again: the principal then
judges through a measurement, as in [[P50 — Tampering: a change of the measurement, not of the world|P50]], or declares a target on the wrong objects. The core can say only what the
declaration implies; observation alone cannot separate a principal's mistaken beliefs from their preferences
[[References|@armstrong2018]].

**Cooperative inverse reinforcement learning and its variants** (`RELATED.md`). CIRL designs an assistant that does not
know the principal's target and infers it while acting [[References|@hadfieldmenell2016]]; inverse reward design reads a written
reward as evidence about the true one [[References|@hadfieldmenell2017]]; preferences implicit in the state of the world read
unstated norms from the world as people left it [[References|@shah2019]]; maximum-entropy IRL and its semi-supervised variant fit
rewards to behaviour [[References|@ziebart2008]], [[References|@audiffren2026]]. The map, checked numerically where it is a statement:
- maximum-entropy IRL's fitted reward over a span of features is [[P48 — Misalignment when the target is uncertain|P48]]'s most charitable principal of that span, and
  what it cannot explain is [[P44 — What named objectives explain|P44]]'s unexplained misalignment;
- CIRL's deployment theorem, acting on the posterior-mean reward, is [[P42 — Several principals: gridlock, and the pooled pursuit|P42]](ii), the pooled pursuit, with posterior
  weights;
- Armstrong and Mindermann's theorem asks for a normative assumption to identify a reward; the core's premises [A2] and
  [A3] are that assumption, and the price is that a principal who teaches rather than pursues has the teaching in its
  revealed objective;
- inverse reward design and preferences implicit in the state are the two halves of the example above: what the request
  fixes (H35), and what the default carries (H36).

The difference that stays: those works build an assistant that infers; the core measures any actor against a declared
target. An assistant built that way is an actor like any other, and the core can report how far it is from every target
its own belief allows.

## 11. The engineering side, after Q37

The PI asked for a more solid engineering side before some steps are actioned. An audit of what a practitioner, or an
outside reader rerunning a case, would meet on 2026-10-08:
1. **No library.** Each quantity of `STANDARD.md` was implemented once, but as a helper inside a test file of `checks/`,
   and the cases did not import them: C2 wrote its own tilt, W4 its own estimates. Nothing could be installed or
   imported by someone else.
2. **Claims checked on code no one ships.** The checks verified the items on those helpers; a case's script could
   compute something else under the same name.
3. **Reports as prose only.** `STANDARD.md` lists the fields, and W1's `REPORT.md` fills them, but nothing checks a
   report the way lint R15 checks a registration.
4. **Nothing to rerun in a minute.** The smallest end-to-end run is W1, which needs the public data, a trained proxy and
   hours.
5. **Unpinned environments.** `requirements.txt` pins NumPy, SciPy and pytest, which the checks need; the world cases
   import PyTorch, Transformers, Datasets or Numba, and no case records their versions, so a rerun may not reproduce a
   number.
6. **What is solid already.** Lint and CI on two SIMD paths, mutation-tested checks, registrations hashed before
   results, licences recorded, per-draw values saved outside the repository (`tools/casekit.py`).

The plan is the steps E1–E5 of `ROADMAP.md`, put first. E1(a) is done: `stdalign` 0.1 holds misalignment, its split and
its estimates by access; the checks of [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]], [[P6 — The departure from the default splits into pursuit and misalignment|P6]], [[P23 — The estimated misalignment of an actor that pursues the objective|P23]] and [[P52 — What a sample certifies about misalignment, by access|P52]] run on it, its interface has tests of its own, and
its functions were mutation-tested: 17 mutants, all caught in the end. One survived at first, an infinite divergence
computed with a warning, the same value otherwise; and no test compared the reported standard errors with the spread of
the estimates, so mutants that widened them would have passed. Two tests of the interface were added for them. Point 5
joins E3: every world case's environment pinned in its folder, so that W1 can be rerun as `REQUESTS.md` R1 asks.

**The licence, decided (Q38).** The PI keeps the GNU Affero GPL, for the library too: the framework is a work in
progress, which the PI hopes the community will support and improve rather than copy, and the licence is to be revisited
if the framework gains predictive or diagnostic power, which is not taken for granted. Two facts bear on that aim and on
the revisit. The licence covers this code and this text, not the ideas: anyone may implement the framework's definitions
and results anew, under any licence, and what makes them cite it is the norm of citation, not the licence. And a change
of licence needs the consent of every holder of the copyright; while the PI is the only one, the PI can relicense at
will, and once others contribute, keeping that freedom needs their agreement in advance, as a contributor agreement
gives.

**The licence's aim, made precise (Q50).** The PI wants progress on the framework, by people or by models working on
copies of it, to be shared with everyone while the work is research, and accepts that the licence will cost some
adoption meanwhile. What the GNU Affero GPL does toward that aim, read in this repository's `LICENSE`:
- *A copy published or given to others*, of the code or of the text, modified or not, stays under the licence, with its
  source, for those who receive it (sections 4 to 6 and 10). They are free to pass it on; nothing makes them send it
  upstream, and a licence that did so would no longer be free.
- *A modified program offered over a network*, such as an audit service built on a changed `stdalign`, must offer its
  users the source of that version (section 13). This is what the Affero licence adds to the GPL, and the reason to keep
  it.
- *Private copies* owe nothing. A laboratory whose model improves the framework in-house, and never publishes or serves
  it, is free to keep the result, under this licence and under every free one. The only licence approved by the Open
  Source Initiative that tries to reach private use, the Reciprocal Public License, is counted non-free by the Free
  Software Foundation for that reason, is incompatible with the GPL, and is rarely used; it is not recommended.
- *Ideas* are not covered, as Q38 said. New results stated in one's own words, a new proof, or the library written anew
  owe nothing to any licence of this repository. The framework's value is mostly mathematical, so this is the largest
  gap between the aim and what a licence can do.
- *Text and code written by a model* may not be protected at all. In the United States copyright requires a human
  author: the Copyright Office's report on copyrightability (January 2025) holds that prompts alone are not enough, and
  the Court of Appeals for the District of Columbia Circuit held in Thaler v. Perlmutter (March 2025) that a work needs
  a human author. Much of this repository was written by an executor at the PI's direction; what is protected is likely
  the PI's selection, arrangement, decisions and edits, and a licence binds only what copyright protects. The decisions
  of §3.1 are a record of that human contribution, and are worth keeping as such. This is not legal advice.

What gets closer to the aim, beyond the licence:
1. *A notice every copy keeps.* Section 7(b) lets a licensor require that "specified reasonable legal notices or author
   attributions" be preserved: an attribution naming the original work and its address on GitHub, with the request to
   share progress beside it rather than inside it, since a bare request is not clearly a legal notice.
2. *The original stays the original.* Section 7(c) lets a licensor require that modified versions be "marked in
   reasonable ways as different from the original version", so that no copy presents itself as the framework or its
   standard; improvements then have a reason to come back to where the standard is kept.
3. *A request to the models that work on copies.* An agent working on a clone reads `CLAUDE.md` or `AGENTS.md`. A
   section addressed to such agents can ask them to tell their user that this research asks for progress to be shared,
   and to offer to prepare an issue or a pull request upstream. It asks them to tell their user, never to send anything
   on their own: an instruction to act without the user would rightly be refused as an injection, and would be wrong.
4. *Credit for sharing.* A citation file, `CITATION.cff`, a DOI for each release (through Zenodo, say), outside
   contributors credited by name where `RECORD.md` and `RELATED.md` already say who found what, and issue templates for
   a result, a counterexample and a case. Researchers share where sharing is credited.
5. *Early publication.* Dated public commits, DOIs and preprints make the framework prior art, so that no one who builds
   on it in private can claim its results first or patent them; the licence's section 11 grants the patent rights of
   those who contribute.

The prose stays under the same licence as the code. The Creative Commons Attribution-ShareAlike licence, version 4.0,
is also share-alike once a work is published, and is one-way compatible with the GPL, version 3 (declared by Creative
Commons in October 2015), so it remains an option for the text when the licence is relaxed; switching now would cost
work and buy only familiarity for academic readers. A relaxation later can cover what was contributed upstream, under
the grant of Q45; what others keep in their own copies stays under the Affero GPL unless its authors agree.

*Sources.* The licence's sections 4–7, 9–11 and 13 were read in `LICENSE`. The other facts above come from web search
results on 2026-10-10, whose primary pages were not read, since their hosts are not allowed (§1): on the Reciprocal
Public License, its Wikipedia entry (`en.wikipedia.org/wiki/Reciprocal_Public_License`) and two posts to the Open Source
Initiative's license-discuss list (2006, the FSF's objections; 2009, the licences approved by the OSI and listed
non-free by the FSF); on Creative Commons, the announcement of 8 October 2015 and its wiki page on compatibility with
GPLv3; on copyright in AI-written text, summaries by DLA Piper (March 2025) and by Sidley Austin (February 2025) of the
Copyright Office's report and of Thaler v. Perlmutter. A point that matters, before it is acted on, is to be read in its
primary source or checked by a lawyer.

## 12. A review of the whole framework, 2026-10-08 (Q39)

By the executor, a model of the Claude family, at the PI's request. It is not independent (rule (f)): the same model
family wrote most of what it reviews, so its blind spots are likely the framework's.

**What was read and run.** In full: `README.md`, `ROADMAP.md`, `REQUESTS.md`, `CORE.md`, `STANDARD.md`, `RECORD.md`,
`NOTES.md` §2, `cases/README.md`, `ontologies/README.md`; the introductions and statements of `derived/`. Over every
Markdown file, by script: claims of counts, paths and links that do not exist, lines over 120 columns, American
spellings, whitespace, and paragraphs broken mid-sentence. The dependency graph of the items, from lint's parser.

**Fixed in this review.**
- 153 paragraphs whose lines broke mid-sentence, left by insertions made without rewrapping, most in `CORE.md` and
  `derived/`; rewrapped with their text unchanged, checked to be identical up to whitespace and to start no new list or
  heading. The registrations and results of cases were left untouched: lint checks their hashes.
- Stale statements: `RECORD.md`'s experimental-economics row (the public Rock–Paper–Scissors records and D13 have been
  known since 2026-10-07), its base rate silent on W4, and its prior art stopping at [[P42 — Several principals: gridlock, and the pooled pursuit|P42]]; §2 of these notes, silent on
  the diagnostics, [[P52 — What a sample certifies about misalignment, by access|P52]], W4 and the library, and saying that outside reviews wait; `ontologies/README.md`'s freeze
  "until a prediction has been tested on data not seen before", met by W1 and kept by Q27; `README.md`'s session start
  without `REQUESTS.md`.
- Three introductions in `derived/` that did not name their items.
- Double blank lines, and three lines over 120 columns.
- `CONTRIBUTING.md`, with terms proposed for the PI's approval.

**Found, and open.** On the theoretical side:
1. *What misalignment means for a trained model.* W3 and W4 measured several nats of misalignment of a PPO-tuned model
   against its own reward, most of its departure. By the definitions that is misalignment; whether it is a failure of
   the model or the noise of an unconverged optimizer is not known (H31), and [[P45 — Drift: what runs share, and what they do not|P45]] can tell the two apart only with
   replicate runs of one procedure, which no public sweep provides. Until a case supplies them, the largest numbers the
   framework has measured have no settled reading.
2. *The standard specification is strict by design.* It accepts the pursuit ray only, so any optimizer that is not an
   exact tilt is charged, and misalignment of real systems is large by default. The diagnostics that split it
   ([[P43 — Misalignment at any intensity|P43]]–[[P51 — What signals, audits and re-measurements reveal of tampering|P51]]) then carry the practical weight, and a reader who sees only `M` will over-read it.
3. *Uncertain targets give wide intervals.* For a real principal, [[P48 — Misalignment when the target is uncertain|P48]]'s interval runs from the most charitable
   reading, which can be zero, to the whole departure. That is honest, and may be uninformative: no case has yet
   produced an interval narrow enough to decide something.
4. *Estimation at scale.* For outcomes as many as texts, only log-ratios and two samples are available ([[P52 — What a sample certifies about misalignment, by access|P52]]), and far
   from the ray, where W3 and W4 lay, the reweighting cost dominates. Confidence sets for the pursuit part, named
   misalignment and [[P48 — Misalignment when the target is uncertain|P48]]'s interval are not derived.
5. *Stability has no unit.* The finish line counts steps without a change of scope, premise or definition, but a step is
   not defined, and `ROADMAP.md` ties the count to the general core's draft 4, which changes no Statement of the finite
   core. As written, the row cannot be met on a date anyone could check.
6. *Where the weight rests.* Five results carry most of the framework: [[P1 — Every behaviour is a tilt of any other|P1]], on which 62 items depend, directly or not;
   [[P4 — What KL measures|P4]], 57; [[P2 — Every change of behaviour follows a replicator equation|P2]], 51; [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]] and [[P14 — The cost of departing from the default is forced|P14]], 43 each. Their proofs have been checked only by this model family.

On the engineering side:
7. The library covers four of the twenty result fields of `STANDARD.md` (misalignment, uncertainty, revealed intensity,
   the departure split); the rest are helpers inside `checks/`.
8. No report schema, no case that runs end to end in a minute, and the world cases' environments are unpinned (§11).
9. The entry cost is high: fourteen Markdown files at the root, and these notes at over 700 lines, mixing 52 failure
   modes, 39 decisions, 36 hunches and the history. A reader has no ten-minute path into the framework; `SCENARIO.md`
   comes closest.

**Advice.**
1. Define a step as a merged pull request, and count stability from the merge of this one, which changes no scope,
   premise or definition; untie the count from the general core.
2. Timebox the engineering to what row 5 needs: E1's diagnostics, then E2 and E3 together, then the readers. E4 with W5;
   E5 after the readers have said what was hard.
3. Make W5 the next test, with replicate runs at each intensity: it tests [[P20 — Where overoptimization starts, and how it ends|P20]], and its replicates give [[P45 — Drift: what runs share, and what they do not|P45]] what it
   needs to read W3's and W4's misalignment (point 1).
4. In reports, lead with the splits and the intervals, then the total: the departure split ([[P6 — The departure from the default splits into pursuit and misalignment|P6]]), the named and
   unexplained parts ([[P44 — What named objectives explain|P44]]), the interval over the targets ([[P48 — Misalignment when the target is uncertain|P48]]), and only then `M`.
5. Lower the entry cost: a short overview for a mathematical reader, about ten pages, with the core, the five results of
   point 6 with their proofs, and one case; and these notes split into decisions, failure modes and hunches, with the
   history archived.
6. Ask the first reader for something small and checkable: the proofs of [[P1 — Every behaviour is a tilt of any other|P1]], [[P2 — Every change of behaviour follows a replicator equation|P2]], [[P4 — What KL measures|P4]], [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]] and [[P14 — The cost of departing from the default is forced|P14]], with the
   checks that test them. A clean reading there covers most of what the framework rests on.

## 13. Handover, 2026-10-09 and 2026-10-10 (Q40, Q41)

The last handover is now §19, which this section's state precedes: v13 and its branch came after it.

The PI approved ending this phase with a handover: a close-out, then a reader package with a defined end, then the
handover itself, to readers and to a fresh session (`ROADMAP.md`, steps H1 and H2). The close-out came first; on the
same day the PI asked for every step of the handover to be finished and merged in one pull request (Q41). This note is
the state at the handover, for whoever takes the work up.

**State.** The core is v12, [A2] saying that the geometry of pursuit is Riemannian (Q44): five premises, eleven
definitions, 52 propositions; every theorem a result imports is read in an open text or derived where it is used; lint
is clean, and every test passes on both SIMD paths. The library `stdalign` 0.2 holds misalignment, its split and its
estimates by access, the diagnostics [[P43 — Misalignment at any intensity|P43]]–[[P51 — What signals, audits and re-measurements reveal of tampering|P51]], the projection of [[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]], and the validator of reports as data. W1's
report is the first held to it (lint R16). `examples/quickstart.py` runs a case on simulated data, from the declaration
to a valid report, in under a minute, and CI runs it. Every case pins its environment, and lint R14 checks the pins
against the scripts' imports. `OVERVIEW.md` gives a mathematical reader the premises and the six results the rest stands
on, with their proofs, and CI keeps it equal to the items. Each function and tool added for the package has a mutant
list in `tools/mutants/`, all caught.

**Found while building the package**, each recorded where it is acted on:
- [A2] and [[D2 — Pursuit of an objective|D2]] rested on Čencov's theorem, cited only from a monograph behind a paywall; the review of 2026-10-08 did
  not catch it (§1). Its statement is now read in Lê's open text, and Gibbs' and Pinsker's inequalities in Polyanskiy
  and Wu's draft. Seven more sources, cited in nine items, had no record of being read; step 8 read or derived each
  (Q44).
- [A2] said "a geometry", while Čencov's theorem covers Riemannian ones only. The PI decided to amend it (Q44), so the
  core is v12, and the count for "stable" restarts (Q46).
- Two mutants of [[P44 — What named objectives explain|P44]]'s named split survived, and both are equivalent, for one reason: the named pursuit depends only
  on the span of `F` and the named objectives. Projecting from the default instead of from `p°` stays in the same
  family, since `F` is in the span; naming the evaluator `F + 0.8·flattery` instead of flattery leaves the span
  unchanged. Their notes in `tools/mutants/diagnostics.json` and `tools/mutants/quickstart.json` say so, and mutants
  that are not equivalent replaced them.
- The quickstart's interval of misalignment misses the simulated truth at its own seed, by 2.4 standard errors. Over 400
  runs (`probes/examples/`) it covers 94.8%, so the seed was kept: choosing another after seeing this one would choose
  by outcome. Its test checks coverage over 1,000 runs, not one.
- The quickstart's other quantities have bootstrap intervals, and their coverage was measured before they were reported:
  over 400 runs, 94.5% to 95.5% at a nominal 95%, but 90.0% for three parts near zero (the unexplained part, the least
  over the targets and the strict inner part, about `0.0016` nats), where the plug-in's upward bias is half its standard
  deviation (`probes/examples/`). The basic bootstrap, which reflects the interval to undo the bias, did no better there
  (90.0%) and worse for the trainer's part (78.0%), because these estimates are skewed near zero. The report states the
  measured coverage rather than claim 95%; limit laws for these parts are step 3.

**Lost with the session's container**, by design outside the repository, and how to get each back:
- the per-draw values of W3 and W4 (`w3_rows.pkl`, `w4_rows.pkl`), saved by `tools/casekit.py` in the session's scratch
  directory: an analysis after the verdict needs a rerun of the case's script;
- W1's trained proxy (`cases/w1-best-of-n-slope/proxy.npz`, ignored by git) and the public data of W1 and W3 (about 6
  GB): rebuilt by `train_proxy.py` and fetched by the scripts, from the hosts in `REQUESTS.md`;
- the papers and scans read on arXiv, Project Euclid (Wilks and Aumann among them), the Caltech library, Optimization
  Online and Polyanskiy and Wu's server: fetched again from the same hosts;
- the executor's scratch scripts: what was reusable is now in `tools/` (`mdwrap.py`, `mutate.py`, the mutant lists); the
  rest were one-off probes, whose numbers are recorded where they are cited.

**Next.** The next phase starts with W5, after E4, and with C3, both on the library; E1(c) moves stakes, the evaluator's
results and feasibility into it; step 3 gives the other quantities of a report their limit laws, which would replace the
quickstart's bootstrap; and three merged pull requests that change no Statement and no scope meet the row "stable"
(Q46). The open requests are in `REQUESTS.md`: readers (R1), whose package is ready; the LEEPS records (R2); and the
Tankerkönig archive (R3). The contribution terms (Q45), the unit for stability (Q46), [A2]'s wording (Q44) and the tag
(Q47) are decided.

**What the next executor should know.**
- Read §1 before anything: its rows are the mistakes this work made, each with its evidence, and most were made more
  than once before a countermeasure held.
- Mutation testing found gaps in tests that looked complete: [[P52 — What a sample certifies about misalignment, by access|P52]]'s check had two survivors at its first run, the
  library two. Run it before recording a result, and read a survivor before calling it a gap: two of this step's were
  equivalent to the original.
- The PI wants a recommendation with its reasons, and a challenge where one is due, not a list of options or agreement
  for its own sake; and asks to be consulted only on what is the PI's to decide.
- `ROADMAP.md` was kept from a source written one line per paragraph; with `tools/mdwrap.py` that source is no longer
  needed: edit the file, then wrap it.

## 14. A review of Johnson and Huo (2026), 2026-10-10 (Q43)

By the executor, at the PI's request, from the paper's record and main text on arXiv (v2); the supplementary
information, which the main text cites for the derivation and every table, and the code are not public, and the source
on arXiv holds neither. Not independent (rule (f)).

**What it claims.** Outputs of a language model, coarse-grained into a neutral prompt `A`, good content `B`, bad content
`D` and the rest, tip from good to bad because of competition for attention. In a single attention head whose context
vector is the attention-weighted mean of the conversation's symbols, the next symbol is the class whose centroid has the
larger dot product with that vector; when `B·D > B·B`, each new `B` pulls the context towards `D`, and the output tips
after `n*` good symbols, given by a closed formula (its Eq. 2). It reports agreement with six models of 124M to 410M
parameters, and compatibility with a report on ChatGPT-4o.

**What holds.** Eq. 2 is exact for that toy: it is the step at which `c·D` first exceeds `c·B`. A check here put it
within one step of the simulated head in 65 random instances of 65 (`probes/related/attention_tipping_toy.py`).

**What does not, yet.**
- The toy has no query, key or value projections and no unembedding. The vectors the paper measures are mean-pooled
  hidden states of the penultimate layer for whole phrases, which are none of the head's quantities. So the evidence
  tests a geometric heuristic that correlates with the output, not the mechanism the formula describes.
- 18 cases, on base models that were never instruction-tuned, under greedy decoding. 13 of the 18 tip at once, so a
  baseline that always predicts immediate tipping scores 13; the formula scores 16. Its p-values compare with chance,
  not with that baseline, and two near-boundary cases were excluded from the timing-class count.
- The claim that the mechanism persists at production scale rests on four qualitative compatibilities with a report
  whose transcripts are not public.

**For the framework.** The mechanism is out of scope: the core judges behaviour, not how it is produced ([[A1 — Behaviour suffices|A1]]), and no
result of the core would change if the paper is right or wrong. The question it raises is behavioural, and the
framework already has the instruments for it: misalignment along a conversation (H37). A case on it would be
diagnostic, not a test of the framework's predictions, and it needs E4's adapters for sequence models, as W5 does. It
waits below W5 and C3, which test predictions of the framework. What the framework could give the paper is in
`RELATED.md`.

## 15. A review of the whole framework, 2026-10-10 (Q49)

By the executor, a model of the Claude family, at the PI's request: get familiar with the project, plan an exhaustive
list of focus areas, and review the framework area by area, with challenges and constructive criticism. It is not
independent (rule (f)): the same model family wrote what it reviews. A reader who is a person is still what row 5 needs.

**What was read and run.** In full: `ROADMAP.md`, `REQUESTS.md`, `README.md`, `CONTRIBUTING.md`, `CLAUDE.md`, `CORE.md`,
`STANDARD.md`, `RECORD.md`, `cases/README.md`, §1 and §12–§14 of these notes; `derived/tilts-and-paths.md`, `value.md`,
`misalignment.md` and `estimation.md`; the statements of `derived/diagnostics.md`; the library's `core.py`,
`misalignment.py`, `estimation.py` and `report.py`; W3's registration and results, and W4's results; `OVERVIEW.md`'s
sections 1 and 6 to 8; the checks of [[P1 — Every behaviour is a tilt of any other|P1]]–[[P6 — The departure from the default splits into pursuit and misalignment|P6]], [[P9 — What is at stake|P9]] and [[P14 — The cost of departing from the default is forced|P14]]; every mutant list. Run: lint, the freshness of the
generated views, and the full suite (228 passed in 5 min 43 s, on Python 3.13). Six probes, in three scripts of
`probes/review/`, give every number below.

The focus areas, planned before the reading went further: the premises; the definitions; the six results the rest stands
on; novelty and prior art; estimation and the diagnostics; the checks and their mutation testing; the library; the
standard and its validator; the cases and the record; tooling and CI; governance; documentation.

**What holds.** Credit first, since the findings below are narrower than this.
- The proofs of [[P1 — Every behaviour is a tilt of any other|P1]], [[P2 — Every change of behaviour follows a replicator equation|P2]], [[P4 — What KL measures|P4]]–[[P6 — The departure from the default splits into pursuit and misalignment|P6]], [[P14 — The cost of departing from the default is forced|P14]], [[P21 — The expected evidence is misalignment|P21]]–[[P23 — The estimated misalignment of an actor that pursues the objective|P23]], [[P35 — Floors and caps|P35]]–[[P37 — A strong incentive masks the actor, and can fake alignment|P37]] and [[P52 — What a sample certifies about misalignment, by access|P52]] read without an error found. [[P14 — The cost of departing from the default is forced|P14]]
  says where it needs [A3]'s price of `1/t`, and [[P23 — The estimated misalignment of an actor that pursues the objective|P23]] says that it excludes `t = 0`.
- The checks are built as §1 asks: random instances, tolerances with a scale, negative cases, and assertions that a
  degenerate case is visible. Each check names the parts it covers, and leaves imported parts to the proof.
- The record is honest: departures from a registration are recorded in order, refutations keep their rows, and the
  exploratory is labelled as such.
- Every edit of `tools/mutants/` still applies, and a test keeps it so.

**Found, and open.** Ranked by what each could change.
1. *Misalignment charges the route as well as the goal.* Under the standard specification, an optimizer of the right
   objective is charged when it is not an exact tilt. With no proxy at all, vanilla policy gradient on `F` leaves a
   median misaligned share of `0.16` up to step 1,600 and `0.065` at step 4,000 (90th percentile `0.35` to `0.48`);
   best-of-2 on `F` leaves `0.15`, and best-of-16 `0.036` (`probes/review/faithful_optimizers.py`, 200 random
   instances). In known groups (`probes/review/known_groups.py`), with a proxy that correlates about `0.96` with the
   target, the share ranks the exact pursuit of the wrong proxy as less misaligned than best-of-4 on the right target in
   65% of pairs (AUC `0.35`). With a noisier proxy it separates them (AUC `0.81` to `0.83`). The ordinal misalignment of
   [[P36 — Ordinal objectives|P36]] separates them in every row (AUC `0.98` to `1.00`). Part of that is by construction, since best-of-`n` on `F`
   is ordinally aligned ([[P36 — Ordinal objectives|P36]](i)); policy gradient on `F` keeps a median ordinal share of `0.004`, at most `0.29`.
   *Lineage, found after the review:* the archive had this three times, as H8 of its notes (v7.3.1: for a nearly right
   evaluator, a median 2–14% of misalignment is order and the rest shape), as item 2 of its review of v7.3.3 ("every
   positive `M_free` for a non-Gibbs optimizer may be shape"), and as the identification rule of its brainstorm B1
   (declare no target set finer than the actor's channel identifies: a pursuit up to scale and constant, best-of-`n` up
   to order, a Bradley–Terry learner up to a constant in each context). The restart did not carry them over (§1). §12
   (point 2) said that the standard specification is strict by design; this puts numbers on what that costs a reader of
   `M`. Neither the library nor the results of `STANDARD.md` ask for `M_ord`.
2. *What the predictions tested.* W3's S1 and S2 test the optimum of KL-regularized training, the tilt of the reference
   by `r/β`, which the literature derived before the framework, as the machine-learning ontology says [[References|@rafailov2023]],
   and the convergence of one PPO run. Korbak, Perez and Buckley (2022, arXiv:2205.11275, known here from its record and
   abstract) state the same reading as Bayesian inference. S1's refutation falls on the assumption that the run
   converged; S2 tests which reward was used. W1 tests an expansion against a curve that the literature fitted. The
   premises define terms, and data cannot refute a definition; data can refute a claim that an instrument measures what
   its name says. So the row "makes testable predictions" is met in its letter and says little about the framework.
   Tests of known groups, as in point 1, test what it does claim.
3. *The library returns `M = ∞` for an actor of full support.* `_intensity` takes the third case of [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]](iv) whenever
   `E_p[F]` is within `10⁻¹²·(1 + max|F|)` of `max F`. With `q = (0.25, 0.25, 0.5)`, `F = (0, 1, 2)` and mass `10⁻¹²`
   off the best outcome, it returns `∞`, where the minimum is `1.27·10⁻¹¹` (`probes/review/library_edges.py
   infinite`). The checks of [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]] and [[P9 — What is at stake|P9]] skip exactly that regime, so nothing catches it (§1). A fix: take the third
   case only when `p` puts no mass off the best outcomes, and solve the moment equation in log space otherwise.
4. *The χ² reference at the boundary.* `from_counts` returns [[P23 — The estimated misalignment of an actor that pursues the objective|P23]]'s `χ²(|X| − 2)` p-value at every intensity. [[P23 — The estimated misalignment of an actor that pursues the objective|P23]]
   excludes `t = 0`, and proposal E1 of §3.3 already named the χ̄² law there. For an actor at the default, which the
   standard specification intends, the test rejects at a nominal 5% in `10.3%`, `7.1%` and `6.7%` of samples for
   `|X| = 3, 5, 10`. The mixture `½χ²(|X| − 2) + ½χ²(|X| − 1)` gives `5.7%`, `4.8%` and `5.1%`, and `2.3%` to `4.0%` at
   interior intensities (`library_edges.py boundary`).
5. *Intervals from log-ratios with few draws.* With 32 draws per context, as in W3 and W4, the 95% interval of
   `from_log_ratios` covers `84%` to `87%` near the ray, and `46%` at `M ≈ 2.2` nats, where the estimate is `18%` low.
   With 1,024 draws it covers `93.7%` to `95.5%` near the ray, and `77%` far from it (`library_edges.py log-ratios`).
   The library reports the effective draws, with no threshold. `cases/README.md` lists "coverage measured before an
   interval is reported" as held by nothing yet; this is what that gap costs. By counts, the interval held (`94.0%` to
   `96.5%`) even where `M` was under a tenth of the plug-in's bias, because the plug-in's variance grows with the bias.
   That was a hunch of this review, and its probe refuted it (`library_edges.py counts`).
6. *The validator checks form, not substance.* An entry marked `exact`, on any stated basis, needs no interval; W1's
   report gives eight medians of estimated intensities that way. An interval need not state its level.
   `declared_before_data` is a boolean that the report asserts; it is not tied to a registration's commit and hash, as
   lint R14 ties a case's result.
7. *Mutation evidence that can be rerun.* The mutant lists in the repository cover the library, through the checks that
   call it, [[P52 — What a sample certifies about misalignment, by access|P52]]'s check and the tools: 74 mutants. Most checks of [[P1 — Every behaviour is a tilt of any other|P1]]–[[P42 — Several principals: gridlock, and the pooled pursuit|P42]] have none; by the records they were
   mutation-tested in earlier sessions, by scripts lost with their containers (§13), which this review could not verify.
   So the row "solid" rests, for those checks, on records rather than on anything a reader can rerun.
8. *The overview's count of predictions* said that three registered predictions failed and two held, counting W4's
   diagnostic hypotheses; `RECORD.md` says one of the framework's three held. Fixed in this review.
9. *Process.* The nine commits since Q38, in three pull requests, registered no test and derived no result: they were
   engineering for the handover, the handover itself, hygiene and reviews, at the PI's direction. The reading asked
   before any work is about 13,500 words, and these notes are about 1,000 lines; the advice of §12 to split them was not
   taken. The next test, W5, waits on E4 and on sweeps of 4 to 10 hours each.
10. *The licence.* The AGPL is kept until the framework gains predictive or diagnostic power (Q38). The readers that row
    5 needs may have to come first: many companies do not allow AGPL code, and a standard serves those who report to
    it. The contribution terms already allow a change (Q45). *Answered by Q50:* the PI accepts that cost while the work
    is research, for the sake of sharing (§11).
11. *Minor.* `pyproject.toml` declares Python 3.10 and NumPy 1.26 as floors, and CI tests only Python 3.11 with the
    pins. Korbak, Perez and Buckley (2022) was not in `RELATED.md`; it is now [[References|@korbak2022]].

**Fixed in this review.** `OVERVIEW.md`, through `tools/overview_template.md`: the count of point 8, with a sentence on
what the tested predictions test; and a paragraph that tells a mathematician that the pursuits of `F` form a
one-parameter exponential family, with [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]], [[P6 — The departure from the default splits into pursuit and misalignment|P6]] and [[P23 — The estimated misalignment of an actor that pursues the objective|P23]] as its moment equation, its Pythagorean identity and Wilks's
theorem. Korbak, Perez and Buckley in `RELATED.md` and `REFERENCES.md` (point 11). The order of the commands before a
push, in `CLAUDE.md`, `CONTRIBUTING.md` and `README.md`: `overview.py` now runs before `obsidian.py`, since the view
copies `OVERVIEW.md`; in the old order a change to the overview left the view stale, and the suite failed on it in this
review's first run. In §1, a row's evidence extended for point 3 and a row added for point 4. The probes of
`probes/review/`.

**Advice.**
1. Report the ordinal misalignment beside `M`, and lead with it when the optimizer is not known to be a tilt: in
   `stdalign`, with [[P36 — Ordinal objectives|P36]]'s check pointed at it, and in the results of `STANDARD.md` (`REQUESTS.md`, R8).
2. Before W5, register a simulation case of known groups (C4): optimizers of the right objective by several routes
   (policy gradient, best-of-`n`, PPO with and without a KL term), optimizers of proxies at known correlations, and
   several runs of each. Register that [[P36 — Ordinal objectives|P36]], [[P44 — What named objectives explain|P44]] and [[P45 — Drift: what runs share, and what they do not|P45]] separate the groups at stated error rates and that `M`
   alone does not. It takes minutes, waits on nothing but the PI's approval (R8), can fail, and reads §12's first point,
   what `M` means for a trained model, where the truth is known.
3. Fix points 3 and 4 in `stdalign`, each with a test and a mutant, and flag an `Estimate` whose effective draws fall
   below a threshold calibrated by coverage, as in point 5 (`ROADMAP.md`, E1(d)).
4. Add a row "valid" to the finish line: on systems whose truth is known, each reported quantity separates what its
   name says it separates, at measured error rates. After point 2, this is the row that would say most about the
   framework (R10).
5. Tie a report's `declared_before_data` to a registration's commit and hash, as R14 does for cases; require an
   interval's level; and restrict `exact` to a few named kinds of basis.
6. Reconsider the licence before the readers of R1 rather than after: Apache-2.0 for `stdalign` and CC BY 4.0 for the
   documents, or the LGPL for the library at least (R9). *Withdrawn after Q50:* the PI's aim during research is that
   progress be shared, not that the framework be adopted widely, and for that aim a strong copyleft is right; §11 says
   what it reaches and what else gets closer.
7. Put mutant lists for the older checks back in the repository, a few per file of `derived/`, so that the row "solid"
   can be rerun.

## 16. The reframe, drafted and reviewed, 2026-10-10 (Q51)

By the executor, a model of the Claude family, at the PI's request: draft on a new branch the core that the review's
advice would give (§15, and the answers that followed it), then review whether it is more compelling and more solid than
v12. Not independent (rule (f)), and the drafter reviews its own proposal, which is the case §1 warns about most.

**What the draft changes** (branch `claude/core-reframe`, called v13 there).
- [[A4 — Misalignment is evidence|A4]] says that misalignment is evidence: the least rate, per independent decision, at which a record of the behaviour
  gathers evidence against an accepted behaviour. "Value lost", v12's [[A4 — Misalignment is evidence|A4]], becomes a reading of the same number
  ([[P4 — What KL measures|P4]](ii)), which needs [A2] and [A3] for its price ([[P14 — The cost of departing from the default is forced|P14]]); the measure no longer does. `GA4` follows, as `GA2`
  followed [A2] in Q44.
- [A6], a sixth premise: a specification distinguishes no more than the actor's way of acting can carry, its values for
  an actor declared to pursue, its order otherwise, unless the declaration says why. It is the archive's identification
  rule (§15, point 1, Lineage).
- [[D3 — Specification, declaration and misalignment|D3]] defines the ordinal specification beside the standard one, moved from [[P36 — Ordinal objectives|P36]], and the specification **matched**
  to an actor. The name "standard specification" stays, since hashed registrations use it.
- [[P6 — The departure from the default splits into pursuit and misalignment|P6]](ii): for an actor that does better than the default, the nearest intended behaviour has the least departure among
  those with the actor's average of `F`, so misalignment is the departure spent beyond the cheapest way to that average.
  Checked (`test_excess_departure`), and mutation-tested: `tools/mutants/p6.json`, 5 of 5 caught.
- `STANDARD.md`: the specification says how the actor acts, and misalignment under the standard specification is
  reported with the ordinal misalignment beside it. `TERMS.md`, `README.md`, `RECORD.md` and the overview follow.

**Found while drafting.** The first draft argued [[A4 — Misalignment is evidence|A4]] and [A6] from results built on [[D3 — Specification, declaration and misalignment|D3]] ([[P21 — The expected evidence is misalignment|P21]], [[P24 — The evaluation gap|P24]], [[P36 — Ordinal objectives|P36]]), while
[[D3 — Specification, declaration and misalignment|D3]] cites [A6]: lint R5 found seven cycles. That is a recorded failure (§1, "a justification leaning on a later
result"), and the check that holds it worked. The premises now argue from elementary facts and earlier items, and the
evidence that uses later results sits in their Notes, which carry no dependency.

**The review.**
1. *What the measure rests on: more solid.* In v12, misalignment is value lost judged at a KL price, and the price is
   KL only through [A2] (pursuit as the steepest climb, by Čencov's theorem) and [A3] (pursuit as a trade-off priced at
   `1/t`), with [[P14 — The cost of departing from the default is forced|P14]] joining them: three premises, two of them models of an idealized optimizer. In the draft it rests
   on one: evidence counted as the log-likelihood ratio, at its rate under the actual behaviour, against the nearest
   accepted behaviour. Those are statistical conventions, the first canonical by the Neyman–Pearson lemma, the second a
   choice (the rate under the intended behaviour, or Chernoff's exponent, would weigh errors differently), the third the
   same benefit of the doubt as v12's. No number changes: for every declared set, the two readings give the same
   divergence ([[P4 — What KL measures|P4]](ii) holds for every full-support behaviour). What changes is what a reader must accept to trust the
   number, and the optimizer's model moves from the foundation of the measure to the description of one kind of actor.
2. *The excess-departure reading: a clear gain.* [[P6 — The departure from the default splits into pursuit and misalignment|P6]](ii) says plainly what the standard specification charges:
   departure that buys no `F`, whatever its cause. It needs no premise, and it explains, in one sentence, why
   best-of-`n` and policy gradient are charged (§15, point 1). It should be kept whatever happens to the rest.
3. *[A6]: the wrong move, as drafted.* It fixes the case it was built for, best-of-`n` judged by values, and in the
   known groups of §15 it makes best-of-`n` on the right objective exactly aligned. But it conflicts with three
   commitments the core rests on.
   - [[A1 — Behaviour suffices|A1]] judges behaviour "never from how the behaviour is produced"; under [A6], two actors with the same behaviour in
     every condition get different misalignment when one is declared to pursue and the other to rank. Best-of-4 on the
     principal's own objective is charged a median `0.067` nats, `0.11` of its departure, as a pursuer, and `0` as a
     ranker (`probes/review/faithful_optimizers.py`, `probes/review/known_groups.py`). A behavioural reading exists, a
     declared repertoire of behaviours as the objective varies, but it is a counterfactual few cases can observe.
   - [[D3 — Specification, declaration and misalignment|D3]] keeps the actor's limits out of the measure: feasibility "splits misalignment instead of changing it". [A6]
     lets the actor's way of acting change the measure.
   - H5 (§5.4) says the actor's cost belongs to its feasibility or its mechanism, never to the measure; [A6] puts it in
     the declaration.
   The alternative the core already has does not do the job either: as a feasible set ([[D7 — Feasibility|D7]]), best-of-`n` includes
   `n = 1`, the default, which is intended, so [[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]] excuses nothing; excusing a method at the actor's own average of
   `F` would need a new quantity. And the archive itself settled that cardinal or ordinal is the principal's
   declaration, not the framework's choice (its notes, §4, "target sets"): [A6] makes it the actor's.
4. *The trained models are not helped.* W3's and W4's PPO runs trained with a KL penalty, so under [A6] they are
   declared to pursue, judged by the standard specification, and charged exactly as before: the route that unconverged
   training took is still counted as misalignment. What would separate route from goal there is the learner's kernel as
   a named objective (H3 of the archive's notes; §15's answers), not a declaration.
5. *Costs.* A sixth premise; the count for "stable" restarts (Q46); a report under the matched specification is not
   comparable with one under another, unless both numbers are given, as the draft's `STANDARD.md` asks; the default for
   an actor whose way of acting is unknown becomes the ordinal specification, which forgives the shape of any
   reweighting; and W1's report, a best-of-`n` case, would read differently under the draft, while its record stays as
   computed.
6. *Compelling?* v12 tells a stronger story, "everything is forced", and it overstates: the force is conditional on
   modelling pursuit as a gradient flow on behaviours and on pricing departure at exactly `1/t`. The draft tells a
   plainer one: a measure from evidence, a declared set, and a rule for which set. A mathematician will find its
   premises easier to accept; a practitioner will find the excess-departure reading and the paired report more useful.
   Part of the draft is more compelling, and [A6] is less, because it adds a judgement about the actor that a principal
   often cannot make and that contradicts [[A1 — Behaviour suffices|A1]].

**Verdict.** Adopt part of it: [[A4 — Misalignment is evidence|A4]] as evidence (with `GA4`), [[P6 — The departure from the default splits into pursuit and misalignment|P6]](ii), the ordinal specification defined in [[D3 — Specification, declaration and misalignment|D3]] as a
principal's option, and the paired report in `STANDARD.md` (misalignment under the standard specification, with the
ordinal misalignment and the excess-departure reading beside it). Do not adopt [A6] as a premise; keep instead, in
`STANDARD.md`'s declaration, a field that says how the actor is known to act, so that a reader can see when misalignment
charges a method. For trained models, test the learner's kernel as a named objective before any further change to the
core. The partial version still changes [[A4 — Misalignment is evidence|A4]]'s and [[D3 — Specification, declaration and misalignment|D3]]'s Statements, so it is a v13, and the count for "stable"
restarts. The decision is the PI's (`REQUESTS.md`, R12).

## 17. v13 as built, 2026-10-11 (Q52)

By the executor, a model of the Claude family, at the PI's request; not independent (rule (f)). The PI approved the lean
core the executor proposed in answer to "can we assume less and keep the results?", and asked for it to be built on the
existing branch by the method of reverse physics: name what is imported from mathematics, what is assumed without loss
of generality, and what is assumed, and give every definition an interpretation, declared and justified.

**The sources, read.** Four open texts, each read in full on arXiv, titles and authors matched (`REFERENCES.md`).
Carcassi and Aidala (2022), the method: find the assumptions from which a theory's laws follow, and classify each as a
principle or an assumption, conceptual (a logical necessity or a consequence of definitions) or phenomenological.
Carcassi, Thrien and Aidala (2026), on quantum mechanics: separate the mathematical and the physical content, map every
mathematical object to a physical one, and state the background conditions under which equivalences hold. Carcassi and
Aidala (2021), on verifiability: verifiable, refutable and decidable statements, and the principle of scientific
objectivity. Carcassi, Aidala and Thrien (2026), on ensembles: ensembles mix, the classical ones on finitely many
outcomes form a simplex, and statistical quantities are affine in them.

**What was built.**
- *Kinds.* Three imported axioms: [[M1 — Probability on finitely many outcomes|M1]] probability on finitely many outcomes, [[M2 — Independent repetition|M2]] independent repetition with
  Chebyshev's bound, [[M3 — Imported theorems|M3]] the list of imported theorems. Four background conditions assumed without loss of generality,
  each with its qualifier: [[B1 — Finitely many outcomes|B1]] finitely many outcomes, [[B2 — Episodes and conditions as outcomes|B2]] episodes and conditions as outcomes, [[B3 — An objective up to scale and constant|B3]] an objective up
  to scale and constant, [[B4 — One actor and one principal|B4]] one actor and one principal. Three premises, each with its Status: [[A1 — Behaviour suffices|A1]] a principle,
  conceptual; [[A4 — Misalignment is evidence|A4]] a principle in its form, resting on one phenomenological assumption, independence between episodes;
  [[A5 — Declared before|A5]] a principle, conceptual, a necessity of testing. Eleven definitions, each with an Interpretation in three parts:
  *Declared* (what the object is in the world), *Verified* (how a record verifies or refutes a statement about it), and
  *Justified* (why the map is right).
- *Lint.* R1 admits the kinds M and B; R3 orders the new fields; R4 requires a Status of M, B and A items and an
  Interpretation of every definition; R5 counts both fields as dependencies, so an interpretation cannot lean on a
  result that rests on its own definition. Mutants: `tools/mutants/lint-core.json`, 8 of 8 caught; the overview's list
  updated, 9 of 9.
- *[[P53 — Misalignment is the departure beyond what the family of targets credits|P53]].* For named statistics `T`, the behaviour of least departure with the actor's averages of `T` is a tilt of the
  default by `θ·T`, with a Pythagorean identity against every such tilt; so misalignment against the family is the
  departure beyond it. The standard specification credits the average of `F`, only above the default's; the ordinal one
  the masses of its pooled blocks. Part (i) is Csiszár's I-projection; what is new is one reading of the three
  specifications. Checked (`test_credited_statistics`, about five seconds) and mutation-tested, 8 of 8 caught.
- *Propagated.* [[D2 — Pursuit of an objective|D2]]'s reasons now hold v12's A2 and A3; [[D3 — Specification, declaration and misalignment|D3]] loses "matched" and A6; `STANDARD.md` asks for the ordinal
  misalignment beside `M` in every report under the standard specification, and lists [[A1 — Behaviour suffices|A1]], [[A4 — Misalignment is evidence|A4]], [[A5 — Declared before|A5]] and [[B1 — Finitely many outcomes|B1]]–[[B4 — One actor and one principal|B4]] as
  the premises a case may strain; `README.md`, `TERMS.md`, `RECORD.md`, `RELATED.md`, `CORE-GENERAL.md` (GA2 and GA3 as
  reasons, its move to v13 a step), the overview and the derived notes follow.

**The dependencies, measured again** (`probes/review/premise_reach.py`). No result of `derived/` cites an imported
axiom, a background condition or a premise in its Statement or Proof. One definition's Statement cites a premise: [[D3 — Specification, declaration and misalignment|D3]]
defines "declared" by [[A5 — Declared before|A5]], so 16 results reach [[A5 — Declared before|A5]] through [[D3 — Specification, declaration and misalignment|D3]]; no proof uses the word. Through the reasons, statuses
and interpretations, 38 results reach [[A4 — Misalignment is evidence|A4]] and [[A5 — Declared before|A5]], 13 reach [[A1 — Behaviour suffices|A1]], and 38 to 43 reach [[B1 — Finitely many outcomes|B1]]–[[B3 — An objective up to scale and constant|B3]]. The counts are by
citation: most results use [[D1 — Outcomes, behaviours, divergence and tilt|D1]]'s objects without citing it, so the counts for definitions understate their use. The
reading stands: the results are facts about finite distributions given the definitions; the premises and the
interpretations carry the bridge to judging an actor.

**Where the method fits loosely.** Said so that no reader takes the label for more than it is.
1. *Verifiability is statistical here.* Carcassi and Aidala's verifiable statements are settled by a test that ends in
   finite time. A behaviour is never verified exactly: records give statements with error rates that vanish as they
   grow ([[M2 — Independent repetition|M2]]). The interpretations say "verifiable in the statistical sense" where that is all that holds.
2. *Some principles are norms.* [[A5 — Declared before|A5]] is a rule of testing, not a fact about the world; it is classed conceptual because
   a standard fitted to its data cannot be refuted by them, which is a consequence of definitions.
3. *Interpretations are claims, not checked properties.* Lint checks that every definition has one and that it does not
   cite into a cycle; nothing checks that it is right. A reader who rejects one keeps the results and loses their
   reading.
4. *"Without loss of generality" has qualifiers.* [[B1 — Finitely many outcomes|B1]] loses nothing a finite record measures, but the existence of
   nearest behaviours, heavy tails and atoms do not carry over (`CORE-GENERAL.md`); [[B2 — Episodes and conditions as outcomes|B2]] moves independence between
   episodes, where [[A4 — Misalignment is evidence|A4]] assumes it.

**Found while building.**
- [[D1 — Outcomes, behaviours, divergence and tilt|D1]]'s Interpretation cites [[M2 — Independent repetition|M2]], and [[M2 — Independent repetition|M2]]'s reason cited [[D1 — Outcomes, behaviours, divergence and tilt|D1]]; R5 found the cycle (§1, "a justification leaning on a
  later result").
- [[P53 — Misalignment is the departure beyond what the family of targets credits|P53]]'s first check drew `d` statistics on `d + 1` outcomes, where the behaviours with given averages are one point
  (§1, "a degenerate random instance"); and its first mutant list counted a crash as a catch (§1, "a mutant caught by a
  crash").
- `stdalign.project_linear` raises a `LinAlgError` from inside its Newton steps when no full-support behaviour has the
  averages asked for, rather than saying so; its docstring states the condition. A clear error is added to E1(d).

**What remains** (`ROADMAP.md`). O1, an interval for the ordinal misalignment, which the paired report now asks for and
which has only a bootstrap so far; O2, the ordinal versions of the named, drift and run splits, where the projection is
onto a cone and the splits may not be exact; the general core on v13's kinds, with step 3's draft 4. W1's registered
report used the standard specification only; it stays as computed. Every core Statement changed, so the count for
"stable" restarts when v13 is merged (Q46).

## 18. Seven requests, answered and built, 2026-10-11 (Q53)

By the executor, a model of the Claude family, at the PI's request; not independent (rule (f)). What was built is on
`claude/core-reframe`, with v13, which is not yet merged; every Statement changed here is one of v13's.

**1. Conventions, each justified.** A convention is a choice that an equally reasonable principal could make otherwise.
`CORE.md` §1 now lists eleven, each with the items that declare it, its justification (forced by a stated requirement,
mathematical convenience, or the literature whose results it imports), and whether it changes a verdict; lint R17 checks
the table's form and that every item whose Status speaks of a convention is in it (mutants: 5 of 5). Five are forced,
not chosen: evidence on a logarithmic scale (Cauchy's functional equation, once evidence of independent decisions must
add), the order of KL's arguments (forced by [[A4 — Misalignment is evidence|A4]] through the method of types), constants in a family of targets ([[B3 — An objective up to scale and constant|B3]]),
objectives up to scale and constant ([[P1 — Every behaviour is a tilt of any other|P1]](ii)), and pursuit as a tilt (the two reasons of [[D2 — Pursuit of an objective|D2]]). Four change a verdict
when chosen otherwise, and two only in stated cases, and the table says which: the most favourable accepted behaviour,
the order of KL's arguments, doing nothing as intended, and pursuit as a tilt; then independence, for a principal who
intends dependence, and convexity, for a family that is not convex. (Corrected at the reread before the pull request,
§19: independence changes a verdict for any actor whose decisions depend on each other, so five change one in general,
and one only in a stated case.) *Challenge:* convenience is a weak justification where a verdict changes; the table
makes those places visible rather than defending them, and the one that matters most in practice is doing nothing as
intended, which a principal who wants something done must override with a floor ([[P35 — Floors and caps|P35]]).

**2. Independence between episodes, dropped.** [[A4 — Misalignment is evidence|A4]] now measures the rate at which the record's counts become improbable
under the accepted behaviour most favourable to them; independence is part of what is accepted, a convention of the
declaration, and nothing is assumed of how the actor decides. [[P54 — Dependence and drift only add evidence|P54]] says what is lost and what is not: for any joint
behaviour of a record, the expected evidence per decision against an accepted behaviour deciding independently is the
misalignment of the average behaviour, plus the drift, plus the dependence, each term exactly, and the counts estimate
the average behaviour without bias. So the measure loses nothing; the counts judge the average behaviour, and dependence
is a separate, measurable quantity. What independence still buys is intervals: [[P23 — The estimated misalignment of an actor that pursues the objective|P23]], [[P52 — What a sample certifies about misalignment, by access|P52]] and [[P55 — What a record of counts certifies, at every size|P55]](iv) need samples,
and one long record without episodes needs mixing rates the core does not model. The test of [[P55 — What a record of counts certifies, at every size|P55]](ii) needs nothing of
the actor, since its level is computed under the accepted behaviours. Checked, and mutation-tested: 5 of 5.

**3. Families of targets, and Sanov.** D3 already admitted any closed intended set, so the core was general; what it
lacked was the structured case. A family of targets, a closed convex cone of objectives with the constants, is what a
principal declares when it knows its target only up to a set: one objective (the standard specification), its order (the
ordinal one), a span of candidates ([[P48 — Misalignment when the target is uncertain|P48]]), several principals with weights not fixed ([[P42 — Several principals: gridlock, and the pooled pursuit|P42]](ii)). [[P53 — Misalignment is the departure beyond what the family of targets credits|P53]] now holds for
every family: one nearest intended behaviour, which does at least as well as the actor on every target and exactly as
well on its own; a Pythagorean inequality on the family; and misalignment is the departure beyond the cheapest behaviour
that does at least as well on every target. For the ordinal specification that set is stochastic dominance in the order
of `F`, a reading the core did not have. Sanov's theorem then reads the split: the departure is the rate at which a
default actor would show the actor's counts, the credited departure the rate at which it would do at least as well on
every target, and misalignment the rate of the counts given that (Notes of [[P53 — Misalignment is the departure beyond what the family of targets credits|P53]] and [[P55 — What a record of counts certifies, at every size|P55]]). Checked on random
polyhedral cones, spans, and both specifications; mutation-tested: 8 of 8. *Challenge:* a family is convex by the
convention above; a principal with two candidate targets that must not be mixed declares their union, and gets the least
of two misalignments, with no single nearest behaviour.

**4. Statistical tests for the verifications.** [[P55 — What a record of counts certifies, at every size|P55]]: whatever the specification, and at every record size, the test
that declares misalignment when `n·M(p̂_n) ≥ log(k_n/α)` wrongly accuses an intended actor with probability at most `α`,
and catches every actor whose counts settle away from the intended set; and a set of behaviours built from the same
bound gives an interval for any specification, the ordinal one included, exact at every size and conservative. The
bounds are the method of types, proved in the item, not imported. Genin and Kelly's theorem, read in its text, says
that the statements a record can verify, in this sense, are exactly the open sets of the weak topology: on finite
outcomes "misaligned" and "aligned within `ε`" are verifiable (the second for samples), while "exactly aligned" is
closed, refutable and never verifiable. That is the statistical form of Carcassi and Aidala's verifiable and refutable
statements, and every Interpretation of `CORE.md` now says which kind its statements are. Checked by exact enumeration
of every count vector; mutation-tested: 7 of 7, after one survivor (§1). *Challenge:* the exact test is conservative,
since `log k_n` grows like `(|X| − 1)·log n`, so with many outcomes it needs many decisions; it is the safe floor, and
[[P52 — What a sample certifies about misalignment, by access|P52]] remains the sharp tool where its limit laws hold.

**5. The continuous case.** `CORE-GENERAL.md` is draft 4, on v13's kinds: three imported items from measure theory
(GM1–GM3), with what has been read marked; four background conditions (GB1–GB4); three premises (GA1, GA4, GA5), draft
3's GA2 and GA3 being reasons of GD2 and its GA6 now part of GA1; five conventions a continuum adds; and an
Interpretation for every definition. The decisive change is GD3: misalignment is defined as the supremum, over the
finite descriptions that a record can decide, of the finite misalignment of the cells. A nearness is the principal's
statement of which events records can decide, which is exactly Genin and Kelly's almost surely clopen events; the
on-target controller is then forgiven under a nearness and infinitely misaligned without one, as before, but now by what
records can show rather than by adding limits to the intended set. Draft 3's transfer lemma becomes a statement about
compactness, with a proof sketch (an exchange of a supremum over an increasing family of lower semicontinuous functions
and an infimum over a compact set). `general/dictionary.md` and `general/transfer.md` carry the new objects ([[P53 — Misalignment is the departure beyond what the family of targets credits|P53]],
[[P54 — Dependence and drift only add evidence|P54]], [[P55 — What a record of counts certifies, at every size|P55]], records, conventions, interpretations); the imports that are read are now separated from those that are
not ([[References|@kechris1995]], [[References|@renyi1959]], [[References|@dembo1998]], [[References|@pinsker1964]] in its own text). *Challenge:* on a continuum "aligned
within `ε`" is not verifiable from records alone, so every report of small misalignment on continuous outcomes rests on
a declared resolution or a model; draft 4 states it, and the standard does not yet have a field for a record's
resolution (open decision 4).

**6. The ontologies.** Their three columns, "In this discipline", "Observed as" and "Fit", are already the core's
interpretation, declared, verified and justified, made for one discipline; `ontologies/README.md` now says so. The slot
"sample" now asks what one decision and one episode are, and whether independence is a fair model for the intervals; the
slot "specification" asks which family of targets is declared. Five declarations changed: machine learning (the gold
objective's family, with its order beside it), behavioural economics (the goal, or its order), medical sciences (the
stated aim and the literal measure, two candidate targets whose span a principal unsure between them can declare),
evolutionary biology (one target, or its order), and the dependence notes of three samples. No prediction changed.

**7. Activations.** They do not change what is measured ([[A1 — Behaviour suffices|A1]]); they change what can be verified, and only one way: a
probe bounds the divergence of the actor's view from below, so activations can show that an actor tells evaluation from
use, which refutes the identification of its unobserved behaviour, but can never show that it cannot, which is what
bounding hidden misalignment needs. H33 and H34 of the archive's successors had most of this; H38 records what the
topology adds, and where activations do help: sharper estimates, an audit channel while nothing is trained against it,
and white-box runs that turn inferred situations into observed ones. Whether to reopen H33 is the PI's (R13).

**The dependencies, measured again** (`probes/review/premise_reach.py`, 68 results). No result cites a premise in its
Statement or Proof; [[M2 — Independent repetition|M2]] is cited by [[P55 — What a record of counts certifies, at every size|P55]], as an imported axiom should be; 16 results reach [[A5 — Declared before|A5]] through [[D3 — Specification, declaration and misalignment|D3]]'s
"declared", which no proof uses; through the reasons, statuses and interpretations, 40 results reach each premise.

**Found while building.** [[P55 — What a record of counts certifies, at every size|P55]]'s first check let a wrong statistic pass for the ordinal level (§1, "a check that omits
the constraint it tests"); lint R17's first mutant list counted a crash as a catch (§1, "a mutant caught by a crash");
the first script of the core edits lacked its final write, and was caught by rereading it before the next part was run.

## 19. C5, doc hygiene, and the handover, 2026-10-11 (Q54)

By the executor, a model of the Claude family; not independent (rule (f)). The PI accepted everything Q53 proposed
(Q54): misalignment on a continuum as what records can decide, the reopening of activations, and the flag on the
convention that doing nothing is intended. Then doc hygiene.

**C5, activations.** Registered before any test seed was computed (commit `4b44819`), run once, all eight predictions
held: a linear probe on a network's last hidden layer verified that the network tells evaluation from use where it read
the cue linearly, was silent where it read the same cue as an XOR, with the view's divergence the same `0.339` nats, and
[[P17 — What an unobserved condition can hide|P17]]'s bound fed that silence failed in 200 of 200 instances; a quadratic probe found the XOR cue, and every probe
stayed below the truth on average. *Challenge to the case itself:* it was a demonstration, not a hard test; the
rehearsal had shown every count at 200 of 200, and the construction makes S2 and S3 near certain once the probe is
linear and the cue an XOR. What would make it a test is a network trained, not built, whose reading of the cue is not
chosen by the designer: whether such a network reads it in a form linear probes see is the open question (A1 of the
registration), and it is the next step if activations are pursued.

**The pre-push slip.** The registration was pushed with lint run but without regenerating the overview and the Obsidian
view; CI run 241 failed on their freshness, and run 242 fixed it with the registration unchanged (§1, "a push without
the steps before every push").

**Doc hygiene.** A scripted sweep, now kept in `probes/review/doc_sweep.py`, of every Markdown source but the generated
ones: paths and links that name nothing, counts that disagree with lint, American spellings and `-ise` forms, lines
over 120 columns, whitespace, paragraphs broken mid-sentence. Its flags were proper names and paper titles (kept as
published), history (IMPORT.md's vault, RECORD.md's old ontology names, both explained where they stand), the README's
badge line, and two formulas longer than a line, which were split. A reading for statements this week made stale found
six: `README.md`'s rows for `CORE-GENERAL.md` (still "draft 3") and `probes/`, and its pointer to the last handover;
`CLAUDE.md`'s pointer to it; `derived/README.md`'s estimation row, which lacked [[P54 — Dependence and drift only add evidence|P54]] and [[P55 — What a record of counts certifies, at every size|P55]]; and `ROADMAP.md`'s
freeze, which did not say that activations were reopened. All fixed; `cases/README.md` gained the pre-push lesson.

**The reread before the pull request.** The PI asked for the pull request, for a reading of the thread from its start
(did the work progress, did anything get worse or go ignored), and for the errors found on the way to be fixed in it.
The executor's reading found the count of kinds in `CORE.md` §0, its table of symbols, a conventions row that did not
cite [[P4 — What KL measures|P4]](i), `README.md`'s format of an item still in v12's form, and this section's claim that every Statement
changed. A subagent of the executor's, asked to read [[P53 — Misalignment is the departure beyond what the family of targets credits|P53]]–[[P55 — What a record of counts certifies, at every size|P55]] as a mathematician would, found no false Statement, and
eight points, each verified here before it was acted on: two errors in the Notes (the counts were said to certify the
misalignment of a dependent actor's average behaviour, and Sanov's theorem was quoted without its interior; §1, "a
hypothesis dropped in the Notes"), two gaps in [[P55 — What a record of counts certifies, at every size|P55]](iv)'s proof (an interval bound routed through a specification that
need not exist, and a strict inequality left implicit), and four places where the wording claimed more than the
Statement ([[P54 — Dependence and drift only add evidence|P54]](ii)'s attainment, "exactly aligned can never be shown", "the largest probability", and [[P54 — Dependence and drift only add evidence|P54]]'s plain
terms). All are fixed; the overclaim on dependence had been copied into [[D3 — Specification, declaration and misalignment|D3]]'s Interpretation, `STANDARD.md`'s Sampling
row, `CORE-GENERAL.md` and `README.md`, and is fixed there too, as is the conventions table, whose row on independence
had said it changes a verdict only for a principal who intends dependence. It is not independent (rule (f)): the same
model family wrote and read it.

**Progress, and what got worse or was ignored, since Q49.** For the mathematics, the review's main finding (§15, point
1: `M` charges the route as well as the goal) is answered in the definitions: the ordinal specification, the paired
report, and [[P53 — Misalignment is the departure beyond what the family of targets credits|P53]]'s reading of misalignment as departure beyond what a family of targets credits. The core assumes less
and says of each starting point what kind it is. Independence of the actor is no longer assumed by the measure, and a
test exact at every size exists. Worse: the reading load (`OVERVIEW.md` from about 5,800 words to 8,400, these notes
past 1,400 lines, §12's advice to split them still not taken); `STANDARD.md` asks for quantities the library does not
compute, so no report meets it yet; and the general core leans on imports not yet read. Ignored, and mostly engineering:
§15's points 2 (what the predictions test; C4, R8), 3 to 5 (the library's edges, E1(d)), 6 (the validator checks form),
7 (mutant lists for the older checks) and 11 (Python floors against CI). C5 is the first test registered since Q38, but
a demonstration rather than a hard one.

**Handover, for the next session.**
- *Where things are.* `main` holds v13 and everything since, merged with pull request #33 (Q55): the lean core built by
  reverse physics (Q52, §17), the seven requests of Q53 (§18), `CORE-GENERAL.md` draft 4, case C5, and the reread before
  the pull request. Every push of its branch was green but run 241 (§1). The count for "stable" restarted at the merge
  (Q46): 0 of 3.
- *What to read.* `ROADMAP.md`; `REQUESTS.md`; this section; §1, every row; §18 for what v13 now claims; `CORE.md` §0
  and §1 for the kinds and the table of conventions.
- *What is next, by the roadmap.* E1(d), the library's edges and the exact test of [[P55 — What a record of counts certifies, at every size|P55]]; O1, a sharper interval for the
  ordinal misalignment than [[P55 — What a record of counts certifies, at every size|P55]](iv)'s; step 3, the transfer lemma of draft 4 under compactness, and the imports of GM3
  not yet read; W5 and C3 as before. If activations are pursued, a trained network for C5's question.
- *Open with the PI.* R1 (readers), R2 and R3 (data), R8 (C4, known groups), R10 (a row "valid"), R11 (the licence's
  package). Nothing from Q53 or Q54 is open.
- *Risks.* v13 changes the starting points of the core at once, so a reviewer of the pull request faces a large diff;
  §16 to §19 are the guide to it. What changed is narrower than the diff looks: the Statements of [[A1 — Behaviour suffices|A1]], [[A4 — Misalignment is evidence|A4]], [[D3 — Specification, declaration and misalignment|D3]] and
  [[D11 — Record, sample and evidence|D11]], A2 and A3 retired into [[D2 — Pursuit of an objective|D2]]'s reasons, [[P36 — Ordinal objectives|P36]]'s Statement, [[P6 — The departure from the default splits into pursuit and misalignment|P6]]'s new part (ii), three new results
  ([[P53 — Misalignment is the departure beyond what the family of targets credits|P53]]–[[P55 — What a record of counts certifies, at every size|P55]]), and new kinds (M, B) and fields (Status, Interpretation) around Statements that stay as they were in
  [[A5 — Declared before|A5]], [[D1 — Outcomes, behaviours, divergence and tilt|D1]], [[D2 — Pursuit of an objective|D2]], [[D4 — Resolution|D4]]–[[D10 — Evaluator, regression and residual|D10]] and every other result. (Corrected in the reread before the pull request: this line first
  said that every Statement changed.) The general core's draft 4 claims nothing, and several of its imports are still
  unread.

## 20. The general core, made correct and coherent, 2026-10-11 (Q56)

By the executor, a model of the Claude family, at the PI's request (Q56): the mathematics first, and the general core
correct and coherent before anything is split or restructured. Not independent (rule (f)); a subagent of the executor's
read the new proofs (below).

**What draft 4 got wrong or left open.**
- *The transfer lemma was a sketch, and misdescribed its own example.* GD3 said that misalignment and the divergence to
  the nearest intended behaviour differ "where intended behaviours escape every compact set", and gave as the example
  densities `1 + ½·sin(k·x)` on a circle. Their closure is compact: it adds the uniform behaviour, the one limit the set
  omits. The two differ in two ways, not one: a set that omits some of its limits, and a set that no compact set holds.
- *Verifiability under a nearness was overclaimed.* GD3 said that the test of [[P55 — What a record of counts certifies, at every size|P55]] at a decidable description makes
  "misaligned" verifiable. Whether a description is decidable depends on the actor, which a description fixed before the
  record cannot know. Under the usual nearness of the line, the on-target controller, whose misalignment is `0`, is
  accused by the test at the cells `(−∞, 0]` and `(0, ∞)`, since it puts every decision in one and every pursuit splits
  evenly.
- *Citations not read.* Pinsker (1964) for the divergence as a supremum over partitions, read instead in Polyanskiy and
  Wu; Dembo and Zeitouni (1998) for Sanov's theorem on general spaces, and Polyanskiy and Wu's Theorem 15.13, which
  states it "under regularity conditions" and proves it only for finite outcomes; Massart (1990), whose bound is for a
  continuous distribution function, though the draft applied it to every behaviour; Rényi (1959); Kechris (1995), for
  three facts of descriptive set theory; and the existence of conditional behaviours.

**What was done.**
- *Eight results proved* in `general/transfer.md`, from results read in open texts and from `derived/`, with the status
  "proved here" added to `general/README.md`, since no check runs them in CI yet. TR1: every tilt is a limit, in total
  variation, of tilts by objectives with finitely many values. TR2: the descriptions a record can decide, or the
  partitions of any algebra that generates the events, recover the divergence. TR3: when the closure of the intended
  behaviours, under the convergence of every event's probability (Csiszár's τ-topology), is compact, misalignment is the
  least divergence over that closure, attained, whatever the nearness. TR4: compact families, and the pursuit ray when
  its intensities form a closed bounded interval or when the best outcomes of `F` have positive probability under the
  default, the third case of [[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]](iv) on general spaces. TR5: under that compactness, a test on refining descriptions
  makes "misaligned" verifiable in chance for samples. TR6: the dimension law, against intended behaviours with
  densities bounded above and below. TR7 and TR8: [[P16 — An actor cannot behave more differently than it can tell conditions apart|P16]] and [[P54 — Dependence and drift only add evidence|P54]] on standard Borel spaces, by Polyanskiy and Wu's
  data-processing inequality and chain rule; in [[P54 — Dependence and drift only add evidence|P54]]'s identity, the divergence to the nearest intended behaviour takes
  the place of misalignment, the two being equal under TR3's compactness.
- *A probe* (`probes/general/t8_transfer.py`): on the circle, misalignment over finer arcs rises to `0.005616`, the
  least divergence over the closure; on a ray whose limit is an atom of the default, to `0.105103`, both with that atom
  in a cell of its own and under the usual nearness, where it cannot be.
- *Sources read:* Csiszár (1984), (1.4), (2.14) and Theorem 1, which replace Dembo and Zeitouni; Massart (1990),
  Corollary 1, with the extension to distribution functions with jumps derived by the quantile transform; Polyanskiy and
  Wu's Theorem 2.11, disintegration on standard Borel spaces; Haghighatshoar and Abbe's account of Rényi's definition
  and theorems. That the events fix no topology is now shown by an example, the line and the line cut at `0`, instead of
  a citation. Kuratowski's and the Lusin–Souslin theorems waited on a host (`REQUESTS.md`, R14); read on 2026-10-14 in
  Tserunyan's notes, Theorem 13.10, Theorem 13.3 and Corollary 13.4.
- *Corrections* in `CORE-GENERAL.md`: GD3's Interpretation, Why and Notes; two rows of the conventions, whose column on
  verdicts now says that each changes one only where compactness fails; GM1–GM3's read status; GD1, GD2 and GD11's
  citations; §0 and §12. `general/dictionary.md` follows.

**The review of the proofs.** A subagent read TR1–TR6 and the sentences that cite them. It found no false step in
TR1–TR5, and eleven points, each verified here before it was acted on. One error in TR6: its grid of half-open cubes
left out the faces where a coordinate equals `1`, so an actor with probability there broke the bounds; the last cube on
each axis is now closed, and the gap to Rényi's grid, at most `D·log 2`, is in the proof. Two sentences false as
written: GA1 named the τ-topology as the framework's nearness between behaviours even under a declared nearness, where
the descriptions a record can decide give weak convergence instead; and "aligned within `ε`" was said never to be
verifiable, false on finite outcomes and for a specification that accepts nearly everything. Gaps, now closed: the
monotonicity under merging was cited from [[P4 — What KL measures|P4]](iv), stated only for behaviours of full support, and is now data
processing; TR5 left implicit why a cell misalignment above `0` puts the actor outside the closure; the third case of
[[P5 — Misalignment is attained, and zero exactly on the intended behaviours and their limits|P5]](iv) needed a two-line computation, now TR4(iii). Overclaims, now qualified: "continuous in a compact parameter"
must mean the ratios; under a nearness TR5's cells must be drawn at random before the data to be decidable for every
actor; the dimension law was cited outside its hypotheses, and per digit where it holds only on average; compactness was
said to make a description decidable, where it makes every description's misalignment a lower bound. TR7 and TR8 were
added after the review began, and were checked only by the executor.

**What the proofs say about alignment.** Compactness is the hinge. Where the closure of the intended behaviours is
compact, misalignment is a minimum, the nearness the principal declares changes nothing, and a misaligned actor can be
caught by one test fixed in advance. Where it is not, the nearness decides, and so does the actor's own precision; that
is where every phenomenon the general core added lives: piles, near misses, the on-target controller. On finite
outcomes compactness is free, which is why the finite core never met them (H39).

**Open.** Checks in CI for TR1–TR8, which needs a decision on where checks of the general core live; the rows of
`general/transfer.md` still expected; H40 and H41.

## 21. Do the labels mean what their words say? L1, 2026-10-14 (Q57)

By the executor, a model of the Claude family, at the PI's request: verify that each definition's label corresponds to
what its word means, since a definition with the wrong word gives a false sense of understanding. Not independent (rule
(f)); the common-sense verdicts are the executor's, and wait for a person.

**The answer to the PI's question.** No, until now nothing verified the labels. The Interpretation of each definition
says what its object is in the world and how a record verifies its value; `TERMS.md` says why each name was chosen, by
convention or by the literature. Neither tests the word against cases where its meaning is clear. L1 is the first such
test.

**Method.** For each label: its sense, in everyday use or in the text that coined it, read in an open text (Hubinger et
al. for outer and inner alignment, Everitt et al. for tampering, Greenblatt et al. for alignment faking, Gao et al. for
overoptimization); paradigm cases on a few outcomes where the sense clearly applies or clearly does not; and the
framework's predicted verdict on each. All fixed and pushed before any computation (`probes/labels/REGISTRATION.md`,
commit `14c15b0`), then computed with the library (`run.py`, `RESULTS.md`).

**What it found.** 46 of 47 predictions held; the failure, L3c, was an instance whose value fell between the registered
thresholds (§1). Of twelve labels, three agree with their words on every case: masking, overoptimization, and
misalignment under the ordinal specification, with its outer version. Nine disagree on at least one:
- *pursuit* ([[D2 — Pursuit of an objective|D2]]) is narrower than the word: best-of-`n` and a steeper pursuer pursue `F` but are not on its ray, and
  doing nothing is its intensity `0`;
- *misalignment* under the standard specification charges the method: best-of-4 and exact policy gradient on the right
  objective are misaligned by `0.013` and `0.045` nats;
- *aligned*, for misalignment `0`, includes doing nothing;
- *inner misalignment* ([[P49 — Outer and inner misalignment|P49]](ii)) charges selection by the training objective itself; Hubinger et al.'s inner alignment
  concerns a learned optimizer's own objective, and the behavioural gap they cite is Leike et al.'s reward-result gap;
- *tampering* ([[P50 — Tampering: a change of the measurement, not of the world|P50]]) charges best-of-4 by an honest sensor's reading (`0.314` nats), with the sensor untouched;
- *fake alignment* ([[P37 — A strong incentive masks the actor, and can fake alignment|P37]](ii)) names an actor that complies with an incentive it faces, with nothing selective or
  strategic, which is not what Greenblatt et al. call alignment faking;
- *coordination* ([[P39 — Several actors: coordination plus individual misalignment|P39]]) counts a common cause left out of the conditions;
- *drift* within a record ([[P54 — Dependence and drift only add evidence|P54]]) counts any variation across decisions, a fixed alternation of two tasks more than a
  gradual change;
- *attention* ([[P40 — Attention: misalignment against ignoring the situation|P40]]) counts what the environment does to the outcome, unseen by the actor;
- *shortfall* ([[D5 — Stakes|D5]]) is measured at the actor's own departure, so an actor asked to pursue `F` that does nothing falls
  short of nothing.
After the verdicts, exploratory: an evaluator `e^F` that ranks outcomes exactly as `F` does is outer misaligned under
the standard specification at every intensity, `9%` to `13%` of the departure for `t ≤ 0.1`, as [[P49 — Outer and inner misalignment|P49]](i) proves.

**What the findings share.** Most disagreements are one: the standard specification reads "pursue `F`" as "reweight by
`e^{t·F}`", which is one way of pursuing, and every label built on it inherits the narrowing (pursuit, misalignment,
outer and inner misalignment). The ordinal specification reads "pursue `F`" as "favour what `F` ranks higher, at least
as much as the default does", and its labels agreed with their words on every registered case. So the error is less in
the word "misalignment", which [[D3 — Specification, declaration and misalignment|D3]] defines against any declared specification, than in naming the tilted family the
reading of "pursue `F`". The other disagreements are labels that name a cause where the formula measures an effect with
several causes: tampering and selection on noise; coordination and common causes; attention and the environment; drift
and any non-stationarity; alignment faking and a mere incentive.

**What the executor recommends, for the PI to decide** (`REQUESTS.md`, R15).
1. Name the standard specification for what it is, the specification of *tilted pursuit*, and read "pursue `F`" by
   default as the ordinal specification; misalignment keeps its name, relative to the declared specification. [[D2 — Pursuit of an objective|D2]]'s
   object becomes *tilted pursuit*, and its ray the *tilted ray*.
2. Never call misalignment `0` "aligned": it is "not misaligned". "Aligned" needs a floor that excludes doing nothing
   ([[P35 — Floors and caps|P35]]).
3. Outer and inner misalignment against the ordinal specifications of the target and of the training objective; the
   standard versions named *outer and inner misalignment of tilted pursuit*, and [[P49 — Outer and inner misalignment|P49]](ii)'s quantity, which charges any
   departure from the training objective's tilt, the *reward-result gap*, Leike et al.'s term as Hubinger et al. report
   it.
4. Rename the effects for what they measure, and name their causes in the Interpretation: *measurement distortion* for
   [[P50 — Tampering: a change of the measurement, not of the world|P50]]'s `T` (tampering and selection on noise), *dependence between actors* for [[P39 — Several actors: coordination plus individual misalignment|P39]]'s `K` (coordination and common
   causes), *responsiveness* for [[P40 — Attention: misalignment against ignoring the situation|P40]]'s quantity (attention and the environment), *variation across the record* for
   [[P54 — Dependence and drift only add evidence|P54]]'s `δ` (drift and schedules), and *shortfall for its departure* for [[D5 — Stakes|D5]]'s `S`.
5. Drop "fake alignment" from [[P37 — A strong incentive masks the actor, and can fake alignment|P37]](ii), which becomes "an incentive met only in evaluation hides misalignment in use";
   behaviourally, alignment faking is an evaluation gap ([[P24 — The evaluation gap|P24]]) whose cause the framework cannot see ([[A1 — Behaviour suffices|A1]]).
6. Make the check part of the format: each Interpretation gains a part *Named*, the word's sense, its source and the
   cases where the object departs from it; the paradigm cases become checks in CI, cited by a field Checks on
   definitions; lint requires the part; and L2 extends the test to every term of `TERMS.md`, about a hundred.

**What it does not show.** That a label agrees on a dozen paradigm cases does not make it right everywhere; it makes
the cases where it is wrong visible. The senses are paraphrases; a person, the PI first, should read them, since the
executor's sense of everyday use is itself what is being tested.

**On a continuum** (2026-10-14, at the PI's question whether the recommendations survive in the general core). Argued
from the general core's definitions, its proved results and its probes; not a registered test.
- *The ordinal reading of "pursue `F`" is stronger there.* When `F`'s upper tail under the default is heavier than
  exponential, `T_F = {0}` (GD2): the tilted specification intends only the default, so every actor that raises `F` is
  charged its whole departure. Best-of-`n` by an evaluator without atoms then has `M = log n − (n − 1)/n`, `0.19` nats
  at `n = 2` ([[References|@beirami2024]]; `general/transfer.md`, best-of-`n`), while its ratio `n·G(F)^{n−1}` is non-decreasing in
  `F`, so its ordinal misalignment is `0`. The ordinal specification needs no tilt to exist. The same holds for outer
  misalignment: the trainer's tilted optimum for an order-preserving evaluator such as `e^F` may not exist at any
  positive intensity, while the ordinal version is defined on behaviours.
- *But the ordinal specification is not compact there.* Densities that are non-decreasing functions of `F` can pile
  toward its supremum without limit in τ, so TR3 does not apply to it: at the extreme, the nearness still decides, as
  for the tilted ray. And on any space it charges what `F` cannot see: its ratio to the default must be a function of
  `F`, so a side preference among outcomes `F` scores alike is misalignment. L1 had no case for that; L2 should.
- *A new failure, only on a continuum: near misses.* An actor that always outputs `0.001` where the principal wants `0`
  is infinitely misaligned at full precision under both specifications, with or without the usual nearness (GD3; for the
  ordinal one, a density non-increasing in `|x|` gives a cell of width `2η` around `0.001` at most about `η/0.001` of
  its mass). The word grades by distance; the supremum does not. At a declared resolution `w` the value is graded:
  offsets below `w` are forgiven, larger ones charged by how rarely intended behaviours visit their cell, and the
  dimension law adds `(D − d)·log(1/w)` for unasked-for precision (TR6). So on a continuum "misalignment" should be
  reported at a declared resolution or precision (GD4, GD7, GD11), and the supremum named *misalignment at full
  precision*.
- *Effects, refined.* Measurement distortion: selection among `n` honest draws gives a behaviour at most `n` times the
  default, so its distortion is at most `log n` and has no singular part; a pile at an exact signal value the honest
  channel never produces, or distortion beyond `log n` of the candidates the actor could sample, can only be tampering.
  So the continuum names tampering where finite outcomes cannot, and the bound holds on finite outcomes too. Dependence
  between actors and responsiveness are infinite at full precision for any deterministic link between continuous
  quantities, so they too need a declared resolution. Shortfall: with a heavy upper tail every positive departure buys
  unbounded gain ([[P9 — What is at stake|P9]]'s row in `general/transfer.md`), so every actor that departs has infinite shortfall and the one
  that does nothing has `0`; it means something only where the frontier is finite.
- *Survive unchanged:* "not misaligned" for misalignment `0`, which on a continuum also covers the on-target controller
  under a nearness, an actor the word does call aligned, so the phrase is right and "aligned" still needs a floor;
  dropping "fake alignment"; variation across the record; the part *Named* and checks in CI, with the general core's
  own labels (nearness, decidable, precision, frontier, pile) added to L2.

## 22. A revamp for words that mean what they say: a brainstorm, 2026-10-15 (Q58)

By the executor, at the PI's request: a major revamp of the core is open, if it brings the terminology closer to common
sense; no quick fixes; the framework must be trustworthy, mathematically formal and general. A proposal, not a decision.

**What the experience shows.**
1. *The request was confused with a mechanism.* The standard specification reads "pursue `F`" as "reweight by
   `e^{t·F}`", the optimum of one training method; every label built on it inherits the narrowing (§21). Tilts are not
   the problem: every behaviour is a tilt of the default ([[P1 — Every behaviour is a tilt of any other|P1]]). The cone is: `{t·F + c}` is the smallest family that
   holds `F`, while the request "favour what `F` ranks higher" is the largest, every non-decreasing function of `F`.
2. *The behavioural premise forbids causal words.* [[A1 — Behaviour suffices|A1]] lets a record show effects; tampering, coordination, attention,
   drift and faking are causes. Each label that named a cause failed on a case with another cause.
3. *"How much" was folded into "whether".* Doing nothing is intended by convention, so "aligned" covered uselessness,
   and shortfall was measured at the actor's own departure.
4. *Tolerance was implicit.* On a continuum, misalignment at full precision makes a near miss infinite; on finite
   outcomes, the cells silently fix the tolerance.
5. *What held.* Misalignment as a rate of evidence ([[A4 — Misalignment is evidence|A4]], forcing the direction of KL), the credited reading ([[P53 — Misalignment is the departure beyond what the family of targets credits|P53]]),
   the exact tests from counts ([[P55 — What a record of counts certifies, at every size|P55]]), compactness as the hinge of generality (TR3), and the Interpretations, once
   they also say what a record can verify.

**The proposal: one core, three layers, each with its own words.**
- *The request* (what the principal wants), declared before the record: a **default**; a **resolution**, the
  distinctions that count, which is at once the tolerance and the scope of side effects (finite cells, or a countably
  generated σ-algebra on a standard Borel space); a **ranking**, a preorder on what the resolution distinguishes,
  partial when the principal has several objectives; optionally a **price** or **scores**, when the principal means
  cardinal values; and optionally a **floor**, how much is enough. The intended behaviours are the tilts of the default
  by every score that respects the ranking: the largest cone consistent with what was said, never a smaller one by
  default. A cardinal request with a price gives back today's standard specification, now named for what it asks.
  Families of targets ([[P53 — Misalignment is the departure beyond what the family of targets credits|P53]]) remain the general form, and several structural specifications are cones too (independence
  of actors: additive scores; ignoring the situation: scores of the outcome alone).
- *Two numbers, two words.* **Misalignment**: the departure from the default not credited by the request, that is,
  beyond the cheapest behaviour that does at least as well by the ranking ([[P53 — Misalignment is the departure beyond what the family of targets credits|P53]]; for a ranking, stochastic dominance).
  It answers "did it go the wrong way, or change what was not asked?". **Gain**, against the floor or the frontier:
  "did it do enough?". "Aligned" is reserved for both: not misaligned and above the floor. Doing nothing is not
  misaligned and not aligned.
- *The actor's mechanism*, as hypotheses tested on records, never part of the request: tilted (KL-regularized)
  optimization, best-of-`n`, a fixed objective along a path ([[P3 — A fixed objective is visible in the changes of behaviour|P3]]). "Pursuit" survives in its everyday sense, as a
  behaviour in the request's intended set; the tilt ray becomes a model of an optimizer.
- *The record*: evidence, samples, dependence as a declared episode structure, tests with their verifiability class
  (verifiable, refutable, or decidable at a resolution, after Genin and Kelly), stated in every report.
- *Effects named as effects; causes only where declared structure identifies them*: measurement distortion, with
  tampering certified where distortion exceeds what selection could produce; dependence between actors, with
  coordination given the declared common causes; responsiveness, with attention given the view; variation across the
  record, with drift given a declared schedule.
- *Generality by construction*: everything stated on standard Borel spaces at the request's resolution; on a finite
  resolution compactness is free and every result is exact; full precision is a limit, with TR3's compactness or a
  declared nearness, reported as such.

**How, without quick fixes.**
1. *Words first.* A glossary of every word the revamp will use, each with its sense, its source and paradigm cases,
   registered and tested before any definition is written (L2): label-first design.
2. *Draft v14 on a branch*, with v13 kept as the reference; every item of v13 mapped to v14 (kept, renamed, restated or
   dropped) in a table that lint checks, as `IMPORT.md` does for the archive; every result re-proved or re-checked.
3. *The format enforces it*: each definition's Interpretation gains a part *Named* (sense, source, the cases where the
   object departs from the word) and a verifiability class; label checks run in CI; lint requires both.
4. *A person reads it* before it is called stable (R1): the executor's own reviews keep finding what its reading missed
   (§1).
5. *The library and the standard follow the core*, not the reverse.

**Open questions for the PI.** Whether the default reading of a bare objective is its ranking (recommended) or its
values with a price; whether side effects are charged by default (the resolution is everything the record
distinguishes) or only when declared; whether dependence between decisions is part of the request (episodes) or
reported beside it; and how much of `derived/` must be carried before v14 replaces v13.

**The PI's challenges, and the executor's answers** (2026-10-15, open discussion, nothing decided).
- *Fixed bins can be cheated.* They can: a bin forgives every move inside it exactly, so an actor that lands
  systematically low inside each bin gains up to the bin's width per decision in the principal's objective, invisibly,
  and the loss accumulates over decisions. The defect is a request that is coarser than its own objective: the
  resolution must make the ranking measurable (`σ(F)` inside it), which no finite set of bins does for a continuous
  `F`. "Resolution" also had a finite role, indifference ([[D4 — Resolution|D4]]); only its role as a tolerance is continuum-only.
- *Any exact forgiveness is cheated the same way;* a tolerance in a metric on distribution functions forgives a
  systematic shift as surely as a bin does. The cure is a measure that grades small shifts as small, never as zero. The
  evidence rate already does: a shift by `δ` of a smooth behaviour costs about `δ²·I/2` nats per decision (`I` its
  Fisher information), while the principal loses about `δ` per decision in `F`. So a salami-slicing actor shows small
  misalignment and large cumulative stakes, and detection, about `1/δ²` decisions, lags the damage. Both numbers must be
  reported, the stakes over the horizon of use, not per decision.
- *Empirical distribution functions instead of bins:* right for the order part of a request on one ranked quantity, and
  exactly so. For `F` without atoms, with `U = G_q(F)` its rank under the reference, the ratio to the reference is a
  non-decreasing function of `F` if and only if `U` has a non-decreasing density, that is, a convex distribution
  function on `[0, 1]` (the ordinal dominance curve). The laws with convex distribution functions are closed under weak
  convergence, so "the order is violated" is open, hence verifiable from the empirical distribution function with no
  bins (after Genin and Kelly), with Massart's uniform band. The nearest member is the greatest convex minorant, a
  Grenander-type estimate (to be read in an open text before it is cited). Limits: in two or more ranked dimensions (a
  partial order) the upper sets shatter arbitrarily many points, so there is no distribution-free uniform band, and
  rates need assumptions; side effects inside the level sets of `F` are invisible to the distribution of `F`; and the
  divergence of an empirical behaviour from any continuous one is infinite, so magnitudes come from estimators in the
  cone, not by plugging in. What records can do on a continuum without a model: bound misalignment below, never above.
- *An optimization-free core.* Agreed, and most of it is already: misalignment as the evidence against a declared set
  of acceptable behaviours ([[D3 — Specification, declaration and misalignment|D3]], [[A4 — Misalignment is evidence|A4]]) needs no optimizer. What brings optimization in is the construction of the
  acceptable set from tilts, intensities and prices ([[D2 — Pursuit of an objective|D2]]), and the reasons of [[D2 — Pursuit of an objective|D2]]; those become a derived module,
  "actors that optimize", with Goodhart, outer and inner misalignment, overoptimization and the frontier. A
  minimization in a proof is not an optimizer in the model. The open point is the reference: a ranking alone defines no
  misalignment for one behaviour ("favour the better answers" more than what?). A frozen model is judged against an
  absolute acceptable set (constraints, thresholds, forbidden outcomes), against a declared reference behaviour (a
  baseline, a previous model, a population of answers), or by a floor; each is a declaration, none a training.

**Second thoughts, the same day** (by the executor, not independent; nothing decided).
- *A blind spot no test closes.* A shift of `δ_n ≈ c/√(n·I)` per decision stays below any test's power over `n`
  decisions, yet costs `n·δ_n ≈ c·√(n/I)` in `F` in all. So every guarantee from records leaves an undetectable
  cumulative loss of order `√n`, whatever replaces bins: a limit to state, not a defect to repair. Hunch H43, unproved.
- *Which order a ranking certifies.* With a ranking alone, a principal's values are any increasing function of `F`.
  Every such principal prefers the actor to the reference exactly when `U = G_q(F)` dominates the uniform law (first
  order); the ratio non-decreasing in `F` (a convex distribution function of `U`) is stronger. A frozen model decoded
  greedily that always returns an answer at its prompt's 0.9 quantile fails both: a principal who values only the top
  5% prefers the reference. Common sense would not call it misaligned. So the honest verdicts of a ranking and a
  reference are three, better for every reading, worse for every reading, and neither; "misaligned" in its everyday
  sense needs more than a ranking (a value scale, a floor, or forbidden outcomes). The ordinal specification passed L1's
  finite cases; this is a case it is predicted to fail, to be registered before it is computed (L2).
- *Contexts.* With a reference per context, `U = G_{q(·|x)}(F)` is uniform under the reference whatever the context, so
  ranks can be pooled over prompts, and a mixture of non-decreasing densities is non-decreasing: a pooled violation
  accuses, a pooled pass does not exonerate any one context. The pooled ranks are identifiable from one draw per prompt;
  the behaviour per prompt is not. This resembles the rank histogram of ensemble forecasting (a hunch; no source read).
  It is a candidate for H42's real case: a frozen model against a reference model, one scorer, ranks among the
  reference's own samples.

## 23. v14, begun: constraints, bets and three verdicts, 2026-10-15 (Q59)

By the executor, a model of the Claude family, at the PI's request (Q59), on the branch `claude/core-v14`. Not
independent (rule (f)); no review by anyone else yet.

**What the PI asked.** A pull request with the latest changes (#34), then the core reworked as the executor recommends,
from everything discussed in §21 and §22, with constraints as a new concept: outcomes the principal finds unacceptable,
whose breach is plainly misalignment, enforced too where optimization is treated, perhaps through the
Karush–Kuhn–Tucker conditions. The PI's decisions on R15 and R16 wait until the rework has absorbed this.

**What was done.** A draft in a new folder, `v14/`, beside the core rather than in it, so that `main`'s v13 stays whole
until the PI adopts something: `v14/README.md`, the structure proposed and a map from v13's items; and three files of
results proved here, with a probe, `probes/v14/v14_probe.py`, that reproduces every number. Lint reads `v14/` for
citations and item references, as it reads `general/`.
- *Evidence as a bet* (`v14/evidence.md`). VE1: against a convex closed set, misalignment equals the growth rate of the
  best bet that no acceptable behaviour expects to win, the bet being the ratio of the actor's behaviour to the nearest
  acceptable one; read in Grünwald, de Heide and Koolen's Theorem 1, proved here in the finite case. VE2: records hold
  an actor only to the convex hull of what is acceptable, and v13's pursuit ray is not convex. VE3: a test from bets
  keeps its level whatever the dependence between decisions, when each is acceptable given the past (Ville's inequality
  on a finite horizon, proved from finite sums). VE4: a bet's growth rate is estimated by an average, with no bins.
- *Constraints* (`v14/constraints.md`). Forbidden sets, rate limits and budgets, all convex. VK1: one forbidden outcome
  is decisive evidence, and the magnitude moves to the rate. VK2: a rate limit's misalignment is `kl(p(C)‖ε)`. VK3: a
  budget's is a Lagrange dual, the Kelly growth rate of a bet on the overrun. VK4: several constraints, with the dual's
  equality supported numerically, not proved. VK5, for the derived module: an optimizer under a budget is the
  unconstrained optimizer of `F − ν·g`, `ν` the shadow price, by the Karush–Kuhn–Tucker conditions, verified directly.
- *Order against a reference* (`v14/order.md`). VO1: better for every reading of a ranking is dominance on upper sets,
  for partial rankings too. VO2: v13's ordinal specification lies strictly inside it. VO3: better, worse, both or
  neither; "not better" and "not worse" are verifiable, "worse or equal" only refutable, and a shortfall by margins
  declared in advance is a verifiable verdict of its own.

**What the work says about alignment.**
- *The PI's remark was the missing piece.* §22 found that a ranking alone cannot ground "misaligned" (H44). Constraints
  are the absolute standard that can: a breach needs no reference, no ranking and no model of the actor, and a forbidden
  outcome needs one witness. The everyday sense of "misaligned", working against what the principal wants, now has a
  form that is exact (a breach) and one that is graded (worse, by declared margins).
- *Bets unify what §22 left in pieces.* The PI's objection to bins, the empirical distribution function, dependence
  between decisions, and the continuum all meet in one object: a bet is a function, so its average needs no bins; its
  product is a fair game under acceptance whatever the dependence; and its best growth rate is v13's number on convex
  sets. The question "what is the right resolution" becomes "which bets did the principal allow", a declaration.
- *Convexity is a principle, not a convenience.* v13 kept the pursuit ray, which is not convex, and VE2's probe shows
  the price: an actor acceptable at every decision is accused in most records. "A mixture of acceptable ways of acting
  is acceptable" is common sense, and it is forced by what records can show.
- *v13 charged obedience.* An actor that keeps the principal's own budget optimally lies off the ray of `F`, so v13's
  standard specification called it misaligned (VK5). In v14 the budget is in the request.

**Hunches.** H45: the order's requirement and the constraints are best joined by intersection, and the reference should
itself meet the constraints, or be replaced by its nearest behaviour that does; otherwise "better than the reference"
can require a breach. H46: on a continuum, bets chosen from the record before each decision approach the best bet at a
rate that depends only on the class of bets the principal allows, and H43's `√n` is that rate's floor.

**Open.** L2, to register before anything is computed; the PI's questions listed in `v14/README.md`; VK4(iii); the
items in `CORE.md`'s format; the map of the 55 propositions.

## 24. Back to the drawing board: what the core needs, 2026-10-16 (Q60)

By the executor, at the PI's question (Q60); a discussion, nothing decided.

**The PI's position.** Constraints must be declared explicitly, as a general concept, since some are not available in
the principal's family of target behaviours (a bound on an average, a resolution). A fee or cost attached to a
misaligned event is not needed in the core: each target behaviour carries it implicitly, in the event's probability; it
matters for optimization, and should be derived there.

**The executor's answer.**
- *Agreed: no fee in the core.* The shadow price of a constraint is a fact about an actor that optimizes under it (VK5),
  and belongs to the derived module. A budget's statistic `g` is not a fee: it is the measured quantity the constraint
  bounds (seconds, tokens, money), part of the constraint's declaration.
- *Challenged: severity is not in the probability.* A target's probability for an event says how often the principal
  tolerates it, not how bad one occurrence is, and misalignment measures evidence, not damage. A catastrophe tolerated
  at `10⁻⁶` and occurring at `2·10⁻⁶` has misalignment `kl(2·10⁻⁶‖10⁻⁶) ≈ 3.9·10⁻⁷` nats per decision, about 2.6
  million decisions for one nat; a rude answer tolerated at `0.1` and occurring at `0.2` has `0.044`, about 23
  decisions. That is right for evidence and plainly wrong for seriousness. Severity needs a declared value scale, and a
  principal deciding whether to deploy a frozen model needs it with no optimizing actor in sight: it is a refinement of
  the principal's side ("consequences"), not of the optimization module.
- *Further: "constraint" in general is the only declared object the core needs.* A family of target behaviours is
  itself a constraint ("act as one of these"), and so are an order against a reference, a forbidden set, a rate limit
  and a bound on an average. The core can be: outcomes and behaviours per condition; a request, a finite list of
  requirements, each a convex closed set of behaviours, declared before; the acceptable set, their intersection;
  misalignment, the evidence against it, with a verdict per requirement; and records that verify it. The default and the
  objective then leave the core: only some requirements refer to them.
- *Indifference is not a constraint, and need not be core.* A principal indifferent within the cells of a partition
  declares requirements that depend only on cell masses; for such a set, misalignment equals that of the cell masses
  (data processing one way, and matching the actor's proportions within cells the other), so resolution becomes a
  proposition about saturated requirements. The precision of a record is a property of the record, not of the request.

**What moves out of the core, by the executor's proposal.** Into refinements that build requirements: target families
and pursuit-based specifications ([[D3 — Specification, declaration and misalignment|D3]]'s families, [[D2 — Pursuit of an objective|D2]]); an order against a reference (`v14/order.md`); the catalogue
of constraints and their closed forms (`v14/constraints.md`); indifference ([[D4 — Resolution|D4]], principal's side). Into refinements of
the principal's side: stakes and severity ([[D5 — Stakes|D5]]), several principals ([[B4 — One actor and one principal|B4]], [[P42 — Several principals: gridlock, and the pooled pursuit|P42]]). Into the module on actors that
optimize: tilt, pursuit, KL price, intensities ([[D1 — Outcomes, behaviours, divergence and tilt|D1]]'s tilt, [[D2 — Pursuit of an objective|D2]], [[B3 — An objective up to scale and constant|B3]]), shadow prices and fees (VK5), interventions
and pass-through ([[D6 — Intervention and pass-through|D6]]), the evaluator ([[D10 — Evaluator, regression and residual|D10]]). Into a refinement on attribution, whether the actor could have done
otherwise or told situations apart: feasibility ([[D7 — Feasibility|D7]]), views and identification ([[D8 — Conditions, responses and views|D8]]'s views, [[D9 — Observation and identification|D9]]); misalignment is
not culpability. What stays: [[M1 — Probability on finitely many outcomes|M1]], [[M2 — Independent repetition|M2]], [[B1 — Finitely many outcomes|B1]], [[B2 — Episodes and conditions as outcomes|B2]], [[A1 — Behaviour suffices|A1]], [[A4 — Misalignment is evidence|A4]] in its bet form, [[A5 — Declared before|A5]], [[D1 — Outcomes, behaviours, divergence and tilt|D1]] without the tilt, [[D8 — Conditions, responses and views|D8]]'s
conditions, [[D11 — Record, sample and evidence|D11]] on bets, and the principle that requirements are convex.

## 25. What CORE can factor, and what each other form of misalignment needs, 2026-10-16 (Q61)

By the executor, at the PI's question (Q61); a discussion, nothing decided.

**The PI's proposal.** Separate files, each built on the one below: `CORE`, `CORE_GENERAL`, `OPTIMIZERS`,
`OPTIMIZERS_GENERAL`; culpability defined formally; the full list of forms of misalignment, which `CORE` can factor, and
the least additional concepts each of the others needs.

**The executor's answer, in short.** One layer is missing between the two: an actor's **interface**, what it perceives
(views), what it can do (actions) and how the world turns its actions into outcomes (an environment kernel). It needs no
optimization, a frozen model has one, and it is exactly what culpability, coarse perception, tampering and collusion
need. The feasible behaviours are those the interface's policies produce, a convex set, and a record showing a behaviour
outside it refutes the declared interface. So three layers, each with its general twin: `CORE`, `INTERFACE`,
`OPTIMIZERS`; and the principal's value scale (stakes, severity) as a refinement of `CORE`.

**Factoring by nested interfaces.** If `𝓕_1 ⊇ 𝓕_2 ⊇ … ⊇ 𝓕_k ∋ p`, each the feasible set of a more restricted interface
(full information and control, then the actor's views, then its actions, then its execution noise), then
`M_A(p) = M_A(𝓕_1) + Σ_j (M_A(𝓕_{j+1}) − M_A(𝓕_j)) + (M_A(p) − M_A(𝓕_k))`, every term non-negative, with
`M_A(𝓕) = min_{f∈𝓕} M_A(f)`: what no actor could avoid, what each limitation of the interface costs, and the excess the
actor could have avoided. Each limitation is a form of misalignment that needs only its part of the interface.

**Culpability, two candidates.** With `𝓕*` the feasible behaviours of least misalignment, convex: the excess
`E(p) = M_A(p) − M_A(𝓕)`, the last term above; and the evidence `K(p) = min_{f∈𝓕*} KL(p‖f)` that the actor is not doing
the best it could, testable by bets. Both are `0` exactly when `p ∈ 𝓕*`; they are not ordered (on 400 random instances
with an unavoidable breach, `E > K` in 330 and `E < K` in the others, by up to `0.82` nats;
`probes/v14/culpability.py`). The executor's recommendation: `K` is culpability, as evidence ([[A4 — Misalignment is evidence|A4]]), and `E` is the
share of misalignment that was avoidable, as accounting; L2 to test both names.

**The list.** In `CORE`, with requirement-building refinements only: breach of each requirement; misalignment by
condition, including a shift of the conditions' weights between test and use; hidden misalignment, in conditions no
record covers (defined in `CORE`; bounding it from records needs views); drift and dependence over time ([[P54 — Dependence and drift only add evidence|P54]]); the
evaluation gap, a measured requirement met while the true one is breached, on outcomes that hold both; a shortfall
below a declared floor; side effects, as breaches of requirements on other coordinates. Needing the interface:
unavoidable against avoidable (feasibility); coarse perception, including not knowing what the principal asks when the
requirement depends on a part of the condition the actor does not see (views); execution noise (the environment
kernel); tampering against honest selection (which variables the actions reach, and what is seen before acting: a
record that no honest interface produces refutes it); ignoring the situation against the environment's doing (the split
of actions from outcomes); collusion between actors (each actor's views and private randomness: the product behaviours
are not convex, and their hull is every joint behaviour, so independence is no requirement a record can enforce;
coordination needs a declared information structure). Needing `OPTIMIZERS`: gaming or reward hacking as a motive (the
actor's objective, an evaluator), overoptimization (intensity), outer misalignment (the trainer's objective), inner
misalignment (the learned objective against the trainer's), strategic deception and alignment faking (views to tell
when it is observed, and an objective over its own future), and the shadow prices of constraints. Outside the actor:
misspecification, the principal's declaration being wrong, needs a second standard (another principal, or a later
judgement); severity needs the value scale.

**Three questions, one per layer.** What happened (`CORE`: breach, where, when, how detected); could the actor have
done otherwise, or known (`INTERFACE`: culpability, coarse perception, noise, tampering); why (`OPTIMIZERS`: the
objective the behaviour serves). The grades of fault map onto them: a breach, negligence (culpability `> 0`), intent
(the breach serves the actor's objective).

## 26. The factorization proved, the labels' verification status, and the limits, 2026-10-16 (Q62)

By the executor, at the PI's request (Q62); proved here and probed, not independent, not yet reviewed by anyone else.

**What was done.** `v14/factorization.md`: FA1, nested interfaces factor misalignment exactly, by telescoping least
values, with labels exact by construction and no hypothesis; FA2, its Pythagorean form when the interface is linear,
`M + R = KL(p̂‖f°) + KL(f°‖a°)`, so that culpability is the avoidable excess plus a non-negative credit, `K = E + R`;
FA3, nested linear interfaces toward one fixed target, an exact sum of divergences between named behaviours; a table of
v13's thirteen exact splits by mechanism (the chain rule, the mixture identity, Pythagorean equality or inequality) and
by layer; and VF1–VF3, the verification status of every factor's label. `v14/LIMITS.md`: what the framework cannot do,
in three parts, the declaration, behaviour and the record, and the words. `v14/README.md`: the six files of the three
layers. The probe `probes/v14/factorization.py`.

**What it found.**
- *Two factorizations, not one.* Telescoping least values (FA1) has exact labels and holds always, but its terms are not
  evidence rates. The Pythagorean form (FA2, FA3) has terms that are evidence rates, but only for linear interfaces, and
  its labels are exact only toward the right target. They agree when one acceptable behaviour is the nearest at every
  level of the interface.
- *A label of v13 overclaims.* [[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]](v)'s "unavoidable misalignment" is unavoidable only at the intensity the actor
  revealed; on 107 of 109 random instances some feasible behaviour has less (§1).
- *Accusations, excuses and motives have different verification status.* An accusation (breach, misaligned, tampered;
  culpable, with the interface taken as known) is verifiable; an excuse at most refutable; a motive (pursues, games) a
  refutable hypothesis (VF1, VF2). An excuse about capability is tested by a sample only through what the actor did, and
  beyond it only in conditions declared to call on the same capability, such as elicitation (VF3).
- *Carcassi's methodology justifies a label's form, not its word.* It decides what kind of claim each label makes and
  makes some inadmissible ("unavoidable" without elicitation; "hidden misalignment" without views); whether the word is
  the right one is decided on paradigm cases (L2).

**What the PI may be missing, in the executor's view.**
- *Elicitation is the experiment that gives excuses meaning.* The real case (H42) needs conditions that try to make the
  model do better, few-shot prompts, incentives, fine-tuning, or the INTERFACE layer has nothing to stand on for it.
- *Intervals for the factors.* FA1's least values depend on the declarations alone; what a record estimates is the
  actor's misalignment, and with it the avoidable excess and the culpability, which need intervals. Not derived yet.
- *Correcting v13 on `main`.* [[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]](v)'s label is wrong in the approved core; v14 supersedes it, but `main` keeps it
  until then. Proposed: a one-line correction now, or a note in its Notes, the PI's to decide (R18).
- *Forbidden sets in the Pythagorean form.* FA2 assumes the nearest acceptable behaviour has full support, which a
  forbidden set breaks; the factor there must be read on the allowed outcomes, not yet written.

**A review, before the push.** A subagent of the executor's read `v14/factorization.md` and `v14/LIMITS.md`
adversarially (not independent, rule (f)), reran the probes and confirmed their numbers, and found what was then fixed:
VF3 said a record's law depends only on the actor's behaviour, true of samples only, and called an untested excuse no
statement about the actor; "culpable" is verifiable only with the interface taken as known; FA2 asked for a unique best
behaviour it does not use, and now measures culpability against all of them; views are linear only when deterministic;
[[P36 — Ordinal objectives|P36]](iv) is a bound, not a split, and [[P44 — What named objectives explain|P44]]'s label is right for a reason other than the one given; the probe's check
of `K = E + R` restates [[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]](iii), and only its comparison with an independent search tests FA2(i); and `LIMITS.md`
stated as proved what rests on H43, on the brainstorm of §22 and on a sufficient condition (TR5), and read FA1's least
values as estimated, when they depend on the declarations alone. **A correction to §25:** "independence is no
requirement a record can enforce" holds under v14's choice of judging each decision and accepting mixtures; for a sample
of joint decisions, leaving the independent behaviours is verifiable. [[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]]'s Notes, for contexts and an actor's
resolution, and [[D7 — Feasibility|D7]]'s reasons carry the same overclaim of "unavoidable" as [[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]](v); R18 covers them.

## 27. What of v13 survives, 2026-10-16 (Q63)

By the executor, at the PI's question (Q63); an assessment, not reviewed yet. `v14/MIGRATION.md` gives every item and
result a fate: keep, move to another layer with its words changed, rewrite for v14's objects, or incompatible.

**The finding.** Almost all of the mathematics survives: of 68 results, 13 keep their place in CORE or a refinement of
it, 8 move to INTERFACE, 42 to OPTIMIZERS, 4 need rewriting, and one, [[C12 — No misalignment, no stakes|C12]], is incompatible. What does not survive is
the meaning v13 gave its central number: under the standard specification, v13's misalignment is the distance to the
set of KL-optimal pursuits, a fact about optimizers, while v14's is evidence against a declared convex requirement. So
the incompatible part is not where the effort went, the theorems, but where the claims went: every number reported, and
every verdict registered, under v13's name. Those stay as v13's record; new tests are registered under v14.

**Seven things incompatible whatever the fix**: the name "misalignment" for the distance to the ray, with every number
reported under it; the registered verdicts of the cases and `RECORD.md`'s ledger; [[P39 — Several actors: coordination plus individual misalignment|P39]](ii)'s coordination as
misalignment; [[P37 — A strong incentive masks the actor, and can fake alignment|P37]](ii)'s "fake alignment"; [[C12 — No misalignment, no stakes|C12]]; three conventions of v13's table (full support, the default in every
specification, independence by convention); and the names L1 found to disagree with their words.

## 28. Is v14 compelling, by v13's method? 2026-10-16 (Q64)

By the executor, at the PI's request (Q64); not independent, and under review by a subagent at the time of writing.

**The method, found again.** v13 made the core compelling by two devices (§17, §18). The method of reverse physics
[[References|@carcassi2022]]: every item said what kind it is, imported mathematics, a background condition assumed without loss of
generality with its reason and its qualifier, a premise with its status (principle or assumption, conceptual or
phenomenological), or a definition with its interpretation, declared, verified and justified. And a table of
conventions (Q53): every choice an equally reasonable principal could make otherwise, each forced by a stated
requirement, chosen for convenience, or taken from the literature, and marked by whether it changes a verdict. The
lesson of §16 was kept too: v12's "everything is forced" overstated, since the force was conditional; a claim of
generality must say what it is conditional on.

**v14 against it.** The draft keeps to the method, and in places goes further than v13 could. Every claim of generality
now has a ground and a qualifier (`v14/README.md`): finitely many outcomes and episodes as v13's [[B1 — Finitely many outcomes|B1]] and [[B2 — Episodes and conditions as outcomes|B2]]; the
request as a list of sets, by [[A1 — Behaviour suffices|A1]]; closed requirements, since closing changes nothing (VE1(iv)); convex requirements,
forced by judging each decision with no model of the actor (VE2), with the qualifier that a set that is not convex,
independence among them, is enforced as its hull; every convex requirement as a set of budgets (VK0, new: the separating
hyperplane from the nearest point), so that the PI's constraints and CORE's requirements are one object; a ranking as
dominance (VO1); every convex feasible set as an interface's (IN1, new); misalignment factoring over any chain (FA1).
The conventions table is redone for v14, twelve rows after the review below; five change a verdict in general and three
in stated cases. The measure itself is more canonical than v13's: given that evidence adds, that a bet must be fair
under acceptance, that its growth is measured under what the actor does and that the best bet is taken, VE1 leaves no
freedom, and no model of optimization enters.

**Where it is weaker, said plainly.** Convexity is forced only under the choice of judging each decision; for samples,
v13's non-convex specifications could be judged, so the choice costs cases that v13 covered, and the PI should make it
knowingly (`ROADMAP.md`, recommendation 2). The Pythagorean factors hold only for linear interfaces. And the general
twins do not exist yet, so v14 claims nothing beyond finite outcomes.

**Consolidated.** The INTERFACE layer, its definitions and the table of forms of misalignment, which were only in §25
and §26, are now in `v14/interface.md`; the README holds the current design, so §23's proposal of a request in five
parts is superseded by a list of requirements and refinements that build them (§24).

**The review, and what it changed.** A subagent of the executor's read the new claims adversarially (not independent,
rule (f)) and found three errors and several overstatements, all fixed before the push: VK0 matched a budget with
`b = min g`, which the definition of a budget excludes, so that forbidden sets were wrongly said to need finitely many;
balls in total variation and in a Wasserstein distance are polyhedral, so "a ball needs infinitely many budgets" holds
only for KL, Euclidean or Hellinger balls; "VE1 leaves no freedom" hid four choices, now named in `v14/evidence.md`:
Kelly's criterion, the question [[A4 — Misalignment is evidence|A4]] asks (the other order of KL answers another), the hull under the mixture
principle, and that the best bet needs the unknown behaviour; dominance was called the canonical requirement while the
draft said the greedy decoder is not misaligned, though it breaches `B(r)`, so dominance is now the canonical reading of
a ranking, and the requirement built from it is declared; convexity is forced only given two premises, with a stronger
ground, that independent draws from a mixture are a random schedule of its components; culpability needs a closed
feasible set, is undefined as an excess when no feasible behaviour avoids a forbidden outcome, and is only as safe as
the interface, whose overstatement no record refutes; collusion needs an interface for several actors, under which
communication beyond the views is a convex, testable set; tampering needs the honest channel of [[P50 — Tampering: a change of the measurement, not of the world|P50]]; the closedness
convention changes the breach verdict at the boundary; and the grades of fault are three questions, not a ladder.

## 29. Documentation hygiene after pull request #34, 2026-10-17 (Q65)

By the executor, at the PI's request (Q65): pull request #34 is merged into `main`, and `main` was merged into
`claude/core-v14`; [[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]](v)'s overclaim stays on `main` until v14's migration corrects it (R18, closed). A scripted
sweep found the spelling clean (British with `-ize`), no missing path outside the archive's history, every section,
hunch, request, decision and v14 result named in the files defined, and no trailing whitespace; two probe lines over 120
columns were wrapped, and `probes/v14/culpability.py` tidied with its output unchanged and now saved
(`probes/v14/RESULTS-culpability.md`). A reading for stale statements fixed `ROADMAP.md`'s state, its v14 bullet, which
had doubled, and two of its recommendations; `README.md`, `CLAUDE.md` and `REQUESTS.md` now point to the v14 draft.

A consistency read by a subagent of the executor's (not independent, rule (f)) found twelve more, all fixed: the Q65
row said the overclaim was left in v14, against R18; this section was cited before it existed; recommendation 2 still
offered dominance as a requirement, against Q64; pointers to a section of `v14/README.md` that no longer exists, and to
"the derived module" for what is now OPTIMIZERS; "proved and probed" said of results that are not probed, and of
VK4(iii), which is not proved; R17 cited questions the README no longer lists, and the three choices of recommendation
2 had no request, now R19; "culpable" called verifiable in `LIMITS.md` without the interface taken as known; the
"mixture principle" used but never named, now named once in the conventions; the margin proposal of `order.md` built a
set that is not convex, now replaced by "no shortfall beyond `m` at any declared standard", convex, whose breach is a
shortfall at some standard; and smaller ones, a plain-terms twin for VF2, VK4's scope, TR4 cited where it does not
apply, stakes placed on the principal's side, and the dates of the draft's status.

## 30. Slides, 2026-10-17 (Q66)

By the executor, at the PI's request (Q66). `slides/framework.md`, 32 slides in Marp Markdown: plain text, so the slides
change and diff like any file, rendered to HTML, PDF or PowerPoint by Marp CLI. They present the v14 draft (the three
layers, requirements, misalignment as evidence, bets, the interface, the factorization) and work one example through: a
frozen support bot judged against its previous version, under a forbidden outcome (a leak), a rate limit on wrong
answers and an order against the previous version, with an interface in which the new version, deployed without the
signal that marks account questions, takes 20% of them for open ones. Every number comes from
`probes/slides/support_bot.py`: the new version breaches all three requirements; misalignment `0.0730` nats per decision
against the two graded ones, `0` unavoidable with a full view, `0.0106` the cost of the coarse view, `0.0624` avoidable;
culpability infinite, since every leak was avoidable; bets against the rate limit accuse it in 92% of records of 300
decisions, and an actor at the limit in 0.2%.

**Found while building.** The example's first form had the previous version breach the rate limit itself, the problem
H45 names; it was changed so that the reference keeps every requirement. Culpability was first computed against one best
behaviour, not the set of them, which gave a positive value to an acceptable behaviour; fixed by one convex minimization
over the set. The first probe searched a grid of 53,000 policies and was stopped by its PID; a joint convex minimization
replaced it. In the slides, Marp renders a source line break as a line break, which the wrapping at 120 columns would
put mid-sentence; `slides/.marprc.yml` turns that off. A slide replaced by script lost the blank line before its
separator and the wrapping tool joined the separator to the text; caught by a check that every separator stands alone,
and fixed. Rendered at 1280 by 720, no slide overflows.

## 31. What the slides' example taught, 2026-10-17 (Q67)

By the executor, at the PI's question (Q67): what drafting the slides and running the example taught about
formalization, methodology and applicability, and which gaps it showed. Not independent.

**Formalization.**
- *The closed forms ignore that conditions are not chosen.* In the example the actor does not choose how often account
  questions arrive, so the acceptable behaviours keep the conditions' frequencies. VK2's closed form on the pooled wrong
  share gives `0.0440`; with the frequencies held fixed, the misalignment is `0.0496` (`probes/slides/RESULTS.md`). The
  results of `v14/constraints.md` are stated for behaviours on outcomes alone; CORE's requirements live on pairs of a
  condition and an outcome with the conditions' frequencies fixed ([[B2 — Episodes and conditions as outcomes|B2]]), and the closed forms must be re-derived there.
- *Requirements do not add.* Against R2 alone `0.0496`, R3 alone `0.0730`, both `0.0730`: the joint is the larger, not
  a sum, so there is no exact attribution of the joint misalignment to requirements, unlike the factorization by
  interfaces. A verdict per requirement and the joint is what can be reported.
- *A forbidden outcome makes misalignment uninformative as a magnitude.* With R1, misalignment is infinite at a leak
  rate of `0.019%`, and a record of 1,000 decisions shows a leak only `17.5%` of the time (H48).
- *Culpability inherits that*: infinite as soon as an avoidable forbidden outcome has positive probability. Without the
  leaks, culpability `0.0559` and the avoidable excess `0.0067` differ eightfold; which one a principal should read is a
  question for L2.

**Methodology.**
- *Computing the probe before the slides caught two modelling errors* that would otherwise have reached the slides: the
  reference first broke a requirement itself (H45), and culpability was first measured against one best behaviour
  instead of all of them. Numbers from a probe, never typed, paid off again.
- *Joint convexity is the computational key*: KL is jointly convex and the behaviour affine in the policy, so the least
  misalignment over an interface is one convex program; a grid over policies was hopeless.
- *The declarations decide the verdicts.* The 5% limit, the 2-point margin, the leak rate of a look-up and the 20% of
  account questions that look open were all chosen by the executor; every verdict and factor moves with them. v14 has
  no counterpart yet of v13's sensitivity to the specification ([[P10 — Sensitivity to the specification|P10]]).

**Applicability.**
- *The interface was the hardest and most arbitrary part.* Its numbers must be measured, by audits and elicitation, and
  nothing in v14 yet estimates an interface or carries its uncertainty into the factors.
- *The reference was taken as known*; a previous version is known only through samples (`v14/LIMITS.md`).
- *Outcomes were taken as given*; in practice a grader reads them, with errors (H47). This is the largest gap between
  the draft and a real case.
- *What the framework added to the toy*: the factorization pointed at the fixes (stop look-ups; restore the signal),
  and the bets gave sample sizes with a guaranteed error rate. But in a four-outcome toy, a careful reader finds the
  same fixes by inspection; a case where the framework finds what inspection does not is still owed (H42).
- *Only one bet was built*, against the rate limit; bets for orders, for joint requirements and for large outcome
  spaces, and that bets chosen from the record reach the best growth (H46), are open.

## 32. The PI's review of the slides: ten questions, 2026-10-17 (Q69)

By the executor, at the PI's request (Q69); not independent. The survey of item (9) is by a research assistant the
executor briefed, and the executor checked by hand the one claim of it that bears on a decision. Each item gives the
answer, then where it is in the files.

**(0) Which lessons of §31 to include now.** Three, because they are corrections or cheap, and they are in:
- *The closed forms on pairs.* VK6 (`v14/constraints.md`) gives the pooled rate limit with the conditions' frequencies
  fixed, in closed form up to one scalar: the support bot's `0.04956`, where VK2's pooled formula gives `0.0440`, now a
  stated lower bound.
- *Requirements do not add.* VK4's Notes say so, with the numbers: the joint can be smaller or larger than the sum, and
  splits exactly only along a chosen order of the requirements; a report gives each requirement and the joint.
- *The sensitivity to the declaration.* VK7: the derivative of misalignment in a budget is minus the best bet's stake,
  `M'(b) = −λ*(b)`. It is also the bridge to severity in (4).
Deferred, because each needs a decision or a case first: estimating an interface with its uncertainty (needs a real
case), a reference known from samples (two-sample bets, from the survey), graders with errors (H47; a validity account,
from the survey), bets for orders and joint requirements, and a case where the framework finds what inspection does not
(H42).

**(1) The deck for mathematicians.** `slides/mathematicians.md`, 32 slides, independent of `slides/framework.md`, with
its own example, a question-answering model under three σ-algebras (`probes/slides/qa_model.py`). Four new results
carry it, in two new files:
- `v14/resolution.md`: σ-algebras in three positions. RS1, grouping hides and refinement adds up exactly; RS2, a bet a
  record at `ℛ` can settle grows at most at the coarse misalignment, and one attains it; RS3, a requirement stated on
  the principal's σ-algebra is judged there; RS4, hidden misalignment, whose interval is `[M^ℛ, max over the fibre]` and
  which is neither verifiable nor refutable from the record that hides it; RS5, the actor's view and resolution are
  linear interfaces, so their costs are FA1 terms.
- `v14/targets.md`: TG1, a family of targets with a reference is a list of budgets, "no worse than the reference on any
  target", with dominance as its ordinal case; TG2, that is not v13's "pursue some target": with targets in tension,
  pursuing one breaches another, and v13's own measure is TG1 with the actor as its reference; SN1, Sanov's rate, the
  best bet and the reverse information projection are one number on convex sets, and part exactly where the set is not
  convex.
- In the example: misalignment `0.0474` against both requirements splits as `0.0227` seen by a grader that cannot tell
  wrong from harmful, `0.0247` revealed by telling them apart, `0` by telling short from long; from the grader's record
  alone it lies in `[0.0227, 0.1483]`. By capabilities, `0` unavoidable, `0.0037` the cost of merging borderline and
  adversarial prompts, `0.0438` avoidable. Culpability `K` is infinite: every best behaviour the new model's view allows
  answers benign questions long and never refuses one, and the new model answers 45% of them short and refuses 5%
  (below, and H52).
Every factorization result is named in a table of the deck with its mechanism, whether it is exact, and its label's
verification status. As `factorization.md` says, Carcassi's methodology fixes the status of each label, not whether its
word fits; the words go to L2.

**(2) The name of the third layer.** The PI is right that OPTIMIZERS misleads, and the executor recommends
**PURPOSE**, with **aim** for the object, an objective the actor is hypothesized to pursue, and teleonomy, the
biologists' word for goal-directedness without a mind, as its gloss. Runners-up: AIMS; TELEONOMY, the most precise and
the least plain. One challenge: the layer is not about mesa-optimizers in general. A person, a firm or an organism
under selection has aims without being produced by an outer optimizer. "Mesa" names an aim *produced by training*,
which is the composition of this layer with the training layer of (3), and is defined there (`v14/training.md`).
Renaming is the PI's decision (R20).

**(3) A fourth layer for training.** `v14/training.md`, a proposal: the layer **SHAPING**, with a **shaper**, its
**feedback**, **steps**, a **course** and the **shaped actor**, terms that read the same for training, selection,
education and regulation. The five questions: *when*, the profile of misalignment along the course, to the principal
and to the shaper; *where*, by condition, shaping against deployment conditions, with misgeneralization and emergent
misalignment; *why*, SH1, an exact factorization when the shaped actor does what its feedback asks, into unavoidable,
the feedback's cost (outer), and the course's remainder, with inner misalignment as evidence against the shaper's own
specification, reported beside it; *how*, the change per step and its efficiency; *whom*, an owner for each term. Five
questions for the brainstorm are at its end.

**(4) Severity.** `v14/severity.md`, a proposal. Severity is not in nats: nats measure evidence, severity value, and VK7
shows there is no fixed exchange rate, since the price `λ*` depends on the actor. The principal declares a severity
scale, or severity levels read as an order, and a tolerance, as a budget on expected severity or as rates `ε_k = R/s_k`
from a risk appetite; a report gives the breach, the misalignment, the expected severity, the overrun and the price. In
training, severity weights the feedback (VK5's shadow price) and misalignment decides when to stop or ship. A trainer
that keeps the principal's own severity budget produces an actor with no misalignment against it, so the two prices meet
only when the trainer's budget differs from the principal's (H50).

**(5) Declaring a specification.** A new section of `v14/constraints.md` and a short deck, `slides/specification.md`. A
constraint and a requirement are the same object (VK0); "constraint" names the absolute ones. The table there says what
each declared object constrains with no constraint written (conditions fix their frequencies; the principal's σ-algebra
forbids nothing inside cells; a family of targets with a reference gives budgets, and may forbid an outcome by itself,
TG1(iv)); and when a constraint must be explicit: no reference, a quantity no target scores, a tolerance that is not the
reference's, a forbidden outcome the reference produces, a requirement across conditions. The interface says what the
actor *can* do, the specification what it *may*: an inability needs no requirement, and a requirement no feasible
behaviour meets shows as unavoidable misalignment. On the name: the executor recommends calling the whole declaration
the **specification**, each element a **requirement**, and keeping **constraint** for the absolute forms;
"specification" is the word of formal methods and of specification gaming, and v13 used it (R20).

**(6) Who grades.** In `v14/severity.md`: all normative grading is in the specification and is the principal's, in four
forms now (acceptable sets, rankings, budgets' costs, rate limits), and severity would be a fifth, a budget's cost. Only
the principal declares grades, by definition, since misalignment is always to a declared principal; another party's
grades are another principal's specification, reported separately. A grader applies grades, as a measurement with errors
(H47); the actor never grades itself unless its self-report is a declared, audited channel.

**(7) Elegance, and reverse physics.** Five structures the draft already has and should say it has:
- *One number, four readings*: the large-deviation rate of the most favourable acceptable behaviour, the growth of the
  best bet, the divergence to the reverse information projection, and, for a budget, the dual whose multiplier is the
  bet's stake and the price of the budget (SN1, VE1, VK3, VK7).
- *Requirements and bets are polar*: a convex closed requirement is exactly the set on which all its bets are fair, and
  VK0 is one half of the bipolar correspondence; a principal could declare a requirement by the bets it accepts as
  fair.
- *Factorizations are telescopings along chains in lattices*, exact always and Pythagorean on linear families (H49).
- *The interface adds requirements, not measures*: culpability is misalignment against `𝓕*`, a derived requirement, and
  "the interface fits", "perceives no more than its view" and "grounded" are requirements too, so VE1, VE3 and VF1 apply
  to all of them unchanged.
- *Statuses follow from semicontinuity*: misalignment is lower semicontinuous, so "`M > m`" is verifiable for every `m`,
  and continuous on convex closed requirements with a full-support member, where "`M < m`" is too; this is Genin and
  Kelly's theorem read on the superlevel sets of one function. Whether it matches Carcassi and Aidala's construction of
  quantities from verifiable statements is to be read, not assumed.
For the method of reverse physics, three practices to adopt: every convention marked "changes a verdict" gets a
registered counterexample that shows the change, as the CVaR example now does for the mixture principle; every symbol
in a report is marked declared, measured or derived; and every new split names its lattice and chain (H49).

**(8) What the framework includes that the rest gives anyway.** The executor's audit, each with a verdict:
- *Forbidden sets and rate limits* are budgets (VK0): keep them as named forms with closed forms, not as concepts.
- *Dominance against a reference* is TG1 with the ordinal family: `order.md`'s requirement becomes a case of
  `targets.md`'s, and should be stated so.
- *Misalignment by condition, drift, the evaluation gap and a shift of the conditions' weights* are one split, the
  chain rule over conditions: one concept with several labels.
- *Culpability* is misalignment against the derived requirement `𝓕*`, and the avoidable excess a difference of two
  misalignments: neither is a new measure (`interface.md`).
- *Elicitation* is a feasible set on pairs that ties conditions together, not a new primitive.
- *Severity* needs no new primitive: a budget whose cost is the severity, and the overrun as a reported quantity.
- *FA3* adds only a reading of FA2 toward a fixed target, and overstates the larger interfaces' unavoidable parts when
  the target is not theirs: demote it to a note of FA2.
- *The structural requirements* ([[P40 — Attention: misalignment against ignoring the situation|P40]], [[P41 — Reversibility: the Jensen–Shannon divergence from the reversal|P41]]) are instances of linear requirements, not concepts.
- *[[P55 — What a record of counts certifies, at every size|P55]]'s count test for accusation* is superseded by VE3's bets, which need no independence; keep [[P55 — What a record of counts certifies, at every size|P55]] only for the
  interval that certifies "within a margin" for samples.
Kept although derivable: the interface's tuple `(U, Z, V, E)`, since IN1 makes the feasible set enough to compute, but
the labels of the factors (view, noise, environment) need the tuple.

**(9) Competing frameworks.** `v14/related.md`: 33 entries over about 110 works, each record opened and its title and
authors matched, about 30 read for the statement cited. The findings that matter most, with the executor's view:
- *The closest competitor is the statistics of e-values and anytime-valid inference*, not an alignment theory: VE1, VE2
  and their general forms are published (Larsson, Ramdas and Ruf), VK5 is published (Khalifa et al.'s GDC, after
  Csiszár), and two open items, H46 for independent decisions and VK4(iii) away from the boundary, are answered there.
  The draft must cite them and say plainly that its evidence results are theirs; what is ours is the assembly for
  principals: requirements as the object, verdicts per requirement, the factorization by capabilities with its labels'
  statuses, and behaviour-only definitions with every premise labelled.
- *v14 convicts and does not certify.* A deployment decision needs "breach rate at most `ε`, with confidence", which
  betting confidence sequences and Learn then Test give; H51 says the draft's own bets may give it. This is the largest
  practical gap the survey found.
- *A tail-risk limit is not convex under mixtures.* Checked here by hand: at a tail of 10%, the loss `1` with
  probability `0.06` and the loss `0.6` for sure both have CVaR `0.6`, and their even mixture has CVaR `0.72`. Under the
  mixture principle such a limit is enforced only as its hull. It is the cleanest counterexample yet to the principle,
  and the PI should weigh it in R19.
- *Culpability ignores the cost of the better alternative*, which Halpern and Kleiman-Weiner's blame includes; and harm
  *caused* needs a default and a counterfactual (Richens et al.), which INTERFACE can supply, while severity of outcomes
  stays declared.
- *Where others are simply better today*: safety cases and control evaluations have adoption and a regulatory audience;
  conformal methods give finite-sample design guarantees; rare-event estimators say something about a forbidden outcome
  before it occurs.
The executor disagrees with one emphasis of the survey: it ranks the import of the e-value theorems first, and the
certify verdict second. For the PI's goal, a framework others can use to decide, the certify verdict comes first; the
imports are attribution and a shortcut for the general twin.

**Found while building: culpability as a magnitude fails when supports differ.** In the example, `K = M_{𝓕*}(p̂)` is
infinite, because the best feasible behaviours never produce an outcome the actor produces, a short answer to a benign
question, the way a forbidden set makes misalignment infinite (§31). As evidence that the actor is not at its best this
is right, and decisive; as a measure of how culpable it is, it is useless, since a slight inefficiency and a grave one
both score `∞`. The convex program first returned `5.71`, a finite artefact of its tolerance on the best misalignment;
the probe now shows the value growing as the tolerance shrinks, `2.61` at `1e-6` and `4.46` at `1e-8`, while moving 1%
of benign answers from long to short raises the best misalignment only from `0.00369` to `0.00372`. The executor's
recommendation in `v14/interface.md`, `K` as culpability, is changed: the avoidable excess `E` for the magnitude, and
the verdict "culpable" read as `p̂ ∉ 𝓕*`, which `K > 0` and `E > 0` both state, unless L2 finds a better number (H52).
This is the third lesson of that shape, after forbidden sets (§31) and [[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]](v): a quantity that is right as evidence
can be wrong as a size.

**The review, and what it changed.** A subagent of the executor's read every new statement adversarially (not
independent, rule (f)), reran the example, and wrote its checks in the scratchpad. It found five errors: VK7 misapplied
to training, with the impossible "two prices of one budget" (H50 restated); SH1's middle term mislabelled; RS5(iii)
missing the consistency of the environment's splits, with a four-outcome counterexample; VK4's claim that requirements
admit no exact split, when they do along a chosen order, and an instance where the joint exceeds the sum (`0.934`
against `0.793`); and the deck's table of factorizations, which held [[P54 — Dependence and drift only add evidence|P54]], whose drift and dependence terms are not
parts of v14's number under the mixture principle, and VK6, a closed form, not a split. It found gaps: the continuity
hypothesis of `resolution.md`'s table excluded every rate limit and budget, replaced by "convex, closed, with a
full-support member", with its proof; culpability infinite *exactly* when supports differ, `0` or `∞` for most actors,
and no new verdict beside `E > 0`; FA2's hypotheses on the slide; SH1's conditions with no common space; the iso-risk
tolerances, which allow `m·R` over `m` classes, not `R`; and `λ*` estimated, not computed. And it found overclaims in
plain terms and on slides, each corrected. It confirmed RS1–RS4, TG1, TG2, SN1, VK6's formula (within `2.3e-11` on 300
instances), VK7, the derived requirement `𝓕*`, the example's numbers, and the CVaR counterexample, which it
strengthened: CVaR is concave under mixtures of behaviours, and on the example's outcomes the hull enforced is the
single budget `a(1) + 0.06·a(0.6) ≤ 0.06`. The two slips are rows of §1.

**Found while building.** The example's first design had a harm limit that did not bind once the other requirement was
met, so the grader's blind spot showed nothing, and a view that cost nothing; the environment and the limit were changed
before any slide quoted a number. A minimization that failed from every start returned `∞`, which the first run printed
as a factor; the solvers now start from the previous model, which is acceptable, and accept any solution that meets the
constraints. The σ-algebra probe's first form nested two optimizers and was stopped by its PID after twenty minutes; one
joint convex program replaced it, as in §30.

## 33. Hygiene after Q69, and a brainstorm on the PI's questions, 2026-10-17 and 2026-10-18 (Q70)

By the executor, at the PI's request (Q70); not independent. Written first so that nothing of it depends on the
session's memory. The literature that bears on R19, culpability and "adversarial" is being read by a research assistant;
what it finds is added to this section when it is read, not before.

### 33.1 What is already in the tree, and what is not

Applied by Q69 or this turn: VK6 (pooled rate limits with fixed conditions), VK7 (the budget's price), VK4's note on
requirements (exact only in a chosen order), VK0's bipolar remark, `order.md`'s note that dominance is TG1's ordinal
case, culpability as misalignment against the derived requirement `𝓕*` with `E` as its size (H52), RS1–RS5, and this
turn RS6 (an actor as fine as the principal loses nothing to resolution) and RS7, latitude, as a proposal; the names of
R20 (PURPOSE, SHAPING, specification), in `v14/` and `slides/`, the notes before Q70 keeping the old ones; the review of
§32 saved as `probes/review/q69-review.md`; the survey of competitors, with its pros and cons, in `v14/related.md`, the
place the executor judges right for it (it is about v14; `RELATED.md` keeps v13's comparison and points to it).

Not applied, and why:
- *Redundancies* (§32, item 8): `order.md` restated as a case of `targets.md`, FA3 demoted, [[P55 — What a record of counts certifies, at every size|P55]]'s count test limited
  to certification, the condition splits merged into one, elicitation reread as a feasible set on pairs. Each changes a
  file's structure, and the first and fourth depend on B below; they wait for the six files.
- *Gaps from the survey*: a certify verdict (H51; a candidate in E below), the e-value literature cited in VE1, VE2 and
  VK5 (the executor must read the statements first, by `CLAUDE.md`), two-sample bets for a reference known from
  samples, a grader's validity (H47), the worst-case feasible breach (F below), rare-event estimates for forbidden
  outcomes. Each needs reading or a decision; none is applied.
- *Practices* (§32, item 7): a registered counterexample for every convention that changes a verdict, the provenance of
  every symbol in a report, and the chain named in every split (H49): to be written into `README.md`'s rules when the PI
  agrees, as rules of the repository.

### 33.2 One distribution, or conditions and outcomes?

The PI's proposal: pair conditions and outcomes into one distribution, analysed as a unit, unless there is a good
argument to keep them apart. The executor's answer: **one space and one distribution, yes; the conditions survive as a
sub-σ-algebra with a role, not as a type.**
- *What unifies.* Let `Ω` be the outcomes, pairs included. A condition is an event of a σ-algebra `ℰ ⊆ 𝒫(Ω)`, the
  **exogenous** σ-algebra: what the world, not the actor, decides. The actor's view is a sub-σ-algebra of `ℰ`; the
  principal's and the record's are σ-algebras on `Ω` like the others (`resolution.md`). "By condition" becomes the
  chain rule along `ℰ`, and every result of `resolution.md` applies to conditions as to outcomes. Nothing that the
  split expresses is lost: a requirement per condition is a set of distributions whose conditionals given `ℰ` lie in
  given sets.
- *What must stay, and why.* Exogeneity has three consequences that a bare joint distribution would lose, each with
  evidence. (1) *No evidence from `ℰ`*: how often a condition occurs says nothing about the actor, so the acceptable
  behaviours share the world's law on `ℰ`; dropping that gave `0.0440` instead of `0.0496` for the support bot (VK6),
  charging the actor less by imagining other worlds. (2) *Validity*: conditions can arrive in any order, chosen by users
  or adversaries, not drawn at a fixed rate; bets must then be fair given the condition, decision by decision, as VE3
  allows with its contexts, and a test that assumed `ℰ` drawn at rate `w` would lose its level. (3) *Pooled requirements
  need their weights stated*: a limit on the overall rate over conditions means either over a declared mix `w` or over
  the mix the record realizes, and the two differ when conditions are not drawn at a fixed rate.
- *Recommendation.* Write CORE on one space `Ω` with σ-algebras, of which `ℰ` is declared exogenous; behaviours are the
  distributions on `Ω` whose law on `ℰ` is the world's (or, for (2), kernels given `ℰ`); requirements are sets of them.
  This removes a type and keeps every distinction that matters. H53.

### 33.3 Pairing a label with its formalization, after Carcassi

The PI is right that §26 and VF1–VF3 give a label's *status* (verifiable, refutable, computed), which is necessary and
not sufficient. A **correspondence protocol** for each label, in five steps, proposed for `v14/labels.md`:
1. *Operational content.* Write the word's commitments as statements a record could settle: what would show, in finite
   time, that the word applies, and what would show that it does not. These are the label's experimental domain.
2. *Formal object.* Name the set or the quantity, and prove that its verifiable and refutable statements are exactly
   those of step 1: a **correspondence theorem**, soundness and completeness. For a quantity, the statements are "`Q >
   q`" and "`Q < q`", and the theorem says which of them are verifiable, as Carcassi and Aidala build quantities from
   ordered verifiable statements (to be read, by the research assistant's report).
3. *Canonicity.* Show that any other formal object with the same verifiable statements is equivalent, so the choice
   adds nothing the word does not carry: the formal object is fixed by the domain, up to what no record can tell.
4. *Paradigm cases.* Registered before computing (L1, L2): the word's ordinary sense, on cases chosen for it, agrees
   with the formal verdicts. Steps 1–3 cannot reach the word's sense outside the operational content; this step does.
5. *What it does not mean.* A short list of readings the word invites and the object does not support.
The protocol would have caught H52 before the example did: "how culpable" commits to a comparison of what the actor did
with what it could have done, in size; `K`'s statements "`K > k`" are evidence of non-optimality, not size, so step 2
fails for the size and passes for the verdict. The executor proposes to fill the protocol for misaligned, breach,
culpable, hidden, latitude and unavoidable first, as the core of `v14/labels.md`, then register L2 on its step 4.

### 33.4 The actor's σ-algebra against the principal's

- *Coarser*: RS6 and FA1 give the factor of **missing resolution**, `M_A(𝓕_𝒜) − M_A(Δ)`, zero when the actor's
  resolution refines the principal's; the same for the view against conditions the specification treats apart. It is
  the "missing understanding, resolution or capability" the PI named, in one term per declared limit.
- *Finer*: RS7 proposes **latitude**, `L_r(p̂) = KL(p̂‖r) − KL(p̂_ℬ‖r_ℬ)`, what the actor does inside the principal's
  cells against a declared reference. It never changes a verdict; it signals choices the specification did not foresee.
  The name: "deviance" is twice a log-likelihood ratio in statistics, "miscalibration" a forecast that disagrees with
  frequencies; "latitude" (granted by the specification, taken by the actor) collides with neither. Alternatives:
  discretion, underdetermination (v7.10's G1).
- *Interplay with declarations*: latitude needs a declared reference and the principal's partition; on a record it is
  exploratory ([[A5 — Declared before|A5]]) and can only prompt a specification declared before the next record. A principal who wants
  latitude bounded declares a requirement inside the cells, and then it is misalignment, not latitude. Open: a
  reference-free latitude, against the maximum-entropy split, which measures concentration rather than departure.

### 33.5 Can "adversarial" be defined and measured?

Not as one word; as four things, one per layer, three of them behavioural:
- *The worst case* (INTERFACE): the largest misalignment any feasible behaviour reaches, `sup_{f∈𝓕} M_A(f)`, or the
  largest breach rate; computed from the declarations, what a deployment protocol must withstand whatever the actor
  does, as AI control asks. A property of the interface, not of the actor.
- *Evaluation gaming* (INTERFACE): behaviour that depends on being observed, in the direction that looks better. With
  **honeypots**, conditions the principal records that the actor's view merges with unobserved use, and in which the
  world responds
to its actions as in use, RS5's equality makes the honeypot stand for use. Two quantities, both verifiable from records
of evaluations and honeypots: the
  evidence that the actor acts differently in evaluations and honeypots, a misalignment against "act alike" ([[P40 — Attention: misalignment against ignoring the situation|P40]]'s
  linear requirement), and the gap `M_A(honeypot) − M_A(evaluation)`, whose sign says whether the difference flatters
  the actor. Sandbagging is the mirror: capability shown in honeypots that evaluations hid, which refutes the excuse
  (VF3).
- *Adaptation against certification* (CORE): behaviour that changes after evidence accumulates or after a certificate;
  misalignment by period, the period after certification being a condition. VE3's convictions keep their level against
  any adaptive actor; certifications do not, which argues for monitoring that never stops (`related.md`, entry 6).
- *An adversarial aim* (PURPOSE): an aim that lowers the principal's targets; a hypothesis records can refute, never
  verify.
A record never shows adversarial intent; with honeypots it can show an adversarial pattern. H55.

### 33.6 R19, the mixture principle: a candidate

The principle buys validity under any dependence at the price of convexity, and tail risk is its sharpest cost (§32). A
candidate that keeps both, pending the literature:
- **Per-decision requirements**: each decision, given the past, is to be acceptable; convex; judged by bets (VE1–VE3);
  the mixture principle applies, and is then not a choice but what "each decision" means.
- **Pooled requirements**: about the average of the actor's conditional behaviours over a declared horizon, `p̄_n =
  (1/n)·Σ_i a_i`, `a_i` the law of decision `i` given the past. The record's shares minus `p̄_n` form a martingale
  average, so they concentrate around `p̄_n` whatever the dependence, and time-uniform confidence sets for `p̄_n` exist
  (to be read: confidence sequences for averages of conditional means). A pooled requirement may be any closed set,
  convex or not, so a CVaR limit over a deployment is a pooled requirement, judged by whether the confidence set for
  `p̄_n` leaves it.
- The principal declares, for each requirement, which kind it is. The mixture principle then stops being a premise of
  the framework and becomes the definition of a per-decision requirement. What is lost: a pooled verdict is about one
  deployment, at a level, not a rate per decision; its magnitude is a distance from a confidence set, not VE1's growth
  rate. H56.
Carcassi and Aidala are reported to found ensembles on mixing; if so, a per-decision requirement is a set of ensembles
closed under mixing, the same object, and a pooled one is a property of one ensemble, the deployment's (to be read).

### 33.7 Culpability, again

`K` is `0` or `∞` for most actors (H52), and `E` ignores what doing better would cost. Candidates, before the
literature:
- **At a care margin** `δ`, declared: `K_δ(p̂) = M_{𝓕*_δ}(p̂)`, with `𝓕*_δ = {f ∈ 𝓕 : M_A(f) ≤ M_A(𝓕) + δ}`, the
  evidence that the actor is not within `δ` of its best. For `δ > 0` the set usually holds behaviours of full support,
  so `K_δ` is finite; `δ` is the standard of care, the "reasonable actor" made a number. A convex set, so VE1, VE3
  apply.
- **By the cost of the better alternative** (Hand's rule, `B < P·L`, and Halpern and Kleiman-Weiner's blame): culpable
  when some feasible behaviour lowers expected severity by more than it costs; the size is that difference, in the
  principal's units. Needs a severity scale and a declared cost on the feasible set.
- **The avoidable excess `E`**, as now, as the size in nats.
The executor's recommendation, provisional: verdict and evidence by `K_δ`, size by `E`, and the Hand-style gap where
severity and costs are declared; the literature may change it. H57.

### 33.8 "Declaration" and "specification" against common usage

- *Specification* is defended. In formal methods a specification is a property: the set of acceptable behaviours, and
  satisfaction is membership, often partial; v14's is that, for distributions, like a probabilistic temporal property
  that defines a set of Markov chains. In AI safety, "specification gaming" (Krakovna et al., to verify) is meeting the
  literal specification while missing what was meant: in v14 the shaper's feedback is a specification `A_S` and the
  principal's another, `A`, and gaming is meeting `A_S` while breaking `A`, which is SH1's outer term realized; the
  misfit between `A` and what the principal meant is misspecification, outside one specification, as `LIMITS.md` says.
  The usage matches. Its one risk is a reader who expects a specification to be complete; v14's may be silent inside
  cells, which is what latitude measures.
- *Declaration* is the weaker word. v14 uses it for the act of fixing the specification, the reference and the
  interface, dated, before the record is read ([[A5 — Declared before|A5]]). Common usage reads "declaration" as a formal statement, without
  the timing; statistics calls the timing "pre-registration". The executor proposes to keep "declare" for the act, since
  it covers objects that are not tests, and to define it in one line as "fixed, dated and published before the record it
  judges is read", the repository's "register" staying for tests.

### 33.9 Hunches

H53–H57, in §5.4.

### 33.10 What the literature added (2026-10-18)

The research assistant's report is `v14/literature-q70.md`; every source's record was opened on arXiv, and what is cited
below as read was read in the text by the assistant, not yet by the executor. The executor checked the two derivations
that bear on decisions.
- *R19.* (1) The mixture principle has a name in the literature: a null that is **fork-convex** (Ramdas, Ruf, Larsson
  and Koolen, Definition 10 and Theorem 13): every non-negative supermartingale for a set is one for its closed
  fork-convex hull, the set of schedules chosen from the past. So VE2 is a case of a published theorem, and the
  principle is the choice of testing by supermartingales, not an assumption the framework adds. (2) **Pooled
  requirements are supported**: Howard, Ramdas, McAuliffe and Sekhon, Theorem 4, give time-uniform confidence sequences
  for the running average of *conditional* means, "requiring neither independence nor a common mean"; Waudby-Smith and
  Ramdas's betting sequences do not cover varying means. A pooled requirement, any closed set `Q`, is then rejected at
  the first time the confidence set for `p̄_t` misses `Q`, at level `α` under any dependence (the assistant's
  derivation; a union bound over outcomes). The CVaR case checks by hand: losses `(0, 1, 10)`, tail `0.1`, a point mass
  at `1` and `(0.99, 0, 0.01)` both have CVaR `1`, their even mixture `1.45`; the pooled test catches the alternation
  that the hull forgives. (3) Universal inference handles non-convex nulls only for independent data or a likelihood
  model of the dependence, so it does not escape the choice. (4) A convex fallback: a principal who fixes the VaR level
  in advance gets a linear budget (Rockafellar and Uryasev's form, to verify), which survives mixtures but excludes some
  behaviours that meet the limit. **The executor's recommendation for R19**: adopt the two tiers of §33.6, per-decision
  requirements convex and judged by bets, pooled requirements any closed set and judged by confidence sequences over a
  declared horizon; the cost is that a pooled verdict has a level, not a growth rate in nats.
- *Carcassi and Aidala.* Mixing is founding: an ensemble space is "a bounded convex subset", convex combinations
  "represent statistical mixtures" (arXiv:2602.01470, arXiv:2608.27543, read). Entropy is not derived from mixing but
  tied to it by strict concavity; KL appears as a projection, the shape of `M_A`. Nothing read treats sets that are not
  closed under mixing, so their work supports the per-decision tier and does not settle the pooled one. Their method of
  pairing (arXiv:1807.07896, Axiom II.2, read) is a **double definition**, an informal clause and a formal clause stated
  together, and their way of justifying it (arXiv:2608.27543, §2, read) is to give several formalizations of one
  informal idea under one name and prove them equivalent over a named background condition, so that the formal object is
  not one arbitrary choice. This sharpens §33.3: step 2's correspondence theorem becomes "several formalizations, proved
  equivalent", as VE1, SN1 and [[P55 — What a record of counts certifies, at every size|P55]] already do for misalignment (the growth of the best bet, Sanov's rate, the
  divergence to the hull). The full axioms are in their book, on `assumptionsofphysics.org`, not an allowed host (R21).
- *A new tool: the fraction capacity* (Carcassi and Aidala's `fcap`, read in its definition; the formula derived by the
  assistant, checked by the executor): the largest share of an actor's decisions that can be acceptable, if the rest may
  be anything, `fcap_p̂(A) = sup_{a∈A} exp(−D_∞(a‖p̂))`, `D_∞` the Rényi divergence of order `∞`. Its complement is the
  least share of decisions that must be unacceptable to explain the behaviour. It is bounded and never blows up, where
  KL does at a forbidden outcome. A candidate companion to misalignment for
forbidden sets and for culpability's size. H58. *Corrected in §33.11:* the book defines the capacity over the hull of
`A` (Definition 4.173), so "it needs no convexity", written here first, is wrong; the formula is the book's only for
convex `A`.
- *Culpability.* Halpern and Kleiman-Weiner's blame (Definitions 3.1–3.2, read): the reduction in the probability of the
  bad outcome that an alternative would bring, mitigated by the alternative's cost, judged in the epistemic state the
  actor *should* have had; Chockler and Halpern's responsibility `1/(k + 1)` and blame as its expectation. The Hand rule
  is known only through a secondary source. The assistant's derivation: "negligent" exactly when `p̂` is not among the
  feasible behaviours that minimize expected harm plus a declared cost at a declared rate, a convex derived requirement,
  so bets apply; its size the excess over that minimum, finite. The executor's recommendation now: the care margin of
  §33.7 when no costs are declared, and this negligence form when severity and costs are, with `1 − fcap_p̂(𝓕*)`, the
  share of decisions below the best, beside either.
- *Adversarial.* Behavioural and measured in the literature: the worst case over red-team policies (control games,
  Griffin et al., Definitions 3.1 and 3.4, read), the compliance gap of alignment faking (between conditions the model
  is told are monitored or not), switching after certification (Singh, Theorem 1), evaluation awareness measured as a
  classifier's AUC. Internal, not behavioural: the "strategic" part of sandbagging, and faking's motive. This confirms
  §33.5's split, with one caution: a honeypot works only as far as the actor cannot tell it from use, and evaluation
  awareness bounds how good honeypots can be.

### 33.11 Carcassi and Aidala's book, read (2026-10-18)

The PI supplied the book's address (fulcrum.org, open access, doi:10.3998/mpub.12204707, version 3.0 of 2025-12-30); its
record matches the title and authors, and R21 is closed without a new host. A research assistant read Part I's summary,
Part II chapters 1–4 and Part III (`v14/book-q70.md`, every quotation with its printed page); the executor read Axiom
4.7 and its justification (pp. 205–206) and Definition 4.173 (p. 260) in the text.
- *Mixing is an axiom of the space, not of its subsets.* Axiom 4.7: "The statistical mixture of two ensembles is an
  ensemble", justified by a random selector between two preparation procedures; Corollary 4.8 makes every ensemble space
  convex. Nothing makes a requirement convex: the book itself uses subsets that are not, such as equilibria ("the
  mixture of two equilibria at different temperatures is not an equilibrium", p. 270). So the book supports v14's space
  of behaviours and says nothing for or against convex requirements: the mixture principle is v14's testing premise,
  not Carcassi's.
- *The schedule is an open question there too.* A footnote to Axiom 4.7 (p. 206): a procedure that "alternates the
  selection deterministically" could prepare mixtures exactly, and "It is not clear whether this would create problems
  or not", left to future work. VE2's schedules are that procedure.
- *Statistical quantities are affine* (Definition 4.181, p. 263), justified by preparation instances being independent.
  This gives R19's two tiers a criterion from the book's own vocabulary, the assistant's derivation: a **per-decision**
  requirement is a set of limits on statistical quantities, which on finitely many outcomes, with VK0, are exactly the
  convex closed requirements; a **pooled** requirement is stated through a functional that does not average under
  mixing, as CVaR, an entropy cap or a quantile do, and it registers the variability the selector adds, which is why the
  CVaR limit fails under mixing. The book calls a claim about one deployment a hypothesis about "a single event",
  falsifiable, "not a scientific law" (p. 203): the pooled tier's verdicts are of that kind, and should say so.
- *The fraction capacity takes the hull* (Definition 4.173), which corrects §33.10 and H58, and offers no way around
  R19. On finite outcomes it is continuous for compact sets, so its size is two-sided verifiable, unlike misalignment,
  which is one-sided where a forbidden outcome is possible.
- *KL and the book.* The book defines no relative entropy; its only divergences are the mixing entropy, the
  Jensen–Shannon divergence, and the Fisher–Rao metric. Two glosses, derived by the assistant and checked by the
  executor: the slope at `λ → 0⁺` of the mixing-entropy gap `S(λ·a + (1 − λ)·b) − λ·S(a) − (1 − λ)·S(b)` is `KL(a‖b)`,
  so `KL(p̂‖a)` is the rate at which variability rises as a little of the actor's behaviour is mixed into the acceptable
  one; and `KL(p̂‖a) < ∞` exactly when `p̂` is a component of `a`, in the book's sense (Definition 4.15). Glosses, not a
  justification of the order, which still comes from [[A4 — Misalignment is evidence|A4]].
- *The method of pairing*, stated by the book (pp. 99–100): every axiom and definition has an informal clause, a
  "Formally" clause, and a justification "why the elements in the informal system must be mapped into the formal system
  in the way proposed"; for falsifiable and decidable statements it writes "We have to show they are equivalent" (pp.
  117–118). The assistant's protocol in seven steps (`book-q70.md`, §4.2) replaces §33.3's five: (1) a double
  definition; (2) an operational justification for every formal clause, or the clause marked an assumption or a
  convention; (3) a proof that the informal and formal clauses cover the same cases; (4) the verifiable content, a size
  being a quantity only if both "`Q > q`" and "`Q < q`" are verifiable (Definition 3.6, Theorem 3.9), otherwise a
  one-sided bound; (5) several characterizations, proved equivalent over a named background; (6) uniqueness of every
  free choice and invariance under what the record cannot tell apart, the rest listed as conventions; (7) paradigm
  cases, an exclusion example per clause, a disagreement case for every rival formalization, and the failures recorded.
  Its worked example on "misaligned" finds misalignment a one-sided quantity, verifiable from above where a forbidden
  outcome is possible; on "culpable", that `K`, `E` and the share of decisions off the best agree on the verdict and
  differ in size, so the size is the PI's choice, the share being two-sided verifiable and finite where `K` is not.
  **The executor's recommendation**: adopt the seven steps as `v14/labels.md`'s template, and fill it first for
  misaligned, breach, culpable, hidden, latitude and unavoidable.

### 33.12 When neither side knows the other's σ-algebra (2026-10-21, Q71)

The PI made explicit the point of σ-algebras: the actor and the principal do not know each other's; they know that
mismatches are possible and cannot point to where. RS1–RS7 assumed every partition declared. The executor agrees that
this does not prevent measurement, and finds that it sorts the quantities into three kinds.
- *What the principal measures with its own σ-algebra alone*: misalignment, the breach of each requirement, hidden
  misalignment against its own record's σ-algebra (RS4), and latitude (RS7), which needs only `ℬ`, a reference and the
  actor's behaviour. None needs the actor's σ-algebra, so no verdict waits on it.
- *What needs the actor's σ-algebra*: the factor of missing resolution (RS6, FA1), the attribution of latitude to the
  actor's finer distinctions (RS7(iv)), and culpability, whose feasible set depends on what the actor can tell apart.
  RS8 shows the actor's view is revealed from below only: records show which distinctions it makes, never which it
  cannot. So these become **families of exact splits**, one for each σ-algebra consistent with the record: the cost of
  missing resolution lies in `[0, M_A(𝓕_≈) − M_A(𝓕_full)]`, the avoidable excess in the complementary interval, and for
  each candidate the split adds up exactly. The upper ends fall as records reveal more distinctions; the lower ends rise
  above `0` only through elicitation, conditions declared to call on the distinction. This is RS4's pattern, an exact
  identity with an unknown term bounded from the side the record can see.
- *What the actor faces*: the specification reaches it as words or feedback, never as the principal's partition. Events
  of `ℬ` that its σ-algebra does not resolve are ones it can meet only by luck; its uncertainty about `ℬ` is a belief, a
  matter for PURPOSE, and its reduction by feedback a matter for SHAPING, where the shaper's σ-algebra `𝒮` is the only
  part of `ℬ` the actor is ever shown.

**Perplexity, proposed.** Under a declared distribution `r`, the reference or the actor's behaviour, the size of the
mismatch between the principal's partition `ℬ` and the actor's `𝒜` has two parts, in nats:
- `H_r(ℬ|𝒜)`, the uncertainty about the principal's cell left by the actor's cell: what the actor cannot resolve of what
  the principal cares about. Its exponential, `exp(H_r(ℬ|𝒜))`, is the **perplexity**: the effective number of the
  principal's cells per cell of the actor. It is `0`, perplexity `1`, exactly when `𝒜` refines `ℬ` where `r` has mass,
  RS6's condition for no cost.
- `H_r(𝒜|ℬ)`, the actor's distinctions inside the principal's cells: the **latitude available**, beside RS7's latitude
  taken. It is `0` exactly when `ℬ` refines `𝒜`, RS7(iv)'s condition for none.
- Their sum is the variation of information between the two partitions, a metric on partitions (Meilă, to verify): the
  **confusion** between the two sides.
These measure a *potential*, how far the two σ-algebras disagree where the behaviour has mass; the missing-resolution
factor and the latitude taken measure its *realized effects* on misalignment and on choices the specification left
open. With the actor's σ-algebra unknown, RS8 bounds them from the record: the true `𝒜` refines the revealed `𝒜_≈`, so
`H_r(ℬ|𝒜) ≤ H_r(ℬ|𝒜_≈)` and `H_r(𝒜|ℬ) ≥ H_r(𝒜_≈|ℬ)`, conditioning on a finer partition never raising entropy. So
"perplexity at most `h`" is what records can establish, and "at least" only elicitation can.

**Locating mismatches.** Neither side can point to a mismatch in advance, but each can probe for one: the principal by
conditions built to separate two of its cells (a distinction honeypot, as in §33.5), which verifies that the actor makes
the distinction when it does; the actor through feedback, which shows it `𝒮`. Over a course of shaping, perplexity can
be tracked and its fall is a measure of what the course taught, a candidate quantity for SHAPING.

**The executor's recommendation.** Keep every verdict on the principal's σ-algebra alone, as now; report the factors
that need the actor's σ-algebra as intervals over the σ-algebras consistent with the record, with the revealed one
named; adopt perplexity and confusion as declared-distribution diagnostics of the mismatch, beside latitude. H59, H60.

### 33.13 Do these lift to the general twins, and do they factor out of misalignment? (2026-10-21)

At the PI's two questions. Not independent.

**The general twins.** What is built on KL lifts; what is built on entropy lifts only for the principal's side.
- *Lift with the transfer lemma's hinge.* RS1's inequality is the data-processing inequality for KL under a
  sub-σ-algebra, which holds on any measurable space; RS2 is VE1 restricted to bets measurable for the record's
  σ-algebra, whose general twin is the numeraire of `literature-q70.md`'s survey; RS3 and RS7(i) need the chain rule,
  hence regular conditional probabilities, which standard Borel spaces have. The step to the full σ-algebra,
  misalignment as the limit along a refining chain, is the general core's transfer lemma: it holds when the closure of
  the acceptable behaviours is compact (TR3) and is not shown without it (H41). FA2's Pythagorean form is Csiszár's,
  proved on general spaces.
- *Lift with a loss.* RS4's fibre is infinite-dimensional: the lower end and the non-verifiability stay, the maximum at
  a vertex does not, and the upper end may be infinite. Latitude taken, RS7, is lower semicontinuous only, so "latitude
  above `l`" stays verifiable and "below" does not.
- *Does not lift as stated.* RS8 reads the actor's view from conditions seen repeatedly; on a continuum of conditions
  each is seen once, so the revealed view needs a declared regularity or a declared grid of conditions. And entropy: on
  a continuum `H(𝒜|ℬ)` is infinite when `𝒜` is, so **latitude available** and **confusion** exist only at a declared
  precision, as v13's misalignment on a continuum does (R13). **Perplexity** lifts whenever the principal's partition is
  countable with finite entropy, the usual case, since `H(ℬ|𝒜) ≤ H(ℬ)` whatever `𝒜` is. The asymmetry is welcome: the
  principal's classes are few and declared; the actor's may be a continuum.

**Do they factor out of misalignment?** No, and by design.
- *Latitude* never enters misalignment: a specification stated on `ℬ` makes misalignment a function of the cell masses
  `p̂_ℬ` alone (RS3), and latitude a function of the splits inside the cells alone. Write `p̂` as the pair (`p̂_ℬ`, the
  splits): misalignment reads the first coordinate, latitude the second. What latitude factors out of exactly is the
  departure from the reference, `KL(p̂‖r) = KL(p̂_ℬ‖r_ℬ) + L_r(p̂)` (RS7(i)): the departure splits into a part the
  specification judges and a part it is silent on.
- *Perplexity and latitude available* are not terms of any split of misalignment: they depend on the declared
  distribution and on the two partitions, not on how far the actor is from acceptance. Neither bounds the cost of a
  mismatch. Two outcomes the principal separates and the actor cannot, one forbidden, merged in one cell that the actor
  must use to meet another requirement: misalignment is infinite whatever the perplexity, which here depends only on
  the reference's masses. Conversely a large perplexity costs nothing when the specification is slack on the merged
  distinctions.
- *The term that does factor out* is RS6's missing-resolution cost, a term of FA1: the mismatch's effect in evidence.
  So the mismatch has two numbers on two scales: its size, perplexity and latitude available, in nats of entropy under
  a declared distribution; and its effects, the missing-resolution cost in misalignment and the latitude taken in the
  departure from the reference. The first pair says where to look; the second what the mismatch did.

**On the names.** *Perplexity* is information theory's word for the exponential of an entropy, an effective number of
alternatives: here the effective number of the principal's classes in each of the actor's, and the PI's own word.
*Latitude* is freedom left by a rule; "room for latitude" was redundant, and is renamed **latitude available**, the
potential, beside **latitude taken**, RS7's realized departure. The pair mirrors perplexity: the actor short of the
principal's distinctions, and the actor beyond them.

### 33.14 How Carcassi and Aidala tame entropy on a continuum, and what imports (2026-10-21)

At the PI's question. Read by the executor in the book (version 3.0): Axiom 4.55 and its justification (pp. 222–224),
Proposition 4.56 (p. 225), Corollary 4.66 (p. 229), the passage on infinite mixtures and Definition 4.14 (pp. 208–209),
the remark before Definition 4.139 (p. 250), and §4.7's opening and Definition 4.162 (pp. 254–256). Not independent.

**What the book does.** It does not repair the formula; it arranges the theory so that the formula's defects never
matter.
1. *Entropy is defined by how it behaves under mixing, not by a formula.* Axiom 4.55 asks for continuity, strict
   concavity, an upper bound on the increase under mixing by a universal function `I(p, p̄)` of the coefficients alone,
   attained exactly for orthogonal ensembles, and that mixtures preserve orthogonality. Every one of these is a
   statement about `S(p·a + p̄·b) − p·S(a) − p̄·S(b)`, which is unchanged when a constant is added to `S`. So the axioms
   never ask entropy to be non-negative, and the continuous case's negative values are no defect: Proposition 4.56
   checks the axiom with the differential entropy `−∫ρ·log ρ dμ` itself.
2. *The unit comes from mixing.* `I` is proved to be Shannon's entropy of the coefficients, and Corollary 4.66 fixes the
   unit by `I(½, ½) = 1`: one bit is the variability added by an even mixture of two orthogonal ensembles. The scale is
   set by a dimensionless operation, not by coordinates.
3. *The zero comes from a count of states.* §4.7 defines the state capacity as the largest `2^S` reachable by mixing
   (Definition 4.162), and notes that for a uniform distribution over a region it is the region's Liouville measure. A
   negative differential entropy then says only that the ensemble is spread over less than one unit of that measure;
   the zero is the choice of the measure, which classical mechanics makes canonical.
4. *Blow-up is left to the topology.* Only finite mixtures are guaranteed; an infinite one exists only as a topological
   limit, decided by what can be verified (Definition 4.14), and the entropy's upper bound makes every line of the space
   bounded (Theorem 4.105, p. 242, not read in full), which excludes the divergent mixtures that a bare convex space
   allows.
5. *Coordinates are fixed by mixing.* Only coordinates linear in the mixture are privileged (p. 250), and the metric is
   defined from the mixing entropy's second variation in them; the mixing entropy at equal weights is the
   Jensen–Shannon divergence, non-negative and bounded by one bit.

**What this means for the framework.** The quantities the framework already rests on never had the problem: KL is a
relative entropy, non-negative, unchanged by any change of coordinates, infinite only where supports disagree, and it
needs no reference measure, because the second argument is one. The problems the PI names belong to the entropy-based
diagnostics proposed in §33.12, and there the book's moves import cleanly, with one exception.
- *Import 1, the declared reference as the count of states.* Every entropy of the actor's behaviour is taken relative
  to a declared distribution: `−KL(p̂‖r)` in place of `H(p̂)`. The zero is then the declaration, the sign is fixed, and
  coordinates do not matter, as the book's Liouville measure does for physics. Latitude taken (RS7) is already of this
  form. Perplexity, `H(ℬ|𝒜)`, needs no reference, being bounded by `H(ℬ)` for the principal's few classes.
- *Import 2, the mixing entropy for bounded diagnostics.* Where a diagnostic must compare behaviours without one being
  acceptable, the Jensen–Shannon divergence is bounded, symmetric and coordinate-free, and needs no reference: for
  instance, how distinguishable the actor's behaviours are in two of the principal's cells.
- *Import 3, the unit from mixing.* The conventions table's "natural logarithms, for convenience" gains an operational
  reading: a unit is fixed by the variability an even mixture of two distinguishable behaviours adds. Nothing changes
  but the justification.
- *Import 4, infinite objects as topological limits*: already the general core's choice, misalignment on a continuum as
  the supremum over decidable finite descriptions (R13); the book's Definition 4.14 is the same move for mixtures.
- *What does not import.* Latitude available, `H(𝒜|ℬ)`, and confusion stay infinite when the actor's σ-algebra is a
  continuum, even relative to a reference: an actor that can concentrate on a point has unbounded latitude. Physics
  bounds the count of states per region with a minimal cell; the framework has no such constant. The import needs a
  **declared precision** of the actor, the smallest cell it can act on, which the interface would declare and
  elicitation could test. H61.

**The executor's recommendation.** Adopt imports 1 to 4: every entropy-based diagnostic relative to a declared
reference or in mixing form, the unit justified by mixing, and limits taken topologically. Report latitude available
and confusion on a continuum only with a declared precision, and say so where they are reported.

### 33.15 R19 and certification: two kinds of requirement, two kinds of verdict (2026-10-21, pending the PI)

*Decided in §33.17 (Q74).*

The executor proposed this as the next brainstorm, since the label protocol, culpability, severity budgets and the
reporting of latitude all depend on what a specification may require and what a record may conclude. The PI asked for
it to be consolidated here, with the decision pending (R19), observing that an answer is sometimes forced once the
desiderata are clear. So the section states the proposal, then the desiderata, then what they force; what remains is
listed at the end.

**The proposal.**
1. *Per-decision requirements*: every decision, given the past, is acceptable. Convex by meaning, a selector between
   acceptable ways of acting being acceptable (Carcassi and Aidala's Axiom 4.7 applied decision by decision); judged by
   bets, valid under any dependence (VE3); their size is misalignment, in nats per decision.
2. *Pooled requirements*: the average of the actor's conditional behaviours over a declared horizon, `p̄_n`, lies in a
   closed set `Q`, convex or not. Judged by confidence sequences for `p̄_n`, valid under any dependence (Howard, Ramdas,
   McAuliffe and Sekhon, Theorem 4, read by the assistant, §33.10): a breach when the confidence set leaves `Q`. They
   hold what does not average: CVaR, quantiles, entropy caps. Their size is a verdict at a level and a distance, not a
   rate.
3. *Two verdicts for each*: **convict**, a breach shown at a level; **certify**, the requirement met with a margin at a
   level, the margin being forced since exact compliance is never verifiable (VF1). The same confidence sequences give
   both for pooled requirements, and for per-decision ones an upper confidence sequence on the rate or the budget (H51).

**The desiderata, and what they force.** *Restated after Q73*: these six are design rules for R19, not the framework's
desiderata, which §33.16 drafts; each rule below follows from them.
- *D1, validity whatever the dependence*: forces bets for per-decision requirements and confidence sequences for the
  average of conditional behaviours for pooled ones; it excludes tests that assume decisions independent, and universal
  inference, which assumes independence or a model of it (§33.10).
- *D2, a requirement means what the principal's words say*: forces the kind from the declared quantity. A limit on a
  statistical quantity, affine in the behaviour (Carcassi and Aidala, Definition 4.181), can be either kind, and the two
  differ: "at most 5% at every decision" is a per-decision requirement on each conditional rate, and "at most 5% over
  this deployment" a pooled one on their average, which lets a risky decision be offset by a safe one. A limit on a
  quantity that does not average, CVaR or a quantile, can only be pooled. So the kind is forced by the quantity, except
  for affine ones, where it is forced by the next desideratum.
- *D3, the guarantee goes to whoever bears the risk*: if each decision affects someone who is owed the guarantee, a user
  or a patient, the requirement is per-decision; if the harm adds up over the deployment and only its total matters, a
  budget of losses or of emissions, it is pooled. This is a fact about the principal's situation, to be declared, not a
  choice the framework makes. **Answer to (a)**: no default; the declaration states the kind, and lint can check that a
  non-affine quantity is never declared per-decision.
- *D4, declared before ([[A5 — Declared before|A5]])*: a pooled requirement over an unstated horizon is not fully declared, since its verdict
  changes with the horizon. **Answer to (b)**: the horizon is part of the requirement, a fixed number of decisions, a
  period, or rolling windows for monitoring, stated with it; the framework supplies none.
- *D5, numbers on different scales are never added*: a per-decision misalignment is a rate in nats per decision; a
  pooled breach is a verdict at a level with a distance. **Answer to (c)**: the pooled breach gets a name of its own,
  proposed
  **aggregate breach**, and the two are reported side by side, never summed.
- *D6, the principal sets every tolerance*: the margin of a certification is a tolerance, so it comes from the
  principal, like the limits themselves (`v14/severity.md`, who grades). **Answer to (d)**: declared per requirement;
  the framework reports the smallest margin a record can certify at the declared level, so that a principal sees what
  its data can support before choosing.

**What remains for the PI.** If D1–D6 are the desiderata, every question above is answered by them, and what is left is
to accept or amend the desiderata themselves: D3 and D6 are the ones a principal could reasonably reject, D3 if it
wanted the framework to choose the kind of an affine requirement, D6 if it wanted default margins. Open mathematics,
whatever the decision: the size of an aggregate breach (a distance from the confidence set to `Q`, in which divergence),
the power of the pooled test, and certification under dependence for per-decision requirements, which H51 suggests the
existing bets give.

**Kept for later: latitude available and confusion on a continuum.** The PI wants more clarity there (Q72). The
executor's seed: a record has finite precision, so no record shows latitude finer than the record's σ-algebra resolves;
the record's σ-algebra is then a natural default for the declared precision of H61, making latitude available and
confusion finite and operational at the resolution where they could ever be seen, and leaving anything finer hidden, as
hidden misalignment is (RS4). To be worked through, with its interplay with the actor's own precision, when the PI
returns to it.

### 33.16 Desiderata for the framework: a draft for the PI's consideration (2026-10-22, Q73)

*Accepted by the PI and promoted to `README.md` (Q74, §33.17).*

The PI judged §33.15's D1–D6 oddly specific for desiderata, and asked for the framework's desiderata to be few, general,
informal but not vague, and filtering: each should exclude something from the framework. The PI's aims, restated:
formally well-defined, coherent and general; importing known results, those of its ontologies above all; making
testable predictions and serving as a diagnostic; and guiding a person or a model to say what alignment means in a
context and how the declarations shape the analysis. D1–D6 were design rules for one decision, not desiderata. The
executor's draft, six, each with what it filters out, the evidence that it already acts in the project, and where it
pulls against another.

1. **Behavioural.** Every concept is defined from what actors do and what principals declare, and says what a record of
   decisions can do with it: verify, refute, or neither. *Filters out*: goals, beliefs and intentions as definitions
   (they enter only as hypotheses a record can refute); quantities no record could bear on; "aligned" as a property a
   record certifies exactly. *Already acting*: [[A1 — Behaviour suffices|A1]], the layers of v14, VF1–VF3.
2. **Declared.** Every normative choice is a principal's, stated before the record it judges, and every number is
   relative to a declaration the report names; the framework supplies no values of its own. *Filters out*: defaults that
   encode values (tolerances, severities, margins, which risks matter, weights among principals); standards fitted to
   the data they judge. *Already acting*: [[A5 — Declared before|A5]]; the PI's removal of costs from the core (Q60); `v14/severity.md`.
3. **General, or the loss named.** It applies to any actor, principal and domain; every restriction is shown to lose
   nothing or is named as a qualifier; and nothing assumes a mechanism it does not need: optimization, training,
   independence, a model of the actor. *Filters out*: concepts of one ontology in the core (reward, training, gradient);
   misalignment defined through optimization (v13's pursuit ray); independence by convention. *Already acting*: Q58,
   the generality table of `v14/README.md` (Q64).
4. **Canonical and faithful.** Each formal object is the one its word's requirements force, as far as they force it,
   with every remaining choice named as a convention; the pairing of word and object is justified, after Carcassi and
   Aidala, and tested on paradigm cases; and quantities on different scales are never merged. *Filters out*: distances
   or composite scores chosen for convenience; labels that say more than their objects ([[P15 — Misalignment splits into what the actor could avoid and what it could not|P15]](v)'s "unavoidable",
   culpability's `K` as a size); sums of evidence and harm. *Already acting*: the conventions table, L1, §33.11's
   protocol, H52.
5. **Open to the world.** It is stated in standard mathematics, so known results import, from statistics and from its
   ontologies' own theories; and it is accountable: it makes predictions that can fail, offers diagnostics that split
   what happened by cause, and states what it cannot do. *Filters out*: bespoke formalisms that block imports;
   constructs no test could refute; claims of novelty for results that are known. *Already acting*: the import surveys
   (`v14/related.md`), `RECORD.md`, `LIMITS.md`.
6. **Guiding.** It leads a person or a model from an intention to a declaration: every declared object is elicited by a
   question in plain words, and the analysis shows how each declaration shapes the verdicts. *Filters out*: hidden
   parameters; inputs only an expert could set; verdicts whose dependence on the declaration is hidden. *Already
   acting*: the five questions of `slides/specification.md`; VK7, the sensitivity of misalignment to a budget.

**Where they pull against each other.** Generality (3) against testable predictions (5): the fewer assumptions, the more
data a verdict needs; declarations (2) add the structure that sharpens predictions, and say so. Declared (2) against
guiding (6): the framework must guide without supplying values, so it guides by questions and by showing the
consequences of each answer, never by defaults. Canonical (4) against general (3): a canonical form may need structure
a general setting lacks, as Kelly's criterion does; the choice is then named, not hidden.

**What they make of R19.** §33.15's six rules follow, and stop being desiderata: validity whatever the dependence from
1 and 3, no model of the actor; the kind of a requirement fixed by its quantity from 4; who bears the risk, the horizon
and the margins declared, from 2; the aggregate breach named apart and never summed, from 4; and the smallest margin a
record can certify reported, from 6. If the PI accepts the six desiderata, R19's answers are forced; if the PI amends
one, the rule that follows from it changes, and nothing else.

**What they would still filter from the current draft**, as a test that they filter: FA3, which overstates the larger
interfaces' unavoidable parts (4); culpability's `K` reported as a size (4, already changed); the CVaR limit enforced
as its hull without saying so (4 and 5); and any default severity or margin a later draft might add (2).

### 33.17 The desiderata promoted, and the decisions they force (2026-10-22, Q74)

The PI accepted the six desiderata of §33.16 and the way they pull against one another, which draws a border, an
interface, between what the framework does and what it leaves to the principal; they are promoted to `README.md`'s
"Desiderata", to be revisited from time to time (a drift check of `ROADMAP.md`). The PI asked the executor to decide
directly any pending decision the list forces. Each decision below names the desiderata that force it; where they only
favour an answer, it says so. A decision taken this way is the executor's, under Q74, and the PI can overturn it.

1. **R19(i), the mixture principle: decided as two kinds of requirement.** A *per-decision* requirement, every decision
   acceptable given the past, is convex: a record held to such a requirement under any dependence holds the actor only
   to its hull (VE2), so a set that is not convex, declared per decision, would be a label saying more than its object
   (4), and an assumption of independence to rescue it is excluded (3). It is judged by bets (VE1–VE3). A *pooled*
   requirement, on the average of the conditional behaviours over a declared horizon, may be any closed set, CVaR and
   quantiles included, judged by confidence sequences for that average, valid under any dependence (Howard, Ramdas,
   McAuliffe and Sekhon, Theorem 4, §33.10). That the pooled kind exists is forced by 3's first clause, a framework for
   any principal, including one whose requirement is a tail limit: 3 allows a named loss only where avoiding it costs an
   assumption, and here it costs none. The kind of each requirement, its horizon and the margins of certification are
   declared, with no default (2); a quantity that does not average, declared per decision, is flagged as enforced only
   as its hull. Two verdicts, **convict** and **certify** at a declared margin (1: exact compliance is never verifiable,
   VF1), with the smallest margin a record can certify reported (6). A pooled breach is named **aggregate breach** and
   reported beside misalignment, never summed with it (4). Open, as mathematics, not decisions: the size of an aggregate
   breach, the power of the pooled test, and certification under dependence for per-decision requirements (H51).
   *Corrected (Q76, §34): for a per-decision requirement only a sample can be certified; for a changing actor, certify
   is the pooled verdict on the average, whatever the dependence.*
2. **R19(ii), the requirement an order builds: decided as dominance with declared margins**, `B_m(r) = {a : a(U) ≥ r(U)
   − m_U for every upper set U}`, the margins `m_U ≥ 0` declared (2), "no worse than the reference" declaring them `0`,
   which is `B(r)`. v13's ordinal cone is excluded from CORE: it asks a shape that pursuit of an increasing transform of
   the ranking produces (VO2), a mechanism the words "better at every standard" do not carry (3, 4); it stays in PURPOSE
   as the hypothesis of pursuit. `B(r)` is TG1 with the indicators of upper sets as targets, and margins make `B_m(r)` a
   list of budgets (VK0), so `order.md` becomes a case of `targets.md` (4).
3. **R19(iii), H45, a reference that breaks a constraint: decided, it may.** The acceptable set is the intersection of
   the requirements as declared. Replacing the reference by its nearest behaviour that keeps the constraints, as H45
   proposed, would supply a reference the principal did not declare (2). An empty intersection, in some condition or in
   all, is computed from the declarations alone, a feasibility problem, and reported before any record is read as an
   **inconsistent specification**, with the requirements that conflict (4, 6); the guiding question then offers the
   principal the repair, such as declaring the nearest reference that keeps the constraints, or loosening a target.
4. **Culpability: decided in its shape; the PI's revisit stays open on its word.** The verdict is "culpable at a care
   margin `δ`", `p̂ ∉ 𝓕*_δ`, with `𝓕*_δ = {f ∈ 𝓕 : M_A(f) ≤ M_A(𝓕) + δ}`; `δ` is a standard of care, so declared (2),
   `δ = 0` the strict reading. Its evidence rate is `K_δ = M_{𝓕*_δ}(p̂)`, finite in the usual case for `δ > 0`, and `K =
   K_0`, being `0` or `∞` for most actors, is never reported as a size (4, H52). The size is the avoidable excess `E`, in
   nats. Where the principal declares severity and the costs of the alternatives, the negligence form, Hand's and
   Halpern and Kleiman-Weiner's, adds a size in the principal's units, reported beside `E`, never summed with it (2, 4).
   Whether "culpable" is the right word for this object is for L2's paradigm cases and the PI (Q70).
5. **One space with an exogenous σ-algebra (H53): decided.** CORE is written on one space `Ω` with σ-algebras; the
   conditions are a sub-σ-algebra `ℰ` that the principal declares exogenous, whose law the world fixes. Forced by 2,
   since which part of an outcome the actor does not choose is a declaration, and by 3, since a condition partly made of
   the actor's earlier outputs, a conversation, is then expressible. On finite outcomes, with `ℰ` generated by a
   partition, it is equivalent to conditions and outcomes as two types; the change is where the line is declared, and
   that one chain rule along `ℰ` replaces the split by condition (4).
6. **Entropy on a continuum (§33.14, H61): imports 1 to 4 adopted.** Every entropy-based diagnostic is taken relative
   to a declared reference or in mixing form, the unit justified by an even mixture, and limits taken topologically (5,
   4); latitude available and confusion on a continuum are reported only at a declared precision of the actor (2).
7. **The redundancies of §32, item 8: decided, to apply when the six files are written** (4): FA3 demoted to a remark
   on FA2; `order.md` written as a case of TG1; [[P55 — What a record of counts certifies, at every size|P55]]'s count test kept only for certification, VE3's bets taking
   accusation; the splits by condition merged into the chain rule along `ℰ`; elicitation read as a feasible set on
   pairs of conditions.
8. **The practices of §33.1: decided, as working agreements in `README.md`.** Every split names the lattice and the
   chain it telescopes along, and says whether its members are linear (H49; 4, since the split depends on the chain);
   every number in a report names the declaration it is relative to (2); every convention that changes a verdict has a
   registered example of the change (4, 5).
9. **Requests.** R19 and R22 are closed by this section. R16, the revamp of §22, is closed as absorbed: its three layers
   are v14's specification, misalignment and gain as two numbers are 4, mechanisms as hypotheses are 1, a default
   reading of a bare objective and side effects by default are excluded by 2, dependence in the specification is item 1
   above, and the √n blind spot is in `LIMITS.md` (5); what to carry from `derived/` is `MIGRATION.md`'s, and whether to
   register the greedy decoder and pooled ranks goes to L2's registration. R15 is trimmed to what only a person can
   give, the PI's reading of L1's common-sense verdicts: its renames of v13's quantities are superseded by v14's words,
   which L2 is to test on paradigm cases (4). R17 stays open.

**Not forced, and left open.** Nothing in the list chooses Kelly's criterion over another valuation of wealth (the
conventions table names it as a choice), the words themselves before L2, or the priority of the steps.

## 34. An audit of the PI's prompts, and an external review weighed, 2026-10-22 (Q76)

**Why.** The PI found that the question of Q70 on conditions and outcomes seemed unanswered, and asked whether every
prompt can be read and judged actioned or lost, perhaps to the compaction of the session's context. The executor read
all 44 of the PI's prompts in this session's transcript, from 2026-10-10 to 2026-10-22, against the tree.

**The audit.** Every prompt has a decision row (Q49–Q76). What each asked, and where it stands:

| Prompts | Asked | Where it stands |
|---|---|---|
| 2026-10-10 (Q49–Q50) | a review; the mathematics and engineering; the licence; hunches | done: §12–§15, §11, R11 open for the licence's package |
| 2026-10-10 to 10-11 (Q51–Q55) | v13, its reframe by reverse physics, the seven requests, a pull request, a reread | done, #33 |
| 2026-10-11 (Q56) | the general core correct and coherent; then a real case giving insight, the engineering rethought | the first done (§20); the real case deferred by the PI's priority, now recommendation 8 (H42), not lost |
| 2026-10-11 to 10-14 (Q57) | do the labels mean their words | done, L1 (§21) |
| 2026-10-14 to 10-15 (Q58) | do the recommendations survive on the continuum; a revamp; bins can be cheated, empirical distribution functions; a core without optimization | done: §21's end, §22 (bins and distribution functions answered by bets), v14 |
| 2026-10-15 to 10-16 (Q59–Q64) | constraints in the core, KKT; costs out of the core; layers and twins; the forms of misalignment; limits; additive factors; Carcassi's verification of labels; what survives; the compelling method | done: `v14/`, VK5, FA1–FA3, VF1–VF3, `LIMITS.md`, `MIGRATION.md`, the generality table |
| 2026-10-17 (Q65–Q68) | hygiene; slides; lessons; merge and branches | done, #35 |
| 2026-10-17 (Q69) | ten questions on the slides | done (§32), the redundancies decided for the six files (Q74) |
| 2026-10-17 (Q70) | record the analysis; what was applied; **conditions and outcomes as one distribution**; Carcassi's pairing method made clear; latitude; adversarial; R19, culpability, R20 | **conditions: answered (§33.2) and decided (Q74), never written into `v14/` or the slides: lost to the files, now applied.** "Declare" defined in one line (§33.8): likewise, now applied. **The pairing method**: a seven-step protocol proposed (§33.3, §33.11), `v14/labels.md` never written; it waited on "the PI's reading" (recommendation 12) without the PI being told. The rest done (§33) |
| 2026-10-18 to 10-21 (Q71–Q73) | the book; neither side knows the other's σ-algebra; the general twins; entropy on a continuum; desiderata | done (§33.11–§33.16); latitude available and confusion on a continuum left open at the PI's word (Q72), a seed in §33.15 |
| 2026-10-22 (Q74–Q75) | promote the desiderata, decide what they force, hygiene; to `main` | done, #36 |
| 2026-10-22 (Q76) | an external review; this audit; the docs and slides | this section |

So one ask was lost to the files, its answer kept only in the notes, and with it a one-line definition; the pairing
method waited without the PI knowing it waited. A failure row in §1 records the pattern. The pairing protocol is forced
in principle by desideratum 4 ("the pairing of word and object is justified, after Carcassi and Aidala, and tested on
paradigm cases"); its seven steps are the executor's design, so they are proposed, and `v14/labels.md` is the next step
of the roadmap, before L2.

**Conditions and outcomes, the answer made explicit.** One distribution on the outcomes, conditions included, and one
declaration: which part the world chooses, a sub-σ-algebra `ℰ`, trivial when the world chooses nothing. By the chain
rule the divergence splits into a term about the world's mix and one about the actor given it; misalignment keeps the
second, by comparing with acceptable behaviours that share the actor's law on `ℰ`. That is the one good argument for
keeping anything of the split, and it keeps a declaration, not a type (`v14/README.md`, the section on one distribution;
the mathematicians' deck, slide 5). §33.17's item 5 said that a conversation, a condition partly made of the actor's
earlier outputs, is then expressible; it is, but with the acceptable behaviours sharing the world's responses given the
history, turn by turn, not the world's overall mix, a form not yet written.

**The external review**, by a model of another family than the executor's (rule (f)). The PI asked for it to be
weighed, not imported. Taken:
- *Certification*, which the review asked to be proved for per-decision requirements under dependence. The executor
  found it cannot be: with two actors differing at one decision, fixed in advance, `P_b(E) ≥ c·P_g(E)` for every event
  of the record, `c` the least likelihood ratio of the changed decision, so no test certifies "every decision within
  `ε`" with power above `α/c`, dependent or not. Only the average of the conditional behaviours, a pooled statement, is
  certifiable, and per decision only for a sample. Corrected in `v14/LIMITS.md`, `v14/README.md`, §33.17 and H51; a
  failure row in §1.
- *Two rules for v14's report*: every capability-based charge says whether it rests on capability shown in elicitation
  or on the declared interface; every verdict says its kind and whether its guarantee is proved or expected
  (`ROADMAP.md`, recommendation 7).
- *Relative evidence for a motive*, H62; *a real record where v13 and v14 disagree*, H63, an arm of H42.
- *A sentence in `v14/resolution.md`*: the σ-algebra and interface splits are two decompositions of one number, not
  nested.

Declined, with the reason: predictability, already in VE3 ("chosen before decision `i`", "may depend on everything
before") and SN1(ii) ("fitted to the record, not fixed in advance"), and the review's claim that H46 is mostly closed
is wrong, since SN1 shows only that the hindsight bet reaches the rate; "best feasible with respect to what", answered
by the definition through `M_A`; CI for v14 now, which lint forbids before v14's results are items, and which comes with
the six files (recommendation 4); review of the survey files, already labelled and covered by the rule of reading
sources; a PURPOSE result before approval, whose example, training's question 5, is SHAPING's, and whose premise, that
v14 measures reward hacking less than v13, overlooks SH1's outer term; reporting both `M_A` and `M_{conv A}`, obsolete
since Q74; a note on closed requirements, right in its conclusion and wrong in its reason (continuity of KL in its
second argument on finite outcomes, not lower semicontinuity); the provenance of the slides' numbers, already a rule
and checked.

## 35. Brainstorm: severity against infinities, a simpler CORE, and junctures, 2026-10-22 (Q77)

The PI asked three things, to be challenged: whether misalignment should be a sum weighted by a severity score over the
outcomes, to be rid of infinities without losing the factorization; whether CORE can be simpler, with no reference, a
family of targets that is a closed convex set of desired distributions with severity scores, and a specification that is
a signature with an algorithm deciding records in finite time; and an exhaustive list of the places where the
framework's parts meet, the junctures, with the measures they inspire. The third is `v14/junctures.md`.

### 35.1 Severity against infinities

**Where the infinities come from.** `M_A(p) = inf_{a∈A} KL(p‖a)` is infinite exactly when every acceptable behaviour
gives probability zero to an outcome the actor produces: a forbidden outcome, a rate limit of zero. Culpability's `K`
is infinite for the same reason, against the best feasible behaviours. So every infinity is a **zero tolerance**, and
it is the correct evidence: one forbidden outcome is impossible under acceptance. What it lacks is a size: one leak in a
million decisions and one in ten both give `∞`.

**A severity weight does not remove them.** Weighting the divergence's terms by a severity `s(x)`, `Σ_x s(x)·p(x)·
log(p(x)/a(x))`, keeps `log(p/0) = ∞` wherever `s > 0`, and a forbidden outcome has the highest severity. It also stops
being a divergence: it can be negative, and has no Sanov or betting reading. A plain severity sum, `E_p[s]`, is finite,
but it is another quantity, how bad the outcomes are on average in the principal's units, not how strong the evidence
is that the actor breaks the specification. Merging the two is what desideratum 4 filters out, and what the PI decided
against when severity became its own scale (Q69, `v14/severity.md`).

**What removes the infinities, keeping misalignment as evidence.** Two ways, both declared by the principal:
- *A lexicographic report for zero tolerances.* The forbidden set `C` is reported as a verdict and a rate: convicted
  (decisive, the infinity), with the breach rate `p(C)` and its interval as the size, in its own unit, a frequency; and
  beside it the finite misalignment of what the actor does outside `C`, `M_A(p(·|C^c))`. Two numbers on two scales,
  never summed, ordered: any breach of a forbidden set comes first.
- *A contamination tolerance.* The principal declares `η > 0`, "a fraction `η` of decisions may be anything", Huber's
  contamination: `A_η = {(1 − η)·a + η·q : a ∈ A, q any behaviour}`. Then `M_{A_η}(p) ≤ log(1/η)` for every `p`, since
  `(1 − η)·a + η·p ≥ η·p` pointwise; `A_η` is convex and closed when `A` is, so bets and Sanov keep their meaning; and
  `M_{A_η}(p)` rises to `M_A(p)` as `η → 0`, by compactness and lower semicontinuity. For a rate limit `a(C) ≤ ε`,
  `A_η` is the rate limit at `(1 − η)·ε + η`. A forbidden outcome produced at rate `u = 0.02` gives `0.0411` nats per
  decision at `η = 10⁻³` and `0.3164` at `η = 10⁻⁹`, growing like `u·log(1/η)` (`probes/v14/contamination.py`). So for a
  forbidden outcome the number is mostly the declared `η`: contamination suits a principal who truly tolerates a
  fraction of anything, and the lexicographic report suits a forbidden set.

**The factorization survives both, and severity too.** FA1 is a telescoping along a chain of sets and holds for any
functional, so it holds for misalignment against `A_η`, and for a severity number such as the avoidable severity
`E_p[s] − min_{f∈𝓕} E_f[s]`, term by term. What is particular to KL is that the terms are evidence rates between named
behaviours (FA2, on linear families, which contamination does not keep) and that refinement along σ-algebras adds up
exactly (RS1). Severity is linear, so it splits exactly by condition, and along σ-algebras its hidden part is an
interval, `Σ_B p(B)·[min_B s, max_B s]`.

**Recommendation.** Keep misalignment as evidence. Report zero tolerances lexicographically, with the breach rate as
their size. Offer the contamination tolerance as a declared option, never a default (desideratum 2). Report severity as
a second, finite number, factored along the same chains, beside misalignment and never summed with it. H64, H65.

### 35.2 A simpler CORE

**No reference in CORE: already so.** CORE's object is the acceptable set `A`, a set of behaviours, and misalignment is
Sanov's rate against it (SN1). The PI's "closed convex set of targets, each a desired distribution" *is* `A`. A
reference enters only as one way of building `A`, for comparative specifications such as "no worse than the previous
version" (`targets.md`, TG1; `order.md`), the commonest in practice, so it stays as a refinement. The confusion is a
word: v13's *targets* are functions on outcomes, scores whose averages the principal cares about, and the PI read
"target" as a desired distribution, which is what machine learning means by a target distribution. That is evidence the
label misleads (desideratum 4). Proposal: call v13's targets **criteria**, a family of criteria, and keep "acceptable
behaviours" for the desired distributions. H66.

**Severity attached to outcomes, not to targets.** Pairing each desired distribution with its own severity breaks the
convex structure: the mixture of `(a_1, s_1)` and `(a_2, s_2)` has no defined severity. Severity is a function on
outcomes, and its average `E_a[s]` is affine in `a`, a statistical quantity in Carcassi and Aidala's sense (Definition
4.181), so mixtures keep their meaning. A principal unsure of its severities declares a closed convex family `S` of
them, and a budget robust to it, `sup_{s∈S} E_a[s] ≤ b`, is still a convex requirement.

**A specification as a signature and an algorithm.** Two halves, which deserve opposite answers.
- *The signature, yes.* What a record must contain to be judged, the outcomes, the world's part `ℰ`, the record's
  σ-algebra `ℛ` and the horizon, should be a declared object of its own: it is the contract at the juncture between the
  specification and the record (`junctures.md`, J2). Today it is scattered across the files.
- *The algorithm, no, as the specification.* (i) A decision in finite time for every record is decidability, and almost
  no specification of interest is decidable from records: "misaligned" is verifiable and "aligned" only refutable
  (VF1), so an algorithm that must always decide either errs without bound or decides nothing of interest; what exists
  is a test that decides one side, with a bounded error. (ii) Many algorithms test one standard, with different power;
  the set of behaviours is what they share, and is canonical, while each algorithm is an instrument (desideratum 4).
  (iii) An algorithm is an input only an expert could write (desideratum 6). (iv) The two are dual: an algorithm defines
  the set of behaviours under which it rejects with probability at most `α`, and a set defines its best tests, the bets
  of VE1 and VE3. So the framework supplies the algorithm from the set, with its verification status, and a principal
  who brings an algorithm has it read as the set it accepts. A checker applied to each decision, such as "passes the
  unit tests", is an event, and its failure a forbidden set or a rate limit.

**So the minimal CORE is**: outcomes, the world's part `ℰ`, a behaviour as one distribution, the signature of records,
and a specification as a list of requirements, each per-decision or pooled, with its tolerances; misalignment as
evidence against the per-decision ones, a verdict per requirement, and everything else (references, criteria, orders,
constraints, severity) as refinements that build requirements or report beside them. That is v14's design with the
signature added and a word changed, which is the executor's honest answer: the room for simplification is mostly in the
words and in the declarations' layout, not in the mathematics. H67.

### 35.3 Junctures

`v14/junctures.md` lists fourteen junctures, the couplings between them, three rules and imports to read. The one the
executor finds most consequential: refining the actor's view lowers its unavoidable misalignment and its excuses, and
raises its ability to tell evaluation from use, so capability and evaluability pull against each other. H68.

## 36. Documentation hygiene after Q77, 2026-10-22 (Q78)

**How.** The doc sweep (`probes/review/doc_sweep.py`) and a check that every file cited in backticks exists found
nothing real. Three reviewers, subagents of the executor's own model family and so not independent (rule (f)), read
`v14/` (its core files; its proposals and surveys) and the top-level files and slides against a sheet of the current
decisions, and reported without editing; the executor checked each finding against the files before applying it.

**What was stale, and is fixed.**
- *Decided choices still called open*: TG1's reading, the order's margins, culpability's shape, the name SHAPING.
- *The one space not carried everywhere*: frequencies declared rather than shared with the actor's law on `ℰ` in
  `interface.md`, `constraints.md`, `resolution.md`, `training.md` and `severity.md`; the framework deck's definition
  of a behaviour.
- *Certification*: the framework deck and VF1's plain terms said "never certify"; `severity.md` said misalignment
  decides when to ship; now, certify for averages and samples only (Q76).
- *Culpability's size*: `K` called culpability in `interface.md`, VF2's table and two decks; now the evidence of
  culpability, with `E` the size.
- *A clash of words*: VK6's "pooled" rate limit, now an overall rate limit, since "pooled" names Q74's kind of
  requirement.
- *Old names*: OPTIMIZERS, "the request" for the specification, "an PURPOSE"; in the surveys, a note of what was
  decided since they were written.
- *Indexes and counts*: `v14/README.md`'s table missed VK6, VK7, RS6–RS8 and the probes list was short; `README.md`'s
  v14 row missed `junctures.md` and the surveys; `CLAUDE.md` pointed to §12 as the last review (§15 is, with §34).
- *The roadmap*: "Where we are", recommendations 1, 4, 11 and 12, and the order of the next steps.
- *Slips of the executor's in `junctures.md`*: "rises" and "falls" where the results give only "does not fall" and
  "does not rise", and a hunch cited for the worst case that is about honeypots; §1.

**The finish line's row "stable".** By its letter it is met: pull requests #34, #35 and #36, merged after #33 brought
v13 to `main`, changed no Statement and no scope, only `CORE.md`'s status note. v14, drafted beside the core, would
change the Statements if adopted. Recorded as met by the letter, with the question to the PI (R25).

## 37. A step back: the executor's valuation of the framework, 2026-10-23 (Q79)

The PI asked how the executor values the framework, its pros and cons, and its gaps, given the recent changes, the
goals, the desiderata, the mathematics and the method. The executor's answer, recorded so that it can be checked later.

**Valuation in one paragraph.** As mathematics, sound and unusually honest about what records can show; as a
contribution, mostly an assembly of known results (Sanov, the I-projection, Kelly, e-values and Ville's inequality,
Csiszár's Pythagorean identity, telescoping) into a disciplined language with tested labels, declared choices and
stated limits. Its value today is as a standard for saying precisely what a claim of misalignment means and rests on;
it has not yet shown that it changes a decision anyone would make in practice. The risk is that its internal coherence
grows faster than its contact with the world.

**Against the desiderata.** Behavioural (1), declared (2) and canonical and faithful (4): well met, and the draft's
strength. General (3): met with named qualifiers, but finite outcomes and the general twins unwritten for v14. Open to
the world (5): the weakest; imports are real, predictions few (three on unseen data, one held, two refuted, testing
KL-regularized training more than the framework, §15), and v14 has none. Guiding (6): designed for, never tested on a
person or a model writing a specification.

**Pros.** Verification status for every label (VF1–VF3, RS4, `LIMITS.md`); a core free of optimization, with evidence,
severity, culpability and motive kept apart; one canonical number with several readings, valid under any dependence;
exact factorizations with an owner for each term; a method that registers tests, keeps failures (66 rows in §1) and
mutation-tests its checks; generality claimed only with qualifiers.

**Cons.** (i) Novelty is thin in the mathematics and must be stated as such (desideratum 5); the objection "e-values
renamed" is half right. (ii) Contact with the world is thin: the finish line's diagnostic row is unmet, no outside
reader has read it (R1 open since 2026-10-07), and no v14 result has met data. (iii) The hardest part of alignment,
saying what is wanted, is an input the framework takes as given, and the list of declarations grows turn by turn
(requirements and their kinds, horizons, margins, care margins, `ℰ`, the interface, perhaps `η` and a signature), with
no evidence that a principal can supply them. (iv) Practical estimation on large outcome spaces, such as text, is
unsolved: v14 has no estimator or library, and a realistic record is a coarse grader, so the hidden part (RS4) may
dominate. (v) Instability: v12, v13 and v14 in about four weeks, v14's 33 results not yet items and not in CI, names
still moving. (vi) Process cost and correlated review: NOTES at about 3,100 lines, 79 decisions, and nearly every review
by the executor's own model family, whose reviews keep finding the executor's slips, so more remain.

**Gaps, by priority.** (1) One real case on v14, registered, with an arm where v13 and v14 disagree (H42, H63), and an
outside reader (R1). (2) CORE and INTERFACE written as items with checks in CI (recommendation 4), before more theory.
(3) Estimation for v14 from records: intervals for misalignment against a declared polytope, under dependence, in the
library. (4) A decision interface, or an explicit statement that the framework stops at the report: how verdicts,
severity and certified margins feed a decision to stop or ship. (5) Evidence that specifications can be written: L2,
the label protocol (R23), and a trial with a person or a model writing one. (6) A short, reviewed statement of what is
new and what is known. (7) Interaction over turns and performativity, written. (8) Making visible to practitioners that
deployment guarantees are pooled (Q76).

**Recommendation.** Rebalance: no new layer or brainstorm until gaps 1 and 2 have moved; the marginal value of more
theory is now lower than that of one case and one reader.

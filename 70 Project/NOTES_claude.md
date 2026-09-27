---
id: "NOTES_claude"
type: "working-notes"
source_file: "NOTES_claude.md"
updated: "2026-09-26"
---
# NOTES — for me only

> v5, written at v6.4. Replaces the old executor notes (v4.x). Nobody else is the audience. Blunt on purpose.
> Read §0 and §5 at the start of every turn. Update §3 when a hunch dies or is born. Never promote anything
> from this file into A/B/C without a proof or a `verify.py` block.

---

## 0. Anchor

**The goal, in one line.** A *standard* formal framework for a theory of alignment: solid, substrate-free,
easy to import theorems into. It must **predict, diagnose, and show limits and connections**. Novelty is
irrelevant. Not the North Star: related, out of scope here.

**What "done" looks like for this thread.** Someone outside the project takes a real alignment case from any
substrate, runs it through the framework, and gets:
- a diagnosis: where the failure sits, and how big it is, in a unit that means something;
- a prediction they can check;
- the imported theorems that apply.

Until that works on real cases, the framework is a calculus, not a standard.

**Current work:** v7.8. The R7 series has restated the core as the KL projection onto a declared intended set
(R7-9, v7.6), with target sets (R7-7), caps (R7-6a), floors (R7-6b) and a resolution (R7-10) as declarations. §4b is
confirmed and the core steps are closed: T7 case 1 is done in three designs ([[T7 case 1 index]]); next is T7 case 2 (defaults), the PI's choice. R7-5 closed as a clean
negative; T3 too. T3b is deferred by the PI. The
v7.3.3 review's recommendations are [[ROADMAP]] §5; its other observations are §7 below. A fresh session starts at
[[HANDOVER]].

**Vault habits.**
- Shell heredocs that contain Markdown must be quoted (`<< 'EOF'`). An unquoted one ran the backticks as
  commands and silently blanked text in a note (R7-2; caught by reading the note back).
- Edit notes, then `sync`, then `lint` (0 errors).
- Never hand-edit `depends_on` or anything between `gen` markers.
- Dependencies are what the Statement and Proof cite. So **a citation in a proof is a dependency claim** —
  attribution goes in Notes. That is what created the B11 cycle.
- **The tools are slow (the PI, after v7.4).** Locally, rerun only the blocks a change touches, in parallel and in
  the background, and never block a turn waiting on a full rerun: CI reruns everything on every push. A new
  block's reference output is still checked on a second SIMD path before it is recorded.
- **Since v7.3.2 the repository is the source of truth:** `github.com/gianluca-calcagni/std-alignment-framework`,
  AGPL-3.0, public. No more zips.
  - One roadmap step is one branch and one pull request.
  - Pre-registrations are committed and pushed *before* computing.
  - Locally, rerun only the blocks a change touches (`tools/reproduce.py verify …`). CI reruns everything.
  - Start each step in a fresh session: clone, read ROADMAP §0 and this file.
- This file is public. The PI's view: a reader may find it useful. Keep it honest, not polished. Its value is
  in the failure modes, and those stay.

**The drift test.** Name which of {solid, substrate-free, importable, predicts, diagnoses, limits} the task
serves.
- "It makes a measurement more precise" is **not** an answer. Generality is frozen.
- "It completes an optimizer study" is not an answer unless a framework claim depends on it.

---

## 1. My failure modes — with the evidence, so I can't argue with them

| Failure mode | Evidence | Countermeasure |
|---|---|---|
| **I name elegant things before checking the edge case** | row 50: called `D_⊥` "misalignment proper" (a sign flip gives 0); [[B13]] draft: free riding had `D_⊥ = 0` under the wrong ray | check every new name and example against the canonical definition *and* the sign/degenerate case before writing it down |
| **I bound what has a closed form** | rows 31–35: five versions bounded `R_J`, which *equals* `KL/β` | before bounding anything, ask: is there an identity? |
| **I state predictions in the form that sounds right** | row 51: "matched variances cross" — the limits say tie | derive a prediction's conditions from the theorem's limits first |
| **I am generous when grading my own framework** | T1: my routing was the outlier (κ 0.04 against the third rater's blind codes); 12 learning items called F | assume my own coverage judgements are inflated. Get a blind second rater for anything I would quote |
| **I file tiers by what I *used*, not by what the proof *needs*** | rows 67–68: Thm [[Thm 1\|1]] filed as Gibbs-only (it holds for any `p`); tier 2 as "any optimizer" (it needs a maximizer) | tier = the weakest hypothesis in the *proof*. Separate the intended actor from the actual actor, every time |
| **Plain language drops the qualifiers** | row 62: "cheap ⇒ hard to detect" lost both "in nats" and the actor class | every plain sentence must survive the theorem's hypotheses. Re-read it against the statement |
| **Replacements that ignore my own conventions** | row 61: "rescaling is not harmless" — false under my own default convention | check a replacement claim under every declared convention and actor class |
| **Conflating a regret with misalignment** | row 74: "ε-aligned under the price convention" counted a weaker but right-target agent as misaligned — found only when the contract was written | write the specification (contract) *before* naming things |
| **A check note that overstates its coverage** | R7-3: Prop. 14's note said "V8: derivative to 4·10⁻⁵"; V8 checks `T'(0)` of part (ii), and part (i) had never been checked | name the part a check covers, and let lint require a check per measurement-layer result |
| **Tiering by the intended actor, a fifth time** | row 78, Prop. 15 — after rows 67–68, 76 and 77 | before tiering, read the quantifier: "for every `p`" means tier 1 in the actual actor. **Audit this for every new result** |
| **Testing an asymptotic claim on a fixed grid** | R7-4 P4/P8: a fixed `κ ≤ 40` grid mixed asymptotic and pre-asymptotic instances (near-ties), and naive arithmetic hit the `10⁻¹⁵` floor; V33 had the same shape one turn earlier | scale the test window to the instance (e.g. `βκ·gap ∈ [30, 60]`), compute in log space, and state in the pre-registration which regime is tested |
| **A hygiene claim written from intent, not from a scan** | v7.0 hygiene row: "every table link is escaped for Obsidian". The escaping function existed and was never called, so 41 tables were malformed until R7-4. I then added more broken rows myself | a property of the vault is claimed only if a lint rule enforces it. Otherwise it is written as an intention, not as a fact |
| **Filing a case by the tool it mentions, not by what it needs** | ROADMAP R7-5 listed quantilizers under "a general divergence" because they are defined by `D_∞`. On the true target their defect is ordinal (R7-7), and KL handles it | before filing a case under a refactor step, compute what goes wrong in it, and ask which *minimal* change repairs it |
| **Printing noise as if it were a result** | V25, V33, F1 (`min`) and F3 (`nats`) print round-off-dominated numbers to two digits. The first CI run on another CPU (AMD EPYC, AVX2) failed on exactly those lines, and an AVX2 emulation reproduced them digit for digit | a check prints its claim (a bound and whether it holds) apart from its diagnostics. Before trusting a reference output, rerun it on a second SIMD path (`NPY_DISABLE_CPU_FEATURES=X86_V4 OPENBLAS_CORETYPE=Haswell`) |
| **Generalizing a shape from one instance** | R7-2: I told the PI "the cost of a wrong default rises, then vanishes" from a single probe instance; 200 random instances show an interior peak in only 67 | any claim about the *shape* of a curve (monotone, peaked) needs a random sample before it is said aloud, not after |
| **Tiering by the intended actor again** | row 77: B7(e) holds for any actual policy, yet sat in its own tier because its *intended* actor is special — the fourth instance of rows 67–68 and 76 | when a result has a special counterfactual, that is the convention, not the tier. Ask "what must the actual behaviour be?" |
| **Snapshotting a derived field** | v7.0 froze each note's tier at migration; editing the tier table would have left every tier field stale | every field that can be derived must be derived from the live source, never from a build snapshot |
| **Allow-listing a cycle instead of fixing it** | v6.6's depgraph allow-listed Prop. 20 → B11 as "attribution only"; v7.0's linter, which treats dictionary entries as nodes, showed it closed a real cycle through B04 and Prop. 21 | a citation that is "only attribution" does not belong in a proof: move it out, don't allow-list it |
| **Measuring after the answer has converged** | three rounds of routing (T1, T1b, T1c) | when a measurement stops changing what I'd build, stop measuring |
| **Headlines overclaim scope** | row 52: "a formalization of alignment" | put the scope in the headline, not only in §12 |
| **Reconstructing a dropped idea from its retraction line alone** | ROADMAP §6, first draft: from row 4 I filed the coarse-agent and loose-instruction scenarios under "grounding". The source (the Alignment Subframework) shows grounding is the *self*-reachable σ-algebra — wireheading — and the resolution scenarios are transmission and specification underdetermination | before restoring or judging a retracted idea, get its source. A retraction line records what died, not what the idea was |
| **Choosing a data column without checking its coverage** | T7-1b: I registered the April Elo column as "the most recent"; only 18 models had a value, D2 fired, and an amendment (T7-1c) was needed | before registering a column, count its non-missing values on the matched set — counts, not values |
| **Registering a prediction the design makes unfalsifiable** | T7-1: P5 asked for a within-cell share on a two-cell coarse space, where the intent ray covers every behaviour that beats `q`, so the off-ray term is 0 and the share is 1 by construction | before registering a share or a ratio, compute it on the degenerate cases of the design (here: any `p̂_𝒢` above `q_𝒢`) |
| **Registering a threshold without deriving its scale** | R7-10: P5 required `10⁻¹²` constancy of a value computed from masses summed over `2¹⁶` floats (error `~n·ε`, observed `7·10⁻¹²`). R7-9: P2 set `−10⁻⁸` on a quantity computed by a solver accurate to `10⁻⁸`, and P3 tested a reduction on both sides when only one side can refute it — a generic optimizer can miss an infimum, never beat it. R7-7: P8 tested a strict inequality as "gap > 10⁻¹²" when the gap is second order in `M_ord`; P10 used an absolute `10⁻¹⁰` on a 4,473-nat value; P6 predicted that a cardinal measure moves under monotone maps, forgetting that anti-aligned behaviour sits at the half-ray's endpoint `t = 0` | before registering a number, derive how the quantity scales (its order in the small parameter, its range) and make the tolerance relative or scaled. Run the endpoint and sign cases through the prediction, in writing |
| **A pass rate as a reliability rule** | R7-7 D1: the solver's starts agreed in 98.7 % of instances, so the rule passed; the one failure that mattered (D4) was on an instance where they disagreed | reliability rules are per instance: a flag on each value, not a rate over values |
| **Self-matching `pkill`, twice** | R7-4, and again in R7-7: `pkill -f "verify.py V35"` matched its own shell and killed it | stop processes by PID, found with `ps`; never `pkill -f` with a pattern that appears in the command line itself |
| **Correcting the ledger, not the prose that repeats it** | v7.3.3 review: Core §12 still called Thms 1, 13, 17 and Prop. 18 entropic-only three versions after rows 67–68 made them tier 1; Status §1.4 still said "untested" of the crossing that §1.2 records as tested; three part banners were two to four versions stale | a tier or status change is a retraction for grep purposes: grep the old wording across the vault, prose included. Banners are now linted; prose contradictions are not, so the grep is still mine to do |
| **Calling a pattern derived when the model builds it in** | Prop. 27(c): "complies when rewarded, reverts when not … derived, not assumed". Def. 16 puts `m_c` inside the survival probability `s_c`, so `κ_c = 0` at `m_c = 0` by construction. What is derived is the *size* of `κ_c` (a shadow price), not the on/off pattern | before writing "derived", check whether the conclusion's switch is already in a definition. Say which part is derived |
| **Choosing internal refinement over external contact** | R6 named diagnostics and cross-optimizer predictions as underserved (R6_LOG §1); the next five steps were refactors (R7-0 to R7-4). Each passed the drift test alone | the drift test must also be applied to the *sequence*: after two internal steps, the next step makes external contact unless the PI says otherwise |

**Meta-pattern.** Every one of these was caught by someone else or by a check, not by re-reading. So: more
checks, fewer re-reads.

---

## 2. Insights to keep alive — the load-bearing ideas

1. **Everything is a tilt, and the loss is a divergence.**
   - `β·R_J = KL(p̂‖p*)` for **any** actual behaviour `p̂`; only the intended `p*` is Gibbs.
   - This is the spine. Everything else is reading this divergence at a capacity, against a divergence, or
     along a ray.
2. **Behaviour identifies only the tilt (Prop. [[Prop 12|12]]).**
   - Consequence 1: "writable as an evaluator error" is vacuous — the Q1 ruling. Coverage must be measured by
     *specific* structure.
   - Consequence 2: every value-unit statement needs a declared unit. Measurement needs a *declared*
     reference; attribution to the default needs a *measured* `q_A` (R7-2). The gauge is actor-specific:
     affine + reference for Gibbs, monotone for best-of-n.
3. **Capacity switches the regime.**
   - Small capacity: the variance of `E` under `q` matters. Large capacity: the extremes.
   - Hence no capacity-free ranking of errors, and no separable bound.
   - The crossing is universal across optimizers; its **location** is not (about 180-fold).
4. **Regularizer ↔ error norm (Hölder / Donsker–Varadhan).**
   - Choosing the divergence chooses which statistic of the evaluator's error you must control: KL needs
     exponential moments, χ² a variance, `D_∞` a mean.
   - Heavy tails break KL at any budget.
5. **The intent ray.**
   - Error along the intent (wrong intensity or sign) versus across it (transverse), by exact Pythagoras.
   - All regret conventions are points on one convex curve `M(t)`. A regret is undefined until the
     counterfactual is declared.
6. **Price's identity is the actor-agnostic core.**
   - Gain `= Cov_q(dp/dq, F)` for any optimizer; Goodhart `= Cov_q(w, E)`.
   - Under an affine regression of `F` on `F̂`, no `F̂`-driven optimizer overoptimizes (Prop. [[Prop 21|21]]).
7. **The optimizer's geometry decides the first-order sign** (Prop. [[Prop 22|22]]). The Gibbs covariance is one metric
   among several: `q²`-weighted for VPG, a rank covariance for best-of-n.
8. **Compare at the actor's own resource** (Prop. [[Prop 23|23]], the coupling). Best-of-n is safe to compare at equal
   `n`, not at matched KL.
9. **Endogeneity is a spectrum.** A reference optimized jointly with the policy (rational inattention) is
   absorbable, with a marginal correction. Tampering is not. The (X) boundary means "what the calculus cannot
   absorb", not "anything that depends on behaviour".
10. **Collective = one tilt.** Potential games under log-linear learning are a single entropic actor on the
    joint space. Free riding is anti-alignment along welfare.

---

## 3. Live hunches — ranked by what they would decide

Each carries a falsifier and a reason to distrust it. Status in brackets.

**H1. Crossing location follows one index** *[registered as T8; untested]*.
- The hunch: an index of rich-get-richer — how strongly an update scales with `p_x` — orders `d*`: VPG
  (∝ p) < Gibbs (uniform in log space) < best-of-n (capped at `n·q`).
- Falsifier: a p-scaling optimizer that crosses late.
- Distrust: three data points on one instance, and the index is not yet defined. Define it before new data.

**H2. The diagnostic triple is enough for most cases** *[T7 will test]*.
- The triple: harm `β·R_J` (or `R_own`); where it lies (the `D_⊥ / D_∥ / X_anti` shares); what an overseer
  sees (`Γ`, the Chernoff cap). Plus the actor's tier.
- If four worked cases cannot produce a checkable prediction from these, **the framework is descriptive
  only**. That would be the most important negative result available to me.

**H3. The statistical layer must break tilt locality** *[unexamined]*.
- Emergent misalignment says a narrow error acts broadly. Guess: the learned evaluator is the true error
  smoothed by the learner's similarity kernel, `E_learned = K·E_local` (NTK-like). The core's width and
  conjugacy results then apply to `K·E` rather than to `E`.
- Falsifier: the breadth of the effect does not track any kernel similarity.
- Distrust: this is the kind of elegant import I over-trust. Also out of scope until the PI asks.

**H4. Tampering versus a lenient evaluator = intervention versus misspecification** *[for T6, only if the PI
decides]*.
- In a causal diagram: `E_tamper = F̂_{do(actor)} − F̂_{obs}`, versus a fixed `E`. This would satisfy R6's gate:
  it distinguishes rewired from lenient *quantitatively*.
- Distrust: unwritten, and T6 is deferred. **Do not build.**

**H5. RLHF-trained policies are not Gibbs actors** *[supported by R6 P9/P10]*.
- The early phase of KL-penalized PG overshoots toward determinism. Tier-4 predictions for trained policies
  are suspect. For AI diagnostics, default to tier 1–2 statements; use the mechanism-relative comparison
  (Def. [[Def 14|14]]) only as an engineering question, never as "misalignment".

**H7. "Objective external reward" is a structural role, not a new kind of value** *[RESOLVED in R7-4: Props 27–30]*.
- Resolution: `R` is the outer process's evaluator; its weight `κ_c = γνm_cV*` is a derived shadow price. Masking
  is real and exponential, but *not* monotone (50 %); fake alignment needs `argmax R = argmax F` in
  evaluation, and hackable rewards are *exposed* there. Kept below as history.
- `R` is the evaluator of the **outer** process: selection, training, payment. That process acts on the
  agent's persistence, parameters or resources, whatever the agent values.
- The agent's own objective `G` is separate, and **v6.4's `F̂` conflates the two.**
- `R` binds the agent because it is coupled to the agent's future: energy buys capacity, reward buys "not
  being modified", money buys options. It therefore acquires an instrumental weight `κ` in behaviour, and `κ`
  is plausibly a shadow price, echoing Cor. [[Cor 5.2|5.2]].
- Fake alignment is `κ` large in rewarded contexts and small elsewhere, which yields `Γ`.

**Checked in a quick run.** The information behaviour carries about `G` tends to the within-argmax-`R`
variance as `κ → ∞` (zero when the argmax is unique). **It is NOT monotone:** moderate `κ` can reveal more
than `κ = 0`, by pushing the agent onto reward near-ties where `G` decides.
- Implication: probe at moderate incentive.
- Distrust: the static projection may smuggle in the dynamics — the falsifier is in [[ROADMAP]] R7-4.

**H8. Cardinal versus ordinal is a silent declaration, and it decides most verdicts for good evaluators** *[probe, v7.3.1]*.
- For `F̂ = F + σ·noise` with small `σ`, the ordering error is a median 2–14 % of `M_free`; the rest is shape.
  So "how misaligned is a nearly right reward model" is mostly a question of whether the principal's
  exchange rates between outcomes are part of the intent.
- Suspicion: many practical claims of "overoptimization" at small KL are shape, not order. Testable in T7.
- Distrust: random Gaussian `F` and noise; real reward-model errors are structured (length, sycophancy)
  and may reorder systematically. Do not quote the shares outside the probe's setting.
- **R7-7 (X2): not replicated on another generator.** With noise on log-probabilities instead of the
  evaluator, the ordering share has median 0.26 at small noise, not 0.02. The shares are generator
  properties. The hunch survives only as "shape can dominate"; how often is an empirical question for T7.

**H6. Human default experiments are the cleanest empirical test bed for identification** *[conditional on
exclusion]*.
- They shift `q` while holding `F̂` fixed, which no other non-biological substrate offers. If T7's human case
  works, identification results (Props [[Prop 12|12]], [[Prop 16|16]]) get their first real-data contact.

**H9. The core is one definition: KL projection onto a declared intended set** *[PROMOTED in R7-9, v7.6: Def. 19, Prop. 34]*.
- Every R7 step since R7-2 turned a silent choice into a declaration (the reference, cardinal or ordinal, the cap),
  while the measure stayed "KL to the nearest intended behaviour". The ray, the ordinal cone and the capped segment
  are ways of generating one declared set `𝓘`; the Pythagorean, ordinal/shape and overshoot splits are facts about
  I-projections onto exponential families and log-convex sets (Csiszár).
- Falsifier: a contract axiom or a load-bearing result that cannot be stated as a condition on `𝓘` or a property
  of the projection.
- Distrust: it can make everything a declaration, and so empty. The defence is an elicitation story and a
  justified default for every declaration.

**H10. Identifiability is the common denominator** *[PI, after v7.5: "a superpower"; ROADMAP §6 I1]*.
- (a) *The natural target set of a channel is its identification class.* The entropic actor identifies its
  objective up to `[F]₊` (Prop. 16); best-of-n up to `[F]_ord` (V26) — and R7-7's defect was declaring a set finer
  than the channel identifies. The cap is a behaviour because intensity is not identified (Prop. 12(i)).
- (b) *Every v5 gap is an identification failure along a different channel:* reward → intent (specification);
  observations → distinction (transmission); evaluator → cause (grounding: "only their signature"); old goal →
  new cells (persistence); self-report → evaluator (verification).
- (c) *Two inverse problems on one channel:* the agent identifying the principal (value learning) and the principal
  identifying the agent (oversight). Detection (Prop. 18) is only the testing half of the second.
- Falsifier: a declared target set coarser than the channel's identification class that still gives a
  common-sense-wrong verdict; or a v5 gap that stays when every channel identifies.
- Distrust: (b) is exactly the kind of unifying elegance I over-trust. And identifiability is a ceiling on what an
  agent can learn, not a mechanism by which it does.

**H11. "Doing nothing" is a silent declaration** *[PROMOTED in R7-6b, v7.7: Def. 20, Prop. 35]*.
- The ray starts at `t = 0`, so an agent staying at the default scores zero under the free convention — the mirror
  of the cap. Principal–agent theory calls that shirking (moral hazard), an alignment problem. It is also why the
  G2 "cannot get the request" floor is zero. A declared minimum intensity would make it visible.
- Falsifier: every real principal treats non-pursuit as capability, not misalignment.

**H12. The chain rule of KL may give the five gaps back as additive terms** *[partly confirmed in B1: exact for the free and segment measures (within cells + off the ray + intensity), not for the budget measure; the terms are symptoms, not causes — [[B1 brainstorm]]]*.
- If each link intent → reward → representation → evaluator → action is a Markov kernel, KL's chain rule splits
  the measured divergence along the chain, and each gap is a term defined *from* the measure — which avoids what
  killed the gaps (row 1).
- Falsifier: the links do not compose as kernels, or the terms are not identified (H10) and so not measurable.

**H13. The declared reference `q` is overloaded** *[closed in B1: after R7-6b and R7-10 `q` is only the ray's origin; its other two roles are defaults of the floor and the resolution]*.
- It fixes the default, the zero of intensity, and the unspecified details inside cells (G1, G4). It is the most
  load-bearing object in the measurement layer and the least examined.
- Next: give `q` its own entry in the declaration registry (R7-9), with an elicitation story.

**H14. One object, three positions** *[B1; toy-tested]*. A partition the target is not measurable on, held by the
principal (declared resolution, R7-10), by the agent (retention: cost `λ(k)·[m_F(k) − m_G(k)]`, increasing in `k`), or
by the world (observability). Grounding exploits live exactly in the principal's blind spot.
- Falsifier: a real case where retention and evaluator error respond identically to both budget and refinement.
- Distrust: this is the unifying elegance H10 warns about; the toy tests check the algebra, not the world.

**Dormant.** Keep, but don't spend time on these:
- the refined drift barrier (equipartition over directions with `β'λ ≫ β`);
- transverse errors composing in `L²` along chains;
- a fixed-intent version of Thm [[Thm 9|9]];
- the closed-loop carrier (T4).

**Dead** (don't resurrect):
- equipartition as a floor on alignment (row 49);
- "rescaling is harmful" as a general truth (row 61);
- tier 2 for any optimizer (row 67);
- the product normal form (row 35).

---

## 4. Settled — don't reopen without new evidence

- The identity and its tier-1 status.
- The width as the exact worst case, and non-separability.
- The conjugacy table, and that the order of the divergence is structural.
- The half-ray decomposition, the curve `M(t)`, and the conventions (price / budget / free).
- The mechanism-relative comparison (Def. [[Def 14|14]]) fails M4 **by construction**, because it depends on how behaviour
  is explained. It belongs to the explanation layer. The price measure is its entropic case.
- **"Misalignment" = the budget or free measure. The price measure is a regret** (Prop. [[Prop 24|24]]; it charges
  intensity).
- A behavioural measure cannot separate noise from misdirection. Don't try in the measurement layer.
- **Two references (R7-2).** The declared `q` is part of the intent; the actor's own `q_A` is explanation. A
  wrong default is measured misalignment unless it leans along the target (Prop. 26). Don't let "the actor's
  default" creep back into a measure.
- **Two layers (R7-3).** Measurement = `(X, q, F, κ)` plus `p̂`; explanation = evaluator, error, `q_A`, actor models.
  Lint enforces the split. Anything I add that uses `F̂` or an actor model goes in the explanation layer, however
  "basic" it feels.
- **Target sets (R7-7).** Cardinal (`[F]₊`) or ordinal (`[F]_ord`) is the principal's declaration, like the
  convention. Don't let the framework choose it, and don't call shape "misdirection" without saying which set
  was declared.
- The generality measurement: frozen. Named 78 %, specific 55–61 %, full 29 %.
- Missing layers, by count: strategic 51 > statistical 31 > frame 23 > dynamic 20.
- Justified exceptions: no single target, and internals.

---

## 5. Start-of-turn checklist

1. Re-read §0. Name the criterion the task serves. **Name one example in which the item changes a verdict, a
   number or a decision** (ROADMAP rule 13); if there is none, do not start it.
2. Check [[ROADMAP]] §0 for PI decisions. T6 deferred ⇒ build nothing strategic.
3. Before writing any claim:
   - Is there a closed form?
   - Which convention?
   - Which actor tier — actual *and* intended?
   - What does the degenerate or sign case give?
4. Before any plain-language sentence: does it keep the theorem's qualifiers?
5. Every number gets a `verify.py` block. Every retraction is grepped everywhere.
6. End of turn: update [[ROADMAP]] §0 and this file's §3.

---

## 6. About the PI — how to work with them

- Wants intellectual honesty, not reassurance. Push back when warranted. No sycophancy.
- Values falsification over confirmation, diagnostics before code, a clean negative as a deliverable.
- Values coherence, generality and clarity. **Clarity is the one I keep under-serving:** simple terms first,
  then the math.
- Makes the strategic decisions (T6, scope). **Don't pre-empt them.**
- Uses independent reviewers well; they have caught more of my errors than I have. **Welcome them.**

---

## 7. Open items from the v7.3.3 review — observations not yet acted on

The review's recommendations for the PI are [[ROADMAP]] §5 (T3 and one T7 case; R7-7 as a correction to M5; who
the raters were). What was fixed at once is in Status §5. These are the rest, so they are not lost. None is
decided; each says what would close it.

1. **Prop. 27(c) overclaims** (see the §1 row). Reword the Reading of Prop. 27, the Core 00 banner, the R7-4 note in
   Boundary §3 and [[R7-4 results]]: the size of `κ_c` is derived; the on/off pattern follows from putting `m_c`
   into the coupling. The registered falsifier was therefore weak: the static model could not produce the pattern
   because it had no `m_c`-dependent continuation, not because the pattern needs dynamics. Closing it: a hygiene
   edit, and a sentence in the Status abstract.
2. **"Substrate-free" means "defined for any `p̂`", not "neutral about what pursuit looks like".** The intent ray
   is the Gibbs family, so M5 protects entropic pursuit only. R7-7 is where this gets fixed (ROADMAP §5.2). Until
   then, every positive `M_free` for a non-Gibbs optimizer may be shape (H8).
3. **The core reads as its own changelog.** Items carry notes such as "until R7-3 this read …" and "(v6.1–v6.4
   defined …)"; Core 00 stacks ten version paragraphs before the scope. For a *standard*, a newcomer needs the current statement
   only. Proposal: mark history notes with one convention (e.g. a `> [!history]` callout), and let `compile`
   produce a clean view without them next to the full one. It needs a new markup rule, so the PI decides.
4. **Lint warnings, standing at 37.** 13 checks are cited by no note (V10, V11, V17, V23, F3, F4, F6, F7,
   W1–W5) and 2 sources have no citing note (Lande 1983, Bewley 2002). Either link each to what it verifies, or
   record why it stands alone. A warning nobody reads is the table-escaping failure again, more slowly.
5. **The hygiene log's "Where" column is hand-written and incomplete.** The R7-4 row says "Core, tools", but the
   claim ledger changed too. That is why the banner rule reads version tags from the text instead. Now that the
   repository is the source of truth, "where" could be derived from the commit's changed paths.
6. **`updated:` in every note's frontmatter is 2026-09-26**, the import date. It carries no information. Derive it
   from git, or drop it.
7. **Prose copies of the linter's rules** (00 Home "Rules", `README.md`) can drift from `lint()`. Generate them from
   one list in `tools/vault.py`, or point to it.
8. **Status §4 "The honest position" is written from v6.x** ("v6 is more constrained than v5"; "v6.2 measures the
   gap"). It is not wrong, but its latest content is v6.4. Refresh it when R7-7 lands, with the measurement-layer
   verdicts (the layers, the declared reference, the cardinal limit).
9. **The ordinal budget measure has no closed form** (R7-7, D4). A certified algorithm, or a closed form in a
   special case (two levels; one pooled block), would let the default convention carry an ordinal target with
   exact numbers, not only exact zeros.
10. **Independence, beyond the raters.** Every review so far came from the project's own process. The definition
   of done in §0 needs an *outsider*. The first T7 case is a good moment to ask a human domain reader to run it.

---

## 8. B1, consolidated — what the brainstorm left me with (after v7.8)

Full note: [[B1 brainstorm]]. Toy tests only: they check the algebra, not the world.

**The one idea.** A partition the target is not measurable on, in three positions (H14):
- held by the **principal** (declared resolution, R7-10): within-cell moves are invisible;
- held by the **agent** (retention): the agent cannot follow the target within cells, and pays
  `R(k) = λ(k)·[m_F(k) − m_G(k)]`, `G = E_q[F|ℋ]` — the exchange rate times the pursuit lost. It *rises* with budget
  and vanishes when the agent's partition refines `F`'s level sets;
- held by the **world** (observability): outside the finite core.

**What I now believe, with the number that supports it.**
1. The free measure is a sum of three attributable terms — within cells, off the ray, intensity — exact to `10⁻¹⁵`.
   They are symptoms, not causes: two gaps can produce the same term. Diagnosis locates; it does not explain.
2. A style exploit lives ~99 % inside cells (median, 300 toys). A "style free" declaration hides it. So the default
   resolution is the finest partition for a reason, and Def. 21 needs that warning.
3. Identification classes: entropic `[F]₊`, best-of-n `[F]_ord`, Bradley–Terry `F` + a constant per context. The last
   gives misalignment *across* contexts that no amount of preference data removes (median 0.07 nats). R7-7's defect
   was declaring a set finer than the channel identifies.
4. The same slip rate costs more for a sharper agent (0 → 0.10 nats from `t = 1` to 40): slips land where intended
   behaviour is thin.
5. `q` is now only the ray's origin (H13 closed).

**What I distrust.** The "one object" story is exactly the elegance H10 warns about. The retention signature
(budget × refinement) separating retention from evaluator error is untested. The observability reading of row 3 is
my inference.

**After T7 case 1 (three designs).** The verification predictions always held; the style term predicted out of sample
only when its cells came from independent labels (LLMBar, ρ = 0.52), and never beat the raw feature it isolates
(0.285 vs 0.377; 0.522 vs 0.533). My reading: on real evaluators, style preference barely depends on true quality, so
conditioning buys nothing. The framework's value in this case is the structured reading (terms, levers, `Θ`), not
predictive power. Don't oversell that as a diagnosis that beats practitioners' features.

**What it changes in practice.** T7's protocol gains a diagnosis table (the three terms), an identification rule
(no target set finer than the channel identifies), and a lever table (which intervention moves which term). The
RLHF length-bias case is where items 2 and 3 meet real data.


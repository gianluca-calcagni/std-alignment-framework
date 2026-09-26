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

**Current work:** the R7 refactor, one assumption per turn. R7-0 (v6.5), R7-1 (v6.6), R7-2 (v7.1), R7-3 (v7.2) and R7-4 (v7.3) are done; R7-5 closed as a clean negative (v7.3.1). **v7.0: the
package is an Obsidian vault.** Next is R7-7 (target sets, confirmed by the PI), led by the ordinal target. Apply the PI's test — a real case,
or no step — before R7-6 and R7-8 too.

**Vault habits.**
- Shell heredocs that contain Markdown must be quoted (`<< 'EOF'`). An unquoted one ran the backticks as
  commands and silently blanked text in a note (R7-2; caught by reading the note back).
- Edit notes, then `sync`, then `lint` (0 errors).
- Never hand-edit `depends_on` or anything between `gen` markers.
- Dependencies are what the Statement and Proof cite. So **a citation in a proof is a dependency claim** —
  attribution goes in Notes. That is what created the B11 cycle.
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
| **Generalizing a shape from one instance** | R7-2: I told the PI "the cost of a wrong default rises, then vanishes" from a single probe instance; 200 random instances show an interior peak in only 67 | any claim about the *shape* of a curve (monotone, peaked) needs a random sample before it is said aloud, not after |
| **Tiering by the intended actor again** | row 77: B7(e) holds for any actual policy, yet sat in its own tier because its *intended* actor is special — the fourth instance of rows 67–68 and 76 | when a result has a special counterfactual, that is the convention, not the tier. Ask "what must the actual behaviour be?" |
| **Snapshotting a derived field** | v7.0 froze each note's tier at migration; editing the tier table would have left every tier field stale | every field that can be derived must be derived from the live source, never from a build snapshot |
| **Allow-listing a cycle instead of fixing it** | v6.6's depgraph allow-listed Prop. 20 → B11 as "attribution only"; v7.0's linter, which treats dictionary entries as nodes, showed it closed a real cycle through B04 and Prop. 21 | a citation that is "only attribution" does not belong in a proof: move it out, don't allow-list it |
| **Measuring after the answer has converged** | three rounds of routing (T1, T1b, T1c) | when a measurement stops changing what I'd build, stop measuring |
| **Headlines overclaim scope** | row 52: "a formalization of alignment" | put the scope in the headline, not only in §12 |

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

**H6. Human default experiments are the cleanest empirical test bed for identification** *[conditional on
exclusion]*.
- They shift `q` while holding `F̂` fixed, which no other non-biological substrate offers. If T7's human case
  works, identification results (Props [[Prop 12|12]], [[Prop 16|16]]) get their first real-data contact.

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
- The generality measurement: frozen. Named 78 %, specific 55–61 %, full 29 %.
- Missing layers, by count: strategic 51 > statistical 31 > frame 23 > dynamic 20.
- Justified exceptions: no single target, and internals.

---

## 5. Start-of-turn checklist

1. Re-read §0. Name the criterion the task serves.
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

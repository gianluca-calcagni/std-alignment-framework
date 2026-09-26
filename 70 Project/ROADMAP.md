---
id: "ROADMAP"
type: "project"
source_file: "ROADMAP.md"
updated: "2026-09-26"
---
# ROADMAP v4

**Operational document. Read at the start of every turn. Current position is in §0; the goal is in §1.**

---

## 0. Position

| | |
|---|---|
| **Current** | **v7.3.3 — review of the package against §1.** Mathematics sound, every check reproduces on a second machine; stale status text corrected, and lint now rejects a part banner older than its own text. The review's recommendations are §5, for the PI. Before that: **v7.3.2 — bibliography consolidated** (`references.bib`, one entry per source note, lint-checked). **v7.3.1 — R7-5 closed as a clean negative** ([[R7-5 go-no-go]]). The PI's rule: proceed only if a real case needs a divergence other than KL. None was found. Detectability and the measure's KL are forced (Stein/Chernoff; Thm 1). The regularizer cases belong to the explanation layer (Props 10–11). The one real defect — best-of-n and quantilizers on the true target score as misaligned — is an **ordinal-target** issue that KL handles (R7-7). Before that: v7.3 (R7-4, external reward), v7.2 (R7-3, two layers), v7.0 (vault) |
| **Next** | **R7-7** — target sets, with the **ordinal target** as its lead case: `M_ord` (the KL projection onto the monotone-ratio cone, closed form by isotonic regression) and the split `M_free ≥ M_ord + M_free(p°)`. First task: pre-register, then write the target-set definition against the contract. §5 proposes running T3 and one T7 case before or alongside it, and restating M5 in R7-7 |
| **Baseline** | v6.4 is the revert target for the whole R7 series |
| **PI decisions pending** | T6 (the strategic/frame layer) is **deferred by the PI**. Do not build toward it |
| **Scope** | this thread's purpose (§1). The North Star is related but not in scope here |
| **Workflow** | since v7.3.2 the repository is the source of truth: [github.com/gianluca-calcagni/std-alignment-framework](https://github.com/gianluca-calcagni/std-alignment-framework), AGPL-3.0, public. One roadmap step is one pull request, and CI reruns every check. Pre-registrations are pushed before computing |

---

## 1. The goal — re-read before every turn

**A standard formal framework for a theory of alignment.** It should be:
- solid enough to build on;
- substrate-independent (AI, humans, institutions, organisms);
- easy to import existing theorems into;
- able to make **testable predictions**, support **diagnostics**, and show **limits and connections**.

Novelty is not the point.

**Drift test.** Before starting any piece of work, name the criterion above that it serves. "It makes the
measurement more precise" is not one: the measurement is frozen. "It makes an optimizer study more complete"
counts only if a stated framework claim depends on it.

---

## 2A. The refactor series R7 — simplifying the core *(highest priority; serves: solid, substrate-free, importable)*

**Aim.** Split the core into two layers.
- **Measurement layer.** Misalignment is defined from behaviour, a target and a declared counterfactual.
- **Explanation layer.** Actor models, evaluators and resources.

Each dropped assumption moves from the *definitions* into the *hypotheses* of the results that need it.
Nothing is lost; everything becomes explicit.

**Discipline — every R7 turn follows these seven steps, in order. One assumption per turn.**
1. **Dependency scan.** Run `python3 tools/vault.py scan A<k>` for the assumption, and `python3 tools/vault.py deps "<note>"`
   for anything touched. Read every hit by hand: the scan patterns are regular expressions.
2. **Definitions first.** Write the new definition(s). Show they satisfy the misalignment contract (below),
   and that they reduce *exactly* to the v6.4 definitions in the special case.
3. **Restate dependents.** Each dependent result is restated with the re-introduced hypothesis made explicit.
   Proofs are not changed unless forced; a changed proof is a new result with a new check.
4. **Soundness check** (`python3 tools/vault.py sync`, then `python3 tools/vault.py lint`, which must report 0 errors).
   - Dependencies are the references in a note's Statement and Proof, parsed from the text. They cannot be
     hand-edited, so they cannot drift.
   - The linter checks:
     - no cycles;
     - definitions citing only earlier items (earlier results only for well-definedness; these are listed);
     - `[Assumes …]` tags;
     - that links resolve and checks and sources exist;
     - that generated sections are current.
   - Commentary goes under "Notes and checks", never in the Statement.
5. **Checks.** `verify.py` and `final_audit.py` all green; a new block for every changed claim.
6. **Record.** Hygiene log and any retractions in D; NOTES §3; `ROADMAP` §0.
7. **Stop rule.** If a dependent cannot be restated soundly within the turn, stop, restore it from v6.4, and
   report which dependency blocked.

### R7-0 — Tools and the definition contract *(done, v6.5)*

**Outcome.**
- The contract is Def. [[Def 11|11]] (M1–M6 and M8 are axioms; M7 and M9 are refactor constraints).
- Prop. [[Prop 24|24]]: budget and free satisfy it; **the price measure fails M5**; raw `ΔF` fails M1–M2. So ε-alignment
  is restricted to budget and free (row 74).
- The behavioural limit is recorded: unsystematic error cannot be told apart from misdirection without an
  actor model.
- The dependency tool found two weak circularities (Thm [[Thm 13|13]] ↔ Thm [[Thm 17|17]] ↔ Prop. [[Prop 16|16]]) and claims inside
  definitions. **All fixed.**

*The plan as written before the turn follows.*

**Work.**
- A **dependency-graph tool** (`tools/depgraph.py`). It parses A, B and C for result labels and references,
  plus which primitives each result uses (`q`, `F̂`, `KL`, `β`, `F`, the actor). It reports cycles, orphans,
  and the dependents of any primitive.
- **The misalignment contract.** Written into A as a definition-level specification, with a check for each
  property (proof, or numeric where the property is empirical in character). A misalignment measure `M`
  should satisfy:

| | Property |
|---|---|
| M1 | `M = 0` iff the actual behaviour equals the intended behaviour under the declared counterfactual |
| M2 | `M ≥ 0` |
| M3 | invariant under re-representations of the same target — positive affine maps — given the declared convention |
| M4 | defined from behaviour: needs no internal objective of the agent |
| M5 | separates *misdirection* from *weakness*. An agent pursuing the target itself at lower intensity is not misdirected (the transverse part is zero) |
| M6 | substrate-free: defined for any distribution on `X` |
| M7 | reduces to `β·R_J = KL(p̂‖p*)` in the v6.4 special case |
| M8 | context-aware: deployment misalignment and evaluation misalignment are separately defined (Prop. [[Prop 19\|19]]) |
| M9 | sanity cases pass: a sign-flipped agent, a rescaled agent, a pure-noise agent, and an agent aligned in evaluation but not deployment are each classified as common sense expects. This is a **numeric test suite**, not a theorem |

**Gate.** v6.4's measures must pass M1–M9 before anything is dropped. Any failure is fixed, or recorded as a
known limitation, first.

### R7-1 — A1: the actual actor is no longer assumed to be a Gibbs optimizer *(done, v6.6)*

**Outcome.**
- `p̂` is a primitive. Def. [[Def 13|13]] defines actor models, with hypothesis (E) for the entropic model; Def. [[Def 5|5]] names
  (C). Twenty-odd results carry explicit tags, and the tool checks for untagged uses.
- Five items were mis-tiered (row 76).
- The mechanism-relative comparison `M_own` (Def. [[Def 14|14]]) fails M4 by construction, so it belongs to the
  explanation layer; `R_own` also fails M1 and M2 (Prop. [[Prop 25|25]], row 75).
- Insight: the price measure is the mechanism-relative measure for the entropic model. That explains why it
  needs a unit and fails M5.
- The DAG is clean. M7 holds trivially: no measure changed.

*The plan as written before the turn follows.*
- Primitive: the actual behaviour `p̂ ∈ Δ(X)`.
- The Gibbs actor becomes one explanatory model among others.
- Expected dependents: the tier-4 results, which already carry tags. Low risk.

### R7-2 — A3: separate the intended reference from the actor's own reference *(done, v7.1)*

**Outcome.**
- **Notation:** `q` stays the symbol for the **declared** reference, now part of the intent; the actor's own
  reference is `q_A`, in Def. 13 under the new hypothesis (E_A). Keeping `q` for the declared one made the
  reduction to v7.0 exact (M7): no measure changed, and V1–V31 reproduce.
- **Prop. 26:**
  - absorption, which transfers every (E) result to (E_A);
  - behaviour cannot separate the two loci;
  - a wrong default is misalignment unless it leans along the target, `log(q_A/q) = aF + c` with `β + a ≥ 0`;
  - the second-order size;
  - the limits in `β`: the cost of a wrong default is not monotone in optimization strength.
- The alternative — the budget matched on `q_A` — fails M4 (V32).
- **Found by the scan:**
  - B7(e) was mis-tiered (row 77);
  - B12's entropic reading was untagged;
  - the vault's tier field had been frozen at migration, and now derives from the live table.

*The plan as written before the turn follows.*

**Proposal to settle first (from the v7.0 turn).** Match the budget measure against the **intended** reference
`q*`: `λ` solves `KL(p^{q*}_{F,λ} ‖ q*) = KL(p̂ ‖ q*)`.
- Reason: M4. The actual actor's reference `q` is not identified from behaviour (Prop. 12), so a measure that
  uses it is not behavioural.
- Consequence: a wrong default registers as misalignment, which agrees with Rem. 16.1 (a wrong reference is
  behaviourally an evaluator error).
- Alternative (match against `q`): rejected, because it fails M4.
- To check: the contract suite V30 run with `q* ≠ q`, and the reduction to v6.4 when `q* = q`.
- Measurement uses only `q*`; `q` moves to the explanation layer.
- Reference misspecification becomes a named failure mode.
- Watch: the gauge results (Props [[Prop 12|12]], [[Prop 16|16]]) and the budget convention, which matches `KL(p̂‖q)` or
  `KL(p̂‖q*)` — decide which, and justify it.

### R7-3 — A2: the evaluator moves to the explanation layer *(done, v7.2)*

**Outcome.**
- **Layers.** 20 measurement items and 36 explanation items. Lint enforces three rules:
  - no explanation vocabulary in a measurement statement or proof;
  - no measurement item depending on an explanation item;
  - a check for every measurement-layer result.

  Each rule was tested by a planted violation.
- **Splits.** Def. 1 → Def. 13 (the evaluator); Def. 5 → Def. 15 (hypothesis (C)); Prop. 14(i) → Lemma 5.1;
  Cor. 1.1(a) → Thm 1. An instance is `(X, q, F, κ)`.
- **Symbol-derived dependencies** recovered about 120 missing edges, with no new cycle.
- **Found:**
  - Prop. 15 was tiered by its intended actor (row 78) — the fifth instance, so tier 3 is empty;
  - Prop. 14(i) / Lemma 5.1 had never been checked (V33).
- **M7:** no measure changed. The frozen census routing is untouched.

*The plan as written before the turn follows.*
- The measurement layer no longer mentions `F̂`.
- Watch: the error-based bounds, Prop. [[Prop 20|20]]'s decomposition, the routing rules in [[T1_RULES_FROZEN]] (Q1
  mentions evaluator errors), and the dictionary entries. The frozen measurement is recorded against v6.3
  and is not re-run.

### R7-4 — The two-evaluator explanation layer: external reward versus the agent's own objective *(done, v7.3)*

**Outcome** ([[R7-4 results]]).
- Def. 16 and (E_R). Prop. 27 derives the weight on reward as a shadow price, `κ_c = γνm_cV*` (Dinkelbach).
- Prop. 28 gives masking at rate `β·gap_R`; Prop. 29 shows selection sees only rewarded behaviour.
- Prop. 30 is the fake-alignment gap; reward hacking is exposed, with an exact limit.
- The falsifier fired as anticipated: one stationary dynamic element is needed. Pre-registered 8, 6 held,
  and 2 failed as registered on test design.

*The plan as written before the turn follows.*

**Work.**
- Split the explanation-layer evaluator into:
  - `R`, the **external reward**: the evaluator of the *outer* process — selection, training, payment —
    that acts on the agent's persistence, parameters or resources;
  - `G`, the **agent's own objective**.
- Add a **coupling rule** saying how earning `R` feeds the agent's future resource or survival.

**Derive, or refute:**
- *selection equivalence* — the outer process cannot separate types with equal reward on its evaluation
  contexts;
- *instrumental tracking* — the weight on `R` in behaviour is a shadow price of reward in terms of `G`;
- *incentive masking* — as that weight grows, behaviour carries vanishing information about `G`;
- *the fake-alignment gap* — `Γ` generated by the reward's contingency across contexts.

**Pre-registered falsifier.** If the static projection cannot reproduce "complies when rewarded, reverts when
not" without assuming it, the layer needs dynamics, and it is recorded as such.

**Depends on** R7-3.

### R7-5 — A4: KL is replaced by a general divergence or resource *(not pursued, v7.3.1: no real case — [[R7-5 go-no-go]])*
- **Outcome.** The PI's test: proceed only if a real case needs it. Five candidates were examined. Each belongs to another layer or step: the explanation layer (heavy-tailed error, semantic blindness, diversity), R7-7 (best-of-n and quantilizers on the true target), R7-6 (coverage), R7-8 (deterministic behaviour on a continuous `X`). **Revival trigger:** a real principal whose intended regularizer is not KL, whose KL-measured verdict is wrong by common sense, and whose case none of R7-6, R7-7 or R7-8 repairs.
- *The original plan, kept as history:*
- The identity becomes Bregman (Prop. [[Prop 15|15]]).
- **Verify the decoupling claim:** outside KL, harm (a Bregman divergence) and detectability (KL / Chernoff)
  separate. The "cheap ⇒ hard to detect" link becomes a property of the entropic counterfactual.
- Quantilizers (`D_∞`) and χ²-regularization become native. *(v7.3.1: mis-filed. χ² is already native in the explanation layer, Props 10–11. Quantilizers on the true target are an ordinal-target case, R7-7.)*

### R7-6 — A5: non-linear targets
- The target becomes a functional `U` on `Δ(X)`.
- *PI's test (v7.3.1):* passes at first sight — coverage and diversity targets, where the entropic intent charges dropped modes only logarithmically ([[R7-5 go-no-go]], case 4). Apply the test properly before starting.
- The intent ray and Props [[Prop 20|20]]–[[Prop 22|22]] re-introduce linearity as a hypothesis.

### R7-7 — A6: a set of targets *(confirmed by the PI, v6.5; part of the core — the target is a measurement-layer primitive)*
- **Lead case (from [[R7-5 go-no-go]]): the ordinal target** `{φ∘F : φ increasing}`. Best-of-n and quantilizers on the true target score as misaligned under the cardinal measures (`M_free` median 0.04–0.39 nats, positive in 93–100 % of instances). `M_ord` scores them 0 and keeps KL. For nearly correct evaluators, most of `M_free` is shape, not order. Whether shape counts is a declaration the framework currently makes silently.
- Set-valued measures; aggregation only when a scalar is demanded.
- This changes the status of the "disagreeing principals" exception.

### R7-8 — A7: measurable spaces *(optional, last)*
- Integrability hypotheses per result.
- *Real trigger (v7.3.1):* deterministic behaviour on a continuous `X` saturates every f-divergence ([[R7-5 go-no-go]], case 5). The cheap remedy keeps KL: measure outcomes, or declare a resolution.

**Not dropped:** frame exogeneity (A8). It stays a stated hypothesis until a frame layer exists.

---

## 2B. Other turns

### T7 — Diagnostics, end to end *(after R7-3 or R7-4, so that it uses the two-layer core; serves: diagnostics, importability, predictions)*
**Work.**
1. Write a short **diagnostic protocol**:
   - identify target, evaluator, reference and resource, and declare the comparison convention (Def. [[Def 8|8]]);
   - name the actual-actor class and hence the tier of results that may be used;
   - locate the failure (L1–L7);
   - compute or bound the regret, the decomposition, and the evaluation gap `Γ` where applicable;
   - state one testable prediction and the imported theorems used.
2. Apply it to **four cases, one per substrate**:
   - RLHF length bias (AI);
   - retirement-enrolment defaults (humans);
   - free riding in public goods (institutions);
   - supernormal stimuli / evolutionary mismatch (biology).

   Each case gets numbers on a toy instance checked by a `verify.py` block, and cites its literature.

**Gate.** Each case must produce a prediction the case's own literature could check. A case that yields
only a relabelling is reported as such.
**Stop rule.** Four cases, not more. No new theory unless a case cannot be written without it; if so,
record the missing piece and stop.

### T8 — A prediction that holds across optimizers *(after T7; serves: testable predictions)*
**Work.**
- **Hypothesis (R6):** the capacity at which the C8 crossing happens is ordered by one index — how strongly
  an optimizer's update favours already-probable behaviour.
- Define the index **before** looking at new data.
- Pre-register predictions for at least two optimizers not yet tested, and for a second instance.

**Falsifier.** An optimizer whose update scales with `p` but that crosses late, or an order that the index
does not predict.
**Stop rule.** One index, one pre-registration, one run. If it fails, report the failure; do not search for a
second index in the same turn.

### T6 — The strategic/frame layer *(PI decision, deferred)*
**Evidence gathered** — useful whenever the PI decides:
- 51 items need a strategic layer and 23 a frame layer;
- R6's split: a causal / multi-agent influence-diagram layer fits about 45 AI and institutional items, while
  the 23 biological items need evolutionary game theory, extending [[B13]];
- R6's gate: the layer must attach `β·R_J` or `Γ` to diagram nodes, and distinguish a *rewired* evaluator
  from a *lenient* one.
- First tests: the tampering family (A3–A5, L5) and the off-switch game (D4, L15).

**Do not start until the PI decides.**

### T2 — closing the optimizer tests *(optional, for the record)*
- P12, instances 1150–1999: about 15 minutes of CPU. The verdicts are already stable.
- P9, KL-penalized policy gradient at scale: **dropped.** No framework claim depends on it.

### Later, only if a turn's goal needs them
- T3: the overoptimization slope against published coefficients.
- T4: the closed-loop carrier decision.
- T5: the dynamic form.
- A statistical layer. It must allow narrow errors to have broad effects: emergent misalignment contradicts
  the tilt model's locality.

---

## 3. Stop list

| Stopped | Why |
|---|---|
| census re-routing or re-adjudication | frozen (PI decision, v6.4). Future measurement only on held-out items, with frozen rules ([[T1_RULES_FROZEN]] §3) |
| further optimizer dynamics (KL-PG convergence, NPG numerics) | no framework claim depends on them |
| building the strategic/frame layer | awaits the PI (T6) |
| the North Star (minimal independent desiderata) | out of scope for this thread (PI, v6.4) |

---

## 4. Anti-drift rules

1. **Re-read §1 at the start of every turn**, and name the criterion each piece of work serves.
2. **The carrier is fixed:** the regularized actor with a fixed reference, entropic by default (Prop. [[Prop 15|15]]).
3. **Structure (v7.0): one note per item, typed, from `_templates/`.** New notes are free, but must have a type
   and pass lint. New *types* need the PI's approval. The scripts and `tools/` sit outside the vault.
4. **Search before claiming**, in the same turn.
5. **Elegance is a warning.** Write the falsifier before the consequences.
6. **A gate that fires is obeyed**, and its outcome becomes the headline.
7. **Retractions are propagated by grep** (F_method item 30).
8. **Every number in A or B has a `verify.py` block.** A number without one is not quoted.
9. **The generality measurement is frozen.** Quote it only as three nested shares with the band.
10a. **R7 discipline.** One assumption per turn; definitions before dependents; a DAG check every turn; exact
    reduction to v6.4 in the special case. If in doubt, stop and restore.
10. **Every turn ends with §0 updated.**

---

## 5. Recommendations from the v7.3.3 review *(for the PI; not decided)*

A review of the whole package against §1. The mathematics is sound, as far as the proofs read go; the limits are
shown unusually well; and every numerical check reproduces on a second machine. The two outward criteria of §1 —
**testable predictions** and **diagnostics** — are not yet met, by the project's own definition of done ([[NOTES_claude]]
§0: an outsider runs a real case and gets a diagnosis, a checkable prediction and the imported theorems). Three
recommendations, in order. A fourth — a lint rule for stale status banners, and the corrections it prompted — was
applied in v7.3.3. The review's other observations are in [[NOTES_claude]] §7.

1. **Run T3 and one T7 case before R7-7, or alongside it.** *Serves: predicts, diagnoses.*
   - R6 marked "diagnostics on real cases, and predictions that transfer across optimizers" as underserved, and
     named T7 and T8 as the next turns ([[R6_LOG]] §1). Five refactor steps followed (R7-0 to R7-4), then R7-5's
     go/no-go. Each passed the drift test on its own terms. Together they deferred the two criteria that no
     refactor can serve.
   - C8, C9 and C11 have been checked only on the project's own generators. Status §6: almost nothing has come from
     a prediction succeeding on its own terms.
   - T3 — C9, the overoptimization slope `α ≈ √2·ρ·sd` against published coefficients — is by Status §3 "the
     cheapest external contact", and it sits under "Later".
   - **Proposal.** T3 as one small pre-registered step. T7 with one case first, before committing to four: the
     human default case, where B12 supplies the identification ([[NOTES_claude]] H6). If that case yields only a
     relabelling, T7's gate has fired early and cheaply.
2. **Treat R7-7 as a correction to the definition of misalignment, not an extension.** *Serves: solid.*
   - The measurement layer's intended behaviour is always a Gibbs tilt of the declared reference. So
     "misalignment" is the distance from what an **entropic** agent pursuing `F` would do. M5 protects pursuit by
     that one model only: best-of-n and quantilizers run on the true target score as misaligned in 93–100 % of
     instances ([[R7-5 go-no-go]]).
   - **Proposal.** R7-7 restates M5 without the Gibbs family: an agent that pursues a declared member of the
     target set, at any intensity, has `M = 0`. It then shows that the cardinal declaration recovers the current M5
     exactly (M7). The cardinal/ordinal choice becomes a declared convention of Def. 8, like price, budget and free,
     instead of a silent default.
3. **Say who the raters and reviewers were, and add one from outside.** *Serves: solid, limits.*
   - The census raters and reviews R5 and R6 are called independent, but the vault never says who or what they
     were. R5's scripts ran under `/home/claude/` (`reviews/R5_independent/compare.py`), which suggests sessions of
     the same model family as the executor. Errors from one model family are correlated, and "independent"
     then means less than it says.
   - Agreement was moderate: κ 0.54–0.57 between the first two raters on expressibility, and 0.04 between the
     first rater and the third rater's blind codes on the disputed items. The "specific" band, 55–61 %, spans two
     codings of one rater; it does not carry the between-rater uncertainty.
   - **Proposal.** State the raters' and reviewers' identity in [[T1_census_routing]], [[R5_LOG]] and [[R6_LOG]]. For the
     next measurement on held-out items ([[T1_RULES_FROZEN]] §3), use at least one human rater or a different model
     family. The frozen measurement is not re-run (§3).

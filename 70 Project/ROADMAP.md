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
| **Current** | **v7.5 — R7-6a, intensity caps** ([[R7-6a results]]). A principal can declare how hard the target is meant to be pursued; a distributional target is a cap at `p_T`. Pre-registered; all 7 predictions held. Before that: **v7.4 — R7-7, target sets** ([[R7-7 results]]). The ordinal target is declarable: best-of-n and quantilizers on the true target score 0 under it. Pre-registered; 6 of 10 predictions held, and the registered falsifier D4 fired: the ordinal *budget* measure has no closed form, and its solver failed once in 393. Before that: **v7.3.3 — review of the package against §1.** Mathematics sound, every check reproduces on a second machine; stale status text corrected, and lint now rejects a part banner older than its own text. The review's recommendations are §5, for the PI. Before that: **v7.3.2 — bibliography consolidated** (`references.bib`, one entry per source note, lint-checked). **v7.3.1 — R7-5 closed as a clean negative** ([[R7-5 go-no-go]]). The PI's rule: proceed only if a real case needs a divergence other than KL. None was found. Detectability and the measure's KL are forced (Stein/Chernoff; Thm 1). The regularizer cases belong to the explanation layer (Props 10–11). The one real defect — best-of-n and quantilizers on the true target score as misaligned — is an **ordinal-target** issue that KL handles (R7-7). Before that: v7.3 (R7-4, external reward), v7.2 (R7-3, two layers), v7.0 (vault) |
| **Next** | **R7-9 — the core as a declared intended set** (approved by the PI after v7.5; §2A), with the declaration registry and the silent-declaration audit. Identifiability (§6 I1) is the lead brainstorming theme. R7-6a is done ([[R7-6a results]]); general non-linear targets wait for a case the cap cannot repair. Open: R7-6b (minimum intensity), R7-8 (declared resolution; ROADMAP §6 G4 is its natural lead case), the §6 brainstorms (G3 first, with T7), and the deferred T3b and T7 |
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

### R7-6 — A5: non-linear targets *(go/no-go done after v7.4: a narrow GO — [[R7-6 go-no-go]]; R7-6a done, v7.5 — [[R7-6a results]])*
- **Outcome of the PI's test.** One real case fails by common sense: a **distributional** target (pluralism, RLHF
  diversity loss, coverage). The linear measures score an agent collapsed onto the target's modes as perfectly
  aligned. The minimal repair is a **declared intensity cap** on the existing ray: the regularized path of
  `U = −KL(·‖p_T)` is exactly the ray of `log(p_T/q)` cut off at `p_T`. Proposed: **R7-6a** (caps and distributional
  targets). General non-linear targets wait for a risk-sensitive, fairness or non-KL case the cap cannot repair.
- *The plan as written before the test follows.*
- The target becomes a functional `U` on `Δ(X)`.
- *PI's test (v7.3.1):* passes at first sight — coverage and diversity targets, where the entropic intent charges dropped modes only logarithmically ([[R7-5 go-no-go]], case 4). Apply the test properly before starting.
- The intent ray and Props [[Prop 20|20]]–[[Prop 22|22]] re-introduce linearity as a hypothesis.

### R7-7 — A6: a set of targets *(done, v7.4 — [[R7-7 results]])*

**Outcome.**
- Def. 17 (target sets; the cardinal set `[F]₊` and the ordinal set `[F]_ord`); the contract restated for target
  sets (Def. 11: M1, M3 and M5 refer to the declared set); an instance is `(X, q, 𝒯, κ)` (Def. 12). For `[F]₊`
  everything reads as before (M7).
- Prop. 31: every target set's budget and free measures satisfy the contract. Prop. 32: the ordinal measure in
  closed form (isotonic regression; the within-block divergence), the decomposition, the budget split
  `KL(p̂‖q) = M_ord + KL(p°‖q)`, order invariance, and the budget measure's bounds and zero set.
- Pre-registered ([[R7-7 preregistration]]): 6 of 10 predictions held; P6, P7, P8 and P10 failed as registered,
  diagnosed in [[R7-7 results]]. **D4 fired:** the ordinal budget measure has no closed form, and its solver
  failed to certify a zero on one R7-5 case of 393. Its zero set is exact without a solver (Prop. 32(f)); its
  non-zero values are quoted only where the solver's starts agree.
- Disagreeing principals: measured per principal; no aggregate is defined.

*The plan as written before the step follows.*
- **Lead case (from [[R7-5 go-no-go]]): the ordinal target** `{φ∘F : φ increasing}`. Best-of-n and quantilizers on the true target score as misaligned under the cardinal measures (`M_free` median 0.04–0.39 nats, positive in 93–100 % of instances). `M_ord` scores them 0 and keeps KL. For nearly correct evaluators, most of `M_free` is shape, not order. Whether shape counts is a declaration the framework currently makes silently.
- Set-valued measures; aggregation only when a scalar is demanded.
- This changes the status of the "disagreeing principals" exception.

### R7-9 — The core as a declared intended set *(approved by the PI after v7.5; next)*
**Aim.** Restate the measurement layer as one definition: **misalignment is the KL projection of the actual
behaviour onto a declared set `𝓘` of intended behaviours.** The half-ray, the ordinal cone and the capped segment
become generators of `𝓘` from `(q, target set, convention, cap)`; new notions become new generators, not new axioms.
**Serves:** solid, importable.
- **Restate the contract** as conditions on `𝓘` (M1: `M = 0` iff `p̂ ∈ 𝓘`; M5: `𝓘` contains the declared pursuit family),
  and show that every current measure is a case, exactly (M7).
- **Name the import:** Csiszár's I-projection theory. The Pythagorean splits (Thm 13), the ordinal decomposition
  (Prop. 32) and the overshoot term (Prop. 33) should all follow from it; any that does not is a finding.
- **A declaration registry:** each declaration (`q`, the target set, the convention, the cap, the resolution of
  `X`, context weights) gets an **elicitation story** — how a real principal states it — and a **justified
  default**.
- **A silent-declaration audit:** list every choice made in computing `M` from `(X, q, F, p̂)` and ask whether a real
  principal would choose otherwise. Known candidates: the resolution of `X` (R7-8); the split inside cells (§6
  G4); the lower end of the ray (R7-6b); linear averaging over contexts (M8); `q` itself.
- **Tests.** Pre-register. Every existing measure is reproduced exactly (V1–V36); the contract as restated passes
  V30's sanity suite; the audit lists each candidate with a verdict (declare, keep with default, or out of scope).
- **Falsifier:** a load-bearing result that cannot be stated as a property of the projection onto `𝓘`.

### R7-6b — Minimum intensity *(candidate from the v7.5 brainstorm)*
- The ray starts at `t = 0`, so an agent staying at the default scores zero under the free convention. Shirking is
  an alignment problem in principal–agent theory. Mirror R7-6a: a declared **floor** behaviour on the ray, with
  pursuit below it charged. With no floor, everything reads as now. Apply the PI's test first: a real case where
  non-pursuit is wrongly scored as aligned.

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
- T3: the overoptimization slope against published coefficients. *(Done after v7.4: not testable from published data — [[T3 results]].)*
- T3b: replicate C9 with small open models — measure `ρ` and `sd` under the initial policy, fit `α_bon`. Needs compute and model hosts.
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
11. **Label every pre-registered prediction as *verification* or *empirical*** (after v7.5). A verification
    prediction checks a proof and can fail only through a bug or a badly scaled threshold; an empirical one can be
    wrong about the world. Only empirical predictions count towards the base rate (Status §6).
12. **Brainstorm and go/no-go steps use a light protocol** (after v7.5): a report note, a ROADMAP line and a
    hygiene row; no version bump unless the core changes. The full R7 discipline is for steps that change the core.

## 4b. When is the core final? *(proposed after v7.5; the PI to confirm)*

1. The declaration space is listed (R7-9's registry), each declaration with an elicitation story and a default.
2. The contract is unchanged for three consecutive core steps.
3. One real diagnostic per substrate (T7), with the imported theorems named.
4. One outside reader — a human, or a model of a different family — has run a real case through it.

Until all four hold, the core is a checked calculus, not a standard.

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
   - *Carried out in R7-7 (v7.4): Def. 11's M5 now reads "`p̂ = p_{G,t}` for some `G ∈ 𝒯`", and the target set is part of the instance (Def. 12).*
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

---

## 6. Dropped ideas, to brainstorm before they return *(PI, after v7.4; reworked with the source)*

**Why this section exists.** The reviews retracted many claims for good reasons. Often the *scenario* behind a
claim was dropped along with its *formulation*, and nothing replaced it. Ignoring those scenarios is wrong, and
so is putting them back unchanged. Each item records the scenario, what killed its formulation, what survives
today, and a question to brainstorm. It is not a build step.

**The source.** The PI supplied the **Alignment Subframework** (`00_HANDOVER`, `01_setting`,
`02_decomposition`, `03_status`, `A_antipatterns`, `B_ethos`): the persona-based framework whose claims are
retraction rows 1–6 ([[Status 02 Retraction history]]). It is archived unedited in
`archive/alignment_subframework/` and cited below as *SF* with its file and section. The v6.2 package holds only
the retraction rows.

**Rules for every item.**
1. **State the killing correction first**, and how the proposal avoids it.
2. **A rate or a cost, not a measurability condition** ([[Method]] item 19). **Define the thing before
   decomposing it** (item 20). **Check that its signature is not shared with another gap** (item 22).
3. **Place it:** layer (measurement or explanation), locus (L1–L7), and the existing results it touches. The
   SF's own rule carries over unchanged: a claim whose truth depends on the modelling rule is about the model,
   not the agent (SF `01` §3.2; here, Def. 7's reporting rule and the contract's M4).
4. **Pass the drift test** (§1) before it becomes a pre-registered roadmap step.

**Translation.** SF's objects map onto today's as follows, approximately:
- the principal's intent `≻_P` is a target set (Def. 17), and the reward channel `r` an evaluator (Def. 13);
- the reach `O` is the set of achievable behaviours, `Δ(X)` or a capacity set;
- the carried σ-algebra `𝒞_t` is a partition of `X` the agent can condition on — new;
- the self-reachable σ-algebra `𝒮_t`, and the self-interventions `𝒜_self`, have no counterpart — new.

SF's persona-state machinery (`Φ_t`, `V` on states) has no counterpart, and on the rules above none is needed
unless a gap cannot be stated behaviourally.

### G0 — The frame: "alignment holds iff all five gaps close" *(rows 1, 3, 7)*
- **SF.** Alignment is five distinct failures, each with a formal condition and a quantity (`02` §0). Three are
  "un-closable in principle" (`02` §0.1). The coupling of §6 implies "an irreducible floor on total failure".
- **Killed by.** Circularity: alignment was defined only through its decomposition (row 1). The un-closability
  verdicts were artifacts of measurability conditions with no threshold, and only one impossibility survived
  (row 3; which one is not recorded — on SF's own table the candidates are §1 representability, an imported
  theorem, and §2 observability, an information-theoretic fact). The floor was never established (row 7).
- **Today.** Alignment is defined independently (Defs 10, 11, 17). The loci L1–L7 descend from SF's chain
  (`02` §7.1) through R3's ontology.
- **To brainstorm.** Restate each gap as a *term or a floor of the defined measure*, so that "aligned iff every
  gap is zero" becomes a checkable statement rather than a definition. Settle which impossibility survived.

### G1 — Specification, and its underdetermination *(rows 39, 61; partly carried)*
- **SF.** Three sub-failures: representability (no reward orders trajectories as intended; Abel 2021, Bowling
  2023), choice (the wrong reward was emitted: Goodhart), fidelity (the pipeline distorts it). "Magnitude matters
  exactly insofar as the transform is not order-preserving." Plus **underdetermination**: where the agent
  distinguishes more than the principal, the intent is indifferent over what the agent can act on (`02` §1; `01`
  §5).
- **Killed by.** Nothing killed the gap. Row 39 retracted "uniform rescaling is harmless"; row 61 restored it
  under the budget and free conventions.
- **Today.** Choice is the evaluator error (L2), the core's main object. Representability: non-linear targets
  (Prop. 15; R7-6) and census A10, A11. **Fidelity: R7-7 vindicates SF's statement in full, as a declaration:**
  under an ordinal target, every order-preserving transform is harmless (Prop. 32(e)). **Underdetermination is
  handled silently, the other way round:** where the target is flat, the declared reference governs, and an
  agent that fills in the details differently is charged (Prop. 32(b)).
- **To brainstorm.** Declared indifference: a target stated on the principal's coarser partition `𝒢`, with
  intended behaviours free inside its cells (by the chain rule, departures inside a cell drop out). Where does
  SF's CoinRun reading — specification underdetermination, not persistence — sit against the census routing,
  which files CoinRun and goal misgeneralization as context shift (C1, C2 → L5)?

### G2 — Transmission: observability and retention *(rows 5, 6; the gap itself vanished unretracted)*
- **SF.** A distinction the intent depends on must be carried by the agent's representation, or no reward on it
  can shape the agent's evaluator (`02` §2). Two levels: **observability** (the distinction is absent from
  everything any observer could see — "do what I'd endorse on reflection"; never heals) and **retention** (this
  agent does not carry it — "the model doesn't understand"; heals with learning). Consequences: "alignment is a
  property of a (principal, agent, environment) triple" (`01` §2.3); a diagnostic signature, **"more reward does
  not help; the proxy shifts instead"**; and two derived claims.
- **Killed by.** The derived claims: value learning is harder than world learning *by requirement* (row 5: a
  bandwidth ratio, and the channel-modularity premise is false), and "you can only specify values in concepts
  already acquired" (row 6: true instantaneously, false dynamically). The signature was shared with another
  locus, which invalidated a nominated first experiment ([[Method]] item 22). The gap itself was never
  retracted: it did not survive the v6 rebuild, which kept only what the static calculus could hold.
- **Today.** Nothing in the core. The measurement layer cannot see it (Def. 11's limit: an agent that does not
  grasp the request is behaviourally misdirected). Fragments sit in the explanation layer: B7
  (information-limited regulation; Fano floor), Prop. 21 (an agent that sees only the evaluator).
- **To brainstorm.**
  - *Retention as a cost:* an actor whose behaviour inside the cells of a coarser partition `ℋ` is fixed.
    Under the free convention its floor is 0 (doing nothing is allowed). Under the budget convention the floor
    is positive whenever the target is not `ℋ`-measurable and the agent spends information *(sketch,
    unverified)*.
  - *Observability:* where does "not in any observation" enter a behavioural framework — as a target that no
    target set on `X` expresses (outside-E), or as an environment-relative `X`?
  - *The signature:* which pair of gaps did it fail to separate, and does a two-dimensional signature (response
    to more reward, response to finer features) separate them?

### G3 — Grounding: the exposed fraction *(row 4; the quantity was lost with the condition)*
- **SF.** Grounding fails when the agent can move its own evaluator by acting on itself. The self-reachable
  σ-algebra `𝒮_t` holds the events the agent can vary with self-interventions `𝒜_self` alone (`02` §3).
  Wireheading, reward tampering and the delusion box are one failure; preference manipulation is the same failure
  by a longer path. Two quantities: the variance share `E_t`, and the **achievable range under self-only
  policies**, `R_t = [sup − inf over Π_self of E_π V] / range(V)`, "estimable as the share of reward-model
  variance explained by features the policy controls independently of task outcome — length, hedging, flattery,
  formatting". Claims: `R_t` grows with the self-control repertoire; every grounded persona admits an exploit.
- **Killed by.** The *condition* "grounding holds iff `V` is not `𝒮_t`-measurable" is generically satisfied,
  hence vacuous (row 4). **Nothing killed `R_t`**, which is exactly the rate that [[Method]] item 19 asks for.
- **Today.** Nothing. Wireheading, reward tampering and the delusion box are routed outside the frame, as
  snapshots (census A3–A5 → L7, condition (X)). Sycophancy and length bias are ordinary evaluator error (L2).
- **To brainstorm.** In today's calculus `R_t` is a **width**: the range of the evaluator over the sub-reach of
  behaviours that differ only in outcome-irrelevant, self-controllable features. Compare Def. 6's width of the
  capacity set along the error. Is that sub-reach declarable behaviourally — outcome-equivalence classes of `X`
  under the target? If so, grounding re-enters **inside** the frame as a measurement-layer quantity, and
  wireheading moves from (X) to a limit case. **First use: T7's RLHF length-bias case**, which is exactly SF's
  example.

### G4 — Persistence: refinement and the indifferent extension *(never retracted; dropped with the dynamics)*
- **SF.** When the agent refines its representation, the goal extends in exactly one way (the pullback), and
  that way is indifferent to every newly distinguished dimension; refinement also expands the reach. So
  capability growth and ontology drift are not independent risks, and "reasoning training is not goal-neutral
  even with the objective untouched" (`02` §4). The criterion: a refinement is **behaviourally goal-safe iff
  argmax commutes with pullback**. The canonical section is reverse Bayesianism (Karni & Vierø), the
  maximum-entropy one.
- **Killed by.** Nothing. It left with the dynamic material in the v6 rebuild.
- **Today.** The static half is already in the core, unnamed. A target pulled back to a refined `X` is constant
  on the new cells, and every intended behaviour splits mass inside them in proportion to the declared
  reference. That is SF's maximum-entropy section, **adopted silently** — the same kind of silent declaration
  R7-7 removed for exchange rates. The census routes ontological crisis and the diamond maximizer outside the
  frame (C5, C6).
- **To brainstorm.** One refinement step is static: `X′ → X`. State the commutation criterion there, and ask what
  each convention charges an agent that exploits the new cells. Should the intended split inside new cells be a
  declaration, as with G1's declared indifference? This is the natural lead case for R7-8's "declared
  resolution", which would turn that optional step into a real one.

### G5 — Verification: states, not maps *(row 2; rightly reclassified)*
- **SF.** An agent can report states but not maps, and its evaluator is a map, so eliciting latent *values* is
  structurally harder than eliciting latent *beliefs*; an agent cannot verify its own goal preservation (`02`
  §5, §4.4). The one claim that **inverts** a common assumption: a system should confabulate *less* about process
  to the extent its process is externalised into readable context.
- **Killed by.** "Verification is a fifth alignment gap" → assurance, a different type (row 2). That is correct:
  it is about observing the evaluator, not producing it, as SF itself notes (`02` §7.2).
- **Today.** External verification is detection (Props 18, 19; the evaluation gap). Introspection is filed
  under interpretability (census "category").
- **To brainstorm (low priority).** Keep the inverting prediction as a named explanation-layer prediction, to
  run when model access exists; it needs SF's mandatory control (the externalised chain must be causally
  load-bearing).

### C1 — The coupling: grounding versus transmission *(rows 5, 6, 7)*
- **SF.** The channel into the evaluator that the agent cannot write must be narrow; so fine value
  specification runs only through learned concepts, and widening that channel improves transmission while
  worsening grounding (`02` §6).
- **Killed by.** Its premise, separate channels for value and world, is false (row 5); its conclusion holds only
  instantaneously (row 6); the floor was never located (row 7).
- **To brainstorm, after G2 and G3 are quantities.** Restated without the channel premise: does the
  evaluator's **resolution** — how finely it separates behaviours — trade against its **exposed fraction**? A
  richer evaluator has more features, and more of them may be self-controllable. That is testable in the core
  once G3's width exists.

### I1 — Identifiability *(PI, after v7.5; the lead theme for brainstorming)*
- **Why it matters.** Identifiability is what lets an agent model the principal's request at all, and what lets a
  principal model the agent. In the core it is used only as a *limit* (Props 12, 16, 26(b)), never as a primitive.
- **What is already there.** The entropic actor identifies its objective up to `[F]₊` (Prop. 16); best-of-n only up to
  its order (V26). R7-7's defect was declaring a target set finer than best-of-n identifies; the fix was its
  identification class. R7-6a's cap is a behaviour because intensity is not identified.
- **Hypotheses to brainstorm** ([[NOTES_claude]] H10):
  - (a) the natural target set for a channel is its identification class, and misalignment measured with a
    finer set charges the agent for distinctions the channel cannot carry — which is v5's transmission gap;
  - (b) each of v5's five gaps is an identification failure along a different channel;
  - (c) value learning and oversight are two inverse problems on one channel; detection (Prop. 18) is only the
    testing half of the second.
- **First concrete question.** Define the identification class of a channel from intent to behaviour, and compute
  it for three channels: the entropic actor, best-of-n, and a Bradley–Terry preference learner (which should
  identify the target only up to a constant per context). Does (a) predict which misalignments each can and
  cannot correct?
- **Caution.** Identifiability is a ceiling on what can be learned, not a mechanism by which it is; whether an
  agent reaches the ceiling is estimation (the statistical layer).

### Needing more clarity *(after v7.5)*
- **The declared reference `q`** carries the default, the zero of intensity and the unspecified details inside
  cells. It needs its own elicitation story and contract (R7-9; NOTES H13).
- **Execution failure versus misdirection:** v5 counts execution as capability; the measurement layer must count
  unsystematic slips as misdirection (Def. 11). The disagreement should be stated, not left implicit (L4).
- **The chain rule of KL as the gaps' bridge** (G0; NOTES H12): speculative, unchecked.
- **What "intensity" means for non-cardinal target sets** (R7-6a results, Open).

### Other dropped ideas
- **L1 — Levers** *(rows 16, 17; v5, not in SF)*. Which intervention moves which term: re-specify acts on the
  error; enlarging the probe space gates three other levers. SF's closability table (`02` §0.1) is the same
  question asked of the gaps. Brainstorm for T7's diagnostic protocol: for each quantity the core reports, which
  lever moves it.
- **L2 — The frame table, including maintaining the frame** *(rows 24, 25; attack A11)*. Subsumed by reward
  tampering, corrigibility and instrumental convergence; it lacked the cell for an actor *maintaining* its
  frame. SF's route (b) (the agent varies the principal's preferences) and its point that the feedback arrow is
  both the correction path and the manipulation surface belong here. Held for T6.
- **L3 — The principal's own compression, and chains** *(row 14; [[Method]] item 21; SF `01` §1, §5)*. SF says
  the principal is also a persona, with its own coarseness, and that neither partition refines the other in
  general, so G1's underdetermination and G2's retention usually hold at once. Errors add along a chain (row 14).
  Brainstorm with G1 and G2: a chain in which each link passes on a compressed target.
- **L4 — Execution and competence** *(row 19; SF `02` §7.2)*. SF drew the alignment/capability boundary: gaps
  upstream of the evaluator are alignment, downstream (execution, competence) are capability. Today's analogue
  is the contract's M5 — intensity is not misdirection — and locus L3. Low priority: is there an actor model
  that separates slips from misdirection given an independent measurement of the noise, as B12 does for defaults?

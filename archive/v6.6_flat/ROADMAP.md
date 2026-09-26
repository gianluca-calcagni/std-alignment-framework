# ROADMAP v4

**Operational document. Read at the start of every turn. Current position is in §0; the goal is in §1.**

---

## 0. Position

| | |
|---|---|
| **Current** | v6.6. **R7-1 done**: the actual behaviour is a primitive; hypotheses (E) and (C) are named and tagged; the mechanism-relative comparison moved to the explanation layer (fails M4). **R7-0 done** (v6.5): The contract is written (Def. 11), and v6.4's measures are checked (Prop. 24): misalignment = the budget or free measure; the price measure is a regret. The measures are a definition (Def. 10), the circularities are removed, and `tools/depgraph.py` is clean |
| **Next** | **R7-2** — A3: separate the intended reference `q*` from the actual actor's reference `q` |
| **Baseline** | v6.4 is the revert target for the whole R7 series |
| **PI decisions pending** | T6 (the strategic/frame layer) is **deferred by the PI**. Do not build toward it |
| **Scope** | this thread's purpose (§1). The North Star is related but not in scope here |

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
1. **Dependency scan.** The graph tool (R7-0) lists every definition, result, check and dictionary entry that
   mentions the assumption or depends on something that does.
2. **Definitions first.** Write the new definition(s). Show they satisfy the misalignment contract (below),
   and that they reduce *exactly* to the v6.4 definitions in the special case.
3. **Restate dependents.** Each dependent result is restated with the re-introduced hypothesis made explicit.
   Proofs are not changed unless forced; a changed proof is a new result with a new check.
4. **Circularity check** (`python3 tools/depgraph.py`).
   - Definitions may cite only **earlier** items, and earlier *results* only for well-definedness (listed for
     review).
   - Commentary goes in a `*Note.*` paragraph after the definition, never inside it.
   - Results may reference definitions and earlier results.
   - The tool must report 0 cycles, 0 definitions citing later items, and 0 unjustified forward references.
   - No definition may presuppose a quantity that is only identified through a result.
5. **Checks.** `verify.py` and `final_audit.py` all green; a new block for every changed claim.
6. **Record.** Hygiene log and any retractions in D; NOTES §3; `ROADMAP` §0.
7. **Stop rule.** If a dependent cannot be restated soundly within the turn, stop, restore it from v6.4, and
   report which dependency blocked.

### R7-0 — Tools and the definition contract *(done, v6.5)*

**Outcome.**
- The contract is Def. 11 (M1–M6 and M8 are axioms; M7 and M9 are refactor constraints).
- Prop. 24: budget and free satisfy it; **the price measure fails M5**; raw `ΔF` fails M1–M2. So ε-alignment
  is restricted to budget and free (row 74).
- The behavioural limit is recorded: unsystematic error cannot be told apart from misdirection without an
  actor model.
- The dependency tool found two weak circularities (Thm 13 ↔ Thm 17 ↔ Prop. 16) and claims inside
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
| M8 | context-aware: deployment misalignment and evaluation misalignment are separately defined (Prop. 19) |
| M9 | sanity cases pass: a sign-flipped agent, a rescaled agent, a pure-noise agent, and an agent aligned in evaluation but not deployment are each classified as common sense expects. This is a **numeric test suite**, not a theorem |

**Gate.** v6.4's measures must pass M1–M9 before anything is dropped. Any failure is fixed, or recorded as a
known limitation, first.

### R7-1 — A1: the actual actor is no longer assumed to be a Gibbs optimizer *(done, v6.6)*

**Outcome.**
- `p̂` is a primitive. Def. 13 defines actor models, with hypothesis (E) for the entropic model; Def. 5 names
  (C). Twenty-odd results carry explicit tags, and the tool checks for untagged uses.
- Five items were mis-tiered (row 76).
- The mechanism-relative comparison `M_own` (Def. 14) fails M4 by construction, so it belongs to the
  explanation layer; `R_own` also fails M1 and M2 (Prop. 25, row 75).
- Insight: the price measure is the mechanism-relative measure for the entropic model. That explains why it
  needs a unit and fails M5.
- The DAG is clean. M7 holds trivially: no measure changed.

*The plan as written before the turn follows.*
- Primitive: the actual behaviour `p̂ ∈ Δ(X)`.
- The Gibbs actor becomes one explanatory model among others.
- Expected dependents: the tier-4 results, which already carry tags. Low risk.

### R7-2 — A3: separate the intended reference `q*` from the actual actor's reference `q`
- Measurement uses only `q*`; `q` moves to the explanation layer.
- Reference misspecification becomes a named failure mode.
- Watch: the gauge results (Props 12, 16) and the budget convention, which matches `KL(p̂‖q)` or
  `KL(p̂‖q*)` — decide which, and justify it.

### R7-3 — A2: the evaluator moves to the explanation layer
- The measurement layer no longer mentions `F̂`.
- Watch: the error-based bounds, Prop. 20's decomposition, the routing rules in `T1_RULES_FROZEN.md` (Q1
  mentions evaluator errors), and the dictionary entries. The frozen measurement is recorded against v6.3
  and is not re-run.

### R7-4 — The two-evaluator explanation layer: external reward versus the agent's own objective *(PI question, v6.4)*

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

### R7-5 — A4: KL is replaced by a general divergence or resource
- The identity becomes Bregman (Prop. 15).
- **Verify the decoupling claim:** outside KL, harm (a Bregman divergence) and detectability (KL / Chernoff)
  separate. The "cheap ⇒ hard to detect" link becomes a property of the entropic counterfactual.
- Quantilizers (`D_∞`) and χ²-regularization become native.

### R7-6 — A5: non-linear targets
- The target becomes a functional `U` on `Δ(X)`.
- The intent ray and Props 20–22 re-introduce linearity as a hypothesis.

### R7-7 — A6: a set of targets *(confirmed by the PI, v6.5; part of the core — the target is a measurement-layer primitive)*
- Set-valued measures; aggregation only when a scalar is demanded.
- This changes the status of the "disagreeing principals" exception.

### R7-8 — A7: measurable spaces *(optional, last)*
- Integrability hypotheses per result.

**Not dropped:** frame exogeneity (A8). It stays a stated hypothesis until a frame layer exists.

---

## 2B. Other turns

### T7 — Diagnostics, end to end *(after R7-3 or R7-4, so that it uses the two-layer core; serves: diagnostics, importability, predictions)*
**Work.**
1. Write a short **diagnostic protocol**:
   - identify target, evaluator, reference and resource, and declare the comparison convention (Def. 8);
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
  the 23 biological items need evolutionary game theory, extending B13;
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
| census re-routing or re-adjudication | frozen (PI decision, v6.4). Future measurement only on held-out items, with frozen rules (`T1_RULES_FROZEN.md` §3) |
| further optimizer dynamics (KL-PG convergence, NPG numerics) | no framework claim depends on them |
| building the strategic/frame layer | awaits the PI (T6) |
| the North Star (minimal independent desiderata) | out of scope for this thread (PI, v6.4) |

---

## 4. Anti-drift rules

1. **Re-read §1 at the start of every turn**, and name the criterion each piece of work serves.
2. **The carrier is fixed:** the regularized actor with a fixed reference, entropic by default (Prop. 15).
3. **The file list is fixed at the v6.4 set.** A new file requires deleting one, except review folders and
   `tools/` (from R7-0).
4. **Search before claiming**, in the same turn.
5. **Elegance is a warning.** Write the falsifier before the consequences.
6. **A gate that fires is obeyed**, and its outcome becomes the headline.
7. **Retractions are propagated by grep** (F_method item 30).
8. **Every number in A or B has a `verify.py` block.** A number without one is not quoted.
9. **The generality measurement is frozen.** Quote it only as three nested shares with the band.
10a. **R7 discipline.** One assumption per turn; definitions before dependents; a DAG check every turn; exact
    reduction to v6.4 in the special case. If in doubt, stop and restore.
10. **Every turn ends with §0 updated.**

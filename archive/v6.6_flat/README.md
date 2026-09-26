# Alignment as the tilt of an error by a bounded actor — v6.6 (R7-1)

**Read `D_status.md` before quoting anything.**

## What this is

**A verified calculus for one module of alignment — not yet a general theory.**

An actor pursues an objective slightly different from a designated target, and trades value against the
information cost of departing from a default behaviour. The same statement applies to a trained model, an
institution, a person, or an organism. What differs by substrate is whether value has a measurable unit, and
whether the default can be measured (`A_core.md` §10).

**How general it is — measured, adjudicated and frozen (v6.4, `T1_RULES_FROZEN.md`).** Three raters routed 221
catalogued alignment phenomena; a third adjudicated the disputes. The core:
- **names** 78 % of them;
- is **specific** about **55–61 %**;
- treats **29 % fully**.

These are nested shares, not a pass or fail: the specific share sits on the pre-registered threshold. The
missing layers are strategic interaction (51 items), statistical/learning (31), frame endogeneity (23) and
dynamics (20). Justified exceptions are 31: no single target (e.g. disagreeing principals), or
internals-only questions.

**The module covers:**
- a single target, in a static setting, with an exogenous frame;
- **any actual actor** for the central identity, the decomposition, the regret curve and the detection cap
  (tier 1, against a Gibbs intended actor); no overoptimization under an affine regression (Prop. 21);
- exact maximizers for the capacity bounds (tier 2), and argmax selectors compared at equal budget
  (tier 2′, Prop. 23);
- which predictions transfer beyond the Gibbs actor was tested in R5 and R6 (`C_boundary.md` C7);
- i.i.d. observation;
- rational-inattention humans;
- potential games.

**The v6 core in one sentence:** the loss in nats from pursuing the wrong objective **equals** the
divergence between actual and intended behaviour, `β·R_J = KL(p̂‖p*)`. Read at different capacities, that
one object gives:

- variance-dominated harm at small capacity and extremes-dominated harm at large capacity, so no
  capacity-free ranking of errors (Thm 9);
- a regularizer that fixes which norm of the error must be controlled — KL needs exponential moments, χ²
  a variance (Props 10, 11);
- an exact split into error along the intent and error across it, only the latter free of unit conventions
  (Thm 13); all regret notions lie on one convex curve, and the counterfactual must be declared (Thm 17);
- a Bregman-divergence version for any convex regularizer and concave target (Prop. 15);
- a bound on detection: no behavioural test beats the regret in nats (Prop. 18); evaluation gaming is the
  evaluation gap `Γ` (Prop. 19).

**Nothing in the core is new mathematics, and most results are known individually.** The prior-art check
(C14) found the package to be predominantly an **index**: known results, derived inside one calculus, with
proofs and checks. That is the intended role of a standard framework. Nine dictionary entries are derived
rather than asserted (`B_dictionary.md`).

## Files

| File | Contents | |
|---|---|---|
| `A_core.md` | definitions, theorems, proofs, what the core forbids, scope | start here |
| `B_dictionary.md` | other literatures read through the core: derived / stated / does not translate | the substance |
| `C_boundary.md` | attack surface C1–C14, what is outside and why, untested extensions | **start here if attacking** |
| `D_status.md` | claim ledger, seventy-three retractions, hygiene log, honest position | before quoting |
| `E_census.md` | 221 alignment problems across four substrates — frozen test set | reference |
| `F_method.md` | working rules, each earned from a failure (§5 added in v6) | reference |
| `ROADMAP.md` | the next five turns and their gates | operational |
| `NOTES_claude.md` | the executor's personal notes: failure modes, load-bearing insights, ranked hunches, start-of-turn checklist | private |
| `verify.py`, `verify_output.txt` | reproduces every number in A and B; blocks `V1`–`V29` | `python3 verify.py` |

## What changed from v5

v5's central product bound `R_J ≤ osc(E)·√(2δ)` is replaced by an identity and by the exact worst case (the
width of the capacity set). The v5 capacity-ball version was invalid under two of its three readings and
vacuous under the third.

Also retracted in v6:

- separability-by-capacity;
- the Ashby reconciliation (it survives only in a closed-loop extension);
- the Holmström derivation (its condition was wrong);
- `e*(τ) ∝ τ` (a proportional-control artifact);
- "rescaling is harmless" — itself partly reversed in v6.3: it holds under the default (budget) convention
  and fails only under the price convention (Remark 13.5, row 61);
- the claim that `β` is a system property in every substrate.

`D_status.md` §2, rows 31–51 (v6), 52–57 (v6.1), 58–60 (v6.2), 61–66 (v6.3) and 67–73 (v6.4).

## If you are here to break it

`C_boundary.md` §6 ranks the targets.

- The algebra is checked by hand and by `verify.py`; attacking it is low-yield.
- The weakest joint for the AI substrate is **C7**, now a corrected tier map. The identity is tier 1 in the
  actual actor; the capacity bounds need exact maximizers; the rest is Gibbs-specific. The crossing
  transfers, but its location does not.
- **C14** (does this already exist?) is answered: predominantly an index.
- **Generality is measured and frozen** (`T1_RULES_FROZEN.md`). The open work is to build the missing layers,
  which awaits the PI's decision on T6, and to show the framework diagnosing real cases (`ROADMAP.md` T7).

## Added in R7-1 (v6.6)

| Item | Contents |
|---|---|
| A Def. 13; hypotheses (E), (C) | actor models are explanations. The actual behaviour is any distribution, and every result that needs the entropic or capacity model says so |
| A Def. 14, Prop. 25; `V31` | the mechanism-relative comparison (the same algorithm run on the target with the same resource): an engineering quantity that fails M4, not a misalignment measure |

## Added in R7-0 (v6.5), the first step of the refactor

| File or item | Contents |
|---|---|
| `tools/depgraph.py`, `tools/depgraph_report.txt` | the dependency graph of every numbered item: cycles, forward references, and per-assumption dependents. Run every R7 turn |
| A Def. 10, Def. 11, Prop. 24, Def. 12 | the measures as a definition; the misalignment contract; the measures checked against it (**misalignment = budget or free measure; the price measure is a regret**); the formal alignment instance |

## Added in review R6 (v6.4)

| File | Contents |
|---|---|
| `R6_LOG.md` | the refocus on the goal, dispositions of the third review, and what was applied or not, with reasons |
| `T1_RULES_FROZEN.md` | the frozen generality result (three nested shares), the eight routing rulings, and how to measure again on held-out items |
| `t1/adjudicated_routing.py` | the final 221-item codes |
| `reviews/R6_independent/` | the third reviewer's files: message, transfer-test results, hashed blind routing and adjudication, test code and logs |

## Added in review R5 (v6.3)

| File | Contents |
|---|---|
| `R5_LOG.md` | feedback on the independent review, and what was applied or not, with reasons |
| `reviews/R5_independent/` | the independent reviewer's files: blind routing, agreement analysis, tier-4 transfer tests and their pre-registration |
| `t1/reviewer_routing_R5.py` | the second routing, used by `t1/make_report.py` to compute `T1_census_routing.md` §9 |

## Added in review R4 (v6.2)

| File | Contents |
|---|---|
| `R4_LOG.md` | the answer to the PI's generality question; dispositions of every point in the previous executor's two messages; errors caught |
| `T1_preregistration.md` | categories, predictions and decision rule, written before routing |
| `T1_census_routing.md` | the routing of all 221 census items, with counts, hard cases and robustness |
| `t1/` | routing data and analysis scripts |
| `MSG_1_findings.md`, `MSG_2_steering.md` | the previous executor's review of v6.1 |

## Added in review R3 (v6.1)

`R3_FIX_LOG.md` lists every R3 recommendation, whether it was applied, where, and — for those not applied —
why.

| File | Contents |
|---|---|
| `R3_FIX_LOG.md` | what was applied from review R3, what was not, and why |
| `MESSAGE_to_previous_executor.md` | review R3, written against v6: prior art, a formal-completeness audit, derivations, what is missing, a recommended architecture |
| `REFERENCES.md` | every source cited in the package and in the message, with status codes; includes the census's own attributions, item by item |
| `references.bib` | BibTeX for the non-census references |
| `final_audit.py`, `final_audit_output.txt` | independent audit: closed forms vs a generic optimizer, exact finite-`n` detection, a unit (scale-covariance) check, edge cases, cross-references |
| `verify_addendum.py`, `verify_addendum_output.txt` | checks `W1`–`W5` for the message; superseded by `verify.py` V12–V17, kept as the record of what R3 checked |

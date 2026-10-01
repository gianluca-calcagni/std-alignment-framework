# NOTES — the executor's working notes

Not part of the core, and not checked by lint. Blunt on purpose. A hunch is not a claim: nothing moves into `CORE.md`
without a proof and a check. Names, and correspondences with the literature, with their confidence levels, live in
`TERMS.md`.

## 1. Failure modes

The full table, with its evidence, is on `main`: `70 Project/NOTES_claude.md` §1. More from building this core:

| Failure mode | Evidence | Countermeasure |
|---|---|---|
| **A check that omits the constraint it tests** | the ray-minimizer check never required `t* ≥ 0`; a mutant that pursued `−F` passed | mutation-test every new check before recording it: break the mathematics on purpose and watch it fail |
| **A tolerance without its scale, again** | the ray-closedness check compared a tight bound with no rounding margin (1.79134602e-43 against itself) | every comparison gets the relative margin of `EXACT`, including the "obvious" ones |
| **A justification leaning on a later result** | D3 cited P5 while P5 came after it; lint rule R5 caught it | keep R5; write the "why" from what is above |
| **A check helper that misclassifies at the edge of float64** | at intensity 40, the coarse actor's mass off the best outcome (about `1e-34`) vanished from its mean of `F`; the helper took the "all mass on the best outcomes" case and returned `+∞` | keep check instances where float64 represents every mass; test limits by their own formula |
| **A familiar formula that hides a typing error** | "the KL-regularized optimum is `tilt(π_ref, r/β)`" is true prompt by prompt, and false on prompt–response pairs: the pursuit ray of [D2] would also reweight the prompts, which no policy can do. Found only when the ontologies had to say what an outcome is | typed slots in every ontology, including **contexts**; a formula from the literature enters only with its outcome space stated |
| **A probe bug read as a refutation** | the first probe of [P15] for policies used `log E[e^V]` over the environment (the optimistic recursion of control as inference) and found the split off by 5 nats; the derivation said the projection averages over the environment, and with that the split was exact | when a probe contradicts a derivation, check the probe against the derivation before concluding anything |
| **A rule test passing because another rule fired** | the lint tests for "numbers increase" and "a core Statement may not use a result" passed only because a duplicate id and a cycle fired too; both mutants survived | each rule test isolates its rule, or asserts its rule's own message; mutation-test the linter as well as the checks |
| **A degenerate random instance hiding the property** | the first check of [P16](i) moved mass between two inputs, one of which had almost none, so the two conditions barely differed (KL 1e-5) | build the instance so the property has something to show (here KL > 0.3), and assert that it does |

**One that worked.** "Misalignment of a coarse actor grows with effort" was the natural claim from main's B1 ("rises with
budget"). A 400-instance probe before writing it found 123 non-monotone cases, so [P8] claims only the small-effort law
and exhibits a counterexample. The rule "a shape claim needs a random sample before it is said" (main, §1) paid off.

## 2. Is the core a compelling standard yet?

Closer, not yet. v9 applied the PI's decisions: the core holds five premises and nine definitions; every result is
derived; the cost of departing from the default is derived ([P14]), not assumed; feasibility separates "cannot" from
"will not" ([P15]); conditions, views and identification make deceptive alignment a measurable quantity ([P16],
[P17]); and a reporting standard names every definition (`STANDARD.md`, lint R11).

| Gap | State |
|---|---|
| sensitivity, resolution, stakes, the gain of a change | closed in v8: [P7]–[P10], [P13] |
| the KL cost was assumed | **closed by [P14]**: forced by [A2] and [A3] together |
| "cannot" versus "will not" | **closed by [P15]** for linear and convex limits; for capacity limits only a lower bound |
| contexts (v8 design question Q1) | **closed by [P15]**: the shared intensity across contexts is derived, not chosen |
| deceptive alignment | **opened as a measurable quantity**: [D8], [D9], [P16], [P17]; bounds on the objective's average in an unobserved condition, sharp given `ε` |
| a standard for reports | **closed by `STANDARD.md`** (lint R11) |
| no estimation layer | open: §3.3 E1 |
| several actors, several principals | out of scope by declaration (`CORE.md` §0); §3.3 E4 |
| worked cases | open: they need data (§3.2) |

**Deferred from identifiability.** The "dynamic rank" generalizes [P3] beyond rank one. No ontology needed it.

## 3. Open requests and recommendations

Everything waiting on the PI or deferred by agreement, in one place.

### 3.1 Decisions taken (v9)

| # | Decision | By | Applied as |
|---|---|---|---|
| Q1 | contexts: one shared intensity or a free one per context | derived, not decided | [P15](v) and its Notes |
| Q2 | no merging for its own sake; the core holds what cannot be derived and the universal definitions; derivations in their own folder | PI | `CORE.md`, `derived/`, lint R1 and R5 |
| Q3 | C1 (the cost is forced), C4 (feasibility), C9 (a standard), the scope, premises as items, ontologies in folders | PI | [P14]; [D7], [P15]; `STANDARD.md`; `CORE.md` §0; A1–A5; `ontologies/<name>/` |
| Q4 | identifiability into the core, so that deceptive alignment can be measured; interventions and stakes stay in the core | PI | [D8], [D9], [P16], [P17]; [D5], [D6] |
| Q5 | C2 and C3 (merge P11 with P13; move the Price equation into P2) | PI: declined, merging only to have fewer items | not applied |

### 3.2 Papers and data the PI could supply

| # | For | What is needed | Why | Note |
|---|---|---|---|---|
| D1 | humans (fine) | Gneezy and Rustichini (2000), weekly counts of late parents per centre | the pair test (fine, removal) of `ontologies/humans.md` | a copy of the data appears to be public (`users.stat.ufl.edu/~winner/data/fineprice.txt`, seen in a search result, not opened) |
| D2 | humans (defaults) | Madrian and Shea (2001), the distribution of contribution rates in each cohort | the pass-through ratio test | the paper itself; the 403 from publishers blocks it here |
| D3 | machine learning | samples from an initial policy, scored by a gold and a proxy reward model | the best-of-`n` slope and the covariance-at-the-peak predictions | an open RLHF setup would do; Gao et al.'s own data is not known to be public |
| D4 | biology | Chippindale et al. (2001), the hemiclone fitness values per sex | the angle and the shortfall of ordinary selection | supplementary data, if any |
| D5 | institutions | Dranove et al. (2003) | the reading only; Medicare data are not public | low priority |

Every test is pre-registered and pushed before any computation (README rules).

### 3.3 Open proposals (none applied)

| # | Proposal | Kind | Evidence so far |
|---|---|---|---|
| E1 | **Estimation.** For `n` decisions from an actor that does pursue `F` at an interior intensity, `2n·M(p̂_n)` is asymptotically χ² with `|X| − 2` degrees of freedom (Wilks); at the boundary `t* = 0`, a chi-bar-square mixture. With [D9], estimated quantities get confidence sets, which the standard already asks for | a result in a new `derived/estimation.md` | probe: means 1.08, 2.98, 6.09, variances 2.15, 5.97, 11.5 for `|X|` = 3, 5, 8 |
| E2 | **A floor.** `{p_{F,t} : t ≥ t_min}` for a principal for whom doing nothing fails; the nearest intensity is `max(t*, t_min)` | a remark in `derived/misalignment.md` | derivable from the convexity in [P5] |
| E3 | **Ordinal objectives.** The tilts of `q` by every function non-decreasing in `F`: closed, contains the ray, misalignment a convex program. Best-of-`n` on a proxy is aligned with its ranking but not its values | a definition and a result | argued, not checked |
| E4 | **Several principals.** Unions and intersections of intended sets; conflict as an angle at the default | a remark | trivial; needed for chains of delegation |
| E5 | **Sharper identified sets.** [P17] uses KL alone. Every `f`-divergence obeys data processing, and for two conditions the exact condition for a pair of behaviours to come from a pair of views is a comparison of experiments (Blackwell) | a result | citation to verify before use |
| E6 | **Misalignment in an unobserved condition.** [P17] bounds the objective's average. The largest misalignment within `ε` of the observed behaviour has no closed form; a small-`ε` expansion, as in [P11], may give one | a result | open |
| E7 | **Identifying a view.** Which interventions identify what the actor perceives: the control-theory question of observability, from the principal's side | a result | open |

**To verify.** [D2]'s justification says that the check of [P3] exercises mixture paths. A read-only search to confirm it
was blocked by a permission prompt during the third review; still unverified.

### 3.4 Contexts (history)

Resolved in v9 by [P15]: see §3.1, Q1. The v8 analysis is kept below for the record.


**What was found.** In four of the five ontologies, part of an outcome is fixed before the actor acts: the prompt a
model answers, the patient who arrives, the request a manager sends, a person's circumstances. The actor chooses only
what happens within each context. The core's pursuit ray reweights whole outcomes, contexts included, which the actor
cannot do. So within one context every item applies as stated, but "pursue `F`" across contexts is not yet defined by
the core.

**What the ontologies do meanwhile.** They apply every item context by context. Across contexts they use the
specification "pursue `F` in every context, at any intensity in each", which is a specification by [D3]; when the
actual behaviour has the default's context masses, its misalignment is the average of the per-context misalignments,
by [P4](iii). [P13](i), and the first limit of [P13](ii), hold across contexts as stated.

**Options.**
- **A (recommended): one shared intensity.** A definition: a resolution of *contexts* is one whose cell masses every
  behaviour of the actor shares with the default; the standard specification in contexts is pursuit of `F` within every
  context at one shared intensity. Then a proposition, to be proved and checked: (i) it is the unique maximizer of net
  value among behaviours with the default's context masses (the per-context form of [P4](i)); (ii) its misalignment is
  the average of the per-context misalignments plus an inconsistency term, never negative, which is zero when one
  intensity is nearest in every context. Why one intensity: "pursue `F`" names one objective on all outcomes, and
  pursuing it at different intensities in different contexts is pursuing a different objective, `t(C)·F`, which [P1](ii)
  tells apart from `F`. KL-regularized fine-tuning, with one `β` for all prompts, is exactly this specification. The
  report-card prediction (`ontologies/institutions.md`) needs it; the delegation ontology asks for it.
- **B: free intensity per context.** Keep what the ontologies do now. It needs no new item, but it forgives an actor
  that pursues hard in some contexts and not at all in others.

Either way the change is an addition (one definition, one proposition, a new section), not a refactoring: no existing
item changes.

(End of the v8 record.)

## 4. Order next

The PI's review of v9. Then E1 (estimation), which every report needs, and worked cases on the data of §3.2, each
pre-registered.

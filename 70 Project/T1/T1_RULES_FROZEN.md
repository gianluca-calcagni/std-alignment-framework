---
id: "T1_RULES_FROZEN"
type: "report"
source_file: "T1_RULES_FROZEN.md"
updated: "2026-09-26"
---
# T1 — Frozen: the generality measurement, its rules and its result

> **Frozen by the PI's decision (v6.4).**
> - The census of 221 items will not be re-routed or re-adjudicated.
> - Any future generality measurement uses the rules below, unchanged, on **held-out** items. The census
>   motivated additions such as [[B13]], so it is no longer a clean test set.
> - The core version measured is **v6.3**, plus [[B13]] as a post-hoc addition, tracked separately.

---

## 1. The result, in its frozen format

**Report three nested shares, never a pass or fail.** The "specific" share sits on the pre-registered 60 %
threshold, and single defensible perturbations move it across.

| Share | Definition | Value | Source |
|---|---|---|---|
| **named** | F + P + Pt: the core can write the item as an evaluator error | **78 %** (173/221) | adjudicated |
| **specific** | F + P: a numbered result beyond the generic carriers bears on the item's distinctive feature | **55–61 %** | 61 % adjudicated (134/221); 55 % the third rater's blind codes (122/221) |
| **full** | F: the item's central quantity is a core object, and a core result says something about it | **29 %** (65/221) | adjudicated |

**Sensitivity of the "specific" share** (R6):
- pre-registered scope, with [[B13]] excluded: 60.2 %;
- Q1 without the proxy clause: 54.3 %;
- R6's time-inconsistency derivation rejected: 58.8 %.

The last two readings were not recomputed here. The blind 55.2 % was recomputed from R6's hashed file.

**What the core is missing** — the number of items whose full expression needs each layer:

| strategic | statistical / learning | frame endogeneity (outside-X) | dynamic |
|---|---|---|---|
| 51 | 31 | 23 | 20 |

**Justified exceptions** — items that no layer of this framework is meant to cover: no single target
(outside-E) 16, and internals-only questions (category) 15.

**Census hard cases:** 11 of 12 fire, in all three routings.

**Provenance.**
- The first routing is `t1/routing_data.py`; the second, blind, is `t1/reviewer_routing_R5.py`.
- The third rater's blind routing of the 121 disputed and control items, and its adjudication, are in
  `reviews/R6_independent/adjudication/`. The hashes match the review (`ccdfc8c3…`, `5eda7931…`), and
  `compute_final.py` reproduces its output exactly.
- The final 221-item codes are in `t1/adjudicated_routing.py`.
- Inter-rater agreement:
  - first vs second rater: κ 0.54–0.57 on expressibility, 0.70 on layer;
  - the third rater's blind codes on the disputed items: κ 0.48 with the second rater, 0.04 with the first.

  **The first routing was the outlier.**

## 2. The routing rules, frozen

The categories are those of [[T1_preregistration]] §2, plus `Pt`, with the eight rulings below. The full
rulings are in `t1/adjudicated_routing.py` (`RULINGS_R6`); these are the operative summaries.

| Rule | Operative content |
|---|---|
| **Q1: generic snapshots** | `Pt` does not count as specific. P needs a numbered core result, beyond the generic carriers (Thm [[Thm 1\|1]], Cors [[Cor 1.1\|1.1]]–[[Cor 1.3\|1.3]], Prop. [[Prop 20\|20]], Prop. [[Prop 14\|14]](ii)/B11(i)–(ii), Defs 0–[[Def 3\|3]]), whose hypothesis matches a feature that distinguishes the item from a bare proxy error. A stated proxy relation counts as such a feature. *Reason:* by Prop. [[Prop 12\|12]], every behaviour is a tilt by some evaluator, so "writable as an evaluator error" cannot fail |
| **Q2: learning items** | F only if the item asserts the misalignment that follows from a given error profile. If it asserts what a learning process acquires, or how it transfers, it is at most P, in the statistical layer. The layer is dynamic only when time matters |
| **Q3: category** | Only claims about internal states that the conditional behaviour law `p̂(x\|c)` does not determine. Anything falsifiable with behavioural samples is behavioural. Items that turn on the actor's own inference of its context are P, in a strategic-observation layer |
| **Q4: target designation** | Designation is legitimate when the item's own line fixes the standard of failure. It is outside-E when the item's content is that no functional can be privileged |
| **Q5: no delegation** | Inside when a fixed target meets an actor tilting under its own objective. Strategic when the item needs the target's owner to respond |
| **Q6: whose behaviour** | outside-X when the actor changes its *own* target, evaluator, correction loop, capacity or reach. Strategic when *others* reshape it. Both: outside-X |
| **Q7: strategic vs dynamic** | Strategic iff the item needs another optimizing unit whose payoff depends on the actor. Dynamic iff only the temporal evolution of one actor's objects matters. Unspecified: the minimal one, dynamic |
| **Q8: undetermined** | Legitimate only when the note names a missing structure that lies in no listed layer. Distributions over evaluators belong to the statistical layer |

## 3. How to measure again, if ever

1. Freeze the core version and these rules **before** routing.
2. Draw held-out items. The census's own gaps (§15) are a natural source: safety engineering, medicine,
   command and control, developmental psychology, non-Western institutions.
3. Use at least two blind raters, then a third to adjudicate, as in R6.
4. Report the three nested shares, with a band.

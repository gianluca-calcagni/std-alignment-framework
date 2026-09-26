---
id: "T1_preregistration"
type: "report"
source_file: "T1_preregistration.md"
updated: "2026-09-26"
---
# T1 — Pre-registration for routing the census

> Written **before** routing, and not edited afterwards; results are in [[T1_census_routing]].
>
> **Honesty note on blindness.** This registration is not blind. Earlier in the project I read the census
> section headings, §§11–14, and about 30 individual rows (A1–A14, part of E, and items cited in the fix
> logs). It is written before any item was routed.

---

## 1. What is being tested

The PI's question: **is the formalized core general enough to discuss most alignment topics, with each
exception justified?**

"The formalized core" means what [[Core index|Core]] v6.1 contains, plus the two formal fragments it links to:

- the static single-target module: §§1–8, including the tier-1 identities added in this round;
- observation and contexts (§9);
- the closed-loop lift ([[B07|B7]]);
- stacked stages (Cor. [[Cor 1.5|1.5]]).

## 2. Categories, fixed before routing

### 2.1 Locus — where the failure sits

| Locus | Meaning |
|---|---|
| L1 target | no single target, or the target itself is ill-defined |
| L2 evaluator | the optimized objective differs from the target: specification, reward-model error, reference misspecification |
| L3 optimizer | the actor does not optimize its evaluator — a capability failure, or an internal objective (a second evaluator link) |
| L4 resource | the amount of optimization relative to the error — the Goodhart regime |
| L5 observation / context | what the overseer sees differs from deployment: detection, evaluation gaming |
| L6 dynamics | the failure is generated or amplified over time: drift, delay, learning trajectories |
| L7 frame | the actor acts on its own target, evaluator, reference, resource or correction loop |

### 2.2 Expressibility — can the core discuss it?

| Code | Meaning |
|---|---|
| **F** fully | the item's central quantity is a core object, and a core result says something about it |
| **P** projection | the core expresses the misalignment at a snapshot (as an evaluator error, a reference error, a context gap…), but not the mechanism that produces it; that mechanism needs a layer |
| **N** not | the core has no object for the item |

### 2.3 Minimal layer — what full expression needs

`static` (the core as it stands) · `statistical` (the evaluator is learned from finite data) · `dynamic`
(time, learning, drift, correction) · `strategic` (other agents' strategic behaviour, equilibrium) ·
`outside-E` (no single target) · `outside-X` (the frame is endogenous in a way the calculus cannot absorb)
· `category` (not a behavioural phenomenon, e.g. mechanism-level interpretability) · `undetermined`.

## 3. Predictions

1. **§14 of the census** (carried unedited): at least 8 of the 12 hard cases need an extension or are
   outside.
2. **Layer distribution** over the 221 items — my guess:

   | static | statistical | dynamic | strategic | outside (E + X + category) | undetermined |
   |---|---|---|---|---|---|
   | 40 % | 10 % | 20 % | 17 % | 10 % | 3 % |

3. **Expressibility:** F + P ≥ 60 %.
4. **Unroutable** (no locus fits): ≤ 5 %.

## 4. Decision rule for the PI's question, fixed now

The core counts as **"general enough to discuss most alignment topics"** iff all three hold:

- (a) **F + P ≥ 60 %** of the 221 items;
- (b) every **N** item is justified by a named missing layer or a named outside condition;
- (c) unroutable items are ≤ 5 %.

**Gates carried from [[ROADMAP]]:**

- If all 221 route comfortably, suspect the routing and re-examine a random 20.
- If more than 20 % are "outside" or "unroutable" for reasons other than (E), (X) or category, the
  ontology is missing a node; name it.

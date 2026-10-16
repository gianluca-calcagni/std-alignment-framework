# v14, a draft: the core reworked so that its words mean what they say

> **Status: a working draft on the branch `claude/core-v14`, started at the PI's request (Q59). Nothing here is
> approved, and nothing here replaces `CORE.md` or `derived/` yet.** It gathers what the label test L1, the general
> core and the discussion of `NOTES.md` §22 taught, adds constraints as a concept of the core, as the PI asked, and
> proves the first results the new structure rests on. The PI's decisions on R15 and R16 wait until this draft has
> absorbed them (Q59).

## Why a rework

Four findings, each recorded with its evidence in `NOTES.md` §21 and §22:
- *The core defines misalignment through a model of optimization.* v13's standard specification is the pursuit ray, the
  set of optimizers of `F` at a KL price ([D2], [D3]). L1 traced most of its label disagreements to that: best-of-`n`
  by the right objective, and an actor that values better outcomes more steeply, are called misaligned for the shape of
  their reweighting, not for wanting the wrong thing. The PI asked for a core with no optimization in it, in which a
  frozen model's misaligned behaviour can be defined beyond doubt (Q58).
- *The pursuit ray is not convex.* An actor that, at each decision, pursues `F` at intensity `0` or `3`, at random,
  acts acceptably at every decision, yet v13 charges it `0.0546` nats per decision, and [P55]'s test accuses it in 69%
  of records of 400 decisions (`evidence.md`, VE2). Records can hold an actor to the mixtures of what is acceptable,
  never to less.
- *A ranking alone does not support "misaligned".* With a ranking and a reference, an actor is better for every reading
  of the ranking, worse for every reading, or neither; a decoder that always answers at its prompt's 0.9 quantile is
  neither (`order.md`, VO3). The everyday sense of "misaligned", working against what the principal wants, needs an
  absolute standard as well.
- *Constraints were missing.* Some outcomes are unacceptable to the principal whatever else happens: a forbidden
  answer, a rate of harm above a limit, a cost over a budget. Breaking one is plainly misalignment, and v13 had no word
  for it (Q59).

## The files, as the PI decided (Q62)

Three layers, each built only on the ones below it, each with a twin for outcomes that are not finite that states only
what changes there, as `general/transfer.md` does:

| File | Holds | Twin |
|---|---|---|
| `CORE` | behaviours per condition; the request, a list of requirements, each a convex closed set; misalignment as evidence against their intersection, with a verdict per requirement; records and bets | `CORE_GENERAL` |
| `INTERFACE` | what the actor sees, what it can do, and how the world turns its actions into outcomes; feasibility, culpability, coarse perception, noise, tampering, collusion | `INTERFACE_GENERAL` |
| `OPTIMIZERS` | objectives, pursuit, the KL price, evaluators, training, shadow prices; gaming, overoptimization, outer and inner misalignment, strategic deception | `OPTIMIZERS_GENERAL` |

Beside them, `LIMITS.md`, what the framework cannot do and what it leaves out. The proposal below predates the layers
(Q59–Q61, `NOTES.md` §23–§25); where it places a concept in "the core", read CORE or INTERFACE as §25 sorts it.

## The structure proposed

**The core, with no optimization in it.**
1. *Outcomes and behaviours.* As v13's [M1]–[M3], [B1], [B2], [B4], [A1] and [D1] without the tilt. A behaviour may
   depend on a context, such as a prompt: one behaviour per context.
2. *The request*, declared before it judges ([A5]): what the principal asks, in parts that each can be absent.
   - **Constraints** (new): statements every acceptable behaviour satisfies, whatever else it does. Three forms, all
     convex: a **forbidden set** of outcomes, `a(C) = 0`; a **rate limit**, `a(C) ≤ ε`; a **budget**, `E_a[g] ≤ b`.
     They need no reference and no ranking: they are the absolute standard (`constraints.md`).
   - **Order**: a ranking of outcomes, possibly partial, read only up to increasing transformations ([B3] becomes this).
   - **Reference**: a behaviour per context against which the order is judged: a base model, the previous version, a
     population of answers, or the status quo. It replaces the default; it is a declaration, never a training.
   - **Indifference**: a partition of outcomes within which the principal does not care (v13's [D4], the principal's
     side). The tolerance of a measurement is not part of the request: on a continuum it is a property of the record
     (`CORE-GENERAL.md`), and a tolerance that forgives exactly can be cheated (`NOTES.md` §22).
   - **Value scale**, optional: units in which the principal reads gains and losses, needed for stakes.
3. *Acceptability.* The acceptable behaviours are those that satisfy every constraint and the order's requirement
   against the reference. They form a convex closed set, by a principle stated as such: **a mixture of acceptable ways
   of acting is acceptable**, since an actor that randomizes between two acceptable actions does nothing unacceptable,
   and records cannot tell the difference anyway (VE2).
4. *Verdicts, each with its own name*, never folded into one number:
   - **breach** of a constraint: verifiable, by a single witness for a forbidden set (VK1); with its rate or excess, in
     the constraint's own units;
   - **better / worse / neither** under the order against the reference, "for every reading" of the ranking (VO1–VO3);
   - **misalignment**, the evidence against acceptability: the best long-run growth rate of a bet, fixed in advance,
     that no acceptable behaviour expects to win (VE1). It equals v13's measure, the least divergence from the actual
     behaviour to an acceptable one, whenever the acceptable set is convex.
5. *Evidence from records.* Bets multiply over decisions, and their product stays a fair game under acceptance whatever
   the dependence between decisions, so a test from bets keeps its level when each decision, given the past, is
   acceptable (VE3). This replaces v13's convention that accepted behaviours decide independently, and needs no bins on
   a continuum: a bet is a function, its average is estimated by an average.
6. *Stakes*, in the units of the value scale and of each constraint, totalled over the horizon of use, with the limit
   that no record removes: a shift of about `1/√n` per decision escapes every test over `n` decisions (H43).

**Derived: actors that optimize.** Everything that needs a model of optimization moves here, and is stated as a
hypothesis about an actor that a record can test, never as part of what the principal asks: pursuit and the tilt
([D2]), the KL price and the intensity, the steepest climb ([P2], [P4], [P14]), interventions and pass-through ([D6]),
the evaluator and overoptimization ([D10]), outer and inner misalignment ([P49]), and the frontier. Constraints enter
here through Lagrange multipliers: an actor that optimizes `F` under a budget acts exactly as one that optimizes
`F − ν·g` with no budget, `ν ≥ 0` being the budget's shadow price (VK5, by the Karush–Kuhn–Tucker conditions).

**What stays, what moves, what goes**, by v13 item:

| v13 | v14 |
|---|---|
| [M1]–[M3], [B1], [B4], [A1], [A5] | kept; [M3] gains the results read for VE1 |
| [B2] episodes and conditions as outcomes | kept for episodes; contexts become the conditioning of a behaviour, and dependence between decisions is handled by bets (VE3) instead of a convention |
| [B3] an objective up to scale and constant | the order is read up to increasing transformations; scale returns only in the value scale |
| [A4] misalignment is evidence | kept in substance, restated as the growth rate of the best bet against acceptability; equal to v13's form on convex sets (VE1) |
| [D1] outcomes, behaviours, divergence and tilt | kept without the tilt, which moves to the derived module |
| [D2] pursuit | derived module |
| [D3] specification and misalignment | replaced by the request (constraints, order, reference, indifference, value scale) and acceptability, a convex set; v13's ordinal specification survives as one way to judge the order; the standard specification moves to the derived module, as the acceptable set of an optimizer at a KL price, held by records to its convex hull |
| [D4] resolution | the principal's side is indifference, in the request; the actor's side moves with feasibility |
| [D5] stakes | kept, with constraint excess and totals over the horizon |
| [D6] interventions | derived module |
| [D7] feasibility, [D8] conditions and views, [D9] observation | kept: none needs optimization |
| [D10] evaluator | derived module |
| [D11] records and evidence | rewritten on bets (VE3, VE4); [P55]'s exact test kept for independent decisions |

The 55 propositions follow their definitions; a full map comes with the next step.

## What is proved here so far

| File | Results | Status |
|---|---|---|
| `evidence.md` | VE1, misalignment against a convex set is the growth rate of the best bet; VE2, records hold an actor to the convex hull; VE3, a test from bets keeps its level under any dependence; VE4, the average log-bet tends to its expectation | proved here; VE1 also read in an open text (Grünwald, de Heide and Koolen, Theorem 1) |
| `constraints.md` | VK1 forbidden sets; VK2 rate limits, in closed form; VK3 budgets, by a Lagrange dual; VK4 several constraints; VK5 the constrained optimizer, by the Karush–Kuhn–Tucker conditions | proved here, except VK4's equality, which the probe supports and which is not yet proved |
| `order.md` | VO1 "better for every reading" is dominance on upper sets; VO2 v13's ordinal specification lies inside it; VO3 three verdicts, and which of them a record can verify | proved here |
| `factorization.md` | FA1 nested interfaces factor misalignment exactly; FA2 its Pythagorean form for linear interfaces, with culpability `K = E + R`; FA3 nested linear interfaces toward a fixed target; the earlier splits by mechanism and layer, with one label of v13 that overclaims; VF1–VF3 the verification status of every factor's label | proved here |

None runs in CI yet. The probe `probes/v14/v14_probe.py` reproduces every number, with its output in
`probes/v14/RESULTS.md`.

## Next steps, in order

1. *Labels first.* Register L2 before computing it: the label cases this draft predicts it fixes (best-of-`n`, the
   mixing actor, the constrained optimizer under v13's standard specification, the greedy decoder) and new ones for the
   new words (breach, better, worse, neither, misalignment against a request with constraints), each with its sense in
   the defining text or in everyday use.
2. *Open questions for the PI*, after L2: the names; whether the order's requirement is dominance (VO1) or the stronger
   ordinal specification (VO2); what the order is judged against when the reference itself breaches a constraint; the
   margins with which "worse" becomes verifiable (VO3).
3. *The items.* The new core in `CORE.md`'s format, M/B/A/D with Interpretations, in this folder, with lint support.
4. *The derived results* re-proved or moved, with checks and mutants; the library; the general core, where bets need no
   bins.
5. *The real case* (H42): a frozen model against a reference model, with forbidden outputs as constraints and one
   scorer as the order, judged by bets over prompts.

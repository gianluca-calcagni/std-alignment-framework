# v14, a draft: a core whose words mean what they say

> **Status: a working draft on the branch `claude/core-v14` (Q59–Q65). Nothing here is approved, and nothing here
> replaces `CORE.md` or `derived/` yet.** It gathers what the label test L1, the general core and the discussions of
> `NOTES.md` §22–§28 taught, and proves the results the new structure rests on. The PI's decisions on R15 and R16 wait
> until the draft has absorbed them (Q59). The work ahead is in `ROADMAP.md`'s recommendations.

## Why a rework

Five findings, each recorded with its evidence in `NOTES.md` §21–§26:
- *v13 defines misalignment through a model of optimization.* Its standard specification is the pursuit ray, the set of
  optimizers of `F` at a KL price ([D2], [D3]). L1 traced most of its label disagreements to that: best-of-`n` by the
  right objective is called misaligned for the shape of its reweighting. The PI asked for a core with no optimization in
  it, in which a frozen model's misaligned behaviour is defined beyond doubt (Q58).
- *The pursuit ray is not convex.* An actor that pursues `F` at intensity `0` or `3` at random, acceptably at every
  decision, is charged `0.0546` nats per decision, and [P55]'s test against the ray accuses it in 69% of records of 400
  decisions (`evidence.md`, VE2).
- *A ranking alone does not support "misaligned".* A decoder that always answers at its prompt's 0.9 quantile, level 8
  of 10 in `order.md`'s instance, is neither better nor worse than its reference for every reading of the ranking
  (`order.md`, VO3).
- *Constraints were missing.* Some outcomes are unacceptable whatever else happens, and breaking one is plainly
  misalignment (Q59).
- *v13 mixed what happened, whether the actor could have done otherwise, and why.* Culpability, coarse perception and
  tampering need what the actor sees and can do, not a model of optimization (Q61); and one of v13's labels, [P15](v)'s
  "unavoidable", says more than its split proves (`factorization.md`).

## The files

Three layers, each built only on the ones below it, each with a twin for outcomes that are not finite that states only
what changes there, as `general/transfer.md` does (Q62):

| File, to be written | Holds | Twin |
|---|---|---|
| `CORE` | behaviours per condition; the request, a list of requirements, each a convex closed set; misalignment as the evidence against their intersection, with a verdict per requirement; records and bets | `CORE_GENERAL` |
| `INTERFACE` | what the actor sees, what it can do, and how the world turns its actions into outcomes; feasibility, culpability, coarse perception, noise, tampering, collusion | `INTERFACE_GENERAL` |
| `OPTIMIZERS` | objectives, pursuit, the KL price, evaluators, training, shadow prices; gaming, overoptimization, outer and inner misalignment, strategic deception | `OPTIMIZERS_GENERAL` |

The draft so far, in this folder:

| File | What it holds | Status |
|---|---|---|
| `evidence.md` | VE1 misalignment against a convex set is the growth rate of the best bet; VE2 records hold an actor to the convex hull; VE3 a test from bets keeps its level under any dependence; VE4 a bet's growth is an average; why this measure | proved here; VE1 also read in an open text ([@grunwald2023], Theorem 1) |
| `constraints.md` | VK0 every convex requirement is a set of budgets; VK1 forbidden sets; VK2 rate limits; VK3 budgets, by a Lagrange dual; VK4 several constraints; VK5 the constrained optimizer, by the Karush–Kuhn–Tucker conditions (for OPTIMIZERS) | proved here, except VK4(iii), supported by a probe |
| `order.md` | VO1 better for every reading is dominance on upper sets; VO2 v13's ordinal specification lies inside it; VO3 three verdicts and what a record verifies; why dominance is canonical | proved here |
| `interface.md` | the interface, feasibility, culpability, elicitation; IN1 every convex feasible set is an interface's; every form of misalignment by the layer that defines it | definitions proposed; IN1 proved here |
| `factorization.md` | FA1 nested interfaces factor misalignment exactly; FA2, FA3 its Pythagorean forms; v13's exact splits by mechanism and layer; VF1–VF3 the verification status of every factor's label | proved here |
| `LIMITS.md` | what the framework cannot do and leaves out | proved, chosen, or marked as a hunch |
| `MIGRATION.md` | what of v13 survives, item by item | the executor's assessment, not reviewed |

None runs in CI yet. The probes in `probes/v14/` reproduce every number, with their outputs beside them; VK0, VO1, VO2,
IN1, FA1 and VF1–VF3 have no probe, as their proofs leave nothing to compute.

## The design

**CORE**, with no optimization in it, built by the method v13 used, reverse physics [@carcassi2022]: imported
mathematics (M), background conditions assumed without loss of generality, each with its qualifier (B), premises with
their status (A), and definitions with their interpretation (D).
1. *Outcomes and behaviours.* As v13's [M1], [M2], [B1], [B2], [A1] and [D1] without the tilt; a behaviour may depend
   on a condition, such as a prompt.
2. *The request*, declared before it judges ([A5]): a finite list of **requirements**, each a convex closed set of
   behaviours. The **acceptable set** is their intersection.
3. *Misalignment*, the evidence against acceptability: the best long-run growth rate of a bet, fixed in advance or
   chosen before each decision, that no acceptable behaviour expects to win ([A4] in its bet form, VE1), with a
   **breach** verdict for each requirement.
4. *Records*, judged by bets, valid whatever the dependence when each decision is acceptable given the past (VE3), with
   [P55]'s exact test for samples.

**Refinements of CORE that build requirements**, none of them a new kind of object: the catalogue of constraints
(`constraints.md`); an order against a reference (`order.md`); indifference, as requirements that depend only on the
masses of cells; structural requirements, such as acting alike in every condition ([P40]) or invariance under time
reversal ([P41]). **Refinements of the principal's side**: a value scale for stakes and severity (`NOTES.md` §24), and
several principals with weights ([P42]).

**INTERFACE** (`interface.md`) and **OPTIMIZERS**, as in the table above; a constraint enters OPTIMIZERS through its
shadow price (VK5).

## Why the design loses no generality, and where it does

A framework meant for every case of misalignment, in any domain, must say of each of its choices that no case is lost,
or say which cases are. These are the claims, each with its ground and its qualifier.

| Claim | Why nothing is lost | Qualifier |
|---|---|---|
| finitely many outcomes | a record of finitely many decisions at finite precision decides finitely many events, and misalignment on a continuum is the supremum over them ([B1]; `general/transfer.md`, TR2) | that supremum equals the least divergence to the acceptable behaviours only when their closure is compact (TR3); heavy tails and atoms in `CORE-GENERAL.md`; v14's own results are proved for finite outcomes only |
| episodes and conditions as outcomes | an episode, or a condition with its outcome, is again an outcome ([B2]) | one long record with no episodes |
| a request is a list of requirements, each a set of behaviours | by [A1] a judgement from behaviour is a statement about behaviours, which is a set of them, and a list holds a conjunction | comparisons with a reference (`order.md`, VO3) are reported beside the verdicts; they become requirements only when the principal declares which |
| requirements are closed | closing a requirement changes no misalignment and no bet (VE1(iv)) | the breach verdict changes at boundary behaviours, such as a rate exactly at a strict limit, which no record can tell apart |
| requirements are convex | forced given two premises: a schedule of acceptable behaviours is acceptable, and tests must keep their level whatever the dependence. Independent draws from a mixture have the law of a random schedule of its components, so a test valid for every schedule is valid at the hull; and no bet separates a set from its hull (VE2) | a set that is not convex, independence among them, is enforced as its hull; for a sample it can still be judged (`factorization.md`, VF1); the premises are a choice the PI should make knowingly |
| every convex requirement is a set of budgets | the separating hyperplane, from the nearest point (`constraints.md`, VK0) | some need infinitely many budgets |
| a ranking is read as dominance | dominance is exactly "better for every holder of the ranking" (VO1) | reading "better" as unanimity over the ranking's readings is a choice; the requirement built from the order (`B(r)`, the ordinal cone, or margins) is declared, not implied |
| every convex feasible set is an interface's | the actions can be the feasible behaviours themselves (`interface.md`, IN1) | an actor that cannot randomize has a feasible set that is not convex, declared as a set |
| misalignment factors over any chain of interfaces | telescoping, with no hypothesis (`factorization.md`, FA1) | the terms are evidence rates only for linear interfaces (FA2, FA3) |
| misalignment is the growth rate of the best bet | equal to the least divergence to the hull (VE1, VE2), whatever the requirement | given the conventions below, Kelly's among them; that bets chosen from the record reach the best growth is not proved (H46) |

## The conventions, each justified

A convention is a choice an equally reasonable principal could make otherwise. As in v13's table (`CORE.md` §1), each
is forced by a stated requirement, chosen for mathematical convenience, or taken from the literature whose results it
imports, and marked by whether it changes a verdict.

| Convention | Where | Justified by | Changes a verdict | Why |
|---|---|---|---|---|
| natural logarithms | everywhere | convenience | no | another base rescales every number alike |
| evidence on a logarithmic scale, per decision | `evidence.md` | forced, literature | no | evidence of independent decisions must add, and only multiples of the logarithm turn products into sums (Cauchy's functional equation) |
| bets fair under acceptance | VE1, VE3 | forced, literature | no | otherwise a large wealth is no evidence against acceptability, and the level of VE3 fails; the definition of an e-variable [@grunwald2023] |
| wealth valued by its long-run growth, the expected logarithm | VE1, VE4 | literature, a choice | yes: expected wealth would give the Rényi divergence of order `∞` | Kelly's criterion; the one under which evidence of independent decisions adds and the number is [A4]'s rate |
| the question is how improbable acceptance makes the actor's record, `KL(p̂‖a)` in this order | VE1, VE4 | forced, given [A4] | yes: the other order, Stein's exponent, answers how fast a misaligned actor stops escaping | the exponent of false accusation while the actor is reliably convicted; Sanov's rate |
| the best bet, the acceptable behaviour most favourable to the record | VE1 | literature | yes: an average or the least favourable would charge more | the generalized likelihood ratio's benefit of the doubt, as in v13 |
| each decision judged given the past, mixtures accepted: the **mixture principle** | VE2, VE3 | forced, given two premises | yes, for a requirement that is not convex | the premises: a schedule of acceptable behaviours is acceptable, and the level holds whatever the dependence; under them the number is the least divergence to the hull |
| requirements closed | VE1(iv) | convenience | no for misalignment and bets; yes for the breach verdict at the boundary | minima are attained; a boundary behaviour no record can tell apart |
| a ranking read as dominance | `order.md` | forced, given unanimity over the ranking's readings | yes, against v13's ordinal cone | the cone adds a shape the ranking does not declare (VO2); which requirement the order gives is the PI's to decide |
| culpability as evidence, `K` | `interface.md` | convenience, consistency with [A4] | no on whether the actor is culpable, yes on how much | `K` and the avoidable excess `E` vanish together; `K` is an evidence rate, testable by bets, `E` a difference of two |
| every concept in the least layer that can define it | `interface.md` | convenience | no | a reader learns what each form of misalignment needs, and no concept depends on more than it must |
| pursuit as a tilt, its price KL | OPTIMIZERS | forced, given v13's two reasons of [D2] | yes, within OPTIMIZERS | the steepest climb in the Fisher geometry and the best trade-off at a KL price agree only there ([P14]); it no longer touches what misalignment is |

## Challenges, and the answers

Objections a reader is likely to raise, with what the draft says to each; acknowledging one without these answers would
weaken the framework more than it should.
- *"KL is one divergence among many; why not total variation or a Wasserstein distance?"* Misalignment is not chosen as
  a distance; it is the rate at which a fair bet against acceptability grows, and given the conventions above, Kelly's
  criterion and [A4]'s question among them, the formula has no freedom left (`evidence.md`, why this measure). A
  principal who cares about a geometry of outcomes declares it as a requirement, which VK0 always allows.
- *"Convex requirements lose cases, such as 'act independently' or 'pursue exactly `F`'."* They lose what no record
  could enforce when each decision is judged with no model of the actor: an actor that switches between acceptable
  behaviours shows only a mixture (VE2). For a sample of independent decisions such a requirement is still judged
  (VF1), and the choice between the two is stated, not hidden (`LIMITS.md`).
- *"A core that is a list of sets says nothing."* It says exactly what a judgement from behaviour can say ([A1]), and
  every convex requirement is a list of limits on averages (VK0), possibly infinite, the form in which principals state
  constraints. The content of a domain is in its requirements, declared through refinements whose results are proved.
- *"Without optimization the core cannot see reward hacking or goal-directed failure."* It sees what happened: the
  measured requirement met and the true one breached is the evaluation gap, in CORE. Why it happened, the motive, is an
  OPTIMIZERS hypothesis that records can refute and never verify (`factorization.md`, VF2), as it should be.
- *"Culpability depends on an interface the principal declares; that is arbitrary."* The interface is a hypothesis that
  records refute when the actor does what it says the actor cannot, and an excuse about capability is tested in
  elicitation conditions or reported as resting on the declaration (VF3). The refutation runs one way: an interface that
  overstates the actor's capability charges it for what no record can show it could not do, so the declared capabilities
  should be ones demonstrated in elicitation. Reporting what an excuse or a charge rests on is a rule of the report, not
  a theorem.
- *"Severity is ignored."* It is separated, on purpose: evidence and harm rank breaches differently (`NOTES.md` §24),
  and stakes on a declared value scale are reported beside misalignment, never folded into it.
- *"Dominance is too weak: a good greedy decoder comes out as neither."* Dominance is the strongest comparison every
  holder of the ranking agrees with (VO1); a verdict of misalignment needs a requirement built from it, `B(r)`, under
  which the decoder is misaligned, or margins at declared standards, under which it is not, or a value scale. The
  principal declares which.
- *"Finite outcomes and finitely many conditions are a restriction."* They are what a record decides (TR2). The general
  twins are to carry v14's results to standard Borel spaces with their qualifiers, as `general/transfer.md` already
  carries v13's transfer lemma, [P16] and [P54]; until they are written, v14 claims nothing beyond finite outcomes.

# v14, a draft: a core whose words mean what they say

> **Status: a working draft, drafted on the branch `claude/core-v14` (Q59–Q68), brought to `main` as a draft, and
> extended (Q69–Q77). It is not approved as a whole, and nothing here replaces `CORE.md` or `derived/` yet.** It gathers
> what the label test L1, the general core and the discussions of `NOTES.md` §22–§35 taught, and proves the results the
> new structure rests on. Its design follows the framework's six desiderata (`README.md`, Q74); the three choices it
> rests on, R19, were decided as they force them (`NOTES.md` §33.17), and the PI's other decisions on it are rows of
> `NOTES.md` §3.1. The work ahead is in `ROADMAP.md`'s recommendations.

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

Three layers, and a fourth on training (Q69, Q70), each built only on the ones below it, each with a twin for outcomes
that are not finite that states only what changes there, as `general/transfer.md` does (Q62):

| File, to be written | Holds | Twin |
|---|---|---|
| `CORE` | behaviours on one space, the conditions an exogenous σ-algebra; the specification, a list of requirements, each per-decision, a convex closed set, or pooled over a declared horizon, any closed set; misalignment as the evidence against the per-decision ones, with a verdict per requirement, convict or certify; records, bets and confidence sequences | `CORE_GENERAL` |
| `INTERFACE` | what the actor sees, what it can do, and how the world turns its actions into outcomes; feasibility, culpability, coarse perception, noise, tampering, collusion | `INTERFACE_GENERAL` |
| `PURPOSE` | aims: objectives, pursuit, the KL price, evaluators, shadow prices; gaming as a motive, strategic deception | `PURPOSE_GENERAL` |
| `SHAPING` | how an actor is changed by feedback: training, selection, education, regulation; outer and inner misalignment, overoptimization, misgeneralization (`training.md`, a proposal) | `SHAPING_GENERAL` |

The draft so far, in this folder:

| File | What it holds | Status |
|---|---|---|
| `evidence.md` | VE1 misalignment against a convex set is the growth rate of the best bet; VE2 records hold an actor to the convex hull; VE3 a test from bets keeps its level under any dependence; VE4 a bet's growth is an average; why this measure | proved here; VE1 also read in an open text ([@grunwald2023], Theorem 1) |
| `constraints.md` | VK0 every convex requirement is a set of budgets; VK1 forbidden sets; VK2 rate limits; VK3 budgets, by a Lagrange dual; VK4 several constraints; VK5 the constrained optimizer, by the Karush–Kuhn–Tucker conditions (for PURPOSE); VK6 a rate limit over conditions the world chooses; VK7 how misalignment moves with a budget | proved here, except VK4(iii), supported by a probe |
| `order.md` | VO1 better for every reading is dominance on upper sets; VO2 v13's ordinal specification lies inside it; VO3 three verdicts and what a record verifies; why dominance is canonical | proved here; to be written as a case of TG1 (Q74) |
| `interface.md` | the interface, feasibility, culpability, elicitation; IN1 every convex feasible set is an interface's; every form of misalignment by the layer that defines it | definitions proposed, except culpability's shape, decided (Q74); IN1 proved here |
| `factorization.md` | FA1 nested interfaces factor misalignment exactly; FA2, FA3 its Pythagorean forms; v13's exact splits by mechanism and layer; VF1–VF3 the verification status of every factor's label | proved here |
| `LIMITS.md` | what the framework cannot do and leaves out | proved, chosen, or marked as a hunch |
| `MIGRATION.md` | what of v13 survives, item by item | the executor's assessment, not reviewed |
| `resolution.md` | σ-algebras of the principal, the record and the actor: RS1 refinement adds up exactly; RS2 bets a coarse record can settle; RS3 indifference; RS4 hidden misalignment, neither verifiable nor refutable; RS5 views and resolutions are linear interfaces; RS6 a resolution at least as fine as the principal's costs nothing; RS7 latitude taken, a proposal; RS8 a view is revealed from below | proved here, except RS7, a proposal |
| `targets.md` | TG1 a family of targets with a reference is a list of budgets; TG2 that is not pursuing one target; SN1 Sanov's rate, the best bet and the projection are one number | proved here; TG1's reading decided (Q74) |
| `severity.md` | severity as a declared scale, never in nats; what a report gives; who grades | a proposal |
| `training.md` | a fourth layer, SHAPING, for training, selection, education and regulation; SH1 | a proposal; SH1 proved |
| `junctures.md` | where the framework's parts meet, how each meeting fails, and the measure it inspires; how refining one σ-algebra moves the others | a brainstorm (Q77) |
| `related.md` | competing frameworks, both ways | a survey by a research assistant, not reviewed |
| `literature-q70.md` | mixtures after Carcassi, the cost of the mixture principle, culpability, adversarial actors | a survey by a research assistant, not reviewed; two derivations checked, one claim corrected |
| `book-q70.md` | Carcassi and Aidala's book read: ensemble spaces, the method of pairing a word with its formal object, a seven-step protocol for the labels | a research assistant's reading, not reviewed |

**Names** (R20, approved by the PI, Q70): PURPOSE for the third layer, once OPTIMIZERS; SHAPING for a fourth, on
training (`training.md`); and "specification" for what the principal declares, once "the request". Notes written before
Q70 keep the old names. None runs in CI yet. The probes in `probes/v14/` reproduce every number, with their outputs
beside them; VK0, VO1, VO2, TG1, IN1, FA1, VF1–VF3, RS6–RS8 and SH1 have no probe, as their proofs leave nothing to
compute.

## The design

**CORE**, with no optimization in it, built by the method v13 used, reverse physics [@carcassi2022]: imported
mathematics (M), background conditions assumed without loss of generality, each with its qualifier (B), premises with
their status (A), and definitions with their interpretation (D).
1. *Outcomes and behaviours.* As v13's [M1], [M2], [B1], [B2], [A1] and [D1] without the tilt. An outcome holds
   everything a record notes of a decision, the situation it arose in included, such as a prompt; a behaviour is one
   distribution on the outcomes, analysed as a unit. One declaration remains of the old split into conditions and
   outcomes: which part of an outcome the world, not the actor, chooses (the next section).
2. *The specification*, **declared** before it judges ([A5]), declared meaning fixed, dated and published before the
   record it judges is read (`NOTES.md` §33.8; a test is "registered", in the repository's older word): a finite list of
   **requirements**, each declared of one of two kinds (Q74, `NOTES.md` §33.17). A **per-decision** requirement, that
   every decision given the past be acceptable, is a convex closed set of behaviours; a **pooled** one, on the average
   of the conditional behaviours over a declared horizon, is any closed set, CVaR limits included. The **acceptable
   set** is the intersection; when it is empty, which the declarations alone show, the specification is reported as
   **inconsistent** before any record is read.
3. *Misalignment*, the evidence against acceptability: the best long-run growth rate of a bet, fixed in advance or
   chosen before each decision, that no acceptable behaviour expects to win ([A4] in its bet form, VE1), with a
   **breach** verdict for each requirement.
4. *Records*, judged by bets, valid whatever the dependence when each decision is acceptable given the past (VE3), and
   pooled requirements by confidence sequences for the average of the conditional behaviours, valid whatever the
   dependence; two verdicts, **convict** and **certify** at a declared margin, a pooled breach named an **aggregate
   breach** and never summed with misalignment; [P55]'s exact test kept for certifying samples. Certify applies to a
   pooled requirement, and to a per-decision one only for a sample, independent draws from one behaviour: no record
   certifies that every decision of a changing actor was acceptable (`LIMITS.md`, Q76).

**Refinements of CORE that build requirements**, none of them a new kind of object: the catalogue of constraints
(`constraints.md`); an order against a reference (`order.md`); indifference, as requirements that depend only on the
masses of cells; structural requirements, such as acting alike in every condition ([P40]) or invariance under time
reversal ([P41]). **Refinements of the principal's side**: a value scale for stakes and severity (`NOTES.md` §24), and
several principals with weights ([P42]).

**INTERFACE** (`interface.md`) and **PURPOSE**, as in the table above; a constraint enters PURPOSE through its shadow
price (VK5).

## Conditions and outcomes: one distribution, and the one declaration that remains

The PI asked whether conditions and outcomes can be paired into one distribution, analysed as a unit, unless a good
argument keeps them apart (Q70). They can, and v14 does (`NOTES.md` §33.2, decided under Q74, §33.17, item 5): a
condition is part of the outcome, and every specification is a set of distributions on the pairs, so nothing a
specification can say is lost. What the split carried that one distribution does not is one fact, which the principal
declares: **which part of the outcome the world chooses**, a sub-σ-algebra `ℰ` of the outcomes, its cells what were
called conditions. When the world chooses nothing, `ℰ` is trivial and nothing else is needed.

**Why it cannot be dropped.** By the chain rule, for behaviours `p` and `a`,
`KL(p‖a) = KL(p_ℰ‖a_ℰ) + Σ_C p(C)·KL(p(·|C)‖a(·|C))`, the sum over the cells `C` of `ℰ`. The first term is evidence
about how often the world posed each situation, which says nothing about the actor. So misalignment is taken against the
acceptable behaviours that share the actor's law on `ℰ`, `M_A(p) = inf {KL(p‖a) : a ∈ A, a_ℰ = p_ℰ}`, which leaves the
second term only. Without the declaration the framework errs one of two ways, both seen in numbers: it charges the actor
for the world's mix, when the requirement fixes a mix the world did not deliver; or it credits the actor with acceptable
behaviours that would need the world to have posed the situations at other rates, as merging the conditions does for the
support bot, `0.0440` nats per decision against `0.0496` with the mix held fixed (`constraints.md`, VK6). Bets are
likewise fair given the world's choice, decision by decision, the contexts of VE3, or a world that changes its mix would
move the wealth.

**What it gains.** Requirements across situations ("act alike whatever the user's name", [P40]) and within them are one
kind of object; the σ-algebra results of `resolution.md` apply to what the world chooses as to what the actor does; and
a situation partly made by the actor, a conversation whose later turns follow its earlier answers, is expressed by
declaring the user's turns exogenous given the history: the chain rule is then taken turn by turn, and the acceptable
behaviours share the world's responses given the history rather than its overall mix, which is not yet written. The
results stated per condition (VK6, `interface.md`) are the case where `ℰ` is generated by a finite list of conditions.

## Why the design loses no generality, and where it does

A framework meant for every case of misalignment, in any domain, must say of each of its choices that no case is lost,
or say which cases are. These are the claims, each with its ground and its qualifier.

| Claim | Why nothing is lost | Qualifier |
|---|---|---|
| finitely many outcomes | a record of finitely many decisions at finite precision decides finitely many events, and misalignment on a continuum is the supremum over them ([B1]; `general/transfer.md`, TR2) | that supremum equals the least divergence to the acceptable behaviours only when their closure is compact (TR3); heavy tails and atoms in `CORE-GENERAL.md`; v14's own results are proved for finite outcomes only |
| episodes and conditions as outcomes | an episode, or a situation with what the actor did in it, is again an outcome ([B2]); which part the world chooses is declared as a sub-σ-algebra `ℰ` (the section above) | one long record with no episodes; a principal who leaves out `ℰ` charges the actor for the world's mix, or credits it with mixes the world did not deliver |
| a specification is a list of requirements, each a set of behaviours | by [A1] a judgement from behaviour is a statement about behaviours, which is a set of them, and a list holds a conjunction | comparisons with a reference (`order.md`, VO3) are reported beside the verdicts; they become requirements only when the principal declares which |
| requirements are closed | closing a requirement changes no misalignment and no bet (VE1(iv)) | the breach verdict changes at boundary behaviours, such as a rate exactly at a strict limit, which no record can tell apart |
| per-decision requirements are convex | forced given two premises: a schedule of acceptable behaviours is acceptable, and tests must keep their level whatever the dependence. Independent draws from a mixture have the law of a random schedule of its components, so a test valid for every schedule is valid at the hull; and no bet separates a set from its hull (VE2) | a set that is not convex, declared per decision, is enforced as its hull; a limit on tail risk, which is not convex (at a tail of 10%, two behaviours with CVaR `0.6` mix into one with CVaR `0.72`, `NOTES.md` §32), is declared pooled, and judged on the average behaviour over its horizon, whatever the dependence (Q74) |
| every convex requirement is a set of budgets | the separating hyperplane, from the nearest point (`constraints.md`, VK0) | some need infinitely many budgets |
| a ranking is read as dominance | dominance is exactly "better for every holder of the ranking" (VO1) | reading "better" as unanimity over the ranking's readings is a choice; the requirement built from the order is dominance with declared margins, `B_m(r)`, margins `0` giving `B(r)` (Q74) |
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
| each decision judged given the past, mixtures accepted: the **mixture principle**, for per-decision requirements | VE2, VE3 | forced, given two premises | yes, for a requirement that is not convex, which is then declared pooled | the premises: a schedule of acceptable behaviours is acceptable, and the level holds whatever the dependence; under them the number is the least divergence to the hull. What a principal states about a whole deployment is a pooled requirement, outside the principle (Q74) |
| requirements closed | VE1(iv) | convenience | no for misalignment and bets; yes for the breach verdict at the boundary | minima are attained; a boundary behaviour no record can tell apart |
| a ranking read as dominance | `order.md` | forced, given unanimity over the ranking's readings | yes, against v13's ordinal cone | the cone adds a shape the ranking does not declare (VO2), a mark of pursuit, kept for PURPOSE; the order gives `B_m(r)`, with declared margins (Q74) |
| culpability's verdict as `p̂ ∉ 𝓕*_δ` at a declared care margin `δ`, its size as the avoidable excess `E`; `K_δ` as its evidence rate | `interface.md` | forced by the desiderata in its shape (Q74); `δ` declared | no on whether the actor is culpable at `δ`, yes on how much | `K`, `E` and `p̂ ∉ 𝓕*` agree on the verdict; `K` is an evidence rate, testable by bets, but infinite exactly when the actor produces an outcome no best feasible behaviour does, the common case, so it ranks nothing (H52); `E` is a difference of two misalignments, finite with them |
| every concept in the least layer that can define it | `interface.md` | convenience | no | a reader learns what each form of misalignment needs, and no concept depends on more than it must |
| pursuit as a tilt, its price KL | PURPOSE | forced, given v13's two reasons of [D2] | yes, within PURPOSE | the steepest climb in the Fisher geometry and the best trade-off at a KL price agree only there ([P14]); it no longer touches what misalignment is |

## Challenges, and the answers

Objections a reader is likely to raise, with what the draft says to each; acknowledging one without these answers would
weaken the framework more than it should.
- *"KL is one divergence among many; why not total variation or a Wasserstein distance?"* Misalignment is not chosen as
  a distance; it is the rate at which a fair bet against acceptability grows, and given the conventions above, Kelly's
  criterion and [A4]'s question among them, the formula has no freedom left (`evidence.md`, why this measure). A
  principal who cares about a geometry of outcomes declares it as a requirement, which VK0 always allows.
- *"Convex requirements lose cases, such as 'act independently' or 'pursue exactly `F`'."* They lose what no record
  could enforce when each decision is judged with no model of the actor: an actor that switches between acceptable
  behaviours shows only a mixture (VE2). Such a set can be declared pooled instead, a requirement on the average
  behaviour over a declared horizon, judged whatever the dependence; it then speaks of the deployment, not of each
  decision (Q74). For a sample of independent decisions it is also judged as it stands (VF1), and which reading applies
  is stated, not hidden (`LIMITS.md`).
- *"A core that is a list of sets says nothing."* It says exactly what a judgement from behaviour can say ([A1]), and
  every convex requirement is a list of limits on averages (VK0), possibly infinite, the form in which principals state
  constraints. The content of a domain is in its requirements, declared through refinements whose results are proved.
- *"Without optimization the core cannot see reward hacking or goal-directed failure."* It sees what happened: the
  measured requirement met and the true one breached is the evaluation gap, in CORE. Why it happened, the motive, is a
  PURPOSE hypothesis that records can refute and never verify (`factorization.md`, VF2), as it should be.
- *"Culpability depends on an interface the principal declares; that is arbitrary."* The interface is a hypothesis that
  records refute when the actor does what it says the actor cannot, and an excuse about capability is tested in
  elicitation conditions or reported as resting on the declaration (VF3). The refutation runs one way: an interface that
  overstates the actor's capability charges it for what no record can show it could not do, so the declared capabilities
  should be ones demonstrated in elicitation. Reporting what an excuse or a charge rests on is a rule of the report, not
  a theorem.
- *"Severity is ignored."* It is separated, on purpose: evidence and harm rank breaches differently (`NOTES.md` §24),
  and stakes on a declared value scale are reported beside misalignment, never folded into it; the two meet only
  through a budget's price, VK7, which depends on the actor (`severity.md`).
- *"A limit on tail risk, such as CVaR, is a natural requirement, and it is not convex."* True, and the sharpest cost of
  the mixture principle: an actor that alternates between a safe and a risky acceptable behaviour can raise the tail of
  the pooled outcomes beyond the limit while every decision is acceptable. Declared per decision, the limit is enforced
  as its hull; a principal for whom the pooled tail is what matters must declare it pooled, over a horizon it states,
  and it is judged on the average of the conditional behaviours by confidence sequences, valid whatever the dependence
  (Q74, `NOTES.md` §33.17).
- *"This is the statistics of e-values, renamed."* Its evidence results are, and the draft should cite them
  (`related.md`, entry 1). What is not in that literature is the object they are applied to: requirements and their
  calculus, a verdict per requirement, the factorization by capabilities and by σ-algebras with each label's status,
  and definitions from behaviour alone.
- *"Dominance is too weak: a good greedy decoder comes out as neither."* Dominance is the strongest comparison every
  holder of the ranking agrees with (VO1); a verdict of misalignment needs a requirement built from it, `B(r)`, under
  which the decoder is misaligned, or `B_m(r)` with margins at declared standards, under which it need not be, or a
  value scale. The principal declares the margins (Q74).
- *"Finite outcomes and finitely many conditions are a restriction."* They are what a record decides (TR2). The general
  twins are to carry v14's results to standard Borel spaces with their qualifiers, as `general/transfer.md` already
  carries v13's transfer lemma, [P16] and [P54]; until they are written, v14 claims nothing beyond finite outcomes.

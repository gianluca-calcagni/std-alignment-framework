# INTERFACE on two concepts: a draft

> **Status: a draft for v14 (Q89), the executor's, at the PI's direction that INTERFACE be general and define no
> distinct concept where a few can do; not reviewed, not in CI.** Its results are proved here and are short; the numbers
> come from `probes/review/q89_interface.py` (`probes/review/RESULTS-q89.md`). It replaces nothing yet: `interface.md`
> holds the earlier definitions, which appear below as implementations.

CORE has one kind of declared object, a requirement: a set of behaviours, built in many ways. INTERFACE can have the
same shape. The earlier drafts gave it actions, signals, views, an environment, a resolution, a precision, an honest
channel, observed conditions, interventions and elicitation, ten notions. Two suffice, and each of the ten is a way of
building one of them. The PI's precedent is CORE's own: conditions and outcomes, once two types, became one
distribution and one declaration (`README.md`, one distribution).

Notation as in `mvp/CORE.md`: `Δ` the behaviours on the outcomes, the world's part `ℰ` included; `A` the acceptable
set; `M_A(p)` the misalignment of `p`; for a set `S` of behaviours, `m(S) = inf_{f∈S} M_A(f)`.

## Definitions

### ID1 — Limit
**Statement.** A **limit** is a closed set `L ⊆ Δ` of behaviours, declared as a fact: that the actor's behaviour lies in
it whatever the actor does. It is declared with its **owner**, the party that could lift it (the world, whoever deployed
the actor, whoever shaped it), and with what verifies it apart from the actor's own record. The **limits** of a case are
a finite list, and `L` also names their intersection. With no limit declared, `L = Δ`.

**In plain terms.** Something the actor cannot get around: the world does not allow it, or the actor was not given the
information or the tool, or it does not have the skill. Each comes with who could change it and how one knows.

**Interpretation.** A limit is to "can" what a requirement is to "may": the same kind of object, a set of behaviours,
with another status. A requirement is a norm the principal declares; a limit is a fact someone must be able to check. A
record of the actor can refute a limit, by a behaviour outside it, and never confirm it.

### ID2 — Shown capability, and link
**Statement.** A **link** is a declaration that what the actor does in one condition, it could do in another: a map from
conditions to conditions under which the actor's conditional behaviour is available. A **shown capability** is a
behaviour that the actor produced, in the condition judged or in a linked one and carried over by the link. The
**shown set** `G` is the set of shown capabilities, with their mixtures when the principal declares that the actor can
mix them. The actor's own behaviour is shown, so `p ∈ G`.

**In plain terms.** What the actor has been seen to do, here or in a situation declared to call on the same ability:
under another prompt, another incentive, an instruction, a test.

**Interpretation.** A link is the one new declaration of INTERFACE. Elicitation, an intervention, a honeypot and a
re-measurement are all conditions that someone chose, with a link to the condition judged; they differ in who chose
them and why, not in kind.

### ID3 — What the actor could do
**Statement.** The actor's **feasible set** `𝓕`, the behaviours it could produce, is not declared. It is known to lie
between the two sets: `G ⊆ 𝓕 ⊆ L`.

**In plain terms.** Nobody knows all an actor can do. One knows some things it did, and some things it cannot.

**Interpretation.** `interface.md` and the MVP's D9 declare `𝓕` itself. That is the case `G = L`, a claim to know the
actor's capability exactly, which no record supports (`factorization.md`, VF3; `resolution.md`, RS8).

## Results

### IR1 — Unavoidable and avoidable, as far as they are known
**Statement.** Let `G ⊆ 𝓕 ⊆ L` with `p ∈ G` and `M_A(p) < ∞`. The unavoidable misalignment `m(𝓕)` lies in
`[m(L), m(G)]`, and the avoidable excess `M_A(p) − m(𝓕)` in `[M_A(p) − m(G), M_A(p) − m(L)]`; all four ends are
non-negative, and each is computed from the declarations and the shown behaviours.

**In plain terms.** What the actor could not avoid is at least what its limits force and at most the best it has been
seen to do. What it could have avoided is at least the improvement it has shown, and at most everything its limits do
not force.

**Proof.** An infimum over a larger set is smaller, so `m(L) ≤ m(𝓕) ≤ m(G)`; and `p ∈ G` gives `m(G) ≤ M_A(p)`. ∎

**Notes.** For the support bot deployed with the view and without the look-up: the limit forces `0.2315`; from the
record as deployed alone the unavoidable part is anywhere in `[0.2315, 0.3274]`; with a second record, under an
instruction, and their mixtures, it is `0.2315` exactly. With no limit declared and nothing else shown, it is anywhere
in `[0, 0.3274]`.

### IR2 — Three verdicts on culpability
**Statement.** At a declared care margin `δ ≥ 0`, with `G`, `𝓕`, `L` and `p` as in IR1: if `M_A(p) − m(G) > δ`, the
actor is culpable at `δ` (**culpable, shown**); if `M_A(p) − m(L) ≤ δ`, it is not (**excused by the limits**);
otherwise the declarations and the records leave it **open**. When `A` is convex and closed with a member of full
support, "culpable, shown" is verifiable from samples of the conditions involved, given the link; "excused" is
refutable, and rests on the limits.

**In plain terms.** An actor is shown culpable when it has been seen to do better than it did by more than the margin.
It is excused when even its limits leave no more than the margin to gain. Between the two, nobody can say, and the
report says so.

**Proof.** By IR1 the excess is at least `M_A(p) − m(G)` and at most `M_A(p) − m(L)`. `M_A` is convex and lower
semicontinuous (`mvp/CORE.md`, R15), and finite, hence continuous on `Δ`, when `A` has a member of full support; so
`M_A(p) − min_g M_A(g) > δ`, over finitely many shown behaviours and their mixtures, is an open condition on the
behaviours shown, and open conditions are the verifiable ones (`factorization.md`, VF1). "Excused" is a closed
condition on `p`. ∎

**Notes.** This turns `interface.md`'s "verifiable with the interface taken as known" into a verdict no declared
capability supports alone: the charge rests on a record, the excuse on a fact. The probe's four cases: culpable, shown
(`0.0959` avoidable, a better behaviour on record); excused (`0.0018` to gain within the limit); and open twice, when
nothing better is shown and the limit does not cover the gap. Case M1 of the MVP reads "open" here, not "not culpable":
no decoding shown does better, and no limit was declared that forces the breach.

### IR3 — The earlier notions are limits, shown capabilities or links
**Statement.** Each notion below is an instance of ID1 or ID2, with the stated shape.

| Notion | Is | Its shape | Proved in |
|---|---|---|---|
| actions, tools, an environment that responds | a limit | the closure of the behaviours the policies produce, convex; a polytope for finitely many actions | `interface.md`, IN1 |
| a view: situations the actor cannot tell apart | a limit | the same conduct in conditions the view merges: linear | `resolution.md`, RS5(i) |
| a resolution: outcomes the actor cannot tell apart | a limit | fixed splits inside cells: linear | `resolution.md`, RS5(ii) |
| precision: noise the actor does not control | a limit | the images of a fixed kernel: convex | `CORE-GENERAL.md`, GD7 |
| inputs that differ little between two conditions | a limit | conduct in the two differs by at most the inputs' divergence: a convex sublevel set | [P16](iii) |
| an honest channel the actor cannot touch | a limit | the grounded behaviours: linear | [P50] |
| conditions no record covers | a limit and a record | the behaviours within the limits that agree with the record | `mvp/CORE.md`, R13(iv) |
| elicitation, an instruction, an incentive | a link | a condition someone chose, its conduct carried over | `factorization.md`, VF3 |
| a honeypot | a link | a condition the actor's inputs cannot tell from use | [P16](i) |
| an audit or a re-measurement | a link, on the record's side | the same outcomes read through another channel | [P51] |

**In plain terms.** Seeing less, having fewer tools, being imprecise, being unable to touch the sensor: each is a set
the actor cannot leave. Being instructed, rewarded, tested or audited: each is a situation someone chose, tied to the
one judged.

**Proof.** Each row restates the result it names. ∎

**Notes.** Pass-through, [D6]'s measure of how strongly an actor follows an incentive, models the response as a
reweighting and belongs to PURPOSE, as `MIGRATION.md` places it; the condition under the incentive is a link here.

### IR4 — Limits add up along any order, and the sum validates the diagnosis
**Statement.** For limits `L_1, …, L_k` taken in an order,
`m(L_1 ∩ … ∩ L_k) = m(Δ) + Σ_j (m(L_1 ∩ … ∩ L_j) − m(L_1 ∩ … ∩ L_{j−1}))`, every term non-negative. The terms depend on
the order.

**In plain terms.** Add the limits one at a time, and what each adds to the unavoidable part sums to the whole. The
split checks that nothing was counted twice or left out; how much is put on each limit depends on which came first.

**Proof.** `factorization.md`, FA1, on the nested intersections. ∎

**Notes.** The owners give one order that is not a choice, the world's limits, then the deployment's, then the actor's,
each inside the one before (`NOTES.md` §44). Within one owner the order is a convention; `NOTES.md` §42 shows a case
where it moves a term from `0.3628` to `0.2379`.

### IR5 — An intervention needs no object of its own
**Statement.** An intervention is a condition chosen by someone, with a link (ID2), or a change of a limit (ID1). For a
change from `L` to `L' ⊇ L`, its **potential** is `m(L) − m(L') ≥ 0`. For an actor with behaviour `p` before and `p'`
after, its **realized gain** is `M_A(p) − M_A(p')`. If the condition after is linked to the one judged, `p'` is shown,
and the avoidable excess of `p` is at least the realized gain.

**In plain terms.** To intervene is to put the actor in a situation of one's choosing, or to lift one of its limits.
The first shows what it can do; the second shows what the limit was costing. Neither needs a new kind of thing.

**Proof.** `L ⊆ L'` gives `m(L') ≤ m(L)`. If `p'` is shown, `m(G) ≤ M_A(p')`, and IR1 gives the bound. ∎

## What this draft does not do

- It proves nothing new: IR1 and IR4 are monotonicity, IR2 a reading of them, IR3 a table of results already in the
  tree. Its content is the reduction.
- A link is a declaration, and a wrong one shows a capability the actor does not have in the condition judged. Nothing
  here tests a link; retraining makes another actor (`factorization.md`, VF3).
- Mixing shown behaviours needs the declaration that the actor can mix. Without it `G` is a finite set.
- The numbers are for misalignment known exactly. From records, every end of IR1 is an estimate with its own interval.
- Limits over time, such as the options an actor's conduct leaves its principal, and an actor that changes its own
  limits, are not written.

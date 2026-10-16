# Factoring misalignment, and verifying the factors' labels

> **Status: draft of v14 (Q62); proved here, not yet checked in CI.** The numbers come from
> `probes/v14/factorization.py`.

The PI asked for two proofs: that the factorization of misalignment by the actor's interface (`NOTES.md` §25) is
exactly additive, as the framework's earlier splits were thanks to Pythagoras, with a look at which factors those
splits had already found; and that Carcassi's methodology of verification can justify the factors' labels. This file
gives both, and what they found: two ways to factor, which agree only in a special case; a label of v13 that claims more
than its split proves; and a rule that tells accusations from excuses by what a record can do with them.

Notation as in `evidence.md`. `A` is the acceptable set, `M_A(p) = inf_{a∈A} KL(p‖a)`. An actor's **interface** fixes
its **feasible set** `𝓕`, the behaviours its policies can produce (`NOTES.md` §25), and `M_A(𝓕) = inf_{f∈𝓕} M_A(f)`.
The actual behaviour `p̂` lies in `𝓕` unless the declared interface is wrong.

## Two ways to factor

### FA1 — Nested interfaces factor misalignment exactly
**Statement.** Let `A ⊆ Δ` be any set, and `𝓕_1 ⊇ 𝓕_2 ⊇ … ⊇ 𝓕_k` sets of behaviours with `p̂ ∈ 𝓕_k` and `M_A(p̂) < ∞`.
Write `m_j = M_A(𝓕_j)`. Then `M_A(p̂) = m_1 + Σ_{j=1}^{k−1} (m_{j+1} − m_j) + (M_A(p̂) − m_k)`, and every term is
non-negative.

**In plain terms.** Take the most capable actor one can declare, then remove its capabilities one at a time, down to
the actor's own. Misalignment is exactly: what even the most capable could not avoid; plus, for each capability
removed, how much its loss costs; plus what this actor could have avoided and did not.

**Proof.** The sum telescopes. `m_1 ≥ 0`. `𝓕_{j+1} ⊆ 𝓕_j` gives `m_{j+1} ≥ m_j`, an infimum over fewer behaviours, and
`p̂ ∈ 𝓕_k` gives `M_A(p̂) ≥ m_k`. ∎

**Notes.** The labels are exact by construction: `m_j` is the least misalignment that any behaviour of interface `j`
has, so "unavoidable with interface `j`" says no more than its definition. No hypothesis of convexity or linearity is
needed. What FA1 does not give is a reading of each term as evidence: a difference of two least misalignments is not
itself the divergence between two behaviours. FA2 gives that reading, under a hypothesis.

### FA2 — The Pythagorean form, for linear interfaces
**Statement.** Let `A` be closed in `Δ`, and `𝓕` linear ([D7]) and containing a full-support behaviour, with
`M_A(𝓕) < ∞`. Then `KL(f‖a)` has a minimizer `(f°, a°)` over `𝓕 × A`, since `𝓕 × A` is compact and `KL` jointly lower
semicontinuous; suppose `a° ∈ Δ°`. Let `𝓕*` be the behaviours of `𝓕` with `M_A(f) = M_A(𝓕)`, and suppose every `f ∈ 𝓕*`
has a nearest acceptable behaviour `a_f ∈ Δ°`. For `p̂ ∈ 𝓕`:
(i) `M_A(𝓕) = KL(f°‖a°)`, and `f°` is the behaviour of `𝓕` nearest to `a°`, minimizing `KL(·‖a°)` over `𝓕`.
(ii) `M_A(p̂) + R(p̂) = KL(p̂‖f°) + KL(f°‖a°)`, where `R(p̂) = KL(p̂‖a°) − M_A(p̂) ≥ 0`, with `R(p̂) = 0` exactly when
`a°` is a nearest acceptable behaviour of `p̂`.
(iii) The **culpability** `K(p̂) = min_{f∈𝓕*} KL(p̂‖f)`, the evidence that the actor does not do the best it could, and
the **avoidable excess** `E(p̂) = M_A(p̂) − M_A(𝓕)` satisfy `K(p̂) = E(p̂) + min_{f∈𝓕*} R_f(p̂) ≥ E(p̂)`, where
`R_f(p̂) = KL(p̂‖a_f) − M_A(p̂) ≥ 0`.

**In plain terms.** When the actor's limits are of the form "these averages are fixed", misalignment splits into two
divergences between named behaviours: the evidence that the actor is not at its best feasible behaviour, and the
evidence that this best is not acceptable. The split is exact up to one non-negative term, which credits the actor for
being near a different acceptable behaviour than the one its best feasible behaviour is nearest to.

**Proof.** (i) `inf_{(f,a)} KL(f‖a) = inf_f M_A(f) = M_A(𝓕)`, attained at `(f°, a°)`. For fixed `a°`, `f°` minimizes
`KL(·‖a°)` over `𝓕`, which [P15](i) makes unique, with full support, since `a° ∈ Δ°`.
(ii) [P15](iii) with `r = a°`: `KL(p̂‖a°) = KL(p̂‖f°) + KL(f°‖a°)` for every `p̂ ∈ 𝓕`. Substitute `KL(p̂‖a°) = M_A(p̂)
+ R(p̂)`. `R ≥ 0` because `a° ∈ A`, and `R = 0` exactly when `a°` attains `M_A(p̂)`.
(iii) For `f ∈ 𝓕*`, `(f, a_f)` is a minimizer of `KL` over `𝓕 × A`, so `f` is the behaviour of `𝓕` nearest to `a_f`, and
(ii) holds with `(f, a_f)` in place of `(f°, a°)`: `KL(p̂‖f) = M_A(p̂) − M_A(𝓕) + R_f(p̂)`. Take the least over
`f ∈ 𝓕*`. ∎

**Notes.** Convexity of `A` is not used in the proof; it makes `𝓕*` convex, so that culpability is tested by bets (VE1).
Checked on 200 random instances, with `A` v13's ordinal specification and `𝓕` fixing one average: the alternating
minimization over `𝓕 × A` reaches, to within `2e-5`, the least misalignment found by an independent search over `𝓕`,
which tests (i); the identity `K = E + R`, to within `3e-13`, only restates [P15](iii)
(`probes/v14/RESULTS-factorization.md`, (2)). Two hypotheses carry the equality. Linearity: a feasible set is linear
when it fixes averages, as deterministic views ([D8]), an actor's resolution ([D4]) and an environment whose responses
are recorded with the actions are ([P15], Notes); a noisy view gives inequalities, and when the actions are not recorded
the feasible set is a polytope; then only [P15](ii)'s inequality remains, so `K` and `E` need not be ordered: on 400
random polytopes, `E > K` in 330 (`probes/v14/culpability.py`). And `a° ∈ Δ°`: a forbidden set breaks it, and its factor
is then read on the allowed outcomes, not yet written here.

### FA3 — Nested linear interfaces, with a fixed target
**Statement.** Let `𝓕_1 ⊇ … ⊇ 𝓕_k` be linear, each containing a full-support behaviour, `r ∈ Δ°`, and `f_j` the
behaviour of `𝓕_j` nearest to `r` (minimizing `KL(·‖r)`). Then `f_{j+1}` is the behaviour of `𝓕_{j+1}` nearest to `f_j`,
and for every `p̂ ∈ 𝓕_k`, `KL(p̂‖r) = KL(p̂‖f_k) + Σ_{j=1}^{k−1} KL(f_{j+1}‖f_j) + KL(f_1‖r)`.

**In plain terms.** Toward one fixed target, each capability removed costs exactly the divergence between the best the
actor can do with it and the best it can do without it, and the costs add up with no remainder.

**Proof.** By [P15](iii) on `𝓕_j` with target `r`, every `p ∈ 𝓕_{j+1} ⊆ 𝓕_j` has `KL(p‖r) = KL(p‖f_j) + KL(f_j‖r)`, so
minimizing `KL(·‖r)` over `𝓕_{j+1}` is minimizing `KL(·‖f_j)` there, and `f_j ∈ Δ°` by [P15](i): `f_{j+1}` is the
behaviour of `𝓕_{j+1}` nearest to `f_j`. The identity follows by applying [P15](iii) on `𝓕_1` with target `r`, then on
`𝓕_2` with target `f_1`, and so on inward, to `p̂ ∈ 𝓕_k` at each step. ∎

**Notes.** Checked on 200 random pairs of nested sets, within `1e-7` (`probes/v14/RESULTS-factorization.md`, (3)). With
`r = a°`, FA3's terms are evidence rates between named behaviours; but `KL(f_1‖a°)` is the least misalignment of `𝓕_1`
only if `a°` is also the acceptable behaviour nearest to `𝓕_1`. When it is not, the target, chosen for the smallest
interface, is not the best for the larger ones, and FA3 overstates what the larger interfaces could not avoid. FA1 is
then the factorization with exact labels, and FA3 the one with readings as evidence. **Generality.** FA1 needs nothing
of the sets: every chain of capabilities a principal can declare, convex or not, factors exactly. The Pythagorean forms
are the special case in which each term is also an evidence rate; their hypotheses, linear interfaces and full-support
targets, are the qualifiers, listed in `LIMITS.md`.

## What the earlier splits had found

Every exact split of v13, by the mechanism that makes it exact and the layer it belongs to.

| Split | Result | Mechanism | Layer | Its label |
|---|---|---|---|---|
| conditions, and the coarse and the fine within a condition | [B2], [P4](iii) | chain rule: always exact | CORE | exact |
| frequency, drift and dependence, along a record | [P54] | chain rule and the mixture identity: always exact | CORE | exact |
| shared and drift, across runs | [P45] | the mixture identity `Σ w_i KL(p_i‖r) = KL(p̄‖r) + D`: always exact | CORE | exact |
| reproducible and run-specific, between conditions | [P46] | chain rule: always exact | CORE | exact |
| ordinal and the shape of the reweighting | [P36](iii), (iv) | Pythagorean: equality at the default, (iii); against the standard specification an inequality, (iv) | CORE, building a requirement | (iii) exact; (iv) a bound, not a split |
| coordination and individual | [P39] | chain rule: always exact | INTERFACE (`NOTES.md` §25: independence is no convex requirement) | exact as a number; "misalignment" only with an information structure |
| world and tampering | [P50](i), (ii) | chain rule: always exact | INTERFACE (the channel the actions cannot reach) | exact |
| the actor's resolution: best effort and what it cannot remove | [P8] | Pythagorean, linear | INTERFACE | exact |
| avoidable and unavoidable | [P15](v) | Pythagorean, linear, toward the nearest intended behaviour `p°` | INTERFACE | **overclaims**: below |
| departure: pursuit and misalignment | [P6] | Pythagorean, exponential family | OPTIMIZERS | exact |
| named and unexplained | [P44] | Pythagorean, linear | OPTIMIZERS | exact: the unexplained part is a least value over the span ([P48]), and `𝓛` fixes `E_p[F]`, so `p°` is the right target |
| outer and strict inner | [P49](ii) | Pythagorean, via [P48] | OPTIMIZERS | exact |
| what tampering adds to net value | [P50](iv) | Pythagorean, linear | OPTIMIZERS | exact, at the trainer's intensity |

**The label that overclaims.** [P15](v) splits `M(p̂) = KL(p̂‖p*°) + KL(p*°‖p°)` exactly, and calls the second term the
unavoidable misalignment. It is unavoidable only toward `p°`, the intended behaviour nearest to the actor's own, at the
intensity the actor revealed. A feasible behaviour aimed at another intensity can have less misalignment. On 109 random
instances with one fixed average, the term exceeded the least misalignment of any feasible behaviour in 107, by up to
`0.86` nats (`probes/v14/RESULTS-factorization.md`, (1)). The split is right; the word "unavoidable" says more than it.
FA1 gives the exact unavoidable part, and FA2 the Pythagorean form with the right target. The same word carries the same
overclaim in [P15]'s Notes, for contexts and an actor's resolution, and in [D7]'s reasons. Recorded in `NOTES.md` §1.

## Verifying the labels, by Carcassi's methodology

Carcassi's principle asks that a theory's statements be tied to experimental verification: a statement is
**verifiable** when a test exists that succeeds in finite time if it is true, **refutable** when its negation is
verifiable, and a theory's objects get their meaning from the verifiable statements about them ([@carcassi2021]). For
statements about behaviours, verified in the statistical sense, the verifiable statements are exactly the open sets of
behaviours ([@genin2017], as [D3] cites it). What that methodology can justify about a label, and what it cannot, is
below.

### VF1 — Accusations are verifiable, and statements of compliance only refutable
**Statement.** Let `S ⊆ Δ` be closed, neither empty nor all of `Δ`. Then "`p ∉ S`" is verifiable and not refutable, and
"`p ∈ S`" is refutable and not verifiable. When `S` is convex, VE3's bets test "`p ∉ S`" at level `α` whatever the
dependence between decisions, as long as each decision, given the past, is drawn from `S`; that the test's power tends
to one is shown for samples only.

**In plain terms.** A record can show that an actor is outside a closed standard, never that it is inside one: it can
convict, never certify.

**Proof.** The complement of `S` is open, so "`p ∉ S`" is verifiable. `Δ` is convex, hence connected, so the only sets
both open and closed in it are `∅` and `Δ`; `S` is neither, so `S` is not open, and "`p ∈ S`" is not verifiable, which
is to say "`p ∉ S`" is not refutable. "`p ∈ S`" is refutable since its negation is verifiable. The test is VE3's. ∎

### VF2 — The verification status of every factor's label
**Statement.** With the declared requirements and interfaces closed, the statements below have the status given.

| Label | Statement | Status |
|---|---|---|
| breach of requirement `j`; misaligned | `p̂ ∉ A_j`; `p̂ ∉ A` | verifiable (VF1) |
| culpable | `p̂ ∉ 𝓕*`, the feasible behaviours of least misalignment, closed since `M_A` is lower semicontinuous | verifiable with the declared interface taken as known (VF1); with the interface itself under test, `p̂ ∈ 𝓕 ∖ 𝓕*` has an empty interior when `𝓕` is linear, and is not verifiable |
| the declared interface fits | `p̂ ∈ 𝓕` | refutable (VF1) |
| the actor perceives no more than its declared view | `p̂_c` depends on `c` only through the view: linear equalities for a deterministic view, inequalities for a noisy one, closed either way | refutable, from records of the conditions the view merges (VF1) |
| the actor perceives more than its declared view | its negation | verifiable |
| tampered | `p̂` not grounded ([P50]), when the world is recorded | verifiable; with the world never recorded, verifiable only where the signals alone force tampering, through [P51]'s lower bound |
| unavoidable, with interface `j`; the cost of a limitation | `m_1 > 0`; `m_{j+1} − m_j > 0` | not about the record: decided by computation from the declarations |
| the actor pursues an objective (OPTIMIZERS) | `p̂` in the closure in `Δ` of a family of pursuits (v13's ray is closed in `Δ°`, not in `Δ`) | refutable, never verifiable |

**Proof.** Each row applies VF1 to the closed set named. `𝓕*` is closed: `M_A` is lower semicontinuous, as an infimum of
the jointly lower semicontinuous `KL` over a compact `A`, so `{f ∈ 𝓕 : M_A(f) ≤ M_A(𝓕)}` is closed. A deterministic view
makes `p̂_c = p̂_{c'}` for conditions it merges, linear equalities; a noisy one gives linear inequalities. The grounded
behaviours are linear ([P50](iv)). `m_j` depends on `A` and `𝓕_j` only. ∎

### VF3 — An excuse needs a route to its refutation
**Statement.** A sample in condition `c`, independent decisions all drawn from the actor's behaviour `p̂_c` there
([D11]), has a law that depends only on `p̂_c`. So the excuse "every behaviour the actor can produce in `c` lies in
`𝓕_c`" is tested by such a sample only through its consequence "`p̂_c ∈ 𝓕_c`": two actors with the same `p̂_c`, one
capable of more and one not, give samples of the same law. A record that is not a sample can show more: decisions drawn
from behaviours outside `𝓕_c` refute the excuse even when their average lies in it. Beyond the record of `c`, a record
of another condition `c'` bears on the excuse only through a declared link between the actor's feasible behaviours in
`c` and in `c'`, such as one set of policies faced with a different prompt or incentive; elicitation is the design of
such conditions. Further training makes another actor, so it bears on the excuse only if the declaration links the
trained actor's feasible behaviours to the untrained one's.

**In plain terms.** "It could not have done better" is checked only partly by watching what the actor did: a sample can
show that it did something the excuse says it cannot, never that it could not do more. The rest is checked by trying to
make it do better, in conditions declared to call on the same capability. Without such conditions, the excuse is
refutable only through what the actor actually did.

**Proof.** A sample's law is the product of `p̂_c`, so any test, a function of the sample, has the same law for two
actors with the same `p̂_c`. In a record that is not a sample, the decisions have their own behaviours `p̂_{c,i}`, and
one outside `𝓕_c` refutes the excuse, by VF1 applied to the decisions drawn from it. If the declaration constrains `c'`
too, a record there showing `p̂_{c'} ∉ 𝓕_{c'}` refutes the joint declaration, by VF1. ∎

## What the methodology justifies, and what it cannot

VF1–VF3 justify the *form* of every label: what kind of claim it makes, and what a record can do with it. An accusation
(breach, misaligned, tampered; culpable, with the interface taken as known) is verifiable; an excuse is at most
refutable: "could not tell" and "grounded" from ordinary records, "unavoidable" only partly from them and fully only
with conditions declared to call on the excused capability; a motive (pursues, games, fakes) is a refutable hypothesis;
and the size of a factor of FA1 is a computation on the declarations, whose meaning for the actor rests on an interface
that records can only refute. A label whose claim has the wrong status says more than a record can back: "unavoidable",
reported as a fact about the actor without such conditions, and "hidden misalignment", asserted of conditions no record
covers, which becomes verifiable once they are recorded and is bounded meanwhile only through views or feasible sets
that tie them to recorded ones ([D9], [P17]).

The methodology cannot justify the *word*: that the set a label names is the set the word means. That is decided on
paradigm cases, chosen for the word's sense and registered before computing, as L1 did; so every factor's name goes to
L2. Carcassi's method gives the necessary condition; the label test gives the rest.

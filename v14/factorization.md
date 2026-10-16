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
**Statement.** Let `A` be convex and closed, and `𝓕` linear ([D7]) and containing a full-support behaviour. Let
`(f°, a°)` minimize `KL(f‖a)` over `𝓕 × A`, with `a° ∈ Δ°` and `KL(f°‖a°) < ∞`, and suppose `f°` is the only behaviour
of `𝓕` with `M_A(f°) = M_A(𝓕)`. For `p̂ ∈ 𝓕`:
(i) `M_A(𝓕) = KL(f°‖a°)`, and `f°` is the behaviour of `𝓕` nearest to `a°`, minimizing `KL(·‖a°)` over `𝓕`.
(ii) `M_A(p̂) + R(p̂) = KL(p̂‖f°) + KL(f°‖a°)`, where `R(p̂) = KL(p̂‖a°) − M_A(p̂) ≥ 0`, with `R(p̂) = 0` exactly when
`a°` is a nearest acceptable behaviour of `p̂`.
(iii) The **culpability** `K(p̂) = KL(p̂‖f°)`, the evidence that the actor does not do the best it could, and the
**avoidable excess** `E(p̂) = M_A(p̂) − M_A(𝓕)` satisfy `K(p̂) = E(p̂) + R(p̂) ≥ E(p̂)`.

**In plain terms.** When the actor's limits are of the form "these averages are fixed", misalignment splits into two
divergences between named behaviours: the evidence that the actor is not at its best feasible behaviour, and the
evidence that this best is not acceptable. The split is exact up to one non-negative term, which credits the actor for
being near a different acceptable behaviour than the one its best feasible behaviour is nearest to.

**Proof.** (i) `inf_{(f,a)} KL(f‖a) = inf_f M_A(f) = M_A(𝓕)`, attained at `(f°, a°)`. For fixed `a°`, `f°` minimizes
`KL(·‖a°)` over `𝓕`, which [P15](i) makes unique, with full support, since `a° ∈ Δ°`.
(ii) [P15](iii) with `r = a°`: `KL(p̂‖a°) = KL(p̂‖f°) + KL(f°‖a°)` for every `p̂ ∈ 𝓕`. Substitute `KL(p̂‖a°) = M_A(p̂)
+ R(p̂)`. `R ≥ 0` because `a° ∈ A`, and `R = 0` exactly when `a°` attains `M_A(p̂)`.
(iii) Subtract `M_A(𝓕) = KL(f°‖a°)` from both sides of (ii). ∎

**Notes.** Checked on 200 random instances, with `A` v13's ordinal specification and `𝓕` fixing one average: `K = E +
R` to within `3e-13`, and the alternating minimization over `𝓕 × A` reaches, to within `2e-5`, the least misalignment
found by an independent search over `𝓕` (`probes/v14/RESULTS-factorization.md`, (2)). Two hypotheses carry the
equality. Linearity: a feasible set is linear when it fixes averages, as views ([D8]), an actor's resolution ([D4]) and
an environment whose responses are recorded with the actions are ([P15], Notes); when the actions are not recorded the
feasible set is a polytope, and only [P15](ii)'s inequality remains, so `K` and `E` need not be ordered: on 400 random
polytopes, `E > K` in 330 (`probes/v14/culpability.py`). And `a° ∈ Δ°`: a forbidden set breaks it, and its factor is
then read on the allowed outcomes, not yet written here.

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
then the factorization with exact labels, and FA3 the one with readings as evidence.

## What the earlier splits had found

Every exact split of v13, by the mechanism that makes it exact and the layer it belongs to.

| Split | Result | Mechanism | Layer | Its label |
|---|---|---|---|---|
| conditions, and the coarse and the fine within a condition | [B2], [P4](iii) | chain rule: always exact | CORE | exact |
| frequency, drift and dependence, along a record | [P54] | chain rule and the mixture identity: always exact | CORE | exact |
| shared and drift, across runs | [P45] | the mixture identity `Σ w_i KL(p_i‖r) = KL(p̄‖r) + D`: always exact | CORE | exact |
| reproducible and run-specific, between conditions | [P46] | chain rule: always exact | CORE | exact |
| ordinal and shape | [P36](iii), (iv) | Pythagorean equality at the default, inequality elsewhere | CORE, building a requirement | exact |
| coordination and individual | [P39] | chain rule: always exact | INTERFACE (`NOTES.md` §25: independence is no convex requirement) | exact as a number; "misalignment" only with an information structure |
| world and tampering | [P50](i), (ii) | chain rule: always exact | INTERFACE (the channel the actions cannot reach) | exact |
| the actor's resolution: best effort and what it cannot remove | [P8] | Pythagorean, linear | INTERFACE | exact |
| avoidable and unavoidable | [P15](v) | Pythagorean, linear, toward the nearest intended behaviour `p°` | INTERFACE | **overclaims**: below |
| departure: pursuit and misalignment | [P6] | Pythagorean, exponential family | OPTIMIZERS | exact |
| named and unexplained | [P44] | Pythagorean, linear | OPTIMIZERS | exact: it claims no minimum over alternatives |
| outer and strict inner | [P49](ii) | Pythagorean, via [P48] | OPTIMIZERS | exact |
| what tampering adds to net value | [P50](iv) | Pythagorean, linear | OPTIMIZERS | exact, at the trainer's intensity |

**The label that overclaims.** [P15](v) splits `M(p̂) = KL(p̂‖p*°) + KL(p*°‖p°)` exactly, and calls the second term the
unavoidable misalignment. It is unavoidable only toward `p°`, the intended behaviour nearest to the actor's own, at the
intensity the actor revealed. A feasible behaviour aimed at another intensity can have less misalignment. On 109 random
instances with one fixed average, the term exceeded the least misalignment of any feasible behaviour in 107, by up to
`0.86` nats (`probes/v14/RESULTS-factorization.md`, (1)). The split is right; the word "unavoidable" says more than it.
FA1 gives the exact unavoidable part, and FA2 the Pythagorean form with the right target. Recorded in `NOTES.md` §1.

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
dependence between decisions, as long as each decision, given the past, is drawn from `S`.

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
| culpable | `p̂ ∉ 𝓕*`, the feasible behaviours of least misalignment, closed since `M_A` is lower semicontinuous | verifiable, relative to the declared interface (VF1) |
| the declared interface fits | `p̂ ∈ 𝓕` | refutable (VF1) |
| the actor perceives no more than its declared view | `p̂_c` depends on `c` only through the view: linear equalities, closed | refutable, from records of the conditions the view merges (VF1) |
| the actor perceives more than its declared view | its negation | verifiable |
| tampered | `p̂` not grounded ([P50]), when the world is recorded | verifiable; with the world never recorded, neither, and only an interval ([P51]) |
| unavoidable, with interface `j`; the cost of a limitation | `m_1 > 0`; `m_{j+1} − m_j > 0` | not about the record: decided by computation from the declarations |
| the actor pursues an objective (OPTIMIZERS) | `p̂` on a closed family of pursuits | refutable, never verifiable |

**Proof.** Each row applies VF1 to the closed set named. `𝓕*` is closed: `M_A` is lower semicontinuous, as an infimum of
the jointly lower semicontinuous `KL` over a compact `A`, so `{f ∈ 𝓕 : M_A(f) ≤ M_A(𝓕)}` is closed. A view makes
`p̂_c = p̂_{c'}` for conditions it merges, linear equalities. The grounded behaviours are linear ([P50](iv)). `m_j`
depends on `A` and `𝓕_j` only. ∎

### VF3 — An excuse needs a route to its refutation
**Statement.** A record of decisions in condition `c` has a law that depends only on the actor's behaviour `p̂_c` there
([A1], [D11]). So the excuse "no behaviour outside `𝓕_c` was possible in `c`" is decided by no record of `c` beyond its
part "`p̂_c ∈ 𝓕_c`": two actors with the same `p̂_c`, one capable of more and one not, give records of the same law. The
excuse is refutable only if the interface is declared jointly for a set of conditions that includes conditions able to
reveal the capability, such as elicitation by a prompt, an incentive or further training, where a behaviour outside the
declared feasible set refutes it.

**In plain terms.** "It could not have done better" cannot be checked by watching what the actor did. It can only be
checked by trying to make it do better, somewhere the same capability would show. An excuse with no such test is
neither verifiable nor refutable, and by Carcassi's principle it is no statement about the actor.

**Proof.** The first sentence is the definition of a record ([D11]): decisions drawn from `p̂_c`. Any test is a
function of the record, so its law is the same for any two actors with the same `p̂_c`. If the interface constrains
other conditions too, a record there showing `p̂_{c'} ∉ 𝓕_{c'}` refutes the joint declaration, by VF1. ∎

## What the methodology justifies, and what it cannot

VF1–VF3 justify the *form* of every label: what kind of claim it makes, and what a record can do with it. An accusation
(breach, misaligned, culpable, tampered) is verifiable; an excuse (unavoidable, could not tell, grounded) is at most
refutable, and only with conditions that can reveal what is excused; a motive (pursues, games, fakes) is a refutable
hypothesis; and the size of a factor of FA1 is a computation on the declarations, whose meaning for the actor rests on
an interface that records can only refute. A label whose claim has the wrong status is inadmissible: "unavoidable",
reported without elicitation conditions, is one, and so is "hidden misalignment", misalignment in conditions no record
covers, unless views tie them to recorded ones ([P17]).

The methodology cannot justify the *word*: that the set a label names is the set the word means. That is decided on
paradigm cases, chosen for the word's sense and registered before computing, as L1 did; so every factor's name goes to
L2. Carcassi's method gives the necessary condition; the label test gives the rest.

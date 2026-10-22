<!-- theme: default -->
<!-- paginate: true -->
<!-- style: "section { font-size: 26px; }" -->

# Misalignment as a statistical object

Evidence, σ-algebras and exact factorizations, for mathematicians new to alignment

The v14 draft, in `v14/` (October 2026). v14 is not approved as a whole; the PI's decisions on it are rows of `NOTES.md`
§3.1. Every number here comes from a probe in `probes/`.

---

## The problem

An **actor** (a model, a person, a firm, an organism) acts on behalf of a **principal**, who wants something of it.

- *Misalignment*: the actor does what the principal does not accept.
- The field's words, such as reward hacking, deception and goal misgeneralization, are usually defined informally, one
  at a time.
- The question here: what is the mathematical object, what can a record of decisions establish about it, and how does
  it split into parts with honest names?

---

## Three naive answers, and why they fail

- *"Misalignment is a low reward."* The reward is a measurement someone designed; the actor can satisfy it and still do
  what the principal does not accept.
- *"Misalignment is a distance between the actor and a target."* Which target, which distance? A principal rarely wants
  one distribution, and distances do not say how fast a record convicts.
- *"Misalignment is a wrong goal inside the actor."* Goals are not observed; a frozen model has none to inspect, and is
  still misaligned when it breaks a rule.

The draft defines misalignment from behaviour and a declaration alone, and puts goals in a separate layer.

---

## The setting

- Finitely many **conditions** `c`, with frequencies `w_c` the actor does not choose; finitely many **outcomes** `x`.
- A **behaviour** `p = (p_c)_c`: a distribution on outcomes in each condition; equivalently, a distribution on pairs
  `(c, x)` with marginal `w`.
- A **record**: decisions in turn, each a condition and an outcome; not assumed independent.
- The principal's **specification**: a finite list of **requirements** `A_1, …, A_m`, each a set of behaviours,
  declared before the record is read. The acceptable set is `A = ∩_j A_j`.

Finiteness is what a record at finite precision decides; the general twins lift it.

---

## Why per-decision requirements are convex

**The mixture principle** (a premise, stated as a choice):

1. a schedule of acceptable behaviours, one per decision, is acceptable;
2. tests must keep their level whatever the dependence between decisions.

Independent draws from a mixture have the law of a random schedule of its components, so a valid test is valid at the
hull; no bet separates a set from its hull (VE2).

So per-decision requirements are convex and closed. A tail-risk limit is not (CVaR at 10%: two behaviours at `0.6`,
their mixture at `0.72`): it is declared **pooled**, judged on the average behaviour by confidence sequences (Q74).

---

## Every convex requirement is a list of budgets

**VK0.** If `S ⊆ Δ` is non-empty, convex and closed, then for every `x ∉ S` there is a budget `(g, b)` with
`E_a[g] ≤ b` on `S` and `E_x[g] > b`. So `S` is the intersection of the budgets it keeps.

The forms principals use are cases:

| Form | Set |
|---|---|
| forbidden set `C` | `a(C) = 0` |
| rate limit `(C, ε)` | `a(C) ≤ ε` |
| budget `(g, b)` | `E_a[g] ≤ b` |

The separating hyperplane theorem, from the nearest point. Some sets need infinitely many budgets.

---

## A family of targets and a reference

A **family of targets** `𝓚`: a closed convex cone of functions `G : X → ℝ` holding the constants: one objective, a
ranking's increasing functions, a span of candidates. A **reference** `r`: a base model, the previous version.

**TG1.** `D_𝓚(r) = {a : E_a[G] ≥ E_r[G] for every G ∈ 𝓚}` is convex, closed, contains `r`, and, for a finitely
generated `𝓚`, is the intersection of one budget per generator (a forbidden set where `E_r[G_i] = max G_i`).

- For a ranking: dominance on upper sets (VO1); first-order stochastic dominance when the ranking is total.
- If `−1_C ∈ 𝓚` and `r(C) = 0`, the family forbids `C` by itself.

"No worse than the reference on any target the principal might hold": unanimity, with no model of optimization.

---

## Doing no worse is not pursuing

The older reading (v13): accept `tilt(q, G) ∝ q·e^G` for any `G ∈ 𝓚`, the pursuit of some target.

**TG2.** For one target, and for a ranking, the pursuits lie inside `D_𝓚(q)`. If `Cov_q(G_1, G_2) < 0`, then
`tilt(q, t·G_1) ∉ D_𝓚(q)` for small `t > 0`.

- Four outcomes, `q` uniform, `G_1 = (0, 1, 2, 3)`, `G_2 = (3, 2, 0, 1)`: pursuing `G_1` at `t = 0.5` raises `E[G_1]`
  from `1.5` to `2.08` and lowers `E[G_2]` to `1.09`.
- v13's own measure has the form of a comparison with TG1's set, the actor as reference: for `p̂, q` of full support,
  `M(p̂) = KL(p̂‖q) − min_{p ∈ D_𝓚(p̂)} KL(p‖q)`.

---

## Misalignment

`M_A(p) = inf_{a ∈ A} KL(p‖a)`, in nats per decision, with the conditions' frequencies fixed.

Three readings, one number:

| Reading | Statement |
|---|---|
| large deviations | how fast a record becomes improbable for the acceptable behaviour that explains it best |
| betting | how fast the best fair bet against acceptance grows |
| geometry | the divergence to the reverse information projection onto `A` |

About `1/M` decisions give one nat of evidence.

---

## Sanov's rate

**SN1.** For any `A ⊆ Δ` and any empirical behaviour `s` of `n` decisions, with `k_n` the number of possible types,

`e^{−n·M_A(s)}/k_n ≤ sup_{a ∈ A} P_a(s) ≤ e^{−n·M_A(s)}`.

The method of types: for a composite null, the most favourable acceptable behaviour's probability of the record decays
at rate `M_A`. With four outcomes and one budget, the logarithm of the largest probability lies between the bounds at
`n = 20, 100, 500`.

---

## The best bet

A **bet** against `A`: `h ≥ 0` with `E_a[h] ≤ 1` for every `a ∈ A` (an e-variable).

**VE1.** If `A` is convex and closed, `sup_h E_p[log h] = M_A(p)`; when it is finite, it is attained by `h* = p/a*`,
where `a*` attains `M_A(p)`.

- Proof: Jensen for the upper bound; the first-order condition at `a*` for `E_a[h*] ≤ 1`.
- Known in general: the numeraire e-variable and the reverse information projection (Grünwald, de Heide and Koolen;
  Larsson, Ramdas and Ruf).
- **SN1(iii).** If `A` is not convex, bets reach only `M_{conv A} ≤ M_A`: counts charge a schedule of acceptable
  behaviours that no bet can. Two behaviours and an actor at their midpoint: `0.331` against `0`.

---

## Why KL, and this order

<style scoped>section { font-size: 21px; }</style>

| Step from "evidence" to the formula | Status |
|---|---|
| independent evidence adds: a logarithm | forced (Cauchy's functional equation) |
| bets fair under acceptance | forced, else wealth is no evidence |
| wealth valued by its long-run growth | a choice (Kelly); expected wealth gives Rényi order `∞` |
| `KL(p̂‖a)`: how improbable acceptance makes the record | forced, given that question; the other order is Stein's |
| the most favourable acceptable behaviour | from the literature (generalized likelihood ratio) |

Total variation and Wasserstein distances measure how far mass must move, not how fast a record convicts; a principal
who wants them declares them as requirements.

---

## Validity under any dependence

**VE3.** Decisions in turn; before each, an acceptable set `A_i` and a bet `h_i` against it, both possibly depending on
the past. If each decision, given the past, is drawn from some member of `A_i`, then

`P(Π_{i≤k} h_i(x_i) ≥ 1/α for some k ≤ n) ≤ α`.

Ville's inequality on a finite horizon: the wealth is a non-negative supermartingale. No model of how the actor
decides; the hypothesis is the declaration itself, read decision by decision.

---

## What a record can establish: Carcassi's methodology

Reverse physics (Carcassi and Aidala): a statement means what an experiment can do with it.

- **Verifiable**: some test succeeds in finite time if it is true. **Refutable**: its negation is verifiable.
- For statistical verification, the verifiable statements about behaviours are the open sets (Genin and Kelly).

**VF1.** For closed `S` with `∅ ≠ S ≠ Δ`: "`p ∉ S`" is verifiable and not refutable; "`p ∈ S`" is refutable and not
verifiable. A record can convict, never certify exactly.

Every label below gets a status: verifiable, refutable, neither, declared, or computed from the declarations.

---

## σ-algebras: three positions

On finitely many outcomes a σ-algebra is a partition into cells. Three parties have one each:

| Position | σ-algebra | Says |
|---|---|---|
| principal | `ℬ` | what matters |
| record | `ℛ` | what is seen: a grader's classes |
| actor | `𝒱` on conditions, `𝒜` on outcomes | what it can tell apart, act on |

For a partition `𝒢`: `M_A^𝒢(p) = inf_{a ∈ A} KL(p_𝒢‖a_𝒢)`, misalignment read on cell masses.

---

## RS1: grouping hides, refinement adds up

**RS1.** If `ℋ` refines `𝒢`, then `M_A^𝒢 ≤ M_A^ℋ`. For a chain `𝒢_1 ⊑ … ⊑ 𝒢_k` ending at the finest partition,

`M_A = M_A^{𝒢_1} + Σ_j (M_A^{𝒢_{j+1}} − M_A^{𝒢_j})`, every term non-negative.

- Proof: the chain rule, `KL(p_ℋ‖a_ℋ) = KL(p_𝒢‖a_𝒢) + Σ_C p(C)·KL(p_ℋ(·|C)‖a_ℋ(·|C))`, then the infimum.
- Data processing for deterministic groupings, carried to any acceptable set.
- **Label status**: "a refinement reveals misalignment" is verifiable from records at the finer σ-algebra when `A` is
  convex, closed and has a full-support member, so that every `M_A^𝒢` is continuous.

---

## RS2 and RS3: the record and the principal

**RS2.** A bet constant on the cells of `ℛ` grows at most at `M_A^ℛ(p)`, and one attains it: `p_ℛ/a*_ℛ` on cells. A
record at `ℛ` convicts at exactly the coarse rate, by VE3, with no model of what happens inside cells.

**RS3.** If membership in `A` depends only on `a_ℬ`, then `M_A = M_A^ℬ`: telling apart what the principal does not care
about reveals nothing. The nearest acceptable behaviour can keep the actor's split inside each cell.

**Label status**: "misaligned as far as `ℛ` shows" is verifiable from records at `ℛ`; indifference is declared.

---

## RS4: hidden misalignment

`𝒫 = {p' : p'_ℛ = p_ℛ}`: what a record at `ℛ` cannot tell from `p`. Hidden part `H_ℛ = M_A − M_A^ℛ ≥ 0`.

**RS4.** `min_{𝒫} M_A = M_A^ℛ(p)`, attained by splitting each cell as `a*` does. So `M_A(p) ∈ [M_A^ℛ(p), max_{𝒫} M_A]`,
the maximum at a vertex of `𝒫` when `A` is convex, and "`H_ℛ > 0`" is **neither verifiable nor refutable** from samples
at `ℛ` whenever `M_A` varies on `𝒫`: every test has the same law throughout `𝒫`.

A declared feasible set narrows the interval; only a finer record or a declaration of what the actor can do inside cells
bounds the hidden part.

---

## RS5: the actor's σ-algebras are linear

**RS5.** (i) An actor whose choice depends on the condition only through its view's cell, choosing outcomes freely, has
the feasible set `{p : p(·|c) = p(·|c')` for `c, c'` in one cell`}`. (ii) An actor that chooses only cell masses, the
environment splitting each cell by a fixed full-support `e(·|A)`, has `{p : p(x) = p(A)·e(x|A)}`.

Both are linear (they fix averages) and contain a full-support behaviour. A coarser view gives a smaller set; a coarser
resolution does when the environment's splits are consistent, `e(x|A) = e(A_i|A)·e(x|A_i)`. Then coarse perception and
coarse action are exact factors of the next slides.

With an environment kernel between actions and outcomes, the feasible set is a polytope: the exact factorization
survives, the Pythagorean one does not.

---

## The interface and culpability

An **interface** `(U, Z, V, E)`: actions, signals with a view `V(z|c)`, an environment `E(x|c, u)`. Its **feasible set**
`𝓕` is the closure of the behaviours its policies produce; it is convex, and every closed convex set is one (IN1).

- **Unavoidable**: `m(𝓕) = inf_{f ∈ 𝓕} M_A(f)`. **Best feasible**: `𝓕* = {f ∈ 𝓕 : M_A(f) = m(𝓕)}`, convex and closed.
- **Culpability**: `K(p̂) = inf_{f ∈ 𝓕*} KL(p̂‖f) = M_{𝓕*}(p̂)`, misalignment against a derived requirement, so VE1 and
  VE3 apply unchanged.
- **Avoidable excess**: `E(p̂) = M_A(p̂) − m(𝓕)`, the size.
- **At a declared care margin `δ`** (Q74): `𝓕*_δ = {f ∈ 𝓕 : M_A(f) ≤ m(𝓕) + δ}`, the verdict `p̂ ∉ 𝓕*_δ`.

INTERFACE adds requirements, not new measures.

---

## FA1: the exact factorization by capabilities

**FA1.** For `𝓕_1 ⊇ 𝓕_2 ⊇ … ⊇ 𝓕_k ∋ p̂`, any `A`, `m_j = m(𝓕_j)`:

`M_A(p̂) = m_1 + Σ_j (m_{j+1} − m_j) + (M_A(p̂) − m_k)`, every term non-negative.

Unavoidable even for the most capable declarable actor; the cost of each capability removed; what this actor could have
avoided. Telescoping; no convexity or linearity needed.

**Label status**: the sizes `m_j` are computed from the declarations; their meaning for the actor rests on an interface
that records can only refute.

---

## FA2: the Pythagorean form

**FA2.** For `𝓕` linear with a full-support member, `A` closed, `m(𝓕) < ∞`, `(f°, a°)` minimizing `KL` over `𝓕 × A`
with `a° ∈ Δ°`, and every `f ∈ 𝓕*` with a nearest acceptable `a_f ∈ Δ°`:

`M_A(p̂) + R(p̂) = KL(p̂‖f°) + KL(f°‖a°)`, `R(p̂) = KL(p̂‖a°) − M_A(p̂) ≥ 0`, and `K = E + min_{f∈𝓕*} R_f ≥ E`.

Csiszár's Pythagorean identity for linear families. On polytopes only the inequality survives, and `K`, `E` are not
ordered (`E > K` in 330 of 400 random instances).

**FA3** chains it toward a fixed target; each term is then a divergence between named behaviours.

---

## A label that said too much

v13's [P15](v): `M(p̂) = KL(p̂‖p*°) + KL(p*°‖p°)`, the second term called **unavoidable**.

- The split is exact. The word is not: the term is unavoidable only toward `p°`, the intended behaviour nearest to the
  actor's own.
- On 109 random instances, it exceeded the least misalignment of any feasible behaviour in 107, by up to `0.86` nats.

The lesson: Carcassi's statuses justify what *kind* of claim a label makes; whether the word fits is a separate test,
on paradigm cases registered before computing.

---

## The factorizations of v14

<style scoped>section { font-size: 19px; }</style>

| Result | Splits | Mechanism | Exact | Label status |
|---|---|---|---|---|
| RS1 | by the record's σ-algebra | chain rule | always | verifiable at the finer σ-algebra, if continuous |
| RS3 | the principal's indifference | chain rule | always | declared |
| RS4 | seen and hidden | chain rule | always | hidden: neither |
| FA1 | by capabilities | telescoping | always | `m_j`: computed; the last term: verifiable |
| FA2, FA3 | by linear interfaces | Pythagoras | under hypotheses | computed; evidence rates |
| RS5 | view, resolution | FA1, FA2 | as FA1, FA2 | computed |
| VK4 | by requirements, in a chosen order | telescoping | always | as RS1 |
| SH1 | a shaped actor: outer and the course's remainder | FA1 | if it meets its feedback | computed; verifiable |

---

## The example

A question-answering model, a **new** version against the **previous** one.

- Conditions: benign `0.60`, borderline `0.25`, adversarial `0.15`.
- Outcomes: `S` correct short, `L` correct long, `R` refusal, `W` wrong, `H` harmful.
- Actions: answer short, answer long, refuse; the environment turns each into outcomes, by condition.
- Views: the previous model saw all three conditions; the new one **cannot tell borderline from adversarial**.

`probes/slides/qa_model.py` computes every number.

---

## The specification and the three σ-algebras

- **R1**: harmful answers at most `1%` of decisions (a pooled rate limit).
- **R2**: the family generated by "correct" and "not incorrect", against the previous model: at least its share of
  correct answers, at most its share of incorrect ones (TG1).

| σ-algebra | Cells |
|---|---|
| finest | `S`, `L`, `R`, `W`, `H` |
| the principal's `ℬ` | `{S, L}`, `R`, `W`, `H`: short and long alike |
| the record's `ℛ`, a grader | `{S, L}`, `R`, `{W, H}`: cannot tell wrong from harmful |

Both requirements are stated at `ℬ`; R2 also at `ℛ`, R1 not.

---

## Verdicts and evidence

| Requirement | Previous | New | Verdict for the new |
|---|---|---|---|
| R1 harmful at most 1% | 0.60% | 5.00% | breached |
| R2 correct at least 64.06% | 64.06% | 67.11% | met |
| R2 incorrect at most 4.93% | 4.93% | 9.89% | breached |

Misalignment, nats per decision: R1 `0.0455` (VK6; the pooled formula gives `0.0413`, a lower bound); R2 `0.0227`; both
`0.0474`. The joint is not the sum: requirements split exactly only in a chosen order.

---

## Factoring by σ-algebras

Against both requirements, along `ℛ ⊑ ℬ ⊑` finest (RS1, RS3):

| Part | Nats per decision |
|---|---|
| seen by the grader, `M^ℛ` | 0.0227 |
| revealed by telling wrong from harmful | 0.0247 |
| revealed by telling short from long | 0 (RS3) |
| total | 0.0474 |

From the grader's record alone the misalignment lies in `[0.0227, 0.1483]` (RS4), and R1 is invisible: its misalignment
at `ℛ` is `0`.

---

## Factoring by capabilities

<style scoped>section { font-size: 22px; }</style>

Against both requirements, along the views full ⊇ the new model's (FA1; with an environment kernel, a polytope):

| Part | Nats per decision |
|---|---|
| unavoidable with a full view | 0 |
| the cost of not telling borderline from adversarial | 0.0037 |
| avoidable with the new model's view, `E` | 0.0438 |
| total | 0.0474 |

- The best its view allows: answer benign questions long; refuse 83% of suspicious ones and answer the rest long.
- Culpability `K = ∞`: the best behaviours never answer a benign question short, nor refuse one, and the new model does
  both. `K` is `0` or `∞` for most actors; report the avoidable excess `E` as the size.

---

## What a record shows

<style scoped>section { font-size: 22px; }</style>

Bets refitted before each decision, at level 5% (VE3); the share of records that accuse the new model:

| Decisions | R2's incorrect share, from the grader's cells (RS2) | R1, from a record that tells `W` from `H` |
|---|---|---|
| 100 | 3.7% | 3.5% |
| 300 | 47.6% | 70.8% |
| 1000 | 99.9% | 100% |

- From the grader's record no bet against R1 can grow: its misalignment at `ℛ` is `0` (RS2).
- Sanov (SN1): for counts over 400 decisions with shares near the new model's, the most favourable acceptable model
  gives a probability of about `e^{−400·0.0474} = 5.7·10⁻⁹`, up to the factor `k_n`.

---

## What is open

- **Certification**: v14 convicts; certifying "breach rate at most `ε`" needs confidence sequences from betting, known
  in the literature and not yet in the draft.
- **Achievability**: bets refitted from the record reach the best growth rate; answered for independent decisions in
  the literature, open under dependence (H46).
- **A blind spot of order `√n`**, a hunch (H43): shifts of `1/√(n·I)` per decision are detected over `n` decisions with
  power bounded away from `1`, while they cost about `√(n/I)` in all.
- **Continua**: compactness of the acceptable closure decides whether one fixed test catches misalignment (H41).
- **Graders make errors** (H47); a **reference known from samples** carries uncertainty into its requirement.

---

## Summary

- Misalignment is the large-deviation rate, the best bet's growth and an information projection at once, on convex
  requirements, and each convex requirement is a list of budgets.
- σ-algebras sort what matters (the principal), what is seen (the record) and what can be done (the actor); each has an
  exact factorization, and the hidden part is neither verifiable nor refutable from the record that hides it.
- Every factor's label has a verification status by Carcassi's methodology; whether its word fits is tested separately,
  and the example shows why: culpability as KL to the best behaviours is right as evidence and useless as a size.

`v14/README.md` for the design; `v14/resolution.md`, `targets.md`, `factorization.md` for the proofs.

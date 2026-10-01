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

**One that worked.** "Misalignment of a coarse actor grows with effort" was the natural claim from main's B1 ("rises with
budget"). A 400-instance probe before writing it found 123 non-monotone cases, so [P8] claims only the small-effort law
and exhibits a counterexample. The rule "a shape claim needs a random sample before it is said" (main, §1) paid off.

## 2. Is the core a compelling standard yet?

Not yet: a credible foundation. The PI has the full assessment. Progress against the gaps listed after the second
review:

| Gap | State |
|---|---|
| everything is relative to a declared specification; no sensitivity result | **closed by [P10]**: an error in the default moves misalignment by at most its spread, and an error in the objective by at most the revealed intensity times its spread |
| no resolution: cannot say "I don't care about these details" | **closed by section 4**: [P7] forgives exactly the within-cell departure; [P8] gives the coarse actor's unavoidable misalignment and its small-effort law |
| no stakes report | **closed by [P9]**: the shortfall at matched intensity splits into misalignment, under-pursuit and anti-pursuit; misalignment is scale-free, stakes are not |
| identifiability: what can be read from behaviour, and what cannot | **closed in part by section 6**: [P11] the misaligned share at the start of any change; [P12] pass-through is identified from behaviour alone, and revealed objectives certify an actor's distinctions but cannot prove their absence |
| no estimation layer | open: the deviance identity of [P5] is the way in; [P12](i) needs it to be tested on data |
| known mathematics, organization not yet shown across disciplines | **addressed by `ontologies/`**: five disciplines, each with typed slots, one known result, and claims labelled as consequences, predictions or readings (lint rule R10). Next: worked cases, which need data |
| what one change of behaviour gains, not only what it misaligns | **closed by [P13]**: the average moves at the covariance rate (the Price equation), and at the start each unit of departure gains `cos θ` of the objective's spread |
| outcomes that are partly fixed before the actor acts (contexts) | **open, found by the ontologies**: see the design question below |

**Deferred from identifiability.** The "dynamic rank" (the dimension of the span of the revealed objectives along a
path, modulo constants) generalizes [P3] beyond rank one. It adds no verdict the core needs yet: [P3] already says when a
single objective explains a path. It stays on `main` until an ontology needs it; none did.

## 3. Open requests and recommendations

Everything waiting on the PI or deferred by agreement, in one place. Nothing here is applied to the core. Each entry says
what it is, the evidence for it, and what would settle it. The PI has asked to return to these later, not to push them
now.

### 3.1 Decisions for the PI

| # | Decision | Recommendation | Evidence | Status |
|---|---|---|---|---|
| Q1 | Contexts: one shared intensity, or a free intensity per context (below) | one shared intensity | four of five ontologies need contexts; RLHF's single `β` is exactly this | open |
| Q2 | Whether the core may grow past "about a dozen items" (README) or must be consolidated (§3.3, C2–C3) | consolidate: 19 items to about 15 | the slim rule is a working agreement, now broken | **decided by the PI**: no merging for its own sake; instead the core keeps only premises and universal definitions, and derivations move out (§4) |
| Q3 | Which of the proposed additions (§3.3) enter the core, and in what order | C1, then C4, then C5 | C1 closes the one circular step in the justification; C4 is what every ontology lacked | **decided by the PI**: C1 yes; C4 yes if natural (it is, for linear feasible sets: §4.2); C9 (a standard) yes; scope stated. Blueprint §4 awaits approval |

### 3.2 Papers and data the PI could supply

| # | For | What is needed | Why | Note |
|---|---|---|---|---|
| D1 | humans (fine) | Gneezy and Rustichini (2000), weekly counts of late parents per centre | the pair test (fine, removal) of `ontologies/humans.md` | a copy of the data appears to be public (`users.stat.ufl.edu/~winner/data/fineprice.txt`, seen in a search result, not opened) |
| D2 | humans (defaults) | Madrian and Shea (2001), the distribution of contribution rates in each cohort | the pass-through ratio test | the paper itself; the 403 from publishers blocks it here |
| D3 | machine learning | samples from an initial policy, scored by a gold and a proxy reward model | the best-of-`n` slope and the covariance-at-the-peak predictions | an open RLHF setup would do; Gao et al.'s own data is not known to be public |
| D4 | biology | Chippindale et al. (2001), the hemiclone fitness values per sex | the angle and the shortfall of ordinary selection | supplementary data, if any |
| D5 | institutions | Dranove et al. (2003) | the reading only; Medicare data are not public | low priority |

Every test is pre-registered and pushed before any computation (README rules).

### 3.3 Proposed changes to the core (from the third review; none applied)

| # | Proposal | Kind | Evidence so far |
|---|---|---|---|
| C1 | **The cost is forced.** Among differentiable costs `c(p)`, the optima of `E_p[F] − c(p)/t` lie on the pursuit ray for every `F` exactly when `c` is an increasing function of `KL(p‖q)`; additivity over independent decisions makes it `KL` itself. This closes the one circular step: D3 chose net value with a KL cost, and [P4] then showed KL measures it | new part of [P4], with proof and check | proof sketched; probe: χ², reverse KL and squared Hellinger put the optima off the ray at every intensity (KL distance up to 0.46), while `KL + KL²` keeps them on it (3e-14) |
| C2 | **One angle governs the start of a change.** Merge [P11] and [P13](ii): share `sin²θ`, gain `cos θ·σ`, shortfall `(1 − cos θ)·σ` | merge | same expansion, same hypotheses |
| C3 | **The Price equation belongs with the replicator equation.** Move [P13](i) to [P2] as (iv) | move | it is a property of any path, with no default |
| C4 | **Feasible behaviours.** The actor can produce only a set `𝓕` of behaviours. By [P4](i), the best net value within `𝓕` is the behaviour of `𝓕` nearest to the pursuit, `argmin_{p∈𝓕} KL(p‖p_{F,t})`. [P8](ii) is the case of a coarse actor; contexts are the case of fixed context masses; sequential decisions with stochastic dynamics are the case of policies. The unavoidable misalignment is `inf_{p∈𝓕} M(p)`, the distance from what the actor can do to what is intended, which separates "cannot" from "will not" | new definition and proposition; generalizes [D4]'s actor position and answers Q1 | derivation is one line from [P4](i); the decomposition of `M` into unavoidable and chosen parts is not yet known to hold beyond an inequality |
| C5 | **Estimation.** For `n` independent decisions from an actor that does pursue `F` at an interior intensity, `2n·M(p̂_n)` is asymptotically χ² with `|X| − 2` degrees of freedom (Wilks); at the boundary `t* = 0` a chi-bar-square mixture | new proposition | probe: means 1.08, 2.98, 6.09 and variances 2.15, 5.97, 11.5 for `|X|` = 3, 5, 8 (1500 runs, `n` = 2000) |
| C6 | **A floor.** A principal for whom doing nothing fails declares `{p_{F,t} : t ≥ t_min}`. By the convexity in the proof of [P5](iv), the nearest intensity is `max(t*, t_min)` | remark | derivable; no check yet |
| C7 | **Ordinal objectives.** A principal who ranks outcomes without values declares the tilts of `q` by every function that is non-decreasing in `F`. That set is closed, contains the ray, and its misalignment is a convex program (isotonic regression in KL). Best-of-`n` on a proxy is aligned with the proxy's ranking, and misaligned with its values: a case where the slot changes a verdict, as [D3] requires | new definition and proposition | convexity and closedness argued, not checked |
| C8 | **Several principals.** Union of intended sets gives the minimum of the misalignments; intersection gives at least their maximum; conflict between two objectives is their angle at the default ([P11]), as the biology ontology used | remark | trivial, but needed for chains of delegation |
| C9 | **A reporting standard.** What a misalignment report must contain: the declaration (default, intended set, resolution, date), the departure split ([P6]), misalignment with its estimation error, the shortfall ([D5]), and sensitivity ([P10]). This is what would make the core usable as a standard | a section of the README, not an item | — |

**To verify.** [D2]'s justification says that the check of [P3] exercises mixture paths. A read-only search to confirm it
was blocked by a permission prompt during the third review, so this is unverified.

### 3.4 Contexts (Q1)

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

**Order next.** As the PI decides: Q1–Q3 above, then worked cases on the data of §3.2, each pre-registered.

## 4. Blueprint for v9 (awaiting the PI's approval; nothing applied)

The PI's principle: the core holds what cannot be derived, and the definitions used everywhere. Derivations live
elsewhere, split by topic, because splitting concepts aids clarity more than merging them.

### 4.1 Premises and the cost theorem (C1, approved)

What cannot be derived, stated as premises. Everything else is a definition or a derived result.

| # | Premise | In plain terms | Replaces |
|---|---|---|---|
| A1 | **Behaviour suffices.** Alignment is judged from the distribution of outcomes alone, over finitely many outcomes. | We judge what happens, not how it was produced. | D1's "why" (behaviour is any distribution) |
| A2 | **Pursuit is steepest climb.** Pursuing `F` climbs `E_p[F]` as steeply as possible, in a geometry that does not depend on how finely outcomes are described. | Wanting more of something means moving toward it by the shortest route, however finely we describe what happens. | D2's "why" (canonical, given one premise) |
| A3 | **Pursuit is the best trade-off.** At intensity `t`, pursuit maximizes the objective's average minus `1/t` times a cost of departing from the default, a cost that depends only on the behaviour. | Pursuing harder means accepting a higher cost of change for more of the objective. | P4's definition of net value with a KL cost |
| A4 | **Misalignment is value lost.** Misalignment is the least net value the actual behaviour loses against an acceptable behaviour, each acceptable behaviour judged by its own objective, in nats. | Misalignment is how much worse the actor did than the closest acceptable way of acting, by that way's own standard. | D3's formula, which becomes a result |
| A5 | **Declared before.** A specification is fixed before, and without using, the behaviour it judges. | Decide what counts as acceptable before looking. | D3's rule of use |

**Theorem C1 (the cost is forced).** Let `q ∈ Δ°` and `c : Δ° → ℝ` be differentiable. Then for every `F` and every
`t > 0` the pursuit `p_{F,t}` maximizes `E_p[F] − c(p)/t` if and only if `c = KL(·‖q) + C` for a constant `C`.
*Proof.* If: [P4](i). Only if: at the interior maximizer `p_{F,t}`, the derivative of `E_p[F] − c(p)/t` vanishes along
every tangent direction, so `∇c(p) − t·F` is constant across outcomes. Since `t·F = log(p/q) + log E_q[e^{tF}]`,
`∇c(p) − log(p/q)` is constant across outcomes. Every `p ∈ Δ°` is a pursuit (`p = p_{G,1}` with `G = log(p/q)`,
[P1](i)), so this holds at every `p ∈ Δ°`. Then `c − KL(·‖q)` has zero derivative along every tangent direction on
the connected set `Δ°`, and is constant. ∎
*Notes.* A2 and A3 are independent motivations, geometric and economic; C1 says they agree in exactly one way. If
A3 only asked that the optima lie on the ray, at some intensity, any increasing function of KL would do (checked:
`KL + KL²` keeps the optima on the ray, to 3e-14). Reading `t` as the inverse price removes that freedom. χ², reverse
KL and squared Hellinger put the optima off the ray at every intensity (KL distance up to 0.46).
*Consequence.* With A4, misalignment is `inf_{p∈𝓘} KL(p̂‖p)` by [P4](ii), including the direction of KL. The value
lost in nats, `t·(J_t(p_{F,t}) − J_t(p̂)) = KL(p̂‖p_{F,t})`, depends only on the product `t·F`, so it does not depend
on how an acceptable behaviour is written as an objective and an intensity ([P1](ii)).

### 4.2 Feasibility (C4): is "cannot versus will not" natural?

Yes, for a precise class of feasible sets, and the answer is both geometric and economic.

**Definition (draft).** The actor's **feasible set** `𝓕 ⊆ Δ` is the set of behaviours it can produce. It is
**linear** if it is cut out by linear constraints, `𝓕 = {p ∈ Δ : E_p[f_i] = a_i, i = 1..m}`: the actor cannot change
certain averages.

**Theorem C4 (draft).** Let `𝓕` be linear and contain a full-support behaviour, and let `r ∈ Δ°`.
(i) There is a unique `p* ∈ 𝓕` nearest to `r`, `p* = argmin_{p∈𝓕} KL(p‖r)`; it has full support, and
`p* = tilt(r, Σ θ_i f_i)` for some `θ`.
(ii) For every `p ∈ 𝓕`, `KL(p‖r) = KL(p‖p*) + KL(p*‖r)`.
(iii) If `r = p_{F,t}`, then `p*` maximizes net value over `𝓕`, and `J_t(p*) − J_t(p) = KL(p‖p*)/t` (value the actor
left unclaimed: *will not*), while `J_t(p_{F,t}) − J_t(p*) = KL(p*‖p_{F,t})/t` (value no feasible behaviour can reach:
*cannot*).
(iv) Under the standard specification, with `p°` the nearest intended behaviour of `p̂ ∈ 𝓕` and `p*°` its nearest
feasible behaviour, `M(p̂) = KL(p̂‖p*°) + KL(p*°‖p°)`.
*Proof of (ii).* With `p* = r·e^{θ·f}/Z`, `KL(p‖r) − KL(p‖p*) = E_p[θ·f] − log Z = θ·a − log Z`, the same for every
`p ∈ 𝓕`; at `p = p*` it is `KL(p*‖r)`. (iii) is (ii) with [P4](i). ∎ This is Csiszár's Pythagorean theorem for linear
families (Csiszár 1975, *Annals of Probability* 3(1); to be verified before citing).

**Why this is natural.** Two independent readings coincide: the Pythagorean theorem of information geometry (a linear
family is flat in the mixture sense, and the projection meets it at a right angle in the Fisher metric), and the exact
accounting of net value from [P4](i). And the three cases met so far are all linear:

| Case | Constraints | Nearest feasible behaviour | *Cannot* | Probe (max error) |
|---|---|---|---|---|
| contexts | fixed context masses, `E_p[1_C] = q(C)` | pursuit within each context at one shared intensity: Q1's option A, now derived | `KL(q_𝒞‖(p_{F,t})_𝒞)`: how much the full pursuit would have reweighted contexts | 2.7e-15 |
| coarse actor ([D4]) | fixed ratios inside cells, `p(x)q(y) − p(y)q(x) = 0` | `tilt(q, t·F̄)`: [P8](ii) becomes a corollary | the Jensen gap of [P8](iii) | 1.8e-15 |
| policies in a random environment | `p(h, a, s') = P(s'|h, a)·p(h, a)` | the maximum-entropy policy (soft Bellman recursion, with the expectation over the environment) | positive when the environment is random (median 0.46 nats); zero when it is deterministic (4e-16) | 2.7e-15 |

Random linear constraints: 3.7e-11 (solver tolerance). No policy beat the projection in net value (1500 tries).

**Where it stops.** For a convex feasible set that is not linear, (ii) holds only as an inequality,
`KL(p‖r) ≥ KL(p‖p*) + KL(p*‖r)` (no violation in about 6000 cases, strict in 1916). For a non-convex set, such as a
parametric family limited by capacity, even the inequality fails (3319 of 6300 cases on a curved family); only the
lower bound `M(p̂) ≥ inf_{p∈𝓕} M(p)` survives. So: exact split for linear constraints, an inequality for convex
ones, and nothing beyond the lower bound for capacity limits.

**Common sense.** "You cannot be blamed for the dice": in a random environment the joint tilt is out of reach, and
the core charges that part to *cannot*, not to the actor. In a deterministic environment the actor can reach the
intended behaviour, and nothing is excused.

### 4.3 Layout

| Place | Holds | Rule |
|---|---|---|
| `CORE.md` | scope (in and out), the premises A1–A5, and the universal definitions: outcomes and behaviours, default and pursuit, specification and misalignment, resolution, feasibility, stakes, intervention | a Statement uses only earlier core items; a "why" may cite derived results, provided the dependencies stay acyclic |
| `derived/` (name to confirm; `tools/` already holds the linter) | one file per topic: tilts and paths, value and the cost theorem, misalignment, resolution, feasibility, stakes and sensitivity, identifiability | every result has a proof and checks; item ids stay as they are, so no reference elsewhere breaks |
| `STANDARD.md` | the reporting standard: what a misalignment report must declare and report | each required field names the core item it reports |
| lint | R5 becomes "the dependency graph is acyclic" across files, with Statements in `CORE.md` depending only on `CORE.md` | tested like the other rules |

**Out of scope (draft for `CORE.md` §0).** Interaction among several actors, and actors who respond to the
measurement itself beyond a fixed intervention; aggregating the preferences of several principals (only set
operations on specifications); continuous outcomes (deferred, with integrability conditions); explanations of why an
actor behaves as it does; and which objective is right, which the principal declares and the core does not choose.

**Questions for the PI.** (1) The name of the folder for derived results. (2) Whether premises become their own kind
of item (A), checked by lint like definitions. (3) Whether stakes and interventions count as universal definitions
(they are inputs to every report), or move with their results.

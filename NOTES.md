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
| Q2 | Whether the core may grow past "about a dozen items" (README) or must be consolidated (§3.3, C2–C3) | consolidate: 19 items to about 15 | the slim rule is a working agreement, now broken | open |
| Q3 | Which of the proposed additions (§3.3) enter the core, and in what order | C1, then C4, then C5 | C1 closes the one circular step in the justification; C4 is what every ontology lacked | open |

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

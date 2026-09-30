# NOTES — the executor's working notes

Not part of the core, and not checked by lint. Blunt on purpose. A hunch here is not a claim: nothing moves into
`CORE.md` without a proof and a check.

## 1. Failure modes

The full table, with its evidence, is on `main`: `70 Project/NOTES_claude.md` §1. Two more from building this core:

| Failure mode | Evidence | Countermeasure |
|---|---|---|
| **A check that omits the constraint it tests** | the ray-minimizer check never required `t* ≥ 0`; a mutant that pursued `−F` passed | mutation-test every new check before recording it: break the mathematics on purpose and watch it fail |
| **A tolerance without its scale, again** | the ray-closedness check compared a tight bound with no rounding margin (1.79134602e-43 against itself) | every comparison gets the relative margin of `EXACT`, including the "obvious" ones |
| **A justification leaning on a later result** | D3 cited P5 while P5 came after it; lint rule R5 caught it | keep R5; write the "why" from what is above |

## 2. Terminology left for the PI

- **declaration → specification?** "Specification" is the word in AI safety (specification gaming, misspecification) and
  in formal verification (the set of acceptable behaviours). The PI chose "declaration"; D3's Notes give the
  correspondence. My recommendation: keep "declaration" for the act, and say "specification" for what is declared, if
  the PI wants the bridge in the text.
- **intended / acceptable.** Formal "intended", plain "acceptable". Consistent now; revisit if readers stumble.
- **reference → default.** Done in this step (D2). It matches behavioural economics and the "do nothing" reading; the
  RL name (reference policy) is in D2's Notes.

## 3. Correspondences with the literature, not yet confident enough for the core

- **The centred revealed objective `F_s − E[F_s]` as the advantage function.** For natural policy gradient on a
  softmax policy, the log-policy moves along the advantage (Kakade 2001; Agarwal et al. 2021). The exact statement depends
  on the algorithm; check it before promoting, with the dynamics section.
- **P5's third case as underspecification** (D'Amour et al. 2020): many behaviours are equally good under the
  objective, and the choice among them is left to the actor, which the default then judges. Promote with the resolution
  item if the mapping survives.
- **`2n·M(p̂)` as a test statistic.** By Wilks' theorem it is roughly χ² with `|X| − 2` degrees of freedom when the actor
  pursues `F`, except near `t* = 0`, where the half-ray boundary gives a mixture (chi-bar-square). This is the bridge to
  estimation, and it needs its own item and checks. The identity itself is in P5's Notes, checked.
- **The pursuit part `KL(p°‖q)` as "optimization pressure"** in the reward-overoptimization curves of Gao, Schulman and
  Hilton (2023): the gold score should track the pursuit part, and the proxy–gold gap the misaligned part. This is the
  first real test for the ML discipline.
- **The misaligned share `M/KL(p̂‖q)`.** It is tempting as a normalized index. Distrust it: it is 0/0 at small
  departures, and a share hides the scale (main's R8-1 lesson). It is in P6's Notes as a reading only.
- **"Evidence rate" as a Chernoff–Stein exponent.** The lemma would turn `M` into a testing exponent, but the direction
  of KL decides which error it governs. The core uses only the expected log-likelihood ratio, which needs no lemma.
  Don't upgrade the claim before working out the direction.
- **The meet σ-algebra as common knowledge** (Aumann 1976), and the join, with the default filling in, for the next
  section. The Jensen gap `−log E_q[exp(E_q[b|𝒜])]` is the retention cost (checked in the scratchpad only).

## 4. Is the core a compelling standard yet?

Not yet. It is a credible foundation, and I told the PI so. The reasons, so the next session can check progress
against them:

**What makes it credible.**
- Every object is justified twice. The pursuit ray is the steepest climb in the only geometry that does not depend on
  how finely outcomes are described (D2), and it is the set of best behaviours for the net value at every price (P4).
- The score has three readings that agree: net value lost (P4), nats of evidence per decision (D3), and a deviance
  (P5's Notes).
- The departure splits exactly into pursuit and misalignment (P6).
- No actor model is assumed, and every claim has a proof and a mutation-tested check.

**What a sceptical reader would still say.**
1. Everything is relative to a declaration, and real principals rarely write one down. The core measures misalignment
   given intent. It says nothing yet about eliciting intent, nor about how sensitive `M` is to a slightly wrong default
   or objective. A standard needs that sensitivity result.
2. There is no resolution yet, so the core cannot express the most common real specification: "I don't care about these
   details". P5's third case shows the gap already.
3. There is no stakes report yet. Nats of misalignment say nothing about how much of `F` is lost at the same departure.
4. There is no estimation layer. `M` of an empirical distribution is biased upward at small samples. The deviance
   identity is the way in.
5. The mathematics is known (exponential families, I-projections, replicator dynamics, MaxEnt IRL). That is by design,
   but the claim to be a standard rests on organizing it across disciplines better than the alternatives, and that is
   not shown until the four worked cases exist.

**Order I would take next.** The resolution (σ-algebras) first, because it fixes gap 2 and is needed for the
identifiability items. Then stakes and sensitivity, which are small. Then identifiability dynamics. Then one worked case
per discipline.

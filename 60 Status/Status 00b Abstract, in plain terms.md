---
id: "Status 00b Abstract, in plain terms"
type: "section"
title: "Abstract, in plain terms"
part: "status"
order: 1
updated: "2026-09-26"
---
## Abstract, in plain terms

How much of this to believe, and why. **Read this before quoting anything from the other files.** They state
claims without hedging, by design; the hedging is here.

**Status: v7.6 (R7-9)** — the core restated as one definition: misalignment is the KL projection onto a declared set of
intended behaviours, and its decompositions come from log-convexity. No measure changed. The hedge: the first run of the
check stopped on its own registered rule because of two test-design errors; the adopted items rest on the corrected
second run ([[R7-9 results]]).

**v7.5 (R7-6a)** — intensity caps. How hard a target is meant to be pursued is now a declaration. Without a cap
the measures behave as before; with one, an agent that overshoots it is charged. This repairs a real defect: an agent
collapsed onto a distributional target's modes used to score as perfectly aligned. All seven pre-registered
predictions held ([[R7-6a results]]). The hedge: the repair is exact because the distributional target is scored by KL;
a principal scoring the spread by another divergence is not covered.

**v7.4 (R7-7)** — target sets. The target can now be declared **ordinal**: only the order of outcomes is
intended. Under that declaration, best-of-n and quantilizers run on the true target are aligned (`M_ord = 0`),
which repairs the defect v7.3.1 found. Three hedges:
- **Under the budget convention the repair is exact only at zero.** The ordinal budget measure has no closed
  form. A solver computes it, and the registered falsifier D4 fired: on one case of 393 the solver did not
  certify a zero. Zeros are exact without it (Prop. [[Prop 32|32]](f)); non-zero values carry solver error.
- **4 of 10 predictions failed as registered** (P6, P7, P8, P10), on test design or on predictions about the
  cardinal measures; one proved claim, a strict inequality, is withdrawn under the registered rule D2
  ([[R7-7 results]]).
- **Which set to declare is the principal's choice, not the framework's.** A positive cardinal measure for a
  non-Gibbs optimizer may be shape, not misdirection; the ordinal measure separates the two.

**v7.3.3** — a review of the whole package against its stated goal.
- **Nothing proved changed, and every numerical check still reproduces.** The review found no error in the
  proofs it read.
- **Status text had gone stale.** This abstract stood at v6.6, the Dictionary banner at v6.3 and the Boundary
  banner at v6.4. Core §12 still called Thms [[Thm 1|1]], [[Thm 13|13]], [[Thm 17|17]] and Prop. [[Prop 18|18]] entropic-only,
  although they have been tier 1 since v6.4. §1.4 still listed as untested the crossing that R5 and R6 had tested.
  All are corrected ([[Status 05 Hygiene log|§5]]), and `lint` now rejects a part banner older than its own text.
- **The open risk is external contact, not internal consistency.** No prediction has been tested against
  outside data (C8, C9 and C11 have been checked only on the project's own generators). No real case has been
  run through the framework end to end ([[ROADMAP]] T7). Until then it is a checked calculus, not yet a standard.

**v7.3.1 (R7-5 closed)** — no real case needs a divergence other than KL. One real defect was found: an agent
that pursues the **true** target with best-of-n or a quantilizer scores as misaligned: `M_free` has a median of
0.04–0.39 nats ([[R7-5 go-no-go]]), and `M_budget` is never smaller. The cardinal measures charge the *shape* of the
pursuit as well as its direction.
R7-7 (the ordinal target) is the planned repair; until then, read a positive `M_budget` or `M_free` for a
non-Gibbs optimizer as possibly shape, not misdirection.

**v7.3 (R7-4)** — external reward versus the agent's own objective (Props [[Prop 27|27]]–[[Prop 30|30]]), with one stationary
dynamic element. Pre-registered: 6 of 8 predictions held, and 2 failed as registered on test design.

**v7.2 (R7-3)** — two layers. The measurement layer says what misalignment is from behaviour, a declared
reference, the target and a convention; lint keeps explanation out of it. **v7.1 (R7-2)** — the declared
reference is part of the intent; a wrong default in the actor is measured misalignment unless it leans along the
target (Prop. [[Prop 26|26]]). **v7.0** — the package became a vault, with one content edit: Prop. [[Prop 20|20]]'s proof no longer cites B11(i), which
closed a dependency cycle.

**v6.6 (R7-1)** — the actual behaviour is now any distribution, and no actor model is assumed in the
definitions.
- The entropic actor is a named explanatory hypothesis (E) in Def. [[Def 13|13]], and (C) in Def. [[Def 5|5]]. Every result that
  needs one says so; the tool checks.
- The mechanism-relative comparison moves to the explanation layer (Def. [[Def 14|14]], Prop. [[Prop 25|25]]): it fails M4 by
  construction.
- Retractions 75–76.

**v6.5 (R7-0)** — the first step of the refactor.
- The misalignment contract (Def. [[Def 11|11]]) and Prop. [[Prop 24|24]] are added.
- **"Misalignment" now names the budget or free measure; the price measure is a regret** (row 74).
- The measures become Def. [[Def 10|10]].
- Circularities are removed, and the dependency tool `tools/depgraph.py` is added.

**v6.4** — v6.3 plus the fixes prompted by the third independent review (R6, [[R6_LOG]]):
- corrected assumption tiers, with Thm [[Thm 1|1]], Thm [[Thm 13|13]], Thm [[Thm 17|17]] and Prop. [[Prop 18|18]] tier 1 in the actual actor;
- Prop. [[Prop 23|23]] (tier 2′) and the own-resource convention;
- the generality measurement frozen as three nested shares ([[T1_RULES_FROZEN]]);
- retractions 67–73.

v6.3 was v6.2 plus the fixes prompted by an independent review (R5, [[R5_LOG]]): a blind second
routing of the census, tier-4 transfer tests, Props [[Prop 21|21]]–[[Prop 22|22]], Remark [[Rem 13.5|13.5]], and retractions 61–66.

v6.2 was v6.1 (v6 plus the R3 fixes, [[R3_FIX_LOG]]) plus review R4 ([[R4_LOG]]):
- assumption tiers;
- Prop. [[Prop 20|20]];
- the human substrate (B §12, [[B07|B7(e)]]);
- potential games (B §13);
- the census routing ([[T1_census_routing]]).

**The short version.** v6 replaces v5's central inequality with an identity. The loss in nats from pursuing
the wrong objective equals the divergence between actual and intended behaviour. Everything in [[Core index|Core]]
is a theorem with a proof, using standard mathematics, checked numerically by `verify.py`. Nine dictionary
entries are derived rather than asserted (six in v6). The prior-art check (C14) found the package to be
**predominantly an index**: most results are known and are now cited where used. The core's weakest joint has moved from "is the normal form
vacuous?" (it was: v6 abandons it) to "does anything survive for actors that are not exponential tilts?". That
question is now answered in part (v6.4, R5, R6): the tier-1 results hold for any actual actor, and the capacity bounds
for exact maximizers. The E-based bounds do not transfer, and the crossing transfers but its location does not.

Review R2 retracted nineteen v5 claims; the rebuild found two more in R2's own text; review R3 added five. **§2 is the corpus's
memory.**

---


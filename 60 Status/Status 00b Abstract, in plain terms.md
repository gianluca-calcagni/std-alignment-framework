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

**Status: v6.6 (R7-1)** — the actual behaviour is now any distribution, and no actor model is assumed in the
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
vacuous?" (it was: v6 abandons it) to "does anything survive for actors that are not exponential tilts?".

Review R2 retracted nineteen v5 claims; the rebuild found two more in R2's own text; review R3 added five. **§2 is the corpus's
memory.**

---


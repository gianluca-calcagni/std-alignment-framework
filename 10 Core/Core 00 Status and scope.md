---
id: "Core 00 Status and scope"
type: "section"
part: "core"
order: 0
updated: "2026-09-26"
---
# A — Core

> **Status: v7.3.3.** Only §12 changed, whose actor paragraph had not fully absorbed the v6.4 tier corrections. It now matches the tier table: Thms 1, 13
> and 17 and Prop. 18's cap hold for any actual actor. It also states the one dynamic element of (E_R), and the limit that
> R7-5 found: the target is cardinal, so best-of-n run on the true target scores as misaligned (R7-7 is the repair).
>
> **v7.3 (R7-4).** The explanation layer gains **external reward**: the agent's own objective `G`
> versus the reward `R` of an outer process. The weight on `R` is a derived shadow price
> (Prop. [[Prop 27|27]]), and "complies when rewarded, reverts when not" follows from one stationary dynamic element.
> Also new: incentive masking, selection blindness and the fake-alignment gap (Props [[Prop 28|28]]–[[Prop 30|30]]). The work
> was pre-registered: 6 of 8 predictions held; 2 failed as registered on test design, and their proved limits
> hold ([[R7-4 results]]).
>
> **v7.2 (R7-3).** **The core is split into two layers.**
> - The **measurement layer** says what misalignment is, from the declared reference, the target, the
>   conventions and the actual behaviour.
> - The **explanation layer** says why behaviour departs: evaluators, errors, the actor's own reference, actor
>   models.
>
> Every item carries its layer, and lint enforces that measurement never uses or depends on explanation. Four
> mixed items were split. Dependencies now also come from symbols. Found on the way: Prop. [[Prop 15|15]] was
> mis-tiered ([[R078|row 78]]), and the monotone mean (was Prop. 14(i), now Lemma [[Lemma 5.1|5.1]]) had never been checked
> ([[V33]]).
>
> **v7.1 (R7-2).** Two references are now separate.
> - The **declared** reference `q` is part of the intent, and the misalignment measures use only it.
> - The actor's **own** reference `q_A` is an explanation-layer object, under the new hypothesis (E_A).
>
> **A wrong default is measured misalignment unless it leans along the target** (Prop. [[Prop 26|26]]), and every
> (E) result transfers to (E_A). B7(e) was re-tiered: it is tier 1 in the actual actor ([[R077|row 77]]).
>
> **v7.0 (vault).** The content is v6.6 plus one edit: Prop. 20's proof no longer cites B11(i) (a cycle;
> moved to Notes). The package is an Obsidian vault; start at [[00 Home]]. Every item is its own note, and
> dependencies are derived and linted by `tools/vault.py`.
>
> **Status: v6.6 (R7-1).** The actual behaviour `p̂` is now any distribution; no actor model is assumed in
> the definitions.
> - The entropic actor is one explanatory model, named (E) in Def. [[Def 13|13]], and every result that needs it says
>   so.
> - Comparing a mechanism with itself on the target (Def. [[Def 14|14]]) is an explanation-layer quantity; it fails M4
>   (Prop. [[Prop 25|25]]).
>
> **v6.5 (R7-0)** was the first step of the refactor that simplifies the core.
> - The misalignment contract is added (Def. [[Def 11|11]]), and the v6.4 measures are checked against it (Prop. [[Prop 24|24]]):
>   **misalignment is the budget or free measure; the price measure is a regret.**
> - The intent ray and the measures are now a definition (Def. [[Def 10|10]]).
> - Two weak circularities are removed (Thm [[Thm 13|13]] ↔ Thm [[Thm 17|17]] ↔ Prop. [[Prop 16|16]]), and claims are moved out of the
>   definitions.
> - Def. 0 becomes an overview; the formal definition of an instance is Def. [[Def 12|12]].
>
> **v6.4:** v6.3 plus the fixes prompted by the third independent review (R6, [[R6_LOG]]):
> - the assumption tiers are corrected, separating the model of the *actual* actor from that of the
>   *intended* one;
> - Prop. [[Prop 23|23]] (tier 2′) and an own-resource convention are added;
> - the generality measurement is frozen and reported as three nested shares ([[T1_RULES_FROZEN]]).
>
> v6.3 was v6.2 plus the fixes prompted by an independent review (R5, [[R5_LOG]]):
> - a blind second routing of the census;
> - tests of whether the tier-4 predictions transfer to non-Gibbs optimizers;
> - new Props [[Prop 21|21]]–[[Prop 22|22]] and Remark [[Rem 13.5|13.5]].
>
> v6.2 itself was v6.1 plus review R4 ([[R4_LOG]]), and v6.1 was v6 plus review R3 ([[R3_FIX_LOG]]).
>
> **What this file is.** A verified calculus for *one module* of alignment: a single target, a static
> setting, an exogenous frame, and an optimizer that trades value against a divergence from a default
> behaviour.
>
> **What it is not.** A general theory of alignment. Three raters routed 221 catalogued alignment phenomena,
> the third adjudicating the disputes ([[T1_census_routing]] §10; frozen in [[T1_RULES_FROZEN]]). The core:
> - **names** about 78 % of them — it can write them as an evaluator error;
> - says something **specific** about **55–61 %** — a numbered result bears on the item's distinctive
>   feature. The third rater's blind codes give 55 %, its adjudication 61 %;
> - treats about **29 % fully**.
>
> This is reported as nested shares, not as a pass or fail: the specific share sits on the pre-registered
> 60 % threshold. The missing layers, by the number of items that need them, are strategic interaction (51),
> statistical/learning (31), frame endogeneity (23) and dynamics (20). Justified exceptions are no single
> target (16) and internals-only questions (15).
>
> Potential games are the one strategic piece already inside ([[B13|B §13]]).
>
> **Prior art.** Most individual results here are known, and are cited where used. The prior-art check
> (C14) found the package to be predominantly an **index**: its contribution is the arrangement of known
> results inside one calculus, with proofs and checks, plus a few organizing statements not found elsewhere
> ([[Status 04 The honest position|Status §4]]).
>
> Every statement below is a definition, a theorem with a proof, or a measured number with a pointer to the
> block of `verify.py` that reproduces it. Result numbers are stable across versions; new results get new
> numbers.


---
id: "B1 brainstorm"
type: "report"
updated: "2026-09-27"
---
# B1 — brainstorm of ROADMAP §6 (after v7.8)

Light protocol (ROADMAP §4 rule 12): no pre-registration, no core change. Toy tests are in `b1_toys.py` (output in
`b1_toys_output.txt`); they probe hunches and prove nothing. Each item ends with a verdict: **promote** (to T7 or to a
step), **keep** (brainstorm stays open), or **archive**.

## The main finding: one object, three positions

A **partition that the target is not measurable with respect to** appears in three places. The same mathematics
covers each position, but the causes differ:

| Position of the partition | Who holds it | Gap (SF) | What it costs | Status |
|---|---|---|---|---|
| principal's declared resolution `𝒢` | the principal | underdetermination (G1), persistence (G4) | the principal cannot see within-cell moves: `W` is dropped | R7-10, Def. 21 |
| agent's representation `ℋ` | the agent | retention (G2) | the agent cannot follow the target within cells: a cost under the budget convention | T2 below |
| the observables `X` itself | the world | observability (G2) | nobody can: the target is not a function on `X` | outside the finite core (R7-8) |

SF already noted part of this: "principal-coarseness is the static analogue of refinement-induced indifference"
(`03` §1). What is new is that the three positions have computable costs, with the same chain-rule algebra behind
each.

## G0 — the gaps as terms of the measure

**Insight.** The free and segment measures split exactly into attributable terms, by the chain rule (Prop. 36) and
Pythagoras on the ray (Prop. 35):

```
M_seg_free = W  +  KL(p̂_𝒢 ‖ p_{F,t̂})  +  KL(p_{F,t̂} ‖ p_{F,t*})
             within cells   off the ray (misdirection)   intensity (under/overshoot)
```

**Test T1:** exact to `3·10⁻¹⁵` on 300 instances. This partly confirms H12, "the chain rule as the gaps' bridge", for
the free and segment measures. It does not hold for the budget measure, which adds the misattribution `Θ` (Prop. 36(c)).

**What it settles.** "Aligned iff every gap is zero" becomes checkable: `M = 0` iff each non-negative term is 0. The
terms are *symptoms*. The gaps are *causes*, and several causes produce the same term: evaluator error and retention
both move mass off the ray. So the measure can locate a failure but cannot name its cause. That is M4 seen as an
identifiability limit, and it is why G0 cannot be restored as a definition.

**Which impossibility survived (row 3).** It is not recorded. My inference: **observability**, the only one SF calls
"impossible in principle" with no training that helps (`02` §2.1). Grounding's condition was killed separately as
vacuous (row 4).

**Verdict: promote to T7.** The three-term split is the diagnosis table of T7's protocol. It could also become a core
corollary of Props 35 and 36, but no case needs that yet.

## G2 — retention, as a closed-form cost

**Insight.** Consider an agent that can move mass only between the cells of its partition `ℋ` (`p/q` is
`ℋ`-measurable), while the target `F` varies inside cells. Under the budget convention its least misalignment at
budget `k` is

```
R(k) = λ(k) · [ m_F(k) − m_G(k) ],     G = E_q[F | ℋ],
```

where `m_F(k)` and `m_G(k)` are the largest means of `F` and `G` reachable with `KL(p‖q) ≤ k` (Def. 6's reach, in
the `+` direction), and `λ(k)` is the budget-matched exchange rate.
- **In words: the exchange rate times the pursuit lost to the distinctions the agent does not carry.**
- **Proof sketch.** `KL(p̂‖p_λ) = k − λ·E_p̂F + log Z(λ)`; inside the family `E_p̂F = E_p̂G`, maximized by the tilt by
  `G`; and `log Z = λ·m_F − k`.
- **Test T2:** matches a constrained solver to `1.7·10⁻⁸` on 100 instances. A first penalty-based solver disagreed
  by 0.68 nats; that was the solver, not the formula.

**The signature, restated.** `R(k)` *increases* with `k` in every instance: "more reward does not help", and in fact
hurts. It vanishes when the agent's partition refines the level sets of `F`. That is the second axis SF's signature
lacked: evaluator error also grows with `k`, but does not vanish when the agent's representation is refined.
*Hunch, not tested:* the pair (response to budget, response to refinement) separates retention from evaluator error.

**Observability.** Same algebra, with `X` itself as the coarse partition: the target is not a function of what
anyone observes. The finite core cannot state it without a latent variable; it belongs with R7-8.

**Verdict: promote.** This is a candidate step with a closed form, a toy rule-13 example (an agent that cannot see a
distinction pays `λ·Δm`), and a two-dimensional signature a real case could check.

## G3 and C1 — grounding, and what a coarse declaration hides

**Insight.** SF's exposed fraction `R_t` is a width. Take the evaluator `F + E`, where `E` varies only inside the
level sets of `F` (length, tone, formatting). An agent exploiting `E` moves mass *within* cells.

**Test T3:** a Gibbs actor on `F + E`, with `E` pure style, on 300 instances. The within-cell term `W` carries a
median of **98.7 %** of its misalignment (minimum 65 %). A principal who declares "style free" (Def. 21) sees a median
of **1.3 %** of it.

**What it settles.**
- **C1 becomes an identity in the measurement layer.** The blind spot of a declared resolution is exactly the
  sub-reach where grounding exploits live. The coarser the declaration, the larger the exposed sub-reach. SF's
  trade-off (resolution against exposure) needs no channel premise here.
- **This is the strongest argument for R7-10's default** (the finest partition), and a warning that belongs on
  Def. 21. Declaring "style free" is safe only if style cannot be exploited.
- **Grounding re-enters the frame as a quantity:** the width of the evaluator over within-cell moves. Wireheading is
  its limit, where the within-cell moves reach the evaluator itself.

**Verdict: promote to T7.** The RLHF length-bias case measures exactly this. Add the warning note to Def. 21 at the
next core step.

## G5 — verification

**Verdict: archive** as a named explanation-layer prediction (process confabulation falls as the process is
externalised), to run only when model access exists, with SF's control that the externalised chain be causally
load-bearing.

## I1 — identifiability

**Identification classes of three channels, from intent to behaviour:**
- the entropic actor identifies `F` up to `[F]₊`;
- best-of-n only up to `[F]_ord` (its order);
- a Bradley–Terry learner identifies `F` up to a constant *per context*.

**Retrodiction.** R7-7's defect was declaring the cardinal set, which is finer than what best-of-n identifies.
Hypothesis (a) — the natural target set is the channel's identification class — predicts that defect.

**Test T4.** An agent acting on `F + a_c`, with the unidentified per-context offsets `a_c`, over two contexts:
- aligned within every context (to `3·10⁻¹⁶`);
- misaligned across them (median 0.07 nats).

No amount of preference data removes this, because `a_c` is not identified. **Prediction:** a preference-trained
agent is aligned within prompts and misallocates across them, and the error does not shrink with data. *Hunch:*
per-prompt normalization in current RL recipes (group-relative advantages) discards exactly the unidentified
offsets, which is the identification class in practice.

**The superpower, stated.** Two inverse problems sit on one channel.
- The principal's side: M4 says the measure uses only what behaviour identifies.
- The agent's side: the target set should be no finer than what the training channel identifies.

A mismatch in either direction charges, or fails to charge, distinctions the channel cannot carry.

**Verdict: keep as the lead theme, and promote one rule to T7's protocol:** declare no target set finer than the
channel identifies, or state why.

## Needing more clarity

- **The reference `q` (H13): closed structurally.** After R7-6b and R7-10, `q` has one role, the origin of the
  intent ray. "Doing nothing is intended" is now the default of the floor, and "the split inside cells follows `q`"
  is the default of the resolution. Elicitation: "the behaviour pursuit is measured from" (the base policy, the status
  quo). **Verdict: close H13.**
- **Execution slips (L4).**
  - *Test T5:* 1 % uniform slips on an on-ray agent are charged 0, 0.0003, 0.006, 0.04 and 0.10 nats at intensities
    1, 5, 10, 20 and 40.
  - *Insight:* a sharper agent with the same slip rate scores worse, because slips land where the intended
    behaviour is small.
  - *Candidate declaration:* "execution noise", an intended set of mixtures with a declared noise law. It is not
    log-convex, and it needs an independent measurement of the noise, as B12 does for defaults.
  - **Verdict: keep,** with this toy rule-13 example.
- **The chain rule as the bridge (H12):** holds for the free and segment measures (T1), not for the budget measure.
  **Verdict: record; partly confirmed.**
- **Intensity for non-cardinal target sets.** *Proposal:* measure intensity in nats, `KL(p‖q)`, for every target set.
  For cardinal sets it orders the ray exactly as `t` does (Lemma 5.1). An ordinal cap is then `C_F ∩ {KL(p‖q) ≤ k}`,
  which is convex, so the capped ordinal free measure is a convex program. **Verdict: keep;** a step only if a case
  needs ordinal caps.

## L1–L4

- **L1 levers: promote to T7's protocol.** Each term has its lever:

  | Term | Lever that moves it |
  |---|---|
  | off the ray | re-specify the target |
  | within cells (`W`) | declare the resolution, or constrain style |
  | intensity | a KL penalty, a cap, a floor |
  | retention (`R(k)`) | refine the agent's representation |
  | beyond the identification class | nothing on this channel: change the channel (T4) |

- **L2, the frame table:** held for T6, which is deferred. No change.
- **L3, chains of principals:** for nested partitions the within-cell terms add along the chain, by the chain rule.
  Non-nested partitions (neither refines the other) are open. **Keep, low priority.**
- **L4:** see "execution slips" above.

## Summary of verdicts

| Promote | Keep | Archive or close |
|---|---|---|
| G0's three-term split (T7 diagnosis table); G2 retention cost (candidate step); G3/C1 exposed sub-reach (T7 RLHF case, plus a warning on Def. 21); the I1 rule (T7 protocol); L1 levers (T7 protocol) | I1 (lead theme); execution noise (L4); ordinal intensity; L3 | G5 (named prediction); H13 (closed); L2 (T6) |

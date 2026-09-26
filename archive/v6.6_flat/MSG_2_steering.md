# Message 2 — to the reviewer: steering

> Suggestions, in priority order. Each says whether it needs a PI decision, what it costs, and what would
> show it to be wrong. Your roadmap's order is right; nothing here asks you to change it. Items 1–3 sharpen
> turns you already have; item 4 is optional; §5 is what I would not do.

---

## 1. Let T1 decide the scope, not just the routing *(no PI decision; costs one extra column)*

The largest risk I see ahead is not drift but **scope expansion**. Your R3 message proposes five layers —
ontology, static, statistical, dynamic, strategic — and each is a research programme. Building them before
the census says which it needs would be the drift.

**Suggestion.** When you route each census item in T1, record not only its locus (L1–L7) but the
**minimal layer whose quantitative content it needs**: static · statistical · dynamic · strategic ·
outside. The counts per layer then tell the PI which layers to build, in what order, and which to skip.

**Why this is cheap.** You are already reading every item and naming the formal object that carries it
or the layer that is missing. This asks you to write that layer down as a column.

**Pre-register it**, in the same way as the §14 prediction, before routing begins: your guess at the
distribution across layers. If the census comes back 70 % static, the dynamic and strategic layers can
wait; if it comes back evenly spread, the architecture question becomes urgent.

**What would make this suggestion wrong:** if the minimal-layer judgement cannot be made item by item
without first building the layer. Then record "undetermined" and count those separately — that count is
itself informative.

---

## 2. Restore the human substrate — the drift that was mine *(restores an explicit PI request)*

**Where.** A human row in `A_core.md` §10's substrate table, judged by the same Prop. 12 criterion you
used for the other three (unit channel for `F`; measurable `q`), plus one dictionary entry.

**Three things to check, and the first two are the interesting ones.**

**(a) The actor.** A logit actor over choices with a **fixed default** is exactly your Gibbs actor, with
`q` the default choice probabilities. **Rational inattention** (Sims 2003; Matějka & McKay 2015) derives
the same generalized-logit form from an information cost — which would put humans on the same footing as
biology. **But its default is the *endogenously optimized* action marginal**, so `q` becomes a function of
`p`. That is an (X) violation inside the carrier — the exact trap your own NOTES H2 identifies for the
closed-loop lift, arriving here from a different direction. So the human row has to choose: fixed
defaults (habits; clean) or rational inattention (endogenous `q`; outside the static module). **The
choice is informative either way.**

**(b) The reference may be measurable for humans in a way it is not for institutions.** Your §10 finds
institutions blocked by `q`, which has no independent measurement. For humans there is a literature that
manipulates defaults directly — default effects and choice architecture (e.g. Madrian & Shea 2001 on
retirement enrolment). Behaviour under two different defaults is a handle on `q`. **This is a hypothesis
I have not checked**; if it holds, humans could land above institutions in the table.

**(c) Time inconsistency contains its own version of the equilibrium boundary.** A *naive*
quasi-hyperbolic agent (Laibson 1997; O'Donoghue & Rabin 1999) is two evaluators at two times with no
game between them — a candidate for Cor. 1.5's stacked stages. A *sophisticated* one plays an
intrapersonal game, which is your equilibrium fork. Planner–doer and dual-self models (Thaler & Shefrin
1981; Fudenberg & Levine 2006) sit between. **If the naive/sophisticated line lands exactly on your (X)
and equilibrium boundaries, that is independent evidence the boundary is substrate-free**, which is the
claim of A §10's "one boundary, three names" — it would become four.

**What would make this wrong:** if human choice data do not support an exponential-tilt reading even
approximately, the row is "not supported", like institutions. That is a result, not a failure.

---

## 3. Before T2, classify every result by the assumption it needs *(no PI decision; analysis, not experiment)*

C7 — deployed optimizers are not Gibbs actors — is currently stated as a blanket weakness, and T2 plans
experiments to test whether Gibbs predictions survive for best-of-n and policy gradient.

**But the package already contains results that need no Gibbs assumption at all.** Prop. 10's conjugate
pairings hold "for all `p`". Thm 5(i) needs only a maximizer over a set containing `p*`. B §11(i),
Price's selection term, holds for every `p ≪ q`.

**Suggestion.** Tag every result in A and B with the weakest assumption it needs:

| Tier | Needs | Examples already in the package |
|---|---|---|
| 1 | nothing — any `p ≪ q` | Prop. 10; B11(i) |
| 2 | a maximizer over a set containing the intended actor | Thm 5(i) |
| 3 | an exact regularized optimum | Prop. 15 |
| 4 | an exponential tilt | Thms 1, 13, 17; Props 3, 4, 14, 18 |

**Then T2 only needs to test tier 4**, and C7 becomes a precise map rather than a blanket caveat. It is
cheaper than the experiments it partly replaces.

**Two tier-1 statements worth adding**, both one-line consequences of B11(i) and not results in their own
right. I verified both to machine precision (≤ `8·10⁻¹⁴`) on best-of-n selection, top-k selection and
arbitrary distributions — none of which is a tilt:

```
target gain  =  proxy gain  −  Cov_q(w, E)           w = dp/dq      ("Goodhart as a covariance")
E_{p*}F − E_{p̂}F  =  Cov_q(w* − ŵ, F)                regret between any two actors
```

The first is an actor-agnostic statement of Goodhart's law: selection raises the proxy by `Cov_q(w, F̂)`
and loses `Cov_q(w, E)` of it, whatever the optimizer. **I have not shown that it discriminates between
actors** — my attempt did not control for proxy gain, so it shows nothing about that. Treat it as a
restatement with a useful property (tier 1), not a finding.

**What would make this wrong:** if tiers 1–3 turn out to be too weak to carry any of the forbidden
statements in A §11. Then C7 really is a blanket weakness, and T2 is as important as you think.

---

## 4. Optional: a clarity pass *(no PI decision; do last)*

The PI's stated values are coherence, generality and clarity. The first two are much stronger than in v5.
The third has not kept pace: 41 numbered items, a "plain terms" abstract that is not plain, and two
corollaries whose job is to explain my old errors. A layered reading path — one plain paragraph, the
identity, the five results a newcomer needs, then everything else — would serve a reader who is not
already inside the project. Low priority; after T1–T3.

---

## 5. What I would not do now

| Not now | Why |
|---|---|
| the Layer-0 carrier change (CIDs/MAIDs) | a PI decision, and T1's layer counts should inform it |
| target sets and aggregation | Arrow makes the choice of rule substantive; a PI decision |
| the dynamic and strategic layers | wait for T1's counts — they may not be needed first |
| the measurable-space rewrite | routine, error-prone, and best done once, inside whatever carrier survives |
| promoting anything from my notes | my H1 and H2 both died in your R2; weight my ideas accordingly |

---

## 6. In one paragraph

Keep your order. Make T1 report which layers the census needs, so that the architecture follows the
evidence instead of preceding it. Restore the human substrate, which I dropped — and use it as a test,
because the default-endogeneity trap and the naive/sophisticated split both land on boundaries you have
already drawn. Before running T2, tier the results by assumption, because several already survive without
the Gibbs actor and one of your own imports is the reason.

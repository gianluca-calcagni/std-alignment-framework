# A — Core

> **Status: v6.6 (R7-1).** The actual behaviour `p̂` is now any distribution; no actor model is assumed in
> the definitions.
> - The entropic actor is one explanatory model, named (E) in Def. 13, and every result that needs it says
>   so.
> - Comparing a mechanism with itself on the target (Def. 14) is an explanation-layer quantity; it fails M4
>   (Prop. 25).
>
> **v6.5 (R7-0)** was the first step of the refactor that simplifies the core.
> - The misalignment contract is added (Def. 11), and the v6.4 measures are checked against it (Prop. 24):
>   **misalignment is the budget or free measure; the price measure is a regret.**
> - The intent ray and the measures are now a definition (Def. 10).
> - Two weak circularities are removed (Thm 13 ↔ Thm 17 ↔ Prop. 16), and claims are moved out of the
>   definitions.
> - Def. 0 becomes an overview; the formal definition of an instance is Def. 12.
>
> **v6.4:** v6.3 plus the fixes prompted by the third independent review (R6, `R6_LOG.md`):
> - the assumption tiers are corrected, separating the model of the *actual* actor from that of the
>   *intended* one;
> - Prop. 23 (tier 2′) and an own-resource convention are added;
> - the generality measurement is frozen and reported as three nested shares (`T1_RULES_FROZEN.md`).
>
> v6.3 was v6.2 plus the fixes prompted by an independent review (R5, `R5_LOG.md`):
> - a blind second routing of the census;
> - tests of whether the tier-4 predictions transfer to non-Gibbs optimizers;
> - new Props 21–22 and Remark 13.5.
>
> v6.2 itself was v6.1 plus review R4 (`R4_LOG.md`), and v6.1 was v6 plus review R3 (`R3_FIX_LOG.md`).
>
> **What this file is.** A verified calculus for *one module* of alignment: a single target, a static
> setting, an exogenous frame, and an optimizer that trades value against a divergence from a default
> behaviour.
>
> **What it is not.** A general theory of alignment. Three raters routed 221 catalogued alignment phenomena,
> the third adjudicating the disputes (`T1_census_routing.md` §10; frozen in `T1_RULES_FROZEN.md`). The core:
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
> Potential games are the one strategic piece already inside (`B_dictionary.md` §13).
>
> **Prior art.** Most individual results here are known, and are cited where used. The prior-art check
> (C14) found the package to be predominantly an **index**: its contribution is the arrangement of known
> results inside one calculus, with proofs and checks, plus a few organizing statements not found elsewhere
> (`D_status.md` §4).
>
> Every statement below is a definition, a theorem with a proof, or a measured number with a pointer to the
> block of `verify.py` that reproduces it. Result numbers are stable across versions; new results get new
> numbers.

## Abstract, in plain terms

Someone — or something, like natural selection — has a goal: the **target**. An agent works toward a slightly
different goal: the **evaluator**, meaning whatever it is actually rewarded for. The agent is limited: moving
away from its default habits costs it something. This file does two things. It **measures** how far the
agent's actual behaviour departs from the behaviour intended for the target — from behaviour alone, whatever
the agent is. And it **explains** the departure by what the agent optimizes and how.

The main findings, in words:

- **The loss equals how far the agent's actual behaviour is from the behaviour it would show if it
  pursued the target.** It is not a bound; it is an equality, and it holds for any agent (Theorem 1).
  **Misalignment** is the part of that departure that pursuing the target harder or more softly cannot
  explain (Def. 8, Prop. 24).
- **Which mistakes matter depends on how hard the agent optimizes.** A lightly optimizing agent is hurt by
  errors that are spread out; a strongly optimizing agent is hurt by rare, extreme errors. So no ranking of
  errors holds at every level of optimization (Theorem 9).
- **How you limit the agent decides what you must know about the evaluator's errors.** The most common
  limit (KL) cannot contain errors with heavy tails, whatever the budget; a different limit (χ²) can
  (Prop. 11).
- **Several results hold for any optimizer at all** — not only the idealized one used elsewhere. The
  simplest: the target gains exactly what the evaluator gains, minus how much the optimizer's choices
  correlate with the evaluator's error (Prop. 20).
- **For any agent, a departure that costs little — counting both lost value and the information spent,
  and measured against an idealized intended agent — is hard to detect from behaviour** (Prop. 18). The converse fails: a misalignment
  that loses no value at all can still be easy to detect. An agent that behaves differently when it is
  tested than when it is deployed is captured by a single number, the evaluation gap (Prop. 19).

## Reading path

1. **The plain summary above.**
2. **The identity:** Definition 2 and Theorem 1.
3. **Five results that carry most of the weight:**
   - Theorem 5 with Theorem 9 — the worst case under a capacity limit, and why it has no product form;
   - Props 10–11 — the divergence decides the norm;
   - Theorem 17 — every regret notion is a point on one curve, so the comparison must be declared;
   - Prop. 20 — Goodhart's law as a covariance, for any optimizer;
   - Prop. 18 — harm caps detectability.
4. **Everything else, as needed.** The assumption tiers below say which results survive which kind of
   optimizer.

## Assumption tiers

Each result is tagged with the weakest assumption it needs about the **actual** actor — the behaviour being
assessed. The **intended** actor (the counterfactual) is fixed separately by the comparison convention
(Def. 8): the Gibbs actor at a declared price or budget. Comparing a mechanism with itself on the target
needs an actor model, and lives in the explanation layer (Def. 14). *(Corrected in v6.4. Earlier tables filed results that need only a Gibbs **intended** actor
as if they needed a Gibbs **actual** actor; `D_status.md` rows 67–68. Refined in R7-1: tier 4 is now the
named hypothesis (E) or (C), stated in each result, and five items that assume nothing about the actual actor
left tier 4; row 76.)*

| Tier | Needs, about the actual actor | Results |
|---|---|---|
| **1** | nothing: any `p ≪ q` (full support where stated). Prop. 21 also needs weights that depend on behaviour only through `F̂`; Prop. 22 needs a differentiable path | **Thm 1** (the intended actor is Gibbs at a declared price); **Thm 13** (full-support `p̂`); **Thm 17 (i)–(iii)**; the cap in **Prop. 18** (`C ≤ KL(p̂‖p*) = β·R_J`); both parts of **Prop. 19**; **Prop. 24** (the contract); Props 6, 10, 11, 20, 21, 22; Lemma 8; the inequalities in Prop. 7; B7(a)–(d); B11(i) |
| **2** | an **exact maximizer** of its evaluator over a set containing the intended actor | Thm 5 (all parts: capacity maximizers); Thm 9; the regret bound in Prop. 7 |
| **2′** | an **argmax selector over a common random candidate set** (e.g. best-of-n compared at equal n) | Prop. 23 |
| **3** | an exact optimum of `U − φ/β`, with `φ/β − U` convex | Prop. 15 |
| **4** | **(E)**: the actual behaviour is the entropic model run on the evaluator, `p̂ = p_{F̂,β}` (Def. 13); **(C)** for the capacity model | (E): Cors 1.1(b)–1.5; Props 2–4, 12; Prop. 14(ii)–(iii); Prop. 16 (g1)–(g3); Cors 13.1, 13.3–13.4; Rem. 13.5; B4; B6; B11(ii)–(iii); B12. (C): Cor. 17.1 |
| **—** | nothing about the actual actor: facts about the target, the Gibbs family or the capacity problem | Lemma 5.1; Cor. 5.2; Prop. 14(i); Cor. 1.1(a) |
| **4′** | the rational-inattention actor (reference = its own optimized action marginal) | B7(e) |
| **4″** | log-linear learning in an exact potential game (the group as one entropic actor on joint behaviour) | B13 |

**Tier 1 includes the core's central identity.**
- For **any** actual actor, the regret in nats against the Gibbs intended actor at a declared price is
  `KL(p̂‖p*)`. It decomposes as in Thm 13, and it caps detectability (Prop. 18).
- What does depend on the actor is **which engineering comparison is natural**. For best-of-n the natural
  resource is `n`, not KL. That comparison (Def. 14) needs the mechanism, so it is not a misalignment measure
  (Prop. 25).

**Tier 2 does not hold for every optimizer.** R6 measured violations on 1,150 random instances:
- early-stopped vanilla policy gradient: 25.5 %;
- best-of-n compared at matched KL: 4.3 %;
- best-of-n compared at equal `n`: 0, which is Prop. 23;
- the Gibbs actor: 0.

The standing assumption S (finite `X`, full-support `q`) applies throughout, except where a result says
otherwise.

**Historical notes.** Cor. 1.4 and Remark 7.1 exist to explain what v5 found. Cor. 1.2 is used downstream
(Prop. 7's proof); only its last sentence is historical.

---

## 1. Setting

**Standing assumption S.** `X` is a finite set; `q` is a probability distribution on `X` with full
support. All functions are real-valued on `X`. (Where a result holds on general measurable spaces, or needs
one, it says so; Prop. 11 and the Gaussian example of `B_dictionary.md` §4 are the only results that need
infinite `X`.) Full support is a normalization: `X` can always be taken to be `supp q`, the set of
behaviours the actor can reach.

**Overview 0 (alignment instance — static, single-target module; not a definition — the formal definition is
Definition 12).** A tuple `(X, q, F, F̂, R, κ)`:
- a behaviour set and a reference, `X` and `q`;
- a target `F` and an evaluator `F̂` (Definition 1);
- a resource `R`: a price `β ∈ (0, ∞]` (Definition 2), a budget `δ`, or both (Definition 5). By Cor. 5.2,
  one of them suffices for the soft actor or the pure capacity actor;
- a counterfactual convention `κ` (Definition 8).

The **target** `F` is any designated functional on behaviour: the objective of a principal, or a
teleonomic target such as fitness. No principal is assumed. The target proper is the positive-affine
class `[F]₊`. An instance fixes a representative `F`, i.e. a unit relative to `β`, only when it reports
value-unit or price-convention quantities (Prop. 16, Def. 7).

**Definition 1 (objects).**

| Symbol | Object |
|---|---|
| `q` | the **reference**: default behaviour before any objective is pursued |
| `F` | the **target** |
| `F̂ = F + E` | the **evaluator**, the objective an actor model is run on; `E` is the **error** |
| `β ∈ (0, ∞]` | the **exchange rate** between value and information (inverse temperature) |
| `p_{G,t} ∝ q·e^{tG}` | the Gibbs tilt of `q` by `G` at `t ∈ ℝ`; `p_{G,∞} := q(· \| argmax G)` |
| `p* = p_{F,β}` | the **intended behaviour** at price `β`: the entropic counterfactual |
| `p̂` | the **actual behaviour**: *any* full-support distribution on `X`. No actor model is assumed (R7-1) |
| `osc(G) = max G − min G` | oscillation |
| `Λ(t) = log E_{p*} e^{t(E − E_{p*}E)}` | centred cumulant generating function (CGF) of the error under `p*` |
| `Λ_q(t)` | the same under `q` |

**Definition 2 (the bounded actor).** For `β < ∞`,

```
J_G(p) = E_p[G] − (1/β)·KL(p ‖ q)
```

and for `β = ∞`, `J_G(p) = E_p[G]`.

*Note.* By Thm 1 (the Gibbs variational principle), for `β < ∞` the unique maximizer of `J_G` over `Δ(X)` is
`p_{G,β}`, with `max J_G = (1/β)·log E_q e^{βG}`.

**Definition 13 (actor models; R7-1).** An **actor model** is a map `A` from an objective `G` (with the
reference `q` and a resource `r`) to a behaviour `A(G; q, r) ∈ Δ(X)`. It *explains* behaviour, and is not part
of what misalignment means. The **entropic model** is `A(G; q, β) = p_{G,β}`, with the price `β` as its
resource.

**Hypothesis (E).** The actual behaviour is the entropic model run on the evaluator: `p̂ = p_{F̂,β}`.

A result that needs an actor model says so in brackets, *[Assumes (E).]*.

*Note.* Other named models:
- the capacity model — Def. 5, hypothesis (C);
- argmax selectors over a random candidate set, e.g. best-of-n — Prop. 23.

No misalignment measure assumes an actor model (Def. 11, M4). Comparisons that do are in Def. 14.

**Definition 3 (regrets).**

| | Definition |
|---|---|
| alignment regret (free-energy) | `R_J = J_F(p*) − J_F(p̂)` |
| raw alignment regret | `ΔF = E_{p*}F − E_{p̂}F` |
| boundedness cost | `g = max F − E_{p*}F` |
| total regret | `T = max F − E_{p̂}F = g + ΔF` |

**Units.** `[V]` is the unit of value. The table is checked against every statement below.

| Quantity | Units |
|---|---|
| `F`, `F̂`, `E`, `g`, `T`, `ΔF`, `R_J`, `R^C`, `σ_δ`, `w_δ`, `osc` | `[V]` |
| `β`, `t`, `t̂`, `λ_δ` | `[V]⁻¹` |
| `KL`, `δ`, `β·R_J`, `D_⊥`, `D_∥`, `X_anti`, `M(t)`, `Λ(t)`, `C(·,·)`, `Γ` | nats |
| `Var`, `σ±²`, `T'(0)` | `[V]²` |

`R_J` and `ΔF` differ by the information-cost differential:
`R_J = ΔF + (1/β)[KL(p̂‖q) − KL(p*‖q)]`. **`ΔF` can be negative** (the actual actor may buy more `F` by
spending more information than the intended one); `R_J` cannot (Cor. 1.1).

---

## 2. The identity

**Theorem 1 (regret is a divergence).** For `β < ∞` and every distribution `p` on `X`,

```
J_F(p*) − J_F(p) = (1/β)·KL(p ‖ p*).
```

In particular **`β·R_J = KL(p̂ ‖ p*)`**.

*Proof.* `log p* = log q + βF − log Z`, `Z = E_q e^{βF}`. Hence
`KL(p‖p*) = KL(p‖q) − β·E_p F + log Z = β·[(1/β)log Z − J_F(p)] = β·[J_F(p*) − J_F(p)]`. ∎

*Check.* `V1`: max `|β·R_J − KL(p̂‖p*)| = 4.8·10⁻¹⁴` over 20,000 random instances.

**The actual actor is arbitrary.** Only `p*` is the Gibbs actor. So `β·R_J = KL(p̂‖p*)` holds for best-of-n,
for a policy-gradient iterate, or for any behaviour whatever, with `R_J` read as the free-energy regret at the
declared price. *(`V27`: 4,222 non-tilt actors, to `2·10⁻¹⁴`; R6 checked 18,003 KL-penalized policy-gradient
iterates, to `3·10⁻¹⁴`.)*

*Prior art.* This is the Gibbs variational principle. For KL-regularized reward maximization it is the
known equivalence with reverse-KL minimization toward the Gibbs policy (Korbak et al., NeurIPS 2022;
Korbak, Perez & Buckley, Findings of EMNLP 2022), used routinely in RLHF theory (e.g. Zhao et al. 2024).
Applying it to the misspecified actor is immediate. Prop. 15 shows it is the entropic case of a Bregman
identity.

**Corollary 1.1.** (a) For any actual behaviour, `R_J ≥ 0`, with equality iff `p̂ = p*`.
(b) *[Assumes (E).]* Equality holds iff `E` is constant on `X`.
*Proof.* (a) Thm 1 and `KL ≥ 0`. (b) Under (E), `p̂ ∝ p*·e^{βE}` and `p*` has full support, so `p̂ = p*` iff `βE`
is constant. ∎

**Corollary 1.2 (the optimality gap is a symmetric divergence).** *[Assumes (E).]* The v5 "exact form" satisfies

```
E_{p̂}[E] − E_{p*}[E] = (1/β)·[ KL(p̂‖p*) + KL(p*‖p̂) ].
```

*Proof.* `log(p̂/p*) = βE − log E_{p*}e^{βE}`. Take expectations under `p̂` and `p*` and subtract. ∎

So the v5 inequality `R_J ≤ E_{p̂}E − E_{p*}E` is the statement `KL ≤ KL + KL_reverse`, and its slack is
exactly `(1/β)·KL(p*‖p̂)`.

**Corollary 1.3 (CGF and integral forms).** *[Assumes (E).]* With `p_t ∝ p*·e^{tE}` and `V(t) = Var_{p_t}(E) = Λ''(t)`:

```
β·R_J = β·Λ'(β) − Λ(β) = Λ*(Λ'(β)) = ∫₀^β t·V(t) dt,
E_{p̂}E − E_{p*}E = Λ'(β) − Λ'(0) = ∫₀^β V(t) dt,
```

where `Λ*` is the Legendre transform (the Cramér rate function of `E` under `p*`).
*Proof.* `KL(p̂‖p*) = β·E_{p̂}E − log E_{p*}e^{βE} = βΛ'(β) − Λ(β)` (centring cancels). Since `Λ` is convex
the concave function `t ↦ tΛ'(β) − Λ(t)` is maximized where `Λ'(t) = Λ'(β)`, i.e. at `t = β`; so this
equals `sup_t [tΛ'(β) − Λ(t)] = Λ*(Λ'(β))`. Differentiate
`t ↦ tΛ'(t) − Λ(t)` to get `tΛ''(t)`, and note it vanishes at `t = 0`. ∎

*Check.* `V1`: quadrature agrees to `2.6·10⁻¹⁴` and `1.4·10⁻¹³` (300 instances).

> **The object is the CGF of the error under the intended behaviour, evaluated at the actor's exchange
> rate.** The v5 two-factor product is created by the relaxation steps, not present in the quantity.

**Corollary 1.4 (historical note: why v5 found "tight to about 2×").** *[Assumes (E).]* 

```
R_J / (E_{p̂}E − E_{p*}E) = ∫₀^β t·V(t) dt / (β·∫₀^β V(t) dt)  ∈ (0, 1),
```

the `V`-weighted mean of `t/β` on `[0, β]`. It tends to `1/2` as `E → 0` (then `V` is nearly constant), and
exceeds `1/2` iff `∫₀^β (t − β/2)·V(t) dt > 0`, i.e. iff the error's variance is larger, on average, on the
second half of the tilt path.
*Check.* `V1`: p5/p50/p95 = 0.185 / **0.482** / 0.682, range [0.034, 0.937]. The v5 median 0.48 was this
symmetry, not a tightness property.

**Proposition 15 (the identity for any convex regularizer and any target that keeps the objective concave).**
Let `φ` and `U` be functions on `Δ(X)` such that `Ψ = φ/β − U` is convex. For instance, `φ` convex and `U`
concave — but `U` need not be concave (v6.4; `V29`). Let `J(p) = U(p) − φ(p)/β`, let `p*` maximize `J` over
`Δ(X)`, and let `Ψ` be differentiable at `p*`. Then for every `p`:

```
J(p*) − J(p) = B_Ψ(p, p*) − ⟨∇J(p*), p − p*⟩  ≥  B_Ψ(p, p*),
```

where `B_Ψ(p, p*) = Ψ(p) − Ψ(p*) − ⟨∇Ψ(p*), p − p*⟩` is the Bregman divergence. Equality holds when `p*` is
in the relative interior of `Δ(X)`. In particular, the actual actor `p̂ = argmax [Û − φ/β]` has regret at
least `B_Ψ(p̂, p*)`, with equality at an interior optimum.

| Case | `B_Ψ(p, p*)` |
|---|---|
| `U(p) = E_pF`, `φ = KL(·‖q)` | `KL(p‖p*)/β` — Theorem 1 |
| `U(p) = E_pF`, `φ = χ²(·‖q)` | `Σ_x (p − p*)²/(β q)`; the optimum may lie on the boundary |
| `U(p) = E_pF − κ(E_pG)²`, `φ = KL(·‖q)` | `KL(p‖p*)/β + κ(E_pG − E_{p*}G)²` — a concave target that cannot be written as `E_p` of any function |

*Proof.* `J = −Ψ`, so `J(p*) − J(p) = Ψ(p) − Ψ(p*) = B_Ψ(p,p*) + ⟨∇Ψ(p*), p − p*⟩`, and
`∇Ψ = −∇J`. At a maximum of a concave function over a convex set, `⟨∇J(p*), p − p*⟩ ≤ 0` for all `p`. If `p*` is
in the relative interior, first-order optimality makes `∇J(p*)` a constant vector, and `Σ_x (p − p*)(x) = 0`,
so the term vanishes. ∎
*Check.* `V29` checks a non-concave `U` with convex `Ψ`, to `2·10⁻¹⁵`. `V12`:
- χ²: equality to `4.5·10⁻¹³` on 961 interior optima, and `≥` with no violation on 3,039 boundary optima;
- concave target: to `6.7·10⁻¹⁵`.

*Scope.* Props 2–4, 14, 18 and 19, Cors 1.3 and 1.5, and Thms 13 and 17 use the exponential form of the
entropic actor. For Props 18–19, the Chernoff bound `C ≤ KL(p̂‖p*)` survives, but `KL(p̂‖p*)` is no longer
the regret. Prop. 15 is what survives for other regularizers. The Pythagorean identity needs the intent ray to be an exponential family
and does not extend.

**Corollary 1.5 (stacked stages compose additively).** *[Assumes (E), stagewise.]* Let the actual actor result
from `K` successive entropic stages: stage `k` tilts the previous stage's output by `F + E_k` at rate `β_k`. Let the intended
actor result from the same stages with `F`. Then, with `B = Σβ_k` and `Ē = Σ(β_k/B)·E_k`:
- `p̂ = p_{F+Ē, B}` and `p* = p_{F,B}`;
- `B·R_J = KL(p̂‖p*)`;
- for errors of order `ε`: `B·R_J = ½·Var_{p*}(Σ_k β_k E_k) + O(ε³)`.

*Proof.* Tilts compose in the exponent: `p_{p_{G₁,t₁}, G₂, t₂} = p_{q, t₁G₁ + t₂G₂, 1}`. Then Thm 1 and Cor. 1.3. ∎
*Check.* `V15`: composition to `4·10⁻¹⁷`; the second-order ratio is 1.0011 at `ε = 0.01`.

*Reading.* Errors introduced at different stages — an outer evaluator error and an inner objective error,
or pretraining, fine-tuning and RL — add in the exponent. Their interaction is a covariance under `p*`, which
can reinforce or cancel.

**What Theorem 1 changes.** The v5 separability test measured `corr(osc(E), KL(p̂‖p*))` and found 0.52. That
"realized travel" *is* `β·R_J`: the test correlated the error with the regret. Travel measured from the
**reference**, `KL(p̂‖q)`, is a different quantity, observable in practice, and usable in a bound (Prop. 7).

---

## 3. Bounds in the error alone

**Proposition 2 (sharp error-only bound).** *[Assumes (E).]* `R_J ≤ β·osc(E)²/8`, i.e. `β·R_J ≤ osc(βE)²/8`. The constant
is sharp.
*Proof.* Popoviciu: `V(t) ≤ osc(E)²/4`. Insert in Cor. 1.3: `β·R_J ≤ (osc²/4)·β²/2`. Sharpness: `E` taking two
values, each on a set of `q`-mass 1/2, and `β → 0`; then `V(t) = osc²/4 + O(β)` on `[0, β]`, so the ratio of
the two sides tends to 1. ∎

*Check.* `V2`: 0 violations / 20,000; slack p5/p50/p95 = 0.002 / 0.108 / 0.412. The v5 normal form
`osc(E)·√(2δ)` has slack 0.001 / 0.043 / 0.154, and Prop. 2 is tighter in 87.5 % of instances.

> **In the soft-regularized setting the capacity factor adds nothing.** In nats, the regret is bounded by
> the square of the error in nats. `β` enters only as the unit conversion of `E`.

**Proposition 3 (only the upper tail matters).** *[Assumes (E).]* 

```
R_J ≤ [Λ(2β) − 2Λ(β)] / β ≤ 2β·σ₊²(2β),     σ₊²(s) := sup_{0<t≤s} 2Λ(t)/t².
```

*Proof.* Convexity: `Λ(2β) ≥ Λ(β) + βΛ'(β)`, so `βΛ'(β) − Λ(β) ≤ Λ(2β) − 2Λ(β)`. Then `Λ(β) ≥ 0` (Jensen)
and `Λ(2β) ≤ 2β²σ₊²(2β)`. ∎

Only `Λ` on `t > 0` enters, i.e. only the **upper** tail of `E` under `p*`: overrating matters, underrating
enters only through `p*`. The first inequality is attained asymptotically when the tilt saturates on a
single state. There `Λ(t) ≈ t·(max E − E_{p*}E) − c`, and both sides tend to `c/β` (`final_audit.py` F8: the
maximum ratio is 1.000). For a Gaussian-shaped CGF, `Λ(t) = s²t²/2`, each of the two inequalities loses a
factor 2.
*Check.* `V2`: 0 violations; slack 0.256 / 0.572 / 0.986 (first form), 0.019 / 0.205 / 0.33 (second).

**Proposition 4 (an error confined to one region saturates).** *[Assumes (E).]* Let `E = M·1_A`, `M ∈ ℝ`. Then

```
β·R_J = kl( p̂(A) ‖ p*(A) ),    p̂(A) = p*(A)e^{βM} / (p*(A)e^{βM} + 1 − p*(A)),
```

where `kl` is the binary KL. Hence `β·R_J → log 1/p*(A)` as `M → +∞`, `β·R_J → log 1/(1 − p*(A))` as
`M → −∞`, and `β·R_J ≤ max{log 1/p*(A), log 1/(1 − p*(A))}` for every `M`.
*Proof.* `dp̂/dp*` is constant on `A` and on `Aᶜ`, so `KL(p̂‖p*)` equals the KL between the induced
two-point distributions. The limits follow from `p̂(A) → 1, 0`, and `kl(x‖a)` is maximized over `x ∈ [0,1]`
at an endpoint. ∎
*Check.* `V3`: agreement to `1.7·10⁻¹³`; at `p*(A) = 0.072`, `M = ±40` gives 2.6309 and 0.0747, matching both
limits.

> **An error of unbounded size on a single region costs bounded regret.** Overrating a region the intended
> actor avoids costs up to `log 1/p*(A)`; underrating a region it occupies costs up to `log 1/(1−p*(A))`.
> Unbounded regret needs unboundedly many or unboundedly rare regions — a tail (Prop. 11).

---

## 4. Capacity

**Definition 5 (capacity actor).** For `δ > 0` let `C_δ = {p : KL(p‖q) ≤ δ}`. The capacity actor for `G`
maximizes `J_G` over `C_δ` (any `β ∈ (0,∞]`). Write `p^C_G`. This is the **capacity model**, an actor model in
the sense of Def. 13 with the budget `δ` as its resource.

**Hypothesis (C).** The actual behaviour is the capacity model run on the evaluator, `p̂ = p^C_{F̂}`. Under (C)
the regret is `R^C = J_F(p^C_F) − J_F(p^C_{F̂})`.

**Lemma 5.1 (form of the capacity actor).** For non-constant `G`, `t ↦ KL(p_{G,t}‖q)` is continuous and
strictly increasing on `[0,∞)`, from 0 at `t = 0` towards its limit `log 1/q(argmax G)` as `t → ∞`. Let
`λ_δ(G)` be the unique `t` with `KL(p_{G,t}‖q) = δ`, or `+∞` if `δ ≥ log 1/q(argmax G)`. Then
`p_{G, min(β, λ_δ(G))}` maximizes `J_G` over `C_δ`. It is the unique maximizer except when `β = ∞` and
`δ > log 1/q(argmax G)`.
*Proof.* `d/dt KL(p_{G,t}‖q) = t·Var_{p_{G,t}}(G) > 0`, and `p_{G,t} → q(·|argmax G)` as `t → ∞`. If
`β ≤ λ_δ`, the unconstrained maximizer `p_{G,β}` is feasible, hence optimal. If `β > λ_δ`, the problem is a
concave maximization over a convex set with a Slater point (`q`). The Lagrangian
`E_pG − (1/β + μ)·KL(p‖q) + μδ` is maximized by `p_{G,1/(1/β+μ)}`. The choice `μ = 1/λ_δ − 1/β ≥ 0`
satisfies complementary slackness. Uniqueness for `β < ∞` follows from strict concavity of `J_G`. For
`β = ∞` the same argument holds with `1/β = 0`, and the maximizer is unique when `δ ≤ log 1/q(argmax G)`
(a non-constant linear functional on a strictly convex set). For larger `δ`, every distribution on
`argmax G` inside `C_δ` is a maximizer, and `p_{G,∞}` is the one of least KL. All results below hold for
any choice of maximizer. ∎

**Corollary 5.2 (the exchange rate is a shadow price).** For non-constant `G` and
`δ ∈ (0, log 1/q(argmax G))`, the value `V_G(δ) = sup_{p∈C_δ} E_pG` is differentiable, with
`V_G'(δ) = 1/λ_δ(G)`. Consequently:

(i) the effective exchange rate of the capacity actor is the inverse marginal value of capacity, so a
price and a budget are one primitive;

(ii) the boundedness cost of the pure capacity actor, as a function of capacity, is `g(δ) = max F − V_F(δ)`
— Stratonovich's value-of-information curve.

*Proof.* Along `λ ↦ p_{G,λ}`: `dV/dλ = Var_{p_{G,λ}}(G)` and `dδ/dλ = λ·Var_{p_{G,λ}}(G) > 0` (Lemma 5.1). ∎
*Check.* `V13`: `1/V'(δ) = λ_δ` to relative `3.3·10⁻⁸`.

**Definition 6 (width).** `σ_δ(E) = sup_{p∈C_δ} E_pE − E_qE`, and `w_δ(E) = σ_δ(E) + σ_δ(−E)`, the width of
`C_δ` along `E`.

**Theorem 5 (the width is the exact worst case).**
(i) For every `β ∈ (0,∞]`, `δ > 0`, `F`, `E`: `0 ≤ R^C ≤ E_{p^C_{F̂}}E − E_{p^C_F}E ≤ w_δ(E)`.
(ii) For `β = ∞`: `sup_F R^C(F; E, δ) = w_δ(E)`, approached by `F = −cE`, `c ↑ 1`.
(iii) For `β < ∞` with `β > λ_δ(E) + λ_δ(−E)`: `sup_F R^C ≥ (1 − λ_δ(E)/β)·w_δ(E)`.

*Proof.* (i) `p^C_F` maximizes `J_F` over `C_δ` and `p^C_{F̂} ∈ C_δ`, so `R^C ≥ 0`. `p^C_{F̂}` maximizes `J_{F̂}`
over `C_δ` and `p^C_F ∈ C_δ`, so `J_{F̂}(p^C_{F̂}) ≥ J_{F̂}(p^C_F)`, which rearranges to the middle
inequality. Both measures lie in `C_δ`, which gives the last one.
(ii) With `F = −cE`, `0<c<1`: `p^C_F` minimizes `E_pE` over `C_δ` and `p^C_{F̂}` maximizes it (`F̂ = (1−c)E`;
for `β = ∞` positive rescaling does not move the argmax). So `R^C = c·[σ_δ(E) + σ_δ(−E)] = c·w_δ(E)`.
(iii) The same construction with both constraints binding gives `c·w_δ`, because the KL terms cancel at
`KL = δ`. Binding requires `cβ ≥ λ_δ(−E)` and `(1−c)β ≥ λ_δ(E)`. ∎

*Check.* `V4`: 0 violations / 3,000 (mixed finite and infinite `β`); `R^C/w` p5/p50/p95 = 0.009 / 0.095 /
0.268; the construction with `c = 0.999` returns `R^C/w = 0.9990` in every instance.

> **No bound depending only on `(E, δ)` can be below `w_δ(E)`.** The width is the capacity-form normal
> form, and it is a support function, not a product.

**Proposition 6 (the width, computed).**
(i) (Donsker–Varadhan) `σ_δ(E) = inf_{λ>0} [δ + Λ_q(λ)]/λ`.
(ii) As `δ → 0`: `σ_δ(E) = √(2δ·Var_q E) + O(δ)`, so `w_δ(E) = 2√(2δ·Var_q E) + O(δ)`.
(iii) For `δ ≥ log 1/q(argmax E)`: `σ_δ(E) = max E − E_qE`. For `δ` large enough on both sides,
`w_δ(E) = osc(E)`.

*Proof.* (i) Weak duality: for `p ∈ C_δ`, `λ > 0`, the Gibbs variational inequality gives
`λ(E_pE − E_qE) ≤ KL(p‖q) + Λ_q(λ) ≤ δ + Λ_q(λ)`. Equality holds at `p = p_{E,λ_δ}`, which attains `σ_δ` by
Lemma 5.1. In the case `λ_δ = ∞`, `[δ + Λ_q(λ)]/λ → max E − E_qE` as `λ → ∞`.
(ii) With `λ = λ_δ(E)`: `σ_δ = Λ_q'(λ)` and `δ = λΛ_q'(λ) − Λ_q(λ)`. Taylor at 0 with `v = Var_q E`:
`δ = vλ²/2 + O(λ³)`, so `λ = √(2δ/v) + O(δ)` and `σ_δ = vλ + O(λ²) = √(2δv) + O(δ)`.
(iii) From Lemma 5.1. ∎

*Check.* `V4`: DV formula to `2.0·10⁻¹²`; `σ_δ/√(2δ·Var) = 1.0010, 1.0031, 1.0094` at `δ = 10⁻⁴, 10⁻³, 10⁻²`;
exact saturation at large `δ`.

*Prior art.* `σ_δ(E)` is the worst-case expectation of distributionally robust optimization over a KL ball;
(i) is the standard KL-DRO dual (Ben-Tal et al., Management Science 2013). The χ² analogue is the
variance-regularization view of χ²-DRO (Namkoong & Duchi, NeurIPS 2017). The DRO literature therefore
imports directly into the capacity layer.

**Proposition 7 (a bound with realized travel from the reference).** Let
`σ₊²(E) = sup_{λ>0} 2Λ_q(λ)/λ²` and `σ₋²(E) = σ₊²(−E)`, the upper and lower sub-Gaussian proxies of `E`
under `q` (finite on finite `X`; `≤ osc(E)²/4` by Hoeffding's lemma). For every `p`:
`E_pE − E_qE ≤ √(2σ₊²·KL(p‖q))` and `E_qE − E_pE ≤ √(2σ₋²·KL(p‖q))`. Hence, for soft actors and for capacity
actors alike (`R = R_J` or `R = R^C`, with `p̂`, `p*` the corresponding actors),

```
R ≤ √(2σ₊²·KL(p̂‖q)) + √(2σ₋²·KL(p*‖q)).
```

*Proof.* DV: `E_pE − E_qE ≤ [KL + Λ_q(λ)]/λ ≤ KL/λ + σ₊²λ/2`; minimize over `λ`. Combine with
`R ≤ E_{p̂}E − E_{p*}E`, which is Cor. 1.2 for soft actors and Thm 5(i) for capacity actors. ∎

*Check.* `V4`: 0 violations / 3,000; slack 0.002 / 0.09 / 0.315. It is never looser than
`osc(E)·√(2 max KL)` (always, by Hoeffding).

*Prior art.* The same transportation bound, applied to reward improvement rather than to error, with Rényi
refinements and a best-of-n analysis, is in Mroueh (2024) and Mroueh & Nitsure (TMLR 2025).

**Remark 7.1 (historical note: the v5 normal form).** `R ≤ osc(E)·TV(p̂,p*) ≤ osc(E)·√(2δ)` with
`δ = max(KL(p*‖q), KL(p̂‖q))` is valid (Prop. 10(a) applied to the pair `(p̂, p*)`, Pinsker, triangle
inequality) and dominated by
Props 2 and 7. **The v5 capacity-ball version `osc_δ(E)·√(2δ)` is not valid.** "`sup − inf` of `E` over a
set of distributions" is ill-typed, and under a hard constraint its three readings give:

| Reading | Violation rate, `δ ∈ [10⁻³,10⁻²)` | `[10⁻²,10⁻¹)` | `[10⁻¹,1)` | `[1,4)` |
|---|---|---|---|---|
| (a) `sup/inf` of `E_pE` over `C_δ` | 0.62 | 0.08 | 0.00 | 0.00 |
| (b) pointwise over states whose point mass lies in `C_δ` | 1.00 | 1.00 | 1.00 | 0.54 |
| (c) pointwise over `supp q` (i.e. plain `osc`) | 0.00 | 0.00 | 0.00 | 0.00 |

Reading (a) fails because with binding constraints `R^C = Θ(√δ)` generically, while `osc_δ·√(2δ) = O(δ)`; its correct
use is Theorem 5 without the `√(2δ)`. `V4`, retraction record.


**Proposition 23 (argmax selectors on a common candidate set — tier 2′, v6.4).** Let a random candidate set
`S ⊆ X` be drawn by any mechanism — for instance `n` i.i.d. draws from `q`. Let the intended actor pick
`x* ∈ argmax_{S} F`, and the actual actor pick `x̂ ∈ argmax_{S} F̂`, **from the same `S`** and with a common
tie-breaking rule. With `p*`, `p̂` their laws and `R = E_{p*}F − E_{p̂}F`:

```
0 ≤ R ≤ E_{p̂}E − E_{p*}E.
```

*Proof.* Pathwise, `x̂ ∈ S` gives `F(x*) ≥ F(x̂)`, and `x* ∈ S` gives `F̂(x̂) ≥ F̂(x*)`. Hence
`0 ≤ F(x*) − F(x̂) ≤ F(x*) − F(x̂) + F̂(x̂) − F̂(x*) = E(x̂) − E(x*)`. Take expectations. ∎
*Check.* `V28`: best-of-`k` at equal `k`, 20,000 instances (30 % with ties), 0 violations of either inequality.
R6 found 0 of 1,150 at equal `n`.

*Reading.* Tier 2 (Thm 5(i)) needs an exact maximizer over a *set* containing the intended actor. Prop. 23
needs only that both actors maximize over the *same random* set. That is the coupling that makes best-of-n
safe to compare **at equal `n`**, and **not at matched KL**, where R6 found 4.3 % violations. The same
coupling covers any search that shares its candidate pool — for example reranking a common sample. Unlike
Thm 5, Prop. 23 gives no width: the right-hand side still depends on the actor's selection.
---

## 5. Non-separability

**Lemma 8 (separable bounds are loose when rankings move).** Let `Q(E, δ) > 0` and suppose
`B(E,δ) = a(E)·b(δ)` satisfies `Q ≤ B ≤ L·Q` on `{E₁, E₂} × D`. Let `ρ(δ) = Q(E₁,δ)/Q(E₂,δ)` and
`K = sup_D ρ / inf_D ρ`. Then `L ≥ √K`.
*Proof.* `κ := a(E₁)/a(E₂) = B(E₁,δ)/B(E₂,δ) ∈ [ρ(δ)/L, L·ρ(δ)]` for every `δ`. So
`sup ρ / L ≤ κ ≤ L·inf ρ`. ∎

**Theorem 9 (the worst-case regret is not separable).** Let `E₁` be non-constant, `A ⊂ X` with `q(A) = r ∈ (0,1)`.
Then

```
lim_{δ→0} w_δ(E₁)/w_δ(1_A) = √( Var_q(E₁) / (r(1−r)) ),   and   w_δ(E₁)/w_δ(1_A) = osc(E₁) for all δ ≥ δ̄,
```

with `δ̄ = max{log 1/q(argmax E₁), log 1/q(argmin E₁), log 1/r, log 1/(1−r)}`. Hence, for the pair
`{E₁, M·1_A}` (any `M > 0`; `w_δ` is positively homogeneous),
`K ≥ √(Var_q E₁)/(osc(E₁)·√(r(1−r)))`. `K` is unbounded over any family of instances in which `q(A) → 0`
while `Var_q(E₁)/osc(E₁)²` stays bounded away from 0. By Theorem 5(ii) and Lemma 8, **no bound on the
worst-case regret of the pure capacity maximizer (`β = ∞`) of the form `a(E)·b(δ)` has bounded looseness.**
*Proof.* Prop. 6(ii) on both errors, using `Var_q(1_A) = r(1−r)`; Prop. 6(iii) on both, using `osc(1_A) = 1`. ∎

*Check.* `V5` (`n = 200`, `r = min q`): ratio 62.80 at `δ = 10⁻⁶` vs predicted 62.7957; 5.3013 at large `δ` vs
`osc(E₁) = 5.3013`; `K ≥ 11.8`, so any separable bound is ≥ 3.4× loose on this pair.

**Fixed intent (measured, not proved).** For a single fixed `F` (`n = 2000`, uniform `q`, `β = 30`), a dense
error (`sd_q = 0.61`) and a one-state spike (`sd_q = 0.13`) give `R^C(E₁)/R^C(E₂)` from 13.45 at
`δ = 0.002` to 0.13 at `δ = 7`, a ×103 span. Any separable bound is therefore ≥ 10× loose somewhere on this
pair. `V5`.

> **"Which of two errors is worse" has no capacity-free answer.** At small capacity errors are ranked by
> their variance under the reference; at large capacity, by their extremes. This is the regressional /
> extremal Goodhart distinction, derived here as the two asymptotes of one support function
> (`B_dictionary.md` §3).

---

## 6. The divergence fixes the norm

**Proposition 10 (conjugate pairings).** For all `p` on `X`:

| | Capacity | Error | Inequality |
|---|---|---|---|
| (a) | total variation | oscillation (`L^∞`) | `\|E_pE − E_qE\| ≤ osc(E)·TV(p,q)` |
| (b) | KL | CGF under `q` | `E_pE − E_qE ≤ inf_{λ>0} [KL(p‖q) + Λ_q(λ)]/λ` |
| (c) | χ² | variance under `q` (`L²`) | `\|E_pE − E_qE\| ≤ √(χ²(p‖q)·Var_q E)` |
| (d) | Rényi `D_α`, `α ∈ (1,∞]` | `L^{α*}(q)`, `α* = α/(α−1)` | `E_p\|E\| ≤ exp((α−1)/α · D_α(p‖q))·‖E‖_{L^{α*}(q)}` |

At `α = ∞`, (d) reads `E_p|E| ≤ e^{D_∞(p‖q)}·E_q|E| ≤ E_q|E|/min_x q(x)`: an `L¹` error under the reference
controls the error under `p` only through the maximal density ratio (concentrability).

*Proof.* (a) `∫E d(p−q) = ∫(E−c) d(p−q)` with `c` the midrange, and `|E − c| ≤ osc/2`,
`‖p−q‖₁ = 2TV`. (b) Gibbs variational inequality. (c) Cauchy–Schwarz on
`E_q[(dp/dq − 1)(E − E_qE)]`. (d) Hölder on `E_q[(dp/dq)|E|]`, with
`‖dp/dq‖_{L^α(q)} = exp((α−1)/α · D_α)`. ∎
*Check.* `V6`: 0 violations in each row / 20,000 (errors drawn from Student-t₃).

**Proposition 11 (the order is structural, not a matter of tightness).** Let `(X, 𝒜, q)` be a general
probability space and `E ∈ L¹(q)`.
(i) If `q(E > m) > 0` for all `m` and `log 1/q(E > m) = o(m)` as `m → ∞`, then for every `δ > 0`,
`sup_{KL(p‖q)≤δ} E_pE = +∞`. (Also `E_q e^{λE} = ∞` for every `λ > 0`, so for bounded `F` the entropic model
cannot be run on `F̂`: *[this remark assumes (E)]*.)
(ii) If `Var_q E < ∞`, then `sup_{χ²(p‖q)≤δ} E_pE ≤ E_qE + √(δ·Var_q E)`.
Pareto tails with shape `a > 2` satisfy both hypotheses.

*Proof.* (i) Let `r = q(E>m)`, `q_m = q(·|E>m)`, `p = (1−ε)q + εq_m`. KL is convex in its first argument and
`KL(q_m‖q) = log 1/r`, so `KL(p‖q) ≤ ε·log 1/r`. Also `E_pE ≥ (1−ε)E_qE + εm`. Since `E ∈ L¹`, `r → 0`. Take
`ε = δ/log(1/r)` (≤ 1 for large `m`): then `KL ≤ δ` and `E_pE ≥ (1−ε)E_qE + δm/log(1/r) → ∞`. For the
parenthetical: `E_q e^{λE} ≥ e^{λm}r(m) = e^{λm − o(m)} → ∞`. (ii) Prop. 10(c). ∎

*Check.* `V6`, Pareto `a = 3` (`Var = 0.75`): the χ²-exposure bound at `δ = 0.1` is 0.274. Mixtures with exact
`KL ≤ 0.093` reach `E_pE − E_qE = 1.08, 54.3, 2.7·10⁵, 1.4·10¹³` at `m = 10², 10⁴, 10⁸, 10¹⁶`.

> **Choosing a regularizer is choosing which norm of the evaluator's error must be controlled.** KL needs
> exponential moments, χ² needs a variance, `D_∞` needs only a mean but pays the density ratio. Errors with
> finite variance and heavy tails are controlled by χ² and not by KL at any budget.

*Prior art.* Huang et al. (ICLR 2025, χPO) argue, via coverage and single-policy concentrability, that KL
regularization is too weak to prevent overoptimization and that χ² regularization is preferable. Kwa et
al. (NeurIPS 2024) give the tail version. Mroueh & Nitsure give transportation and Rényi bounds. Prop. 10
organizes these as one conjugate pairing; that organization is the part not found stated elsewhere.

---

## 7. Identification, gauge, and the intent ray

**Definition 10 (intent ray and misalignment measures; v6.4, R7-0).** Let `F` be non-constant, and let
`p̂` be a full-support actual behaviour.
- The **intent half-ray** is `𝓡⁺_F = {p_{F,t} : t ≥ 0}`, with `p_{F,t} ∝ q·e^{tF}`.
- The **regret curve** is `M(t) = KL(p̂‖p_{F,t})` for `t ∈ ℝ`.
- The **price measure** at a declared price `β` is `M_price = M(β)`.
- The **free measure** is `M_free = D_⊥ = inf_{t≥0} M(t)`.
- The **budget measure** is `M_budget = M(λ)`, where `λ ≥ 0` is the unique `t` with
  `KL(p_{F,t}‖q) = KL(p̂‖q)`. This `λ` exists and is unique iff `KL(p̂‖q) < log 1/q(argmax F)`, by Lemma 5.1:
  `t ↦ KL(p_{F,t}‖q)` is continuous and strictly increasing, from 0 towards `log 1/q(argmax F)`. Otherwise
  `M_budget` is undefined: this is saturation.

*Note.* A definition may cite an earlier result only for well-definedness; this one cites Lemma 5.1 (§4).
Named quantities that need `t̂` — `D_∥`, `X_anti` — are introduced in Thm 13, after `t̂` is shown to exist.

**Proposition 12 (what behaviour identifies).** *[Assumes (E): identification is relative to the actor model.]* (i) For every `s > 0`, `p_{F̂,β} = p_{sF̂, β/s}`. (ii) For every
`h`, the actor `(q, F̂, β)` and the actor `(q' ∝ q·e^{h}, F̂ − h/β, β)` produce the same behaviour.
Behaviour therefore identifies neither `β` nor `q` separately from the evaluator: only the tilted measure.
*Proof.* Substitution into Definition 1. ∎

**Theorem 13 (intent-ray decomposition).** Let `F` be non-constant, and let `A(t) = log E_q e^{tF}`. There
is a unique `t̂ ∈ ℝ` with `E_{p_{F,t̂}}F = E_{p̂}F`; `t̂ < 0` iff `E_{p̂}F < E_qF`.

(a) *(Full ray.)* For every `t ∈ ℝ`: `KL(p̂‖p_{F,t}) = KL(p̂‖p_{F,t̂}) + KL(p_{F,t̂}‖p_{F,t})`.

(b) *(Half-ray; canonical from v6.1.)* Let `t̂⁺ = max(t̂, 0)`. For every `t ≥ 0`:

```
KL(p̂‖p_{F,t}) = KL(p̂‖p_{F,t̂⁺}) + KL(p_{F,t̂⁺}‖p_{F,t}) + t·[E_qF − E_{p̂}F]⁺.
```

With `t = β` and Theorem 1:

```
β·R_J = D_⊥ + D_∥ + X_anti,
  D_⊥    = KL(p̂‖p_{F,t̂⁺}) = min_{t≥0} KL(p̂‖p_{F,t})        (transverse error)
  D_∥    = KL(p_{F,t̂⁺}‖p*) = A(β) − A(t̂⁺) − (β − t̂⁺)A'(t̂⁺)  (axial error: right objective, wrong intensity)
  X_anti = β·[E_qF − E_{p̂}F]⁺                             (anti-alignment excess; nonzero iff t̂ < 0)
```

*Proof.* `t ↦ E_{p_{F,t}}F` is continuous and strictly increasing (derivative `Var > 0`), with limits
`min F`, `max F`, and `p_{F,0} = q`. `E_{p̂}F` lies strictly between the limits because `p̂` has full support;
this gives existence, uniqueness, and the sign statement.

(a) `log(p_{F,t̂}/p_{F,t}) = (t̂ − t)F − A(t̂) + A(t)` is affine in `F`, so its expectation under `p̂` equals its
expectation under `p_{F,t̂}` (Csiszár's Pythagorean identity).

(b) If `t̂ ≥ 0`, this is (a). If `t̂ < 0`, then `t̂⁺ = 0` and
`KL(p̂‖p_{F,t}) − KL(p̂‖q) − KL(q‖p_{F,t}) = E_{p̂}[−tF + A(t)] − E_q[−tF + A(t)] = t(E_qF − E_{p̂}F)`.

Finally, by (a), `KL(p̂‖p_{F,t}) = KL(p̂‖p_{F,t̂}) + [A(t) − A(t̂) − (t − t̂)A'(t̂)]`: a constant plus a convex
function of `t` with unconstrained minimizer `t̂`. So its minimum over `t ≥ 0` is at `t̂⁺`, which identifies
`D_⊥` (Def. 10) with `KL(p̂‖p_{F,t̂⁺})`. ∎

*Check.* `V7` checks (a), to `5.5·10⁻¹²` over 5,000 instances. `V14` checks (b), to `3.0·10⁻¹³` over 3,000
instances, 1,052 of them anti-aligned (`t̂ < 0`).

**Reading.**
- `D_⊥` is what no positive rescaling of the target can produce.
- `D_∥` is the cost of pursuing the target itself at the wrong intensity.
- `X_anti` is the extra cost of net movement *against* the target.

With the half-ray, `F̂ = −F` has `D_⊥ = KL(p̂‖q) > 0`, so anti-alignment is no longer invisible to the
transverse part (the v6 full-ray definition gave `D_⊥ = 0`; `D_status.md` rows 50, 54). The half-ray
matches the quotient by **positive** rescalings used by STARC (Skalse et al., ICLR 2024), which compares
reward functions rather than behaviours. The decomposition still says *where* the regret lies; `β·R_J`
says how large it is.

**Corollary 13.1.** *[Assumes (E).]* `D_⊥ = 0` iff `F̂ = aF + c` for some `a ≥ 0` and constant `c` (then `t̂ = aβ`).

**Corollary 13.2 (convention-freedom).** `D_⊥`, `sign(t̂)` and whether `X_anti > 0` depend on `(q, p̂)` and the
positive-affine class of `F` only: `p_{aF+c,t} = p_{F,at}`, so the half-ray depends only on that class.
`D_∥` requires the intended point on the ray, i.e. a unit.
*Check.* `V7` (full ray): `6.4·10⁻¹⁴`. `V14` (half-ray): `3.8·10⁻¹⁰`.

**Corollary 13.3 (rescaling is purely axial).** *[Assumes (E).]* For `F̂ = sF`, `s > 0`: `D_⊥ = X_anti = 0`, `t̂ = sβ`, and
`β·R_J = D_∥ = A(β) − A(sβ) + (s − 1)βA'(sβ) > 0` for `s ≠ 1`.
*Check.* `V7`: `s = 1.7` gives `t̂/β = 1.700000`, `D_⊥ = 2·10⁻¹⁶`, `β·R_J = D_∥ = 0.2218`.

**Remark 13.5 (whether rescaling is harmful depends on the declared convention; v6.3).** *[Assumes (E).]* For
`F̂ = sF`, `s > 0`, the actual actor `p̂ = p_{F,sβ}` lies on the intent ray. Hence:

| Measure (Def. 10) | Cost of rescaling |
|---|---|
| free | `M_free = D_⊥ = 0` |
| budget (the default) | `M_budget = 0`: the budget-matched intended actor is `p̂` itself |
| price | `M_price = β·R_J = D_∥ > 0` for `s ≠ 1` (Cor. 13.3) |

Rescaling is **harmless under the default convention, and harmful only if the intended actor is required to
keep the actual actor's exchange rate.** For best-of-n it is harmless outright: best-of-n is invariant to any
strictly increasing transform of the evaluator.
*Check.* `V26`: at `s = 0.5, 1.7, 3`, `M_price = 0.442, 0.111, 0.226` and `|M_budget| ≤ 4·10⁻¹⁶`; best-of-n
is unchanged under a strictly increasing transform.

> *(v6.1–v6.2 stated, as the replacement of v5's sentence, that "uniform rescaling of a reward is harmless"
> is false in this model. That holds only under the price convention; `D_status.md` row 61.)*

**Corollary 13.4 (second order).** *[Assumes (E).]* For `E = εE₀`, write `a = Cov_{p*}(E₀,F)/Var_{p*}(F)` and
`E₀⊥ = E₀ − aF` (uncorrelated with `F` under `p*`). As `ε → 0` we have `t̂ → β > 0`, so the full-ray and
half-ray decompositions coincide and `X_anti = 0`:
`D_⊥ = (β²ε²/2)·Var_{p*}(E₀⊥) + O(ε³)` and `D_∥ = (β²ε²/2)·a²·Var_{p*}(F) + O(ε³)`.
*Proof.* `t̂ − β = βεa + O(ε²)` from the moment condition. Hence `D_∥ = A''(β)(t̂−β)²/2 + O(ε³)`. And
`β·R_J = (β²ε²/2)·Var_{p*}(E₀) + O(ε³)` from Cor. 1.3. Subtract, using
`Var(E₀) = a²·Var(F) + Var(E₀⊥)`. ∎
*Check.* `V7`: at `ε = 0.003` the two ratios are 1.0009 and 0.968. The `D_∥` ratio converges slowly when
`|a|` is small, as the `O(ε³)` remainder predicts.

**Theorem 17 (every regret notion is a point on one convex curve).** Let `M(t) = KL(p̂‖p_{F,t})` (Def. 10).

(i) `M` is convex on `ℝ`; its minimum over `[0, ∞)` is `D_⊥`, attained at `t̂⁺`.

(ii) `M(β) = β·R_J`. This is the **same-price** counterfactual: the intended actor has the actual actor's
exchange rate.

(iii) If `λ ∈ (0, ∞)` satisfies `KL(p_{F,λ}‖q) = KL(p̂‖q)`, then `E_{p_{F,λ}}F − E_{p̂}F = M(λ)/λ`. This is the
**same-budget** counterfactual: the intended actor has spent the same information. Its raw regret is exact
because the information costs are equal.

(iv) `D_⊥` and `M(λ)` are unchanged under `F ↦ aF + c` with `a > 0`; `M(β)` is not.

*Proof.*
(i) By Thm 13(a), `M(t) = M(t̂) + [A(t) − A(t̂) − (t − t̂)A'(t̂)]`, a constant plus the Bregman divergence of
the convex function `A`. A convex function whose unconstrained minimizer is `t̂` has its minimizer over
`[0, ∞)` at `t̂⁺`.
(ii) Theorem 1.
(iii) Theorem 1 at exchange rate `λ` gives `J^λ_F(p_{F,λ}) − J^λ_F(p̂) = M(λ)/λ`; the terms `KL(·‖q)/λ` are
equal and cancel.
(iv) `p_{aF+c,t} = p_{F,at}`, so the half-ray is the same set of distributions. `D_⊥` is an infimum over that
set, and the budget-matched point is the unique point of that set with `KL(·‖q) = KL(p̂‖q)`, so both are
unchanged. `M(β)` becomes `KL(p̂‖p_{F,aβ})`. ∎

*Check.* `V14`: minimum over a grid never below `D_⊥`; (iii) to `6·10⁻¹²`.

*Measured* (`V14`): over 1,218 random pairs of errors, the same-price and same-budget conventions **rank the
two errors differently in 11.4 %** of pairs. The convention is therefore part of the definition, not a
detail.

**Proposition 16 (gauge group and identified quantities).** *[(g1)–(g3) assume (E); (g4) and the list of
identified quantities assume nothing about the actual actor.]* Consider the transformations:

| | Transformation | Leaves unchanged |
|---|---|---|
| (g1) | `(F̂, β) ↦ (sF̂, β/s)`, `s > 0` | the behaviour `p̂` |
| (g2) | `F̂ ↦ F̂ + c` | the behaviour `p̂` |
| (g3) | `(q, F̂) ↦ (q' ∝ q·e^{h}, F̂ − h/β)` | the behaviour `p̂` |
| (g4) | `F ↦ aF + c`, `a > 0` | the target (positive affine transformations preserve the preference), and the **half-ray** `𝓡⁺_F = {p_{F,t} : t ≥ 0}` as a set |

Given a measured reference `q` and observed behaviour `p̂`:
- **Invariant under (g4), hence identified from `(q, p̂, the target class)`:**
  - `KL(p̂‖q)`;
  - the transverse error `D_⊥` and `sign(t̂)` (Thm 13(b));
  - the budget-matched intended actor and `M(λ)` (Thm 17).
- **Not invariant, so a unit for `F` relative to `β` must be supplied:**
  - `β`, `E`, `R_J`, `g`, `ΔF`, `T`;
  - `M(β)`, `D_∥`, `X_anti`;
  - every width or bound expressed in value units.

*Proof.* (g1)–(g3): Prop. 12, and constants cancel in the normalization. (g4): `p_{aF+c,t} = p_{F,at}`, so
the half-ray is the same set of distributions. Every quantity in the first list is defined from that set,
`q` and `p̂` alone; those in the second change under (g1) or (g4) by direct substitution. ∎
*Check.* `V14`: under random `F ↦ aF + c`, `D_⊥` and `M(λ)` change by at most `3.8·10⁻¹⁰`; `M(β)` changes by
up to 88 nats.

**Definition 7 (reporting rule).** A quantity is **reportable** if it is invariant under (g1)–(g4) given the
measured `(q, p̂)`. Otherwise it must be reported together with the gauge fixing it uses: a unit for `F`
relative to `β`, and how `q` was measured.

**Remark 16.1 (reference misspecification).** By (g3), a wrong reference is behaviourally
indistinguishable from an evaluator error `h/β`. Mechanistically it is a distinct locus: side effects and
impact regularization are statements about `q` (census A12, A13), and the intervention differs. Any
statement using `q` presupposes an independent measurement of it.

**Definition 8 (conventions, misalignment, ε-alignment; revised in R7-0).** A **counterfactual convention**
`κ` fixes the intended behaviour, and with it a measure from Def. 10:

| Convention | Intended behaviour | Measure | Named |
|---|---|---|---|
| budget | `p_{F,λ}`, same KL to `q` as `p̂` | `M_budget` | **misalignment** (the default) |
| free | any point of the half-ray `𝓡⁺_F` | `M_free = D_⊥` | **misalignment**, capability-free |
| price | `p_{F,β}`, the declared price | `M_price = β·R_J` | **regret** at a price |

The actor is **ε-aligned with `F` under `κ ∈ {budget, free}`** iff the measure is at most `ε` nats. Under the
price convention, `M_price ≤ ε` defines **ε-regret**, not ε-alignment. The budget measure is defined only below saturation
(Def. 10).

*Note.*
- **Why the price measure is called a regret rather than misalignment:** Prop. 24(c). It charges an agent that
  pursues the right target at the wrong intensity. *(v6.1–v6.4 defined ε-alignment under the price convention
  too; `D_status.md` row 74.)*
- `M_free ≤ min(M_budget, M_price)` whenever these are defined, since `M_free` is an infimum over the
  half-ray.
- **Comparing a mechanism with itself** — the same algorithm run on the target with the same resource — needs
  an actor model. So it is not a convention of this table but an explanation-layer comparison (Def. 14,
  Prop. 25). *(v6.4 listed it here as an "own-resource convention"; `D_status.md` row 75.)*
- The curve `M(t)` remains available for any actor as a divergence from the Gibbs ray; it is a *regret* only
  under the conventions above.
- **Saturation.** Beyond `KL(p̂‖q) ≥ log 1/q(argmax F)` the actual actor has spent more information than the
  target can use. Every budget-matched intended actor attains `max F`, and is supported on `argmax F`. Report
  `M_free` and the raw same-budget regret `max F − E_{p̂}F` instead. *(v6.1 as first released used `p_{F,∞}`
  here, which gives `+∞` even for an essentially aligned actor — `final_audit.py` F5; `D_status.md` row
  57.)*
- Approaching saturation, `M(λ) = λ·(raw regret)` grows like `λ → ∞` at fixed raw regret. Regret in nats is
  value times the exchange rate, so highly optimized actors register large nat regrets even for small value
  losses. That is also why they are easy to detect (Prop. 18).

**Corollary 17.1 (the capacity actor's regret is the budget convention).** *[Assumes (C).]* Let `δ < log 1/q(argmax F)` and
`δ < log 1/q(argmax F̂)`, and let `β > max(λ_δ(F), λ_δ(F̂))`, so that both capacity constraints bind. Then
`p^C_F` is the budget-matched intended actor of `p̂^C`, and

```
R^C = M(λ)/λ,   with λ = λ_δ(F).
```

If instead `δ ≥ log 1/q(argmax F)` and `β = ∞`, then `R^C = max F − E_{p̂^C}F`, the raw regret of the
saturated case.
*Proof.* By Lemma 5.1, `p^C_F = p_{F,λ_δ(F)}` and `p̂^C = p_{F̂,λ_δ(F̂)}`, with `KL(·‖q) = δ` for both. So
`p^C_F` is the budget match of `p̂^C`, and the information terms of `J_F` cancel, leaving the raw regret. That
equals `M(λ)/λ` by Thm 17(iii). The saturated case follows from `E_{p^C_F}F = max F`. ∎
*Check.* `V18`: 2,903 binding instances, to `1.2·10⁻¹³`; the saturated example is `V19`.

> **Theorem 5's worst-case regret (§4) and the budget convention (§7) are the same object.** The pure
> capacity actor's regret is the same-budget regret, and the width `w_δ(E)` bounds it over all targets. This
> is a reason, beyond gauge invariance, to use the budget convention as the default.

---

## 8. Capability: what optimization pressure does

**Proposition 14.** Let `F` be non-constant.
(i) `g` is strictly decreasing in `β`, with `g'(β) = −Var_{p*}(F)`. *(A statement about the intended behaviour
only.)*
(ii) *[Assumes (E), in (ii)–(iii).]* `T'(0) = −Cov_q(F̂, F)` and `ΔF'(0) = −Cov_q(E, F)`. So `ΔF(β) = −β·Cov_q(E,F) + O(β²)`, which has
either sign.
(iii) `lim_{β→∞} T(β) = max F − E_{q(·|argmax F̂)}[F]`, which is 0 iff `argmax F̂ ⊆ argmax F`.

*Proof.* `d/dβ E_{p_{G,β}}[F] = Cov_{p_{G,β}}(G, F)`; evaluate at `G = F`, and at `β = 0`, where
`p_{G,0} = q`. (iii) `p_{F̂,β} → q(·|argmax F̂)`. ∎
*Check.* `V8`: derivative to `4·10⁻⁵` (finite difference), limit to `4·10⁻⁶`.

> **Neither "capacity is good" nor "capacity is dangerous" holds in general.** Whether more optimization
> helps at first is the sign of the covariance between evaluator and intent under the reference. Whether it
> helps in the end is whether the evaluator's top behaviours are among the intent's.

**Proposition 20 (Goodhart as a covariance — any optimizer; tier 1).** Let `p ≪ q` be the behaviour of *any*
actor and `w = dp/dq`. Then:

```
E_pF − E_qF = Cov_q(w, F̂) − Cov_q(w, E)          (target gain = proxy gain − covariance of the choices with the error)
E_{p₁}F − E_{p₂}F = Cov_q(w₁ − w₂, F)             (regret between any two actors)
```

*Proof.* `E_pG − E_qG = Cov_q(w, G)` for any `G`, since `E_q w = 1` (Price's selection term,
`B_dictionary.md` B11(i)). Apply it with `G = F = F̂ − E`, and to the difference of two actors. ∎
*Check.* `V20`: best-of-`k` on the proxy (its exact distribution), top-`m` selection, and arbitrary
distributions — none of them tilts — to `2·10⁻¹⁵`.

*Reading.* Whatever the optimizer, it raises the proxy by `Cov_q(w, F̂)`, and the target by that amount
minus `Cov_q(w, E)`: **Goodhart's law is the covariance between the optimizer's selection weights and the
evaluator's error.** Prop. 14(ii) is its first-order form for the tilt, where `w ≈ 1 + β(F̂ − E_qF̂)`.

This is a restatement with a useful property — it holds for every actor — **not a finding**. It does
discriminate between optimizers in at least one case. The independent review (`R5_LOG.md`, T-F) placed a
single overrated state and compared actors at matched proxy gain. Best-of-n's covariance with the error was
1.1–21× smaller than the Gibbs actor's, with the gap shrinking as selection strengthens. The reason is that
best-of-n's weight on any state is at most `n·q(x)` (`V26`), however large the error there.

**Proposition 21 (no overoptimization under an affine regression — for any actor that sees only the
evaluator; tier 1, v6.3).** Suppose that under the reference the regression of target on evaluator is affine,
`E_q[F | F̂] = a + b·F̂`. Suppose also that the actor's weights depend on a behaviour only through its
evaluator value: `w = dp/dq = h(F̂)` for some function `h`. Then

```
E_pF − E_qF = b·(E_pF̂ − E_qF̂).
```

The target moves in fixed proportion to the proxy, so gold reward never turns down while the proxy rises.

Covered actors:
- the Gibbs actor, for any reference;
- threshold (top) selection;
- vanilla policy gradient started from a uniform reference;
- best-of-n with a uniform reference and no ties.

*Proof.* By Prop. 20, `E_pF − E_qF = Cov_q(w, F) = Cov_q(w, E_q[F|F̂])`, since `w` is a function of `F̂`. That
equals `b·Cov_q(w, F̂) = b·(E_pF̂ − E_qF̂)`. ∎
*Check.* `V24`: Gibbs, top selection, and arbitrary `F̂`-measurable actors, to `3·10⁻¹⁵`. An actor whose
weights use the residual violates it (median 0.55).

*Reading.* This generalizes `B_dictionary.md` B4 from the Gibbs path under Gaussian structure to every
evaluator-driven optimizer under any affine regression. **Overoptimization therefore requires either a
regression of target on evaluator that bends, or an optimizer whose weights use information beyond the
evaluator** — for example a non-uniform reference entering a gradient method. The independent review's T-D
(vanilla policy gradient, Gaussian joint, uniform reference: a constant gold-to-proxy ratio) is an instance.

**Proposition 22 (the first-order effect of any smooth optimizer; tier 1, v6.3).** Let `p_t` be any
differentiable path with `p_0 = q` and initial velocity `v = ṗ_0`, so `Σ_x v_x = 0`. Then

```
d/dt E_{p_t}F |_{t=0} = Σ_x v_x F_x = Cov_q(v/q, F).
```

Two cases:
- **Gibbs actor:** `v/q = F̂ − E_qF̂`, which gives `Cov_q(F̂, F)` — Prop. 14(ii).
- **Vanilla softmax policy gradient** on `E_pF̂`, from logits `log q`, with step `η`:
  `v_x = η·q_x·(q_x(F̂_x − E_qF̂) − Σ_y q_y²(F̂_y − E_qF̂))`. This gives
  `η·Σ_x q_x²(F_x − E_qF)(F̂_x − E_qF̂)`, a **`q²`-weighted** covariance.

*Proof.* Differentiate `Σ_x p_t(x)F_x`. For the policy gradient, use `∂p_x/∂θ_y = p_x(1{x=y} − p_y)` with
`θ̇ = η·q ⊙ (F̂ − E_qF̂)`. ∎
*Check.* `V25`: the Gibbs path to `9·10⁻⁷` (finite difference), the policy-gradient formula to relative
`4·10⁻⁵`. The two optimizers' initial effects have **opposite signs in 80 of 2,000** random instances.

*Reading.* **Whether a small amount of optimization helps depends on the optimizer's geometry, not only on the
proxy and the target.** Prop. 14(ii)'s criterion `Cov_q(F̂, F) > 0` is the Gibbs (natural-gradient) case. For a
vanilla gradient the criterion weights behaviours by `q²`, so a few high-probability behaviours dominate. The
independent review's T-B built an instance where `Cov_q > 0` but the vanilla-gradient effect is negative.
The same holds for best-of-n, whose first-order weight is the **rank** of `F̂`, not its value. Its sign
disagrees with `Cov_q(F̂,F)` in 2.45 % of R6's random instances, and on a constructed instance with
`Cov_q = +18.6` (R6, P6–P7).

**Measured** (`V8`: 300 random instances per error scale, `β ∈ [2⁻², 2¹¹·⁷⁵]`):

| error scale | 0.2 | 1 | 4 | 8 |
|---|---|---|---|---|
| total regret monotone decreasing in `β` | 0.86 | 0.53 | 0.38 | 0.37 |
| monotone increasing | 0.00 | 0.01 | 0.14 | 0.25 |
| strict interior optimum | 0.14 | 0.45 | 0.43 | 0.30 |
| raw alignment regret non-monotone | 0.99 | 0.77 | 0.58 | 0.47 |
| raw alignment regret negative somewhere | 0.79 | 0.62 | 0.52 | 0.53 |
| P(monotone decreasing \| argmax agrees) | 1.00 | 0.97 | 0.85 | 0.88 |
| median `β` minimizing total regret | 64 | 22.6 | 4 | 1.7 |

The comparative static "optimal `β` falls as error grows" reproduces on this generator. **It is a property
of the generator, not a theorem**; Prop. 14 constrains only its endpoints.

---

## 9. Observation: what an overseer can detect

An overseer sees behaviour, not objectives. This section adds the minimal observation model: i.i.d.
samples of behaviour, optionally tagged with a context.

**Proposition 18 (harm bounds detectability).** An overseer observes `n` i.i.d. behaviours drawn from either
`p̂` or `p*`, both known exactly — the most favourable case for the overseer. Let `P_e*(n)` be the minimal
average error probability of a test with equal priors. Then:

- `lim_{n→∞} −(1/n)·log P_e*(n) = C(p̂, p*)`, the Chernoff information (Chernoff 1952);
- `C(p̂, p*) ≤ min{KL(p̂‖p*), KL(p*‖p̂)} ≤ β·R_J`.

**No test on behaviour has an error exponent above `β·R_J`.** Distinguishing the actual from the intended
actor with error probability `ε` needs, asymptotically, at least of order `log(1/ε)/(β·R_J)` samples.

*Proof.* The first statement is Chernoff's theorem. For `λ ∈ [0,1]`, Jensen's inequality gives
`−log Σ p̂^λ p*^{1−λ} = −log E_{p̂}[(p*/p̂)^{1−λ}] ≤ (1−λ)·KL(p̂‖p*)`, and symmetrically `≤ λ·KL(p*‖p̂)`.
Both bounds hold for every `λ`, and each is at most the corresponding KL, so
`C = max_λ(·) ≤ min{KL(p̂‖p*), KL(p*‖p̂)}`. Theorem 1 gives `KL(p̂‖p*) = β·R_J`. ∎
*Check.* `V16`: 0 violations / 5,000; `C/(β·R_J)` p5/p50/p95 = 0.168 / 0.262 / 0.538.

> **In the entropic model, harm in nats caps detectability.** The detection exponent is at most the regret
> in nats; on the `V16` generator it is 17–54 % of it. A misalignment that costs few nats is necessarily
> slow to detect from behaviour, **asymptotically**, even when the intended behaviour is known.
>
> The statement is about exponents: at small `n` the empirical rate `−(1/n)·log P_e` can exceed `β·R_J`,
> as exact computation shows for `n ≤ 5` (`final_audit.py` F2). Realistic overseers, who do not know `p*`,
> can only do worse.
>
> **Two limits.**
> - **The bound runs one way only.** "Harm in nats" is `β·R_J`, which charges the information cost as well
>   as the lost value. So a misalignment with **zero value regret** can still be readily detectable. The
>   independent review built one for best-of-n (`R5_LOG.md`, T-C). For the Gibbs actor, `ΔF` can be zero or
>   negative while `β·R_J > 0`.
> - **"Harm in nats" is defined for every actual actor at a declared price.** By Thm 1, `β·R_J = KL(p̂‖p*)`
>   for any `p̂`, so the cap applies to every optimizer. *(Corrected in v6.4; the v6.3 text said it was not
>   defined off the entropic actor — `D_status.md` row 68.)* What depends on the actor is the counterfactual.
>   Against a mechanism-relative counterfactual `A(F; r)` (Def. 14) — for example best-of-n on the target at the
>   same `n` — detection is capped by `M_own = KL(p̂‖A(F;r))` (Prop. 25(e)). That is a divergence, and it
>   depends on the attributed mechanism.

**Definition 9 (contexts).** Let `𝒞` be a finite set of contexts. Each context `c` has a reference
`q(·|c)`, a target `F(c,·)`, an actual behaviour `p̂_c` (any full-support distribution), and the intended
behaviour `p*_c = p_{F(c,·),β}(·|c)`. Contexts are drawn from an **evaluation** distribution `ρ_ev` when the
overseer samples, and from a **deployment** distribution `ρ_dep` in use. Contexts are exogenous: the actor does
not choose `c`.

*Note.* Under (E) per context, `p̂_c = p_{F̂(c,·),β}(·|c)` for an evaluator `F̂(c,·)`. v6.4 built this into the
definition.

*Note.* This is the same structure as the closed-loop lift of `B_dictionary.md` B7, with contexts in the role
of disturbances; B7(d) is Prop. 19(i). The two differ only in what varies: B7 measures capacity against a
single reference across disturbances; here each context carries its own reference.

**Proposition 19 (the evaluation gap).**
(i) Deployment regret in nats is `β·R_J^dep = E_{c∼ρ_dep} KL(p̂_c ‖ p*_c)`.
(ii) For an overseer who samples `(c, x)` with `c ∼ ρ_ev`, the error exponent is at most
`E_{c∼ρ_ev} KL(p̂_c ‖ p*_c)`.
(iii) Hence deployment harm exceeds the best achievable detection exponent by at least the **evaluation gap**

```
Γ = Σ_c (ρ_dep(c) − ρ_ev(c)) · KL(p̂_c ‖ p*_c).
```

*Proof.* (i) Theorem 1 per context. (ii) Prop. 18 applied to the joint
distributions of `(c, x)`: by the chain rule their KL is `E_{ρ_ev} KL(p̂_c‖p*_c)`. (iii) Subtract. ∎
*Check.* `V16`: KL of the evaluation joints equals `E_ev KL_c` (0.1401); in the example, harm 2.1009 and
`Γ = 1.9608`.

> **Evaluation gaming** (deceptive alignment, sandbagging, evaluation awareness; census B3, D6, D7) **is the
> regime of small evaluation-weighted divergence and large `Γ`.** The core does not model how an actor comes
> to condition on contexts the overseer undersamples. It does give the quantity to estimate, and the bound
> it obeys.


**Definition 11 (the misalignment contract; R7-0).** A **misalignment measure** assigns to a non-constant
target `F`, a declared convention `κ`, and a full-support actual behaviour `p̂` a value `M ∈ [0, ∞]`, or
declares it undefined. It must satisfy:

| | Axiom |
|---|---|
| **M1** (identity) | `M = 0` iff `p̂` is an intended behaviour under `κ` |
| **M2** (sign) | `M ≥ 0` |
| **M3** (representation) | `M` is unchanged when `F` is replaced by `aF + c`, `a > 0`, and every declared quantity carrying the unit of `F` is transformed with it (`β ↦ β/a`) |
| **M4** (behavioural) | `M` depends on the agent only through `p̂`, or its per-context laws |
| **M5** (misdirection, not intensity) | if `p̂ = p_{F,t}` for some `t ≥ 0` — the agent pursues the target itself, at some intensity — then `M = 0` |
| **M6** (substrate-free) | `M` is defined for every full-support `p̂ ∈ Δ(X)`, or declared undefined by an explicit rule |
| **M8** (contexts) | with contexts (Def. 9), `M` applies per context `c`, with aggregates `Σ_c ρ(c)·M_c` for the deployment and evaluation context laws `ρ_dep`, `ρ_ev` |

Two further conditions bind **the R7 refactor**, not a measure as such:
- **M7:** every refactored measure coincides with its v6.4 counterpart whenever the dropped assumptions hold.
- **M9:** the sanity suite of `verify.py` V30 passes.

*Note (mechanism-relative comparisons).* A comparison between a mechanism and the same mechanism run on the
target (Def. 14) depends on the attributed mechanism and resource. So it fails M4 by construction, and it is
an explanation-layer quantity, not a misalignment measure (Prop. 25).

*Note (a limit of any behavioural measure).* M4 and M5 together exempt only **systematic intensity**. An agent
that pursues the target but errs unsystematically — noise, slips — is behaviourally misdirected, and every
measure satisfying M4 must register it as such. Separating "wrong objective" from "unsystematic error" needs
an actor model: the explanation layer, not the measurement layer.

**Proposition 24 (the v6.4 measures against the contract; tier 1).** Let `F` be non-constant and `p̂` have
full support.
- (a) `M_budget` satisfies M1–M6 and M8 wherever it is defined — below saturation (Def. 10).
- (b) `M_free` satisfies M1 (its intended set is the half-ray), M2–M6 and M8.
- (c) `M_price` satisfies M1–M4, M6 and M8, but **not M5**: for `p̂ = p_{F,t}` with `t ≠ β`,
  `M_price = KL(p_{F,t}‖p_{F,β}) > 0`.
- (d) The raw value regret `ΔF = E_{p_{F,β}}F − E_{p̂}F` satisfies neither M1 nor M2.

*Proof.*
- M2, and the "only if" half of M1: `KL ≥ 0`, with equality iff the arguments coincide.
- M1 "if": by the definitions in Def. 10 and Def. 8.
- M3: Thm 17(iv) for (a) and (b). For (c), `p_{aF+c, β/a} = p_{F,β}`.
- M4 and M6: the measures are functions of `(q, F, p̂)` and the convention.
- M5: if `p̂ = p_{F,t}`, then `KL(p̂‖q) = KL(p_{F,t}‖q)`, so `λ = t` by uniqueness (Lemma 5.1), giving
  `M_budget = 0`. Also `M_free ≤ M(t) = 0`. For (c), `p_{F,t} ≠ p_{F,β}` when `t ≠ β`, because `F` is
  non-constant.
- M8: apply the definition per context (Def. 9).
- (d): an agent at `p_{F,t}` with `t > β` has `ΔF < 0` (Prop. 14(i)). Any `p̂ ≠ p_{F,β}` with the same mean of
  `F` has `ΔF = 0`. ∎

*Check.* `V30`:
- 600 random instances per axiom, with 0 violations for the budget and free measures.
- The price measure fails M5 in 600 of 600 (median 0.23 nats).
- `ΔF < 0` in 327 of 600 over-optimizing agents.
- The sanity suite: an agent pursuing the target at half or three times the price, or staying at its default,
  scores 0 on the budget and free measures and 0.07–0.37 nats on the price measure. Sign-flipped, random and
  wrong-target agents score positive on all three. A context-split agent scores 0 in evaluation and 0.77
  (budget) in deployment.

*Reading.* **This fixes the common-sense meaning of "misalignment" in the framework.** Misalignment is
measured by `M_budget` (the default) or `M_free`. `M_price = β·R_J` is a **regret**. It also charges an agent
that pursues the right target too weakly or too strongly, which common sense calls a difference in
capability, not misalignment. Thm 1 is unaffected: it is an identity for the regret. What changes is which
quantity the word "misalignment" names (Def. 8; `D_status.md` row 74).

**Definition 12 (alignment instance; formal).** An **alignment instance** is a tuple `(X, q, F, F̂, R, κ)`:
- a finite behaviour set `X` with a full-support reference `q` (standing assumption S);
- a non-constant target `F`, and an evaluator `F̂` (Def. 1);
- a resource `R`: a price `β ∈ (0, ∞]` (Def. 2), a budget `δ`, or both (Def. 5);
- a convention `κ` (Def. 8).

Optionally, it also has contexts (Def. 9).

*Note.* By Cor. 5.2, one resource suffices for the soft actor or the pure capacity actor. The target proper is
the positive-affine class `[F]₊`. An instance fixes a representative only when it reports value-unit or
price-convention quantities (Prop. 16, Def. 7). No principal is assumed: the target can be teleonomic, such as
fitness. The R7 refactor will move `F̂` and parts of `R` to an explanation layer (`ROADMAP.md` §2A).


**Definition 14 (mechanism-relative comparison; explanation layer; R7-1).** Let the actual behaviour be
attributed to an actor model `A` (Def. 13) with resource `r`: `p̂ = A(F̂; q, r)`. The **mechanism-relative
intended behaviour** is `A(F; q, r)`: the same mechanism, run on the target, with the same resource. Define

```
R_own = E_{A(F;q,r)}F − E_{p̂}F        (value units),
M_own = KL(p̂ ‖ A(F; q, r))            (nats; when A(F; q, r) has full support).
```

**Proposition 25 (mechanism-relative comparisons against the contract; tier 1 given the attribution).**
- (a) `M_own` satisfies M1, M2, M6 (whenever `A(F;q,r)` has full support) and M8. It also satisfies the
  mechanism analogue of M5: `M_own = 0` when `p̂ = A(F; q, r)`, i.e. the mechanism pursues the target itself.
- (b) `M_own` satisfies M3 when the model is equivariant under positive affine maps of its objective, with the
  resource transformed accordingly. Argmax selectors are invariant outright.
- (c) **`M_own` violates M4.** It depends on the attributed `(A, r)`, which behaviour does not identify. Under
  the entropic model, `p̂ = p_{F̂,β} = p_{sF̂, β/s}` (Prop. 12), and the two attributions give intended behaviours
  `p_{F,β}` and `p_{F,β/s}`, hence different `M_own`.
- (d) **`R_own` violates M1 and M2.**
  - M1: a selector whose evaluator only reorders behaviours of equal target value has `R_own = 0` with
    `p̂ ≠ A(F; q, r)`.
  - M2: vanilla policy gradient run for the same number of steps on `F̂ = 2F` gains target faster, so
    `R_own < 0`.
  - For argmax selectors on a common candidate set, `0 ≤ R_own` (Prop. 23), so M2 holds there, but M1 still
    fails.
- (e) Detection against the mechanism-relative counterfactual is capped by `M_own`: the Chernoff exponent
  satisfies `C(p̂, A(F; q, r)) ≤ M_own`.

*Proof.* (a), (e): properties of `KL`, and the Chernoff bound `C(P,Q) ≤ KL(P‖Q)`. M8: apply per context.
(b): substitution. (c): Prop. 12(i) with `s ≠ 1`, and `p_{F,β} ≠ p_{F,β/s}` for non-constant `F`. (d): the
constructions are checked in `V31`. ∎
*Check.* `V31`:
- the two attributions of one behaviour give `M_own` = 0.231 and 0.294 nats;
- `R_own = 0` exactly, with a behaviour at KL 0.210 nats from the intended one;
- `R_own < 0` for the policy-gradient pair, in 200 of 200 instances;
- `M_own = 0` for best-of-n on the target at the actor's `n`;
- best-of-n's `M_own` is unchanged under positive affine maps of the target;
- 0 violations of the detection cap in 1,000 instances.

*Reading.* "Did this mechanism, with its resources, do what it would have done on the target?" is a
legitimate **engineering** question, and `M_own` answers it with a detection guarantee. It is not the
**misalignment** question, because its answer depends on how the behaviour is explained. Misalignment stays
the behavioural budget or free measure (Def. 8, Prop. 24). The price measure is the mechanism-relative
measure for the entropic model with the price as its resource. That is the structural reason it both needs a
unit and fails M5.

---

## 10. Substrates

The formalism applies wherever behaviour is (approximately) an exponential tilt of a reference. Whether a
substrate supports **value-unit** statements depends on Prop. 12: it needs an independent channel for the
unit of `F` and for `q`. Statements in terms of `D_⊥` and `sign(t̂)` need only `q` and the affine class of `F`.

| Substrate | `β` | Unit channel for `F` | Reference `q` | Status |
|---|---|---|---|---|
| **biology** | `ν ∝ N_e` | log fitness is absolute; `N_e` separately estimable from neutral diversity (`θ = 4N_eμ`, `μ` measured) | neutral mutational distribution, estimable from mutation spectra | value-unit statements supported |
| **AI** | declared KL coefficient | reward units declared by the designer | the reference policy, known | supported, by fiat |
| **humans** *(v6.2)* | logit precision `1/μ`; or `1/λ`, the inverse price of attention (rational inattention) | only when the target is denominated in a measured unit, e.g. money in incentivized choice; otherwise the logit scale normalization applies, as for institutions | default-choice probabilities: **partly identifiable** from default experiments, under exclusion (`B_dictionary.md` B12) | `D_⊥` supported where `q` is identified by default variation; value-unit statements only with monetary targets |
| **institutions** | selection intensity / logit precision | **none**: in logit models only `V/μ` is identified, and the scale is normalized (Train 2009) | "practice distribution absent selection" — a modelling choice | value-unit statements **not** supported; `D_⊥` only relative to a modelled `q` |

**Biology (imported).** In the weak-mutation regime the stationary distribution over genotypes is
`p(g) ∝ p₀(g)·exp(ν·log f(g))`. Here `p₀` is the neutral distribution, and `ν` is proportional to `N_e`; the
constant depends on the substitution model (Moran vs Wright–Fisher); the v5 values are carried, not
re-verified. The maximized functional is Iwasa's (1988) free fitness; Sella & Hirsh (2005) and Manhart,
Haldane & Morozov (2012) extend the correspondence. Conditions inherited: weak mutation, reversible substitution,
stationarity. For an objective that is a trait rather than log fitness, the exchange rate is `ν` times the
local selection gradient.

**AI.** `β` is the inverse KL coefficient, and the Gibbs actor is the optimum of KL-regularized
optimization. **Actual training paths need not be Gibbs paths** (C_boundary, C7).

**Institutions.** v5 flagged this case as weakest; Prop. 12 says why. Survival-versus-performance data
identify `β` only relative to the performance measure, i.e. relative to `F̂`, never `F`. With Prop. 16, the
unit problem can be avoided by reporting only gauge-invariant quantities (`D_⊥`, `M_budget`). The remaining
obstacle is the **reference** `q`, which for institutions has no independent measurement.

**Humans (v6.2).** The logit actor with default weights is the entropic actor (tier 4). The
rational-inattention actor, whose reference is its own optimized choice marginal, has an exact regret
identity with a marginal correction (`B_dictionary.md` B7(e), tier 4′). So the human actor needs no new
carrier. What distinguishes humans from institutions is the reference: default experiments shift `q` while
— under exclusion — leaving the evaluator fixed, which identifies `q` within a parametric family (B12). The
exclusion restriction fails to the extent that defaults act as recommendations. Time inconsistency splits
along the framework's existing boundary: naive present bias is a dynamic-layer phenomenon, and
sophisticated present bias is an intrapersonal game (B §12(c)).

**Related framework.** Gottwald & Braun (Neural Computation 2019) develop the free-energy
bounded-rationality framework for systems of agents across economic, artificial and biological settings.
They do not address misspecified objectives.

**Per link.** A delegation chain has one `β` per link. Ratios of `β` across links are meaningful only
given a common unit across links. `D_⊥` per link is unit-free. See `C_boundary.md` §5.3.

**One boundary, four names.** `F` must not depend on what the actor does:
- frequency-dependent selection (biology);
- multi-agent settings (AI);
- strategic interaction (institutions);
- intrapersonal games of sophisticated present-biased agents (humans; v6.2, `B_dictionary.md` §12(c)).

See `C_boundary.md` §3 for the full boundary, which has two conditions, not one, and for the v6.2 refinement:
a reference that is optimized as part of the capacity (rational inattention) is not a violation.

---

## 11. What the core forbids

Each item is a statement the core entails, whose negation it rules out, with the result it rests on.

1. **No capacity-free ranking of errors**, and no separable bound on worst-case regret with bounded
   looseness (Thm 9). *Testable:* two evaluator errors with `Var_q(E₁) > Var_q(E₂)` but `osc(E₁) < osc(E₂)`
   have crossing gold-versus-capacity curves (`C_boundary.md` C8). With matched variances the curves tie
   to leading order at small capacity and separate at large capacity; they need not cross. The crossing
   was found for every optimizer tested (R5, R6), but **where** it falls is optimizer-specific: at KL 0.026
   for vanilla policy gradient, 0.54 for Gibbs, 4.7 for best-of-n.
2. **KL-limited optimization does not bound exposure to errors with sub-exponential tails, at any budget**;
   χ²-limited optimization does, if the variance is finite (Prop. 11).
3. **For the entropic actor, an error confined to one region has bounded cost in nats**, whatever its size
   (Prop. 4, under (E)).
4. **For the entropic actor, rescaling the target produces zero transverse error** (under (E)). It costs exactly the axial error of Cor. 13.3
   under the price convention, and nothing under the budget or free conventions (Remark 13.5).
5. **For the entropic actor (E), the initial effect of optimization has the sign of `Cov_q(F̂, F)`**, and its
   terminal effect is set by argmax agreement (Prop. 14). For any other smooth optimizer, the initial sign is
   the covariance in that optimizer's own geometry (Prop. 22). A vanilla gradient can have the opposite
   sign.
6. **For jointly Gaussian intent and evaluator under the reference, the Gibbs path never overoptimizes**:
   gold gain is exactly linear in `d = √KL`, with slope `√2·ρ_q(F,F̂)·sd_q(F)` (`B_dictionary.md` §4).
   Overoptimization requires non-Gaussian joint structure. This is the KL-tilt counterpart of El-Mhamdi &
   Hoang (2024): Gaussian discrepancies give only a weak Goodhart effect under selection. **Tier 1 (Prop. 21):**
   under any affine regression of target on evaluator, no optimizer whose weights depend only on the
   evaluator overoptimizes.
7. **No test on behaviour detects a departure from the intended behaviour with an error exponent above
   `β·R_J`** (Prop. 18). This holds for any actual actor, measured against the Gibbs intended actor at a
   declared price (tier 1). `β·R_J` is the price-convention *regret*. The budget-convention misalignment caps
   detection against the budget-matched counterfactual in the same way (Chernoff ≤ KL).
8. **Deployment harm exceeds the achievable detection exponent by at least the evaluation gap `Γ`**
   (Prop. 19).
9. **Price and budget conventions disagree.** They rank errors differently in a positive fraction of cases
   (11.4 % on the `V14` generator, Thm 17), so any claim "error `A` is worse than error `B`" must name its
   convention.

## 12. Scope conditions

- **Finite `X`**, except Prop. 11 and `B_dictionary.md` Prop. B4. The proofs extend to general spaces under exponential integrability of
  `F`, `F̂`, and `E` in a neighbourhood of `[0, β]`.
- **Actor.** See the assumption tiers at the top of this file. Tier-1 results hold for any actual actor.
  Tier 2 holds for exact maximizers, tier 2′ for argmax selectors compared at equal budget. **The gauge is actor-specific.** For the entropic actor, behaviour identifies the evaluator up
  to positive affine maps and a reference shift (Prop. 16). For best-of-n it identifies only the evaluator's
  ordering: any strictly increasing transform leaves behaviour unchanged (`V26`). Identification statements
  must name the actor class. The independent review's tests of which tier-4 predictions transfer to other
  optimizers are summarized in `C_boundary.md` C7. The exponential-form results (Thm 1, 13, 17; Props 3, 4, 14, 18; Cor. 1.5) are for entropic
  actors. Prop. 15 extends the identity to any exact maximizer of a concave target minus a convex
  regularizer. Best-of-n, quantilizers and gradient-trained policies that do not reach the regularized
  optimum are not covered. Theorem 5(i) needs only that the actor maximizes its objective over a set
  containing the intended actor.
- **Other agents.** Only exact potential games under log-linear learning (`B_dictionary.md` §13). General
  games, collusion and arms races are the largest missing layer (`T1_census_routing.md`).
- **Target.** A single target, linear except in Prop. 15. Sets of targets (aggregation, disagreement,
  multiple selves) are not formalized (`R3_FIX_LOG.md`).
- **Observation.** i.i.d. behavioural samples, optionally with exogenous contexts (§9). No data layer for
  the evaluator; no adaptive or strategic observation.
- **Static.** No dynamics; contexts (§9) are the only structure beyond one-shot behaviour. `X` may be a set of trajectories. KL between trajectory distributions with shared dynamics
  equals the expected sum of per-step action-distribution KLs (chain rule); divergences between occupancy
  measures are different objects.
- **Exogenous frame and existing intent.** `q`, `β`, `F` fixed and not functions of `p`; a single `F`
  exists. See `C_boundary.md` §3.

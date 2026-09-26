---
id: "Core A3 Assumption tiers"
type: "section"
part: "core"
order: 3
updated: "2026-09-26"
---
## Assumption tiers

Each result is tagged with the weakest assumption it needs about the **actual** actor — the behaviour being
assessed. The **intended** actor (the counterfactual) is fixed separately by the comparison convention
(Def. [[Def 8|8]]): the Gibbs actor at a declared price or budget. Comparing a mechanism with itself on the target
needs an actor model, and lives in the explanation layer (Def. [[Def 14|14]]). *(Corrected in v6.4. Earlier tables filed results that need only a Gibbs **intended** actor
as if they needed a Gibbs **actual** actor; rows [[R067|67]]–[[R068|68]]. Refined in R7-1: tier 4 is now the
named hypothesis (E) or (C), stated in each result, and five items that assume nothing about the actual actor
left tier 4; row 76.)*

| Tier | Needs, about the actual actor | Results |
|---|---|---|
| **1** | nothing: any `p ≪ q` (full support where stated). Prop. [[Prop 21\|21]] also needs weights that depend on behaviour only through `F̂`; Prop. [[Prop 22\|22]] needs a differentiable path | **Thm [[Thm 1\|1]]** (the intended actor is Gibbs at a declared price); **Prop. [[Prop 15\|15]]** (the intended actor is an exact regularized optimum); **Thm [[Thm 13\|13]]** (full-support `p̂`); **Thm [[Thm 17\|17]] (i)–(iii)**; the cap in **Prop. [[Prop 18\|18]]** (`C ≤ KL(p̂‖p*) = β·R_J`); both parts of **Prop. [[Prop 19\|19]]**; **Prop. [[Prop 24\|24]]** (the contract); Prop. [[Prop 29\|29]](a) (selection sees only rewarded behaviour); Props [[Prop 6\|6]], [[Prop 10\|10]], [[Prop 11\|11]], [[Prop 20\|20]], [[Prop 21\|21]], [[Prop 22\|22]]; Lemma [[Lemma 8\|8]]; the inequalities in Prop. [[Prop 7\|7]]; [[B07\|B7(a)]]–(e) (for (e), the intended actor is the rational-inattention optimum; R7-2, [[R077\|row 77]]); [[B11\|B11(i)]] |
| **2** | an **exact maximizer** of its evaluator over a set containing the intended actor | Thm [[Thm 5\|5]] (all parts: capacity maximizers); Thm [[Thm 9\|9]]; the regret bound in Prop. [[Prop 7\|7]] |
| **2′** | an **argmax selector over a common random candidate set** (e.g. best-of-n compared at equal n) | Prop. [[Prop 23\|23]] |
| **3** | an exact optimum of `U − φ/β`, with `φ/β − U` convex | none since R7-3: the Bregman identity needs this of the *intended* actor only, so it is tier 1 ([[R078\|row 78]]) |
| **4** | **(E)**: the actual behaviour is the entropic model run on the evaluator from the declared reference, `p̂ = p_{F̂,β}` (Def. [[Def 13\|13]]). **(E_A)**: the same from the actor's own reference, `p̂ = p^{q_A}_{F̂,β}`. **(E_R)**: the reward-coupled agent of Def. [[Def 16\|16]], which reduces to (E_A) per context with evaluator `G + κ_c R`. **(C)**: the capacity model | (E): Cors [[Cor 1.1\|1.1]]–[[Cor 1.5\|1.5]]; Props [[Prop 2\|2]]–[[Prop 4\|4]]; Prop. [[Prop 14\|14]](ii)–(iii); Cors [[Cor 13.1\|13.1]], [[Cor 13.3\|13.3]]–[[Cor 13.4\|13.4]]; Rem. [[Rem 13.5\|13.5]]; [[B04\|B4]]; [[B06\|B6]]; [[B11\|B11(ii)]]–(iii). (E_A): Prop. [[Prop 12\|12]]; Prop. [[Prop 16\|16]] (g1)–(g3); Rem. [[Rem 16.1\|16.1]]; Prop. [[Prop 26\|26]]; [[B12]]. (E_R): Props [[Prop 27\|27]], [[Prop 28\|28]], [[Prop 29\|29]](b), [[Prop 30\|30]]. (C): Cor. [[Cor 17.1\|17.1]] |
| **—** | nothing about the actual actor: facts about the target, the Gibbs family or the capacity problem | Lemma [[Lemma 5.1\|5.1]] (including the monotone mean that was Prop. 14(i)); Cor. [[Cor 5.2\|5.2]] |
| **4″** | log-linear learning in an exact potential game (the group as one entropic actor on joint behaviour) | [[B13]] |

**Layers and tiers are different axes (R7-3).**
- A result's **layer** says what it talks about. The **measurement** layer uses only the declared reference,
  the target, the conventions and the actual behaviour. The **explanation** layer also uses an evaluator, an
  error, the actor's own reference or an actor model.
- Its **tier** says what it assumes about the actual actor.

Every measurement-layer result assumes nothing about the actual actor: it is tier 1 or "—". The explanation
layer spans tiers 1–4. For example, Prop. [[Prop 20|20]] is tier 1 but explanatory, because it is about the evaluator's
error. Each item's layer is in its frontmatter, and `tools/vault.py lint` enforces two rules. No
measurement-layer statement or proof may use explanation vocabulary. And no measurement-layer item may depend
on an explanation-layer item.

**(E) results transfer to (E_A)** (R7-2, Prop. [[Prop 26|26]](a)). An actor that is entropic from its own reference
`q_A` is, behaviourally, entropic from the declared reference with error `E + log(q_A/q)/β`. So every (E)
result holds under (E_A) with that effective error. What (E_A) adds is only the *attribution* of part of the
error to the reference, and behaviour cannot confirm that attribution (Prop. [[Prop 26|26]](b)).

**Tier 1 includes the core's central identity.**
- For **any** actual actor, the regret in nats against the Gibbs intended actor at a declared price is
  `KL(p̂‖p*)`. It decomposes as in Thm [[Thm 13|13]], and it caps detectability (Prop. [[Prop 18|18]]).
- What does depend on the actor is **which engineering comparison is natural**. For best-of-n the natural
  resource is `n`, not KL. That comparison (Def. [[Def 14|14]]) needs the mechanism, so it is not a misalignment measure
  (Prop. [[Prop 25|25]]).

**Tier 2 does not hold for every optimizer.** R6 measured violations on 1,150 random instances:
- early-stopped vanilla policy gradient: 25.5 %;
- best-of-n compared at matched KL: 4.3 %;
- best-of-n compared at equal `n`: 0, which is Prop. [[Prop 23|23]];
- the Gibbs actor: 0.

The standing assumption S (finite `X`, full-support declared reference `q`) applies throughout, except where a result says
otherwise.

**Historical notes.** Cor. [[Cor 1.4|1.4]] and Remark [[Rem 7.1|7.1]] exist to explain what v5 found. Cor. [[Cor 1.2|1.2]] is used downstream
(Prop. [[Prop 7|7]]'s proof); only its last sentence is historical.

---


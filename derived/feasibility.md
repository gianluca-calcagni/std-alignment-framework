# Derived — feasibility

When the actor's limits are linear, misalignment splits exactly into what the actor could have avoided and what it
could not ([P15]). When the limit is a budget on how far the actor may depart from the default, the best it can do is
to pursue and stop where the budget runs out, and the budget acts as a price ([P27]); the width of the budget along a
function is how far the budget lets that function's average move ([P28]).

### P15 — Misalignment splits into what the actor could avoid and what it could not
**Statement.** Let `𝓕` be a convex feasible set ([D7]) that contains a full-support behaviour, and let `r ∈ Δ°`.
(i) **The best feasible behaviour.** Exactly one `p* ∈ 𝓕` minimizes `KL(p‖r)` over `𝓕`, and it has full support.
(ii) **Convex limits.** For every `p ∈ 𝓕`, `KL(p‖r) ≥ KL(p‖p*) + KL(p*‖r)`.
(iii) **Linear limits.** If `𝓕` is linear, with functions `f_1, …, f_m`, then `p* = tilt(r, Σ_i θ_i·f_i)` for some
numbers `θ_i`, and equality holds in (ii) for every `p ∈ 𝓕`.
(iv) **Value.** If `r = p_{F,t}` with `t > 0`, then `p*` is the unique maximizer over `𝓕` of the net value `J_t`
of [P4];
for every `p ∈ 𝓕`, `t·(J_t(p*) − J_t(p)) ≥ KL(p‖p*)`, with equality when `𝓕` is linear; and
`t·(J_t(p_{F,t}) − J_t(p*)) = KL(p*‖p_{F,t})`.
(v) **The split.** Under the standard specification of a non-constant `F`, let `𝓕` be linear, let `p̂ ∈ 𝓕` have a finite
revealed intensity `t*` with nearest intended behaviour `p° = p_{F,t*}` ([P5](iv)), and let `p*°` be the best feasible
behaviour for `r = p°`. Then `M(p̂) = KL(p̂‖p*°) + KL(p*°‖p°)`: the **avoidable misalignment** `KL(p̂‖p*°)`, plus the
**unavoidable misalignment** `KL(p*°‖p°)`.

**In plain terms.** Among the behaviours an actor can produce, exactly one comes closest to any given intended
behaviour. When the actor's limits take the form "these averages cannot change", how far the actor is from what was
intended splits exactly into two parts: how far it is from the best it could have done, and how far that best is from
what was intended. The first is what the actor would not do, and the second what it could not. In value, the first is
what the actor left unclaimed, and the second what no feasible behaviour reaches. For limits of other shapes the split
is
only an inequality, or fails.

**Proof.** (i) Since `r` has full support, `KL(·‖r)` is continuous on `Δ` and strictly convex. `𝓕` is closed in the
compact `Δ`, so a minimizer exists, and it is unique because `𝓕` is convex. Let `p̃ ∈ 𝓕` have full support, and
suppose `p*(x) = 0` for some `x`. Along `p_λ = (1 − λ)·p* + λ·p̃`, which stays in `𝓕`, the terms of `KL(p_λ‖r)` at the
outcomes where `p*` vanishes have derivative `−∞` as `λ → 0+` (the derivative of `u·log u` at `0`), while the other
terms have finite derivatives. So `KL(p_λ‖r) < KL(p*‖r)` for small `λ > 0`, a contradiction.
(ii) For `p ∈ 𝓕` the segment `p_λ = (1 − λ)·p* + λ·p` stays in `𝓕`, so the derivative of `KL(p_λ‖r)` at `λ = 0+` is
not negative. Since `p*` has full support and `Σ_x (p(x) − p*(x)) = 0`, that derivative is
`Σ_x (p(x) − p*(x))·log(p*(x)/r(x))`, so `E_p[log(p*/r)] ≥ KL(p*‖r)`. For every `p ∈ Δ`,
`KL(p‖r) − KL(p‖p*) = E_p[log(p*/r)]`, which gives (ii).
(iii) Near `p*`, which has full support, `𝓕` coincides with the affine set `{p : Σ_x p(x) = 1, E_p[f_i] = a_i}`, and
`p*` minimizes `KL(·‖r)` on it locally. So the derivative of `KL(·‖r)` at `p*` vanishes along every `v` with
`Σ_x v(x) = 0` and `Σ_x f_i(x)·v(x) = 0` for all `i`: `log(p*/r) + 1` is orthogonal to that subspace, hence in
`span{1, f_1, …, f_m}`, and `p* = tilt(r, Σ_i θ_i·f_i)`. Then for every `p ∈ 𝓕`,
`E_p[log(p*/r)] = Σ_i θ_i·a_i − log E_r[e^{Σ_i θ_i f_i}]`, the same number for every `p ∈ 𝓕`, so it equals its value at
`p*`, `KL(p*‖r)`, and the identity in the proof of (ii) holds with equality.
(iv) By [P4](i), `t·J_t(p) = log E_q[e^{tF}] − KL(p‖p_{F,t})` for every `p`. So maximizing `J_t` over `𝓕` is minimizing
`KL(·‖p_{F,t})` over `𝓕`, which (i) does at `p*` alone, and the two value differences are (ii), (iii) and the identity
at `p = p*`.
(v) By [P5](iv), `M(p̂) = KL(p̂‖p°)` with `p° ∈ Δ°`. Apply (iii) with `r = p°`.

**Checks.** checks/test_feasibility.py::test_linear_limits_split_exactly,
checks/test_feasibility.py::test_convex_limits_give_an_inequality,
checks/test_feasibility.py::test_curved_limits_can_break_the_split,
checks/test_feasibility.py::test_the_split_is_the_accounting_of_net_value,
checks/test_feasibility.py::test_misalignment_splits_into_avoidable_and_unavoidable,
checks/test_feasibility.py::test_contexts_and_coarse_actors_are_linear_limits,
checks/test_feasibility.py::test_a_random_environment_is_a_linear_limit

**Notes.** (ii) and (iii) are Csiszár's Pythagorean theorem for I-projections [@csiszar1975]; (iv) reads it as an exact
accounting of net value. Three limits met in practice are linear, and the checks confirm each.
- *Contexts*: situations whose frequencies the actor does not choose, `f = 1_C` for each group `C` of outcomes. The best
  feasible behaviour is pursuit within each context at one shared intensity, and the unavoidable part is
  `KL(q_𝒞‖(p_{F,t})_𝒞)`: how much the unconstrained pursuit would have reweighted the contexts.
- *An actor's resolution* ([D4]): `p(x)·q(y) − p(y)·q(x) = 0` for `x`, `y` in one cell. The best feasible behaviour is
  `tilt(q, t·F̄)`, the best effort of [P8](ii), and the unavoidable part is the Jensen gap of [P8](iii).
- *Acting in a random environment*: trajectory distributions with fixed transition probabilities. The best feasible
  behaviour is the maximum-entropy policy, computed backward with the expectation over the environment's moves. The
  unavoidable part is positive when the environment is random and zero when it is deterministic: the actor is not
  blamed for the dice.
A limit of capacity, such as a parametric family, is not convex; the third check shows a curved family on which even
(ii) fails. Then only `M(p̂) ≥ inf_{p∈𝓕} M(p)` remains.

**Lineage.** New. main: Def 23's feasibility slot, B1 and ROADMAP §6 G2 (retention), and the v8 design question on
contexts (`NOTES.md`), which (v) answers: across contexts, the shared intensity is derived, not chosen.

### P27 — The best use of a departure budget
**Statement.** Let `G` be non-constant, `A` the set of outcomes where `G` is largest, and `δ > 0`. The
**departure budget** `𝓑_δ = {p ∈ Δ : KL(p‖q) ≤ δ}` is a convex feasible set ([D7]) that contains `q`. Let
`λ_δ = inf{t ≥ 0 : KL(p_{G,t}‖q) ≥ δ}`, with `λ_δ = ∞` when the set is empty, which happens exactly when
`δ ≥ −log q(A)`; and `p_{G,∞} = q(·|A)`.
(i) For every `t > 0`, the net value `J_t` of `G` ([P4]) has exactly one maximizer over `𝓑_δ`,
`p* = p_{G, min(t, λ_δ)}`, and `J_t(p*) − J_t(p) ≥ KL(p‖p*)/min(t, λ_δ)` for every `p ∈ 𝓑_δ`, with equality when
`t ≤ λ_δ`. So `p*` is the best feasible behaviour of [P15](i) for `r = p_{G,t}`: the pursuit, cut off where the budget
runs out.
(ii) The largest average of `G` over `𝓑_δ` is reached at `p_{G,λ_δ}`, and only there when `δ ≤ −log q(A)`. When
`δ > −log q(A)`, it is `max G`, reached exactly by the behaviours on `A` within the budget, `q(·|A)` among them.
(iii) **The budget as a price.** `V(δ) = max_{p∈𝓑_δ} E_p[G]` is non-decreasing and concave in `δ`. For
`0 < δ < −log q(A)` it is differentiable, with `V'(δ) = 1/λ_δ`; for `δ ≥ −log q(A)`, `V(δ) = max G`.

**In plain terms.** Suppose the actor may depart from the default by at most a fixed amount. Then the best it can do,
for any objective and any price of departing, is to pursue the objective and stop where the budget runs out: either the
budget does not bind, or it fixes the intensity. The last unit of budget buys `1/λ_δ` units of the objective, so a
budget and a price are one quantity in two forms: a budget is spent exactly by pursuit at the intensity `λ_δ`.

**Proof.** Write `d(t) = KL(p_{G,t}‖q)`. By the proof of [P9](i), `d` increases continuously and strictly from `0`
toward `−log q(A)`, with `d'(t) = t·Var_{p_{G,t}}(G)`; so `λ_δ` is finite exactly when `δ < −log q(A)`, and then
`d(λ_δ) = δ`. (i) If `t ≤ λ_δ`, then `d(t) ≤ δ`, so `p_{G,t}` is in the budget, and [P4](i) gives
`J_t(p_{G,t}) − J_t(p) = KL(p‖p_{G,t})/t` for every `p`. If `t > λ_δ = λ`, then for `p ∈ 𝓑_δ`, [P4](i) at intensity
`λ` gives `E_p[G] − KL(p‖q)/λ = E_{p*}[G] − δ/λ − KL(p‖p*)/λ`, so
`J_t(p) = J_t(p*) − KL(p‖p*)/λ + (KL(p‖q) − δ)·(1/λ − 1/t) ≤ J_t(p*) − KL(p‖p*)/λ`, since `KL(p‖q) ≤ δ` and
`1/λ > 1/t`. In both cases the maximizer is unique. And since `J_t(p) = J_t(p_{G,t}) − KL(p‖p_{G,t})/t` for every `p`
([P4](i)), maximizing `J_t` over `𝓑_δ` is minimizing `KL(p‖p_{G,t})` over it. (ii) If `δ < −log q(A)`, the argument of
(i) with `1/t` replaced by `0` gives `E_{p*}[G] − E_p[G] ≥ KL(p‖p*)/λ_δ` for every `p ∈ 𝓑_δ`. Otherwise `q(·|A)` is in
the budget, since its departure is `−log q(A)`, and has the average `max G`; a behaviour reaches `max G` exactly when it
puts all its mass on `A`, and such a behaviour departs by `KL(p‖q) = −log q(A) + KL(p‖q(·|A))`, so at
`δ = −log q(A)` only `q(·|A)` fits. (iii) For `0 < δ < −log q(A)`, `V(δ) = m(λ_δ)` with `m(t) = E_{p_{G,t}}[G]`, and
`m'(t) = Var_{p_{G,t}}(G)` by [P13](i), since the revealed objective of the pursuit is `G` centred. By the inverse
function theorem, `V'(δ) = m'(λ_δ)/d'(λ_δ) = 1/λ_δ`. As `δ` grows, `λ_δ` grows, so `V'` falls; as `δ → −log q(A)`,
`λ_δ → ∞`, `V(δ) → max G` and `V'(δ) → 0`, which joins the constant `max G` beyond with a continuous, non-increasing,
non-negative derivative.

**Checks.** checks/test_feasibility.py::test_the_best_use_of_a_departure_budget

**Notes.** A departure budget is convex but not linear, so [P15](ii) gives only an inequality for it. It is called a
departure budget, not main's "capacity", because [D7] uses capacity for limits such as parametric families. Main's
capacity model, an actor that is the best budget-`δ` pursuit of its evaluator, is the case `G = F̂` of (ii). When its
budget binds, its matched pursuit ([D5]) is the best budget-`δ` pursuit of `F`, so main's capacity regret is the
shortfall of [D5], split into its causes by [P9](ii). (iii) makes the matched intensity of [D5] an exchange rate: at
the margin, `λ_δ` nats of departure buy one unit of the objective.

**Lineage.** main: Def 5 (the capacity actor), Lemma 5.1 (its form), Def 15 (the capacity model), Cor 5.2 (the exchange
rate is a shadow price) and Cor 17.1 (the capacity actor's regret); R076 (they assume nothing about the actor). New: the
budget as a feasible set of [D7], and its best behaviour as the one of [P15](i).

### P28 — The width of a departure budget
**Statement.** Let `E : X → ℝ` be non-constant, `δ > 0`, `𝓑_δ` the departure budget of [P27], and
`Λ(u) = log E_q[e^{u·(E − E_q[E])}]`. Let `σ_δ(E) = max_{p∈𝓑_δ} E_p[E] − E_q[E]`, how far the budget lets the average
of `E` rise. The **width** of the budget along `E` is `w_δ(E) = σ_δ(E) + σ_δ(−E)`.
(i) `σ_δ(E) = inf_{u>0} (δ + Λ(u))/u`, attained at `u = λ_δ(E)` when it is finite.
(ii) As `δ → 0`, `σ_δ(E) = √(2δ·Var_q(E)) + κ₃·δ/(3·Var_q(E)) + O(δ^{3/2})`, with `κ₃ = E_q[(E − E_q[E])³]`. So
`w_δ(E) = 2·√(2δ·Var_q(E)) + O(δ^{3/2})`.
(iii) `σ_δ(E) = max E − E_q[E]` once `δ ≥ −log q(argmax E)`, and `w_δ(E) = max E − min E` once `δ` also reaches
`−log q(argmin E)`.

**In plain terms.** A budget of departure lets the average of any function move only so far, up or down; the width is
the whole range it can move over. For a small budget the range is set by the function's spread under the default: about
twice the square root of twice the budget times the variance. A skewed function moves further toward its long tail, but
that shifts the range without widening it, to second order. A budget that reaches the best and the worst outcomes lets
the average move over the function's whole range.

**Proof.** Write `Ẽ = E − E_q[E]`. (i) For `u > 0`, [P4](i) for the objective `Ẽ` at intensity `u` says that no
behaviour has more net value than its pursuit, whose net value is `Λ(u)/u`; so for every `p ∈ 𝓑_δ`,
`E_p[Ẽ] ≤ (KL(p‖q) + Λ(u))/u ≤ (δ + Λ(u))/u`. By [P27](ii) with `G = E`, the maximum is reached at `p_{E,λ}`,
`λ = λ_δ(E)`, when `λ` is finite. There `KL(p_{E,λ}‖q) = δ` and `KL(p_{E,λ}‖q) = λ·E_{p_{E,λ}}[Ẽ] − Λ(λ)`, so the bound
at `u = λ` is an equality. When `λ = ∞`, the maximum is `max E − E_q[E]` ([P27](ii)), and `(δ + Λ(u))/u` tends to it
as `u → ∞`, because `Λ(u)/u` does. (ii) At `λ = λ_δ(E)`, `σ_δ(E) = E_{p_{E,λ}}[Ẽ] = Λ'(λ)` and
`δ = λ·Λ'(λ) − Λ(λ)`, with `λ → 0` as `δ → 0`. With `V = Var_q(E)`, `Λ(u) = V·u²/2 + κ₃·u³/6 + O(u⁴)`, so
`δ = V·λ²/2 + κ₃·λ³/3 + O(λ⁴)`, which inverts to `λ = √(2δ/V) − 2κ₃·δ/(3V²) + O(δ^{3/2})`. Then
`σ_δ(E) = V·λ + κ₃·λ²/2 + O(λ³) = √(2δV) + κ₃·δ/(3V) + O(δ^{3/2})`. For `−E`, `κ₃` changes sign and `V` does not, so
the terms in `δ` cancel in `w_δ(E)`. (iii) By [P27](ii), the largest average of `E` over the budget is `max E` once
`δ ≥ −log q(argmax E)`; applied to `−E`, the smallest is `min E` once `δ ≥ −log q(argmin E)`.

**Checks.** checks/test_feasibility.py::test_the_width_of_a_departure_budget

**Notes.** `σ_δ(E)` is the worst-case average of `E` over all behaviours within KL `δ` of the default, and (i) is its
dual form: the quantity robust optimization computes over a KL ambiguity set (`TERMS.md`, the width). The width is
unchanged by adding a constant to `E`, and multiplied by `c` when `E` is, for `c > 0`. It is the quantity the worst-case
results imported next are built on (`IMPORT.md`, N3 and N4).

**Lineage.** main: Def 6 (the width) and Prop 6 (the width, computed; its check V4). New: the term in `δ` of (ii), and
with it the symmetry of the width to that order.

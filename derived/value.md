# Derived — value

What the KL divergence measures: the net value lost against a pursuit ([P4]). And why the cost of departing from the
default is KL: it is the only cost for which pursuit, the steepest climb of [A2], is also the best trade-off of [A3]
([P14]). The identity of [P4] has a counterpart for any convex cost and any concave value, with a Bregman divergence in
place of KL ([P38]).

### P4 — What KL measures
**Statement.** Let `q ∈ Δ°`, `F : X → ℝ` and `t > 0`. The **net value** of `p ∈ Δ` is `J_t(p) = E_p[F] − KL(p‖q)/t`:
the average of the objective, minus the cost of departing from the default, priced at `1/t`.
(i) **Value.** For every `p ∈ Δ`, `J_t(p_{F,t}) − J_t(p) = KL(p‖p_{F,t})/t`. So `p_{F,t}` is the unique maximizer of
`J_t`.
(ii) **Every behaviour is an optimum.** For every `r ∈ Δ°`, `r = p_{G,1}` with `G = log(r/q)`. So `r` is the unique
maximizer of `J_1` for the objective `G`, and for every `p ∈ Δ` the net value `p` loses against `r` in that objective is
exactly `KL(p‖r)`.
(iii) **Chain rule.** For every partition `𝒢` of `X` into non-empty cells, every `p ∈ Δ` and every `r ∈ Δ°`,
`KL(p‖r) = KL(p_𝒢‖r_𝒢) + Σ_{C ∈ 𝒢, p(C) > 0} p(C)·KL(p(·|C)‖r(·|C))`, where `p_𝒢` is the distribution of the cell
masses `p(C)`.
(iv) **Merging never increases it.** `KL(p_𝒢‖r_𝒢) ≤ KL(p‖r)`, with equality if and only if `p/r` is constant on every
cell `C` with `p(C) > 0`.

**In plain terms.** Count the net value of a behaviour as the average of an objective minus the cost of moving away from
the default. Then the best behaviour is the pursuit of the objective, at the intensity set by the price of moving away,
and the KL from any behaviour to it is exactly the net value given up. Every full-support behaviour is the best one for
some objective, so this reading always applies. KL also splits into a part between groups and a part within groups when
outcomes are grouped, and grouping outcomes can only hide differences, never create them.

**Proof.** (i) With `Z = E_q[e^{tF}]`, `log p_{F,t} = log q + t·F − log Z`, so for every `p ∈ Δ`,
`KL(p‖p_{F,t}) = KL(p‖q) − t·E_p[F] + log Z = log Z − t·J_t(p)`. Hence `J_t(p) = (log Z − KL(p‖p_{F,t}))/t`. Taking the
difference at `p_{F,t}`, where the KL is `0`, and at `p` gives the identity. KL is non-negative, and zero only between
equal behaviours (Gibbs' inequality), so the maximizer is unique.
(ii) `p_{G,1} = tilt(q, log(r/q)) = r` by [P1](i). Then apply (i) with `t = 1`.
(iii) For `x ∈ C` with `p(x) > 0`, `log(p(x)/r(x)) = log(p(C)/r(C)) + log(p(x|C)/r(x|C))`. Averaging over `p` gives the
identity.
(iv) By (iii), the difference is `Σ_C p(C)·KL(p(·|C)‖r(·|C)) ≥ 0`. It is zero if and only if `p(·|C) = r(·|C)` on every
cell with `p(C) > 0`, that is, if and only if `p/r` is constant there.

**Checks.** checks/test_value.py::test_value_identity, checks/test_value.py::test_every_behaviour_is_an_optimum,
checks/test_value.py::test_chain_rule, checks/test_value.py::test_merging_never_increases,
checks/test_value.py::test_other_divergences_break_the_chain_rule

**Notes.** (i) is the Gibbs variational principle. The net value is the objective of KL-regularized RL fine-tuning, and
a free energy in the literature on bounded rationality [@ortega2013]. The same ray therefore arises twice: as the
steepest climb of [D2] and as the set of best behaviours at every price in (i). The chain rule and Gibbs' inequality are
standard [@cover2006]. Hobson characterized KL, up to a positive factor, by a small set of conditions that includes the
chain rule
(iii) [@hobson1969]. The last check confirms that three common alternatives (χ², squared Hellinger, total variation)
break it.

**Lineage.** v7.10: Thm 1 (regret is a divergence) for (i); Def 21 (the within-cell divergence) for (iii) and (iv). New:
(ii), which follows from [P1] and removes the need to assume that intended behaviour is "Gibbs", since every
full-support behaviour is. v7.10's Prop 15 (other regularizers) is not carried: the score is KL.

### P14 — The cost of departing from the default is forced
**Statement.** Let `q ∈ Δ°` and let `c : Δ° → ℝ` be differentiable. For every `F : X → ℝ` and every `t > 0`, the pursuit
`p_{F,t}` maximizes `E_p[F] − c(p)/t` over `Δ°` if and only if `c(p) = KL(p‖q) + C` for a constant `C`.

**In plain terms.** If pursuing an objective by the steepest route ([A2]) is also the best trade-off between the
objective and a cost of change ([A3]), then the cost of change can only be the KL divergence from the default. No other
cost makes the two agree.

**Proof.** Write `Dc(p)·v` for the derivative of `c` at `p` along a tangent vector `v`, one with `Σ_x v(x) = 0`. If
`c = KL(·‖q) + C`, then `E_p[F] − c(p)/t = J_t(p) − C/t`, which [P4](i) maximizes at `p_{F,t}`. Conversely, `p_{F,t}`
has full support, so it is an interior point of the plane `Σ_x p(x) = 1`, and at a maximizer the derivative along every
tangent `v` vanishes: `Σ_x t·F(x)·v(x) = Dc(p_{F,t})·v`. Since `log(p_{F,t}/q) = t·F − log E_q[e^{tF}]` and
`Σ_x v(x) = 0`, this says `Dc(p)·v = Σ_x log(p(x)/q(x))·v(x)` at `p = p_{F,t}`, and the right side is `D KL(·‖q)(p)·v`.
Every `p ∈ Δ°` is such a pursuit: `p = p_{G,1}` with `G = log(p/q)` ([P1](i)). So `h = c − KL(·‖q)` has zero derivative
along every tangent direction at every point of `Δ°`. `Δ°` is convex, so `h` is constant along every segment in it,
hence constant.

**Checks.** checks/test_value.py::test_the_cost_is_forced,
checks/test_value.py::test_a_function_of_kl_moves_only_the_intensity

**Notes.** [A2] says what pursuit is geometrically, and [A3] economically. [P2] shows that the first gives the
reweighting of [D2]; this result shows that the second agrees with it for exactly one cost. [A3] reads the intensity as
the reciprocal of the price of departure. Without that reading, asking only that the best trade-offs lie on the pursuit
ray at some intensity, any increasing function of KL would also do; the second check shows `KL + KL²`, whose best
trade-off at price `1/t` is the pursuit at intensity `t/(1 + 2·KL)`. The first check shows that χ², reverse KL and
squared Hellinger make no point of the ray a best trade-off, with three or more outcomes. Hobson reached KL from other
conditions [@hobson1969].

**Lineage.** v7.10: Def 2 (the bounded actor, with the KL cost assumed) and Thm 1. New: the cost is derived.

### P38 — Any convex cost
**Statement.** Let `t > 0`, and let `U` and `φ` be functions on `Δ` such that `Ψ = φ/t − U`, extended to the positive
functions on `X`, is convex. Let `p*` maximize `J = U − φ/t` over `Δ`, with `Ψ` differentiable at `p*`, and let
`B_Ψ(p, p*) = Ψ(p) − Ψ(p*) − ⟨∇Ψ(p*), p − p*⟩` be its Bregman divergence. Then for every `p ∈ Δ`,
`J(p*) − J(p) = B_Ψ(p, p*) − ⟨∇J(p*), p − p*⟩ ≥ B_Ψ(p, p*)`, with equality when `p*` has full support. In particular:
(i) for `U(p) = E_p[F]` and `φ = KL(·‖q)`, `B_Ψ(p, p*) = KL(p‖p*)/t`: this is [P4](i);
(ii) for `U(p) = E_p[F]` and `φ(p) = χ²(p‖q) = Σ_x (p(x) − q(x))²/q(x)`, `B_Ψ(p, p*) = Σ_x (p(x) − p*(x))²/(t·q(x))`,
and the best behaviour can rule outcomes out, where the identity becomes an inequality;
(iii) for `U(p) = E_p[F] − κ·(E_p[G])²` with `κ > 0`, a concave value that is not the average of any function, and
`φ = KL(·‖q)`, `B_Ψ(p, p*) = KL(p‖p*)/t + κ·(E_p[G] − E_{p*}[G])²`.

**In plain terms.** Whatever convex cost an actor pays for departing from its default, and whatever concave value it
seeks, every other behaviour gives up at least a divergence built from the cost, exactly that much when the actor's
best behaviour rules nothing out. KL is one such cost, and [P4] is the case. This result is about actors that pay other
costs: the measure of misalignment stays KL ([P14]).

**Proof.** `J = −Ψ`, so `J(p*) − J(p) = Ψ(p) − Ψ(p*) = B_Ψ(p, p*) + ⟨∇Ψ(p*), p − p*⟩`, and `∇Ψ(p*) = −∇J(p*)`. At a
maximum of the concave `J` over the convex `Δ`, `⟨∇J(p*), p − p*⟩ ≤ 0` for every `p ∈ Δ`, which gives the inequality.
If `p*` has full support, the first-order condition makes `∇J(p*)` constant on `X`, and `Σ_x (p − p*)(x) = 0`, so the
term vanishes. For (i)–(iii), the Bregman divergence of a sum is the sum of the Bregman divergences; that of a linear
function is `0`; that of `Σ_x p(x)·log(p(x)/q(x))` is `KL(p‖p*)` on behaviours; that of `Σ_x (p(x) − q(x))²/q(x)` is
`Σ_x (p(x) − p*(x))²/q(x)`; and that of `κ·(E_p[G])²` is `κ·(E_p[G] − E_{p*}[G])²`.

**Checks.** checks/test_value.py::test_any_convex_cost

**Notes.** The budgets of other shapes in [P31] are the hard-limit forms of such costs. (ii) shows why a `χ²` cost can
make an actor rule outcomes out entirely, which a KL cost never does.

**Lineage.** v7.10: Prop 15 (the identity for any convex regularizer).

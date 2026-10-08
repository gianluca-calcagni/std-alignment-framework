# Derived — estimation and evidence

What samples ([D11]) reveal about misalignment. The expected evidence per decision is a KL divergence, so misalignment
is the slowest rate at which evidence against the specification accumulates ([P21]); no test separates an actor from
its nearest intended behaviour faster ([P22]); the estimated misalignment of an actor that does pursue the objective has
a known distribution ([P23]); and an evaluation that weights conditions differently from deployment sees a different
misalignment, by a computable gap ([P24]). [P22] and [P23] rest on classical theorems, quoted with their hypotheses. A
strong incentive makes actors indistinguishable where it applies, which can make an evaluation see no misalignment
while use sees the actor's own ([P37]). What a sample certifies about an actor off the ray depends on what is known of
each draw: counted outcomes, log-ratios against the default, or log-ratios with draws of the default each give a normal
law with its own variance, and near the ray the second is far sharper ([P52]).

### P21 — The expected evidence is misalignment
**Statement.** Let `p, r ∈ Δ°`.
(i) For a sample from `p` ([D11]), the expected evidence per decision for `p` against `r` is `KL(p‖r)`.
(ii) Let `(q, 𝓘)` be a specification and `p̂ ∈ Δ°`. For a sample from `p̂`, the expected evidence per decision for `p̂`
against any intended behaviour is at least `M(p̂)`, with equality against a nearest intended behaviour ([P5](i)).

**In plain terms.** If the actor behaves as `p̂`, each decision gives, on average, at least `M(p̂)` nats of evidence
that it is not behaving as any intended behaviour, and exactly that much against the closest one. Misalignment is how
fast an observer can become sure that the actor is misaligned.

**Proof.** (i) The evidence of one decision is `log(p(x)/r(x))`, whose average under `p` is `KL(p‖r)`; the expectation
of a sum is the sum of the expectations. (ii) By (i), the expected evidence against `p ∈ 𝓘` is `KL(p̂‖p) ≥ M(p̂)`, and
[P5](i) gives an intended behaviour that attains `M(p̂)`.

**Checks.** checks/test_estimation.py::test_expected_evidence_is_misalignment

**Notes.** This is the second meaning of misalignment that [D11] announces: value lost ([A4]) and evidence gained
agree, in the same direction of KL. In a sequential test that stops when the evidence against the nearest intended
behaviour first exceeds `log(1/α)`, the expected number of decisions is about `log(1/α)/M(p̂)`, neglecting the overshoot
at the boundary [@wald1945]. The same identity compares explanations: for two proposed evaluators, the expected evidence
per decision for the pursuit that fits the actor against the one that does not is their KL divergence.

**Lineage.** v8: [D3]'s "what the number means", where this was an argument. New as a result.

### P22 — No test detects misalignment faster than misalignment
**Statement.** For `p̂, p ∈ Δ°` with `p̂ ≠ p`, let `C(p̂, p) = −min_{λ∈[0,1]} log Σ_x p̂(x)^λ·p(x)^{1−λ}`, the Chernoff
information.
(i) For samples of size `n` from `p̂` or from `p`, with equal prior probabilities, the smallest probability of error of
a test between the two is `e^{−n·C(p̂, p) + o(n)}` [@chernoff1952].
(ii) `C(p̂, p) ≤ min{KL(p̂‖p), KL(p‖p̂)}`.
(iii) Under a specification, for `p̂ ∈ Δ°` with a nearest intended behaviour `p° ≠ p̂`, `C(p̂, p°) ≤ M(p̂)`: no test
tells the actor from its nearest intended behaviour at an exponential rate above its misalignment.

**In plain terms.** Even an observer who knows exactly the actor's behaviour and the closest acceptable one cannot tell
them apart, from samples, faster than the misalignment allows. A small misalignment is, necessarily, hard to detect.

**Proof.** (i) is Chernoff's theorem for two simple hypotheses, with independent samples on a finite set
[@chernoff1952]; [@cover2006] gives a proof. (ii) For `λ ∈ [0, 1]`, Jensen's inequality gives
`−log Σ_x p̂^λ·p^{1−λ} = −log E_{p̂}[(p/p̂)^{1−λ}] ≤ (1 − λ)·KL(p̂‖p) ≤ KL(p̂‖p)`, and symmetrically
`−log E_p[(p̂/p)^λ] ≤ λ·KL(p‖p̂) ≤ KL(p‖p̂)`; the maximum over `λ` keeps both bounds. (iii) is (ii) with `p = p°`, since
`KL(p̂‖p°) = M(p̂)` ([P5](i)).

**Checks.** checks/test_estimation.py::test_detection_is_capped_by_misalignment

**Notes.** The bound in (ii) is attained in the limit of a nearly deterministic actor, but slowly: for an actor that
puts mass `ε` on each outcome other than its preferred one, the optimal `λ` and the relative gap `1 − C/KL` both shrink
only like `log log(1/ε)/log(1/ε)`. For typical behaviours the Chernoff information is well below either KL. The bound is
one-sided: a large misalignment does not guarantee easy detection when the observer does not know the nearest intended
behaviour.

**Lineage.** v7.10: Prop 18 (harm bounds detectability), proved there against the Gibbs intended behaviour.

### P23 — The estimated misalignment of an actor that pursues the objective
**Statement.** Let `F` be non-constant, `|X| ≥ 3`, and let the actor pursue `F` from `q` at an intensity `t > 0`, so
that its behaviour is `p_{F,t}`. Let `p̂_n` be the empirical behaviour of a sample of size `n` from it, and `M` the
misalignment under the standard specification of `F`. Then, as `n → ∞`, `2n·M(p̂_n)` converges in distribution to a χ²
distribution with `|X| − 2` degrees of freedom.

**In plain terms.** Even an actor that pursues the objective exactly shows some misalignment in a finite record, by
chance. How much is known: twice the number of decisions times the estimated misalignment follows, approximately, a
chi-squared law with two fewer degrees of freedom than there are outcomes. An estimate well above that law's range is
evidence of real misalignment.

**Proof.** `n·M(p̂_n) = n·min_{s≥0} KL(p̂_n‖p_{F,s})` is the logarithm of the ratio between the largest likelihood of
the sample over all behaviours, reached at `p̂_n`, and over the pursuit ray. The ray is a smooth one-parameter family
inside the `(|X| − 1)`-parameter family of all full-support behaviours, and the true intensity `t > 0` is an interior
point of the half-line `s ≥ 0`. Wilks's theorem then gives the χ² limit with `(|X| − 1) − 1 = |X| − 2` degrees of
freedom [@wilks1938].

**Checks.** checks/test_estimation.py::test_estimated_misalignment_is_chi_squared

**Notes.** At `t = 0`, the true intensity is on the boundary of the half-line and the limit is a mixture of χ²
distributions (chi-bar-square), not covered here. The check is a light simulation (300 samples of size 2000, for three
and five outcomes), which compares the mean with `|X| − 2`.

**Lineage.** v8: the deviance of [P5]'s Notes. New as a result (`NOTES.md` E1).

### P24 — The evaluation gap
**Statement.** Let the actor face finitely many conditions ([D8]); in each condition `c`, let `(q_c, 𝓘_c)` be a
specification under which its behaviour `p_c ∈ Δ°` has misalignment `M_c`. For condition frequencies `ρ`, take as
outcomes the condition–outcome pairs, as the actor's behaviour `ρ(c)·p_c(x)`, and as the specification the default
`ρ(c)·q_c(x)` with the intended behaviours `ρ(c)·p'_c(x)`, `p'_c ∈ 𝓘_c` in each condition. Let `ρ_ev` and `ρ_dep` be the
frequencies when the actor is evaluated and when it is deployed.
(i) The misalignment on pairs at frequencies `ρ` is `Σ_c ρ(c)·M_c`. For a sample of pairs drawn at `ρ_ev`, the expected
evidence per decision against the nearest intended behaviour is therefore `Σ_c ρ_ev(c)·M_c` ([P21](ii)).
(ii) The misalignment in deployment exceeds the misalignment in evaluation by the **evaluation gap**
`Γ = Σ_c (ρ_dep(c) − ρ_ev(c))·M_c`.

**In plain terms.** An evaluation that meets the situations of real use in other proportions than real use does
measures a different misalignment. When the principal judges each situation on its own terms, the difference is
computable: it weighs each situation's misalignment by how much more often real use meets it than the evaluation does.

**Proof.** (i) For pairs, `log(ρ(c)·p_c(x)/(ρ(c)·p'_c(x))) = log(p_c(x)/p'_c(x))`: the frequencies cancel, so
`KL(ρ·p‖ρ·p') = Σ_c ρ(c)·KL(p_c‖p'_c)`. The intended behaviours are chosen condition by condition, so the infimum of the
sum is the sum of the infima, `Σ_c ρ(c)·M_c`. The intended set is closed in `Δ°` because each `𝓘_c` is, so this is a
specification ([D3]), and [P21](ii) gives the evidence. (ii) is the difference of (i) at `ρ_dep` and at `ρ_ev`.

**Checks.** checks/test_estimation.py::test_the_evaluation_gap

**Notes.** The specification here judges each condition on its own terms, which makes misalignment linear in the
frequencies. A principal who asks instead for pursuit of `F` in every condition at one shared intensity declares a set
that is not chosen condition by condition. Its misalignment at frequencies `ρ` is
`min_{t≥0} Σ_c ρ(c)·KL(p_c‖p_{c,F,t})`, with `p_{c,F,t}` the pursuit in condition `c`: at least `Σ_c ρ(c)·M_c`, and
concave in `ρ`, since the nearest intensity moves with the frequencies. Then `Γ` does not give the gap, which is the
difference of the two misalignments, computed directly. In either case, the evaluation gap comes from the weights of the
conditions, while the behaviour in each stays the same. [P17] covers the other case: the behaviour itself differs in
conditions that are not observed, by as much as the actor's view allows. A report needs both.

**Lineage.** v7.10: Def 9 (contexts, with evaluation and deployment frequencies) and Prop 19 (the evaluation gap).

### P37 — A strong incentive masks the actor, and can fake alignment
**Statement.** Let `u` be an intervention ([D6]) with a unique outcome `x_u` of largest value, `d(x) = u(x_u) − u(x)`,
and `γ = min_{x≠x_u} d(x) > 0`. An actor whose behaviour is `p` passes it through with pass-through `φ` when its
behaviour becomes `p^φ = tilt(p, φ·u)`.
(i) **Masking.** For two actors with behaviours `p_1, p_2 ∈ Δ°`, let `a_i(x) = p_i(x)/p_i(x_u)` and
`c(x) = a_1(x)·log(a_1(x)/a_2(x)) − a_1(x) + a_2(x) ≥ 0`. As `φ → ∞`,
`KL(p_1^φ‖p_2^φ) = Σ_{x≠x_u} c(x)·e^{−φ·d(x)} + O(e^{−2φγ})`. So the divergence vanishes like `e^{−φγ}`, and the
Chernoff information between the two actors, the best error exponent of any test between them, at least as fast
([P22](ii)); and `(1/φ)·log KL(p_1^φ‖p_2^φ) → −γ` when `c > 0` at some outcome with `d = γ`.
(ii) **Fake alignment.** In a condition where `u` and the objective `F` have the same unique best outcome, the
misalignment of `p^φ` under the standard specification of `F` tends to `0` as `φ → ∞`. So if an actor faces `u` only
in the conditions where it is evaluated, judged as in [P24], its misalignment in evaluation can be made as small as
one likes by a strong enough incentive, while in the conditions of use, where it faces no incentive, its misalignment
is that of its own behaviour, and the evaluation gap tends to the whole misalignment in use.
(iii) **Reward hacking shows.** In a condition where the unique best outcome `x_u` of `u` is not among the best
outcomes of `F`, the misalignment of `p^φ` tends to `−log sup_{t≥0} p_{F,t}(x_u) > 0`.

**In plain terms.** A strong enough incentive makes every actor behave almost alike: two actors with different aims
become indistinguishable by any test, exponentially fast as the incentive grows. Where the incentive points at what the
principal wants, every actor looks aligned under evaluation, whatever it does where it is not evaluated: alignment can
be faked by incentives at evaluation time alone. Where the incentive points elsewhere, the misalignment it causes shows,
and stays.

**Proof.** (i) For `x ≠ x_u`, `p_i^φ(x) = a_i(x)·e^{−φ·d(x)}/(1 + S_i)` and `p_i^φ(x_u) = 1/(1 + S_i)`, with
`S_i = Σ_{y≠x_u} a_i(y)·e^{−φ·d(y)} = O(e^{−φγ})`. Write `KL(p_1^φ‖p_2^φ)` as the sum over `x` of
`p_1^φ·log(p_1^φ/p_2^φ) − p_1^φ + p_2^φ`, the added terms summing to zero. For `x ≠ x_u` the term is
`e^{−φ·d(x)}·(c(x) + O(S_1 + S_2))`, and at `x_u` it is of order `(S_1 − S_2)²`. Since
`Σ_{x≠x_u} e^{−φ·d(x)} = O(e^{−φγ})`, the corrections are `O(e^{−2φγ})`. By [P22](ii) the Chernoff information is at
most the divergence. (ii) Let `x*` be the shared best outcome. For every `t ≥ 0`, `M(p^φ) ≤ KL(p^φ‖p_{F,t})`, and
`KL(p^φ‖p_{F,t}) ≤ −log p_{F,t}(x*) + Σ_{x≠x*} p^φ(x)·(log(1/q(x)) + t·(max F − min F))`, using `log p^φ ≤ 0` and
`p_{F,t}(x) ≥ q(x)·e^{−t·(max F − min F)}`. With `t = φ^{1/2}`, the first term tends to `0`, since `x*` is the unique
best outcome of `F`, and the sum tends to `0`, since `p^φ(x) = O(e^{−φγ})` for `x ≠ x*`. In the conditions without the
incentive the behaviour, and so its misalignment, does not depend on `φ`; [P24] gives the gap. (iii) `p^φ` tends to the
point mass at `x_u`. For each `t`, `KL(p^φ‖p_{F,t}) → −log p_{F,t}(x_u)`, which bounds the limit superior of the
misalignment by `inf_t (−log p_{F,t}(x_u))`. Conversely, grouping into `{x_u}` and its complement ([P4](iv)) gives
`KL(p^φ‖p_{F,t}) ≥ −p^φ(x_u)·log p_{F,t}(x_u) − h(p^φ(x_u))`, with `h` the entropy of a coin, which gives the matching
lower bound as `p^φ(x_u) → 1`. The limit is positive: `p_{F,t}(x_u) < 1` for every `t` and tends to `0` as `t → ∞`,
since `x_u` is not a best outcome of `F`, so its supremum is below `1`.

**Checks.** checks/test_estimation.py::test_a_strong_incentive_masks_the_actor_and_can_fake_alignment

**Notes.** The archive derived these for an agent that values reward through a continuation value (its hypothesis
`E_R`); here the incentive enters only through the observed pass-through of [D6], so no model of the agent's stake in
the reward is needed. [P17] bounds the other route to the same gap: a behaviour that differs in conditions the actor can
tell apart. Evaluations with strong incentives that point where the principal's objective does are therefore weak
evidence of alignment in use; an incentive that points elsewhere makes misalignment show instead ((iii)).

**Lineage.** v7.10: Prop 28 (incentive masking) and Prop 30 (the fake-alignment gap), without the reward coupling of
Def 16. New: the leading form in (i) as a statement, and the derivation from pass-through alone.

### P52 — What a sample certifies about misalignment, by access
**Statement.** Under the standard specification of a non-constant `F`, let `p ∈ Δ°` have revealed intensity `0 < t* < ∞`
and nearest intended behaviour `p° = p_{F,t*}` ([P5](iv)), and let `w = p°/p` and `M = M(p) = KL(p‖p°)`. Draws are
independent; `x_1, …, x_n` are draws of `p`, and bars denote averages over them.
(i) **Counts.** With `q` and `F` known, let `p̂_n` be the empirical behaviour of the draws and `t̂_n` its revealed
intensity. As `n → ∞`, `√n·(M(p̂_n) − M)` converges in distribution to a normal law with mean `0` and variance
`Var_p(log w)`, and `√n·(t̂_n − t*)` to one with mean `0` and variance `Var_p(F)/Var_{p°}(F)²`.
(ii) **Log-ratios.** With only `ℓ_i = log(p(x_i)/q(x_i))` and `F_i = F(x_i)` known for each draw, let
`M̂_n = min_{s≥0} [ℓ̄ − s·F̄ + log((1/n)·Σ_i e^{s·F_i − ℓ_i})]`. Then `M̂_n ≥ 0`, with equality if and only if, for some
`s ≥ 0`, `ℓ_i − s·F_i` is the same for every draw; so `M̂_n = 0` for every sample of an actor on the ray. As `n → ∞`,
`√n·(M̂_n − M)` converges to a normal law with mean `0` and variance `Var_p(w − log w)`.
(iii) **Two samples.** With, besides (ii), `m` draws `y_1, …, y_m` of `q` and their `F(y_j)`, let
`M̃ = min_{s≥0} [ℓ̄ − s·F̄ + log((1/m)·Σ_j e^{s·F(y_j)})]`. As `n, m → ∞` with `m/n` fixed, `(M̃ − M)/σ` converges to
the standard normal law, with `σ² = Var_p(log w)/n + χ²(p°‖q)/m`. This holds on the ray too, where `M = 0` and `M̃` is
negative with probability tending to one half.

**In plain terms.** How sharply a record pins down misalignment depends on what the observer can compute, not only on
how much is recorded. Counting outcomes, the error shrinks like one over the square root of the number of draws, as for
any average. Knowing how much more likely the actor made each draw than the default would have, as for a language model
scored by both policies, the estimate is never negative, is exactly zero for an actor that pursues the objective, and is
far sharper near it; but it reweights the actor's own draws, which costs samples once the actor is far from its nearest
intended behaviour, and then counting does better. With draws of the default as well, the estimate can be negative, and
its noise does not vanish even for an actor that does pursue the objective: it grows with how far that pursuit has moved
from the default.

**Proof.** Let `A(s) = log E_q[e^{s·F}]`, so that `A'(s) = E_{p_{F,s}}[F]`, `A''(s) = Var_{p_{F,s}}(F) > 0`, and, with
`ℓ = log(p/q)`, `log w = t*·F − A(t*) − ℓ`. Each estimate is `min_{s≥0} Ψ(r̂, s)`, where `r̂` is the empirical behaviour
of the draws and `Ψ` is smooth in both arguments: in (i), `Ψ(r, s) = KL(r‖p_{F,s})`; in (ii),
`Ψ(r, s) = Σ_x r(x)·(ℓ(x) − s·F(x)) + log Σ_x r(x)·e^{s·F(x) − ℓ(x)}`; in (iii), with `r = (r_p, r_q)` the two empirical
behaviours, `Ψ(r, s) = Σ_x r_p(x)·(ℓ(x) − s·F(x)) + log Σ_x r_q(x)·e^{s·F(x)}`. At the true behaviours, all three equal
`KL(p‖p_{F,s})`, since `E_p[e^{s·F − ℓ}] = E_q[e^{s·F}] = e^{A(s)}`: strictly convex in `s`, with second derivative
`A''(s)`, and minimized at `t* > 0` with the value `M`. By the implicit function theorem the minimizer is a smooth
function of `r` near the true behaviours, and interior to `s ≥ 0`; so with probability tending to one the estimate is
`Ψ` at `r̂` and at that minimizer. By the envelope theorem, its derivative along a change `h` of `r`, with
`Σ_x h(x) = 0` in each sample, is that of `Ψ(·, t*)`:
- in (i), `Σ_x h(x)·(log(p(x)/p°(x)) + 1) = −Σ_x h(x)·log w(x)`;
- in (ii), `Σ_x h(x)·(ℓ(x) − t*·F(x) + e^{t*·F(x) − ℓ(x) − A(t*)}) = Σ_x h(x)·(w(x) − log w(x))`, since
  `e^{t*·F − ℓ − A(t*)} = p°/p = w` and constants drop;
- in (iii), `−Σ_x h_p(x)·log w(x) + Σ_x h_q(x)·p°(x)/q(x)`, by the same identities.
By the central limit theorem, `√n·(r̂ − r)` converges to a normal law with covariance `diag(r) − r·rᵀ`, independently
for the two samples of (iii); the delta method gives normal limits with the variances `Var_p(log w)`,
`Var_p(w − log w)`, and `Var_p(log w)/n + Var_q(p°/q)/m`, where `Var_q(p°/q) = χ²(p°‖q)`. In (i), with probability
tending to one, `t̂_n = (A')^{−1}(E_{p̂_n}[F])` ([P5](iv)), and the delta method, with `√n·(E_{p̂_n}[F] − E_p[F])` of
limit variance `Var_p(F)` and the derivative `1/A''(t*) = 1/Var_{p°}(F)`, gives its law. In (ii), by Jensen's
inequality, `log Σ_x r̂(x)·e^{s·F(x) − ℓ(x)} ≥ Σ_x r̂(x)·(s·F(x) − ℓ(x))`, so `Ψ(r̂, s) ≥ 0`, with equality exactly when
`s·F − ℓ` is constant on the outcomes drawn. `Ψ(r̂, ·)` is constant when every outcome drawn has the same `F`, and grows
without bound as `s → ∞` otherwise, so its minimum over `s ≥ 0` is attained, and is `0` exactly when such an `s ≥ 0`
exists. On the ray, `ℓ = t*·F − A(t*)`. In (iii), on the ray `log w = 0`, and the limit is the reference's term alone, a
normal law centred at `0`.

**Checks.** checks/test_estimation.py::test_what_a_sample_certifies_by_access

**Notes.** *How the regimes compare.* Counting, and the actor's half of (iii), carry `Var_p(log w)`, about `2M` near the
ray. Knowing the log-ratios replaces it by `Var_p(w − log w)`: near the ray `w − log w = 1 + (w − 1)²/2 + O((w − 1)³)`,
so the variance is of the order of `M²` rather than `M`, and the relative error of order `1/√n` rather than `1/√(n·M)`.
In five instances near the ray (`probes/diagnostics/probe_access.py`) it is 4.5 to 24 times smaller than by counting.
Far from the ray the order reverses, since `Var_p(w) = χ²(p°‖p) ≥ e^{KL(p°‖p)} − 1` ([P47](i)) measures a reweighting of
the actor's draws towards its nearest intended behaviour. In the probe's survey of 4,000 random actors, the log-ratios
gave the smaller variance for 84% of those with `M` below `0.01` nats, 45% between `0.1` and `0.3`, and 14% above `1`;
by the reweighting, for 86% of those with `χ²(p°‖p)` below `0.5`, and 5% above `2`. So an actor far from its nearest
intended behaviour is better estimated with draws of the default as well, as in (iii); both variances are estimable from
the draws, and which estimate a case reports is declared before. At a known `t*`, the estimate of (ii) is
`log((1/n)·Σ_i w_i) − (1/n)·Σ_i log w_i`, which agrees to first order with `(1/n)·Σ_i (w_i − 1 − log w_i)`, the
control-variate estimator of KL with coefficient `1`, Schulman's; Amini, Vieira and Cotterell show that it can have
enormous variance, larger than the plain average's when the best coefficient is below one half [@amini2025]. Here the
coefficient is not chosen. With log-ratios alone, each `w_i = e^{t*·F_i − ℓ_i − A(t*)}` is known only up to the common
factor `e^{−A(t*)}`, and an estimate built from the averages of `log w_i` and of `w_i` that does not change when every
`w_i` is multiplied by one constant is a function of `log((1/n)·Σ_i w_i) − (1/n)·Σ_i log w_i`: to first order, its
coefficient is `1`. The plain average, `ℓ̄ − t̂·F̄ + A(t̂)`, needs `A`, that is, the default's draws or its full
distribution, as in (iii) and (i). For outcomes generated step by step, as text is, with each step's distribution known
in full, the departure `KL(p‖q)` is estimated more sharply by averaging each step's exact divergence along the draws,
their Rao–Blackwellized estimator [@amini2025]; the normalizer of a pursuit of an objective on whole outcomes is not.
*Intervals.* Each variance is an average, under `p` or `q`, of a function of `w`, and its plug-in at the estimated
intensity is consistent; so the estimate plus or minus `1.96` estimated standard errors is an interval of asymptotic
level `95%` wherever the variance is positive. On the ray, (i) has variance `0` and [P23] gives its law at the scale
`1/n`; the estimate of (ii) is `0` exactly; the interval of (iii) stays valid, and a negative estimate there is noise,
not an error. The laws are asymptotic: they say nothing of the bias of the self-normalized averages at a few draws. Case
W3, in regime (iii) with 32 draws of the reference per prompt, reported its split as an order of magnitude for that
reason.
*Imports.* (i) is the corollary to Theorem 3 of Huber [@huber1967], read in its scan, for `ψ(x, s) = F(x) − A'(s)`:
`λ(s) = E_p[F] − A'(s)`, `Λ = −Var_{p°}(F)`, and `C = Var_p(F)`, with `p` not assumed to lie on the ray; its covariance
`Λ^{−1}·C·Λ^{−1}` is the sandwich that White's theorem gives for misspecified likelihoods [@white1982], known here from
its record. The dichotomy of (i), a normal law at the scale `1/√n` off the ray and [P23]'s χ² law at the scale `1/n` on
it, is the one Vuong's abstract states for likelihood-ratio tests between models [@vuong1989]; read only in its
abstract, it is not used.
*Beyond finite outcomes.* The estimates of (ii) and (iii) are functions of a few averages, so their laws should carry
over to general spaces under conditions on moments and on the minimizer, such as Huber's; not derived here. Among them,
`E_p[w²]` and `E_q[(p°/q)²]` must be finite, χ² divergences that can be infinite when the KL divergences are finite:
existence becomes conditional (`general/dictionary.md`, finding 5). (i) has no analogue, since counting fails on a
continuum (GD11).

**Lineage.** New. (i) specializes Huber's corollary; (ii) and (iii) are new as results here, from the access regimes of
`general/dictionary.md` (finding 7).

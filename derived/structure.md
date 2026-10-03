# Derived — structure

Some specifications are defined by a structure rather than by an objective: several actors meant to act independently,
behaviour meant to ignore the situation, a process meant to look the same run backward. Misalignment against each is a
divergence with a name: the coordination of the actors ([P39]), the attention of the response ([P40]), and the
Jensen–Shannon divergence between a record of transitions and its reversal ([P41]). Several principals, each declaring
a pursuit from one default, are all satisfied by doing nothing, and when each names an intensity their best compromise
is a single pursuit ([P42]). Every outcome set here is finite: joint outcomes, condition–outcome pairs, or transitions.

### P39 — Several actors: coordination plus individual misalignment
**Statement.** Let actors `i = 1, …, k`, with `k ≥ 2`, have finite outcome sets `X_i`, and take as outcomes the joint
outcomes `X = X_1 × … × X_k`. For `p ∈ Δ(X)` let `p_i` be its marginal on `X_i`, and write `⊗_i r_i` for the product of
behaviours `r_i` on the `X_i`. The **coordination** of `p` is `K(p) = KL(p‖⊗_i p_i)`. Let `(q_i, 𝓘_i)` be
specifications for the actors one by one, with misalignments `M_i`, and take on `X` the **independent pursuit**
specification: the default `⊗_i q_i`, and as intended behaviours the products `⊗_i r_i` with `r_i ∈ 𝓘_i`.
(i) For every `p ∈ Δ(X)` and all `r_i ∈ Δ°(X_i)`, `KL(p‖⊗_i r_i) = K(p) + Σ_i KL(p_i‖r_i)`.
(ii) Independent pursuit is a specification ([D3]), and under it `M(p) = K(p) + Σ_i M_i(p_i)`. `K(p) ≥ 0`, with
equality exactly when `p` is the product of its marginals.
(iii) Coordination depends on what counts as one outcome: there is a behaviour of two actors over two rounds whose
coordination is `0` in each round and `2·log 2` on the two rounds taken together.

**In plain terms.** When the principal wants several actors each to pursue its own objective on its own, their joint
misalignment is the sum of their own misalignments plus one more term that no single actor's record shows: how much
their outcomes go together, their coordination. Coordination can hide in time. Two actors can look independent in
every round and still be tightly coordinated across rounds.

**Proof.** (i) Where `p(x) > 0`, every `p_i(x_i) > 0`, and
`log(p(x)/Π_i r_i(x_i)) = log(p(x)/Π_i p_i(x_i)) + Σ_i log(p_i(x_i)/r_i(x_i))`. Averaging under `p`, each last term
gives `KL(p_i‖r_i)`, since `x_i` has the distribution `p_i` under `p`.
(ii) The default and every `⊗_i r_i` with `r_i ∈ Δ°(X_i)` have full support. The intended set is closed in `Δ°(X)`: if
`⊗_i r_i^{(n)} → s ∈ Δ°(X)`, the marginals converge, `r_i^{(n)} → s_i`, with `s_i ∈ 𝓘_i` because each `𝓘_i` is closed
in `Δ°(X_i)`, and `s = ⊗_i s_i` by continuity. So [D3] holds. By (i), the infimum over products splits into one
infimum per actor, which is `M_i(p_i)`. `K(p)` is a divergence, zero exactly when `p = ⊗_i p_i`.
(iii) Draw two fair coins `z_1` and `z_2` independently; actor 1 plays `z_1` then `z_2`, and actor 2 plays `z_2` then
`z_1`. In each round the two plays are independent fair coins, so the coordination is `0`. On the two rounds each actor's
outcome is uniform on four values, and so is the joint outcome, so `K = log 4 + log 4 − log 4 = 2·log 2`.

**Checks.** checks/test_structure.py::test_coordination_splits_misalignment,
checks/test_structure.py::test_coordination_can_hide_in_time

**Notes.** Coordination is the total correlation of the actors' outcomes, the mutual information when there are two.
With finitely many joint outcomes, several actors are one actor on joint outcomes (`CORE.md` §0); coordination is what
that reading adds to the actors' own misalignments. Pricing algorithms that learn to sustain high prices across rounds
[@calvano2020] are the case of (iii): a regulator reading one round's table sees independent firms. Two tit-for-tat
players with 5% errors show `0` in every round and `0.231` nats per round over long records (`probes/general/`, T3).

**Lineage.** New. `CORE-GENERAL.md`, draft 2, independence as a structural specification; `NOTES.md` §5.4, H11.

### P40 — Attention: misalignment against ignoring the situation
**Statement.** Let the actor face finitely many conditions ([D8]) with frequencies `ρ ∈ Δ°(𝒞)`, and let its response
`(p_c)` have every `p_c ∈ Δ°`. Take as outcomes the condition–outcome pairs, as behaviour `ρ(c)·p_c(x)`, as default
`ρ(c)·q(x)` for a declared `q ∈ Δ°`, and as intended behaviours the responses that are the same in every condition,
`ρ(c)·r(x)` with `r ∈ Δ°`. Let `p̄ = Σ_c ρ(c)·p_c`.
(i) For every `r ∈ Δ°`, `Σ_c ρ(c)·KL(p_c‖r) = Σ_c ρ(c)·KL(p_c‖p̄) + KL(p̄‖r)`.
(ii) The misalignment is `Σ_c ρ(c)·KL(p_c‖p̄)`, attained at `r = p̄` alone: the **attention** of the response, the
mutual information between condition and outcome under the pair behaviour.
(iii) Attention is `0` exactly when the response is the same in every condition.

**In plain terms.** Measured against "act the same whatever the situation", an actor's misalignment is how much its
behaviour depends on the situation: its attention, the mutual information between situation and outcome. Theories of
rational inattention charge an actor for exactly this quantity; here it is measured, not charged.

**Proof.** (i) For each `c`, `KL(p_c‖r) − KL(p_c‖p̄) = E_{p_c}[log(p̄/r)]`; averaging over `c` with weights `ρ(c)` gives
`E_{p̄}[log(p̄/r)] = KL(p̄‖r)`.
(ii) For pairs, `log(ρ(c)·p_c(x)/(ρ(c)·r(x))) = log(p_c(x)/r(x))`, so the divergence of the pair behaviour from an
intended one is `Σ_c ρ(c)·KL(p_c‖r)`, as in [P24](i). By (i) its infimum over `r` is attained at `r = p̄`, which has
full support, and only there. The intended set is closed in `Δ°` of the pairs: if `ρ(c)·r_n(x) → s(c, x)` with `s` of
full support, then `r_n` converges to the outcome marginal of `s`, which is in `Δ°`, and `s` is `ρ` times it. So
[D3] holds. The value is the mutual information between condition and outcome, since `p̄` is the outcome marginal.
(iii) A divergence is `0` exactly at equality, so every `p_c = p̄`.

**Checks.** checks/test_structure.py::test_attention_is_mutual_information

**Notes.** Rational inattention [@matejka2015] charges an information cost of this form, and the actor then chooses its
own default, `p̄`; on a continuum the chosen default can be discrete (`general/derived-spaces.md`). (i) is Csiszár's
Pythagorean identity for a mixture: the average of the behaviours is the nearest behaviour to all of them at once.

**Lineage.** New. `NOTES.md` §5.4, H21; probe B7 (`probes/general/`).

### P41 — Reversibility: the Jensen–Shannon divergence from the reversal
**Statement.** Let `S` be a finite set of states, and take as outcomes the transitions, the ordered pairs
`(x, y) ∈ S × S`. The **reversal** of a behaviour `F` on transitions is `F^T(x, y) = F(y, x)`, and `F` is
**reversible** if `F = F^T`. Take a reversible default in `Δ°(S × S)`, and as intended behaviours the reversible ones in
`Δ°(S × S)`. For `F ∈ Δ(S × S)` let `m = (F + F^T)/2`, and let its **entropy production** be `e(F) = KL(F‖F^T)`.
(i) `M(F) = KL(F‖m) = ½·KL(F‖m) + ½·KL(F^T‖m)`, the Jensen–Shannon divergence between `F` and its reversal. The
infimum is attained at `m` when `m` has full support, and approached otherwise.
(ii) `M(F) ≤ e(F)/2`.
(iii) If `F_s = m + s·A`, with `m ∈ Δ°(S × S)` reversible and `A ≠ 0` with `A^T = −A`, then `M(F_s)/e(F_s) → 1/4` as
`s → 0`.
(iv) Let `P` be the transition matrix of a Markov chain on `S` with a stationary distribution `π` of full support, and
`F(x, y) = π(x)·P(x, y)`. Among the transition matrices `R` that are reversible with respect to some distribution and
positive wherever `P` is, the smallest value of `Σ_x π(x)·KL(P(x,·)‖R(x,·))` is `M(F)`, attained at
`R(x, y) = m(x, y)/π(x)` alone.

**In plain terms.** Record transitions and compare the film run forward with the film run backward. If they look
alike, the process is reversible. Measured against reversibility, misalignment is the Jensen–Shannon divergence between
the two films: at most half of the entropy production, the plain divergence from the backward film, and a quarter of it
when the asymmetry is small. For a Markov chain, the nearest reversible chain runs each transition as often as the two
films do on average.

**Proof.** (i) For a reversible `W`, `Σ F·log W = Σ F^T·log W = Σ m·log W`, so `KL(F‖W) = Σ F·log F − Σ m·log W`.
This holds for `W = m`, which is reversible, so `KL(F‖W) − KL(F‖m) = Σ m·log(m/W) = KL(m‖W) ≥ 0`, with equality exactly
at `W = m`. If `m` has zeros, the reversible behaviours `(1 − ε)·m + ε·u`, with `u` uniform, have full support, and
`KL(F‖·)` at them tends to `KL(F‖m)` as `ε → 0`, because `m > 0` wherever `F > 0`. And
`KL(F^T‖m) = KL(F‖m^T) = KL(F‖m)`. The reversible behaviours of full support form a closed set in `Δ°(S × S)`, so this
is a specification ([D3]).
(ii) KL is convex in its second argument, so `KL(F‖m) ≤ ½·KL(F‖F) + ½·KL(F‖F^T) = e(F)/2`.
(iii) `F_s^T = m − s·A`. Second-order expansions give `KL(F_s‖m) = (s²/2)·Σ A²/m + O(s³)` and
`KL(F_s‖F_s^T) = (s²/2)·Σ (2A)²/m + O(s³)`, and `Σ A²/m > 0`, so the ratio tends to `1/4`.
(iv) An `R` reversible with respect to some distribution and positive wherever `P` is has the form
`R(x, y) = W(x, y)/W_1(x)`, with `W` symmetric and non-negative and `W_1(x) = Σ_y W(x, y)`. Since the rows of `F` sum to
`π`, `Σ_x π(x)·KL(P(x,·)‖R(x,·)) = Σ F·log P − Σ F·log W + Σ_x π(x)·log W_1(x)`. As in (i), `Σ F·log W = Σ m·log W`,
and the rows of `m` also sum to `π`, because `π` is stationary. With `Q(x, y) = m(x, y)/π(x)`, a transition matrix, the
value is therefore `Σ F·log P − Σ_x π(x)·Σ_y Q(x, y)·log R(x, y)`
`= Σ F·log P − Σ_x π(x)·Σ_y Q(x, y)·log Q(x, y) + Σ_x π(x)·KL(Q(x,·)‖R(x,·))`, smallest exactly at `R = Q`, which is
reversible with respect to `π`. Its value is `Σ F·log F − Σ m·log m = KL(F‖m)`, the two terms in `log π` cancelling.

**Checks.** checks/test_structure.py::test_reversibility_misalignment_is_jensen_shannon,
checks/test_structure.py::test_entropy_production_bounds_and_the_quarter_law,
checks/test_structure.py::test_the_nearest_reversible_chain

**Notes.** Log-linear learning in a potential game, in which players revise one at a time by a logit rule, has the Gibbs
law of the potential as its long-run behaviour [@blume1993] and is reversible; in other games it need not be. What
drives the circulation is the game's harmonic part [@candogan2011]. On a single cycle the entropy production is the
cycle's flux times its affinity [@schnakenberg1976], and for log-linear learning in a two-by-two game the affinity is
`t·C`, with `C` the payoff gained around the cycle of single-player deviations (`probes/general/`, B2;
`general/derived-spaces.md`). (iii) is the quarter law that probe T4 found before it was derived (B1).

**Lineage.** New. `NOTES.md` §5.4, H12; probes T4, B1 and B2.

### P42 — Several principals: gridlock, and the pooled pursuit
**Statement.** Let principals `k = 1, …, K` declare standard specifications of objectives `F_k` from one default `q`,
with misalignments `M_k`, and let weights `w_k > 0` with `Σ_k w_k = 1` be declared. The **weighted misalignment** of
`p ∈ Δ` is `Σ_k w_k·M_k(p)`.
(i) **Gridlock.** `M_k(q) = 0` for every `k`, so `q` minimizes the weighted misalignment, and every minimizer has
`M_k = 0` for every `k`.
(ii) **Pooling.** If each principal declares one intensity `t_k ≥ 0`, so that its only intended behaviour is
`p_k = p_{F_k,t_k}`, then for every `p ∈ Δ`,
`Σ_k w_k·KL(p‖p_k) = KL(p‖p_{G,1}) + Σ_k w_k·log E_q[e^{t_k·F_k}] − log E_q[e^G]`, with `G = Σ_k w_k·t_k·F_k`. So the
pursuit of `G` at intensity `1` is the unique minimizer.

**In plain terms.** When several principals each ask for a pursuit of their own objective from one default, doing
nothing satisfies all of them: the default is never misaligned under a standard specification, so gridlock is always a
best compromise. When each names the strength it wants, the compromise that disappoints them least on weighted average
is a single pursuit, of their objectives added up, each scaled by its strength and its weight. Who counts how much
remains a declaration, not a result.

**Proof.** (i) `q = p_{F_k,0}` lies on every pursuit ray, so `M_k(q) = 0` for each `k`; a weighted sum of non-negative
terms with positive weights is `0` exactly when each term is.
(ii) `log p_k = log q + t_k·F_k − log E_q[e^{t_k F_k}]`, so
`Σ_k w_k·KL(p‖p_k) = KL(p‖q) − E_p[G] + Σ_k w_k·log E_q[e^{t_k F_k}]`. By [P4](i) at intensity `1` with the objective
`G`, `KL(p‖q) − E_p[G] = KL(p‖p_{G,1}) − log E_q[e^G]`, since the net value of `p_{G,1}` is `log E_q[e^G]`.

**Checks.** checks/test_structure.py::test_gridlock,
checks/test_structure.py::test_pooling_with_declared_intensities

**Notes.** (ii) is logarithmic pooling: the compromise multiplies the intended behaviours, each raised to its weight.
With floors ([P35]) in place of fixed intensities, a probe found the compromise to be a pursuit of `Σ_k w_k·t_k·F_k`,
with `t_k` the intensity of its nearest intended behaviour for principal `k` (T5), often at the floors but not always
(T5b, a failed prediction); this is not claimed. Choosing the weights, by aggregating preferences, is outside the core.

**Lineage.** New. `NOTES.md` §5.4, H13; probes T5 and T5b.

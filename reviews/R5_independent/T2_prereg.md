# Tier-4 transfer tests — preregistration (written before any run)

Actors: Gibbs tilt (reference); best-of-n on F̂ (BoN, exact law on finite X); vanilla softmax policy
gradient on E_p F̂ from logits log q, exact gradient, no KL penalty, early-stopped (VPG); natural policy
gradient (NPG). Counterfactual for every actor: the same algorithm run on F, compared at equal
KL(p‖q) (the core's default budget convention). For BoN with no ties, equal n gives equal KL exactly.
Instance for crossing: the V5 fixed-intent pair (n = 2000, uniform q, F ~ N(0,1), E1 = 0.6·N(0,1),
E2 = 6 on one state).

| # | Tier-4 claim | Prediction for BoN | Prediction for VPG | Mechanism |
|---|---|---|---|---|
| T-A | C8 crossing | **holds** | **holds** | both asymptotes (near-q and argmax) are optimizer-independent |
| T-B | Prop 14(ii): initial effect has sign of Cov_q(F̂,F) | **fails** on a constructed instance | **fails** for non-uniform q, holds for uniform q | BoN's first-order weight is the rank U(F̂), not F̂; VPG's initial velocity is a q²-weighted covariance |
| T-C | Prop 18 link: cheap ⇒ slow to detect | **fails** (value regret → 0 with Chernoff bounded away from 0) | — | "harm in nats" is not defined off the tilt; only C ≤ KL(p̂‖p*) survives |
| T-D | B4: Gaussian joint ⇒ no overoptimization | **holds** | **holds** | any actor with w = dp/dq a function of F̂ alone gives gold gain ∝ proxy gain |
| T-E | Cor 13.3: rescaling F̂ is not harmless | **fails** (harmless) | **fails** at matched KL | BoN is monotone-invariant; VPG under sF̂ is a time reparametrization; Gibbs itself is harmless under the budget convention |
| T-F | Prop 4 / Prop 20: a single high spike | BoN far less exploited than Gibbs at matched proxy gain | — | BoN weight on a state is ≤ n·q(x) whatever the spike height; Gibbs weight grows as e^{βM} |

NPG is expected to reproduce Gibbs exactly (its path is p_{F̂,ηt}); it is a sanity check, not a test.
A prediction that fails is reported as failed, with the mechanism that was wrong.

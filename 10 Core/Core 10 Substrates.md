---
id: "Core 10 Substrates"
type: "section"
part: "core"
order: 13
updated: "2026-09-26"
---
## 10. Substrates

The measurement layer applies to any behaviour, against the declared reference `q` (Def. [[Def 1|1]], Def. [[Def 10|10]]; R7-2).
Two kinds of statement need more:
- **Value-unit** statements — the price measure, `R_J`, `ΔF` — need an independent channel for the unit of `F`
  relative to `β` (Prop. [[Prop 16|16]]).
- **Explanatory** statements — reading behaviour as an entropic actor, and attributing a departure to the
  default rather than the evaluator — need the actor's own reference `q_A`. Behaviour does not identify it
  (Prop. [[Prop 12|12]]).

Statements in terms of `D_⊥`, `M_budget` and `sign(t̂)` need only the declared `q` and the affine class of `F`.
*(Until R7-2 this paragraph read "the formalism applies wherever behaviour is an exponential tilt of a
reference", and required an independent channel "for `q`". Both belonged to the single `q` that served as
the declared and the actor's reference.)*

| Substrate | `β` | Unit channel for `F` | Actor's reference `q_A` (explanation layer) | Status |
|---|---|---|---|---|
| **biology** | `ν ∝ N_e` | log fitness is absolute; `N_e` separately estimable from neutral diversity (`θ = 4N_eμ`, `μ` measured) | neutral mutational distribution, estimable from mutation spectra | value-unit statements supported |
| **AI** | declared KL coefficient | reward units declared by the designer | the reference policy, known | supported, by fiat |
| **humans** *(v6.2)* | logit precision `1/μ`; or `1/λ`, the inverse price of attention (rational inattention) | only when the target is denominated in a measured unit, e.g. money in incentivized choice; otherwise the logit scale normalization applies, as for institutions | default-choice probabilities: **partly identifiable** from default experiments, under exclusion ([[B12]]) | `D_⊥` against a declared `q` always; attribution to the default where `q_A` is identified by default variation; value-unit statements only with monetary targets |
| **institutions** | selection intensity / logit precision | **none**: in logit models only `V/μ` is identified, and the scale is normalized (Train 2009) | "practice distribution absent selection" — a modelling choice | value-unit statements **not** supported; `D_⊥` only relative to a declared `q`, with no attribution to the institution's own default |

**Biology (imported).** In the weak-mutation regime the stationary distribution over genotypes is
`p(g) ∝ p₀(g)·exp(ν·log f(g))`. Here `p₀` is the neutral distribution, and `ν` is proportional to `N_e`; the
constant depends on the substitution model (Moran vs Wright–Fisher); the v5 values are carried, not
re-verified. The maximized functional is Iwasa's (1988) free fitness; Sella & Hirsh (2005) and Manhart,
Haldane & Morozov (2012) extend the correspondence. Conditions inherited: weak mutation, reversible substitution,
stationarity. For an objective that is a trait rather than log fitness, the exchange rate is `ν` times the
local selection gradient.

**AI.** `β` is the inverse KL coefficient, and the Gibbs actor is the optimum of KL-regularized
optimization. **Actual training paths need not be Gibbs paths** (C_boundary, C7).

**Institutions.** v5 flagged this case as weakest; Prop. [[Prop 12|12]] says why. Survival-versus-performance data
identify `β` only relative to the performance measure, i.e. relative to `F̂`, never `F`. With Prop. [[Prop 16|16]], the
unit problem can be avoided by reporting only gauge-invariant quantities (`D_⊥`, `M_budget`). The remaining
obstacle is the **reference**: the institution's own default `q_A` has no independent measurement.

*Note (R7-2).* The table's reference column is the actor's own reference. The measurement layer needs only a
**declared** reference `q`, which is always available, because declaring it is part of stating the intent
(Def. [[Def 1|1]]). Identifying `q_A` matters in two cases:
- attributing a departure to the default rather than to the evaluator (Prop. [[Prop 26|26]](b));
- when the declared reference is *meant* to be the actor's own default.

In biology and AI the two references coincide by construction: the neutral distribution, and the reference
policy of the KL penalty. Before R7-2 one `q` played both roles, so the status column read "supported where
`q` is identified". 

**Humans (v6.2).** The logit actor with default weights is the entropic actor (tier 4). The
rational-inattention actor, whose reference is its own optimized choice marginal, has an exact regret
identity with a marginal correction ([[B07|B7(e)]]; tier 1 in the actual actor, against the rational-inattention
optimum). So the human actor needs no new
carrier. What distinguishes humans from institutions is the reference: default experiments shift the chooser's own reference `q_A` while
— under exclusion — leaving the evaluator fixed, which identifies `q_A` within a parametric family ([[B12]]). The
exclusion restriction fails to the extent that defaults act as recommendations. Time inconsistency splits
along the framework's existing boundary: naive present bias is a dynamic-layer phenomenon, and
sophisticated present bias is an intrapersonal game (B §12(c)).

**Related framework.** Gottwald & Braun (Neural Computation 2019) develop the free-energy
bounded-rationality framework for systems of agents across economic, artificial and biological settings.
They do not address misspecified objectives.

**Per link.** A delegation chain has one `β` per link. Ratios of `β` across links are meaningful only
given a common unit across links. `D_⊥` per link is unit-free. See [[Boundary 05 Stated extensions, untested|Boundary §5.3]].

**One boundary, four names.** `F` must not depend on what the actor does:
- frequency-dependent selection (biology);
- multi-agent settings (AI);
- strategic interaction (institutions);
- intrapersonal games of sophisticated present-biased agents (humans; v6.2, [[B12|B §12(c)]]).

See [[Boundary 03 The boundary as two conditions|Boundary §3]] for the full boundary, which has two conditions, not one, and for the v6.2 refinement:
a reference that is optimized as part of the capacity (rational inattention) is not a violation.

---


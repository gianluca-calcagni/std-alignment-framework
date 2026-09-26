---
id: "Boundary 03 The boundary as two conditions"
type: "section"
title: "The boundary as two conditions"
part: "boundary"
order: 4
mentions: []
updated: "2026-09-26"
---
## 3. The boundary as two conditions

> **(E) Existence.** A single functional `F` on behaviours exists.
> **(X) Exogeneity.** `F`, `β`, the evaluator and the correction loop are not functions of the actor's
> behaviour at the moment of evaluation. Neither is `q`, **unless** `q` is optimized jointly with the policy
> as part of the capacity (rational inattention). That case keeps an exact regret identity
> ([[B07|B7(e)]]) and is inside. *(Refined in v6.2; [[R059|row 59]].)*

| Outside item | Condition that fails |
|---|---|
| Arrow (sincere aggregation) | (E) |
| judge disagreement (census E10) | (E) |
| Gibbard–Satterthwaite (strategic reporting) | (X): `F` depends on reports |
| multi-agent / equilibrium | (X): `F` and the reach depend on others |
| frequency-dependent selection | (X) |
| self-reference; **acquiring capacity or resources** beyond the fixed environment; manipulation of `τ` | (X): the capacity, the correction loop, or `q` *other than by joint optimization*, depends on the actor |
| *not outside:* power-seeking in Turner's sense, within a fixed environment | inside on trajectory space; it needs a prior over intents, not frame endogeneity (R5; [[B09\|B §9]]; D row [[R064\|64]]) |
| sophisticated present bias (intrapersonal game) | (X): later selves' behaviour responds to earlier selves' — the equilibrium fork ([[B12\|B §12(c)]]) |
| auto-induced **preference** change (census G4) | (X): the target depends on the actor |
| *not outside:* auto-induced **distributional** shift with a fixed target (census C8) | inside. On trajectory space with shared dynamics, the shifted state distribution is part of the actor's own trajectory law (R5; D row [[R063\|63]]) |
| interpretability | neither: category difference |

v5 claimed three of four outside items were "one condition". **Arrow breaks that**: it is non-existence
under sincere reporting, not endogeneity. Two conditions, then, and both are needed.

**Not outside (v6.2):** a rational-inattention actor, whose reference is its own optimized action marginal.
Endogeneity of the reference through optimization of the information cost is absorbed by the calculus
([[B07|B7(e)]]). Endogeneity through tampering, manipulation, or the actor changing the target is not.

*Note (R7-4).* An agent that complies where it is rewarded and reverts where it is not is **inside** the
explanation layer: one stationary dynamic element, the continuation value, derives it (Prop. [[Prop 27|27]]). So do its
consequences — masking, selection blindness, and the fake-alignment gap (Props [[Prop 28|28]]–[[Prop 30|30]]). Two things stay
outside, by (X):
- acting on the reward channel `R`, or on the monitoring `m_c`: tampering, or disabling oversight;
- an agent that *learns* `m_c` from its own history — the dynamic layer.

The frozen census routing (v6.3) is not affected.

*Note (R7-2).* Since R7-2 there are two references. The **declared** reference `q` is part of the intent, so it
cannot depend on the actor. The actor's **own** reference `q_A` can drift with its behaviour (habit
formation, census H19). At a snapshot such drift is absorbed into an effective evaluator error
`log(q_A/q)/β` (Prop. [[Prop 26|26]](a)). Across time it is a dynamic-layer phenomenon. It violates (X) only when the
actor changes the reference *other than* through its behaviour's own statistics, e.g. by rewriting the
default. The frozen census routing (v6.3) is not affected: it was recorded against v6.3's single `q`.

---


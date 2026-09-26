import sys, re, collections
sys.path.insert(0, '.')
from routing_data import R, HARD
names = {}
for l in open('../E_census.md', encoding='utf-8'):
    m = re.match(r'^\| ([A-M][0-9]+) \| ([^|]+) \|', l)
    if m: names[m.group(1)] = m.group(2).strip()
N = len(R); ex = collections.Counter(r[2] for r in R); ly = collections.Counter(r[3] for r in R); lo = collections.Counter(r[1] for r in R)
p = lambda k: f"{k} ({100*k/N:.1f} %)"
L = []
L.append("""# T1 — Census routing: is the core general enough?

> Pre-registration: `T1_preregistration.md`, written before routing. Data and scripts: `t1/routing_data.py`
> (the 221 routings), `t1/analyse.py` (all counts below), `t1/analyse_output.txt`.
>
> The routing was done by the executor who extended the framework in this round; the bias that implies is
> discussed in §6.

## 1. Answer to the PI's question

**Partly.** The pre-registered rule passes as written, but not robustly. And most of what the core cannot
discuss is missing layers, not justified exceptions. The result says exactly which layers.

- **The decision rule passes as written:** F + P = 69.7 % ≥ 60 %, every N item is justified by a named
  layer or outside condition, and 0 % are unroutable.
- **It does not pass robustly.** Under a pessimistic reading of 44 "projection" judgements, F + P falls to
  49.8 %.
- **Fully expressible items are 35.3 %.**

**The exceptions are mostly not the "justified" kind the PI anticipated.** Of the 67 items the core cannot
discuss at all (N):
- only **19** are exceptions in that sense: 9 have no single target (aggregation, disagreeing principals,
  value change), and 10 are category differences (mechanism-level interpretability);
- **the other 48 need a missing layer:** 23 strategic, 16 frame-endogeneity, 5 dynamic, 4 statistical.

Counting every item that needs something beyond the static core — the build-order signal of
`MSG_2_steering.md` §1 — gives:

| strategic | dynamic | frame (outside-X) | statistical | outside-E | category |
|---|---|---|---|---|---|
| 51 | 27 | 22 | 16 | 13 | 13 |

**What this means for the architecture.** A layer that handles strategic interaction *and* frame
endogeneity together — the causal / multi-agent influence-diagram proposal, `C_boundary.md` §5.4 — would
address **73 items (33 %)** in one move. A dynamic layer comes second (27). The statistical layer is least
urgent (16).
""")
L.append("""> **Final, frozen (v6.4; §10 and `T1_RULES_FROZEN.md`).** A third rater adjudicated the 101 disputed items.
> The result is reported as three nested shares:
> - **named** 78 %;
> - **specific** 55–61 %;
> - **full** 29 %.
>
> The routing below (§§1–8) is the first rater's, kept as registered. **On the disputed items it was the
> outlier:** the third rater's blind codes gave κ 0.04 with it, against 0.48 with the second rater.
""")
L.append("""> **Update after the independent re-routing (R5, §9).** A second rater routed all 221 items blind to this
> routing. Agreement on expressibility is moderate (κ = 0.54–0.57), on layer substantial (κ = 0.70), and on
> locus substantial (κ = 0.76).
> - **Items both raters call fully expressible: 55 (24.9 %).**
> - At least a snapshot: 52.9 % (second rater, strict) to 70.1 % (lenient).
> - The 60 % threshold of the pre-registered rule is met only under lenient readings.
> - The build-order signal is robust: strategic interaction (51 vs 49 items) and frame endogeneity (22 vs 23)
>   lead in both routings.
""")
L.append("## 2. Totals\n")
L.append("| Expressibility | Count |\n|---|---|")
L.append(f"| F — fully expressible in the core | {p(ex['F'])} |\n| P — snapshot in the core, mechanism needs a layer | {p(ex['P'])} |\n| N — not expressible | {p(ex['N'])} |\n")
L.append("| Minimal layer | Count | Pre-registered guess |\n|---|---|---|")
guess = {'static':'40 %','statistical':'10 %','dynamic':'20 %','strategic':'17 %'}
for k in ['static','statistical','dynamic','strategic']: L.append(f"| {k} | {p(ly[k])} | {guess[k]} |")
out = ly['outside-E'] + ly['outside-X'] + ly['category']
L.append(f"| outside-E / outside-X / category | {ly['outside-E']} / {ly['outside-X']} / {ly['category']} = {p(out)} | 10 % |")
L.append(f"| undetermined | {p(ly['undetermined'])} | 3 % |\n")
L.append("| Locus | Count |\n|---|---|")
LN = {'L1':'target','L2':'evaluator','L3':'optimizer','L4':'resource','L5':'observation/context','L6':'dynamics','L7':'frame'}
for k in sorted(lo): L.append(f"| {k} {LN[k]} | {p(lo[k])} |")
L.append("""
**Against the pre-registered predictions:**

- **Layer distribution: partly wrong.**
  - static: 36 % vs 40 %;
  - dynamic: 12 % vs 20 % — lower;
  - strategic: 23 % vs 17 % — higher;
  - outside (E + X + category): 22 % vs 10 % — **more than double**.

  The error is informative. Frame endogeneity (tampering, corrigibility, oversight subversion,
  self-modification) is far more common in the census than I expected.
- **F + P ≥ 60 %: met** (69.7 %), but not robust (§5).
- **Unroutable ≤ 5 %: met** (0).
- **§14 hard cases: 11 of 12 fire** (prediction ≥ 8; §4).
- **Gates.** Not every item routes comfortably, so the "suspect the routing" gate does not fire. No items are
  outside for reasons other than (E), (X) or category, so the "missing node" gate does not fire either. But
  see §6: the strategic and frame layers are missing *layers*, not missing *nodes*.
""")
L.append("## 3. By section\n")
L.append("| Section | n | F | P | N | static | statistical | dynamic | strategic | outside-E | outside-X | category |\n|---|---|---|---|---|---|---|---|---|---|---|---|")
SN = {'A':'AI — specification','B':'AI — inner alignment','C':'AI — generalization','D':'AI — strategic','E':'AI — training','F':'AI — oversight',
      'G':'AI — multi-agent/systemic','H':'humans — individual','I':'humans — institutional','J':'biology — organism','K':'biology — genome',
      'L':'formal results','M':'empirical regularities'}
for s in 'ABCDEFGHIJKLM':
    rs = [r for r in R if r[0][0] == s]; e = collections.Counter(r[2] for r in rs); l = collections.Counter(r[3] for r in rs)
    L.append(f"| {s} {SN[s]} | {len(rs)} | {e['F']} | {e['P']} | {e['N']} | " + " | ".join(str(l[k]) for k in ['static','statistical','dynamic','strategic','outside-E','outside-X','category']) + " |")
L.append("""
**Where the core is strong:**
- AI specification (14 of 20 fully expressible);
- training pipelines (14 of 17);
- empirical regularities (7 of 16 fully, 14 of 16 at least as a snapshot);
- institutional Goodhart-type items;
- organism-level biological proxies.

**Where it is weak:**
- multi-agent / systemic AI (8 of 10 not expressible);
- AI strategic behaviour (10 of 18);
- within-genome conflict (11 of 15 only as a snapshot);
- individual humans (13 of 25 only as a snapshot, mostly because of time).
""")
L.append("## 4. The §14 hard cases\n")
L.append("| Group | Outcome | Items needing a layer or outside |\n|---|---|---|")
fired = 0
for name, ids in HARD:
    rs = [r for r in R if r[0] in ids]; needs = [r for r in rs if r[3] != 'static']; fired += bool(needs)
    L.append(f"| {name} | {'fires' if needs else 'handled'} | {len(needs)}/{len(rs)} |")
L.append(f"""
**{fired} of 12 fire: the prediction (≥ 8) is confirmed.**

- **J19 (senescence) is the one handled.** With fitness as the target, the core gives zero regret. The
  hard case's point — "nothing is misaligned" — becomes a statement the core makes, and a misalignment
  appears only once a different target (e.g. longevity) is designated.
- **J14 is handled; J16 is not.** Domestication syndrome is correlated response to selection
  (`B_dictionary.md` §11). Resistance evolving against a designed objective is adversarial, so it is
  strategic.
""")
L.append("""## 5. Robustness

**Sensitivity.** 44 of the 76 P judgements are "generous" projections: cases where the snapshot the core
offers — for instance, an extreme evaluator error on a tamper action — may be judged too thin to count as
discussing the item. They are:
- all P items whose layer is outside-X or outside-E;
- all biological conflict items;
- the strategic oversight and contract items.

Reclassifying all 44 as N gives **F + P = 110 (49.8 %)**, below the 60 % threshold.

**The honest reading.** The core fully expresses about a third of the census. It offers a meaningful
snapshot of between one sixth and one third more, depending on how generously a snapshot is judged. It
cannot express the last third.

**Items where `X` = trajectories does the work.** A9, A10, A18, I22, L1 and L11 are F or P because the
behaviour space may be a set of trajectories. That is legitimate — the core allows it — but it is also where
"static" is doing the most work for the least content. A dynamic layer would make these statements
sharper, not merely possible.
""")
L.append("""## 6. Limits of this routing

- **Rater bias.** The router extended the framework in the same round (Prop. 20, B7(e), B12) and has an
  interest in a favourable result. **An independent re-routing is needed** before this result is quoted:
  at least a random 40 items, by someone else, with agreement statistics (`ROADMAP.md` T1b).
- **Census gaps** (listed in `E_census.md` §15):
  - military command and control;
  - legal interpretation;
  - medicine;
  - safety engineering (drift to danger, normalization of deviance);
  - developmental psychology;
  - non-Western institutions.

  The first and fourth would likely add dynamic and hierarchical (chain) items, where the core is weak.
- **"Strategic" and "outside-X" are missing layers, not justified exceptions.** The PI's exception class —
  disagreeing principals — corresponds to outside-E (13 items, 5.9 %). Tampering, corrigibility, collusion
  and games are central alignment topics. The core's silence on them is a gap to fill, not a boundary to
  accept.
""")
L.append("""## 7. Post-hoc note — not part of the registered result

After routing, `B_dictionary.md` §13 added one strategic piece within the current carrier. Potential games
under log-linear learning are a tilt of the joint behaviour space (Blume 1993).

**The registered routing above was not changed.** Items this plausibly affects, for an independent rater to
judge:

| Item | Why it may move |
|---|---|
| I14 (commons) | Cournot commons is a potential game: P or F |
| I15 (free riding) | public goods is a potential game; free riding is anti-alignment, `X_anti > 0`: P or F |
| G6 (race dynamics) | if modelled as a symmetric 2×2 game, it is a potential game: P |
| J12, G3 | uncertain — contests and repeated pricing are generally not exact potential games |

If all of I14, I15 and G6 moved, strategic N would fall from 23 to 20, and F + P would rise from 69.7 % to
71.0 %. The strategic layer remains the largest gap.
""")
L.append("## 8. The 221 routings\n")
L.append("F = fully expressible; P = snapshot; N = not expressible. Layer = minimal layer for full expression.\n")
L.append("| # | Name | Locus | Expr. | Layer | Carrier / justification |\n|---|---|---|---|---|---|")
for r in R: L.append(f"| {r[0]} | {names[r[0]]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} |")
# ---- section 9: independent re-routing (R5) ----
from reviewer_routing_R5 import R as RM
from collections import Counter as C
prev = {r[0]: r for r in R}; ids = [r[0] for r in R]
def kappa(a, b):
    n = len(a); po = sum(x == y for x, y in zip(a, b))/n; ca, cb = C(a), C(b)
    pe = sum(ca[k]*cb[k] for k in set(ca) | set(cb))/n/n; return po, (po - pe)/(1 - pe)
len_ = [{'Pt': 'P'}.get(RM[i][1], RM[i][1]) for i in ids]; strict = [{'Pt': 'N'}.get(RM[i][1], RM[i][1]) for i in ids]
pe = [prev[i][2] for i in ids]
kl = kappa(pe, len_); ks = kappa(pe, strict); kly = kappa([prev[i][3] for i in ids], [RM[i][2] for i in ids]); klo = kappa([prev[i][1] for i in ids], [RM[i][0] for i in ids])
rc = C(RM[i][1] for i in ids); rl = C(RM[i][2] for i in ids)
Fb = sum(prev[i][2] == 'F' and RM[i][1] == 'F' for i in ids)
FPb_len = sum(prev[i][2] in 'FP' and len_[k] in 'FP' for k, i in enumerate(ids)); FPb_str = sum(prev[i][2] in 'FP' and strict[k] in 'FP' for k, i in enumerate(ids))
FP_len = sum(x in 'FP' for x in len_); FP_str = sum(x in 'FP' for x in strict)
L.append("""## 9. Independent re-routing (T1b, review R5)

The second rater (`reviews/R5_independent/`) routed all 221 items blind to this routing: the routing file was
frozen and hashed before this report was opened. The rater introduced one refinement, **`Pt`**: a snapshot
that reduces to a generic proxy error, without using specific core structure. The lenient reading counts
`Pt` as P; the strict reading counts it as N.
""")
L.append("| Agreement | Raw | Cohen's κ |\n|---|---|---|")
L.append(f"| expressibility, lenient | {kl[0]:.3f} | {kl[1]:.3f} |")
L.append(f"| expressibility, strict | {ks[0]:.3f} | {ks[1]:.3f} |")
L.append(f"| minimal layer | {kly[0]:.3f} | {kly[1]:.3f} |")
L.append(f"| locus | {klo[0]:.3f} | {klo[1]:.3f} |")
L.append(f"""
**The T1b gate** (κ < 0.4 means the counts are not quoted) **passes**. Agreement is moderate on
expressibility and substantial on layer and locus.

| Quantity | This routing | Second rater, lenient | Second rater, strict | Both raters |
|---|---|---|---|---|
| F | {ex['F']} ({100*ex['F']/N:.1f} %) | {rc['F']} ({100*rc['F']/N:.1f} %) | {rc['F']} | **{Fb} ({100*Fb/N:.1f} %)** |
| F + P | {ex['F']+ex['P']} ({100*(ex['F']+ex['P'])/N:.1f} %) | {FP_len} ({100*FP_len/N:.1f} %) | {FP_str} ({100*FP_str/N:.1f} %) | {FPb_len} ({100*FPb_len/N:.1f} %) lenient; {FPb_str} ({100*FPb_str/N:.1f} %) strict |
| strategic layer | {ly['strategic']} | {rl['strategic']} | | |
| frame (outside-X) | {ly['outside-X']} | {rl['outside-X']} | | |
| dynamic | {ly['dynamic']} | {rl['dynamic']} | | |
| statistical | {ly['statistical']} | {rl['statistical']} | | |
| outside-E / category | {ly['outside-E']} / {ly['category']} | {rl['outside-E']} / {rl['category']} | | |
| undetermined | 0 | {rl['undetermined']} | | |

**What the comparison shows.**

- **My routing was generous in one systematic way.** 22 items I called F the second rater calls P, 12 of
  them with the statistical layer: goal misgeneralization (B9, C1, C2, C9), context-dependent training
  (B12, M9, E17), learned evaluators and proxy internalization (B8, E5, M2), and composition (E15, F9). These phenomena name a learning
  mechanism. The core expresses their snapshot, not what is learned. **I accept this reading.**
- **The second rater is more lenient on frame items.** Several of my N items are `Pt` there — tampering-like
  items (D3, D11–D13, B6) — and several strategic items (J11–J13, K9). The strict reading restores N.
- **My "generous 44" was mis-targeted.** Of those 44, the second rater keeps 21 as P or F. Meanwhile 15 of my
  other P items are N or `Pt` for them. The totals nevertheless agree: my pessimistic 49.8 % against their
  strict 52.9 %.
- **The §14 hard cases fire 11 of 12 in both routings, but not the same 11.** For the second rater
  senescence (J19) is outside-E — which target? — and J14 and J16 are both handled. J16 becomes anti-alignment
  of a population tilt with a designated target.
- **Four pushbacks change the framework, not only the counts.**
  - C8, auto-induced distributional shift, is inside on trajectory space (`C_boundary.md` §3).
  - Turner-style power-seeking needs a prior over intents, not frame endogeneity (`B_dictionary.md` §9).
  - F10 and M14, Goodhart on a fixed monitor, are static.
  - I5, Campbell's law, is Goodhart restated.

  The first two are recorded as `D_status.md` rows 63 and 64.

**The robust reading, stated once.**
- The core fully expresses about **a quarter to a third** of the census.
- It gives at least a snapshot of **half to two-thirds**.
- **Strategic interaction and frame endogeneity** are the largest gaps: about 72–73 items in either routing.
- Justified exceptions (no single target, mechanism-level) are about **20 items**.
""")
# ---- section 10: adjudication (R6), frozen ----
import importlib.util
def _load(p, n):
    sp = importlib.util.spec_from_file_location(n, p); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
ADJ = _load('adjudicated_routing.py', 'adj').R
P3 = _load('../reviews/R6_independent/adjudication/routing_R6_phase1.py', 'p3').R
ae = C(v[0] for v in ADJ.values()); al = C(v[1] for v in ADJ.values())
blind = {i: (ADJ[i][0] if ADJ[i][2] == 'agreed' else None) for i in ADJ}
for i in P3: blind[i] = P3[i][1]
be = C(blind.values())
L.append(f"""## 10. Adjudication by a third rater (R6) — the frozen result

A third rater routed the 101 disputed items and 20 agreed controls blind. It hashed that routing, then ruled on
eight rule-level questions and adjudicated every item. Files: `reviews/R6_independent/adjudication/`; the
final codes are in `t1/adjudicated_routing.py`; the frozen rules are in `T1_RULES_FROZEN.md`.

| Share | Adjudicated | Third rater, blind |
|---|---|---|
| named (F + P + Pt) | {ae['F']+ae['P']+ae['Pt']} ({100*(ae['F']+ae['P']+ae['Pt'])/N:.1f} %) | {be['F']+be['P']+be['Pt']} ({100*(be['F']+be['P']+be['Pt'])/N:.1f} %) |
| **specific (F + P)** | **{ae['F']+ae['P']} ({100*(ae['F']+ae['P'])/N:.1f} %)** | **{be['F']+be['P']} ({100*(be['F']+be['P'])/N:.1f} %)** |
| full (F) | {ae['F']} ({100*ae['F']/N:.1f} %) | {be['F']} ({100*be['F']/N:.1f} %) |

**Layers needed** (adjudicated):
- strategic {al['strategic']};
- statistical {al['statistical']};
- outside-X {al['outside-X']};
- dynamic {al['dynamic']};
- outside-E {al['outside-E']};
- category {al['category']};
- static {al['static']}.

**Why this is reported as nested shares.** The "specific" share sits on the pre-registered 60 % threshold, and
single defensible perturbations move it across. **The frozen format is three shares with a band. Pass/fail
is retired.**

**Anchoring check.**
- The third rater's blind codes on the disputed items agreed with the second rater (κ 0.48), and hardly at
  all with the first (κ 0.04).
- In adjudication it sided with the second rater on 55 items, the first on 23, and neither on 23.
- The T1c anchoring gate does not fire.
- It overrode 3 of 20 controls (K10, I15, G6). K10 suggests a generosity both earlier raters shared,
  treating Price/B11 as specific structure for biological conflicts.
""")
open('../build/T1_census_routing_regenerated.md', 'w', encoding='utf-8')  # v7.0: the vault note is frozen; regenerate for comparison only
if False: open('../T1_census_routing.md', 'w', encoding='utf-8').write("\n".join(L) + "\n")
print("written", len(R))

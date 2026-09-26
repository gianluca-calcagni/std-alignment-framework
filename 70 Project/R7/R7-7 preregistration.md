---
id: "R7-7 preregistration"
type: "report"
updated: "2026-09-26"
---
# R7-7 — pre-registration (written before any R7-7 computation)

**What is already seen.** The R7-5 probe (`70 Project/R7/r75_probe.py`, `r75_c5.py`; [[R7-5 go-no-go]]) computed
`M_ord` for best-of-n and quantilizers on the true target (400 instances each), compared the isotonic closed form
with a generic optimizer (60 instances), and checked the corollary `M_free ≥ M_ord + M_free(p°)` (1,000 instances).
Predictions that repeat those computations are marked **(R)**: they are replications on fresh seeds, and they can
confirm nothing new. Nothing else below has been computed. The budget-convention ordinal measure, the block
formula and the budget split were derived for this step and have never been evaluated.

## The definitions under test (measurement layer)

**Target set (new Def. 17).** A target set `𝒯` is a non-empty set of non-constant functions on `X`, closed under
positive affine maps. Every member is an admissible statement of one intent.
- The **cardinal** set of a non-constant `F` is `[F]₊ = {aF + c : a > 0}`: the current single target.
- The **ordinal** set is `[F]_ord = {φ∘F : φ strictly increasing}`: only the order of outcomes is intended.
- Intended sets: `I_free(𝒯)` is the closure, within the full-support simplex, of the union of the half-rays
  `{p_{G,t} : t ≥ 0}` over `G ∈ 𝒯`. `I_budget(𝒯; k) = I_free(𝒯) ∩ {p : KL(p‖q) = k}` with `k = KL(p̂‖q)`.
- Measures: `M_κ(𝒯) = inf_{p ∈ I_κ(𝒯)} KL(p̂‖p)` for `κ ∈ {budget, free}`. The budget measure is undefined when
  `I_budget` is empty. `M_ord := M_free([F]_ord)`.
- The price convention needs a representative with a unit, so it is defined for a cardinal set with a declared
  representative only.
- A family of target sets (disagreeing principals) is measured member by member. No aggregate is defined.

**The contract restated (Def. 11).** A measure takes a target set. M1: `M = 0` iff `p̂ ∈ I_κ(𝒯)`. M3: `M` depends on
the target only through `𝒯`. M5: `p̂ = p_{G,t}` for some `G ∈ 𝒯`, `t ≥ 0` implies `M = 0`. M2, M4, M6 and M8 are
unchanged. For `𝒯 = [F]₊` each reads exactly as in v7.3.3.

**Claimed results.**
- **Prop. 31 (target sets against the contract).** (a) `𝒯 = [F]₊` reproduces Def. 10's `M_free` and `M_budget`,
  saturation included. (b) `M_free(𝒯)` and `M_budget(𝒯)` satisfy M1–M6 and M8, and the infimum is attained.
  (c) `𝒯 ⊆ 𝒯′` implies `M_κ(𝒯′) ≤ M_κ(𝒯)`, and `M_free(𝒯) ≤ M_budget(𝒯)`.
- **Prop. 32 (the ordinal measure).** Let the levels of `F` be `L_1 < … < L_m`, and `y = p̂/q`.
  - (a) `I_free([F]_ord) = C_F`, the full-support `p` with `p/q` a non-decreasing function of `F`.
  - (b) The unique minimizer is `p° = q·r°`, where `r°` is the `q`-weighted isotonic regression of the level means
    of `y` (pool-adjacent-violators). With pooled blocks `B`: `M_ord = Σ_B p̂(B)·KL(p̂(·|B) ‖ q(·|B))`.
  - (c) For every `p ∈ C_F`: `KL(p̂‖p) = KL(p̂‖p°) + KL(p°‖p) + ⟨r° − y, log(p/q)⟩_q`, the last term `≥ 0`. At
    `p = q`: `KL(p̂‖q) = M_ord + KL(p°‖q)`.
  - (d) `M_free ≥ M_ord + M_free(p°)`, and, where defined, `M_budget ≥ M_ord + KL(p°‖p_{F,λ})`.
  - (e) `M_ord` depends on `F` only through the ordered partition into levels.
  - (f) `M_budget([F]_ord)` is defined iff `M_budget` is, and then `M_ord ≤ M_budget([F]_ord) ≤ M_budget`, the
    first inequality strict iff `M_ord > 0`.

## Generator (block V35, seeded)

1,200 instances, 200 of each behaviour kind.
- `n` uniform on `{3, …, 12}`. `q ~ Dirichlet(1)`, redrawn until `min q ≥ 10⁻³`.
- `F`: with probability 1/2 i.i.d. `N(0,1)` (no ties); otherwise integers uniform on `{0, …, max(1, ⌊n/2⌋)}`
  (ties). Redrawn until it has at least two values.
- Behaviour kinds:
  - **A** random: `Dirichlet(1)`, redrawn until `min p̂ ≥ 10⁻⁴`;
  - **B** monotone: `p_{ψ∘F,t}`, with `ψ` random strictly increasing and `t ~ U(0, 3)`;
  - **C** best-of-`k` on `F` from `q`, `k ∈ {2, 4, 16, 64}`, ties inside the winning level broken in proportion
    to `q`;
  - **D** quantilizer: `q` restricted to the top `α ∈ {0.1, 0.3}` of `q`-mass by `F` (the boundary level
    included in proportion), mixed with `q` at weight `10⁻³`;
  - **E** noisy: `p_{F,t}` reweighted by `e^{σz}`, `z ~ N(0,1)` per state, `σ ∈ {0.05, 0.3, 1}`, `t ~ U(0, 3)`;
  - **F** sign-flipped: `p_{−F,t}`, `t ~ U(0.1, 3)`.
- Generic optimizers (SLSQP) work in level coordinates: ratios `r_1 > 0` plus non-negative increments,
  `Σ_j q(L_j) r_j = 1`, and for the budget measure also `Σ_j q(L_j) r_j log r_j = k`. `M_ord`: 3 starts. The budget
  ordinal measure: 5 starts, one of them the cardinal budget point `p_{F,λ}`, none of them `p̂`.

## Predictions

| # | Claim | Prediction | Falsified if |
|---|---|---|---|
| P1 (R) | 32(b), closed form | no generic optimum is below the isotonic value | any instance with generic value `< M_ord − 10⁻⁹` |
| P2 | 32(b), block formula | `M_ord` equals the pooled within-block divergence | a difference above `10⁻¹²` (absolute, or relative for values above 1) |
| P3 | 32(c) at `p = q`, the budget split | `KL(p̂‖q) = M_ord + KL(p°‖q)` | a difference above `10⁻¹²` |
| P4 (R) | 32(c)–(d) | the cross term is `≥ 0` for 20 random `p ∈ C_F` per instance; both inequalities of (d) hold | any cross term `< −10⁻¹²`; any (d) slack `< −10⁻¹⁰` |
| P5 | M1 for `M_ord` | `M_ord ≤ 10⁻¹²` exactly when an independent test finds non-decreasing level ratios and `p̂ ∝ q` inside every level, each to relative `10⁻¹⁰`; this includes every instance of kinds B, C and D. `M_ord > 10⁻⁹` in every kind-F instance | any disagreement with the independent test |
| P6 | M3, strong form (32(e)) | `M_ord` is unchanged under a fresh random strictly increasing `ψ` per instance. The cardinal `M_free` changes by more than `10⁻⁶` in at least 95 % of kind-A instances with three or more levels | `M_ord` moves by more than `10⁻¹²`; or the cardinal share is below 95 % |
| P7 | R7-5's defect, repaired under both conventions | kinds C and D: `M_ord ≤ 10⁻¹²` **(R)** and `M_budget([F]_ord) ≤ 10⁻⁸` (new). The cardinal `M_free > 10⁻⁶` in at least 90 % of kind C and D instances with three or more levels **(R)** | any ordinal value above its bound; the cardinal share below 90 % |
| P8 | 32(f) | where defined: `M_ord ≤ M_budget([F]_ord) + 10⁻⁹` and `M_budget([F]_ord) ≤ M_budget + 10⁻⁹`; `M_budget([F]_ord) − M_ord > 10⁻¹²` whenever `M_ord > 10⁻⁹` | any violation |
| P9 | M8 | a two-context agent that is ordinal-aligned in evaluation (kinds B, C) and sign-flipped in deployment (kind F) scores 0 in evaluation (`≤ 10⁻¹²`) and more than `10⁻⁹` in deployment, under `M_ord` | either fails |
| P10 | M7 | with the R7-7 edits, V1–V34 and F1–F8 reproduce (`tools/reproduce.py`). For `𝒯 = [F]₊` the target-set implementation returns Def. 10's `M_free` and `M_budget` to `10⁻¹⁰` | any block differs; any difference above `10⁻¹⁰` |

## Decision rules, stated in advance

- **D1 (can the budget ordinal measure be computed?).** Its problem is not convex: the budget sphere is a level set
  of a convex function. If the best two of the five starts agree to `10⁻⁷` in fewer than 90 % of the instances where
  it is defined, its numbers are not quoted. R7-7 then records the ordinal target as usable under the free
  convention only, with the budget measure defined but not computed.
- **D2 (a failed proof-backed prediction).** P2–P6, P8 and P9 test proofs. If one fails, the statement is wrong,
  not the check. It is recorded as falsified; a corrected statement is a new result with a new check.
- **D3 (stop rule, R7 step 7).** If lint cannot be brought to 0 errors within the step, or P10 fails, Defs 11 and 12
  and Prop. 24 are restored from v7.3.3 and the blocking dependency is reported.
- **D4 (the falsifier of the step's purpose).** R7-7 exists to stop a right-target agent being charged for the
  shape of its pursuit. If D1 passes and the budget part of P7 fails, the ordinal declaration does not repair the
  defect under the default convention. That becomes the headline.

## Exploratory, reported without a prediction

- **X1.** `M_budget([F]_ord) / M_ord` and `M_budget([F]_ord) / M_budget` on kinds A and E.
- **X2** (explanation layer; a replication of R7-5's C5). The share of `M_free` that is ordering error, `M_ord / M_free`,
  on kind E, by `σ`.
- **X3.** How often `p°` pools more than one level into a block, on kinds A and E.

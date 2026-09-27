---
id: "R7-10 results"
type: "report"
updated: "2026-09-27"
---
# R7-10 — results: declared resolution (v7.8)

Pre-registered in [[R7-10 preregistration]] (sha256 `0c4e95a1…`, commit `d1e7a8d`), before any computation. Check:
[[V40]], on two SIMD paths. **Four of five predictions held; P5 failed as registered on a threshold, and the claim it
tested is unchanged.** Adopted: Def. [[Def 21|21]], Prop. [[Prop 36|36]].

## What was found

- **The declared-resolution measure was already inside the core.** For every free-type measure, the finest measure is
  the coarse one plus the style term: `M = M^𝒢 + W`, exactly (P2, to `10⁻¹⁵`). A principal who declares "style
  free" removes `W` and nothing else.
- **The budget convention misreads style as pursuit.** Its matched intensity is fixed by the total information spent,
  `k = k_𝒢 + W`, so the within-cell divergence raises the intensity it compares against. The excess `Θ` (called `E` in
  the frozen pre-registration; renamed because `E` is the evaluator error of the explanation layer) is positive
  exactly when `W` is (P3: at least `7.9·10⁻⁷` wherever `W > 10⁻⁸`, on all 496 instances where both measures are
  defined). **Under the default resolution, a budget verdict of over-optimization can be style drift.** The free
  convention does not have this defect.
- **The budget convention also stops answering.** On 91 of 600 instances, the finest budget measure is undefined
  (style drift pushed `KL(p̂‖q)` past the saturation value) while the measure at the declared resolution is defined.
  This was reported, not predicted.
- **The blind spot is exact.** Resampling the split inside cells moves `M^𝒢` by `10⁻¹⁵` (P4). Exploitation inside a
  cell is invisible at that resolution; this is the price of the declaration, and it is v5's transmission gap
  (ROADMAP §6 G2, I1).

## P5 — failed as registered

P5 required `M^𝒢` constant in the refinement `n` to `10⁻¹²`; it moved by `7.3·10⁻¹²` on both paths. The rest of P5 held:
the free measure rose strictly and ended 11.09 nats above `M^𝒢` at `n = 2¹⁶`.

**Diagnosis** (`r710_diagnose.py`, output in `r710_diagnose_output.txt`). The check rebuilt each cell mass by summing
`2¹⁶` floats. With `np.bincount` the rebuilt masses are off by `3.4·10⁻¹²` and `M^𝒢` moves by `3.8·10⁻¹²`; with exact
summation (`math.fsum`) the masses are exact to `6·10⁻¹⁷` and `M^𝒢` is constant to `1.7·10⁻¹⁶`. The claim is exact by
construction — `M^𝒢` sees only the cell masses — so the statement stands. Under D1 the failure stays recorded; the
threshold was set without summation error in view. This is the second threshold of this kind (R7-7's P8 was the
first); [[NOTES_claude]] §1 records the pattern.

## Declarations

The registry of [[R7-9 results]] gains its sixth declared row: **resolution**, with default the finest partition and
elicitation "Which differences between behaviours matter to you at all?". The silent choice "inside a cell, the
intended split follows `q`" is now the default of that declaration, not a silent choice. R7-8 keeps only the
measurable-space generalization.

## Rule 13, after the fact

The style-drift example changed a verdict as predicted (charged → 0 under the declaration). The budget
misattribution changed a *diagnosis*: an agent pursuing the target at `t = 1` is compared with an intensity of 2.62
in the probe. Neither is yet a real case. T7 is where that is tested (ROADMAP §4b).

## Open

- Budget measures for caps, floors and ordinal sets under a resolution: not claimed.
- Should the budget convention's default be the declared-resolution budget `k_𝒢`? It is, under a declared
  resolution; under the default resolution the defect stands, and the free convention is the safer reading.
- Continuous `X` (R7-8) is covered only by finite refinement.

---
kind: corollary
id: C9
aliases: ["C9"]
source: "derived/forbids.md"
---
# C9 — Grouping outcomes never shows more misalignment
> [!info] Generated from [derived/forbids.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/forbids.md#c9--grouping-outcomes-never-shows-more-misalignment). Edit the source, not this note.

## Statement
For any specification `(q, 𝓘)`, resolution `ℬ` and `p̂ ∈ Δ`,
`inf_{p∈𝓘} KL(p̂_ℬ‖p_ℬ) ≤ M(p̂)`, where `p_ℬ` gives each cell of `ℬ` its mass under `p`.

## In plain terms
A principal who sees only coarse records never sees more misalignment than there is.

## Proof
By [[P4 — What KL measures|P4]](iv), `KL(p̂_ℬ‖p_ℬ) ≤ KL(p̂‖p)` for every intended `p`; take the infimum over `𝓘`.

## Lineage
v8: [[D3 — Specification, declaration and misalignment|D3]]'s "grouping only hides". New as a forbidden statement.

## Checks
- [`checks/test_forbids.py::test_grouping_never_shows_more_misalignment`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_forbids.py)
- [`checks/test_value.py::test_merging_never_increases`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_value.py)

## Depends on
- [[P4 — What KL measures|P4]] — What KL measures

## Used by
- no later item

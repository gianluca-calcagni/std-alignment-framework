---
kind: corollary
id: C7
aliases: ["C7"]
source: "derived/forbids.md"
---
# C7 — No test detects misalignment faster than misalignment
> [!info] Generated from [derived/forbids.md](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/derived/forbids.md#c7--no-test-detects-misalignment-faster-than-misalignment). Edit the source, not this note.

## Statement
From independent samples, no test separates the actor's behaviour from its nearest intended behaviour
with an error exponent above its misalignment `M(p̂)` ([[P22 — No test detects misalignment faster than misalignment|P22]]).

## In plain terms
A small misalignment is, necessarily, slow to detect, even for an observer who knows both
behaviours exactly.

## Proof
[[P22 — No test detects misalignment faster than misalignment|P22]](i) and (iii).

## Lineage
v7.10: §11.7 and Prop 18.

## Checks
- [`checks/test_estimation.py::test_detection_is_capped_by_misalignment`](https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/checks/test_estimation.py)

## Depends on
- [[P22 — No test detects misalignment faster than misalignment|P22]] — No test detects misalignment faster than misalignment

## Used by
- no later item

# std-alignment-framework — the core (v9, in progress)

[![checks](https://github.com/gianluca-calcagni/std-alignment-framework/actions/workflows/checks.yml/badge.svg)](https://github.com/gianluca-calcagni/std-alignment-framework/actions/workflows/checks.yml)

A standard formal framework for alignment problems in general, not only in machine learning: AI systems, humans,
institutions and organisms. The aim is a framework that is solid enough to build on, substrate-independent, easy to
import existing theorems into, and able to make testable predictions, support diagnostics, and show its own limits.

The core holds only what cannot be derived: five premises and the definitions the whole framework uses. Everything
else is derived from them, with proofs and checks, and reported through one standard.

## Where things are

| | |
|---|---|
| `CORE.md` | the core: scope, premises (A) and definitions (D), read top to bottom |
| `derived/` | the results (P), one file per topic, each with proofs and checks; `derived/README.md` gives the reading order |
| `STANDARD.md` | the reporting standard: what a report of misalignment must declare, observe and report |
| `REFERENCES.md` | the sources cited anywhere in the framework |
| `RELATED.md` | related theories: what each shares with the framework, what differs, what to import, and what it could take from us |
| `checks/` | one pytest check, at least, for every result |
| `tools/lint.py` | the rules below, as code; `tools/test_lint.py` tests them |
| `ontologies/` | the core read in five disciplines, each in its own folder: machine learning, biology, humans, institutions, and job delegation from a manager to an employee. Each fills the same typed slots and reframes one known result. Not part of the core |
| `TERMS.md` | the vocabulary: every defined term, its other names in the literature, correspondences not yet worked out, and every naming decision, each with a confidence level |
| `NOTES.md` | the executor's working notes: failure modes, open requests and recommendations. Not part of the core |
| `main` branch | **the archive** (v7.10, commit `9459c14`): everything proved, tested, retracted and logged before the restart. Nothing there changes. A file comes over only when an item needs it (`git checkout main -- <path>`), and the item's lineage says so |

## Rules

**Enforced by lint** (`python3 tools/lint.py`; a property of the framework is claimed only if lint checks it):
- **R1–R2.** Every `###` heading in `CORE.md` and `derived/` is an item: `### D1 — title`. `CORE.md` holds premises (A)
  and definitions (D); `derived/` holds results (P proposition, T theorem, L lemma, C corollary) and remarks (R), in
  files that `derived/README.md` lists in reading order. Ids are unique, and numbers increase within each kind in each
  file.
- **R3–R4.** Every item has a **Statement**, an **In plain terms** twin and a **Lineage**. A premise or definition also
  has a **Why this choice**; a result has a **Proof** and **Checks**. Fields come in a fixed order, with no field empty.
- **R5.** References are written `[D1]`, `[P3]`, and name existing items. A core Statement uses only earlier core
  items; a result uses only the core and results earlier in the reading order; a core "why" may cite a result. The
  dependencies form no cycle.
- **R6–R7.** Every check a result cites exists in `checks/`, and every check there is cited by some item.
- **R8.** Every citation `[@key]` is listed in `REFERENCES.md`, and every listed source is cited somewhere.
- **R9.** Every term an item defines (bold in its Statement) has an entry in `TERMS.md`, and every item `TERMS.md` names
  exists.
- **R10.** Every ontology lives in its own folder, fills each slot listed in `ontologies/README.md` once, naming the
  slot's item and how well it fits; has the five sections in order; cites the known result it reframes; and labels
  every claim as a consequence, a prediction (which says when it is refuted) or a reading, with the items it uses.
- **R11.** `STANDARD.md` names only existing items, and names every definition of the core.
- **R12.** `RELATED.md` names only existing items, and its citations are listed like all others.

**Enforced by CI** (`.github/workflows/checks.yml`, on every push and pull request): lint, and every check on two
SIMD paths. A check asserts its claim with a tolerance derived from the scale of the quantity. It must hold on both
paths, rather than reproduce printed digits.

**Working agreements** (no tool checks these, so they are commitments, not claimed properties):
- **The core holds what cannot be derived**, and the definitions used everywhere. A result belongs in `derived/`. A
  concept earns its own item when splitting it makes the framework clearer; items are not merged only to be fewer.
- **Reliability over elegance.** A result enters with a proof and a check that could fail: random instances, the
  degenerate and sign cases, and tolerances derived from the quantity's scale. Every new check is mutation-tested.
- **Every choice is justified.** "Why this choice" argues it, by generality, by canonicity, or by a named case where the
  alternative gives a wrong verdict. Assume less and derive more.
- **Plain terms keep the qualifiers** of the formal statement.
- **Lineage** names the items on `main` that an item replaces and the retraction rows that touch them
  (`main: 60 Status/retractions/`), or says "New".
- **Empirical tests** are pre-registered and pushed before any computation, as on `main`.
- **One step, one branch, one pull request** into the branch that holds the new core, merged with a merge commit.

## The format of an item

```markdown
### D1 — Outcomes and default
**Statement.** A finite set `X` of outcomes, and a full-support distribution `q` on `X`, the default.
**In plain terms.** The things that can happen, and how often each happens by default.
**Why this choice.** …
**Lineage.** main: Def 1 (in part).

### P1 — Every behaviour is a tilt of the default
**Statement.** For every full-support `p` on `X` there is `F` with `p ∝ q·e^F`; `F` is unique up to a constant.
**In plain terms.** Any way of behaving can be written as the default reweighted by some objective.
**Proof.** …
**Checks.** checks/test_tilt.py::test_every_distribution_is_a_tilt
**Lineage.** New.
```

A premise (A) has the fields of a definition. A result lives in `derived/` and has the fields of P1 above. Optional
fields, in order: **Example** (after Proof) and **Notes** (after Checks; attribution goes here, because a citation in a
proof is a dependency claim).

## Commands

```bash
pip install -r requirements.txt       # Python 3.11
python3 tools/lint.py                 # 0 errors required
python3 -m pytest                     # checks and linter tests
NPY_DISABLE_CPU_FEATURES=X86_V4 OPENBLAS_CORETYPE=Haswell python3 -m pytest   # the second SIMD path
```

## Starting a session

Read this file, `CORE.md`, `derived/README.md`, `STANDARD.md`, `TERMS.md`, `RELATED.md`, `NOTES.md` and
`ontologies/README.md`. Then,
on `main`, read `70 Project/NOTES_claude.md` §1: the failure modes of
past sessions, each with its evidence.

## License

GNU Affero General Public License v3.0 — see `LICENSE`.

# std-alignment-framework — v7.7

[![checks](https://github.com/gianluca-calcagni/std-alignment-framework/actions/workflows/checks.yml/badge.svg)](https://github.com/gianluca-calcagni/std-alignment-framework/actions/workflows/checks.yml)

A standard formal framework for alignment problems in general, not only in machine learning: AI systems,
humans, institutions and organisms. The aim is a framework that is:
- solid enough to build on;
- substrate-independent;
- easy to import existing theorems into;
- able to make testable predictions, support diagnostics, and show its own limits.

The framework is an Obsidian vault of typed, linked notes. Every result links what it depends on, what uses it,
the checks that verify it, and its sources, and the tools keep those links derived and exhaustive.

## Reading it

- **In Obsidian.** Open this folder as a vault and start at `00 Home.md`.
- **On GitHub.** The notes use `[[wiki-links]]`, which GitHub does not follow. The linear views in `build/`
  read top to bottom: `core.md`, `dictionary.md`, `boundary.md`, `status.md`, `references.md`.
- **Where things are.** Current position and next steps: `70 Project/ROADMAP.md`. What is claimed, and how
  strongly: `60 Status/`. Everything retracted, and why: `60 Status/retractions/`. The bibliography:
  `references.bib`.

## Tools

| Command | Does |
|---|---|
| `python3 tools/vault.py sync` | recompute every derived field and generated section, after any edit |
| `python3 tools/vault.py lint` | schema, links, dependency cycles, definition order, actor-model tags, the measurement/explanation layers, checks and sources, table well-formedness, the bibliography's one-to-one match with the source notes, the hashes of frozen files (`tools/frozen.json`), and version banners (the current version stated consistently; no part's banner older than its own text); must report 0 errors |
| `python3 tools/vault.py migration-check` | re-prove the one-time migration: a fresh build from `archive/v6.6_flat/` reproduces all 19 flat files |
| `python3 tools/vault.py compile --check archive/v6.6_flat` | compare the live vault with v6.6. Every difference should be an edit logged in the hygiene log (Status §5) |
| `python3 tools/vault.py deps "Thm 13"` · `scan A3` | dependency queries, and the scan for a refactor step |
| `python3 verify.py [V1 …]` · `python3 final_audit.py` | numerical checks; each block has a note in `40 Checks/` |
| `python3 tools/reproduce.py verify V1 …` · `audit` | rerun checks and compare them with the committed reference outputs |

Install the pinned environment with `pip install -r requirements.txt` (Python 3.11). The reference outputs
`verify_output.txt` and `final_audit_output.txt` were produced with exactly these versions.

The v6.6 flat files are frozen in `archive/v6.6_flat/`. The Alignment Subframework — the source of the five gaps and of
retraction rows 1–6 — is archived in `archive/alignment_subframework/`; ROADMAP §6 says what of it was dropped and why. The one-time migration is `tools/build_vault.py`.

## How the work proceeds

- **Continuous checks.** Every push and pull request runs `.github/workflows/checks.yml`:
  - the vault checks (lint, the migration check, the freshness of `build/`, cross-references, the bibliography);
  - all 39 `verify.py` blocks, in parallel, each compared with its reference output;
  - `final_audit.py`, compared with its reference output.

  Residual-scale digits (|x| ≤ 1e-9) may differ across machines. So may a few lines that measure numerical
  noise (finite differences, for instance), each with a declared tolerance and its reason in
  `tools/reproduce_tolerances.json`. Any other difference fails the run.
- **One roadmap step, one pull request.** The PI reviews the diff and merging accepts the step. Pre-registrations
  are committed and pushed before any computation, so the commit timestamp dates them.
- **Honesty rules.** A falsified prediction is recorded, not repaired. Retractions are never deleted. A property of
  the vault is claimed only if a lint rule enforces it.

## License

GNU Affero General Public License v3.0 — see `LICENSE`.

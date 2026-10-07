# Probes for cases not yet registered

Measurements made before a case is designed, such as the time a procedure takes on this machine (design rule 4,
`cases/README.md`). They compute nothing a test would use, and no result rests on them.

| Probe | For | What it measured (2026-10-07, 4 CPU threads) |
|---|---|---|
| `stopping_rule_timing.py` | `ROADMAP.md`, step 2 | one step of KL-regularized policy gradient on `lvwerra/gpt2-imdb`, scored by `lvwerra/distilbert-imdb`: `2.6` s at batch 16 and `3.8` s at batch 32; the gold, `lvwerra/bert-imdb`, `0.022` s per sample; loading the three models `13` s once downloaded (`159` s with the download). So a sweep of 6 values of `β` × 3 seeds × 500 steps at batch 32 takes about `9.5` hours here, and 5 × 2 × 400 about `4.2` hours |

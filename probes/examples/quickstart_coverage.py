"""How often the intervals of examples/quickstart.py cover the simulated assistant's own values.

Runs the quickstart's own procedure (`estimates`, with its 300 bootstrap resamples) on 400 samples of the assistant,
each with its own seed, none the quickstart's, and counts for every reported quantity how often its interval covers the
value computed from the assistant itself. With 400 runs, a coverage of 95% is measured to about one percentage point.
For the bootstrap intervals it also counts the basic interval, the percentile interval reflected about the estimate,
(max(2·θ̂ − hi, 0), 2·θ̂ − lo), which undoes the bias when the estimate's distribution is symmetric.
Takes about ten minutes on 4 CPU threads.

Usage: python3 probes/examples/quickstart_coverage.py
"""
import sys
from multiprocessing import Pool
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT), str(ROOT / "examples")]
import stdalign as sa                                                                # noqa: E402
import quickstart as qs                                                              # noqa: E402

RUNS = 400


def truth():
    p = qs.assistant()
    a = sa.assess(p, qs.Q, qs.F)
    unexplained, named = sa.named_split(p, qs.Q, qs.F, [qs.FLATTERY])
    least, most = sa.uncertain_target_interval(p, qs.Q, np.vstack([qs.F, qs.FLATTERY]))
    U, mp, mt = sa.inner_split(p, qs.Q, qs.F, qs.FH)
    return {"misalignment": a.misalignment, "departure": a.departure, "pursuit part": a.pursuit_part,
            "unexplained": unexplained, "named": named, "least over the targets": least,
            "largest over the targets": most, "strict inner": U, "principal's part": mp, "trainer's part": mt}


def one(seed):
    rng = np.random.default_rng([20261010, seed])
    counts = rng.multinomial(qs.N, qs.assistant())
    est, _, point, spread = qs.estimates(counts, rng)
    return {"misalignment": (est.value, *est.interval), **{k: (point[k], *spread[k]) for k in point}}


if __name__ == "__main__":
    t = truth()
    with Pool(4) as pool:
        runs = pool.map(one, range(RUNS))
    print(f"{RUNS} runs of the quickstart's procedure, {qs.N} draws each")
    print(f"{'quantity':26s} {'value':>8s} {'bias':>8s} {'sd':>7s} {'covered':>8s} {'basic':>7s}")
    for k, v in t.items():
        x = np.array([r[k] for r in runs])
        cover = np.mean((x[:, 1] <= v) & (v <= x[:, 2]))
        basic = np.mean((np.maximum(2 * x[:, 0] - x[:, 2], 0) <= v) & (v <= 2 * x[:, 0] - x[:, 1]))
        print(f"{k:26s} {v:8.4f} {x[:, 0].mean() - v:+8.4f} {x[:, 0].std():7.4f} {cover:8.3f} "
              f"{'' if k == 'misalignment' else f'{basic:7.3f}'}")

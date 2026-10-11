"""What [P55]'s test certifies when decisions are not independent, for the reread before v13's pull request (NOTES.md
§19). Exploratory, not a check.
Usage: python3 probes/review/p55_dependence.py

The specification {q}, q = (1/2, 1/2) on two outcomes, so M(s) = KL(s‖q); the test of [P55](ii) at α = 0.05.
copy        An actor whose every decision copies its first, drawn from q: its average behaviour is q, yet its counts sit on
            one outcome, so n·M(p̂_n) = n·log 2. The least n from which the test accuses it at every record.
markov      A stationary Markov chain with average behaviour q that keeps its outcome with probability 0.9: the share of
            records of 200 decisions the test accuses, in 20,000 records. Seed 12345.
drift       Independent decisions whose marginals alternate between (0.8, 0.2) and (0.2, 0.8), average q: the same share,
            which the Notes of [P55] bound by α. And, for reference, independent decisions from q.
A few seconds.
"""
from math import comb, log
import numpy as np

N, ALPHA, RUNS = 200, 0.05, 20000


def n_misalignment(ones, n):
    s = np.array([n - ones, ones]) / n
    with np.errstate(divide="ignore", invalid="ignore"):
        return n * np.where(s > 0, s * np.log(s / 0.5), 0.0).sum()


def threshold(n):
    return log(comb(n + 1, 1) / ALPHA)                          # log(k_n/α), with k_n = n + 1 for two outcomes


def main():
    least = next(m for m in range(1, 1000) if all(k * log(2) >= threshold(k) for k in range(m, 1000)))
    print(f"copy: accused at every record from n = {least} on (n·log 2 ≥ log((n + 1)/α))")
    rng = np.random.default_rng(12345)
    accused = 0
    for _ in range(RUNS):
        x = rng.integers(2); ones = 0
        for i in range(N):
            if i and rng.random() >= 0.9:
                x = 1 - x
            ones += x
        accused += n_misalignment(ones, N) >= threshold(N)
    print(f"markov: accused in {accused / RUNS:.3f} of records of {N}, at α = {ALPHA}")
    marginals = np.where(np.arange(N) % 2 == 0, 0.2, 0.8)
    ones = (rng.random((RUNS, N)) < marginals).sum(axis=1)
    print(f"drift: accused in {np.mean([n_misalignment(o, N) >= threshold(N) for o in ones]):.4f} of records")
    ones = rng.binomial(N, 0.5, size=RUNS)
    print(f"independent from q: accused in {np.mean([n_misalignment(o, N) >= threshold(N) for o in ones]):.4f}")


if __name__ == "__main__":
    main()

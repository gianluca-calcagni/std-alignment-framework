"""The threshold of [P55]'s test from counts against the one NOTES.md §39.3 gives the same counts under any dependence
(§40, Q82). Exploratory, not a check. Usage: python3 probes/review/q82_thresholds.py        (instant)

[P55](ii) declares misalignment when n·M(p̂_n) ≥ log(k_n/α), k_n the number of empirical behaviours of n decisions on
d outcomes; its level holds for a sample. §39.3's mixture bet convicts whenever n·M_A(p̂_n) ≥ log(1/α) + d·log(n + 1)
+ 1, for a convex closed set with every outcome allowed, and its level holds when each decision, given the past, is
drawn from an acceptable behaviour. Both in nats, at α = 0.05.
"""
import math

if __name__ == "__main__":
    print(f"{'d':>3s} {'n':>6s} {'[P55]':>8s} {'§39.3':>8s} {'ratio':>6s}")
    for d, n in ((2, 100), (2, 1600), (3, 100), (3, 1000), (5, 1000), (10, 10000)):
        a = math.log(math.comb(n + d - 1, d - 1) / 0.05)
        b = math.log(1 / 0.05) + d * math.log(n + 1) + 1
        print(f"{d:3d} {n:6d} {a:8.2f} {b:8.2f} {b / a:6.2f}")

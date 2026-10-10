"""Johnson and Huo's Eq. 2 against their own one-head toy (NOTES.md §14, RELATED.md).

The toy: the conversation is a sequence of symbol vectors; the context vector is the attention-weighted mean of them, with
the last symbol as the query and weights exp(query·symbol / T); the next symbol is B or D, whichever has the larger dot
product with the context. Starting from a prompt A with A·B > A·D and B·D > B·B, the output is B for a while and then
tips to D. Eq. 2 says after how many B's: n* = ceil[(A·B − A·D)·exp(A·B/T) / ((B·D − B·B)·exp(B·B/T))]. This probe
draws random instances and compares the formula with the simulated head.

Usage: python3 probes/related/attention_tipping_toy.py
"""
import numpy as np

T, DIM, DRAWS, SEED = 0.5, 4, 2000, 0


def simulated(A, B, D, nmax=10000):
    seq = [A]
    for n in range(nmax):
        query = seq[-1]
        keys = np.array(seq)
        w = np.exp(keys @ query / T)
        c = (w / w.sum()) @ keys
        if c @ D > c @ B:
            return n
        seq.append(B)
    return None


def formula(A, B, D):
    return max(0, int(np.ceil((A @ B - A @ D) * np.exp(A @ B / T) / ((B @ D - B @ B) * np.exp(B @ B / T)))))


if __name__ == "__main__":
    rng = np.random.default_rng(SEED)
    agree = total = 0
    for _ in range(DRAWS):
        A, B, D = rng.normal(size=(3, DIM)) * 0.6
        if not (A @ B > A @ D and B @ D > B @ B):              # the delayed-tipping regime the paper describes
            continue
        s, f = simulated(A, B, D), formula(A, B, D)
        if s is None or f > 5000:
            continue
        total += 1
        agree += abs(s - f) <= 1
    print(f"Eq. 2 within one step of the simulated head in {agree} of {total} instances")

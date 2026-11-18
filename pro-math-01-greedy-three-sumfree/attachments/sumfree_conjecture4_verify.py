#!/usr/bin/env python3
"""Finite certificates for greedy strict 3-sumfree seeds (1, d-1, 2*d-1).

Run: python3 sumfree_conjecture4_verify.py
Standard library only; no network, randomness, or parallel workers.

For d=3,4,5 the finite certificates below, together with Lemma 7 of
van Berkel--Bosma, arXiv:2609.16843v2, prove the displayed infinite
periodic descriptions. Each certificate is checked both by enumerating
all distinct triples in its proposed finite set and by an independent
online greedy generator.

For d>=6 the accompanying symbolic proof gives the exact set
  {1,d-1,4*d-1} union [2*d-1,3*d-2]
  union {k*(8*d-3)+r : k>=1, 2*d-2<=r<=3*d-3}.
The sample checks here are consistency checks, not the all-d proof.

Correct least characteristic/gap periods:
  d=3: 5/1; d=4: 27/3; d=5: 104/10; d>=6: (8*d-3)/d.
"""

from itertools import combinations


# d, K, M, Q, prefix E in [1,K], base block B in (K,K+M]
CASES = (
    (3, 7, 5, 9, (1, 2, 5, 6, 7), (11,)),
    (4, 15, 27, 8, (1, 3, 7, 8, 9, 10, 15), (29, 35, 36)),
    (5, 79, 104, 8,
     (1, 4, 9, 10, 11, 12, 13, 19, 37, 45, 46, 72, 79),
     (80, 81, 114, 115, 116, 123, 149, 150, 158, 176)),
)


def greedy_prefix(d, limit):
    """Bit j of the three bitsets records sums of 1,2,3 distinct terms.

    Updating in descending subset size prevents reusing the new term.
    Bits above limit may be discarded since all terms are positive.
    """
    mask = (1 << (limit + 1)) - 1
    one = two = three = 0
    answer = []

    def add(x):
        nonlocal one, two, three
        three = (three | (two << x)) & mask
        two = (two | (one << x)) & mask
        one |= 1 << x
        answer.append(x)

    for x in (1, d - 1, 2 * d - 1):
        add(x)
    for x in range(2 * d, limit + 1):
        if not ((three >> x) & 1):
            add(x)
    return answer


def verify_certificate(case):
    d, K, M, Q, E, B = case
    H = K + Q * M
    assert K >= 2 * d - 1
    assert B and all(K < b <= K + M for b in B)
    assert all(1 <= a <= K for a in E)
    assert (Q - 6) * M >= 2 * K

    A = set(E) | {b + j * M for b in B for j in range(Q)}
    assert all(1 <= a <= H for a in A)
    assert {a for a in A if a <= 2 * d - 1} == {1, d - 1, 2 * d - 1}
    T = {x + y + z for x, y, z in combinations(sorted(A), 3)}
    for n in range(2 * d, H + 1):
        # Positivity ensures any representation of n uses terms < n.
        assert (n in A) == (n not in T), (d, n)

    # Independent online implementation, as a check on transcription.
    assert greedy_prefix(d, H) == sorted(A)
    accepted = sum(n in A for n in range(2 * d, H + 1))
    rejected = H - (2 * d - 1) - accepted
    print(f"CERTIFIED d={d}: K={K}, M={M}, Q={Q}, H={H}, "
          f"terms={len(A)}, admitted={accepted}, rejected={rejected}")


def general_candidate(d, limit):
    assert d >= 6
    M = 8 * d - 3
    A = {1, d - 1, 4 * d - 1} | set(range(2 * d - 1, 3 * d - 1))
    for k in range(1, limit // M + 1):
        A.update(k * M + r for r in range(2 * d - 2, 3 * d - 2)
                 if k * M + r <= limit)
    return sorted(a for a in A if a <= limit)


def main():
    for case in CASES:
        verify_certificate(case)
    for d in (6, 7, 8, 12, 24):
        H = 9 * (8 * d - 3)
        assert greedy_prefix(d, H) == general_candidate(d, H), d
        print(f"SAMPLE CHECK d={d}: matched through H={H}")
    print("All finite certificates and sample checks passed.")


if __name__ == "__main__":
    main()

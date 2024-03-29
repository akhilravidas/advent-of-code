#!/usr/bin/env python
import sys
from collections import defaultdict

with open(sys.argv[1]) as fp:
    inp = fp.read().strip().split("\n")

times = list(map(int, inp[0].split(":")[1].strip().split()))
distances = list(map(int, inp[1].split(":")[1].strip().split()))


def solve(t, d):
    # n * (t - n) >= d
    lo = 0
    hi = int((t + 1) / 2)
    while lo < hi:
        mid = int((lo + hi) / 2)
        if mid * (t - mid) > d:
            hi = mid
        else:
            lo = mid + 1
    g1 = lo
    if g1 * (t - g1) < d:
        return 0

    lo = int((t + 1) / 2)
    hi = t
    while lo < hi:
        # print("l2", lo, hi)
        mid = int((lo + hi + 1) / 2)
        if mid * (t - mid) > d:
            lo = mid
        else:
            hi = mid - 1

    g2 = lo
    print(g1, g2)

    assert g2 * (t - g2) > d
    return g2 - g1 + 1


mul = 1

for t, d in zip(times, distances):
    print(solve(t, d))
    mul *= solve(t, d)

print(mul)

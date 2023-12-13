#!/usr/bin/env python
import sys
from collections import defaultdict

with open(sys.argv[1]) as fp:
    inp = fp.read().strip().split("\n")


def h_count(pat):
    res = []
    L = len(pat)
    for x in range(0, L):
        found = True
        once = False
        for j in range(0, x + 1):
            once = True
            if x + j - 1 < L and pat[x - j] != pat[x + j - 1]:
                found = False

        if found and once:
            res.append(x)

    return res


def v_count(pat):
    pat = list(zip(*pat))
    return h_count(pat)


def process(inp):
    cur = []
    res = []
    for line in inp:
        if line.strip():
            cur.append(line)
        else:
            res.append(cur)
            cur = []
    if cur:
        res.append(cur)
    return res


res = 0
for pat in process(inp):
    v = v_count(pat)
    h = h_count(pat)
    res += sum(v) + 100 * (sum(h))

print(res)

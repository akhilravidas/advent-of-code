#!/usr/bin/env python
import sys
from collections import defaultdict

with open(sys.argv[1]) as fp:
    inp = fp.read().strip().split("\n")


def cnt_mismatch(a, b):
    return sum(1 for x, y in zip(a, b) if x != y)


def h_count(pat):
    res = []
    L = len(pat)
    for x in range(0, L):
        miss = 0
        once = False
        for j in range(0, x + 1):
            once = True
            if x + 1 + j < L and pat[x - j] != pat[x + 1 + j]:
                miss += cnt_mismatch(pat[x - j], pat[x + j + 1])

        if miss == 1 and once:
            res.append(x + 1)

    return res


def v_count(pat):
    pat = list(zip(*pat))
    pat = list(map(lambda x: "".join(x), pat))
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
    print(v, h)

    res += sum(v) + 100 * (sum(h))

print(res)

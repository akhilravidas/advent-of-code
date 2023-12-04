#!/usr/bin/env python
import sys

inp = open(sys.argv[1]).read().strip().split("\n")

res = 0

for row in inp:
    _, y = row.split(":")
    a, b = y.split("|")
    good = set(int(x) for x in a.split())
    gg = set(int(x) for x in b.split())
    cnt = len(gg & good)
    if cnt > 0:
        res += 2 ** (cnt - 1)

print(res)

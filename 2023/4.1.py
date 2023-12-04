#!/usr/bin/env python
import sys

inp = open(sys.argv[1]).read().strip().split("\n")

res = 0

for row in inp:
    _, y = row.split(":")
    y = y.strip()
    a, b = y.split("|")
    a.strip()
    b.strip()
    good = set(int(x) for x in a.split(" ") if len(x))
    cnt = 0
    gg = [int(x) for x in b.split(" ") if len(x)]
    for num in gg:
        if num in good:
            cnt += 1
    if cnt > 0:
        res += 2 ** (cnt - 1)

print(res)

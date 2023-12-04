#!/usr/bin/env python
import sys

inp = open(sys.argv[1]).read().strip().split("\n")

copies = [1] * len(inp)

for idx, row in enumerate(inp):
    _, y = row.split(":")
    a, b = y.split("|")
    good = set(int(x) for x in a.split())
    gg = set(int(x) for x in b.split())
    cnt = len(gg & good)
    for j in range(cnt):
        if idx + j + 1 < len(copies):
            copies[idx + j + 1] += copies[idx]

print(sum(copies))

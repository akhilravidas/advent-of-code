#!/usr/bin/env python
import sys
from collections import defaultdict

with open(sys.argv[1]) as fp:
    inp = fp.read().strip().split("\n")

pat = inp[0]

left = {}
right = {}

for row in inp[2:]:
    x, _, l, r = row.split()
    left[x] = l[1:-1]
    right[x] = r[:-1]

print(left, right)

cur = "AAA"
for i in range(1000000):
    if cur == "ZZZ":
        print(i)
        break
    if pat[i % len(pat)] == "L":
        cur = left[cur]
    else:
        cur = right[cur]

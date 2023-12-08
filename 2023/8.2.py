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

cur = [k for k in left.keys() if k[-1] == "A"]

print(len(cur))
for i in range(1000000000):
    nxt = []
    for c in cur:
        if pat[i % len(pat)] == "L":
            nxt.append(left[c])
        else:
            nxt.append(right[c])

    cur = nxt
    if all([x.endswith("Z") for x in nxt]):
        print(i + 1)
        break

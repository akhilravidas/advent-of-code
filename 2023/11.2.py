#!/usr/bin/env python
import sys
from collections import Counter, defaultdict

with open(sys.argv[1]) as fp:
    inp = fp.read().strip().split("\n")

FACTOR = 1000000


def expand(grid):
    rows = []
    for idx, row in enumerate(grid):
        if all(c == "." for c in row):
            rows.append(idx)

    cols = []
    idx = 0
    while idx < len(grid[0]):
        if all(row[idx] == "." for row in grid):
            cols.append(idx)
        idx += 1
    return rows, cols


grid = inp
rows, cols = expand(inp)


st = []

for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] != ".":
            st.append((r, c, grid[r][c]))


def count(rows, r1, r2):
    mr = min(r1, r2)
    mx = max(r1, r2)
    return len([r for r in rows if mr <= r <= mx])


print("Total = ", len(st))

res = 0
for i in range(len(st)):
    for j in range(i + 1, len(st)):
        r1, c1, _ = st[i]
        r2, c2, _ = st[j]

        res += (
            abs(r1 - r2)
            + abs(c1 - c2)
            + (count(rows, r1, r2) + count(cols, c1, c2)) * (FACTOR - 1)
        )

print(res)

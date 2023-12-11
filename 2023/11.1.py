#!/usr/bin/env python
import sys
from collections import Counter, defaultdict

with open(sys.argv[1]) as fp:
    inp = fp.read().strip().split("\n")


def expand(grid):
    new_grid = []
    for row in grid:
        if all(c == "." for c in row):
            new_grid.append(row)
        new_grid.append(row)

    idx = 0
    while idx < len(new_grid[0]):
        if all(row[idx] == "." for row in new_grid):
            R = len(new_grid)
            C = len(new_grid[0])
            for r in range(R):
                new_grid[r] = new_grid[r][:idx] + ".." + new_grid[r][idx + 1 :]
            idx += 1
        idx += 1
    return new_grid


new_grid = expand(inp)

st = []

for r in range(len(new_grid)):
    for c in range(len(new_grid[0])):
        if new_grid[r][c] != ".":
            st.append((r, c, new_grid[r][c]))


print("Total = ", len(st))

res = 0
for i in range(len(st)):
    for j in range(i + 1, len(st)):
        r1, c1, _ = st[i]
        r2, c2, _ = st[j]
        res += abs(r1 - r2) + abs(c1 - c2)

print(res)

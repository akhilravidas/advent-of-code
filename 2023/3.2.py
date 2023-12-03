import sys
from collections import defaultdict

grid = open(sys.argv[1]).read().strip().split("\n")


def is_gear(grid, r, c):
    if r < 0 or c < 0:
        return False

    if r >= len(grid) or c >= len(grid[r]):
        return False

    ch = grid[r][c]
    return ch == "*"


res = 0

adj = defaultdict(list)

for r, row in enumerate(grid):
    c = 0
    while c < len(row):
        if row[c].isdigit():
            n = 0
            nearby_gears = set()
            while c < len(row) and row[c].isdigit():
                n = n * 10 + int(row[c])
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        if is_gear(grid, r + dr, c + dc):
                            nearby_gears.add((r + dr, c + dc))
                c += 1
            for g in nearby_gears:
                adj[g].append((r, c, n))

        else:
            c += 1


for gear, neighs in adj.items():
    print(gear, neighs)
    if len(neighs) == 2:
        _, _, num1 = neighs[0]
        _, _, num2 = neighs[1]
        res += num1 * num2

print(res)

from base import *
from d10 import knot_hash

inp = "nbysizxe"

def go(grid, r, c, seen):
    if r < 0 or r >= len(grid):
        return
    if c < 0 or c >= len(grid[0]):
        return

    if (r, c) in seen:
        return

    seen.add((r, c))
    if grid[r][c] == '0':
        return

    for d in dir_4:
        go(grid, r + d[0], c + d[1], seen)

def solve(inp):
    def to_bin(x):
        x = int(x, 16)
        return '{0:04b}'.format(x)

    cnt  = 0
    grid = []
    for i in range(0, 128):
        res = ''
        row = inp + '-' + str(i)
        k = knot_hash(row)
        # convert to binary
        res = ''.join(map(to_bin, k))
        grid.append(res)
        cnt += sum(int(c) for c in res)

    seen = set()
    components = 0
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] == '1' and (i, j) not in seen:
                components += 1
                go(grid, i, j, seen)

    print 'Components:', components
    return cnt


print solve(inp)
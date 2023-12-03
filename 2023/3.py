import sys

grid = open(sys.argv[1]).read().strip().split("\n")


def is_symbol(grid, r, c):
    if r < 0 or c < 0:
        return False

    if r >= len(grid) or c >= len(grid[r]):
        return False

    ch = grid[r][c]
    return not ch.isdigit() and ch != "."


res = 0

for r, row in enumerate(grid):
    c = 0
    while c < len(row):
        if row[c].isdigit():
            ff = False
            n = 0
            while c < len(row) and row[c].isdigit():
                n = n * 10 + int(row[c])
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        ff = ff or is_symbol(grid, r + dr, c + dc)
                c += 1
            if ff:
                res += n
        else:
            c += 1


print(res)

from base import *


inp = """     |          
     |  +--+    
     A  |  C    
 F---|--|-E---+ 
     |  |  |  D 
     +B-+  +--+ """.split("\n")
inp = read_lines()


dir_4 = [(-1, 0), (0, -1), (1, 0), (0, 1)]

states = set()
num_seen = 0

def go(grid, r, c, pr, pc, d_idx, seen):
    if (r, c, pr, pc, d_idx) in states or grid[r][c] == ' ':
        print (r, c, pr, pc, d_idx)
        return

    global num_seen
    num_seen += 1

    states.add((r, c, pr, pc, d_idx))
    print r, c, grid[r][c]
    dr = dir_4[d_idx][0]
    dc = dir_4[d_idx][1]
    R = len(grid)
    C = len(grid[0])
    if grid[r][c] in ('|', '-'):
        go(grid, r + dr, c + dc, r, c, d_idx, seen)
    elif grid[r][c] == '+':
        for idx in range(0, len(dir_4)):
            d = dir_4[idx]
            nr = r + d[0]
            nc = c + d[1]
            if nr != pr and nc != pc and nr >= 0 and nc >= 0 and nr < R and nc < C and grid[nr][nc] != ' ':
                go(grid, nr, nc, r, c, idx, seen)
    else:
        seen.append(grid[r][c])
        go(grid, r + dr, c + dc, r, c, d_idx, seen)

def solve(inp):
    R = len(inp)
    C = len(inp[0])
    seen = []
    for i in range(0, C):
        if inp[0][i] == '|':
            go(inp, 0, i, -1, i, 2, seen)

    return ''.join(seen)

if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(1000000000)
    print solve(inp)
    print num_seen

# tried
# 16654
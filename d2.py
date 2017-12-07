from base import *

inp = read_int_2d()

def solve(inp):
    return sum(max(a) - min(a) for a in inp)

def solve2(inp):
    s = 0
    for i in range(0, len(inp)):
        row = inp[i]
        for j in range(0, len(row)):
            for k in range(j + 1, len(row)):
                a, b = row[j], row[k]
                if a > b:
                    a, b = b, a

                if b % a == 0:
                    s += b / a
                    break
    return s

print solve(inp)
print solve2(inp)
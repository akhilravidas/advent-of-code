from base import *

inp = read_strings().strip()

def solve(inp):
    s = 0
    l = len(inp)
    for i in range(0, l):
        if inp[i] == inp[(i+l/2) % l]:
            s += int(inp[i])
    return s

print solve("1122")
print solve("1111")
print solve("1234")
print solve("91212129")
print solve(inp)
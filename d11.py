from base import *


inp = read_string()

def incr(d):
    if d == 'n':
        return (1, -1, 0)
    if d == 's':
        return (-1, 1, 0)
    if d == 'nw':
        return (0, -1, 1)
    if d == 'ne':
        return (1, 0, -1)
    if d == 'sw':
        return (-1, 0, 1)
    if d == 'se':
        return (0, 1, -1)
    assert False


def solve(inp):
    mx = 0
    parts = inp.split(',')
    x, y, z = 0, 0, 0
    for p in parts:
        c = incr(p)
        x += c[0]
        y += c[1]
        z += c[2]

        away = (abs(x) + abs(y) + abs(z)) / 2
        if away > mx:
            mx = away

    return (abs(x) + abs(y) + abs(z)) / 2, mx

print solve("ne,ne,ne")
print solve("ne,ne,sw,sw")
print solve("ne,ne,s,s")
print solve("se,sw,se,sw,sw")
print solve(inp)
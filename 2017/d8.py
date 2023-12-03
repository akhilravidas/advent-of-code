from base import *

inp = read_lines()

vals = defaultdict(int)

def operate(op, v, t):
    t = int(t)
    c = vals[v]  
    if op == '!=':
        return c != t
    elif op == '==':
        return c == t
    elif op == '<':
        return c < t
    elif op == '>':
        return c > t
    elif op == '>=':
        return c >= t
    elif op == '<=':
        return c <= t
    else:
        assert False, op


def solve(inp):
    mx = -1000000000
    for line in inp:
        parts = line.split()
        name, inc, by, ifs, v, op, val = parts
        if operate(op, v, val):
            if inc == "inc":
                multiplier = 1
            else:
                multiplier = -1
            vals[name] = vals[name] + multiplier * int(by)
            if mx < vals[name]:
                mx = vals[name]
    return mx

print solve(inp)
print d_sorted_by_vals(vals)
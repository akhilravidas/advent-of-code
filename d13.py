from base import *

inp = read_lines()

def solve(inp):
    mx = 0
    a = []
    for l in inp:
        n, r = l.split(':')
        r = int(r.strip())
        n = int(n)
        mx = max(mx, n)
        a.append((n, r))

    period = [0] * (mx + 1)
    for b in a:
        period[b[0]] = 2 * b[1] - 2

    res = 1
    delay_by = 0
    found = False
    while True:
        my_pos = 0
        res = 0
        bad = False
        while my_pos <= mx and bad == False:
            if ranges[my_pos] != 0: 
                rem = (my_pos + delay_by) % period[my_pos]
                if rem == 0: 
                    bad = True
                    break
            my_pos += 1

        if my_pos > mx and not bad:
            return delay_by
        delay_by += 1

    return delay_by
    


print solve(inp)
inp = """0: 3
1: 2
4: 4
6: 4""".split('\n')
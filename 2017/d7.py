from base import *

lines = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)""".split('\n')

lines = read_lines()

not_root = defaultdict(bool)
edges = defaultdict(list)
wts = {}

every = set()
for l in lines:
    p = l.split()
    node = p[0]
    wt = int(p[1][1:-1])
    every.add(l.split()[0])
    wts[node] = wt
    if '->' in l:
        pos = l.find('->')
        m = map(lambda x: x.strip(), l[pos + 3:].split(','))
        for k in m:
            not_root[k] = True
            edges[node].append(k)

def go(n):
    child_wts = {}
    for k in edges[n]:
        child_wts[k] = go(k)

    s = 0
    vals = child_wts.values()
    if len(set(vals)) > 1:
        d = histogram(vals)
        assert len(d) == 2
        d_s = d_sorted_by_vals(d)
        bad, good = d_s[0][0], d_s[1][0]
        # Find the child corresponding to bad
        x = d_find_val(child_wts, bad)[0]
        print "Fix:", x, bad, good, wts[x]
        dlog(x, bad, good, wts[x])
        s = len(child_wts) * good
    else:
        s = len(child_wts) * (vals[0] if len(vals) else 0)

    return wts[n] + s

root = None
for e in every:
    if not not_root[e]:
        root = e

print go(root)
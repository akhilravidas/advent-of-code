from base import *

inp = read_lines()


def construct(inp):
    adj = defaultdict(list)
    for l in inp:
        node, neig = map(lambda x: x.strip(), l.split('<->'))
        parts = neig.split(',')
        for n in parts:
            n = n.strip()
            adj[node].append(n)
            adj[n].append(node)
    return adj

def go(seen, adj, cur):
    if cur not in seen:
        seen.add(cur)
        for n in adj[cur]:
            go(seen, adj, n)

def solve(inp):
    pass

adj = construct(inp)
seen = set()
total = 0
for k in adj:
    if k not in seen:
        total += 1
        go(seen, adj, k) 
# go(seen, adj, "0")
print total

# print len(seen)
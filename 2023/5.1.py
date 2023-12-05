#!/usr/bin/env python
import sys
from collections import defaultdict

with open(sys.argv[1]) as fp:
    inp = fp.read().strip().split("\n")


seeds = list(map(int, inp[0][len("seeds: ") :].strip().split(" ")))

cur = seeds.copy()


idx = 2

maps = []
while idx < len(inp):
    print("idx", idx)
    if ":" in inp[idx]:
        map_name = inp[idx][:-1]
        src, dest = map_name.split("-to-")
        idx += 1
        cur_map = []
        while idx < len(inp) and inp[idx].strip() != "":
            dest_start, src_start, cnt = list(map(int, inp[idx].split(" ")))
            cur_map.append((src, dest, dest_start, src_start, cnt))
            idx += 1

        print(cur_map)

        nxt = cur.copy()
        for r_idx, s in enumerate(cur):
            for _, _, dest_start, src_start, cnt in cur_map:
                if s >= src_start and s < src_start + cnt:
                    nxt[r_idx] = dest_start + s - src_start
        print(nxt)
        cur = nxt
    idx += 1


print(min(cur))

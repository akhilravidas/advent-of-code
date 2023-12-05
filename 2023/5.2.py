#!/usr/bin/env python
import sys
from collections import defaultdict

with open(sys.argv[1]) as fp:
    inp = fp.read().strip().split("\n")


seeds = list(map(int, inp[0][len("seeds: ") :].strip().split(" ")))
assert len(seeds) % 2 == 0

interesting_ranges = []
for i in range(0, len(seeds), 2):
    interesting_ranges.append((seeds[i], seeds[i] + seeds[i + 1] - 1))

interesting_ranges = sorted(interesting_ranges, key=lambda x: x[0])


def map_function(seed_st, seed_en, map_st, map_en):
    # first intersect
    st = max(seed_st, map_st)
    en = min(seed_en, map_en)
    if st > en:
        return None, (seed_st, seed_en)

    st1 = seed_st
    en1 = st - 1

    st2 = en + 1
    en2 = seed_en

    return (st, en), [(st1, en1), (st2, en2)]


def _valid(l):
    return [x for x in l if x[0] <= x[1]]


idx = 2
maps = []
while idx < len(inp):
    if ":" in inp[idx]:
        map_name = inp[idx][:-1]
        src, dest = map_name.split("-to-")
        idx += 1
        cur_map = []
        while idx < len(inp) and inp[idx].strip() != "":
            dest_start, src_start, cnt = list(map(int, inp[idx].split(" ")))
            cur_map.append((dest_start, src_start, cnt))
            idx += 1

        qq = interesting_ranges.copy()
        nxt_ranges = []
        while len(qq) > 0:
            st, en = qq.pop(0)
            mtch = False
            for dest_st, src_st, cnt in cur_map:
                offset = dest_st - src_st
                new_range, splits = map_function(st, en, src_st, src_st + cnt - 1)
                if new_range is None:
                    continue
                else:
                    mtch = True
                    qq.extend(_valid(splits))
                    nxt_ranges.append((new_range[0] + offset, new_range[1] + offset))
            if not mtch:
                nxt_ranges.append((st, en))

        interesting_ranges = nxt_ranges.copy()
        interesting_ranges = sorted(interesting_ranges, key=lambda x: x[0])

    idx += 1

print(interesting_ranges[0][0])

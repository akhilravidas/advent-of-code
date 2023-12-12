#!/usr/bin/env python
import sys
from collections import defaultdict

with open(sys.argv[1]) as fp:
    inp = fp.read().strip().split("\n")

# damaged = #
# operational = .


def go(r_num, x, pos, nums, n_idx, cur_run, constructed, cache={}):
    if pos == len(x):
        return n_idx == len(nums)
    if n_idx >= len(nums):
        if x[pos] in ("?", "."):
            return go(r_num, x, pos + 1, nums, n_idx, cur_run, constructed + ".", cache)
        else:
            return 0

    if cur_run > nums[n_idx]:
        return 0

    # look at x[pos]
    res = 0
    if x[pos] in ("#", "?"):
        # continue the run
        res += go(r_num, x, pos + 1, nums, n_idx, cur_run + 1, constructed + "#", cache)
    if x[pos] == (".", "?"):
        if cur_run == nums[n_idx]:
            res += go(r_num, x, pos + 1, nums, n_idx + 1, 0, constructed + "|", cache)
        if cur_run == 0:
            res += go(r_num, x, pos + 1, nums, n_idx, 0, constructed + ".", cache)

    cache[(r_num, pos, n_idx, cur_run)] = res
    return res


def solve(case_id, row):
    x, nums = row.split(" ")
    nums = list(map(int, nums.split(",")))
    print(nums)
    return go(case_id, x + ".", 0, nums, 0, 0, "")


res = 0

for idx, row in enumerate(inp):
    c = solve(idx, row)
    res += c
    print(c)

print(res)

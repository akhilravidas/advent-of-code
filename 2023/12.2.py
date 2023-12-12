#!/usr/bin/env python
import sys
from collections import defaultdict

with open(sys.argv[1]) as fp:
    inp = fp.read().strip().split("\n")

# damaged = #
# operational = .


def go(r_num, x, pos, nums, n_idx, cur_run, cache={}):
    if (r_num, pos, n_idx, cur_run) in cache:
        return cache[(r_num, pos, n_idx, cur_run)]
    if pos == len(x):
        return n_idx == len(nums)
    if n_idx == len(nums):
        if x[pos] in ("?", "."):
            res = go(r_num, x, pos + 1, nums, n_idx, cur_run, cache)
            cache[(r_num, pos, n_idx, cur_run)] = res
            return res
        else:
            return 0

    if n_idx > len(nums):
        return 0

    if cur_run > nums[n_idx]:
        return 0

    # look at x[pos]
    res = 0
    if x[pos] in ("#", "?"):
        # continue the run
        res += go(r_num, x, pos + 1, nums, n_idx, cur_run + 1, cache)
    if x[pos] in (".", "?"):
        if cur_run == nums[n_idx]:
            res += go(r_num, x, pos + 1, nums, n_idx + 1, 0, cache)
        if cur_run == 0:
            res += go(r_num, x, pos + 1, nums, n_idx, 0, cache)
    cache[(r_num, pos, n_idx, cur_run)] = res
    return res


def solve(case_id, row):
    x, nums = row.split(" ")
    nums = list(map(int, nums.split(",")))
    new_x = "?".join([x, x, x, x, x])
    return go(case_id, new_x + ".", 0, (nums * 5), 0, 0, {})


res = 0

for idx, row in enumerate(inp):
    c = solve(idx, row)
    res += c

print(res)

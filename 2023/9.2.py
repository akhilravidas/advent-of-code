#!/usr/bin/env python
import sys
from collections import defaultdict

with open(sys.argv[1]) as fp:
    inp = fp.read().strip().split("\n")


def solve(row):
    arr = [row]
    nums = row
    while True:
        if all(x == 0 for x in nums):
            break
        nxt = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]
        arr.append(nxt)
        nums = nxt

    arr[-1].insert(0, 0)
    idx = len(arr) - 2
    while idx >= 0:
        arr[idx].insert(0, arr[idx][0] - arr[idx + 1][0])
        idx -= 1
    return arr[0][0]


print(sum(solve([int(x) for x in row.split()]) for row in inp))

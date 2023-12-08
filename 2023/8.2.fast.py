#!/usr/bin/env python
import sys
from collections import defaultdict
from math import gcd

with open(sys.argv[1]) as fp:
    inp = fp.read().strip().split("\n")

pat = inp[0]

left = {}
right = {}

for row in inp[2:]:
    x, _, l, r = row.split()
    left[x] = l[1:-1]
    right[x] = r[:-1]

cur = [k for k in left.keys() if k[-1] == "A"]

nums = []

for c in cur:
    st = c
    seen = set()
    nn = []
    i = 0
    while True:
        if pat[i % len(pat)] == "L":
            st = left[st]
        else:
            st = right[st]

        if st.endswith("Z"):
            nn.append(i + 1)
            break

        i += 1

    nums.append(nn)


def lcm(arr):
    ans = arr[0]
    for i in arr[1:]:
        ans = ans * i // gcd(ans, i)
    return ans


print(nums)


def solve(idx, arr):
    if idx == len(nums):
        print(lcm(arr))
        return lcm(arr)

    x = None
    for n in nums[idx]:
        y = solve(idx + 1, arr + [n])
        if x is None or y < x:
            x = y
    return x


solve(0, [])

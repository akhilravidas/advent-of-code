#!/usr/bin/env python
import sys
from collections import defaultdict

with open(sys.argv[1]) as fp:
    inp = fp.read().strip().split("\n")


cards = list("23456789TJQKA")


def _freq(s):
    freq = defaultdict(int)
    for c in s:
        freq[c] += 1
    return freq


def _rank(word):
    f = _freq(word)
    values = sorted(f.values(), reverse=True)
    values += [0] * (5 - len(values))
    positions = [cards.index(x) for x in word]
    return values + positions


X = [x.split() for x in inp]
by_rank = sorted(X, key=lambda x: _rank(x[0]))
res = 0

for idx, (card, val) in enumerate(by_rank):
    res += int(val) * (idx + 1)

print(res)

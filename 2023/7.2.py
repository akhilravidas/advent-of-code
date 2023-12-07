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
    freqs = list(f.items())
    if "J" in word:
        j_freq = f["J"]
        for i in freqs:
            if i[0] == "J":
                freqs.remove(i)
    else:
        j_freq = 0

    if len(freqs) == 0:
        values = [0]
    else:
        values = sorted([x[1] for x in freqs], reverse=True)
    values[0] += j_freq
    values += [0] * (5 - len(values))
    positions = [cards.index(x) if x != "J" else -1 for x in word]
    return values + positions


X = [x.split() for x in inp]
by_rank = sorted(X, key=lambda x: _rank(x[0]))

# print(_rank("JJJJJ"))

res = 0
for idx, (card, val) in enumerate(by_rank):
    res += int(val) * (idx + 1)

print(res)

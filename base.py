from db import *
from trees import *
from collections import defaultdict
from copy import deepcopy
import time


# Input routines
def _reader(fn):
    with open("/Users/ar/Desktop/input.txt") as f:
        return fn(f)

read_string = lambda: _reader(lambda f: f.read().strip())
read_int_2d = lambda: _reader(lambda f: [map(int, s.split()) for s in f.readlines()])
read_int_vertical = lambda: _reader(lambda f: map(int, f.readlines()))
read_int_horizontal = lambda: _reader(lambda f: map(int, f.read().strip().  split()))
read_words = lambda: _reader(lambda f: map(lambda x: x.split(), f.readlines()))
read_lines = lambda: _reader(lambda f: f.readlines())

# returns g, x, y, st: x * b + y * n = g
def xgcd(b, n):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  b, x0, y0

def histogram(arr):
    d = defaultdict(int)
    for a in arr:
        d[a] += 1
    return d

# Dictionary functions
def d_sorted_by_vals(d, reverse=True):
    return sorted(d.iteritems(), key=lambda x: x[1], reverse=reverse)

def d_sorted_by_keys(d, reverse=True):
    return sorted(d.iteritems(), key=lambda x: x[0], reverse=reverse)

def d_max_value_key(d):
    mx = max(d.values())
    return [k for k, v in d.iteritems() if v == mx][0]

def d_find_val_all(d, reqd):
    return [(k, v) for k, v in d.iteritems() if d[k] == reqd]

def d_find_val(d, reqd):
    return d_find_val_all(d, reqd)[0]

def map_strip(arr):
    return map(lambda x: x.strip(), arr)

clone = deepcopy

# Grids
dir_4 = [(-1, 0), (0, -1), (1, 0), (0, 1)]
dir_8 = [(dr, dc) for dr in range(-1, 2) for dc in range(-1, 2) if dr != 0 or dc != 0]
from base import *

mask = (2 ** 16) - 1

def cmp(a, b):
    if (a & mask) == (b &mask):
        return 1
    return 0

def generate_seq(st, factor, m):
    last = st
    while True:
        while True:
            nxt = (last * factor) % 2147483647 
            last = nxt
            if nxt % m == 0:
                break
        yield nxt


def solve():
    a = 116
    b = 299
    a_f = 16807
    b_f = 48271
    times = 5 * (10 ** 6)
    a_seq = generate_seq(a, a_f, 4)
    b_seq = generate_seq(b, b_f, 8)
    return sum(cmp(a_seq.next(), b_seq.next()) for i in range(0, times))

if __name__ == "__main__":
    print solve()

from base import *

def reverse(inp, st, en):
    res = [-1] * len(inp)
    comb = []
    for i in range(st, st + len(inp)):
        idx = i % len(inp)
        comb.append(inp[idx])
        if idx == en:
            break
    rev = comb[::-1]
    for i in range(st, st + len(inp)):
        idx = i % len(inp)
        res[idx] = rev[i - st]
        if idx == en:
            break

    for i in range(0, len(inp)):
        if res[i] == -1:
            res[i] = inp[i]
    return res

def solve(cur_pos, skip_len, arr, inp):
    L = len(arr)
    for l in inp:
        st = cur_pos
        if l != 0:
            en = (cur_pos + l + L - 1) % L
            # print arr, 'l =', l, 'cur =', cur_pos, 'skip =', skip_len
            arr = reverse(arr, st, en)
        cur_pos = (cur_pos + l + skip_len) % L
        skip_len += 1
        # print '\t\t', arr
    # return arr[0] * arr[1]
    return cur_pos, skip_len, arr

# get the sequence

def p(inp):
    ans = [0] * (len(inp) / 16)
    # print inp
    for i in range(0, len(inp)):
        ans[i/16] = ans[i/16] ^ inp[i]

    # print ans

    return ''.join(
        map(lambda x: '%02x' % x, ans)
    )

def knot_hash(new_inp):
    c = s = 0
    inp = range(0, 256)
    lens = map(ord, new_inp) + [17, 31, 73, 47, 23]
    for rep in range(0, 64):
        c, s, inp = solve(c, s, inp, lens)
    return p(inp)


new_inp = read_string()
knot_hash(new_inp)


# print p(inp)

# print solve(0, 0, range(0, 256), lens)
# print solve(range(0, 5), [3, 4, 1, 5])
# print solve(range(0, 5), [3, 4])
# tried:
# 25440
# 8372
# 212
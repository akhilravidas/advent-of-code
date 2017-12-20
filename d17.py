from base import *

def solve(inp):
    buf = [0]
    nxt = 0
    cur_pos = 0
    ans = -1
    zero_pos = 0
    l = 1
    while nxt < 50000000:
        nxt += 1
        cur_pos += inp
        cur_pos %= l
        # insert nxt at cur_pos
        cur_pos += 1
        # buf.insert(cur_pos, nxt)
        if cur_pos == zero_pos + 1:
            ans = nxt
        
        if cur_pos <= zero_pos:
            zero_pos = zero_pos + 1

        l += 1

    return ans

if __name__ == "__main__":
    inp = 345
    print solve(inp)

# 1678
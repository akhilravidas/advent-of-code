from base import *

inp = read_string()
counter = 0 

def strip_garbage(l):
    global counter
    res = ''
    garbage = False
    prev_exc = False
    for idx in range(0, len(l)):
        c = l[idx]
        add = ''
        if garbage:
            if prev_exc:
                prev_exc = False
            else:
                if c == '!':
                    prev_exc = True
                elif c == '>':
                    garbage = False
                else:
                    counter += 1
        else:
            assert not prev_exc
            if c == '}':
                add = '}'
            elif c == '{':
                add = '{'
            elif c == '<':
                garbage = True
        res += add
    return res

    
def solve(s):
    res = 0
    cnt = 0
    for c in s:
        if c == '{':
            cnt += 1
            res += cnt

        if c == '}':
            cnt -=1

    return res


s = strip_garbage(inp)
print solve(s)

print counter
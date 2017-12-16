from base import *


def apply(ins, base):
    if ins[0] == 's':
        l = int(ins[1:])
        assert l > 0 and l < len(base)
        return base[len(base) - l:] + base[:len(base) - l]
    elif ins[0] == 'x':
        p1, p2 = ins[1:].split('/')
        p1 = int(p1)
        p2 = int(p2)
        assert p1 >= 0 and p1 < len(base)
        assert p2 >= 0 and p2 < len(base)
        base[p1], base[p2] = base[p2], base[p1]
        return base
    elif ins[0] == 'p':
        p1, p2 = ins[1:].split('/')
        p1 = ord(p1[0]) - ord('a')
        p2 = ord(p2[0]) - ord('a')
        assert p1 >= 0 and p1 < len(base)
        assert p2 >= 0 and p2 < len(base)
        pos1, pos2 = -1, -1
        for i in range(0, len(base)):
            if base[i] == p1:
                assert pos1 == -1
                pos1 = i
            if base[i] == p2:
                assert pos2 == -1
                pos2 = i

        assert pos1 != -1
        assert pos2 != -1
        base[pos1], base[pos2] = base[pos2], base[pos1]
        return base
    else:
        assert False

def solve(base, instructions):
    for instr in instructions:
        base = apply(instr, base)
    # return ''.join(chr(c + ord('a')) for c in base)
    return base


def brute_force(instructions, num_times):
    st = range(0, 16)
    while num_times > 0:
        num_times -= 1
        st = solve(st, instructions)

    return st

def encode(ans):
    return ''.join(chr(c + ord('a')) for c in ans)


def find_full_cycle(instructions):
    step = 0
    d = {}
    base = range(0, 16)
    while True:
        c = encode(base)
        if c not in d:
            d[c] = step
        else:
            assert encode(base) == encode(range(0, 16))
            return step - d[c]
        step += 1
        base = solve(base, instructions)

if __name__ == "__main__":
    inp = read_string()
    instructions = inp.split(',')
    ans = solve(range(0, 16), instructions)
    l = find_full_cycle(instructions)
    a1 = brute_force(instructions, 1000000000 % l)
    print encode(a1)
        
# output: glfndhpjcaoikemb
# output: hmadkfjegilpnboc
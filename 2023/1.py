import sys

sum = 0

digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

vals = {v: idx + 1 for idx, v in enumerate(digits)}


def get_d(line):
    digits = []
    idx = 0
    while idx < len(line):
        print(line[idx], line[idx].isdigit())
        if line[idx].isdigit():
            digits.append(int(line[idx]))
        for val_str, val in vals.items():
            print(line[idx:], val_str, line[idx:].startswith(val_str))
            if line[idx:].startswith(val_str):
                digits.append(val)
                idx += len(val_str)
                break
        else:
            idx += 1
    return digits


for line in sys.stdin:
    digits = get_d(line)
    sum += digits[0] * 10 + digits[-1]

print(sum)

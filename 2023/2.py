import sys
from collections import defaultdict

lines = open(sys.argv[1]).read().strip().split("\n")

red = 12
green = 13
blue = 14

COLOR = {
    "red": red,
    "green": green,
    "blue": blue,
}

def run_subgame(game):
    parts = game.split(",")
    possible = True
    cnts = defaultdict(int)
    for show in parts:
        show = show.strip()
        num, color = show.split(" ")
        if COLOR[color] < int(num):
            possible = False
        cnts[color] = max(cnts[color], int(num))
    return possible, cnts

def run_game(game):
    parts = game.split(";")
    tot = {x: 0 for x in COLOR}
    for x in parts:
        _, cnts = run_subgame(x)
        for k in cnts:
            tot[k] = max(tot[k], cnts[k])

    mul = 1
    for k, v in tot.items():
        mul = mul * v

    return mul

sum = 0

for line in lines:
    if line.startswith("Game"):
        line = line[len("Game ") :]
        game_num, rest = line.split(":")
        g_num = int(game_num)
        sum += run_game(rest)

print(sum)

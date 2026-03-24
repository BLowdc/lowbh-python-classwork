from itertools import combinations_with_replacement

inp = []
with open("AoC2025\\Day10\\input.txt", "r") as f:
    for line in f:
        inp.append(line.strip().split(" "))

lights = []
tmp = []
buttons = []
joltages = []

for line in inp:
    lights.append([char for char in line[0][1:-1]])
    tmp.append([n.strip("()") for n in line[1:-1]])
    joltages.append(line[-1])

for button in tmp:
    sub = []
    for b in button:
        sub.append(tuple(int(s) for s in b.split(",")))
    buttons.append(sub)


def swap(indicator, index):
    if indicator[index] == ".":
        indicator[index] = "#"
    else:
        indicator[index] = "."
    return indicator


def try_combs(inds: list, btns: list) -> int:
    temp = inds.copy()
    max_length = len(btns)
    for i in range(1, max_length + 1):
        combinations = combinations_with_replacement(btns, i)
        for comb in combinations:
            for a in comb:
                for idx in a:
                    swap(temp, idx)
            if "#" not in temp:
                return i
            temp = inds.copy()

    return 0


# main

ans = 0
for i in range(len(lights)):
    ans += try_combs(lights[i], buttons[i])

print(ans)

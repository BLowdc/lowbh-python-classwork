inp = []
with open("AoC2025\\Day10\\input.txt", "r") as f:
    for line in f:
        inp.append(line.strip().split(" "))

lights = []
tmpb = []
tmpj = []
buttons = []
joltages = []

for line in inp:
    lights.append([char for char in line[0][1:-1]])
    tmpb.append([n.strip("()") for n in line[1:-1]])
    tmpj.append(line[-1].strip("{}"))

for button in tmpb:
    sub = []
    for b in button:
        sub.append(tuple(int(s) for s in b.split(",")))
    buttons.append(sub)

for jolt in tmpj:
    joltages.append(tuple(int(s) for s in jolt.split(",")))


def is_oversize(limit: tuple, ls: list) -> bool:
    for i in range(len(limit)):
        if ls[i] > limit[i]:
            return False
    return True


def bfs(req: tuple, buttons: list):
    queue = {}
    start = [0] * len(req)
    for button in buttons:
        for idx in button:
            start[idx] += 1

    while queue:
        ...

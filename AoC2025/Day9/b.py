reds = []
with open("AoC2025\\Day9\\input.txt", "r") as f:
    for line in f:
        reds.append(
            tuple([int(coord) for coord in line.strip().split(",")])
        )
reds = tuple(reds)


def find_limit(h, v, a, b):
    if a[0] == b[0]:
        if a[0] not in v:
            v[a[0]] = [a[1], b[1]]
            v[a[0]].sort()
        else:
            v[a[0]].append(b[1])
            v[a[0]].append(a[1])
            v[a[0]].sort()
    else:
        if a[1] not in h:
            h[a[1]] = [a[0], b[0]]
            h[a[1]].sort()
        else:
            h[a[1]].append(b[0])
            h[a[1]].append(a[0])
            h[a[1]].sort()

    return h, v


def is_valid(v, c):
    x = c[0]
    y = c[1]
    intersection = 0

    # on boundary
    if x in v:
        if v[x][0] <= y <= v[x][1]:
            return True

    for key in v:
        if key < x:
            if v[key][0] < y <= v[key][1]:
                intersection += 1

    return intersection % 2 == 1


# main

h_limits = {}
v_limits = {}
n = len(reds)

for i in range(n - 1):
    find_limit(h_limits, v_limits, reds[i], reds[i + 1])

find_limit(h_limits, v_limits, reds[-1], reds[0])

max = -1
for i in range(n):
    for j in range(i + 1, n):
        c1 = [reds[j][0], reds[i][1]]
        c2 = [reds[i][0], reds[j][1]]
        if is_valid(v_limits, c1) and is_valid(v_limits, c2):
            width = abs(c1[0] - c2[0]) + 1
            height = abs(c1[1] - c2[1]) + 1
            area = width * height
            if area > max:
                max = area

print(max)

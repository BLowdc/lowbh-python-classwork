reds = []

with open("AoC2025\\Day9\\input.txt", "r") as f:
    for line in f:
        reds.append(
            tuple([int(coord) for coord in line.strip().split(",")])
        )

reds = tuple(reds)


def find_limit(h, v, a, b):
    if a[0] == b[0]:
        y1, y2 = sorted([a[1], b[1]])
        v.setdefault(a[0], []).append((y1, y2))
    else:
        x1, x2 = sorted([a[0], b[0]])
        h.setdefault(a[1], []).append((x1, x2))
    return h, v


def is_valid(h, v, c):
    x = c[0]
    y = c[1]
    if x in v:
        for y1, y2 in v[x]:
            if y1 <= y <= y2:
                return True
    if y in h:
        for x1, x2 in h[y]:
            if x1 <= x <= x2:
                return True
    intersection = 0
    for key in v:
        if key > x:
            for y1, y2 in v[key]:
                if y1 <= y < y2:
                    intersection += 1
    return intersection % 2 == 1


def crosses_boundary(h, v, xmin, xmax, ymin, ymax):
    for x in v:
        if xmin < x < xmax:
            for y1, y2 in v[x]:
                if max(y1, ymin) < min(y2, ymax):
                    return True
    for y in h:
        if ymin < y < ymax:
            for x1, x2 in h[y]:
                if max(x1, xmin) < min(x2, xmax):
                    return True
    return False


h_limits = {}
v_limits = {}
n = len(reds)

for i in range(n - 1):
    find_limit(h_limits, v_limits, reds[i], reds[i + 1])

find_limit(h_limits, v_limits, reds[-1], reds[0])

max_area = -1

for i in range(n):
    for j in range(i + 1, n):
        if reds[i][0] == reds[j][0] or reds[i][1] == reds[j][1]:
            continue
        c1 = [reds[j][0], reds[i][1]]
        c2 = [reds[i][0], reds[j][1]]
        if is_valid(h_limits, v_limits, c1) and is_valid(
            h_limits, v_limits, c2
        ):
            width = abs(c1[0] - c2[0]) + 1
            height = abs(c1[1] - c2[1]) + 1
            area = width * height
            if area > max_area:
                xmin, xmax = sorted([c1[0], c2[0]])
                ymin, ymax = sorted([c1[1], c2[1]])
                if not crosses_boundary(
                    h_limits, v_limits, xmin, xmax, ymin, ymax
                ):
                    max_area = area

print(max_area)

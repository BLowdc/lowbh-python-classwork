boxes = []
with open("AoC2025\\Day8\\test.txt", "r") as f:
    for line in f:
        boxes.append(
            tuple([int(coord) for coord in line.strip().split(",")])
        )

connections = {}
cir = []
unchecked = []
count = 0

for i in range(len(boxes)):
    for j in range(i + 1, len(boxes)):
        distance = (
            (boxes[i][0] - boxes[j][0]) ** 2
            + (boxes[i][1] - boxes[j][1]) ** 2
            + (boxes[i][2] - boxes[j][2]) ** 2
        )
        connections[distance] = (boxes[i], boxes[j])

dists = list(connections.keys())
dists.sort()
# print(dists)
connections = {i: connections[i] for i in dists}

for c in connections.values():
    added = False
    merged = False
    if cir:
        length = len(cir)
        # if length > 1:
        for p in range(length):
            for q in range(p + 1, length):
                if (c[0] in cir[p] and c[1] in cir[q]) or (
                    c[1] in cir[p] and c[0] in cir[q]
                ):
                    for r in cir[q]:
                        cir[p].add(r)
                    cir.pop(q)
                    if len(cir) == 1:
                        print(c)
                    merged = True
                    break
            if merged:
                break
        if not merged:
            for s in range(length):
                if c[0] in cir[s] or c[1] in cir[s]:
                    cir[s].add(c[0])
                    cir[s].add(c[1])
                    added = True
                    break
        if not added and not merged:
            cir.append({c[0], c[1]})
    else:
        cir.append({c[0], c[1]})

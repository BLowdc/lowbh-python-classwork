import math

boxes = []
with open("AoC2025\\Day8\\test.txt", "r") as f:
    for line in f:
        boxes.append(
            tuple([int(coord) for coord in line.strip().split(",")])
        )

connections = {}
circuits = []
unchecked = []
count = 0

for i in range(len(boxes)):
    for j in range(i + 1, len(boxes)):
        distance = math.sqrt(
            (boxes[i][0] - boxes[j][0]) ** 2
            + (boxes[i][1] - boxes[j][1]) ** 2
            + (boxes[i][2] - boxes[j][2]) ** 2
        )
        connections[distance] = (boxes[i], boxes[j])

dists = list(connections.keys())
dists.sort()
# print(dists)
connections = {i: connections[i] for i in dists}
# print(connections)

for k in connections:
    unchecked.append((connections[k]))

while unchecked:
    c = 0
    length = len(unchecked)
    app = False
    if circuits:
        while c < length:
            for r in circuits:
                if unchecked[c][0] in r or unchecked[c][1] in r:
                    r.add(unchecked[c][0])
                    r.add(unchecked[c][1])
                    unchecked.pop(c)
                    c -= 1
                    length -= 1
                    app = True
                    break
            c += 1

    if not app:
        circuits.append({unchecked[0][0], unchecked[0][1]})
        unchecked.pop(0)

print(circuits)

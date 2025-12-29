manifold = []
with open("AoC2025\\Day7\\input.txt", "r") as f:
    for line in f:
        manifold.append([char for char in line.strip()])

# for row in manifold:
#     print(' '.join([str(elem) for elem in row]))

start = manifold[0].index("S")
splitters = set()


def splits(map: list, pos: list, splitters: set) -> int:
    path = map[pos[0]][pos[1]]

    while path != "^":
        pos[0] += 1
        if pos[0] > len(map) - 1:
            return 0
        path = map[pos[0]][pos[1]]

    if (pos[0], pos[1]) not in splitters:
        splitters.add((pos[0], pos[1]))
        # if pos[1] >= 1 and pos[1] <= len(map[0])-2:
        return (
            splits(map, [pos[0], pos[1] - 1], splitters)
            + splits(map, [pos[0], pos[1] + 1], splitters)
            + 1
        )

        # elif pos[1] == 0:
        #     return splits(map, [pos[0],pos[1]+1], splitters) + 1
        # elif pos[1] == len(map[0])-1:
        #     return splits(map, [pos[0],pos[1]-1], splitters) + 1

    return 0


print(splits(manifold, [0, start], splitters))

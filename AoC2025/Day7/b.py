manifold = []
with open("AoC2025\\Day7\\input.txt", "r") as f:
    for line in f:
        manifold.append([char for char in line.strip()])

# for row in manifold:
#     print(' '.join([str(elem) for elem in row]))

start = manifold[0].index('S')
paths = {}

def splits(map: list,pos: list,paths: dict) -> int:

    while pos[0] != len(map) - 1:
        pos[0] += 1
        if map[pos[0]][pos[1]] == "^":
            if (pos[0],pos[1]-1) not in paths:
                paths[(pos[0],pos[1]-1)] = splits(map, [pos[0],pos[1]-1], paths)
            if (pos[0],pos[1]+1) not in paths:
                paths[(pos[0],pos[1]+1)] = splits(map, [pos[0],pos[1]+1], paths)
            return paths[(pos[0],pos[1]-1)] + paths[(pos[0],pos[1]+1)]

    return 1

print(splits(manifold,[0,start], paths))
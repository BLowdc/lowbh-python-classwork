grid = []
with open("AoC2025\\Day4\\rolls.txt", "r") as f:
    for line in f:
        grid.append(list(line.strip("\n")))

# for row in grid:
#     print(" ".join([str(elem) for elem in row]))

g = len(grid)
r = len(grid[0])
accessible = 0

for row in range(g):
    for elem in range(r):
        if grid[row][elem] == "@":
            count = -1
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= row + i <= g - 1 and 0 <= elem + j <= r - 1:
                        if grid[row + i][elem + j] == "@":
                            count += 1
            if count < 4:
                accessible += 1

print(accessible)

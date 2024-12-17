import re

width = 101
height = 103
grid = [[0 for i in range(width)] for j in range(height)]
robots = []

for line in open("c:\\AOC24\\robots.txt").read().split("\n"):
    robots.append(list(map(int, re.findall(r"-?\d+", line))))

minSF = float("inf")
minIter = None

def find2(l):
    for row in l:
        for elem in row:
            if elem == 2:
                return False
    return True

for px,py,vx,vy in robots:
    grid[py][px] += 1

for seconds in range(width*height):

    for i in range(len(robots)):
        vx,vy = robots[i][2],robots[i][3]
        grid[robots[i][1]][robots[i][0]] -= 1
        new_px = (robots[i][0] + vx) % width
        new_py = (robots[i][1] + vy) % height
        grid[new_py][new_px] += 1
        robots[i][0] = new_px
        robots[i][1] = new_py

    if find2(grid):
        print(seconds + 1)

#     ne, nw, se, sw = 0, 0, 0, 0

#     #quad NE
#     for i in range(width//2):
#         for j in range(height//2):
#             ne += grid[j][i]

#     #quad NW
#     for i in range(width//2):
#         for j in range(height//2+1, height):
#             nw += grid[j][i]

#     #quad SE
#     for i in range(width//2+1, width):
#         for j in range(height//2):
#             se += grid[j][i]

#     #quad SW
#     for i in range(width//2+1,width):
#         for j in range(height//2+1,height):
#             sw += grid[j][i]

#     sf = ne*nw*se*sw

#     if sf < minSF:
#         minSF = sf
#         minIter = seconds

# print(minSF, minIter + 1) #OFF BY 1 ERROR
        
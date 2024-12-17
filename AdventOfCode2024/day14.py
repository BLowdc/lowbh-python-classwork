import re

width = 101
height = 103
grid = [[0 for i in range(width)] for j in range(height)]

def seeTree(l):
    for i in range(len(l)):
        for j in range(len(l[0])):
            if l[i][j] == 0:
                l[i][j] = '.'
                
    return l
            

for line in open("c:\\AOC24\\robots.txt").read().split("\n"):
    px, py, vx, vy = map(int, re.findall(r"-?\d+", line))
    for i in range(7344):
        px = (px + vx) % width
        py = (py + vy) % height
    
    grid[py][px] += 1

grid = seeTree(grid)

for row in grid:
    print(' '.join([str(elem) for elem in row]))
print('')

# ne, nw, se, sw = 0, 0, 0, 0

# #quad NE
# for i in range(width//2):
#     for j in range(height//2):
#         ne += grid[j][i]

# #quad NW
# for i in range(width//2):
#     for j in range(height//2+1, height):
#         nw += grid[j][i]

# #quad SE
# for i in range(width//2+1, width):
#     for j in range(height//2):
#         se += grid[j][i]

# #quad SW
# for i in range(width//2+1,width):
#     for j in range(height//2+1,height):
#         sw += grid[j][i]

# print(ne*nw*se*sw)
        
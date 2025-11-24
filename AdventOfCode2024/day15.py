#reading inputs

h, m =  open("c:\\AOC24\\house.txt").read().split("\n\n")
house = []
inst = []
for line in h.split('\n'):
    house.append(list(line))

m2d = list(m.split("\n"))
for r in m2d:
    for c in r:
        inst.append(c)

#main program

def findPos(l2d) -> list:
    for i in range(len(l2d)):
        for j in range(len(l2d[0])):
            if l2d[i][j] == '@':
                return [i,j]


def checkQueue(grid,p,d) -> list:
    pt = [p[0] + d[0], p[1] + d[1]]
    queue = [p]
    while grid[pt[0]][pt[1]] == 'O':
        queue.append(pt)
        pt = [pt[0] + d[0], pt[1] + d[1]]
    
    if grid[pt[0]][pt[1]] == '#':
        return None
    else:
        queue.append(pt)
        queue.reverse()
        return queue
    
def findSum(list2D) -> int:
    sum = 0
    for i in range(len(list2D)):
        for j in range(len(list2D[0])):
            if list2D[i][j] == 'O':
                sum += i*100 + j
    
    return sum

dirs = {'^': [-1,0], '>': [0,1], 'v': [1,0], '<': [0,-1]}
cur_pos = findPos(house)

while inst:
    next_dir = inst.pop(0)
    next_pos = [cur_pos[0] + dirs[next_dir][0], cur_pos[1] + dirs[next_dir][1]]
    if house[next_pos[0]][next_pos[1]] == '.':
        temp = house[next_pos[0]][next_pos[1]]
        house[next_pos[0]][next_pos[1]] = house[cur_pos[0]][cur_pos[1]]
        house[cur_pos[0]][cur_pos[1]] = temp
        cur_pos = next_pos
    elif house[next_pos[0]][next_pos[1]] == 'O':
        q = checkQueue(house,cur_pos,dirs[next_dir])
        if q:
            for i in range(len(q)-1):
                temp = house[q[i][0]][q[i][1]]
                house[q[i][0]][q[i][1]] = house[q[i+1][0]][q[i+1][1]]
                house[q[i+1][0]][q[i+1][1]] = temp
            cur_pos = next_pos

for row in house:
    print(' '.join([str(elem) for elem in row]))

print(findSum(house))
f = open("c:\\AOC24\\hike.txt","r")
map = []
sum = 0
for line in f:
    line = list(line.strip('\n'))
    map.append(line)

def findPath(map,r,c) -> int:
    count = 0
    done = False
    stack = []
    cur_pos = [r,c]
    while not done:
        up = [cur_pos[0]-1,cur_pos[1]] if cur_pos[0] > 0 else None
        down = [cur_pos[0]+1,cur_pos[1]] if cur_pos[0] < (len(map) - 1) else None
        left = [cur_pos[0],cur_pos[1]-1] if cur_pos[1] > 0 else None
        right = [cur_pos[0],cur_pos[1]+1] if cur_pos[1] < (len(map[0]) - 1) else None
        #up
        if up:
            if map[cur_pos[0]][cur_pos[1]] == '8' and map[up[0]][up[1]] == '9':
                count += 1
            elif int(map[up[0]][up[1]]) == int(map[cur_pos[0]][cur_pos[1]]) + 1:
                stack.append([up[0],up[1]])
        #down
        if down:
            if map[cur_pos[0]][cur_pos[1]] == '8' and map[down[0]][down[1]] == '9':
                count += 1
            elif int(map[down[0]][down[1]]) == int(map[cur_pos[0]][cur_pos[1]]) + 1:
                stack.append([down[0],down[1]])
        #left
        if left:
            if map[cur_pos[0]][cur_pos[1]] == '8' and map[left[0]][left[1]] == '9':
                count += 1
            elif int(map[left[0]][left[1]]) == int(map[cur_pos[0]][cur_pos[1]]) + 1:
                stack.append([left[0],left[1]])
        #right
        if right:
            if map[cur_pos[0]][cur_pos[1]] == '8' and map[right[0]][right[1]] == '9':
                count += 1
            elif int(map[right[0]][right[1]]) == int(map[cur_pos[0]][cur_pos[1]]) + 1:
                stack.append([right[0],right[1]])
        
        if len(stack) == 0:
            done = True
        else:
            cur_pos = stack.pop()
    
    return count


for i in range(len(map)):
    for j in range(len(map)):
        if map[i][j] == '0':
            sum += findPath(map,i,j)

print(sum)
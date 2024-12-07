m = open("c:\\AOC24\\map.txt","r")
map = []
exited = False
for line in m:
    map.append(list(line.strip("\n")))

# for i in range(len(map)):
#     for j in range(len(map[i])):
#         if map[i][j] == '^':
#             print(i,j)

# my starting position: map[82][34]

dir = ['^','>','v','<']

cur_pos = [82,34]

print(map)

cur_dir = 0
obs = 0

while not exited:
    row = cur_pos[0]
    col = cur_pos[1]
    if map[cur_pos[0]][cur_pos[1]] == dir[0]: #up
        cur_pos[0] -= 1
    elif map[cur_pos[0]][cur_pos[1]] == dir[1]: #right
        cur_pos[1] += 1
    elif map[cur_pos[0]][cur_pos[1]] == dir[2]: #down
        cur_pos[0] += 1
    elif map[cur_pos[0]][cur_pos[1]] == dir[3]: #left
        cur_pos[1] -= 1
    #end ifs

    if (0 <= cur_pos[0] <= 129) and (0 <= cur_pos[1] <= 129):
        if map[cur_pos[0]][cur_pos[1]] == '#':
            cur_dir = (cur_dir + 1) % 4
            map[row][col] = dir[cur_dir]
            cur_pos = [row,col]
        elif map[cur_pos[0]][cur_pos[1]] == 'X':
            map[cur_pos[0]][cur_pos[1]] = dir[cur_dir]
            map[row][col] = 'X'
            obs += 1
        else:
            map[cur_pos[0]][cur_pos[1]] = dir[cur_dir]
            map[row][col] = 'X'
        #end if
    else:
        exited = True
    #end if
#end while
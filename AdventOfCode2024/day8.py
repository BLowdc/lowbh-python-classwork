total_ans = 0
checked = ['#','.']
lap = 0

def findAntinodes(freq, arr) -> list:
    locs = []
    bound = 50
    for i in range(bound):
        for j in range(bound):
            if arr[i][j] == freq:
                locs.append([i,j])

    length = len(locs)
    
    for k in range(length):
        for l in range(k+1,length):
            x_dist = locs[l][1] - locs[k][1]
            y_dist = locs[l][0] - locs[k][0]
            if (0 <= (locs[l][0] + y_dist) < bound) and (0 <= (locs[l][1] + x_dist) < bound):
                if arr[locs[l][0] + y_dist][locs[l][1] + x_dist] == '.':
                    arr[locs[l][0] + y_dist][locs[l][1] + x_dist] = '#'
            if (0 <= (locs[k][0] - y_dist) < bound) and (0 <= (locs[k][1] - x_dist) < bound):
                if arr[locs[k][0] - y_dist][locs[k][1] - x_dist] == '.':
                    arr[locs[k][0] - y_dist][locs[k][1] - x_dist] = '#'
    return arr

def findOverlaps(freq, arr) -> int:
    locs = []
    overlap = 0
    bound = 50
    for i in range(bound):
        for j in range(bound):
            if arr[i][j] == freq:
                locs.append([i,j])

    length = len(locs)
    
    for k in range(length):
        for l in range(k+1,length):
            x_dist = locs[l][1] - locs[k][1]
            y_dist = locs[l][0] - locs[k][0]
            if (0 <= (locs[l][0] + y_dist) < bound) and (0 <= (locs[l][1] + x_dist) < bound):
                if arr[locs[l][0] + y_dist][locs[l][1] + x_dist] != '.' and arr[locs[l][0] + y_dist][locs[l][1] + x_dist] != '#':
                    overlap += 1
            if (0 <= (locs[k][0] - y_dist) < bound) and (0 <= (locs[k][1] - x_dist) < bound):
                if arr[locs[k][0] - y_dist][locs[k][1] - x_dist] != '.' and arr[locs[k][0] - y_dist][locs[k][1] - x_dist] != '#':
                    overlap += 1
    return overlap
    


with open("c:\\AOC24\\antennas.txt", 'r') as file:
    city = [list(line.strip()) for line in file]
print(city)

for line in city:
    for char in line:
        if char not in checked:
            city = findAntinodes(char,city)
            lap += findOverlaps(char,city)
            checked.append(char)

# for row in city:
#     print(' '.join([str(elem) for elem in row]))

for row in city:
    for char in row:
        if char == '#':
            total_ans += 1

print(total_ans + lap - 1)
grid = [['x' for i in range(4)] for j in range(6)]
grid[0][0] = 'O'
for row in grid:
    print(' '.join([str(elem) for elem in row]))
#next row
pr = 0
pc = 0
while grid[5][3] != 'O':
    r = int(input("Enter row: "))
    while r < 1 or r > 6:
        r = int(input("Must be 1-6: "))
    #end while
    c = int(input("Enter column: "))
    while c < 1 or c > 4:
        c = int(input("Must be 1-4: "))
    #end while
    r -= 1
    c -= 1
    grid[pr][pc] = 'x'
    grid[r][c] = 'O'
    pc = c
    pr = r
    for row in grid:
        print(' '.join([str(elem) for elem in row]))
    #next row
#end while
print("You reached the end.")
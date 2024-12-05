f = open("c:\\AOC24\\XMAS.txt","r")
sls = []
totalCount = 0
for line in f:
    sls.append(line[:-1])
#next line

def checkHorizontal(arr2d,l_index,c_index) -> int:
    forwards = ''
    backwards = ''
    c = 0
    if arr2d[l_index][c_index] != 'X':
        return c
    for i in range(4):
        if c_index <= 136:
            forwards += arr2d[l_index][c_index + i]
        if c_index >= 3:
            backwards += arr2d[l_index][c_index - i]
    #next i
    if forwards == 'XMAS':
        c += 1
    if backwards == 'XMAS':
        c += 1
    #end if
    return c
#end function

def checkVertical(arr2d,l_index,c_index) -> int:
    upwards = ''
    downwards = ''
    arrLen = len(arr2d)
    c = 0
    if arr2d[l_index][c_index] != 'X':
        return c
    for i in range(4):
        if l_index >= 3:
            upwards += arr2d[l_index - i][c_index]
        if l_index <= 136:
            downwards += arr2d[l_index + i][c_index]
    #next i
    if upwards == 'XMAS':
        c += 1
    if downwards  == 'XMAS':
        c += 1
    #end if
    return c
#end function

def checkDiagonal(arr2d,l_index,c_index) -> int:
    NEDiag = ''
    NWDiag = ''
    SEDiag = ''
    SWDiag = ''
    arrLen = len(arr2d)
    c = 0
    if arr2d[l_index][c_index] != 'X':
        return c
    for i in range(4):
        if l_index >= 3 and c_index <= 136:
            NEDiag += arr2d[l_index - i][c_index + i]
        if l_index >= 3 and c_index >= 3:
            NWDiag += arr2d[l_index - i][c_index - i]
        if l_index <= 136 and c_index >= 3:
            SWDiag += arr2d[l_index + i][c_index - i]
        if l_index <= 136 and c_index <= 136:
            SEDiag += arr2d[l_index + i][c_index + i]
    #next i
    if NEDiag == 'XMAS':
        c += 1
        # print(l_index,c_index,'NE')
    if NWDiag == 'XMAS':
        c += 1
        # print(l_index,c_index,'NW')
    if SEDiag == 'XMAS':
        c += 1
        # print(l_index,c_index,'SE')
    if SWDiag == 'XMAS':
        c += 1
        # print(l_index,c_index,'SW')
    #end ifs
    return c


for i in range(len(sls)):
    for j in range(len(sls[i])):
        totalCount += checkHorizontal(sls,i,j) + checkVertical(sls,i,j) + checkDiagonal(sls,i,j)

print(totalCount)

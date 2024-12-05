f = open("c:\\AOC24\\XMAS.txt","r")
sls = []
totalCount = 0
for line in f:
    sls.append(line[:-1])
#next line

def checkDiagonal(arr2d,l_index,c_index) -> int:
    downDiag = ''
    upDiag = ''
    if arr2d[l_index][c_index] != 'A':
        return 0
    if (1 <= l_index <= 138) and (1 <= c_index <= 138):
        downDiag = arr2d[l_index - 1][c_index - 1] + 'A' + arr2d[l_index + 1][c_index + 1]
        upDiag = arr2d[l_index + 1][c_index - 1] + 'A' + arr2d[l_index - 1][c_index + 1]
    #end ifs
    if (downDiag == 'MAS' or downDiag == 'SAM') and (upDiag == 'MAS' or upDiag == 'SAM'):
        return 1
    else:
        return 0
    #end if


for i in range(len(sls)):
    for j in range(len(sls[i])):
        totalCount += checkDiagonal(sls,i,j)

print(totalCount)

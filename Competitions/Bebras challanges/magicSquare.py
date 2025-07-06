def checkMagic(arr) -> bool:
    # check horizontal
    for line in arr:
        t = 0
        for num in line:
            t += num
        #next num
        if t != 15:
            return False
        #end if
    #next line

    # check vertical
    for col in range(3):
        t = 0
        for row in range(3):
            t += arr[row][col]
        #next row
        if t != 15:
            return False
        #end if
    #next col

    #check diagonal

    t = 0
    for i in range(3):
        t += arr[i][i]
    #next i
    if t != 15:
        return False
    #end if

    t = 0
    for i in range(3):
        t += arr[i][2-i]
    #next i
    if t != 15:
        return False
    #end if

    return True

#end function

a = []
for j in range(3):
    a.append([int(k) for k in input().split()])
#next j

if checkMagic(a):
    print("magic")
else:
    print("muggle")
#end if



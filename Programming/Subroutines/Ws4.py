def parkACar(carpark)->list:
    parked = False
    num = input("Enter registration number: ")
    while not parked:
        r = int(input("Enter row: "))
        while r < 1 or r > 6:
            r = int(input("1-6: "))
        #end while
        r -= 1
        c = int(input("Enter column: "))
        while c < 1 or c > 10:
            c = int(input("1-10: "))
        #end while
        c -= 1
        if carpark[r][c] == 'Empty':
            carpark[r][c] = num
            parked = True
        else:
            print("Space taken")
    #end while
    return carpark
#end function

def removeACar(carpark)->list:
    num = input("Enter registration number: ")
    for row in carpark:
        for elem in row:
            if elem == num:
                elem = "Empty"
            #end if
        #next elem
    #next row
    return carpark
#end function

def displayCarParkGrid(carpark)->None:
    for row in carpark:
        print(' '.join([str(elem) for elem in row]))
#end procedure

carpark = [['Empty' for i in range(6)] for j in range(10)]
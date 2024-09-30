def parkACar(carpark)->list:
    parked = False
    num = input("Enter registration number: ")
    while not parked:
        r = int(input("Enter row: "))
        c = int(input("Enter column: "))
        if carpark[r-1][c-1] == 'Empty':
            carpark[r-1][c-1] = num
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
        print(' '.join(str(elem) for elem in row))
#end procedure

carpark = [['Empty']*10 for s in range(6)]
parkACar(carpark)
removeACar(carpark)
displayCarParkGrid(carpark)


        
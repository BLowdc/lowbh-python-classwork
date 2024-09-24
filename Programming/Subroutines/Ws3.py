def getPword(attempt)->str:
    if attempt == 1:
        password = input("Enter password: ")
        while len(password) < 6 or len(password) > 8:
            password = input("Error. Password must be 6 to 8 characters long: ")
        #end while
    elif attempt == 2:
        password = input("Enter password again: ")
    #end if
    return password
#end function

a = 1
same = False
while not same:
    p1 = getPword(a)
    a += 1
    p2 = getPword(a)
    if p1 == p2:
        same = True
    else:
        print("Password must be the same")
        a = 1
    #end if
#end while
print("Password change successful")
    

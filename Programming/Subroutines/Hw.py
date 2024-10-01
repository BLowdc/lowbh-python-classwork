def displayMenu() -> list:
    print("1. Add name")
    print("2. Display list")
    print("3. Quit")
    c = int(input("Enter choice: "))
    while c < 1 or c > 3:
        c = int(input("Invalid choice, try again: "))
    #end while
    return c
#end function

def addName(l) -> list:
    n = input("Enter the name to be added to the list: ")
    p = int(input("Enter position in the list to insert the name: "))
    while p < 1 or p > 10:
        p = int(input("Invalid position, must be 1-10: "))
    #end while
    p -= 1
    l[p] = n
    return l
#end function

def displayList(l) -> None:
    for i in range(len(names)):
        if l[i] != ' ':
            print(str(i+1)+".", l[i])
        #end if
    #next i
#end procedure

names = [' '] * 10
quit = False
while not quit:
    choice = displayMenu()
    match choice:
        case 1:
            addName(names)
        case 2:
            displayList(names)
        case 3:
            quit = True
            print("Program terminating...")
    #end match
#end while
school = ["AAAA","BBBB","CCCC","DDDD"]
medal = [4,7,1,3]
print("Enter -1 to display all data")
print("Enter 'end' to end program")
print("Enter 1-4 to add medal to school")
skl = input("Enter choice: ")
while skl != "end":
    try:
        skl = int(skl)
        if skl == -1:
            for i in range(4):
                print("School number:",i+1,"School name:",school[i],"Number of medals:",medal[i])
            #next i
            skl = input("Enter choice: ")
        else:
            while skl < 1 or skl > 4:
                skl = int(input("Enter 1-4: "))
            #end while
            medal[skl-1] += 1
            skl = input("Enter choice: ")
        #end if
    except:
        skl = input("Enter a valid chocie: ")
#end while
print("Quitting...")
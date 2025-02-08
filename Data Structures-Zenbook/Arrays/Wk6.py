park = [['Empty' for i in range(6)] for j in range(10)]
parked = False
for row in park:
    print(' '.join([str(elem) for elem in row]))
#next row
print("------------------------------------")
while not parked: 
    num = input("Enter registration number: ") 
    r = int(input("Enter row: "))
    while r < 1 or r > 10:
        r = int(input("1-10: "))
    #end while
    r -= 1
    c = int(input("Enter column: "))
    while c < 1 or c > 6:
        c = int(input("1-6: "))
    #end while
    c -= 1
    if park[r][c] == "Empty":
        park[r][c] = num 
        parked = True 
    else: 
        print("That space is taken") 
    #end if 
#end while 
print("------------------------------------")
for row in park:
    print(' '.join([str(elem) for elem in row]))
#next row
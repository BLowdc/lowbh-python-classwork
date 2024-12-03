f = open("c:\\AOC24\\reports.txt","r")
ls = []
ls2 = []
safe = 0

def isIncreasing(list):
    for i in range(1,len(list)):
        if list[i] <= list[i-1]:
            return False
        elif (list[i] - list[i-1]) > 3:
            return False
        #end if
    #next i
    return True
#end function

def isDecreasing(list):
    for i in range(1,len(list)):
        if list[i] >= list[i-1]:
            return False
        elif (list[i-1] - list[i]) > 3:
            return False
        #end if
    #next i
    return True
#end function


for line in f:
    a = [int(s) for s in line.strip().split()]
    ls.append(a)
#next line

for level in ls:
    if isIncreasing(level) or isDecreasing(level):
        safe += 1
    else:
        ls2.append(level)
    #end if   
#next level
print(ls2)

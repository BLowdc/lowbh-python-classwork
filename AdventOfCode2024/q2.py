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

def errorCount1(list):
    error = 0
    for i in range(1,len(list)):
        if (list[i] >= list[i-1]) or ((list[i-1] - list[i]) > 3):
            error += 1
        #end if
    #next i
    if error == 1:
        return True
    else:
        return False
    #end if
#end function

def errorCount2(list):
    error = 0
    for i in range(1,len(list)):
        if (list[i] <= list[i-1]) or ((list[i] - list[i-1]) > 3):
            error += 1
        #end if
    #next i
    if error == 1:
        return True
    else:
        return False
    #end if
#end function

for line in f:
    a = [int(s) for s in line.strip().split()]
    ls.append(a)
#next line

for level in ls:
    if isIncreasing(level) or isDecreasing(level):
        safe += 1
    # else:
    #     ls2.append(level)
    #end if   
#next level

# for level in ls2:
#     if errorCount1(s) or errorCount2(s):
#         safe += 1
#     #end if
# #next level

print(safe)
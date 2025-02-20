def countFreshMangoes(ls) -> int:
    fresh = 0
    old = 0
    freshSold = 0
    for day in ls:
        fresh += day[0]
        if old > 0:
            old -= day[1]
        else:
            fresh -= day[1]
            freshSold += day[1]
        #end if
        if old < 0:
            fresh += old
            freshSold -= old
            old = 0
        #end if

        old += fresh
        fresh = 0
    #next day
    return freshSold
#end function

n = int(input())
a = []
for i in range(n):
    a.append([int(j) for j in input().split()])
#next i

print(countFreshMangoes(a))

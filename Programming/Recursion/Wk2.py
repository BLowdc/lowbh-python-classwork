def sumEven(n):
    if n == 0:
        return 0
    #end if
    return sumEven(n-2) + n
#end function
num = int(input())
print(sumEven(num))
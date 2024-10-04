
def fib(n)->int:
    if n == 0 or n == 1:
        return n
    #end if
    return fib(n-1) + fib(n-2)
#end function
print(fib(10))


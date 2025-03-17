def strip(n) -> int:
    c = 1
    while n > 0:
        temp = str(n)
        sub = 0
        for char in temp:
            sub += int(char)
        # next char
        n -= sub
        c += 1
    #end while

    return c

#end function

num = int(input())
print(strip(num))


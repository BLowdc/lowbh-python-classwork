def sum_even(n):
    t = 0
    if n % 2 == 0:
        for i in range(0,n+1,2):
            t += i
    else:
        for i in range(0,n,2):
            t += i
    #endif
    return t
#endfunction

print(sum_even(int(input())))

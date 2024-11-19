n = int(input())
f = 1
i = 2
fib = [0,1]
while f < n:
    f = fib[i-1] + fib[i-2]
    fib.append(f)
    i += 1
#endwhile
print(fib)
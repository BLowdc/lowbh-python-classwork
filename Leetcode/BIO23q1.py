n = int(input())
fib = [0,1]
f = 1
i = 2
while f < 53316291173:
    f = fib[i-1] + fib[i-2]
    fib.append(f)
    i += 1
#endwhile

print(n)
sum = 0
nums = []

listLen = len(fib)
diff = n - sum

for i in range(listLen-1,0,-1):
    if fib[i] <= diff:
        sum += fib[i]
        diff = n - sum
        nums.append(fib[i])
    #end if
    if diff == 0:
        break
    #end if
#next i
#next number

for n in nums:
    print(n, end=' ')
#next n

n = int(input())
ls = [int(s) for s in input().split()]
total = n*(n+1)//2
for num in ls:
    total -= num

print(total)
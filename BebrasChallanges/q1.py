n = int(input())
ans = 0
for i in range(64):
    ans += 2**i
    if ans > n:
        break

print(i)

a = list(map(int, input().split(" ")))
diff = a[1] - a[0]
count = 1
maxCount = -1
for i in range(1, len(a) - 1):
    if a[i + 1] - a[i] == diff:
        count += 1
    else:
        if count > maxCount:
            maxCount = count
        diff = a[i + 1] - a[i]
        count = 1

if maxCount == 0:
    maxCount = count
print(maxCount + 1)

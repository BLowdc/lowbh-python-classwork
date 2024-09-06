total = 0
count = 1
n = int(input())
while n >= 0:
    total += n
    n = int(input())
    count += 1
avg = total / count
print(avg)

n = int(input())
large = n // 24
if (n % 24) % 5 == 0:
    small = (n % 24) // 5
else:
    small = (n % 24) // 5 + 1
print(large,small)
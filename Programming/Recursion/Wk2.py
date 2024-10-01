def sumEven(n):
    if n == 0:
        return 0
    return sumEven(n-2) + n

num = int(input())
print(sumEven(num))
def high_1d(arr):
    high = arr[0]
    for i in range(len(arr)):
        if arr[i] > high:
            high = arr[i]
    return high

def big_2d(arr):
    big = arr[0][0]
    for row in arr:
        if high_1d(row) > big:
            big = high_1d(row)
    return big

n = int(input())
a = [[int(j) for j in input().split()] for i in range(n)]

print(big_2d(a))
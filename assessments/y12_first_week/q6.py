def high_1d(arr):
    high = arr[0]
    for i in range(len(arr)):
        if arr[i] > high:
            high = arr[i]
    return high

a = [int(s) for s in input().split()]
print(high_1d(a))
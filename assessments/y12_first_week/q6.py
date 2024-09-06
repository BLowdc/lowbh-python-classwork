def high_1d(arr):
    high = arr[0]
    for i in range(len(arr)):
        if arr[i] > high:
            high = arr[i]
    print(high)
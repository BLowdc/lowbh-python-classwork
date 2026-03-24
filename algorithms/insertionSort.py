def insertionSort(arr: list) -> list:
    for i in range(1, len(arr)):
        temp = arr[i]
        while i > 0 and arr[i - 1] > temp:
            arr[i] = arr[i - 1]
            i -= 1
        arr[i] = temp
    return arr


a = [1, 6, 4, 9, 2, 8, 7, 5]
insertionSort(a)

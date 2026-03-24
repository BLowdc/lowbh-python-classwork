def bubbleSort(arr: list) -> list:
    for i in range(len(arr) - 1):
        swap = False
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                swap = True

        if not swap:
            return arr
    return arr


a = [1, 6, 4, 9, 2, 8, 7, 5]
print(bubbleSort(a))

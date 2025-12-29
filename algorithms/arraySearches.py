def linearSearch(t, arr: list, n: int) -> int:
    for i in range(n):
        if arr[i] == t:
            return i
        # end if
    # next i
    return -1


# end function


def linearSearchR(t, arr: list, n: int) -> int:
    if n == 0:
        return -1
    elif arr[n - 1] == t:
        return n - 1
    return linearSearchR(t, arr, n - 1)


def binarySearch(t, arr) -> int:
    up = len(arr) - 1
    low = 0
    while up >= low:
        mid = (up - low) // 2 + low
        if arr[mid] > t:
            up = mid - 1
        elif arr[mid] < t:
            low = mid + 1
        else:
            return mid
        # end if
    # end while
    return -1


def binarySearchR(t, arr: list, n: int) -> int:
    if n == 0:
        return -1

    up = n - 1
    low = 0
    mid = (up - low) // 2 + low
    if arr[mid] > t:
        return binarySearchR(t, arr[0:mid], mid + 1)
    elif arr[mid] < t:
        return binarySearchR(t, arr[mid + 1 :], n - mid)
    else:
        return mid


# end function

ls = [1, 3, 5, 6, 8, 10, 12]
print(binarySearchR(8, ls, len(ls)))

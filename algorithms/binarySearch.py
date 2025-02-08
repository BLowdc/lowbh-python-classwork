def binarySearch(t,arr) -> int:
    up = len(arr) - 1
    low = 0
    while up >= low:
        mid = (up + low) // 2
        if arr[mid] > t:
            up = mid - 1
        elif arr[mid] < t:
            low = mid + 1
        else:
            return mid
        #end if
    #end while
    return "not found"
#end function

l = [1,2,3,4,5,6,7,8,9,10]
print(binarySearch(int(input()),l))
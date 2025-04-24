def merge(arr1,arr2):
    arrNew = []
    while arr1 and arr2:
        if arr1[0] > arr2[0]:
            arrNew.append(arr2[0])
            arr2.pop(0)
        else:
            arrNew.append(arr1[0])
            arr1.pop(0)
        # end if
    # end while
    if arr1:
        arrNew += arr1
    # end if
    if arr2:
        arrNew += arr2
    # end if
    return arrNew
# end function

arr1 = [1,3,5,7,9]
arr2 = [2,4,6,8,10]

print(merge(arr1,arr2))

    
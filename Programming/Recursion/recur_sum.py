def recurTotal(arr)->int:
    if len(arr) == 0:
        return 0
    #end if
    return recurTotal(arr[1:]) + arr[0]
#end function

nums = [1,3,7,11,13,17,23,29]
print(recurTotal(nums))
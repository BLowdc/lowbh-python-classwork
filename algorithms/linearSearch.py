def linearSearch(t, arr) -> int:
    for i in range(len(arr)):
        if arr[i] == t:
            return i
        #end if
    #next i
    return "not found"
#end function
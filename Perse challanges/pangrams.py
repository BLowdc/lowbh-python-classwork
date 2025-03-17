def checkPangram(s) -> str:
    ans = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    alpha = list(alpha)
    for char in s:
        if char.lower() in alpha:
            alpha.remove(char)
        # end if
    # next char
    for elem in alpha:
        ans += elem
    # next elem
    return ans
# end function

string = input()
print(checkPangram(string))
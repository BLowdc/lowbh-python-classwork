def isPangram(sen):
    alp = {}
    for c in sen:
        char = c.lower()
        if char in 'qwertyuiopasdfghjklxcvbznm':
            alp[char] = 1
        #end if
    #next c
    if len(alp) == 26:
        return True
    else:
        return False
    #end if
#end function 

s = input()
if isPangram(s):
    print("Pangram")
else:
    print("Not a pangram")
#end if


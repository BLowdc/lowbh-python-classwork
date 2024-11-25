def contains(s1,s2):
    s1Length = len(s1)
    s2Length = len(s2)

    for i in range(s2Length-s1Length+1):
        substring = s2[i:(i+s1Length)]
        if substring == s1:
            return True
    
    return False

print(contains('fox','foxhound'))

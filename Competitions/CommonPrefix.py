strs = ["flower","flower","flower","flower"]
prefix = ""
n = len(min(strs))
skip = False
index = 0
if n == 0:
    print(prefix)
elif len(strs) == 1:
    print(strs[0])
else:
    for l in range(n):
        letter = strs[0][l]
        for string in range(1,len(strs)):
            if strs[string][l] != letter:
                skip = True
                break
            else:
                skip = False
                continue               
        if skip:
            break
        prefix += letter
    print(prefix)

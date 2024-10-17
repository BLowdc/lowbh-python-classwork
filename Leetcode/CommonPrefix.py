strs = ["flower","flower","flower","flower"]
prefix = ""
n = len(min(strs))
index = 0
if n == 0:
    print(prefix)
elif len(strs) == 1:
    print(strs[0])
else:
    for s in range(n):
        letter = strs[0][index]
        if strs[s][index] != letter:
            break
        else:
            prefix += letter
            index += 1
    print(prefix)

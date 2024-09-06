string = input()
num = ['zero','one','two','three','four','five','six','seven','eight','nine']
for i in range(len(string)):
    if string[i] in '0123456789':
        left = string[:i]
        right = string[i+1:]
        string = left + num[int(string[i])] + right
print(string)
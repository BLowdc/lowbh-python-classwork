sen = input()
i = 0
len_sen = len(sen)
num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
for i in sen:
    if sen[i] in '0123456789':
        left = sen[:i]
        right = sen[i+1:]
        sen = left + num[int(sen[i])] + right
print(sen)
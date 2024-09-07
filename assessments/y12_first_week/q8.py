sen = input()
i = 0
len_sen = len(sen)
num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
while i != len_sen:
    if sen[i] in '0123456789':
        len_sen += (len(str(num[int(sen[i])])) - 1)
        left = sen[:i]
        right = sen[i+1:]
        sen = left + num[int(sen[i])] + right
    i += 1
print(sen)
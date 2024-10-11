def reversed_string(text):
    if len(text) == 1:
        return text
    rtext = reversed_string(text[1:]) + text[:1]
    return rtext

num = input()
ls = ''
while num != '0':
    ls = ls + num
    num = input()
ls = ls + '0'
rList = reversed_string(ls)
for i in range(len(rList)):
    print(rList[i])
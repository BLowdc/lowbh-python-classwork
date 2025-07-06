a = '1010'
b = '1011'

s1 = a[::-1]
s2 = b[::-1]
carry = 0
num = ''
while len(s1) or len(s2) or carry:
    v1 = s1[0] if len(s1) else 0
    v2 = s2[0] if len(s2) else 0
    v1 = int(v1)
    v2 = int(v2)

    val = v1 + v2 + carry
    carry = val // 2
    val = val % 2

    num += str(val)
    s1 = s1[1:]
    s2 = s2[1:]
print(num[::-1])


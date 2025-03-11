def toBinary(n) -> str:
    quo = n
    b = ''
    while quo > 0:
        rem = quo % 2
        quo = quo // 2
        b = str(rem) + b
    return b

print(toBinary(int(input())))



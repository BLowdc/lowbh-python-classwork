n = int(input())
bn = ""

while n > 0:
    bn += str(n % 2)
    n //= 2

print(len(bn))

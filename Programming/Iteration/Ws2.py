n = int(input())
c = 0
old = 0
while n != 9999:
    while len(str(n)) != 4:
        n = int(input("Error: "))
    c += 1
    if str(n % 10) in '678':
        old += 1
    n = int(input())
print("total parts:", c)
print("old parts:", old)
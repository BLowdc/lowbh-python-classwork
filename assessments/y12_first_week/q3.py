mins = int(input())
h = mins // 60
m = mins % 60
if h < 10:
    h = '0' + str(h)
if m < 10:
    m = '0' + str(m)
print(str(h) + ':' + str(m))

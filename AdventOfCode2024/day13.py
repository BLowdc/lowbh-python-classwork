import re
import sympy as sym

total1 = 0
total2 = 0

def isInt(n):
    if n % 1 == 0:
        return True
    else:
        return False

for block in open("c:\\AOC24\\arcade.txt").read().split("\n\n"):
    ax, ay, bx, by, px, py = map(int, re.findall(r"\d+", block))
    for i in range(101):
        for j in range(101):
            if i*ax + j*bx == px and i*ay + j*by == py:
                total1 += i*3 + j

    px += 10000000000000
    py += 10000000000000
    i,j = sym.symbols('i,j')
    eq1 = sym.Eq(i*ax + j*bx, px)
    eq2 = sym.Eq(i*ay + j*by, py)
    ans = sym.solve([eq1,eq2],(i,j))
    if isInt(ans[i]) and isInt(ans[j]):
        total2 += ans[i] * 3 + ans[j]

print('Part 1 answer:',total1)
print('Part 2 answer:',total2)





    
import re

total = 0
for block in open("c:\\AOC24\\arcade.txt").read().split("\n\n"):
    ax, ay, bx, by, px, py = map(int, re.findall(r"\d+", block))
    for i in range(101):
        for j in range(101):
            if (i*ax + j*bx == px) and (i*ay + j*by == py):
                total += i*3 + j
            
print(total)

    
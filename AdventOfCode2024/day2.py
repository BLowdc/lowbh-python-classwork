f = open("c:\\AOC24\\reports.txt","r")
ls = []
ls2 = []
safe = 0

def isSafe(levels):
    differs = [a - b for a, b in zip(levels, levels[1:])]
    is_monotonic = all(i > 0 for i in differs) or all(i < 0 for i in differs)
    is_in_range = all(0 < abs(i) <= 3 for i in differs)
    if is_monotonic and is_in_range:
        return True
    return False

for line in f:
    a = [int(s) for s in line.strip().split()]
    ls.append(a)
#next line

for level in ls:
    if isSafe(level):
        safe += 1
    else:
        for i in range(len(level)):
            tolerated_levels = level[:i] + level[i + 1 :]
            if isSafe(tolerated_levels):
                print(tolerated_levels)
                safe += 1
                break
print(safe)
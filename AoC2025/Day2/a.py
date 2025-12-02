with open("AoC2025\Day2\day2.txt", "r") as f:
    for line in f:
        ids = line.split(",")

ans = 0

for i in range(len(ids)):
    ids[i] = ids[i].split("-")

for id in ids:
    for j in range(int(id[0]), int(id[1]) + 1):
        s = str(j)
        if len(s) % 2 == 0:
            first_half = s[: len(s) // 2]
            second_half = s[len(s) // 2 :]
            if first_half == second_half:
                ans += j

print(ans)

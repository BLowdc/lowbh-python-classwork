banks = []
with open("AoC2025\\Day3\\banks.txt", "r") as f:
    for line in f:
        banks.append(line.strip("\n"))

joltage = 0

for bank in banks:
    highest = ""
    index = -1
    for j in range(11, -1, -1):
        for n in range(9, -1, -1):
            found = False
            for i in range(index + 1, len(bank) - j):
                if int(bank[i]) == n:
                    found = True
                    index = i
                    break
            if found:
                highest += str(n)
                break

    joltage += int(highest)

print(joltage)

banks = []
with open("AoC2025\\Day3\\banks.txt", "r") as f:
    for line in f:
        banks.append(line.strip("\n"))

joltage = 0

for bank in banks:
    for n in range(9, -1, -1):
        found = False
        index = -1
        for i in range(len(bank) - 1):
            if int(bank[i]) == n:
                found = True
                index = i
                break
        if found:
            highest_num = n
            break
    max = -1
    for j in range(index + 1, len(bank)):
        if int(bank[j]) > max:
            max = int(bank[j])

    ans = int(str(highest_num) + str(max))

    joltage += ans

print(joltage)

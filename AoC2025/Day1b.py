test = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""
test = test.split("\n")

f = open("C:\\AoC25\\day1.txt", "r")
rotations = []
for line in f:
    rotations.append(line.strip("\n"))

dial = 50
password = 0
for elem in rotations:
    if elem[0] == "L":
        if dial == 0:
            dial -= int(elem[1::])
            password += abs(dial) // 100
        else:
            dial -= int(elem[1::])
            if dial == 0:
                password += 1
            elif dial % 100 == 0:
                password += abs(dial // 100) + 1
            else:
                password += abs(dial // 100)

    else:
        dial += int(elem[1::])
        password += dial // 100

    dial %= 100

print(password)

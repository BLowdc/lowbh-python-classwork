f = open("C:\\AoC25\\day1.txt", "r")
rotations = []
for line in f:
    rotations.append(line.strip("\n"))

dial = 50
password = 0
for elem in rotations:
    if elem[0] == "L":
        num = int(elem[1::])
        dial = (dial - num) % 100
    else:
        num = int(elem[1::])
        dial = (dial + num) % 100

    if dial == 0:
        password += 1

print(password)

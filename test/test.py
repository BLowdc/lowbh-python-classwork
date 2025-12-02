import random


def positive_loop(r: list):
    while r[2] > r[1]:
        r[1] = r[1] - r[2]
        r[3] = r[3] + 1


def negative_loop(r):
    while r[2] > r[1]:
        r[1] = r[1] + r[2]
        r[3] = r[3] - 1


def division(n1: int, n2: int):
    R = [random.randint(-10, 10) for _ in range(10)]
    R[1] = n1
    R[2] = n2
    R[0] = 0  # check last subtraction
    R[3] = 0  # quotient
    R[4] = 0  # remainder
    R[5] = 0  # zero constant

    if R[1] > R[5]:  # checks if R1 is positive
        # checks if denominator > numerator
        if R[2] > R[1]:
            R[4] = R[4] + R[1]
            return (R[3], R[4])

    # checks division by 0
    if R[2] == 0:
        return "division by 0"

    # main loop

    # R1 negative, R2, positive
    if R[5] > R[1]:
        if R[2] > R[5]:
            while R[2] > R[1]:
                R[1] = R[1] + R[2]
                R[3] = R[3] - 1

    # R1 positive, R2 negative
    if R[5] > R[2]:
        if R[1] > R[5]:
            while R[1] > R[2]:
                R[1] = R[1] + R[2]
                R[3] = R[3] - 1

    # both negative
    if R[5] > R[1]:
        if R[5] > R[2]:
            while R[2] > R[1]:
                R[1] = R[1] - R[2]
                R[3] = R[3] + 1

    # both positive
    if R[1] > R[5]:
        if R[1] > R[5]:
            while R[1] > R[2]:
                R[1] = R[1] - R[2]
                R[3] = R[3] + 1

    # last subtraction check
    R[0] = R[1] - R[2]
    if R[0] == 0:
        R[1] = R[1] - R[2]
        R[3] = R[3] + 1

    R[4] = R[4] + R[1]

    return (R[3], R[4])


num1 = int(input())
num2 = int(input())
print(division(num1, num2))

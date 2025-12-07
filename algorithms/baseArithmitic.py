# n1 = input("Enter first number: ")
# b1 = int(input("Enter base of first number: "))
# n2 = input("Enter second number: ")
# b2 = int(input("Enter base of second number: "))

num_to_hex = {
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F",
}


hex_to_num = {
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15,
}


def to_base10(num: str, base: int):
    num_dec = 0
    for i in range(0, len(num)):
        power = len(num) - 1 - i
        if num[i] in hex_to_num:
            num_dec += hex_to_num[num[i]] * (base**power)
        else:
            num_dec += int(num[i]) * (base**power)

    return num_dec


def from_base10(num: str, base: int):
    result = ""
    quotient = int(num)
    while quotient != 0:
        if (quotient % base) in num_to_hex:
            result += num_to_hex[quotient % base]
        else:
            result += str(quotient % base)
        quotient = quotient // base
    if quotient != 0:
        if quotient in num_to_hex:
            result += num_to_hex[quotient]
        else:
            result += str(quotient)
    result = result[::-1]

    return result


n = to_base10("7075", 8)
print(from_base10(n, 2))

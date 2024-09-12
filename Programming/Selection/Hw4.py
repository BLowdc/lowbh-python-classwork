print("Select one: ")
print("A for Multiplication")
print("B for Division")
print("C for Addition")
print("D for Subtraction")
print("E for Remainder Division")
c = input("Enter here: ")
n1 = int(input())
n2 = int(input())
match c:
    case "A":
        print(n1 * n2)
    case "B":
        print(n1 / n2)
    case "C":
        print(n1 + n2)
    case "D":
        print(n1 - n2)
    case "E":
        print(n1 // n2)
    case _:
        print("Not valid choice")
age = int(input())
valid = False
while not valid:
    if age >= 10 and age < 19:
        print("Valid age")
        valid = True
    else:
        age = int(input("Invalid age, enter age between 10 and 19: "))

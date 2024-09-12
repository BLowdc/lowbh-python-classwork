year = int(input("Enter year: "))
LeapYear = False
if year % 4 == 0:
    LeapYear = True
if year % 100 == 0:
    LeapYear = False
if year % 400 == 0:
    LeapYear = True
if LeapYear:
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
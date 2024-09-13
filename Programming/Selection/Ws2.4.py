exam = int(input("Enter exam mark: "))
attend = int(input("Enter attendance rate: "))

if (attend < 90) or (exam <= 70):
    print("Fail") 
elif (exam > 70) and (exam <= 80):
    print("Grade = C") 
elif (exam > 80) and (exam <= 90):
    print("Grade = B") 
else:
    print("Grade = A") 
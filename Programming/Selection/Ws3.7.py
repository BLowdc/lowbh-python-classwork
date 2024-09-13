temp = input("Do you have a temperature? (y/n): ") 
if temp == 'y': 
    throat = input("Do you have a sore throat? (y/n): ") 
    if throat == 'y':
        print("You may have a throat infection.") 
    elif throat == 'n':
        cough = input("Do you have a cough") 
    if cough == 'y': 
        print("You have a chest infection.") 
    elif cough == 'n': 
        print("You have a fever.") 
elif temp == 'n':
    print("You are not sick.") 

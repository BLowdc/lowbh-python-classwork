print("1: Economy Car") 
print("2: Saloon Car") 
print("3: Sports Car") 
choice = input("Enter 1-3: ") 
if choice >= 1 and choice <= 3:
    n = input("Do you wish to proceed or cancel?") 
    if n == "proceed":
        print("have a nice day.") 
    elif n == "cancel":
        print("Cancelled, have a nice day.")
else:
    print("Invalid choice")

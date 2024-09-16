for i in range(3,0,-1):
    pw = input()
    if pw == "Tues1212":
        print("Password accepted")
        break
    print("Password rejected")
    print("Remaining tries:", i-1)
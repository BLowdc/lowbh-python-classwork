v = float(input("Enter order value: "))
d = int(input("Delivery option 1 or 2: "))
match d:
    case 1:
        print("£5 postage")
        print("Total: £"+ str(v + 5))
    case 2:
        if v >= 15:
            print("Free postage")
            print("Total: £"+ str(v))
        else:
            print("£3.50 postage")
            print("Total: £"+ str(v + 3.5))

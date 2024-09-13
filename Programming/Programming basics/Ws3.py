old = int(input("Enter car mileage the last time the car was filled: "))
new = int(input("Enter car mileage now: "))
litre = float(input("Enter litres taken to fill the tank: "))
print((new-old) / litre * 0.22, "miles per gallon")


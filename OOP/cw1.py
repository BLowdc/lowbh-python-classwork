class Dog:
    def __init__(self, myName, myColour):
        self.name = myName
        self.colour = myColour
    #end function

    def bark(self, barkTimes):
        for _ in range(0,barkTimes):
            print("Woof")
        #next _
    #end procedure

    # def getName(self):
    #     return self.name
    # #end function

    # def getColour(self):
    #     return self.colour
    # #end function

    # def setColour(self, newColour):
    #     self.colour = newColour
    # #end function
#end class

dogs = []

myDog1 = Dog("Mutt", "Unknown")
myDog2 = Dog("Jeff","Unknown")

dogs.append(myDog1)
dogs.append(myDog2)

print("Dogs: ", dogs)

for dog in dogs:
    if dog.colour == "Unknown":
        colour = input(f"Enter colour for {dog.name}: ")
        dog.colour = colour
        print(f"Name: {dog.name}, Colour: {dog.colour}")
        dog.bark(3)
    #end if
#next dog





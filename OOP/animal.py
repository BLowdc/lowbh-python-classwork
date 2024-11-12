class Animal:
    def __init__(self, myType, myName, mycolour) -> None:
        self.type = myType
        self.name = myName
        self.colour = mycolour
    #end fields

    def eat(self):
        pass
    #end public procedure

    def makeNoise(self):
        pass
    #end public procedure

    def move(self):
        pass
    #end public procedure
#end class

class Dog(Animal):
    pass
#end class

myAnimal = Animal("Unknown","Bart","Black")
print(f"Name: {myAnimal.name}, Type: {myAnimal.type}, Colour: {myAnimal.colour}")
myAnimal.makeNoise()

myDog = Dog("Schnauzer","Dordor","Grey")
print(f"Name: {myDog.name}, Type: {myDog.type}, Colour: {myDog.colour}")

print("End")
    


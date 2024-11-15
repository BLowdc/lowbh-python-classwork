import random
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
    def makeNoise(self):
        print("Woof")
    #end public procedure
#end class

class Cat(Animal):
    def makeNoise(self):
        print("Meow")
    #end public procedure
#end class

# myDog = Dog("Schnauzer","Dordor","Grey")
# print(f"Name: {myDog.name}, Type: {myDog.type}, Colour: {myDog.colour}")
# myDog.makeNoise()

# myCat = Cat("Universe","Annihilator","Black")
# print(f"Name: {myCat.name}, Type: {myCat.type}, Colour: {myCat.colour}")
# myCat.makeNoise()

pets = [None for i in range(10)]

for i in range(10):
    choice = random.randint(0,1)
    match choice:
        case 0:
            dog = Dog("DogName","DogType","DogColour")
            pets[i] = dog
        case 1:
            cat = Cat("CatName","CatType","CatColour")
            pets[i] = cat
        #end case
    #end match
#next i

for pet in pets:
    print(f"Name: {pet.name}, Type: {pet.type}, Colour: {pet.colour}")
    pet.makeNoise()
#next pet
    


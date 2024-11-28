class Building:
    def __init__(self,myHeight,myWidth,myFloors) -> None:
        self.__height = myHeight #private
        self.__width = myWidth #private
        self.__floors = myFloors #private
    #end constructor

    def getHeight(self) -> float:
        return self.__height
    #end method
    def setHeight(self,newHeight) -> None:
        self.__height = newHeight
    #end method

    def getWidth(self) -> float:
        return self.__width
    #end method
    def setWidth(self,newWidth) -> None:
        self.__width = newWidth
    #end method

    def getFloors(self) -> int:
        return self.__floors
    #end method
    def setFloors(self,newFloors) -> None:
        self.__floors = newFloors
    #end method
#end class

class House(Building):
    def __init__(self,myHeight,myWidth,myFloors,myBedrooms,myBathrooms):
        self.__bedrooms = myBedrooms
        self.__bathrooms = myBathrooms
        super().__init__(myHeight,myWidth,myFloors)
    #end constructors

    def getBedrooms(self) -> int:
        return self.__bedrooms
    #end method
    def setBedrooms(self,newBedrooms) -> None:
        self.__bedrooms = newBedrooms
    #end method

    def getBathrooms(self) -> int:
        return self.__bathrooms
    #end method
    def setBathrooms(self,newBathrooms) -> None:
        self.__bathrooms = newBathrooms
    #end method
#end class

my_building = Building(10,5,3)
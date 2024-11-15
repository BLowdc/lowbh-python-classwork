class Member:
    def __init__(self, mySurname, myFirstName, myAnnualFee) -> None:
        self.surname = mySurname
        self.firstName = myFirstName
        self.annualFee = myAnnualFee
    #end init
#end class

class JuniorMember(Member):
    def __init__(self, mySurname, myFirstName, myAnnualFee, myDateOfBirth) -> None:
        super().__init__(mySurname, myFirstName, myAnnualFee)
        self.dateOfBirth = myDateOfBirth
    #end init
#end class

newJM = JuniorMember("Mason", "Harry", 25, "12/12/2004")
print(f"Name: {newJM.firstName} {newJM.surname}, Annual Fee: {newJM.annualFee}, Date of Birth: {newJM.dateOfBirth}")
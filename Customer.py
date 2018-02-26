from Person import *

class Customer(Person):
    def __init__(self, name, birthdate, phoneNumber, address):
        """
        Summary line.
        Initializing the variables.

        Parameters
        ----------
        name: str
            name of the person
        birthdate: str
            birthdate of the person
            passed as MM/DD/YYYY
        phonenumber: int
            phonenumber of the person
        address: str
            address of the person

        Returns
        -------
        Doesn't return anything

        """
        Person.__init__(self, name, birthdate, phoneNumber, address)
        self.isMinor = True if self.getAge() < 18 else False

    def getInfo(self):
        """
        Summary line.
        Returns customer info

        Parameters
        ----------
        None

        Returns
        -------
        Returns # of accounts open
        Types of accounts open
        Initialized customer info

        Does NOT return balances - see getBalance()
        """
        return "Name: {}\nBirthdate: {}\nPhone Number: {}\nAddress: {}\nMinor: {}".format(self.name, self.birthdate, self.phoneNumber, self.address, self.isMinor)

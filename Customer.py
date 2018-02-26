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
    def createAccount(self, acctType):
        # this should return True if account create successful else false
        # SHould be able to create savings and checking, but not loans
        return "NOT YET IMPLEMENTED"

    def checkBalance(self, acct=None):
        if acct == None:
            #If not account is specified check balance for all accounts... or maybe promt the user
            pass
        elif acct == "Savings" or acct == 0:
            pass
        elif acct == "Checking" or acct == 1:
            pass
        elif acct == "Loan" or acct == 2:
            pass
        #return account balance based on input

    def makePayment(self, ammt, acct):
        #allows for making payments on loans ONLY
        pass

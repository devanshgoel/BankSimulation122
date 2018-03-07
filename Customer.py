from Person import *
from Savings import *
from Checking import *

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
        self.accounts = {"Savings": False, "Checking": False, "Loan": False}

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

        Does NOT return balances - see checkBalance()
        """
        return "Name: {}\nBirthdate: {}\nPhone Number: {}\nAddress: {}\nMinor: {}\nAccounts open:{}".format(self.name, self.birthdate, self.phoneNumber, self.address, self.isMinor, self.accounts)

    def __doesExist(self, acct):
        return self.accounts[acct]

    def createAccount(self, acct, bal):
        # this should return True if account create successful else false
        # Should be able to create savings and checking, but not loans
        # SHOULD THERE BE createLoan()?
        #TODO: CHECK FOR MIN BALANCES
        if self.__doesExist(acct):
            return "You already have an account of this type"

        if acct == "Savings" or acct == 0 and self.accounts["Savings"]:
            self.savings = Savings(bal)
            self.accounts["Savings"] = True
        elif acct == "Checking" or acct == 1 and self.account["Checking"]:
            self.checking = Checking(bal)
            self.accounts["Checking"] = True
        elif acct == "Cancel" or acct == "x" or acct == -1:
            return "Create cancelled"
        else:
            acctType = input("Please enter account type (Savings, or Checking): ")
            return self.createAccount(acctType)
        return True

    def checkBalance(self, acct=None):
        numAccts = 0
        for account in self.accounts:
            if self.accounts[account]:
                numAccts += 1

        if numAccts == 0:
            return "Please create an account first"

        if acct == "Cancel" or acct == "x" or acct == -1:
            return "Check cancelled"
        elif self.accounts[acct]:
            return "Your {} account balance is: {}".format(acct.lower(), self.savings.getBalance())
        elif acct == "Checking" or acct == "Savings" or acct == "Loan":
            return "Please create the {} account first".format(acct)
        else:
            acct = input("Please enter account type (Savings, Checking, or Loan): ")
            return self.checkBalance(acct)

        #return account balance based on input

    def depositTo(self, acct):
        pass

    def withdrawFrom(selfm acct):
        pass


    def makePayment(self, ammt):
        #allows for making payments on loans ONLY
        pass

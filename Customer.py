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
        self.accounts = {"Savings": False, "Checking": False, "Loan": False} # this is just an easy way to keep track of what accounts are open

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
        #TODO: Types of accounts open
        Initialized customer info

        Does NOT return balances - see checkBalance()
        """
        exists = []
        for account in self.accounts:
            if self.__doesExist(account):
                exists.append(account)

        return "Name: {}\nBirthdate: {}\nPhone Number: {}\nAddress: {}\nMinor: {}\nAccounts open:{}".format(self.name, self.birthdate, self.phoneNumber, self.address, self.isMinor, ", ".join(exists))

    def __doesExist(self, acct):
        """
        Summary:
            check for account existance
        Description:
            Checks the initialized self.accounts dictionary and returns wether an account exists or not

        Parameters
        _________

        acct: str
            Account type either "Savings" or "Checking" or "Loan"

        Returns
        _______
        Boolean
            Returns True if account exists False if account doesnt exist or doesnt match any keywords

        """
        try:
            return self.accounts[acct]
        except KeyError:
            print("Non-Valid account type {} for doesExist check".format(acct))
            return False

    def createAccount(self, acct, bal):
        # this should return True if account create successful else false
        # Should be able to create savings and checking, but not loans
        # SHOULD THERE BE createLoan()?
        #TODO: CHECK FOR MIN BALANCES
        """
        Summary line.
        Creates various accounts for the user

        Parameters
        ----------
        acct: str
            account type as string either "Savings" or "Checking"
        bal: int
            account starting balance

        Returns
        -------
        True if success False if else

        """
        if self.__doesExist(acct):
            print("You already have an account of this type")
            return False

        if acct == "Savings" or acct == 0 and self.accounts["Savings"]:
            self.savings = Savings(bal)
            self.accounts["Savings"] = True
            return True
        elif acct == "Checking" or acct == 1 and self.account["Checking"]:
            self.checking = Checking(bal)
            self.accounts["Checking"] = True
            return True
        elif acct == "Cancel" or acct == "x" or acct == -1:
            print("Create cancelled")
            return False
        else:
            acctType = input("Please enter account type (Savings, or Checking): ")
            return self.createAccount(acctType)

        return False

    def checkBalance(self, acct=None):
        #TODO: return true and false and just print information since this is a interface class(it interfaces between classes
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

    def askForLoan(self, managerId=0):
        #check for correct manager id before creating loan - or should this all be taken care of from the manager standpoint
        pass

    def depositTo(self, acct, ammt):
        """
        Summary:
            deposits to spefied account
            prints an error on fail

        Parameters
        _________

        acct: str
            Account type either "Savings" or "Checking"
        ammt: int
            Ammount to be deposited to acct

        Returns
        _______
        Boolean
            Returns True on success and False on fail

        """
        if self.__doesExist(acct):
            if acct == "Savings":
                self.savings.deposit(ammt)
                return True
            elif acct == "Checking":
                self.checking.deposit(ammt)
                return True
        else:
            print("No account of {} type exists".format(acct))
            return False

    def withdrawFrom(self, acct, ammt):
        """
        Summary:
            Withdraw from account
            prints an error on fail

        Parameters
        _________

        acct: str
            Account type either "Savings" or "Checking"

        ammt: int
            Ammount to withdraw from acct

        Returns
        _______
        Bool
           Returns true on success false on fail

        """
        if self.__doesExist(acct):
            if acct == "Savings":
                out = self.savings.withdraw(ammt)
                print(out)
                if isinstance(out, int):
                    return True
                else:
                    return False
            elif acct == "Checking":
                out = self.checking.withdraw(ammt)
                print(out)
                if isinstance(out, int):
                    return True
                else:
                    return False
        else:
            print("No account of {} type exists".format(acct))
            return False

    def makePayment(self, ammt):
        #allows for making payments on loans ONLY
        pass

from Account import *

class Savings(Account):
    """Class definition for a savings account"""

    __minBalance = 25 #Min balance in dollars
    __interestRate = .01 #Intrest rate 

    def __init__(self, startingBalance=0):
        Account.__init__(self, startingBalance) # inistialize with the same vars a account

    @classmethod
    def getMinBal(self):
        """Returns minimum account balance of type Int"""
        return self.__minBalance

    def intrest(self): # THis might not be right - we should discuss how to implement this and possible make a setBalance() method for account so we dont have to access hidden variables
        if self.getBalance() >= 0:
            self._Account__balance *= (1+self.__interestRate)
            return True
        else:
            print("You have a negative balance - Interest not applied")
            return False

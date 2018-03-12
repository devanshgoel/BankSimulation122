from Account import *
import datetime

class Savings(Account):
    """Class definition for a savings account"""

    __minBalance = 25 #Min balance in dollars
    __interestRate = .01 #Intrest rate 
    def __init__(self, startingBalance=0):
        Account.__init__(self, startingBalance) # inistialize with the same vars a account
        lastInterestUpdate = (datetime.date.day(), datetime.date.month(), datetime.date.year())

    @classmethod
    def getMinBal(self):
        """Returns minimum account balance of type Int"""
        return self.__minBalance

    def intrest(self): # THis might not be right - we should discuss how to implement this and possible make a setBalance() method for account so we dont have to access hidden variables
        if self.getBalance() >= 0:
            self._Account__balance *= (1+self.__interestRate)
            lastIntrestUpdate = datetime.date.today()
            return True
        else:
            print("You have a negative or zero balance - Interest not applied")
            return False

    def addInterest(self, force=False):
        pass # ignore this function for now
        if force:
            print("Forcefully updating intrest regardless of date")
            intrest()
        else:
            now = (datetime.date.day(), datetime.date.month(), datetime.date.year())
            if now[0] > lastInterestUpdate[0]: # make this work better - check for month/year changes
                print("Updating intrest")



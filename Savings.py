from Account import *

class Savings(Account):
    """Class definition for a savings account"""

    __minBalance = 25 #Min balance in dollars
    __interestRate = 1 #Intrest rate in percent

    def __init__(self, startingBalance=0):
        Account.__init__(self, startingBalance) # inistialize with the same vars a account

    @classmethod
    def getMinBal():
        return __minBalance

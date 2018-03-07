from Account import *

class Savigns(Account):
    """Class definition for a savings account"""

    _minBalance = 25 #Min balance in dollars
    _interestRate = 1 #Intrest rate in percent

    def __init__(self, startingBalance=0):
        Account.__init__(self, startingBalance) # inistialize with the same vars a account

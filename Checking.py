from Account import *

class Checking(Account):
    """Class definition for the checking account object"""
    _minBalance = 25 # min balance - should maybe be implemented in account class
    _minorMaxWithdraw = 100 # max minors can withdraw

    def __init__(self, startingBalance):
        Account.__init__(self, startingBalance) # initialize the same as account

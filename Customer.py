from Person import *
from Checking import *
from Savings import *
from Loan import *

import random

class Customer(Person):
    def __init__(self, name, birthdate, phone, address):
        Person.__init__(self, name, birthdate, phone, address)
        self.__social = random.randint(100000000, 999999999)
        if self.getAge() >= 18:
            self.isMinor = False
        else:
            self.isMinor = True
        
    def __str__(self):
        return 'Customer:\n   Name: {} | Age: {}\n'.format(self.name, self.getAge())

    def getInfo(self):
        return 'Customer:\n'\
             '   Name: {}\n   D.O.B: {}\n   Address: {}\n   Phone #: {}'.format(self.name, self._Person__birthdate, self._Person__address, self._Person__phone)

    def openSavings(self, startBalance=0):
        if hasattr(self, 'savings'):
            return 'This customer already has an active savings account!\n'
        else:
            self.savings = Savings(startBalance)

    def openChecking(self, startBalance=0):
        if hasattr(self, 'checking'):
            return 'This customer already has an active checking account!\n'        
        else:
            self.checking = Checking(startBalance)

    def requestLoan(self, amount, Manager):
        return Manager.giveLoan(self, amount)

    def payLoan(self, payment):
        self.loan.pay(payment)
        return 'Remaining Payment Due: ${}'.format(self.loan.getDues())

    __repr__ = __str__





 











    
        

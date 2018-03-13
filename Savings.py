from Account import *

class Savings(Account):
    """Class definition for a savings account"""
    
    def __init__(self, startingBalance):
        Account.__init__(self, startingBalance)
        if startingBalance < 100:
            self.__interestRate = 0 
        else:
            __interestRate = .02 #Intrest rate 
        __minBalance = 100

    def __str__(self):
        return 'Savings Account:\n   Current Balance: ${}\n   Interest Rate: {}%\n'.format(self._Account__balance, self.__interestRate)

    def withdraw(self, amount):
        confirm = input("Current Balance: ${}\nWould you like to withdraw ${}?(Y/N)\n".format(self._Account__balance, amount))
        if confirm == "Y" or confirm == "y":
            if self._Account__minBalance >= (amount):
                newBalance = self._Account__balance - (amount)
                self._Account__balance = newBalance
                return newBalance
            else:
                return "Not enough funds!\n Current Balance: ${} | Minimum Balance: ${}".format(self._Account__balance, self._Account__minBalance)
        elif confirm == "N" or confirm == "n":
            return "Request Cancelled"
        else:
            self.withdraw(self, amount)

    __repr__ = __str__
 

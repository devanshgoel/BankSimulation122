from Account import *

class Checking(Account):
    """Class definition for the checking account object"""

    def __init__(self, startingBalance):
        Account.__init__(self, startingBalance) # initialize the same as account
        self.__withdrawFee = 2 # 2 dollar withdraw fee
    
    def __str__(self):
        return 'Checking Account:\n   Current Balance: ${}\n   Withdraw Fee: {}'.format(self._Account__balance, self.__withdrawFee)

    def withdraw(self, amount):
        confirm = input("Current Balance: ${}\nWould you like to withdraw ${} (${} service fee)?(Y/N)\n".format(self._Account__balance, amount, self.__withdrawFee))
        if confirm == "Y" or confirm == "y":
            if self._Account__balance >= (amount + self.__withdrawFee):
                newBalance = self._Account__balance - (amount + self.__withdrawFee)
                self._Account__balance = newBalance
                return newBalance
            else:
                return "Not enough funds! (withdraw fee ${})\n Current Balance: ${}".format(self.__withdrawFee, self._Account__balance)
        elif confirm == "N" or confirm == "n":
            return "Request Cancelled"
        else:
            self.withdraw(self, amount)

    __repr__ = __str__

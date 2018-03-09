from Account import *

class Checking(Account):
    """Class definition for the checking account object"""
    __minBalance = 25 # min balance - should maybe be implemented in account class
    __minorMaxWithdraw = 100 # max minors can withdraw
    __withdrawFee = 2 # 2 dollar withdraw fee

    def __init__(self, startingBalance):
        Account.__init__(self, startingBalance) # initialize the same as account

    @classmethod
    def getMinBal(self):
        """Returns minimum balance to open account in type Int"""
        return self.__minBalance

    @classmethod
    def setMinorMax(self, amount):
        if isinstance(amount, int) or isinstance(ammount, float):
            self.__minorMaxWithdraw = amount
            return True
        else:
            print("Please enter ammount as int or float")
            return False

    @classmethod
    def getMinorMax(self):
        return self.__minorMaxWithdraw

    def withdraw(self, amount):
        """
        Summary line.
        Withdraws money from a bank account and reduces that amount from the balance

        Parameters
        ----------
        amount: int
        amount to be withdrawn from the balance
        Returns
        -------
        int
            returns the balance of the account after the amount is withdrawn from it.

        str
            tells the user not enough funds if the amount is more than the balance. returns the current balance.

        """
        confirm = input("Would you like to withdraw ${} with a ${} service fee?(Y/N)".format(amount, self.__withdrawFee))
        if confirm == "Y" or confirm == "y":
            if self._Account__balance >= (amount + self.__withdrawFee):
                newBalance = self._Account__balance - (amount + self.__withdrawFee)
                self._Account__balance = newBalance
                return newBalance
            else:
                return "Not enough funds (Withdraw fee ${}), Current Balance: ${}".format(self.__withdrawFee, self._Account__balance)
        elif confirm == "N" or confirm == "n":
            return "Request Cancelled"
        else:
            self.withdraw(self, amount)

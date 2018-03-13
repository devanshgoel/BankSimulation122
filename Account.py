class Account:
    """ Base account class to define common attributes and methods between savings and checking """
    def __init__(self, startingBalance):
        self.__balance = startingBalance

    def __str__(self):
        return 'Account:\n   Current Balance: ${}\n'.format(self.__balance)

    def getBalance(self):
        return self.__balance

    def withdraw(self, amount):
        if self.__balance >= amount:
            newBalance = self.__balance - amount
            self.__balance = newBalance
            return newBalance
        else:
            return "Not enough funds, Current Balance: " + str(self.__balance)

    def deposit(self, amount):
        balance = self.__balance
        self.__balance = balance+amount
        return self.__balance

    __repr__ = __str__

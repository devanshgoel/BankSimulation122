class Account:
    """ Base account class to define common attributes and methods between savings and checking """
    def __init__(self, startingBalance=0):
        """
        Summary line.
        Initializes the variables for the account class

        Parameters
        ----------
        startingBalance: int
            the starting balance for the account. If the parameter is not passed, the default balance is 0.
        Returns
        -------
        Doesn't return anything

        """
        self.__balance = startingBalance

    def getBalance(self):
        """
        Summary line.
        Checks the current balance of the account and returns it.

        Parameters
        ----------

        Returns
        -------
        int
            returns the balance of the account.

        """
        return self.__balance



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

        str + int
            tells the user not enough funds if the amount is more than the balance. returns the current balance.

        """
        if self.__balance >= amount:
            newBalance = self.__balance - amount
            self.__balance = newBalance
            return newBalance
        else:
            return "Not enough funds, Current Balance: " + self.__balance

    def deposit(self, amount):
        """
        Summary line.
        Adds an amount of money to the current balance.

        Parameters
        ----------
        amount: int
            The amount of money to add to the account balance.
        Returns
        -------
        int
            returns the balance of the account after the amount is added to it.

        """
        balance = self.__balance
        self.__balance = balance+amount
        return self.__balance



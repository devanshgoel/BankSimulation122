class Account:
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
		self.balance = startingBalance
		
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
		if self.__balance >= amount:
			newBalance = self.__balance - amount
			self.__balance = newBalance
			return newBalance
		else:
			return "Not enough funds, Current Balance: " + self.__balance
		
	def deposit(self, amount):
		balance = self.__balance
		self.__balance = balance+amount
		return self.__balance
		
		

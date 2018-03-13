class Loan:
	def __init__(self, amount):
		self.__amount = amount
		self.__dues = amount

	def __str__(self):
		return 'Loan:\n   Amount: ${}\n   Remaining Dues: ${}\n'.format(self.__amount, self.__dues)

	def pay(self, payment):
			self.__dues -= payment

	def getDues(self):
		return self.__dues



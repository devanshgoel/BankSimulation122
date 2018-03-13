from Customer import *
import random

class Teller(Person):
    def __init__(self, name, birthdate, phone, address, salary=4000):
        Person.__init__(self, name, birthdate, phone, address)
        self.__salary = salary
        self.id = self.__createID()
        

    def __str__(self):
        return 'Employee:\n   Role: Teller | Name: {} | Salary: {}/mo | Employee ID: {}\n'.format(self.name, self.__salary, self.id)

    def __createID(self):
        return random.randint(100,999)

    def getInfo(self):
        return 'Employee:\n'\
            '   Role: Teller\n   Name: {}\n   Salary: ${}/mo\n   Employee ID: {}\n'\
            '   D.O.B: {}\n   Address: {}\n   Phone #: {}'.format(self.name, self.__salary, self.id, self._Person__birthdate, self._Person__address, self._Person__phone)

    def getCustInfo(self, Customer):
        return 'Customer:\n   Name: {}\n   Address: {}\n   Phone #: {}'.format(Customer.name, Customer._Person__address, Customer._Person__phone)

    def withdraw(Customer, account, amount):
        Customer.account.withdraw(amount)  

    def deposit(Customer, account, amount):
        Customer.account.deposit(amount)
#--------------------------------------------------------------------------------------------------------------------------
class Manager(Person):
    def __init__(self, name, birthdate, phone, address, salary=7500):
        Person.__init__(self, name, birthdate, phone, address)
        self.__salary = salary
        self.id = self.__createID()

    def __str__(self):
        return 'Employee:\n   Role: Manager | Name: {} | Salary: ${}/mo | Employee ID: {}\n'.format(self.name, self.__salary, self.id)

    def __createID(self):
        return random.randint(100,999)

    def getInfo(self):
        return 'Employee:\n'\
             '   Role: Manager\n   Name: {}\n   Salary: {}/mo\n   Employee ID: {}\n'\
             '   D.O.B: {}\n   Address: {}\n   Phone #: {}'.format(self.name, self.__salary, self.id, self._Person__birthdate, self._Person__address, self._Person__phone)

    def getCustInfo(self, Customer):
        return 'Customer:\n   Name: {}\n   Address: {}\n   Phone #: {}\n   D.O.B: {}\n   SSN: {}\n'.format(Customer.name, Customer._Person__address, Customer._Person__phone, Customer._Person__birthdate, Customer._Customer__social)

    def viewAccounts(self, Customer):
        acc = Customer.name + ':\n'
        if hasattr(Customer,'savings'):
            acc += str(Customer.savings)
        if hasattr(Customer,'checking'):
            acc += str(Customer.checking)

        return acc

    def delSavings(self, Customer):
        if hasattr(Customer, 'savings'):
            del zach.savings
            return Customer.name + "'s savings account has been deleted."
        else:
            return Customer.name + ' does not have an active savings account!'

    def delChecking(self, Customer):
        if hasattr(Customer, 'checking'):
            del zach.savings
            return Customer.name + "'s checking account has been deleted."
        else:
            return Customer.name + ' does not have an active checking account!'

    def openSavings(self, Customer, startBalance):
        Customer.openSavings(startBalance)

    def openChecking(self, Customer, startBalance):
        Customer.openChecking(startBalance)

    def giveLoan(self, Customer, amount):
        if Customer.isMinor:
            return 'Request Denied.'
        else:
            Customer.loan = Loan(amount)
            return 'Request Approved'

    def changeFee(self, Customer, newFee):
        if hasattr(Customer, 'checking'):
            Customer.checking._Checking__withdrawFee = newFee

    def changeIR(self, Customer, newRate):
        if hasattr(Customer, 'savings'):
            Customer.savings._Savings__interestRate = newRate


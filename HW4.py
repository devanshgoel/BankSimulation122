class Customer:
    def __init__(self, name, birthdate, phone, address, age):
        self.name = name
        self.birthdate = birthdate
        self.__phone = phone
        self.__address = address
        self.age = age
        

    def __str__(self):
        return 'Customer:\n   Name: {} | Age: {}\n'.format(self.name, self.age)

    def openSavings(self, startBalance=0):
        self.savings = Savings(self,startBalance)

    def getPhone(self):
        return self.__phone

class Savings:
    def __init__(self, Customer, balance=0):
        self.name = Customer.name
        self.balance = balance 

    def __str__(self):
        return 'Savings:\n   Owner: {} | Balance: ${}\n'.format(self.name, self.balance)

    def withdraw(self, amount):
        self.balance -= amount
        return '{} withdrew ${} > New Balance: ${}'.format(self.name, amount, self.balance)

    def deposit(self, amount):
        self.balance += amount
        return '{} deposited ${} > New Balance: ${}'.format(self.name, amount, self.balance)
    
    def checkBal(self):
        print('Balance: ${}\n'.format(self.balance))




zach = Customer('Zach Hayes', '3/28','4693079235', '33 Wilson', 18)
print(zach)

zach.openSavings(500)
print(zach.savings)
print(zach.savings.withdraw(150))
print(zach.savings.deposit(200))
zach.savings.deposit(50)
zach.savings.checkBal()

print('Phone:',zach.getPhone())

class Manager:
    def __init__(self, name):
        self.name = name

    def custInfo(self, Customer):
        return 'Cutomer:\n   Name: {} | Phone: {}'.format(Customer.name, Customer.getPhone())

class Teller:
    def __init__(self, name):
        self.name = name

    def custInfo(self, Customer):
        return 'Cutomer:\n   Name: {}'.format(Customer.name)

print('\n')
rick = Manager('Rick')
print(rick.custInfo(zach))
sarah = Teller('Sarah')
print(sarah.custInfo(zach))





    
        

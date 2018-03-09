from Customer import *
#Make sure to import all subclasses. We wont need to import parent classes since they *should* be imported in the subclass files
"""
This is where everything should come together
"""


customer1 = Customer("Jake", "02/02/1902", 1231231234, "123 Anywhere USA", 123123123) # an average customer
customer2 = Customer("Mike", "06/12/1933", 1231231316, "125 Anywhere USA", 123121234) # another average customer
customer3 = Customer("Sally", "10/14/2007", 1231231282, "130 Anywhere USA", 124164586) # and a customer that is a minor
def main():
    print("creating savings account for customer1")
    acct1 = customer1.createAccount("Savings", 25)
    print("output =", acct1)
    print("Checking balance for account")
    check = customer1.checkBalance("Savings")
    print("output =", check)
    print("checking for account that doesnt exist for customer")
    check = customer1.checkBalance("Checking")
    print("output =", check)

if __name__ == "__main__":
    main()


# raise and assert keywords are used to generate exceptions by user
def checkPin():
    userPIN = int(input("Enter PIN: "))
    assert userPIN == 1234, "Incorrect PIN"
    # if userPIN != 1234:
    #     raise ValueError('Incorrect PIN')


def checkBalance():
    accountBalance = 10000
    amount = int(input('Enter amount to withdraw: '))
    assert amount <= accountBalance, "Insufficient amount"
    # if amount > accountBalance:
    #     raise TypeError('Insufficient Amount')


def withdraw():
    checkPin()
    checkBalance()
    print("Withdrawal successful...")


try:
    withdraw()

except AssertionError as e:
    print("Exception occured", e)
except ValueError as e:
    print("Value error occured")
    print(e)
except TypeError as e:
    print("Type error occured")
    print(e)
except Exception as e:
    # print("Some exception occured...")
    print(e)

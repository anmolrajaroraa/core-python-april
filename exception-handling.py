# error means compilation error (when we are writing code)
# exception means runtime error (when code is running)
# try block means try to run this code, if any error occurs then send that error to the exception block
# exception blocks will check the type of exception generated and accordingly will handle them
# if no exception occurs try block completes and skips all the except blocks
# code after try,except block will always run because now our program is not going to terminate because of some exception as we are already handling them
# finally block is always going to run after try,except finishes
# else block - it runs when except doesn't run and vice versa
try:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    result = x / y

    print(x / y)

    file = open('crawler.py')
    # file.write('hello')
    file.read()
    # file.close()

except TypeError:
    print("Division can only be done on numbers")
except ZeroDivisionError as ex:
    print("Second number cannot be zero while performing division")
    # print(ex)
except ValueError as ex:
    # print("Please use only integers for input")
    print(ex)
except Exception as ex:
    print("Exception occurred", ex)
else:
    print("Thanks for visiting us...")
finally:
    print("File will always be closed here")

# Exception is a class - it is actually the parent class for all other exception classes - means it can handle exceptions related to itself or  any child class
# Exception class should always be used as the last except otherwise it will handle all the exceptions and other except blocks would never work
# TypeError
# ZeroDivisionError

print("Program is going to terminate...")

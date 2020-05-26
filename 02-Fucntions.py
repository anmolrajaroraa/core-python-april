def takeInput():
    f_num = int(input("Enter first num: "))
    s_num = int(input("Enter second num: "))
    return f_num, s_num


def add():
    x, y = takeInput()
    print(x + y)
    # return x + y


def sub():
    x, y = takeInput()
    # return x - y
    print(x - y)


def mul():
    x, y = takeInput()
    # return x * y
    print(x * y)


def div():
    x, y = takeInput()
    # return x / y
    print(x / y)


def errorHandler():
    print("Wrong choice...")


print('''
    1. Add
    2. Sub
    3. Mul
    4. Div
''')

choice = int(input("Enter your choice: "))
# operations = [add, sub, mul, div]
# operations[choice - 1]()
operations = {
    1: add,
    2: sub,
    3: mul,
    4: div
}
operations.get(choice, errorHandler)()
# fnRefToBeCalled = operations[choice - 1]
# fnRefToBeCalled()


'''if choice == 1:
    result = add()
elif choice == 2:
    result = sub()
elif choice == 3:
    result = mul()
elif choice == 4:
    result = div()
else:
    print("Wrong choice...")
print("Result:", result)'''

'''
def first():
...     print("First fn called...")
... 
>>> def second():
...     print("Second fn called...")
... 
>>> op = [first(), second()]
First fn called...
Second fn called...
>>> op
[None, None]
>>> def second():
...     print("Second fn called...")
...     return 10
... 
>>> op = [first(), second()]
First fn called...
Second fn called...
>>> op
[None, 10]
>>> op = [first, second]
>>> op
[<function first at 0x10f2228c8>, <function second at 0x10f2229d8>]
>>> print
<built-in function print>
>>> op[0]
<function first at 0x10f2228c8>
>>> op[1]
<function second at 0x10f2229d8>
>>> op[1]()
Second fn called...
10
'''

# function - reusable code

# def fn_name(param_1, param_2, param_3):
#     pass

# fn_name(1,2,3)

x = 10
y = 20


# def add2(x, y):  # positional arguments
#     print(x + y)

# def add(x, y=0):  # default argument (they should always come after normal arguments)
#     print(x + y)

# def add0(x=0, y=0):  # default arguments
#     print(x + y)

# def add0(x=0, y=0, *z):  # * -> varargs -> variable arguments (dynamic args)
#     print(x + y)

#  *args -> should always be the last paramter in the args list
# def add(*z):  # * -> varargs -> variable arguments (dynamic args)
#     print(z)

# def add(x, y):
#     return x + y
#     print("Function is going to end")  # unreachable code

# def add(x, y):
#     # fn interleaves from here (result is returned, but fn is not terminated)
#     yield x + y
#     print("Going to perform another operation")
#     yield x - y
#     print("Going to end the fn after doing mul also")
#     yield x * y

def add(x, y, *z):
    # packing (make a tuple)
    return x + y, x - y, x * y, x / y, x ** y, x % y, "Done"

# def add1(x):
#     print(x + 1)


def add3(x, y, z):
    print(x + y + z)
    return None   # implicit last line if you dont write return statemenrt


# def add0():
#     print(0)


def sub(x, y):
    print(x - y)


def mul(x, y):
    print(x * y)


def div(x, y):
    print(x / y)


# add()
# sub()
# mul()
# div()
# add()
# add(10)
# add(100, 200)
# add(10, 20, 30)
# add(10, 20, 30, 40)
# sub(100, 50)
# mul(123, 12)
# div(2525363, 4253)

# result = add(10, 20)
# print("Result is", result)
# result = add(100, 200)
# result object is a generator object ( result after first calculation, checkpoint )
# print(result)
# print(result.__next__())  # add result
# # go back to the checkpoint and fetch the next yielded value
# print(result.__next__())
# print(result.__next__())

# for result in add(100, 200):
#     print(result)

result = add(20, 4)   # use packed result
print(result)
# a = result[0]
# b = result[1]
# a = result[2]
# b = result[3]
*a, b, c, d = add(20, 4)  # unpacking - *args can be placed at any position - sharing basis
print(f"a is {a}, b is {b}, c is {c}, d is {d}")


#   **kwargs -> keyword arguments
# def showEmployeeDetails(id, name, gender, salary, department, *someExtraDetails, **otherDetails):
# def showEmployeeDetails(*details, id, name, gender, salary, department, **otherDetails):
# here *args are going to consume everything - selfishness
def showEmployeeDetails(id, name, gender, salary, department, **otherDetails):
    print("Id is", id)
    print("Name is", name)
    print("Gender is", gender)
    print("Salary is", salary)
    print("Department is", department)
    print("Other Details are", otherDetails)
    # print("Some extra details are", someExtraDetails)


showEmployeeDetails(101, 'Ram Kumar', 'M', 15000, 'IT')
# showEmployeeDetails(101, 'Ram Kumar', 'M', 15000, 'IT', 30, 12, 25)
# showEmployeeDetails(id=101, name="Ram Kumar", age=30,
#                     department='IT', salary=15000)
showEmployeeDetails(101, "Ram Kumar", age=30, leavesLeft=12,
                    department='IT', salary=15000, gender='M', ticketsDone=25)
# positional arguments should always come before keyword arguments
# default argument (they should always come after normal arguments)
#  *args, **kwargs -> should always be the last paramter in the args list

x = 1000  # global variable (can be used anywhere in the file)
y = 10

z = 10


def outer():
    global x
    x = x + 1   # a local variable x is created
    print("outer fn called...", x)

    # local fn (local to outer, means it can be accessed only from within outer fn)
    def inner1():
        print("inner1 fn called...")

    def inner2():
        print("inner2 fn called...")

    # inner1()
    # inner2()
    print("outer fn going to return...")
    return inner1, inner2


result = outer()
# print(result)
result[0]()  # calling inner1() using the fn reference returned
# inner1()

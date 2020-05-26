# map is used when fn returns some value
# map appends the result returned from the fn into a list
# filter is used when fn returns some boolean
# if fn returns true, filter will append the param into the list instead of appending the result


def evenFn(num):
    # return not num % 2 == 0
    return num % 2 == 0 and num % 3 == 0


numbers = range(1, 101)

obj = filter(evenFn, numbers)
# obj = filter( lambda num : num % 2 == 0, numbers)
print(list(obj))

a = 10
b = 20
c = str(a+b)

print("Sum of " + str(a) + " and " + str(b) + " is " + str(a+b) )
print("Sum of", a, "and", b, "is", a + b)

print("Sum of %d and %d is %d"%(a, b, a + b) )
print("Sum of %d and %d is %s"%(a, b, c) )

print("Sum of {} and {} is {}".format(a, b, a + b) )
print("Sum of {} and {} is {}".format(a, b, c) )
print("Sum of {2} and {1} is {0}".format(c, b, a) )

# format the string - fast string
print(f"Sum of {a} and {b} is {a+b}")
print(f"Sum of {a=} and {b=} is c={a+b}")

# spaces - done
# double quotes - done
# plus -> overloaded - done
# type casting - done
# remember the order - done
# index count if variables are too much - not done

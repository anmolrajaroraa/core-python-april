def calc(operator):
    f_num = input("Enter first num: ")
    s_num = input("Enter second num: ")
    expression = f_num + operator + s_num
    print(expression)
    print(eval(expression))


print('''
    1. Add
    2. Sub
    3. Mul
    4. Div
''')

choice = int(input("Enter your choice: "))
operations = {
    1: '+',
    2: '-',
    3: '*',
    4: '/'
}
operator = operations[choice]
calc(operator)

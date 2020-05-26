# def temp_convert(c):
#     return 9 / 5 * c + 32

# functions having only one single statement or having return statement as the first line can be converted into lambda fn (anonymous fns, single-line fns)


temp_list = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 49]

# call temp_convert fn for each value in temp_list and append all the returned results into f_list
# f_list = map(temp_convert, temp_list)

# print(list(f_list))

# lambda fn syntax -> lambda param1, param2, param3 : <return statement>

f_list = map(lambda c: 9 / 5 * c + 32, temp_list)

print(list(f_list))

# f_list = []

# for temp in temp_list:
#     f_list.append(temp_convert(temp))

# print(f_list)

# temp = 45
# print(temp_convert(temp))

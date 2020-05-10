set1 = {1, 2, 3, 4, 5, 5.0, "five", True,
        False, 0, "six", "Ram", "Shyam", "Anna", "Jenny"}
set2 = {1, 2, 3, 4, 5, 5.0, "five", True}
set3 = {False, 0, "six", "Ram"}
print(set1)
# for value in set1:
#     print(value)
set1.add(100)
set1.add(1)
print(set1)
print(set1.difference(set2, set3))
print(set1 - set2 - set3)
print("set1 is", set1)
# set1 = set1.difference(set2)
set1.difference_update(set2)
print("set1 is", set1)

fset = frozenset(set1)
fset.add(10)  # error

# print(dir(set))
#'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'

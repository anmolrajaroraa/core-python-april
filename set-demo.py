set1 = {1, 2, 3, 4, 5, 5.0, "five", True,
        False, 0, "six", "Ram", "Shyam", "Anna", "Jenny"}
set2 = {1, 22, 3, 44, 5, 6.0, "six", True}
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
# set1.difference_update(set2)
print("set1 is", set1)
set1.discard(False)
print("set1 is", set1)
print(set1.intersection(set2))
print(set1.union(set2))
print(set1.isdisjoint(set2))
print(set1.isdisjoint({111, 222, 333}))
print({1, 2, 3, 'Ram', 'Jenny', 'Twinkle'}.issubset(set1))
print(set1.issuperset({1, 2, 3, 'Ram', 'Jenny'}))
print(set1.pop())
print(set1.pop())
print(set1.pop())
print(set1.discard(False))
# print(set1.remove(False))
print((set1 - set2).union(set2 - set1))
print(set1.symmetric_difference(set2))
set1.update(set2)
print("set1 is", set1)

fset = frozenset(set1)
# fset.add(10)  # error

# print(dir(set))
#'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'

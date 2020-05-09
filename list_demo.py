import copy
a = 10
b = 20
# str abc = a > b ? "A is greater": "A is smaller";
message = "A is greater" if a > b else "A is smaller"
print(message)
a = 100
message = "A is greater" if a > b else "A is smaller"
print(message)
a = 20
message = "A is greater" if a > b else (
    "A is equal to B" if a == b else "A is smaller")
print(message)


# list is just like an array, and it is actually built C-array
# list can store any type of elements
# and it is dynamic in size (mutable)

list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5.0]
list3 = [1, 2, 3, "four", 5.0]
list4 = [True, 2, 3, "four", 5.0]
print(list1[0])
print(list2[-1])
print(list3[2:4])
print(list4[2:])
#'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
# append - add the element at the end of the list
list4.append(100)
list4.append([6, 7, 8, 9, 10])
print(list4[6][0])
# extend - merge two lists / extend this list with another one
list4.extend([6, 7, 8, 9, 10])
list4.extend("ten")
print("list4 is", list4)
# delete all the elements from the list
# list4.clear()
list4.append(10)
print("list4 is", list4)
# stop pointing to the list
# list4 = None
# list4.append(10)
list5 = list4
print(list4)
print(list5)
del list4[0]
print(list4)
print(list5)
list6 = list4.copy()
print("list4 is", list4)
print("list6 is", list6)
del list4[0]
print("list4 is", list4)
print("list6 is", list6)
print(id(list4[4]))
print(id(list6[5]))
del list4[4][0]
print("list4 is", list4)
print("list6 is", list6)
list7 = copy.deepcopy(list4)
print("list4 is", list4)
print("list7 is", list7)
print(id(list4[4]))
print(id(list7[4]))
del list4[4][0]
print("list4 is", list4)
print("list7 is", list7)
print(list7.count(7))
print(list7.index(7))
print(list7.index([7, 8, 9, 10]))
# insert - inserts element at a specific index
list7.insert(1, 1000)
print("list7 is", list7)
list7[1] = 2000
print("list7 is", list7)
print(list7.pop())
print(list7.pop())
print("list7 is", list7)
print(list7.pop(1))
list7.remove('four')
list7.remove(6)
print("list7 is", list7)
list7.reverse()
print(list7)
list7.remove([7, 8, 9, 10])
list7.sort(reverse=True)
print(list7)
# tuple is just like list, but there are some differences
# [] -> ()
# tuple is immutable, tuple is like fixed list
tuple1 = (1, 2, 3, 4)
# del tuple1[0]
print(dir(tuple))

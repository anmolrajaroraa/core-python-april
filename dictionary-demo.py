student_info = [49, "Ram", "12", "Non-medical", 65, 45, 76, 56, 54, 34]
student = {
    "roll_no": 49,
    "name": "Ram",
    "class": 12,
    "stream": "Non-medical",
    "attendance": 65,
    "marks": {
        "english": 76,
        "physics": 45,
        "chemistry": 56,
        "maths": 54,
        "computer science": 34
    }
}

print(student["name"])
print(student["marks"]["english"])
del student["attendance"]
student["attd"] = 75
student["attd"] = 76
print(student)


print(student.keys())
for i in range(len(student_info)):
    print(f"element at {i} index is {student_info[i]}")

for value in student_info:
    print(value)

for i, value in enumerate(student_info):
    print(i, value)

for key in student:
    print(f"value of {key} is {student[key]}")

for value in student.values():
    print(value)

for pair in student.items():
    print(pair)

product1 = ["OnePlus 8", 50000, "Quad Cam", "Snapdragon 900", 512]
product2 = ["Redmi 10", 30000, "108 MP Quad Cam", "AMD A10", 256]

for i, j in zip(product1, product2):
    print(i, " -- ", j)

# print(f"element at {i} index is {student_info[i]}")
# print("element at {} index is {}".format(i, student_info[i]))

print('''
Roll no is {}
Name is {},
Class is {},
Stream is {},
Marks is {},
Attendance is {}
''' .format(student["roll_no"], student["name"], student["class"], student["stream"], student["marks"], student["attd"]))

print('''
Roll no is {roll_no}
Name is {name},
Class is {class},
Stream is {stream},
Marks is {marks},
Attendance is {attd}
'''.format_map(student))


print(dir(dict))
#'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

keys = student.keys()
raw_student = dict.fromkeys(keys, "NA")
raw_student["roll_no"] = 102
print(raw_student)
print(raw_student.get("roll_no"))
print(raw_student.pop("attd"))
print(raw_student.popitem())
print(raw_student.setdefault("roll_no", 103))
print(raw_student.setdefault("eno", 103))
print(student)
print(raw_student)
student.update(raw_student)
print(student)

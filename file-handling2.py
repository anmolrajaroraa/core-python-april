import csv

database = [
    {
        "name": "Ram Kumar",
        "email": "ram@gmail.com",
        "password": "ram1234"
    },
    {
        "name": "Shyam",
        "email": "shyam@gmail.com",
        "password": "shyam1234"
    },
    {
        "name": "Jenny",
        "email": "jenny@gmail.com",
        "password": "jenny1234"
    }
]

# fileStream = open("users.csv", "a")

# with open("users.csv", "a", newline='') as fileStream:  # av,anvn,
#     writer = csv.writer(fileStream)
#     for user in database:
#         writer.writerow(user.values())

with open("users.csv") as fileStream:
    data = csv.reader(fileStream)
    # print(data)
    for row in data:
        print(row)


# comma separated values -
# Jenny,jenny@gmail.com,jenny1234

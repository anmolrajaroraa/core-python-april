# register -> name, email, password
# verify email -> email should not exist already in our database
# store data in database - register user
# welcome {username}
# login -> email, password
# verify email -> email should exist already
# verify password -> password and email in our database should match to the user's input
# welcome {username}

# if-else
# if this condition is true then run this logic
# if the condition specified is false then run this logic (last case)

# for-else
# for - just a loop
# else - I am attached with for loop, if for loop continues and ends normally then I'll also run
# else - If because of some condition you break the loop (for loop dies) then I'll also die (else block will not run)

# list of dictionaries (list of users, a dictionary represents a user's data)
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

while True:
    print('''
        1. Login
        2. Register
    ''')
    choice = int(input("Enter your choice: "))
    if choice != 1 and choice != 2:  # condition for invalid input
        print("Invalid choice")
        continue

    if choice == 1:
        # isLoginSuccesful = False  # flag variable
        emailInput = input("Enter email address: ")
        passwordInput = input("Enter password: ")
        for user in database:
            if user["email"] == emailInput:
                if user["password"] == passwordInput:
                    print(f"Welcome {user['name']}")
                else:
                    print("Invalid password")
                break
        else:
            print("Email not found")
        # print(f"Welcome {user['name']}") if isLoginSuccesful else print(
        #     "Invalid credentials")

    else:
        emailExists = False
        nameInput = input("Enter name: ")
        emailInput = input("Enter email address: ")
        passwordInput = input("Enter password: ")
        for user in database:
            if user['email'] == emailInput:
                print("Email id already exists! Please login...")
                break
        else:
            user = {
                "name": nameInput,
                "email": emailInput,
                "password": passwordInput
            }
            database.append(user)
            print(database)
            print(f"Registration Successful. Welcome {nameInput}...")

# num = 17 // 2 -> 8
# 17 % 2 -> 1
# 17 % 3 -> 2
# 17 % 4 -> 1
# 17 % 5 -> 2
# 17 % 6 -> 5
# 17 % 7 -> 3
# 17 % 8 -> 1
# for i in range(2, (num // 2) + 1)

# register -> name, email, password
# verify email -> email should not exist already in our database
# store data in database - register user
# welcome {username}
# login -> email, password
# verify email -> email should exist already
# verify password -> password and email in our database should match to the user's input
# welcome {username}

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
        isLoginSuccesful = False  # flag variable
        emailInput = input("Enter email address: ")
        passwordInput = input("Enter password: ")
        for user in database:
            if user["email"] == emailInput:
                if user["password"] == passwordInput:
                    isLoginSuccesful = True
                break
        print(f"Welcome {user['name']}") if isLoginSuccesful else print(
            "Invalid credentials")

    else:
        nameInput = input("Enter name: ")
        emailInput = input("Enter email address: ")
        passwordInput = input("Enter password: ")
        for user in database:
            if user['email'] == emailInput:
                print("Email id already exists! Please login...")
                break
        user = {
            "name": nameInput,
            "email": emailInput,
            "password": passwordInput
        }
        database.append(user)

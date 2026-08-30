# SDEV 245 - Authentication and Role-Based Access Control
# Author: Joel Cooper

# Store usernames, passwords, and roles
users = {
    "JCooperAdmin": {
        "password": "Test1234*",
        "role": "admin"
    },
    "JCooperUser": {
        "password": "1234*Test",
        "role": "user"
    }
}

print("====================================")
print("       User Login System")
print("====================================")

# Ask the user for login information
username = input("Enter username: ")
password = input("Enter password: ")

# Check if the username exists
if username in users:

    # Check if the password is correct
    if password == users[username]["password"]:

        role = users[username]["role"]

        print("\nLogin successful!")
        print(f"Welcome, {username}.")
        print(f"Role: {role}")

        # Role-Based Access Control
        if role == "admin":
            print("\nAdmin Area: Access granted.")
            print("User Area: Access granted.")

        elif role == "user":
            print("\nAdmin Area: Access denied.")
            print("User Area: Access granted.")

    else:
        print("\nERROR: Incorrect password.")

else:
    print("\nERROR: Username not found.")
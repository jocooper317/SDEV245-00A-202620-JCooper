# SDEV 245 - Role-Based Access Control Demo

# Hardcoded users and their roles
users = {
    "JCooperAdmin": "admin",
    "JCooperUser": "user"
}

# Simulated login
# Change this username to test each user
username = "JCooperUser"

print("Role-Based Access Control Demo")
print("--------------------------------")

# Authentication check
if username in users:
    role = users[username]

    print("Login successful.")
    print(f"Username: {username}")
    print(f"Role: {role}")
    print()

    # Protected admin action
    if role == "admin":
        print("Admin Area: Access granted.")
    else:
        print("Admin Area: Access denied.")

    # Protected user action
    if role == "user":
        print("User Area: Access granted.")
    else:
        print("User Area: Access denied.")

else:
    print("Login failed. User was not found.")


##  CIA Triad - Confidentiality
#
# This application demonstrates confidentiality by restricting access
# based on the user's assigned role. An admin can access the admin area,
# while a regular user is denied access and vice versa. 
# This helps prevent unauthorized users from accessing protected resources.
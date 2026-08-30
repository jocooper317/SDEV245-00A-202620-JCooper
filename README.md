# SDEV245-00A-202620-JCooper
Github for class - Security and Secure Coding OLCP

# Role-Based Access Control Demo

## About the Project

This Python program demonstrates basic authentication and role-based access control. The program uses two hardcoded users with different roles to show how a user's role determines what parts of an application they are allowed to access.

The two users are:

* **JCooperAdmin** - Admin role
* **JCooperUser** - User role

The username can be changed in the Python code to simulate logging in as either user.

## Authentication

Authentication determines who the user is. The program checks the username against the users stored in a Python dictionary. If the username exists, the login is successful and the program determines the user's assigned role. If the username does not exist, the program displays a login failure message.

## Role-Based Access Control

After authentication, the program uses the user's role to determine what they are allowed to access.

The **admin** role is allowed to access the Admin Area but is denied access to the User Area.

The **user** role is allowed to access the User Area but is denied access to the Admin Area.

This demonstrates the difference between authentication and access control. Authentication verifies who the user is, while access control determines what that user is allowed to do.

## CIA Triad

This application demonstrates **Confidentiality**, one of the three parts of the CIA triad. Confidentiality focuses on preventing unauthorized users from accessing protected information or resources.

The program demonstrates confidentiality by restricting access based on the user's assigned role. An admin can access the protected Admin Area, while a regular user is denied access. Likewise, the User Area is restricted to users with the user role. This helps prevent users from accessing areas they are not authorized to use.

## Running the Program

1. Open the project in Visual Studio Code.
2. Open the Python file.
3. Change the hardcoded username to either `JCooperAdmin` or `JCooperUser`.
4. Save the file.
5. Run the Python program.
6. View the login and access-control results in the terminal.

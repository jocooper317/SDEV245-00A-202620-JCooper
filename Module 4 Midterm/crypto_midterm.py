# SDEV 245 - Cryptography Midterm
# Joel Cooper

import hashlib
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature


# --------------------------------
# CAESAR CIPHER FUNCTION
# --------------------------------

def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():

            if char.isupper():
                start = ord("A")
            else:
                start = ord("a")

            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char

        else:
            result += char

    return result


# --------------------------------
# USER LOGIN AND ROLES
# --------------------------------

# Hardcoded users with SHA-256 hashed passwords and assigned roles
users = {
    "JCooperAdmin": {
        "password": hashlib.sha256("Admin123".encode()).hexdigest(),
        "role": "admin"
    },
    "JCooperUser": {
        "password": hashlib.sha256("User123".encode()).hexdigest(),
        "role": "user"
    }
}

print("SDEV 245 - Cryptography Midterm")
print("--------------------------------")

username = input("Username: ")
password = input("Password: ")

# Hash the password entered by the user
password_hash = hashlib.sha256(password.encode()).hexdigest()

# Check username and password
if username in users and users[username]["password"] == password_hash:

    # Get the user's assigned role
    role = users[username]["role"]

    print()
    print("Login successful!")
    print(f"Welcome, {username}.")
    print(f"Role: {role}")

else:
    print()
    print("Login failed. Invalid username or password.")
    exit()


# --------------------------------
# MAIN MENU LOOP
# --------------------------------

while True:

    print()
    print("Cryptography Menu")
    print("------------------")
    print("1. Generate SHA-256 Hash")
    print("2. Caesar Cipher - Encrypt")

    # Only administrators can see options 3 and 4
    if role == "admin":
        print("3. Caesar Cipher - Decrypt")
        print("4. Digital Signature")

    print("5. Exit")

    choice = input("Enter your choice: ")


    # --------------------------------
    # OPTION 1 - SHA-256 HASH
    # --------------------------------

    if choice == "1":
        print()
        print("SHA-256 Hash Generator")
        print("----------------------")

        message = input("Enter a message to hash: ")

        # Generate the SHA-256 hash
        message_hash = hashlib.sha256(message.encode()).hexdigest()

        print()
        print("Original Message:")
        print(message)

        print()
        print("SHA-256 Hash:")
        print(message_hash)

        input("\nPress Enter to return to the menu...")


    # --------------------------------
    # OPTION 2 - CAESAR ENCRYPTION
    # --------------------------------

    elif choice == "2":
        print()
        print("Caesar Cipher - Encrypt")
        print("-----------------------")

        message = input("Enter a message to encrypt: ")
        shift = int(input("Enter shift value: "))

        # Encrypt the message
        encrypted_message = caesar_cipher(message, shift)

        print()
        print("Original Message:")
        print(message)

        print()
        print("Encrypted Message:")
        print(encrypted_message)

        input("\nPress Enter to return to the menu...")


    # --------------------------------
    # OPTION 3 - CAESAR DECRYPTION
    # ADMIN ONLY
    # --------------------------------

    elif choice == "3":

        # Check authorization
        if role != "admin":
            print()
            print("Access denied.")
            print("Administrator privileges are required.")

            input("\nPress Enter to return to the menu...")
            continue

        print()
        print("Caesar Cipher - Decrypt")
        print("-----------------------")

        message = input("Enter a message to decrypt: ")
        shift = int(input("Enter shift value: "))

        # Decrypt by reversing the shift
        decrypted_message = caesar_cipher(message, -shift)

        print()
        print("Encrypted Message:")
        print(message)

        print()
        print("Decrypted Message:")
        print(decrypted_message)

        input("\nPress Enter to return to the menu...")


    # --------------------------------
    # OPTION 4 - DIGITAL SIGNATURE
    # ADMIN ONLY
    # --------------------------------

    elif choice == "4":

        # Check authorization
        if role != "admin":
            print()
            print("Access denied.")
            print("Administrator privileges are required.")

            input("\nPress Enter to return to the menu...")
            continue

        print()
        print("Digital Signature")
        print("-----------------")

        message = input("Enter a message to digitally sign: ")
        message_bytes = message.encode()

        # Generate a 2048-bit RSA private key
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )

        # Generate the public key from the private key
        public_key = private_key.public_key()

        # Sign the original message using the private key
        signature = private_key.sign(
            message_bytes,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

        print()
        print("Private and public RSA keys generated.")
        print("Message successfully signed.")

        print()
        print("Digital Signature:")
        print(signature.hex())

        # Ask if the user wants to alter the message
        print()
        tamper = input(
            "Would you like to alter the message "
            "before verification? (y/n): "
        )

        if tamper.lower() == "y":

            verify_message = input("Enter the altered message: ")
            verify_message_bytes = verify_message.encode()

            print()
            print("The message has been altered.")

        else:

            verify_message_bytes = message_bytes

            print()
            print("The original message will be verified.")

        # Verify the digital signature using the public key
        try:

            public_key.verify(
                signature,
                verify_message_bytes,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )

            print()
            print("Signature verification: PASSED")
            print("The message is authentic and has not been changed.")

        except InvalidSignature:

            print()
            print("Signature verification: FAILED")
            print("The message or signature has been changed.")

        input("\nPress Enter to return to the menu...")


    # --------------------------------
    # OPTION 5 - EXIT
    # --------------------------------

    elif choice == "5":

        print()
        print("Program closed.")
        break


    # --------------------------------
    # INVALID MENU OPTION
    # --------------------------------

    else:

        print()
        print("Invalid selection. Please choose a valid menu option.")

        input("\nPress Enter to return to the menu...")
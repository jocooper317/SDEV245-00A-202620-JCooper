import hashlib

# Part 1: SHA-256 Hash Generator
print("SHA-256 Hash Generator")
print("----------------------")

# Ask the user for text to hash
message = input("Enter text to hash: ")

# Convert the text to bytes and generate the SHA-256 hash
hash_value = hashlib.sha256(message.encode()).hexdigest()

print()
print("Original text:")
print(message)

print()
print("SHA-256 Hash:")
print(hash_value)

# Part 2: SHA-256 File Hashing
print()
print("SHA-256 File Integrity Check")
print("----------------------------")

# Open the file in binary mode
with open("Test1.txt", "rb") as file:
    file_data = file.read()

# Generate the SHA-256 hash of the file
file_hash = hashlib.sha256(file_data).hexdigest()

print("File: Test1.txt")
print("SHA-256 Hash:")
print(file_hash)

# Part 3: Caesar Cipher Encryption

print()
print("Caesar Cipher Encryption")
print("------------------------")

# Ask the user for a message
message = input("Enter a message to encrypt: ")

# Ask how many positions to shift each letter
shift = int(input("Enter shift amount: "))

encrypted_message = ""

# Go through each character in the message
for char in message:

    # Encrypt uppercase letters
    if char.isupper():
        encrypted_message += chr(
            (ord(char) - ord('A') + shift) % 26 + ord('A')
        )

    # Encrypt lowercase letters
    elif char.islower():
        encrypted_message += chr(
            (ord(char) - ord('a') + shift) % 26 + ord('a')
        )

    # Leave spaces, numbers, and symbols unchanged
    else:
        encrypted_message += char

print()
print("Original Message:")
print(message)

print("Encrypted Message:")
print(encrypted_message)

# Part 4: Caesar Cipher Decryption

print()
print("Caesar Cipher Decryption")
print("------------------------")

# Ask the user for an encrypted message
encrypted_text = input("Enter a message to decrypt: ")

# Ask for the shift amount that was used to encrypt it
shift = int(input("Enter shift amount: "))

decrypted_message = ""

# Go through each character in the encrypted message
for char in encrypted_text:

    # Decrypt uppercase letters
    if char.isupper():
        decrypted_message += chr(
            (ord(char) - ord('A') - shift) % 26 + ord('A')
        )

    # Decrypt lowercase letters
    elif char.islower():
        decrypted_message += chr(
            (ord(char) - ord('a') - shift) % 26 + ord('a')
        )

    # Leave spaces, numbers, and symbols unchanged
    else:
        decrypted_message += char

print()
print("Encrypted Message:")
print(encrypted_text)

print("Decrypted Message:")
print(decrypted_message)
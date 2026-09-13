import hashlib

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

print()
print("SHA-256 File Integrity Check")
print("----------------------------")

# Open the file in binary mode
with open("Message.txt", "rb") as file:
    file_data = file.read()

# Generate the SHA-256 hash of the file
file_hash = hashlib.sha256(file_data).hexdigest()

print("File: Message.txt")
print("SHA-256 Hash:")
print(file_hash)
# SDEV 245 - Encryption and Access Control Demo

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes


# ----------------------------------------------------
# USERS AND ROLE-BASED ACCESS CONTROL
# ----------------------------------------------------

# Hardcoded users and their roles
users = {
    "JCooperAdmin": "admin",
    "JCooperUser": "user"
}

# Simulated login
# Change this username to test each user
username = "JCooperUser"

print("SDEV 245 Security Demo")
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

    print()
    print("--------------------------------")
    print("SYMMETRIC ENCRYPTION")
    print("--------------------------------")

    # ----------------------------------------------------
    # SYMMETRIC ENCRYPTION
    # ----------------------------------------------------

    # Generate one shared symmetric key
    symmetric_key = Fernet.generate_key()

    # Create the encryption object
    cipher = Fernet(symmetric_key)

    # Message to encrypt
    symmetric_message = "This is a confidential message."

    # Encrypt the message
    encrypted_symmetric = cipher.encrypt(
        symmetric_message.encode()
    )

    # Decrypt the message
    decrypted_symmetric = cipher.decrypt(
        encrypted_symmetric
    ).decode()

    # Display required information
    print(f"Key: {symmetric_key.decode()}")
    print(f"Input: {symmetric_message}")
    print(f"Encrypted Output: {encrypted_symmetric.decode()}")
    print(f"Decrypted Output: {decrypted_symmetric}")

    print()
    print("--------------------------------")
    print("ASYMMETRIC ENCRYPTION")
    print("--------------------------------")

    # ----------------------------------------------------
    # ASYMMETRIC ENCRYPTION
    # ----------------------------------------------------

    # Generate RSA private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    # Generate public key from private key
    public_key = private_key.public_key()

    # Convert keys to readable text for demonstration
    private_key_text = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ).decode()

    public_key_text = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ).decode()

    # Message to encrypt
    asymmetric_message = "This message uses RSA encryption."

    # Encrypt using the public key
    encrypted_asymmetric = public_key.encrypt(
        asymmetric_message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(
                algorithm=hashes.SHA256()
            ),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Decrypt using the private key
    decrypted_asymmetric = private_key.decrypt(
        encrypted_asymmetric,
        padding.OAEP(
            mgf=padding.MGF1(
                algorithm=hashes.SHA256()
            ),
            algorithm=hashes.SHA256(),
            label=None
        )
    ).decode()

    # Display required information
    print("Public Key:")
    print(public_key_text)

    print("Private Key:")
    print(private_key_text)

    print(f"Input: {asymmetric_message}")
    print(f"Encrypted Output: {encrypted_asymmetric.hex()}")
    print(f"Decrypted Output: {decrypted_asymmetric}")

else:
    print("Login failed. User was not found.")
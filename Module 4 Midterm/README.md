# SDEV 245 Cryptography Midterm

## Testing Results Google Drive Link
https://drive.google.com/drive/folders/1hHovDTOrbA7t0hgoyUC-B9rTQTAxEc61?usp=drive_link

## Overview

This project is showing a Python application includes user authentication, role-based access control, SHA-256 hashing, Caesar cipher encryption and decryption, and RSA digital signatures.

The application begins by requiring the user to log in. After successful authentication, the application determines the user's assigned role and displays the cryptography options that the user is authorized to access.

The application contains two roles:

* Admin: Has access to all four cryptography functions.
* User: Has access to SHA-256 hashing and Caesar cipher encryption only.

After completing an option, the program returns to the main menu and continues running until the user chooses to exit.

## Program Features

### 1. User Authentication and Role-Based Access Control

The program begins by requiring the user to enter a username and password. Two accounts are hardcoded into the application for demonstration purposes.

Each account contains a SHA-256 password hash and an assigned role.

The two roles are:

* `admin`
* `user`

When a password is entered, the program uses Python's `hashlib` library to generate a SHA-256 hash of the entered password. The generated hash is compared with the hash associated with the username.

If the username and password are correct, authentication succeeds and the program retrieves the user's assigned role. If the credentials are incorrect, access is denied and the program closes.

The admin account has access to:

1. Generate SHA-256 Hash
2. Caesar Cipher - Encrypt
3. Caesar Cipher - Decrypt
4. Digital Signature
5. Exit

The regular user account has access to:

1. Generate SHA-256 Hash
2. Caesar Cipher - Encrypt
3. Exit

Options 3 and 4 are hidden from regular users. The program also performs an authorization check if a regular user manually enters `3` or `4`. If this occurs, the program displays an access denied message and returns the user to the menu.

This demonstrates the difference between authentication and authorization. Authentication determines whether the username and password are valid, while authorization determines which functions an authenticated user is permitted to access.

## 2. SHA-256 Hash Generator

The first menu option allows an authenticated user to enter a message and generate its SHA-256 hash.

The program uses Python's `hashlib` library:

`hashlib.sha256(message.encode()).hexdigest()`

The message is first converted into bytes and then processed by SHA-256. The resulting 256-bit hash is displayed as a 64-character hexadecimal value.

The same exact input will produce the same SHA-256 hash. However, changing the input will cause the resulting hash to change.

This demonstrates how hashing can be used to help verify data integrity. A hash can be calculated before and after storing or transferring data. If the hashes are different, the data has changed.

## 3. Caesar Cipher Encryption

The second menu option allows both admin and regular users to encrypt a message using a Caesar cipher.

A Caesar cipher is a simple substitution cipher that shifts each letter by a specified number of positions in the alphabet.

The user enters:

* A plaintext message
* A shift value

For example, using a shift value of `3`:

`Hello World`

becomes:

`Khoor Zruog`

The program preserves spaces, numbers, and punctuation while shifting alphabetic characters.

The Caesar cipher demonstrates the basic concept of converting readable plaintext into ciphertext. However, Caesar ciphers are not secure enough to protect sensitive information in modern real-world applications.

## 4. Caesar Cipher Decryption

Caesar cipher decryption is restricted to users with the `admin` role.

The administrator enters the encrypted message and the shift value that was originally used to encrypt it. The program reverses the shift to recover the original plaintext.

For example:

`Khoor Zruog`

using a shift value of `3` becomes:

`Hello World`

This demonstrates how encrypted information can be returned to its original readable form when the correct method and shift value are known.

If a regular user attempts to access this option by manually entering `3`, the program denies access because administrator privileges are required.

## 5. RSA Digital Signature

The digital signature feature is also restricted to the `admin` role.

The program uses Python's `cryptography` library to generate a **2048-bit RSA private key**. A corresponding public key is then derived from the private key.

The administrator enters a message to digitally sign. The private key creates the digital signature using:

* RSA public-key cryptography
* RSA-PSS padding
* SHA-256

The program then uses the corresponding public key to verify the signature.

If the original message has not been changed, the program displays:

`Signature verification: PASSED`

The program also allows the administrator to intentionally alter the message after the signature has been created.

If the message is changed and the original signature is used for verification, the program displays:

`Signature verification: FAILED`

This demonstrates how digital signatures can provide integrity and authenticity. If signed information is modified, the original digital signature will no longer successfully verify against the altered message.

The RSA keys are generated when the digital signature option is selected and are used for that signing and verification demonstration. The program does not save the RSA keys to files for later use.

## Randomness, Entropy, and Key Generation

Entropy refers to the amount of unpredictability in the random values used by cryptographic systems. Good entropy is important because cryptographic keys need to be generated using secure and unpredictable values.

If cryptographic key generation is predictable, an attacker may have a better chance of guessing or reproducing a key.

In this application, the digital signature feature uses Python's `cryptography` library to generate a 2048-bit RSA private key:

`rsa.generate_private_key()`

The program does not ask the user to manually create the RSA private key. Instead, the cryptography library generates the key using secure randomness. A corresponding public key is then derived from the private key.

The private key is used to create the digital signature, while the public key is used to verify the signature.

The application also uses RSA-PSS padding. RSA-PSS incorporates a random salt into the signing process. Because of this randomness, signing the same message multiple times can produce different valid signatures while each valid signature can still be verified using the corresponding public key.

Using secure randomness and proper key generation makes cryptographic keys and operations more difficult for an attacker to predict.

## CIA Triad

This application demonstrates concepts related to the three parts of the CIA triad: Confidentiality, Integrity, and Availability.

### Confidentiality

The program supports confidentiality through authentication and role-based access control.

A user must provide valid credentials before accessing the application. After authentication, the user's role determines which functions they are authorized to use.

The regular user is limited to SHA-256 hashing and Caesar cipher encryption. Caesar cipher decryption and RSA digital signatures are restricted to administrators.

The Caesar cipher also demonstrates the basic concept of transforming readable plaintext into ciphertext. Although a Caesar cipher is not considered secure for modern sensitive information, it provides a simple demonstration of how encryption can make information less readable to someone without the required shift value.

### Integrity

The SHA-256 feature demonstrates data integrity by generating a hash from input data. If the original information changes, its SHA-256 hash will also change.

The RSA digital signature feature provides another demonstration of integrity. A message is signed using a private key and verified using the corresponding public key.

The application allows the administrator to intentionally change the message after signing it. When the altered message is checked against the original signature, verification fails. This demonstrates how digital signatures can identify modifications to signed data.

### Availability

After a user successfully authenticates, the application makes the functions authorized for that user's role available through the main menu.

The program uses a loop that returns the user to the menu after completing a task. This allows an authorized user to continue accessing available functions until they choose to exit the program.

The program therefore demonstrates availability by keeping its permitted cryptography functions accessible to authenticated and authorized users while the application is running.

## Running the Program

Open a terminal in the project folder and run:

`py crypto_midterm.py`

The program will prompt for a username and password.

After successful authentication, the available menu options depend on the user's assigned role.

### Admin Menu

```text
Cryptography Menu
------------------
1. Generate SHA-256 Hash
2. Caesar Cipher - Encrypt
3. Caesar Cipher - Decrypt
4. Digital Signature
5. Exit
```

### User Menu

```text
Cryptography Menu
------------------
1. Generate SHA-256 Hash
2. Caesar Cipher - Encrypt
5. Exit
```

After completing an option, press Enter to return to the main menu.

Select option `5` to exit the application.

## Technologies and Concepts Used

* Python
* Authentication
* Role-Based Access Control (RBAC)
* SHA-256
* Caesar Cipher
* RSA Public-Key Cryptography
* RSA Digital Signatures
* RSA-PSS
* Cryptographic Key Generation
* Entropy and Secure Randomness
* Python `hashlib`
* Python `cryptography` library
* CIA Triad

## Author

Joel Cooper
SDEV 245

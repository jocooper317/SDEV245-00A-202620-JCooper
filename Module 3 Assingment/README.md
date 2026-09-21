# SDEV 245 - Secure Hashing and Encryption

## Overview

This project demonstrates several basic cryptography concepts using Python and OpenSSL. The program demonstrates SHA-256 hashing, file integrity checking, Caesar cipher encryption and decryption, and digital signatures using a public and private key pair.

## SHA-256 Hashing

The Python program uses the `hashlib` library to generate a SHA-256 hash from text entered by the user.

The text is converted into bytes and then processed using the SHA-256 hashing algorithm. The resulting hash is displayed as a hexadecimal value.

The program also generates a SHA-256 hash for a text file called `Test1.txt`. Demonstrating how hashing can be used to check file integrity. If the contents of the file are changed, even slightly, the SHA-256 hash will also change.

## Caesar Cipher

The program includes a Caesar cipher that can encrypt and decrypt text.

The user enters a message and chooses a shift amount. During encryption, each letter is shifted forward through the alphabet by the selected amount.

For example, using a shift of 3:

Hello World → Khoor Zruog

The decryption portion reverses the process by shifting the letters backward using the same shift amount.

Spaces, numbers, and special characters are left unchanged.

## Digital Signature

OpenSSL is used to demonstrate how digital signatures work.

First, an RSA private key is generated. A public key is then created from the private key.

The private key is used to digitally sign `Message.txt` using SHA-256. OpenSSL creates a signature file called `signature.bin`.

The public key can then be used to verify the signature.

If `Message.txt` has not been changed since it was signed, OpenSSL displays:

`Verified OK`

If the contents of the file are changed after the signature was created, verification will fail. This demonstrates how digital signatures can help verify the integrity and authenticity of information.

## OpenSSL Commands

Generate the private key:

`openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:2048`

Generate the public key:

`openssl pkey -in private_key.pem -pubout -out public_key.pem`

Sign the file:

`openssl dgst -sha256 -sign private_key.pem -out signature.bin Message.txt`

Verify the signature:

`openssl dgst -sha256 -verify public_key.pem -signature signature.bin Message.txt`

## Files

- `SDEV 245 - Secure Hashing and Encryption.py` - Main Python program
- `Message.txt` - File used for SHA-256 hashing and digital signature testing
- `private_key.pem` - RSA private key used to create the digital signature
- `public_key.pem` - RSA public key used to verify the digital signature
- `signature.bin` - Digital signature generated for Message.txt

## Author

Joel Cooper  
SDEV 245
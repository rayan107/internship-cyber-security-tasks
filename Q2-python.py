import string
import random

# Shared secret key (password agreed upon by sender and receiver)
password = "mysecretkey123"

# Define the character set to support
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

# Generate a reproducible key from the password
def create_key(password):
    seed = sum(ord(char) for char in password)
    shuffled = chars.copy()
    random.seed(seed)  # Seed random with password-derived number
    random.shuffle(shuffled)
    return shuffled

# Build encryption and decryption functions
def encrypt(message, key):
    return ''.join(key[chars.index(c)] for c in message)

def decrypt(cipher, key):
    return ''.join(chars[key.index(c)] for c in cipher)

# Create the key using the shared password
key = create_key(password)

# Input and process
plain_text = input("Enter a message to encrypt: ")
cipher_text = encrypt(plain_text, key)
print(f"Encrypted message: {cipher_text}")

# Decrypt the same message
decrypted_text = decrypt(cipher_text, key)
print(f"Decrypted message: {decrypted_text}")

#SYMETRIC ENCRYPTION

'''
Symmetric encryption is a method of securing data where the same secret key is used for both encryption and decryption. 
This means that both the sender and the receiver must have access to the same key and keep it confidential. 
It's fast and efficient, making it ideal for encrypting large amounts of data. 

Common symmetric encryption algorithms include:
AES (Advanced Encryption Standard) – The most widely used and secure algorithm today.

DES (Data Encryption Standard) – An older standard, now considered insecure due to short key length.

3DES (Triple DES) – A more secure version of DES, but slower and being replaced.

Blowfish – A fast block cipher often used in software encryption.

Twofish – A successor to Blowfish, offering strong encryption with flexible key sizes.

RC4 – A stream cipher now considered obsolete due to security flaws.

ChaCha20 – A modern, fast, and secure stream cipher used in VPNs and TLS.

'''

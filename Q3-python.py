
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# Generate RSA key pair
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()

# Original message
message = b"Asymmetric encryption with RSA!"

# Encrypt with the public key
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("🔒 Encrypted:", ciphertext)

# Decrypt with the private key
plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("🔑 Decrypted:", plaintext.decode())
#ASYMETRIC ENCRYPTION
'''
Asymmetric encryption, also known as public-key cryptography, 
is a method of securing data using a pair of keys: 
a public key for encryption and a private key for decryption. 
The public key can be shared openly, allowing anyone to encrypt a message, 
but only the holder of the corresponding private key can decrypt it—ensuring that the message remains confidential.
This system removes the need for sharing secret keys over insecure channels and is widely used in secure communications (like HTTPS), 
email encryption, and digital signatures. 

Common asymmetric encryption algorithms include:
RSA (Rivest–Shamir–Adleman) – widely used for secure data transmission.

ECC (Elliptic Curve Cryptography) – more efficient and secure with smaller key sizes.

DSA (Digital Signature Algorithm) – mainly used for digital signatures.

ElGamal – used in some encryption systems and digital signature schemes.

Asymmetric encryption is often used in secure communications (like HTTPS), email encryption, and digital signatures
'''

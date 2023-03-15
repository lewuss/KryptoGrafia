import random
from math import gcd

p = 1061
q = 9473
N = p * q
phi = (p - 1) * (q - 1)
e = 7
while gcd(e, phi) != 1:
    e += 2

d = pow(e, -1, phi)


def encrypt(plaintext, public_key):
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext


def decrypt(ciphertext, private_key):
    d, n = private_key
    plaintext = [chr(pow(c, d, n)) for c in ciphertext]
    return ''.join(plaintext)


print("Public key:", e, N)
print("Private key:", d, N)
message = "Hello have a good day"
encrypted_msg = encrypt(message, (e, N))
print(message, " is encrypted into ", encrypted_msg)
print(encrypted_msg, " is decrypted into ", decrypt(encrypted_msg, (d, N)))

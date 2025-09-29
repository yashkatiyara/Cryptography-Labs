# Simple RSA Implementation (Educational)

# Step 1: Two prime numbers
p = 61
q = 53

# Step 2: n and totient
n = p * q
phi = (p-1)*(q-1)

# Step 3: Choose e
e = 17

# Step 4: Modular inverse
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1u
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q*x0, x0
    return x1 + m0 if x1 < 0 else x1

d = mod_inverse(e, phi)

public_key = (e, n)
private_key = (d, n)

# Encryption & Decryption
def encrypt(msg, key):
    e, n = key
    return pow(msg, e, n)

def decrypt(cipher, key):
    d, n = key
    return pow(cipher, d, n)

message = 65
cipher = encrypt(message, public_key)
decrypted = decrypt(cipher, private_key)

print("Public Key:", public_key)
print("Private Key:", private_key)
print("Message:", message)
print("Encrypted:", cipher)
print("Decrypted:", decrypted)

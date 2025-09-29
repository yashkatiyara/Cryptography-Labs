# 🔑 RSA – Asymmetric Cryptography

Welcome to the **RSA module**! 🚀  
This folder contains simple Python programs that demonstrate how the **RSA encryption algorithm** works.  

RSA is one of the most widely used algorithms in modern cryptography. It is the foundation of **secure communication** on the internet (HTTPS, SSL/TLS, digital signatures, etc.).

---

## 📚 Learning Objectives
By the end of this module, you will:
- Understand the **math behind RSA** (prime numbers, modular arithmetic, public/private keys).
- Generate **public and private keys**.
- Encrypt and decrypt messages using RSA.
- Explore real-world applications of RSA.

---

## 📂 Files in this Folder
- `rsa_basic.py` → A step-by-step RSA implementation from scratch.  
- `rsa_with_lib.py` → RSA using Python libraries (`cryptography` or `pycryptodome`).  
- `rsa_experiments.py` → Space for you to try new ideas and experiments.  

---

## 🧠 How RSA Works (Simplified)
1. **Choose two prime numbers** `p` and `q`.  
2. Compute `n = p * q`.  
3. Compute Euler’s Totient: `φ(n) = (p-1) * (q-1)`.  
4. Choose a number `e` such that `1 < e < φ(n)` and `gcd(e, φ(n)) = 1`. (This is your **public exponent**.)  
5. Compute `d` (modular inverse of `e mod φ(n)`). (This is your **private exponent**.)  
6. Keys are:
   - Public Key = `(e, n)`  
   - Private Key = `(d, n)`  
7. Encryption: `cipher = (message ^ e) mod n`  
8. Decryption: `message = (cipher ^ d) mod n`

---

## 🚀 Quick Start

### Run the basic RSA demo
```bash
python rsa_basic.py

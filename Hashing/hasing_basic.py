# Hash Functions Lab

import hashlib
import hmac

# Example string
msg = "hello world".encode()

# Hashing
print("MD5:    ", hashlib.md5(msg).hexdigest())
print("SHA1:   ", hashlib.sha1(msg).hexdigest())
print("SHA256: ", hashlib.sha256(msg).hexdigest())

# HMAC
key = b'secretkey'
h = hmac.new(key, msg, hashlib.sha256)
print("HMAC:   ", h.hexdigest())

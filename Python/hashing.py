import hashlib
password = b"Jovan210507!"
hashed = hashlib.sha256(password).hexdigest()
print(hashed)
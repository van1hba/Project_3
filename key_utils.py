import hashlib

def get_hashed_key(password: str, length: int = 32):
    return hashlib.sha256(password.encode()).digest()[:length]

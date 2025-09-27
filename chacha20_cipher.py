from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
from cryptography.hazmat.backends import default_backend
import os, base64
from utils.key_utils import get_hashed_key

def encrypt(text, password):
    key = get_hashed_key(password, 32)
    nonce = os.urandom(16)
    cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None, backend=default_backend())
    ct = cipher.encryptor().update(text.encode())
    return base64.b64encode(nonce + ct).decode()

def decrypt(enc_text, password):
    key = get_hashed_key(password, 32)
    raw = base64.b64decode(enc_text)
    cipher = Cipher(algorithms.ChaCha20(key, raw[:16]), mode=None, backend=default_backend())
    return cipher.decryptor().update(raw[16:]).decode()

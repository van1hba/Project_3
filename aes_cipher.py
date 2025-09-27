from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
from utils.key_utils import get_hashed_key

def pad(text): return text + chr(16 - len(text) % 16) * (16 - len(text) % 16)
def unpad(text): return text[:-ord(text[-1])]

def encrypt(text, password):
    key = get_hashed_key(password, 32)
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ct = cipher.encrypt(pad(text).encode())
    return base64.b64encode(iv + ct).decode()

def decrypt(enc_text, password):
    key = get_hashed_key(password, 32)
    raw = base64.b64decode(enc_text)
    cipher = AES.new(key, AES.MODE_CBC, raw[:16])
    return unpad(cipher.decrypt(raw[16:]).decode())

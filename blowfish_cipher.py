from Crypto.Cipher import Blowfish
from Crypto.Random import get_random_bytes
import base64
from utils.key_utils import get_hashed_key

def pad(text): return text + chr(8 - len(text) % 8) * (8 - len(text) % 8)
def unpad(text): return text[:-ord(text[-1])]

def encrypt(text, password):
    key = get_hashed_key(password, 16)
    iv = get_random_bytes(8)
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(pad(text).encode())).decode()

def decrypt(enc_text, password):
    key = get_hashed_key(password, 16)
    raw = base64.b64decode(enc_text)
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, raw[:8])
    return unpad(cipher.decrypt(raw[8:]).decode())

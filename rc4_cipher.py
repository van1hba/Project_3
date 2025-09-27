from Crypto.Cipher import ARC4
import base64
from utils.key_utils import get_hashed_key

def encrypt(text, password):
    key = get_hashed_key(password, 16)
    return base64.b64encode(ARC4.new(key).encrypt(text.encode())).decode()

def decrypt(enc_text, password):
    key = get_hashed_key(password, 16)
    return ARC4.new(key).decrypt(base64.b64decode(enc_text)).decode()

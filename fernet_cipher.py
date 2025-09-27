from cryptography.fernet import Fernet
import base64
from utils.key_utils import get_hashed_key

def get_fernet_key(password):
    return base64.urlsafe_b64encode(get_hashed_key(password))

def encrypt(text, password):
    return Fernet(get_fernet_key(password)).encrypt(text.encode()).decode()

def decrypt(enc_text, password):
    return Fernet(get_fernet_key(password)).decrypt(enc_text.encode()).decode()

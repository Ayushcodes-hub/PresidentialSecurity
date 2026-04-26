from cryptography.fernet import Fernet
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KEY_PATH = os.path.join(BASE_DIR, "vault", "master.key")

def generate_key():
    """Creates a unique encryption key."""
    if not os.path.exists(KEY_PATH):
        key = Fernet.generate_key()
        with open(KEY_PATH, "wb") as key_file:
            key_file.write(key)
        print("[VAULT] New Master Key Generated.")

def encrypt_data(data):
    """Turns data into a 'Ghost' (Unreadable)."""
    with open(KEY_PATH, "rb") as key_file:
        key = key_file.read()
    f = Fernet(key)
    return f.encrypt(data.encode())

if __name__ == "__main__":
    if not os.path.exists(os.path.join(BASE_DIR, "vault")):
        os.makedirs(os.path.join(BASE_DIR, "vault"))
    generate_key()
    secret = "Presidential Secret Data"
    ghost = encrypt_data(secret)
    print(f"[VAULT] Encrypted Data: {ghost[:20]}...")
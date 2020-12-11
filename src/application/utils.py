from passlib.hash import pbkdf2_sha256
from cryptography.fernet import Fernet

def hash_password(password):
    return pbkdf2_sha256.hash(password)


# def check_password(password, hashed):
#     return pbkdf2_sha256.verify(password, hashed)

def check_password(client_id_request, client_id_stored):
    
    client_id_stored = decrypt_message(client_id_stored)

    if client_id_stored.decode('utf-8') == client_id_request:
        return True
    else: 
        return False

def __load_key():
    """
    Load the previously generated key
    """
    return open("secret.key", "rb").read()

def encrypt_message(message):
    """
    Encrypts a message
    """
    key = __load_key()
    
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    return encrypted_message

def decrypt_message(message_encrypted):
    key = __load_key()
    f = Fernet(key)
    message = f.decrypt(message_encrypted)
    
    return message


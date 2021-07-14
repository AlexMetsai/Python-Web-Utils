# Alexandros I. Metsai
# alexmetsai@gmail.com
# Various utilities for ciphering messages.

import rsa

from cryptography.fernet import Fernet
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def fernet_encryptor(message, key):
    """
    Fernet symmetric key cipher.

    :param message: The message to be encrypted
    :param key: Encryption key
    :return: Encrypted message
    """
    fernet = Fernet(key)
    enc_message = fernet.encrypt(message.encode())
    return enc_message


def fernet_decryptor(message, key):
    """
    Fernet symmetric key cipher.

    :param message: the message to be decrypted
    :param key: encryption key
    :return: decrypted message
    """
    fernet = Fernet(key)
    dec_message = fernet.decrypt(message).decode()
    return dec_message


def aes_encryptor(message, key):
    """
    AES symmetric key cipher.

    :param message: the message to be encrypted
    :param key: encryption key
    :return: encrypted message
    """
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    enc_message, tag = cipher.encrypt_and_digest(message.encode())
    return nonce, enc_message, tag


def aes_decryptor(message, key, nonce, tag):
    """
    AES symmetric key cipher.

    :param message: the message to be decrypted
    :param key: encryption key
    :param nonce: number used only once
    :param tag: authentication tag
    :return: decrypted message
    """
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    dec_message = cipher.decrypt(message).decode()
    try:
        cipher.verify(tag)
        print("The message is authentic.")
    except ValueError:
        print("Incorrect key or corrupt message.")
    return dec_message


def rsa_encryptor(message, public_key):
    """
    RSA asymmetric key cipher.

    :param message: the message to be encrypted
    :param public_key: public encryption key
    :return: encrypted message
    """
    enc_message = rsa.encrypt(message.encode(), public_key)
    return enc_message



if __name__ == '__main__':
    # add some functionality demonstration
    pass

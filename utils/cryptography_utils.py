"""
Various utilities for ciphering messages.

Copyright (C) 2021 Alexandros I. Metsai
alexmetsai@gmail.com

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 3
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

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


def rsa_decryptor(message, private_key):
    """
    RSA asymmetric key cipher.

    :param message: the message to be decrypted
    :param private_key: private decryption key

    :return: decrypted message
    """
    dec_message = rsa.decrypt(message, private_key).decode()
    return dec_message


if __name__ == '__main__':
    # Example usage of the algorithms.

    text = "This is a sample text."
    test_type = 'AES'
    test_all = True

    if test_type == 'rsa' or test_all:
        print("RSA asymmetric encryption:\n\n")
        encryptor = rsa_encryptor
        decryptor = rsa_decryptor

        pub_key, priv_key = rsa.newkeys(512)
        encmessage = encryptor(text, pub_key)
        decmessage = decryptor(encmessage, priv_key)

        print("Functionality Demonstration")
        print("Original text: {}".format(text))
        print("Encrypted text: {}".format(encmessage))
        print("Decrypted text: {}\n".format(decmessage))

    if test_type == 'fernet' or test_all:
        print("Fernet symmetric encryption:\n\n")
        encryptor = fernet_encryptor
        decryptor = fernet_decryptor

        cipher_key = Fernet.generate_key()
        encmessage = encryptor(text, cipher_key)
        decmessage = decryptor(encmessage, cipher_key)

        print("Functionality Demonstration")
        print("Original text: {}".format(text))
        print("Encrypted text: {}".format(encmessage))
        print("Decrypted text: {}\n".format(decmessage))

    if test_type == 'AES' or test_all:
        print("AES symmetric encryption:\n\n")
        encryptor = aes_encryptor
        decryptor = aes_decryptor

        cipher_key = get_random_bytes(16)
        encnonce, encmessage, enc_tag = encryptor(text, cipher_key)
        decmessage = decryptor(encmessage, cipher_key, encnonce, enc_tag)

        print("Functionality Demonstration")
        print("Original text: {}".format(text))
        print("Encrypted text: {}".format(encmessage))
        print("Decrypted text: {}\n".format(decmessage))

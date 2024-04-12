from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os


def encrypt_3des(key: bytes, plaintext: bytes) -> bytes:
    """
     Encrypts plaintext using Triple DES algorithm.
     Parameters:
         key (bytes): The key to use for encryption.
         plaintext (bytes): The plaintext to encrypt.
     Returns:
         bytes: The ciphertext produced by encrypting the plaintext.
     """
    padder = padding.PKCS7(algorithms.TripleDES.block_size).padder()
    padded_plaintext = padder.update(plaintext) + padder.finalize()
    cipher = Cipher(algorithms.TripleDES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
    return ciphertext


def decrypt_3des(key: bytes, ciphertext: bytes) -> bytes:
    """
    Decrypts ciphertext using Triple DES algorithm.
    Parameters:
        key (bytes): The key to use for decryption.
        ciphertext (bytes): The ciphertext to decrypt.
    Returns:
        bytes: The plaintext produced by decrypting the ciphertext.
    """
    cipher = Cipher(algorithms.TripleDES(key), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    unpadder = padding.PKCS7(algorithms.TripleDES.block_size).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
    return plaintext


def generate_3des_key(length: int) -> bytes:
    """
    Generates a Triple DES key of specified length.
    Parameters:
        length (int): The length of the key in bits (64, 128, or 192).
    Returns:
        bytes: The generated Triple DES key.
    Raises:
        ValueError: If an invalid key length is provided.
    """
    if length not in [64, 128, 192]:
        raise ValueError("Invalid length of the lock. Select 64, 128, or 192 bits.")
    return os.urandom(length // 8)
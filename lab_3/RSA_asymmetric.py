from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
import logging

logger = logging.getLogger()
logger.setLevel('INFO')


def generate_rsa_key() -> tuple:
    """
     Generates RSA private and public key pair.
     Returns:
         tuple: A tuple containing the private key and the corresponding public key.
     """
    keys = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    private_key = keys
    public_key = keys.public_key()
    logging.info('Asymmetric encryption keys have been generated.')
    return private_key, public_key


def encrypt_rsa(public_key, text: bytes) -> bytes:
    """
    Encrypts text using RSA public key.
    Parameters:
        public_key: The RSA public key used for encryption.
        text (bytes): The text to be encrypted.
    Returns:
        bytes: The encrypted text.
    """
    encrypt_text = public_key.encrypt(text, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                   algorithm=hashes.SHA256(), label=None))
    logging.info('The text is encrypted with an asymmetric encryption algorithm.')
    return encrypt_text


def decrypt_rsa(private_key: object, text: bytes) -> bytes:
    """
    Decrypts text using RSA private key.
    Parameters:
        private_key (object): The RSA private key used for decryption.
        text (bytes): The text to be decrypted.
    Returns:
        bytes: The decrypted text.
    """
    decrypt_text = private_key.decrypt(text, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                     algorithm=hashes.SHA256(), label=None))
    logging.info('The text encrypted with the asymmetric encryption algorithm has been decrypted.')
    return decrypt_text
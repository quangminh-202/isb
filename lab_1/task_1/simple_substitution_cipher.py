import random
import json


ALPHABET = "АБВГДЕЖЗИЙКЛМОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


def generate_key():
    """
    Create an encryption key by randomly sorting the characters of the Russian alphabet.

    Returns:
        dict: a dictionary representing the encryption key, where the source characters are the keys and the encrypted characters are the values.
    """
    alphabet = list(ALPHABET)
    shuffled_alphabet = alphabet[:]
    random.shuffle(shuffled_alphabet)
    return dict(zip(alphabet, shuffled_alphabet))


def transform_text(text, key, mode):
    """
    Encrypt or decrypt a piece of text based on the mode provided.

    Args:
    text (str): The text to be transformed.
    key (dict): Encryption key, a dictionary that maps the original characters into encrypted characters.
    mode (str): The mode of transformation, either 'encrypt' or 'decrypt'.

    Returns:
    str: The transformed text.
    """
    transformed_text = ''
    for char in text:
        if mode == 'encrypt':
            transformed_text += key.get(char, char)
        elif mode == 'decrypt':
            reverse_key = {v: k for k, v in key.items()}
            transformed_text += reverse_key.get(char, char)
    return transformed_text


def generate_key_and_encrypt_and_decrypt():
    """
    Generate encryption key, encrypt and decrypt a piece of text, and save the results.

    This function performs the following steps:
    1. Generates an encryption key.
    2. Reads the original text from 'original_text.txt'.
    3. Encrypts the original text using the generated key.
    4. Decrypts the encrypted text using the same key.
    5. Saves the encrypted text to 'encrypted_text.txt'.
    6. Saves the decrypted text to 'decrypted_text.txt'.
    7. Saves the encryption key to 'encryption_key.txt'.
    """
    key = generate_key()
    try:
        with open('original_text.txt', 'r', encoding='utf-8') as file:
            original_text = file.read()

        encrypted_text = transform_text(original_text, key,"encrypt")
        decrypted_text = transform_text(encrypted_text, key, "decrypt")

        with open('encrypted_text.txt', 'w', encoding='utf-8') as file:
            file.write(encrypted_text)

        with open('decrypted_text.txt', 'w', encoding='utf-8') as file:
            file.write(decrypted_text)

        with open('encryption_key.json', 'w', encoding='utf-8') as file:
            json.dump(key, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print("An error occurred:", str(e))


if __name__ == "__main__":
    generate_key_and_encrypt_and_decrypt()
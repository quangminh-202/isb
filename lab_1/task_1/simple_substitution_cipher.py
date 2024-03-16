import random

# Функция для генерации ключа шифрования на русском языке
def generate_key():
    alphabet = list('АБВГДЕЖЗИЙКЛМОПРСТУФХЦЧШЩЪЫЬЭЮЯ ')
    shuffled_alphabet = alphabet[:]
    random.shuffle(shuffled_alphabet)
    return dict(zip(alphabet, shuffled_alphabet))

# Функция для шифрования текста
def encrypt(text, key):
    encrypted_text = ''
    for char in text:
        encrypted_text += key.get(char, char)
    return encrypted_text

# Генерация ключа шифрования на русском языке
key = generate_key()
try:
    with open('original_text.txt', 'r', encoding='utf-8') as file:
        original_text = file.read()

    # Шифрование текста
    encrypted_text = encrypt(original_text, key)

    # Сохранение зашифрованного текста
    with open('encrypted_text.txt', 'w', encoding='utf-8') as file:
        file.write(encrypted_text)

    # Сохранение ключа шифрования
    with open('encryption_key.txt', 'w', encoding='utf-8') as file:
        for k, v in key.items():
            file.write(f"{k}:{v}\n")
except Exception as e:
    print("An error occurred:", str(e))
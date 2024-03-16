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

# Текст для шифрования на русском языке
original_text = """С 19 ПО 21 ФЕВРАЛЯ УЧАСТВУЙТЕ В БЕСПЛАТНОМ ИНТЕНСИВЕ «ПРОФЕССИЯ ПЕНТЕСТЕР: КАК СТАТЬ ХАКЕРОМ И НЕ ПОПАСТЬ В РОЗЫСК ИНТЕРПОЛА» ОТ SKILLFACTORY. ВАС ЖДЕТ РЕАЛЬНО БОЛЬШАЯ ПРАКТИКА: СКАНИРОВАНИЕ, РАЗВЕДКА И ВЗЛОМ LINUX-СИСТЕМЫ ПОД РУКОВОДСТВОМ ИНЖЕНЕРА ПО ИНФОРМАЦИОННОЙ БЕЗОПАСНОСТИ - ГАМИДА ДЖАФАРОВА. МЫ ПОДРОБНО РАЗБЕРЕМ, КТО ТАКОЙ ПЕНТЕСТЕР И ЧЕМ ОН ЗАНИМАЕТСЯ. ВЫ УЗНАЕТЕ О ПРОГРЕССИВНЫХ СПОСОБАХ ВЗЛОМА И СРАЗУ ЖЕ ПЕРЕЙДЕТЕ К ПРАКТИКЕ — РЕШИТЕ СВОЮ ПЕРВУЮ ЗАДАЧУ В КАЧЕСТВЕ ПЕНТЕСТЕРА.ВАМ НЕ НУЖНЫ СПЕЦИАЛЬНЫЕ ЗНАНИЯ.СПЕЦИАЛИСТ ПО ПЕНТЕСТУ — ОТЛИЧНЫЙ ВЫБОР ДЛЯ СТАРТА В IT. ПОПРОБУЕТЕ СЕБЯ В РОЛИ БЕЛОГО ХАКЕРА И ПОЙМЕТЕ, ИНТЕРЕСНА ЛИ ВАМ ЭТА СПЕЦИАЛЬНОСТЬ. ЗА 3 ДНЯ ВЫ: НАСТРОИТЕ СВОЮ ВИРТУАЛЬНУЮ ЛАБОРАТОРИЮ ВЗЛОМАЕТЕ ИНФРАСТРУКТУРУ КОМПАНИИ ПОЛУЧИТЕ ДОСТУП К СЕРВЕРАМ.
"""

# Генерация ключа шифрования на русском языке
key = generate_key()

# Шифрование текста
encrypted_text = encrypt(original_text, key)

# Сохранение исходного текста
with open('original_text.txt', 'w', encoding='utf-8') as file:
    file.write(original_text)

# Сохранение зашифрованного текста
with open('encrypted_text.txt', 'w', encoding='utf-8') as file:
    file.write(encrypted_text)

# Сохранение ключа шифрования
with open('encryption_key.txt', 'w', encoding='utf-8') as file:
    for k, v in key.items():
        file.write(f"{k}:{v}\n")

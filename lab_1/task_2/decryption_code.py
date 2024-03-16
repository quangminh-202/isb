import json
def frequency_analysis(file_path):
    frequencies = {}
    total_chars = 0
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            for char in line:
                if char != "\n":
                    total_chars += 1
                    if char in frequencies:
                        frequencies[char] += 1
                    else:
                        frequencies[char] = 1
    relative_frequencies = {char: freq / total_chars for char, freq in frequencies.items()}
    sorted_frequencies = sorted(relative_frequencies.items(), key=lambda x: x[1], reverse=True)
    return sorted_frequencies

def write_to_file(path: str, data: list) -> None:
    with open(path, "w") as file:
        for item in data:
            file.write(f"{item[0]}: {item[1]}\n")

def read_frequency_file(file_path: str) -> dict:
    frequency_dict = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if ': ' in line:
                char, freq = line.strip().split(': ')
                frequency_dict[char] = float(freq)
    return frequency_dict

def key_decryption(frequency_text_path: str, standard_frequency_path: str, output_file: str) -> None:
    frequency_text = read_frequency_file(frequency_text_path)
    standard_frequency = read_frequency_file(standard_frequency_path)
    key = {}
    for char, freq_text in frequency_text.items():
        closest_char = min(standard_frequency, key=lambda x: abs(float(freq_text) - float(standard_frequency[x])))
        key[char] = closest_char

    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(key, json_file, ensure_ascii=False, indent=4)

def decryption(input_file_path: str, output_file_path: str, key_path: str) -> None:
    with open(key_path, "r", encoding="utf-8") as json_file:
        decryption_key = json.load(json_file)
    with open(input_file_path, 'r', encoding='utf-8') as input_file, \
            open(output_file_path, 'w', encoding='utf-8') as output_file:
        for line in input_file:
            decrypted_line = ''.join(decryption_key.get(char, char) for char in line.strip())
            output_file.write(decrypted_line + '\n')

if __name__ == "__main__":
    #data = frequency_analysis(r"C:\Users\DELL\PycharmProjects\isb\lab_1\task_2\cod2.txt")
    #write_to_file(r"C:\Users\DELL\PycharmProjects\isb\lab_1\task_2\frequency_text.txt", data)
    #key_decryption("frequency_text.txt", "standard_frequency.txt", "decryption_key.txt")
    decryption("cod2.txt", "decrypted_text.txt", "decryption_key.json")

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


def coder(text):
    str_code = ""
    prev_char = ""
    count = 1
    for char in text:
        if char != prev_char:
            if prev_char:
                str_code += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    return str_code


def decoder(text):
    count = ""
    str_decode = ""
    for char in text:
        if char.isdigit():
            count += char
        else:
            str_decode += char * int(count)
            count = ""
    return str_decode


text = input("Введите текст для кодировки: ")
print(f"Текст после кодировки: {coder(text)}")
print(f"Текст после дешифровки: {decoder(coder(text))}")

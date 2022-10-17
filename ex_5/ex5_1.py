# # Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


def read_text(path):
    with open(path, "r", encoding="UTF-8") as file:
        return file.read()


def del_words(text):
    final_text = list(filter(lambda x: "абв" not in x, text.split(" ")))
    return " ".join(final_text)


def write_text(path, text):
    with open(path, "w", encoding="UTF-8") as file:
        file.write(text)


text = read_text("./text_read_5_1.txt")
text_new = del_words(text)
write_text("./parsing_text_5_1.txt", text_new)

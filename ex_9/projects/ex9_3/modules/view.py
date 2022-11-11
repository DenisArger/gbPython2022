import csv
from telebot import TeleBot


def view_note(msg):
    bot = TeleBot("5621503597:AAF6jm0tSgygi_eSwTa3cRKsmrlq7jJYQpU")
    counter = int(1)
    with open("database.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            bot.send_message(
                chat_id=msg.from_user.id,
                text=str(counter)
                + ". "
                + str(row["Фамилия"])
                + " "
                + str(row["Имя"])
                + " "
                + str(row["Телефон"])
                + " "
                + str(row["Описание"]),
            )
            counter += 1

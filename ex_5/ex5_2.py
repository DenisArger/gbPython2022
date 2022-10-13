# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета.
#  Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""


import random


def change_player(player):  # Метод для смены игрока
    if player == "player1":
        player = "player2"
    else:
        player = "player1"
    return player


def move(player, current_candies):  # Метод хода игрока
    print(f"Ход игрока {names[player]}")
    print(f"Сейчас на столе {current_candies} конфет")
    if bot_game and player == "player2":
        current_move = bot_move(current_candies)
        print(f"{names[player]} взял {current_move} конфет")
        return current_candies - current_move
    else:
        current_move = input("Сколько конфет вы берёте? (от 1 до 28): ")

    if current_move.isdigit():
        current_move = int(current_move)
    else:
        print("Нужно ввести число цифрами")
        return move(player, current_candies)

    if 0 < current_move <= max_move and current_move <= current_candies:
        print(f"{names[player]} взял {current_move} конфет")
        return current_candies - current_move
    else:
        print("Невозможно взять столько конфет")
        return move(player, current_candies)


def bot_move(current_candies):  # Бот
    if current_candies <= max_move:
        return current_candies
    remains = current_candies % (max_move + 1)
    if remains == 0:
        return int(random.randint(1, 28))
    else:
        return remains


candies = int(100)  # Стартовое количество конфет
max_move = int(28)  # Максимальный ход
bot_game = input("Для выбора игры с ботом введите 'bot', иначе, нажмите Enter: ")
if bot_game == "bot":
    bot_game = True
else:
    bot_game = False

current_player = "player1"

if bot_game:
    names = {"player1": input("Введите Ваше имя: "), "player2": "Железный друг"}
else:
    names = {
        "player1": input("Первый игрок, как Вас зовут?: "),
        "player2": input("Второй игрок, как Вас зовут?"),
    }


while True:
    candies = move(current_player, candies)
    if candies == 0:
        print(f"Победил {names[current_player]}")
        break
    else:
        current_player = change_player(current_player)
        print("")

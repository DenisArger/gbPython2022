# 3. Создайте программу для игры в ""Крестики-нолики"".
import math


def change_steps(step):
    if step == "X":
        step = "O"
    else:
        step = "X"
    return step


def change_player(player):  # Метод для смены игрока
    if player == "1":
        player = "2"
    else:
        player = "1"
    return player


def print_field(array):
    print("------------")
    for i in range(0, len(array), 3):
        print(f" {array[i]} | {array[i+1]} | {array[i+2]} ")
        print("------------")


def move(current_player, step, field):
    point = input(
        f"Игрок {current_player}, Введите номер поля, в который вы хотите поставить символ: "
    )
    if point.isdigit():
        if 0 < int(point) < 10:
            point = int(point) - 1
            if field[point] != "X" and field[point] != "O":
                return point
            else:
                print("Указанное поле занаято.")
                return move(current_player, step, field)
        else:
            print("Такого поля не существует")
            move(current_player, step, field)
    else:
        print("Введите поле цифрой от 1 до 9")
        move(current_player, step, field)


def check_victory(field, point):
    check_point = math.floor(point / 3)
    if field[check_point] == field[check_point + 1] == field[check_point + 2]:
        return True
    elif field[point] == field[point - 3] == field[point - 6]:
        return True
    elif point in (0, 2, 4, 6, 8):
        if field[0] == field[4] == field[8] or field[2] == field[4] == field[6]:
            return True
    else:
        return False


field = []
for i in range(0, 9):
    field.append(i + 1)

current_player = "1"
step = "X"

print_field(field)
win = False
for i in range(9):
    point = move(current_player, step, field)
    field[int(point)] = step
    print_field(field)
    if check_victory(field, point) == True:
        win = True
        break
    step = change_steps(step)
    current_player = change_player(current_player)


if win:
    print()
    print(f"Победил игрок {current_player}")
else:
    print()
    print("Ничья!")

# Напишите программу, которая принимает на вход координаты точки (X и Y),
#  причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится
# эта точка.

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3


def show_plane_number():
    print("Введите X не равное 0")
    x = (int)(input())
    print("Введите Y не равное 0")
    y = (int)(input())

    if x == 0 or x == 0:
        print("X или Y равно 0: точка лежит на оси")
        return

    if x > 0 and y > 0:
        plane = 1
    elif x < 0 and y > 0:
        plane = 2
    elif x < 0 and y < 0:
        plane = 3
    else:
        plane = 4
    print(plane)


show_plane_number()

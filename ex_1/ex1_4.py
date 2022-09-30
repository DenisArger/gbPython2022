# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).


def show_plane_data():
    print("Введите номер четверти от 1 до 4")
    number_plane = (int)(input())

    if number_plane == 1:
        data_plane = "x > 0 и y > 0"
    elif number_plane == 2:
        data_plane = "x < 0 и y > 0"
    elif number_plane == 3:
        data_plane = "x < 0 и y < 0"
    elif number_plane == 4:
        data_plane = "x > 0 и y < 0"
    else:
        print("Номер плоскости неопределен")
        return

    print(f"Значение X и Y лежат в следующем диапазоне: {data_plane}")


show_plane_data()

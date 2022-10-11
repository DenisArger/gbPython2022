# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между
#  максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


import sys


def create_list():
    print("Введите размер списка")
    size_list = int(input())
    list = []
    for i in range(0, size_list):
        print("Введите элемент списка")
        item_list = float(input())
        list.append(item_list)
    return list


def dif(list):
    min = sys.float_info.max
    max = sys.float_info.min
    for i in range(0, len(list)):
        part = list[i] - int(list[i])
        if part == 0:
            continue
        if part < min:
            min = part
        if part > max:
            max = part
    return format(max - min, ".2f")


list = create_list()
print(list)
print(dif(list))

# Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


def create_list():
    print("Введите размер списка")
    size_list = int(input())
    list = []
    for i in range(1, size_list + 1):
        print("Введите элемент списка")
        item_list = int(input())
        list.append(item_list)
    return list


def mult(list):
    list_new = []
    len_list = len(list)

    size = 0
    if len_list % 2 == 0:
        size = len_list // 2
    else:
        size = len_list // 2 + 1

    for i in range(0, size):
        list_new.append(list[i] * list[len_list - i - 1])
    return list_new


list = create_list()
print(list)
print(mult(list))

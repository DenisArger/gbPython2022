# Задайте список из нескольких чисел. Напишите программу,
#  которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


def create_list():
    print("Введите размер списка")
    size_list = int(input())
    list = []
    for i in range(1, size_list + 1):
        print("Введите элемент списка")
        item_list = int(input())
        list.append(item_list)
    return list


# Было
# def sum_not_paritiry(list):
#     sum = 0
#     for i in range(1, len(list)):
#         if i % 2 != 0:
#             sum += list[i]
#     return sum

# Стало
def sum_not_paritiry_new(list_new):
    return sum(x for i, x in enumerate(list_new) if i % 2 != 0)


list_ = create_list()
print(list_)
print(
    f"Сумма элементов списка, \
стоящих на нечётной позиции: {sum_not_paritiry_new(list_)}"
)

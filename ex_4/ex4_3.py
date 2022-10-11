# 3 Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности.
#
# *Пример*
#
# - при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]


def create_list():
    print("Введите размер списка")
    size_list = int(input())
    list = []
    for i in range(0, size_list):
        print("Введите элемент списка")
        item_list = int(input())
        list.append(item_list)
    return list


def is_not_reaper(array):
    answer = []
    checked_numbers = []
    for i in range(len(array)):
        if array[i] not in checked_numbers:
            checked_numbers.append(array[i])
            counter = True
            for j in range(i + 1, len(array)):
                if array[j] == array[i]:
                    counter = False
                    break
            if counter:
                answer.append(array[i])

    return answer


list = create_list()
list_not_repeat = is_not_reaper(list)
print(list_not_repeat)

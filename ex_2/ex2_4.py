# Задание 4 Задайте список из N элементов,
#  заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на позициях a и b.
# Значения N, a и b вводит пользователь с клавиатуры.


def input_n():
    print("Введите число N")
    n = int(input())
    return n


def input_a():
    print("Введите число A")
    a = int(input())
    return a


def input_b():
    print("Введите число B")
    b = int(input())
    return b


n = input_n()
a = input_a()
b = input_b()

list = []
for i in range(-n, n + 1):
    list.append(i)

print(f"Содержимое списка:{list}")
print(f"Элемент списка {a}:{list[a]}")
print(f"Элемент списка {b}:{list[b]}")
print(f"Произведение элементов {a} и {b}:{list[a] * list[b]}")

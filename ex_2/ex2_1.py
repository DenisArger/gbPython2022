# Задание 1 Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.

# Пример:

# 6782 -> 23
# 0,56 -> 11


from unittest import result

# Было
# def sum_number():
#     print("Введите число")
#     number = float(input())

#     sum = 0
#     for i in str(number):
#         if i != ".":
#             sum += int(i)
#     print(f"Сумма цифр равна: {(sum)}")

# Стало
def sum_of_digits_new():
    print("Введите число")
    number = input()
    result = sum([int(number[i]) for i in range(len(number)) if number[i].isdigit()])
    print(f"Сумма цифр равна: {(result)}")


sum_of_digits_new()

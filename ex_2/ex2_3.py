# Задание 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
# округлённую до трёх знаков после точки.

# Пример:

# Для n = 6 -> 14.072


def input_number():
    print("Введите число")
    number = int(input())
    return number


def func(number):
    return (1 + 1 / number) ** number


number = input_number()


list = []
sum = 0
for i in range(1, number + 1):
    sum += func(i)

print(f"Сумма чисел из последовательности :  {format(sum,'.3f')}")

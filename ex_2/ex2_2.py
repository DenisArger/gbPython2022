# Задание 2 Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.

# Пример:

# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def input_number():
    print("Введите число")
    number = int(input())
    return number


def mult(number):
    if number == 1:
        return 1
    else:
        return number * mult(number - 1)


number = input_number()


list = []
for i in range(1, number + 1):
    list.append(mult(i))

print(f"Набор произведений чисел от 1 до {number}:  {list}")

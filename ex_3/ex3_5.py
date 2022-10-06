# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так:
#  [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def fibbonachi_and_nega(k):

    fibbonachi = [0, 1]
    for i in range(2, k + 1):
        fibbonachi.append(fibbonachi[i - 1] + fibbonachi[i - 2])

    negafibbonachi = []
    for i in range(len(fibbonachi) - 1):
        if i % 2 == 0:
            k = -1
        else:
            k = 1
        negafibbonachi.append(fibbonachi[len(fibbonachi) - 1 - i] * k)
    negafibbonachi = negafibbonachi + fibbonachi
    return negafibbonachi


print("Введите число")
number = int(input())
print(fibbonachi_and_nega(number))

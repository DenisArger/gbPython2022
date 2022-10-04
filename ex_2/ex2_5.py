# Задание 5 Реализуйте алгоритм перемешивания списка.
import random

list = ["a", "b", "c", "d", "e"]

print(list)

for i in range(0, len(list)):
    j = random.randint(0, len(list) - 1)
    temp = list[i]
    list[i] = list[j]
    list[j] = temp

print(list)

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


def decimal_to_bin(number, answer=""):
    current_bit = str(number % 2)
    number = number // 2

    if number > 0:
        answer += decimal_to_bin(number, answer)
    answer += str(current_bit)
    return answer


print("Введите число")
number = int(input())
print(decimal_to_bin(number))

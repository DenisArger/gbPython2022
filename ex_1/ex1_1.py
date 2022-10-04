# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет


def is_check_day():
    print("Введите день недели")
    numberDay = (int)(input())
    if numberDay > 7 or numberDay < 1:
        print("Неправильно введен день недели")
    elif numberDay < 6:
        print("Нет")
    else:
        print("Да")


is_check_day()

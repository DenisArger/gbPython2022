# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


def is_check_predicate():
    print("Введите X")
    x = input()
    print("Введите Y")
    y = input()
    print("Введите Z")
    z = input()

    val_1 = not (x or y or z)
    val_2 = not x and not y and not z
    if val_1 == val_2:
        print("Утверждение истинно")
    else:
        print("Утвержение ложно")


is_check_predicate()

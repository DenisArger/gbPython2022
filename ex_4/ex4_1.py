# 1 Вычислить число π c заданной точностью d

# *Пример:*

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


def func_leibniz(number, mult):
    return mult * 4 / number


d = float(input("Введите число d: "))
mult = 1
div = 1
curr_leibniz = 1
answer = 0
n = 0
while abs(curr_leibniz) > d / 10:
    n += 1
    curr_leibniz = func_leibniz(div, mult)
    answer += curr_leibniz
    div += 2
    mult *= -1
print(answer)

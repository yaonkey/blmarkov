#!/usr/bin/env python
import random
from config import *


# Требуется разработать генератор двоичных цепей маркова

def toFixed(numObj: float, digits=2) -> str:
    """
    Позволяет определить точно количество чисел после запятой
    :param numObj: Исходное число
    :param digits: Количество чисел после запятой исходного числа
    :return: Число с определенным количеством чисел после запятой
    """
    return f"{numObj:.{digits}f}"


def itoa(value: int) -> float:
    """
    Метод серединных квадратов
    :param value: число, которое нужно разбить
    :return: новое сгенерированное число, умноженное на квадрат
    """
    _temp = list((str(value)))
    _val_len = 0
    isD = len(_temp) % 2
    if isD == 0:
        _val_len = list([len(_temp) / 2 - 1, len(_temp) / 2 + 1])
        __result = _temp[int(_val_len[0])], _temp[int(_val_len[1] - 1)]
        return pow(int(f'{__result[0]}{__result[1]}'), 2)
    else:
        _val_len = len(_temp) / 2
        return pow(int(_temp[int(_val_len)]), 2)


# debug
if DEBUG:
    _a = int(input('Введите любое число: '))
    print(itoa(_a))

# n = int(input('Введите n: '))  # 1
# v = int(input('Введите v: '))

# заполнение L[i], где i = (2...v)
for i in range(0, v):
    L.append(int(random.randint(0, 999)))

_nums = []

# заполнение последующих состояний
for i in range(2, v):
    t = pow(2, (i - 2))
    for k in range(0, t - 1):
        d = (n % L[i]) / (L[i] - 1)  # расчет d
        n /= L[i]  # нахождение вероятности
        n = abs(n)  # модуль числа n
        _nums.append(d)

for index, value in enumerate(_nums):
    print(f'{index}: {toFixed(value, 15)}')

#!/usr/bin/env python3
from datetime import datetime
from config import *

def random_generator(initial_number=None):
    """
        Генератор случайной последовательности.
        Реализован на основе метода срединных квадратов.
    """
    # только в случае, когда входное значение отсутствует, сами генерируем первое случайное число
    if initial_number == None:
        initial_number = _get_initial_number()

    if not isinstance(initial_number, int):
        raise ValueError("Входное значение не является числом!")

    while True:
        square_str = str(initial_number ** 2)
        start_index = len(square_str) // 4
        finish_index = start_index + 1 if len(square_str) % 2 else start_index

        initial_number = int(square_str[start_index:-finish_index])
        yield initial_number


def _get_initial_number():
    """
        Возвращает количество миллисекунд в текущей дате для построения случайных чисел
    """
    now = datetime.now()
    return now.microsecond

# если происходит запуск модуля, то выведем первые 5 случайных чисел
if __name__ == "__main__":
    end_result = 0
    generator = random_generator(N)
    for index, number in (zip(range(V), generator)):
        print("{0}: {1}".format(index+1, number))
        if index == V-1:
            end_result = number
    print(end_result)


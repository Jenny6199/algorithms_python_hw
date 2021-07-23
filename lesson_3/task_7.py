"""
Домашнее задание к 3-му уроку 'Алгоритмы и струтуры данных на Python'
Студент Максим Сапунов Jenny6199@yandex.ru 22.07.2021

Задача №7. В одномерном массиве целых чисел определить два наименьших элемента.
    Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""
from random import randrange


def get_min_from_array(array: list, n: int):
    """
    Возвращает заданное количество минимальных элементов из списка
    :param array:list - анализируемый список
    :param n:int - количество минимальных элементов из array которые будут возвращены функцией.
    """
    work_list = sorted(array.copy())
    min_value = work_list[0:n]
    for el in min_value:
        yield el


def run():
    """Запуск работы программы и вывод результатов на дисплей."""
    arr_1 = [randrange(0, 1000) for _ in range(50)]
    result = get_min_from_array(arr_1, 2)
    print(' Представлен массив элементов:')
    for el in range(0, len(arr_1), 10):
        print(arr_1[el:el+10])
    print(f'\033[032mВ данном массиве минимальными значениями являются {next(result)} и {next(result)}\033[0m.')


if __name__ == '__main__':
    run()

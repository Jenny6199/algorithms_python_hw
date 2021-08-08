"""
Домашнее задание к уроку №7. Алгоритмы и структуры данных на Python.\
Студент: Максим Сапунов Jenny6199@yandex.ru 06.08.2021

Задача №1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке (-100; 100). Выведите на экран исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""
import random       # для заполнения тестового массива.
import cProfile     # для профилирования кода.
import sys      # для вывода информации о системе


def bubble_sort_upgrade(sorted_arr: list, reverse=False):
    """
    Сортировка списка методом 'пузырька'. Сложность O(n**2).
    :param sorted_arr: list - сортируемый список
    :param reverse=False
    :return: result: list - отсортированный список
    """
    n = 1
    was_change_flag = True
    while was_change_flag:  # до доработки было k < len(sorted_arr)
        was_change_flag = False
        for i in range(len(sorted_arr) - n):    # -n добавлено чтобы не проходить повторно по отсортированным элементам
            if not reverse:
                if sorted_arr[i] > sorted_arr[i + 1]:
                    sorted_arr[i], sorted_arr[i + 1] = sorted_arr[i + 1], sorted_arr[i]
                    was_change_flag = True
                    # Здесь усовершенствовал алгоритм путем введения флага
                    # Если замен на данной итерации не было - оставшаяся часть массива отсортирована
                    # и можно выйти из цикла.
            else:
                if sorted_arr[i] < sorted_arr[i + 1]:
                    sorted_arr[i], sorted_arr[i + 1] = sorted_arr[i + 1], sorted_arr[i]
                    was_change_flag = True
                    # Здесь усовершенствовал функцию путем добавления возможности обратной сортировки.
        n += 1
    return sorted_arr


def make_matrix_output(arr):
    """Функция обеспечивает аккуратный вывод значений массива в виде матрицы"""
    for el in range(1, len(arr) + 1):
        print('%4d' % arr[el - 1], end='\n' if el % 10 == 0 else '  ')


def run():
    """Агрегация для тестирования работы функций."""
    get_array = [random.randint(-100, 100) for _ in range(100)]
    make_matrix_output(get_array)       # Вывод на дисплей исходного массива
    print('-'*100)
    get_array = bubble_sort_upgrade(get_array)
    make_matrix_output(get_array)       # Вывод на дисплей сортированного массива.


if __name__ == '__main__':
    cProfile.run(statement='run()')
    print(sys.version)

# Пример сортировки 10 тыс. элементов.
#
#          82403 function calls in 20.969 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000   20.969   20.969 <string>:1(<module>)
#     10000    0.178    0.000    0.490    0.000 random.py:200(randrange)
#     10000    0.128    0.000    0.618    0.000 random.py:244(randint)
#     10000    0.222    0.000    0.312    0.000 random.py:250(_randbelow_with_getrandbits)
#         1   19.624   19.624   19.667   19.667 task_1.py:14(bubble_sort)
#         2    0.145    0.073    0.554    0.277 task_1.py:35(make_matrix_output)
#         1    0.000    0.000   20.968   20.968 task_1.py:41(run)
#         1    0.130    0.130    0.748    0.748 task_1.py:43(<listcomp>)
#         1    0.000    0.000   20.969   20.969 {built-in method builtins.exec}
#      9717    0.042    0.000    0.042    0.000 {built-in method builtins.len}
#     20001    0.409    0.000    0.409    0.000 {built-in method builtins.print}
#     10000    0.040    0.000    0.040    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     12677    0.050    0.000    0.050    0.000 {method 'getrandbits' of '_random.Random' objects}
#
#
# 3.8.10 (default, Jun  2 2021, 10:49:15)
# [GCC 9.4.0]
#
# Process finished with exit code 0
#
# ВЫВОДЫ: На больших массивах квадратичные сортировки слишком затратны по времени.
# К настоящему моменту разработано несколько алгоритмов быстрой сортировки, которые необходимо знать и использовать
# в работе. Быстрые сортировки заложены 'под капотом' языка програмирования. Можно использовать их.
# Для закрепления пройденного материала я создал для себя отдельную библиотеку с алгоритмами сортировок
# где оформил каждый алгоритм в виде функции. Создал на GitHub для них отдельный репозиторий.

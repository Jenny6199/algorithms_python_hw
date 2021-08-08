"""
Домашнее задание к уроку №7. Алгоритмы и структуры данных на Python.
Студент: Максим Сапунов Jenny6199@yandex.ru 06.08.2021

Задача №2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0:50]. Выведите на экран исходный и отсортированный массивы.
"""
import random
import cProfile


def merge_sort(arr_for_sort):
    """Функция сортирует массив методом слияния. Сложность алгоритма O(n*log*n)"""
    k = len(arr_for_sort)
    if k == 1 or k == 0:
        return      # Массив из одного элемента уже отсортирован сам в себе :)
    left_part = arr_for_sort[: k // 2]
    right_part = arr_for_sort[k // 2:]
    merge_sort(left_part)
    merge_sort(right_part)
    n, m, k = 0, 0, 0
    sort_arr = [0] * (len(left_part) + len(right_part))
    while n < len(left_part) and m < len(right_part):
        if left_part[n] <= right_part[m]:
            sort_arr[k] = left_part[n]
            n += 1
        else:
            sort_arr[k] = right_part[m]
            m += 1
        k += 1
    while n < len(left_part):
        sort_arr[k] = left_part[n]
        n += 1
        k += 1
    while m < len(right_part):
        sort_arr[k] = right_part[m]
        m += 1
        k += 1
    for i in range(len(arr_for_sort)):
        arr_for_sort[i] = sort_arr[i]


def make_matrix_output(arr):
    """Функция обеспечивает аккуратный вывод значений массива в виде матрицы"""
    for el in range(1, len(arr) + 1):
        print('%4d' % arr[el - 1], end='\n' if el % 10 == 0 else '  ')


def run(n):
    """Агрегация и запуск"""
    arr_1 = [random.randint(0, n) for _ in range(n)]
    make_matrix_output(arr_1)
    print('*' * 60)
    merge_sort(arr_1)
    make_matrix_output(arr_1)


if __name__ == '__main__':
    run(50)     # согласно условию учебной задачи.
    cProfile.run(statement='run(10000)')
    # Для сравнения с пузырьковой сортировкой использованной в предыдыщей задаче.

#          435060 function calls (415062 primitive calls) in 4.328 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    4.328    4.328 <string>:1(<module>)
#     10000    0.125    0.000    0.448    0.000 random.py:200(randrange)
#     10000    0.094    0.000    0.542    0.000 random.py:244(randint)
#     10000    0.217    0.000    0.323    0.000 random.py:250(_randbelow_with_getrandbits)
#   19999/1    1.993    0.000    3.426    3.426 task_2.py:12(merge_sort)
#         2    0.108    0.054    0.297    0.148 task_2.py:43(make_matrix_output)
#         1    0.000    0.000    4.327    4.327 task_2.py:49(run)
#         1    0.062    0.062    0.604    0.604 task_2.py:51(<listcomp>)
#         1    0.000    0.000    4.328    4.328 {built-in method builtins.exec}
#    338549    1.433    0.000    1.433    0.000 {built-in method builtins.len}
#     20001    0.189    0.000    0.189    0.000 {built-in method builtins.print}
#     10000    0.038    0.000    0.038    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     16504    0.068    0.000    0.068    0.000 {method 'getrandbits' of '_random.Random' objects}
#
# ВЫВОДЫ: На примере сортировки списка из 10 тыс. элементов видно что данная сортировка работает в 5 раз быстрее
# 'пузырьковой'. Алгоритм ее реализации не сложен, при детальном разборе. Добавлено в коллекцию алгоритмов.

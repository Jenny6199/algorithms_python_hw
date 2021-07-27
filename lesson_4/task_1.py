"""
Домашнее задание к уроку № 4 Алгоритмы и структуры данных на Python
Студент Максим Сапунов Jenny6199@yandex.ru 26.07.2021

Задача №1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""
import cProfile
import timeit
import random

# Ретроспективно просмотрев свой предыдущий код, и не найдя в нем достойных функций для анализа
# (захотелось переписать если не все, то многое), решил привести примеры эмпирической
# оценки на алгоритмах сортировки (заодно повторить данную тему).


def square_bubble_sort(array: list):
    """Сортировка массива методом 'пузырька'. Сложность алгоритма O(n**2)"""
    for _ in range(len(array)-1):
        for j in range(len(array)-1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
    return array


def quick_sort(array: list):
    """Сортировка массива методом быстрой сортировки Энтони Хоара. Сложность алгоритма 0(n*log(n))"""
    n = len(array)
    if n <= 1:
        return array
    else:
        l, m, r = [], [], []
        b = array[int(n/2)]
        for el in array:
            if el > b:
                r.append(el)
            elif el < b:
                l.append(el)
            else:
                m.append(el)
        return quick_sort(l) + m + quick_sort(r)


# cProfile.run('square_bubble_sort([random.randint(1, 100) for el in range(10000)])')
arr_1 = [random.randint(1, 100) for el in range(10000)]

# Вывод на экран в виде матрицы с использованием форматирования %
# print(arr_1)
# result = quick_sort(arr_1)
# for i in range(len(result)):
#     print('%4d' % result[i], end=('\n' if i % 10 == 0 else '  --  '))


# Подготовил код для использования в timeit.
import_module = 'import random '

test_code_1 = '''
def square_bubble_sort(array: list):
    """Сортировка массива методом 'пузырька'. Сложность алгоритма O(n**2)"""
    for _ in range(len(array)-1):
        for j in range(len(array)-1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
    return array
    

arr_1 = [random.randint(1, 100) for el in range(10000)]
result = square_bubble_sort(arr_1)
'''

test_code_2 = '''
def quick_sort(array: list):
    """Сортировка массива методом быстрой сортировки Энтони Хоара. Сложность алгоритма 0(n*log(n))"""
    n = len(array)
    if n <= 1:
        return array
    else:
        l, m, r = [], [], []
        b = array[int(n/2)]
        for el in array:
            if el > b:
                r.append(el)
            elif el < b:
                l.append(el)
            else:
                m.append(el)
        return quick_sort(l) + m + quick_sort(r)
        
        
arr_1 = [random.randint(1, 100) for el in range(10000)]
result = quick_sort(arr_1)
'''


# Вывод результатов на дисплей.
print('\033[032mРезультаты для квадратичной сортировки списка длиной 10 тыс.значений:\033[0m')
cProfile.run('square_bubble_sort(arr_1)')
print(f' Время выполнения: {timeit.timeit(stmt=test_code_1, setup=import_module, number=1)}')
print('--'*50)
print('\033[032mРезультаты для быстрой сортировки списка длиной 10 тыс.значений:\033[0m')
cProfile.run('quick_sort(arr_1)')
print(f' Время выполнения: {timeit.timeit(stmt=test_code_2, setup=import_module, number=1)}')


# РЕЗУЛЬТАТЫ.
# "C:/Root/3379 Сапунов/Разное/Програмирование/GeekBrains/Python_alg_2/algorithms_python_hw/lesson_4/task_1.py"
# Результаты для квадратичной сортировки списка длиной 10 тыс.значений:
#          10004 function calls in 17.933 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000   17.933   17.933 <string>:1(<module>)
#         1   17.931   17.931   17.933   17.933 task_1.py:18(square_bubble_sort)
#         1    0.000    0.000   17.933   17.933 {built-in method builtins.exec}
#     10000    0.002    0.000    0.002    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#  Время выполнения: 17.903097926999997
# ----------------------------------------------------------------------------------------------------
# Результаты для быстрой сортировки списка длиной 10 тыс.значений:
#          58185 function calls (57985 primitive calls) in 0.015 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.015    0.015 <string>:1(<module>)
#     201/1    0.011    0.000    0.014    0.014 task_1.py:27(quick_sort)
#         1    0.000    0.000    0.015    0.015 {built-in method builtins.exec}
#       201    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     57780    0.004    0.000    0.004    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#  Время выполнения: 0.025807992000004276
#
# Process finished with exit code 0

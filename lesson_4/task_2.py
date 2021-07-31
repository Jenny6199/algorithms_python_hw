"""
Домашнее задание к уроку №4 Алгоритмы и структуры данных на Python
Студент: Максим Сапунов Jenny6199@yandex.ru 27.07.2021

Задача №2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
Результаты анализа сохранить в виде комментариев в файле с кодом.
"""
import cProfile
import timeit


# Алгоритм поиска простых чисел с помощью решета Эратосфена O(n*log(log*n))
def sieve_1(n):
    """
    Решето Эратосфена. Алгоритм нахождения простых чисел до заданного в параметрах.
    :param = n:int - число до которого будет построен список простых чисел
    :return = primes:list - список простых чисел
    """
    is_prime = [True] * (n + 1)
    primes = []
    for digit in range(2, n + 1):
        if is_prime[digit]:
            primes.append(digit)
            for i in range(digit ** 2, n + 1, digit):
                is_prime[i] = False
    return primes


# Вариант поиска простых чисел метедом перебора делителей  O(n**2)
# Для удобства разбил реализацию на две функции.
def is_easy_digit(n: int):
    """
    Функция возвращает True если заданное число является простым, False - если нет.
    :param n: тестируемое число
    :return: result: bool
    """
    flag = True
    for i in range(2, n):
        if n % i == 0:
            flag = False
    result = True if flag else False
    return result


def all_easy_digits_from(n: int):
    """
    Функция возвращает список простых чисел до заданного числа.
    :param n: int число до которого будет произведен поиск простых чисел
    :return: is_prime: list список простых чисел.
    """
    is_prime = list()
    for i in range(2, n):
        if is_easy_digit(i):
            is_prime.append(i)
    return is_prime


print('\033[032m Тестируем работу алгоритма с использванием решета Эратосфена.\033[0m')
cProfile.run('sieve_1(10000)')
print('-'*70)
print('\033[032m Тестируем работу алгоритма с использванием перебора делителей.\033[0m')
cProfile.run('all_easy_digits_from(10000)')


# Оценка времени работы алгоритмов с помощью timeit
test_code_1 = '''
def sieve_1(n):
    """
    Решето Эратосфена. Алгоритм нахождения простых чисел до заданного в параметрах.
    :param = n:int - число до которого будет построен список простых чисел
    :return = primes:list - список простых чисел
    """
    is_prime = [True] * (n + 1)
    primes = []
    for digit in range(2, n + 1):
        if is_prime[digit]:
            primes.append(digit)
            for i in range(digit ** 2, n + 1, digit):
                is_prime[i] = False
    return primes
'''

test_code_2 = '''
def is_easy_digit(n: int):
    """
    Функция возвращает True если заданное число является простым, False - если нет.
    :param n: тестируемое число
    :return: result: bool
    """
    flag = True
    for i in range(2, n):
        if n % i == 0:
            flag = False
    result = True if flag else False
    return result


def all_easy_digits_from(n: int):
    """
    Функция возвращает список простых чисел до заданного числа.
    :param n: int число до которого будет произведен поиск простых чисел
    :return: is_prime: list список простых чисел.
    """
    is_prime = list()
    for i in range(2, n):
        if is_easy_digit(i):
            is_prime.append(i)
    return is_prime

all_easy_digits_from(n)
'''
var_module = 'n = 10000'

print(f' Время выполнения алгоритма №1: {timeit.timeit(stmt=test_code_1, setup=var_module, number=10)}')
print(f' Время выполнения алгоритма №2: {timeit.timeit(stmt=test_code_2, setup=var_module, number=10)}')


# РЕЗУЛЬТАТЫ
#
# /usr/bin/python3.8 /home/jenny6199/Geek_Brains/python_algorithms/algorithms_python_hw/lesson_4/task_2.py
#  Тестируем работу алгоритма с использванием решета Эратосфена.
#          1233 function calls in 0.011 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.010    0.010 <string>:1(<module>)
#         1    0.008    0.008    0.010    0.010 task_2.py:15(sieve_1)
#         1    0.000    0.000    0.011    0.011 {built-in method builtins.exec}
#      1229    0.003    0.000    0.003    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# ----------------------------------------------------------------------
#  Тестируем работу алгоритма с использванием перебора делителей.
#          11231 function calls in 6.561 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    6.561    6.561 <string>:1(<module>)
#      9998    6.508    0.001    6.508    0.001 task_2.py:33(is_easy_digit)
#         1    0.050    0.050    6.561    6.561 task_2.py:47(all_easy_digits_from)
#         1    0.000    0.000    6.561    6.561 {built-in method builtins.exec}
#      1229    0.003    0.000    0.003    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#
# Process finished with exit code 0

#  Время выполнения алгоритма №1: 9.638999472372234e-06
#  Время выполнения алгоритма №2: 86.7871999630006
#
# Process finished with exit code 0

# ВЫВОДЫ:
# На данных примерах видна важность ассимптотической оценки алгоритма и профилирование времени его работы.
# Необходимо стремиться к снижению ассимптотической сложности алгоритма.
# Для данных задач в Python имеются встроенные библиотеки такие как cProfile, timeit.
# Одним из вариантов оптимизации для некоторых алгоритмов является мемоизация.

"""
Домашнее задание к уровку № 6 Алгоритмы и структуры данных на Python
Студент: Максим Сапунов Jenny6199@yandex.ru 04.08.2021

Задача №1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках
первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
"""
# ВАРИАНТ №2. Здесь установил и использую Memory_profiler

# $ pip install memory_profiler и далее запускал тест из CLI
# $ python -m memory_profiler task_1_2.py
# Демонстрация и выводы в комментариях после кода.

import random as rd


@profile    # При таком подходе PyCharm 'ругается' на данный декоратор.
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


@profile
def square_bubble_sort(array: list):
    """Сортировка массива методом 'пузырька'. Сложность алгоритма O(n**2)"""
    for _ in range(len(array)-1):
        for j in range(len(array)-1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
    return array


a1 = square_bubble_sort([rd.randint(0, 1000) for _ in range(1000)])
a2 = quick_sort([rd.randint(0, 1000) for _ in range(1000)])

#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     21   36.859 MiB   36.859 MiB         969   @profile    # При таком подходе PyCharm 'ругается' на данный декоратор.
#     22                                         def quick_sort(array: list):
#     23                                             """Сортировка массива методом быстрой сортировки Энтони Хоара."""
#     24   36.859 MiB    0.000 MiB         969       n = len(array)
#     25   36.859 MiB    0.000 MiB         969       if n <= 1:
#     26   36.859 MiB    0.000 MiB         485           return array
#     27                                             else:
#     28   36.859 MiB    0.000 MiB         484           l, m, r = [], [], []
#     29   36.859 MiB    0.000 MiB         484           b = array[int(n/2)]
#     30   36.859 MiB    0.000 MiB       10382           for el in array:
#     31   36.859 MiB    0.000 MiB        9898               if el > b:
#     32   36.859 MiB    0.000 MiB        4732                   r.append(el)
#     33   36.859 MiB    0.000 MiB        5166               elif el < b:
#     34   36.859 MiB    0.000 MiB        4330                   l.append(el)
#     35                                                     else:
#     36   36.859 MiB    0.000 MiB         836                   m.append(el)
#     37   36.859 MiB    0.000 MiB         484           return quick_sort(l) + m + quick_sort(r)

# Filename: task_1_2.py
#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     40   38.699 MiB   38.699 MiB           1   @profile
#     41                                         def square_bubble_sort(array: list):
#     42                                             """Сортировка массива методом 'пузырька'."""
#     43   38.699 MiB -941.441 MiB        1000       for _ in range(len(array)-1):
#     44   38.699 MiB -940491.727 MiB      999000           for j in range(len(array)-1):
#     45   38.699 MiB -939551.574 MiB      998001               if array[j] < array[j-1]:
#     46   38.699 MiB -60016.902 MiB      250513                   array[j], array[j-1] = array[j-1], array[j]
#     47   36.859 MiB   -1.840 MiB           1       return array

# ВЫВОДЫ: Профилировщики позволяют находить проблемные места в коде, расходующие ресурсы системы.
# в некоторых ситуациях удобно использовать встроенные функции языка, в других случаях необходимо использовать
# ранее созданные программы. Их необходимо постепенно осваивать и использовать при написании кода.
# Для небольших программ, взятых для примера это может быть неявным. Но по мере увеличения количества кода,
# без поиска "узких мест" невозможна будет оптимизация программы.


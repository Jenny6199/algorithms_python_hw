"""
Домашнее задание к 3-му уроку 'Алгоритмы и струтуры данных на Python'
Студент Максим Сапунов Jenny6199@yandex.ru 22.07.2021

Задача №6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
 Сами минимальный и максимальный элементы в сумму не включать.
"""
from random import randrange

# Заполняем массив случайными значениями и выводим его на дисплей.
arr_1 = [randrange(0, 100) for el in range(15)]
print(arr_1)
# Находим минимальное и максимальное значение в элементах массива и их индексы.
# Генераторы необходимы, так как в больших массивах может быть несколько значений соответствующих максимуму.
max_value = max(arr_1)
max_position = (el for el in range(len(arr_1)) if arr_1[el] == max_value)
min_value = min(arr_1)     # Если не использовать min, max - поиск миним. и максим. значения можно делать в цикле.
min_position = (el for el in range(len(arr_1)) if arr_1[el] == min_value)

print(min_value, max_value)

max_index = next(max_position)
min_index = next(min_position)

# Отрабатываем вариант различного расположения максимального и минимального значения в массиве
# так как по условию массив не отсортирован.
if min_index > max_index:
    result = sum(arr_1[max_index+1:min_index])
else:
    result = sum(arr_1[min_index+1:max_index])
print(result)

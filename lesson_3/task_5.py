"""
Домашнее задание к 3-му уроку 'Алгоритмы и струтуры данных на Python'
Студент Максим Сапунов Jenny6199@yandex.ru 22.07.2021

Задача №5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""
import random as rd
# Создаем тестовый массив элементов
arr_1 = [rd.randint(-10, 10) for el in range(100)]
# Поиск минимального элемента и сохранение его в переменную.
great_negative_element = 0
for el in arr_1:
    if el < great_negative_element:
        great_negative_element = el
# Одинаковые числа могут встречаться в нескольких позициях, отрабатываем с помощью генератора.
find_position = (i for i in range(len(arr_1)) if arr_1[i] == great_negative_element)
# Вывод результатов работы пограммы на дисплей.
print(f'\033[032m Значение максимального отрицательного элемента в массиве равно: {great_negative_element}.\033[0m')
print(f' Эелементы с данным значением находятся в позициях:')
for el in find_position:
    print(el)

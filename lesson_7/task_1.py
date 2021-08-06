"""
Домашнее задание к уроку №7. Алгоритмы и структуры данных на Python.\
Студент: Максим Сапунов Jenny6199@yandex.ru 06.08.2021

Задача №1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке (-100; 100). Выведите на экран исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""
import random


def bubble_sort(sorted_arr: list):
    """
    Сортировка списка методом 'пузырька'. Сложность O(n**2).
    :param sorted_arr: list - сортируемый список
    :return: result: list - отсортированный список
    """
    n = 1
    while n < len(sorted_arr):
        for i in range(len(sorted_arr) - n):
            if sorted_arr[i] > sorted_arr[i + 1]:
                sorted_arr[i], sorted_arr[i + 1] = sorted_arr[i + 1], sorted_arr[i]
        n += 1
    return sorted_arr


def make_matrix_output(arr):
    """Функция обеспечивает аккуратный вывод значений массива в виде матрицы"""
    for el in range(1, len(arr) + 1):
        print('%4d' % arr[el - 1], end='\n' if el % 10 == 0 else '  ')


get_array = [random.randint(-100, 100) for _ in range(100)]
make_matrix_output(get_array)
print('-'*100)
get_array = bubble_sort(get_array)
make_matrix_output(get_array)

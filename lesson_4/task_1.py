"""
Домашнее задание к уроку № 4 Алгоритмы и структуры данных на Python
Студент Максим Сапунов Jenny6199@yandex.ru 26.07.2021

Задача №1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""
import cProfile
from random import randint


def f1(n):
    """doc"""
    arr_1 = [randint(1, 999) for _ in range(n)]
    return arr_1


def f2(n):
    """doc"""
    arr_1 = list()
    for el in range(n):
        arr_1.append(randint(1, 999))
    return arr_1


cProfile.run('f1(5000000)')
cProfile.run('f2(5000000)')

"""
Домашнее задание к 3-му уроку 'Алгоритмы и струтуры данных на Python'
Студент Максим Сапунов Jenny6199@yandex.ru 21.07.2021

Задача №2. 2. Во втором массиве сохранить индексы четных элементов первого массива.
    Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив
    надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
    т.к. именно в этих позициях первого массива стоят четные числа.
"""

from random import randint, seed
seed(1)

# Генерируем первый массив
list_1 = [randint(1, 100) for _ in range(20)]
print(list_1)
# Генерируем второй массив из индексов элемента первого массива с условием
# проверки, что элемент первого массива является четным.
list_2 = [i for i in range(len(list_1)) if list_1[i] % 2 == 0]
print(list_2)

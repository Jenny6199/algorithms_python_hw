"""
Домашнее задание к уроку №7. Алгоритмы и структуры данных на Python.
Студент: Максим Сапунов Jenny6199@yandex.ru 06.08.2021

Задача №3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
Задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
то используйте метод сортировки, который не рассматривался на уроках
"""
import random


def search_middle(analysed_arr: list, rd_el=random.choice):
    """Поиск медианы."""
    k = len(analysed_arr)
    if k % 2 == 1:
        return search_elem(analysed_arr, k // 2, rd_el)
    else:
        return 0.5 * (search_elem(analysed_arr, k // 2 - 1, rd_el) +
                      search_elem(analysed_arr, k // 2, rd_el))


def search_elem(mass: list, k: int, base_el):
    """
    Функция выбирает элемент в списке.
    :param mass: список для анализа
    :param k: индекс
    :param base_el: функция выбора pivot, по умолчанию выбирает случайно
    :return: k-тый элемент lst
    """
    if len(mass) == 1:
        assert k == 0
        return mass[0]

    pivot = base_el(mass)

    lows = [el for el in mass if el < pivot]
    highs = [el for el in mass if el > pivot]
    pivots = [el for el in mass if el == pivot]

    if k < len(lows):
        return search_elem(lows, k, base_el)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return search_elem(highs, k - len(lows) - len(pivots), base_el)


m = 10
arr = [random.randint(-50, 50) for _ in range(2 * m + 1)]
print(arr)
print(f'В исходном массиве медианой является: {search_middle(arr)}')

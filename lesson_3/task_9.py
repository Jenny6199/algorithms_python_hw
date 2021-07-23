"""
Домашнее задание к уроку №3 Алгоритмы и структуры данных на Python.
Студент Максим Сапунов Jenny6199@yandex.ru 23.07.2021

Задача №9. Найти максимальный элемент из минимальных элементов столбцов матрицы
"""

from random import randrange


def get_max_in_min_for_column(matrix: list):
    """
    Функция вычисляет наибольший элемент среди минимальных значений в столбцах матрицы
    :param matrix:list - матрица в которой будет осуществлен поиск
    :return result: int - результат поиска среди элементов матрицы, соответсвующий условию.
    """
    # Создаем список для хранения минимальных значений в каждом из столбцов.
    min_value_from_column = []
    # С помощью двух вложенных циклов заполняем список значений столбцов
    # очищая его на каждой следующей итерации и формируем
    # список минимальных значений для столбцов.
    for i in range(5):
        column_values = []
        for j in range(5):
            column_values.append(matrix[j][i])
        min_value_from_column.append(min(column_values))
    # Находим максимальное значение из минимальных элементов столбцов.
    return max(min_value_from_column)


def get_random_matrix(length: int, height: int, boarder: int):
    """
    Функция создает матрицу со случайными значениями.
    :param length: int - длина строки
    :param height: int - количество строк.
    :param boarder: int - граница значений матрицы (от 0 до boarder).
    :return matrix: list - матрица (вложенные списки).
    """
    return [[randrange(0, boarder) for _ in range(length)] for _ in range(height)]


def run():
    """Агрегация работы функций и запуск программы"""
    # Создаем матрицу 5*5 для тестирования работы функции
    matrix_1 = get_random_matrix(5, 5, 100)
    # Для больших массивов вывод на дисплей избыточен, оставляю для наглядности.
    print('Будет осуществлен поиск наибольшего из минимальных элементов в столбцах матрицы.\n'
          'Представлена следующая матрица: ')
    print('-' * 50)
    for el in matrix_1:
        print(el)
    print('-' * 50)
    result = get_max_in_min_for_column(matrix_1)
    print(f'\033[032mМаксимальный эелемент из минимальных значений столбцов матрицы - {result}.\033[0m')


if __name__ == '__main__':
    run()

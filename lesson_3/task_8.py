"""
Домашнее задание к 3-му уроку 'Алгоритмы и струтуры данных на Python'
Студент Максим Сапунов Jenny6199@yandex.ru 22.07.2021

Задача №8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
    Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
    В конце следует вывести полученную матрицу.
"""

import re
import sys

# Размеры матрицы
_length = 4
_height = 4


class WrongInput(Exception):
    """ Обработка исключения при ошибках ввода пользователя. """

    def __init__(self, text):
        self.text = text


# Ввод данных пользователем
def user_make_digit_list(length: int):
    """
    Реализовано заполнение пользователем списка чисел и проверка данных перед записью.
    При ошибочном вводе вызывается исключение.
    :param length: int - длина строки.
    :return digit_list: list - список с числами введенных пользователем
    """
    print('\033[032mЗаполните строку матрицы целыми числами. (для выхода из программы введите q)\033[0m')
    digits_list = []
    i = 0
    while i != length:
        data = input('Введите число: ')
        if data.lower() == 'q':     # Прерывание работы программы пользователем.
            sys.exit()
        else:
            try:
                result = re.match(r'[-]\d+|\d+', data)
                if result is None:
                    raise WrongInput(f'\033[031mВведено - {data}. Ошибочный ввод. Попробуйте еще раз.\033[0m')
                else:
                    digits_list.append(int(result.group(0)))
                    i += 1
            except WrongInput as err:
                print(err)
    return digits_list


# Создание матрицы
def make_matrix(length: int, height: int):
    """
    Функция создает матрицу с заданной длиной строки и количеством строк, используя вложенные списки.
    :param length: int - длина строки
    :param height: int - количество строк.
    :return:
    """
    matrix = [user_make_digit_list(length) for _ in range(height)]
    return matrix


# Добавление суммы элементов в каждую строку матрицы.
def add_sum_data_to_each_link(array: list):
    """
    Функция добавляет к каждой строке матрицы значение с суммой элементов строки
    :return matrix:list
    """
    for link in array:
        link.append(sum(link[0:len(link)]))
    return array


# Аккуратный вывод результатов на дисплей.
def get_descriptive_output(array: list):
    """Функция обеспечивает аккуратный вывод результатов на дисплей."""
    decor = '-'*50
    print('\n\033[032mВ результате ввода данных получена следующая матрица: \033[0m')
    print(decor)
    for el in array:
        print(el)
    print(decor)
    # Дальше усложнять посчитал избыточным. Даешь pandas! :)


def run():
    """Агрегация работы функций и запуск программы."""
    matrix_1 = make_matrix(_length, _height)
    matrix_1 = add_sum_data_to_each_link(matrix_1)
    get_descriptive_output(matrix_1)


if __name__ == '__main__':
    run()

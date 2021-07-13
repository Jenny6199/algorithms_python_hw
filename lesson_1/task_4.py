"""
Практическое задание к уроку № 1 Алгоритмы и структуры данных на Python. Базовый курс
Студент Максим Сапунов, Jenny6199@yandex.ru
13.07.2021.

Задача №4. Написать программу, которая генерирует в указанных пользователем границах:
    - случайное целое число;
    - случайное вещественное число;
    - случайный символ.
   Для каждого из трех случаев пользователь задает свои границы диапазона.
   Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
   Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""
import random as rd


def get_users_boarder():
    """
    Функция запрашивает у пользователя границы диапазона выборки и возвращает их в виде кортежа.
    :return - кортеж со значением границ диапазона.
    """
    boarders = [input('Введите значения диапазона: ') for _ in range(2)]
    return boarders[0], boarders[1]


def random_symbol(data: tuple):
    """
    Функция возвращает случайный символ латинского алфавита.
    :param data: tuple - кортеж с границами диапазона
    :return result: str - случайный символ заданного диапазона.
    """
    symbols = [chr(el) for el in range(97, 123)]
    boarder_index_right = (i for i, e in enumerate(symbols) if e == data[0])
    boarder_index_left = (i for i, e in enumerate(symbols) if e == data[1])
    result = symbols[rd.randint(next(boarder_index_right), next(boarder_index_left))]
    return result


def random_integer(data: tuple):
    """
    Функция возвращает случайное целое число из полученного диапазона
    :param data: tuple - кортеж с границами диапазона.
    :return: result: int - случайное число в границах диапазона.
    """
    result = rd.randint(int(data[0]), int(data[1]))
    return result


def random_float(data: tuple):
    """
    Функция возвращает случайное вещественное число в границах заданного диапазона
    :param data: tuple - кортеж с границами диапазона.
    :return: result: int - случайное вещественное число в границах диапазона.
    """
    result = rd.uniform(float(data[0]), float(data[1]))
    return result


def run():
    print('Генерация случайного символа: ')
    data_1 = get_users_boarder()
    print(random_symbol(data_1))
    print('Генерация случайного целого числа: ')
    data_2 = get_users_boarder()
    print(random_integer(data_2))
    print('Генерация случайного вещественного числа: ')
    data_3 = get_users_boarder()
    print(random_float(data_3))


if __name__ == '__main__':
    run()

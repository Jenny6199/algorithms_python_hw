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
    :return - list список со значением границ диапазона.
    """
    boarders = [input('Введите значение диапазона: ') for _ in range(2)]
    return boarders


def data_parser(data: str):
    """
    Функция определяет какие данные ввел пользователь.
    Если введено число, вещественное число или буква алфавита возвращает соответствующее сообщение.
    Если введены другие данные возвращает False.
    :param data - str анализируемая строка.
    :return в зависимости от полученных данных возвращает 'int', 'float', 'str' или False
    """
    if len(data) == 1:      # Если введен 1 символ.
        try:
            data = int(data)
            return 'int'
        except ValueError:
            symbols = [chr(el) for el in range(97, 123)]    # Латинский алфавит.
            if data in symbols:     # Поиск символа в границах алфавита.
                return 'str'
            else:
                return False
    else:       # Если введено несколько символов.
        if chr(46) in data:     # Если в строке имеется точка.
            try:        # Преобразовать к вещественному числу
                float(data)
                return 'float'
            except ValueError:
                return False
        else:       # Если точки в строке нет.
            try:        # Преобразовать к целому числу
                int(data)
                return 'int'
            except ValueError:
                return False


def random_symbol(data: list):
    """
    Функция возвращает случайный символ латинского алфавита.
    :param data: list - список с границами диапазона
    :return result: str - случайный символ заданного диапазона.
    """
    symbols = [chr(el) for el in range(97, 123)]
    if data[0] > data[1]:
        data[0], data[1] = data[1], data[0]
    boarder_index_right = (i for i, e in enumerate(symbols) if e == data[0])
    boarder_index_left = (i for i, e in enumerate(symbols) if e == data[1])
    result = symbols[rd.randint(next(boarder_index_right), next(boarder_index_left))]
    return result


def random_integer(data: list):
    """
    Функция возвращает случайное целое число из полученного диапазона
    :param data: list список с границами диапазона.
    :return: result: int - случайное число в границах диапазона.
    """
    data[0], data[1] = int(data[0]), int(data[1])
    if data[0] > data[1]:       # Если границы диапазона были введены в обратном порядке.
        data[0], data[1] = data[1], data[0]
    result = rd.randint(data[0], data[1])
    return result


def random_float(data: list):
    """
    Функция возвращает случайное вещественное число в границах заданного диапазона
    :param data: list - список с границами диапазона.
    :return: result: int - случайное вещественное число в границах диапазона.
    """
    data[0], data[1] = float(data[0]), float(data[1])
    if data[0] > data[1]:
        data[0], data[1] = data[1], data[0]
    result = rd.uniform(data[0], data[1])
    return result


def run():
    """Агрегация функций и запуск работы программы."""
    print('\033[035mПрограмма  в зависимости от типа введенных данных генерирует в указанном диапазоне: '
          'случайное целое число, случайное вещественное число или случайный символ.\033[0m')
    data = get_users_boarder()
    if data_parser(data[0]) == 'int' and data_parser(data[1]) == 'int':
        result = random_integer(data)
    elif data_parser(data[0]) == 'float' and data_parser(data[1]) == 'float':
        result = random_float(data)
    elif data_parser(data[0]) == 'str' and data_parser(data[1]) == 'str':
        result = random_symbol(data)
    else:
        result = '\033[031m Ошибка ввода данных!\033[0m'
    print(result)


if __name__ == '__main__':
    run()

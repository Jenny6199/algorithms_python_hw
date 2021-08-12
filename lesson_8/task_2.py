"""
Домашнее задание к уроку № 8 Алгоритмы и структуры данных на Python
студент Максим Сапунов Jenny6199@yandex.ru 08.08.2021

Задача №2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""
# Реализация через словарь и коллекции.
from collections import deque, Counter


def create_frequency_deque(line: str):
    """
    Функция принимает строку и возвращает дэк содержащий кортежи со значением символа и частоты его
    встречаемости в данной строке.
    :param line: str - строка для анализа.
    :return frequency_deque
    """
    tmp_dict = Counter(line)
    frequency_deque = deque(sorted(tmp_dict.items(), key=lambda item: item[1]))
    return frequency_deque


def create_tree(frequency_table: deque):
    """
    Функция принимает частотную таблицу и выстраивает дерево по алгоритму Хаффмана в виде вложенных словарей.
    :param frequency_table: deque - частотная таблица
    :return tree - дерево в виде вложенных словарей.
    """
    tree = None
    if len(frequency_table) > 1:
        for _ in range(len(frequency_table) - 1):
            freq = frequency_table[0][1] + frequency_table[1][1]
            tree = {0: frequency_table.popleft()[0], 1: frequency_table.popleft()[0]}
            frequency_table.appendleft((tree, freq))
            for el in range(len(frequency_table) - 1):
                if freq > frequency_table[el + 1][1]:
                    frequency_table[el], frequency_table[el + 1] = frequency_table[el + 1], frequency_table[el]
                else:
                    break
    else:
        tree = {0: frequency_table[0][0], 1: None}
    return tree


def create_code_line(my_tree, code_str=''):
    """Функция для кодирования символа в дереве"""
    if not isinstance(my_tree, dict):
        code_dict[my_tree] = code_str
    else:
        create_code_line(my_tree[0], code_str=code_str + '0')
        create_code_line(my_tree[1], code_str=code_str + '1')


def run(string):
    """Агреграция работы функций и запуск программы."""
    create_code_line(create_tree(create_frequency_deque(string)))
    for i in string:
        print(code_dict[i], end=" ")


if __name__ == '__main__':
    code_line: str = 'hello new world!'
    code_dict = {}
    run(code_line)

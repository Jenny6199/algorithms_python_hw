"""
Практическое задание к уроку № 1 Алгоритмы и структуры данных на Python. Базовый курс
Студент Максим Сапунов, Jenny6199@yandex.ru
12.07.2021.

Задача № 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""

import sys


def check_input():
    """
    Функция выводит приветственное сообщение изапрашивает ввод данных у пользователя.
    :return - number:int - число.
    """
    number = input(' Введите трехзначное число и нажмите Enter: ')
    try:
        number = int(number)
        return number
    except ValueError:
        print('Input data error')
        sys.exit()


def parser_digit_var1(number=0):
    """
    Функция создает список из цифр составляющих полученное число и возврает их сумму и произведение в виде кортежа
    :return: var1 - сумма цифр, var2 - произведение цифр.
    """
    digit = [int(el) for el in str(number)]
    var1 = digit[0] + digit[1] + digit[2]
    var2 = digit[0] * digit[1] * digit[2]
    return var1, var2


def run():
    """Запуск расчета и вывод результатов на дисплей"""
    digit = check_input()
    result = parser_digit_var1(digit)
    print(f'сумма чисел составляющих введенное число: {result[0]}, произведение: {result[1]}')


if __name__ == '__main__':
    run()

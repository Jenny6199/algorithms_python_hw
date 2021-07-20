"""
Домашнее задание к уроку № 2 "Алгоритмы и структуры данных на Python"
Студент: Максим Сапунов Jenny6199@yandex.ru 19.07.2021

Задача №8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""
from collections import Counter
from sys import exit


def checker_input(n1, n2):
    """Проверка корректности введенных данных"""
    try:
        int(n1)
        int(n2)
    except ValueError:
        print('\033[031m Ошибка! Вы ввели не число.\033[0m')
        return False
    if 0 <= int(n2) <= 9:
        return True
    else:
        print('\033[031m Ошибка! Необходимо ввести цифру.\033[0m')
        return False


def user_data():
    """
    Запрашивает ввод данных у пользователя, вызывает функцию checker_input для обработки ошибок ввода.
    :return (var1, var2) - анализируемое число и цифра встречаемость которой необходимо посчитать.
    """
    while True:     # Цикл будет завершен либо при получении верных данных, либо прерван пользователем.
        var1 = input(' Введите число для анализа: ')
        var2 = input(' Встечаемость какой цифры вы хотите посчитать? ')
        if var1.lower() == 'q' or var2.lower() == 'q':  # Выход из программы по запросу пользователя
            exit()
        if checker_input(var1, var2):
            return var1, var2       # Если проверка пройдена успешно - выйти из цикла
        else:
            print('Повторите ввод данных или введите q для выхода:')
            continue


# Решение через Counter
def run1():
    """Агрегация функций и запуск работы программы."""
    data = user_data()
    result = Counter(data[0])
    print('-'*50)
    print(f' Количество повторений цифры {data[1]} в числе {data[0]} составило - {result[data[1]]}.')


# Решение через цикл.
def run2():
    """Агрегация функций и запуск работы программы."""
    data = user_data()
    analyzing_string = data[0]
    finding_digit = data[1]
    result = 0
    for i in analyzing_string:
        if i == finding_digit:
            result += 1
    print(f' Количество повторений цифры {data[1]} в числе {data[0]} составило - {result}.')


# Вариант решения через рекурсию.
def number_counter(analyzing_string, finding_digit, result=0):
    """
    Производит подсчет встречаемости цифры в анализируемом числе использую рекурсивный алгоритм.
    :param analyzing_string - число в котором будет осуществляться подсчет.
    :param finding_digit - цифра количество повторений которой будет подсчитано.
    :param result - количество повторений искомой цифры в числе, в начале работы функции по умолчанию равен 0.
    """
    digit = analyzing_string % 10
    if digit == finding_digit:
        result += 1
    if analyzing_string == 0:       # Крайний случай (осталась 1 цифра)
        return result
    else:          # Рекурсивный случай (осталось более 1 цифры)
        return number_counter(analyzing_string//10, finding_digit, result)


def run3():
    """Агрегация функций и запуск работы программы."""
    data = user_data()
    analyzing_string = int(data[0])
    finding_digit = int(data[1])
    result_of_count = number_counter(analyzing_string, finding_digit)
    print(f' Количество повторений цифры {data[1]} в числе {data[0]} составило - {result_of_count}.')


if __name__ == '__main__':
    run1()
    run2()
    run3()

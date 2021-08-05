"""
Домашнее задание к уровку № 6 Алгоритмы и структуры данных на Python
Студент: Максим Сапунов Jenny6199@yandex.ru

Задача №1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках
первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
"""
# ВАРИАНТ №1. Здесь использовал cProfile и sys.getsizeof()

import sys
import cProfile
import pprint


# Для примера взял программу 'калькулятор' из урока №2.

class Calculator:
    """ Учебное представление калькулятора """

    operand_list = ['+', '-', '*', '/']
    flag = True

    def __init__(self):
        """ Конструктор класса."""
        self.input_log = []
        self.calculate_log = []
        self.formula = ''
        self.digit_1 = None
        self.digit_2 = None
        self.operator = None

    def insert_operator(self):
        """ Пользователь вводит оператор."""
        while self.flag:
            operator = input('Выберете операцию +, -, *, / и нажмите Enter:')
            self.input_log.append(operator)
            if operator in self.operand_list:
                return operator
            elif operator == 'q' or operator == 'Q':
                print('\033[031mОперация прервана пользователем.\033[0m')
                self.flag = False
                break
            else:
                print('\033[031m  Ошибка! Неверный ввод.\033[0m')
                print('\033[96m  Попробуйте еще раз, можно вводить операторы +. -. *. /\033[0m')

    def insert_digit(self):
        """ Пользователь вводит число."""
        digit = None
        while self.flag and type(digit) != float:
            digit = input('Введите число и нажмите Enter: ')
            if digit == 'q' or digit == 'Q':
                self.flag = False
                break
            try:
                digit = float(digit)
            except ValueError:
                print('\033[031m  Ошибка! Вы ввели не число.\033[0m')
                print('\033[96m  Попробуйте еще раз - можно вводить целые и дробные числа:\033[0m')
        return digit

    def show_input_log(self):
        """ Просмотр журнала ввода данных пользователем."""
        print('Input log:')
        for el in self.input_log:
            print(el)

    def get_result(self):
        """ Подсчет финального результата."""
        if self.flag:
            if self.operator == '+':
                return self.digit_1 + self.digit_2
            elif self.operator == '-':
                return self.digit_1 - self.digit_2
            elif self.operator == '/':
                try:
                    result = self.digit_1 / self.digit_2
                    return result
                except ZeroDivisionError:
                    print('\033[031m Ошибка! Делить на ноль нельзя!\033[0m')
            elif self.operator == '*':
                return self.digit_1 * self.digit_2
        else:
            return str('Программа завершает работу по запросу пользователя.')

    def create_formula(self):
        """ Конкатенация формулы из введенных пользователем значений. """
        if self.flag:
            print(f'Выполняется расчет: {self.digit_1} {self.operator} {self.digit_2} :')

    def new_calculate(self):
        """ Запуск расчета."""
        self.digit_1 = self.insert_digit()
        self.operator = self.insert_operator()
        self.digit_2 = self.insert_digit()
        self.create_formula()
        print(self.get_result())
        if self.flag:                   # Здесь реализован рекурсивный запуск функции.
            print('Новый расчет:')
            self.new_calculate()


def total_memory_size(var_list: list):
    """
    Функция получает список использованных переменных и возвращает общее количество памяти на них затраченное.
    для реализации использована функция sys.getsizeof()
    :param var_list: list - список переменных использованных в функции
    :return result: int - количество байт израсходованных на переменные.
    """
    result = 0
    for el in var_list:
        result += sys.getsizeof(el)
    return result


if __name__ == '__main__':
    v1 = Calculator()
    cProfile.run('v1.new_calculate()')
    print('На переменные в анализируемой программе израсходовано:  ')
    # Создаю списки используемых переменных и передаю их в функцию для вычисления количества памяти.
    var_list_general = [v1.__dir__()]
    # pprint.pprint(var_list_general) # Можно распечатать и ознакомиться.
    print(f'Экземпляр класса Calculator израсходовано - {total_memory_size(var_list_general)} байт.')
    print(f'Информация о системе: \n{sys.version}')


# "C:/Root/3379 Сапунов/Разное/Програмирование/GeekBrains/Python_alg_2/algorithms_python_hw/lesson_6/task_1_1.py"
# Введите число и нажмите Enter: 2
# Выберете операцию +, -, *, / и нажмите Enter:+
# Введите число и нажмите Enter: 2
# Выполняется расчет: 2.0 + 2.0 :
# 4.0
# Новый расчет:
# Введите число и нажмите Enter: q
# Программа завершает работу по запросу пользователя.
#          36 function calls (35 primitive calls) in 9.739 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    9.739    9.739 <string>:1(<module>)
#         4    0.000    0.000    0.000    0.000 codecs.py:319(decode)
#         4    0.000    0.000    0.000    0.000 codecs.py:331(getstate)
#         2    0.000    0.000    1.068    0.534 task_1.py:34(insert_operator)
#         4    0.000    0.000    8.671    2.168 task_1.py:49(insert_digit)
#         2    0.000    0.000    0.000    0.000 task_1.py:70(get_result)
#         2    0.000    0.000    0.000    0.000 task_1.py:88(create_formula)
#       2/1    0.000    0.000    9.739    9.739 task_1.py:93(new_calculate)
#         4    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
#         1    0.000    0.000    9.739    9.739 {built-in method builtins.exec}
#         4    9.738    2.435    9.738    2.435 {built-in method builtins.input}
#         4    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#         1    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# На переменные в анализируемой программе израсходовано:
# Экземпляр класса Calculator израсходовано - 384 байт.
# Информация о системе:
# 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)]
#
# Process finished with exit code 0
# -----------------------------------------------------------
# ВЫВОДЫ
# Исследованная программа работает без избыточного потребления памяти,
# Временные задержки возникают только на вводе данных в программу.

# PS пример оказался не очень удачным, продолжение в следующем файле.

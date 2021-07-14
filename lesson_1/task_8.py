"""
Практическое задание к уроку № 1 Алгоритмы и структуры данных на Python. Базовый курс
Студент Максим Сапунов, Jenny6199@yandex.ru
14.07.2021.

Задача № 8. Определить, является ли год, который ввел пользователь, високосным или невисокосным.
"""
import sys


try:
    year = (int(input('Введите год: ')))
except ValueError:
    print(' \033[041mОшибка ввода данных!\033[0m')
    sys.exit()
result = 366 if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)) else 365
print(result)

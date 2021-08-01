"""
Домашнее задание к уроку №5 Алгоритмы и структуры данных на Python
Студент: Максим Сапунов Jenny6199@yandex.ru 31.07.2021

Задача №1.  Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
"""
import collections
import pprint

organizations = collections.defaultdict()
n = int(input('Введите количество предприятий: '))
b = 0
for i in range(n):
    org_name = input('Введите название предприятия: ')
    balance = 0
    for i in range(1, 5, 1):
        print(f' Введите прибыль за {i}-й квартал:')
        balance += int(input())
    average = balance/4
    organizations[org_name] = average
    b += average

medium = b / n
print('Cредняя прибыль для всех предприятий: %.0f.' % medium,
      '\n Предприятия с прибылью больше среднего: ')
for i in organizations:
    if organizations[i] > medium:
        print(i)
print(' Предприятия с прибылью меньше среднего:')
for i in organizations:
    if organizations[i] < medium:
        print(i)

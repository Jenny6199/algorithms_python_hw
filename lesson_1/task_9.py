"""
Практическое задание к уроку № 1 Алгоритмы и структуры данных на Python. Базовый курс
Студент Максим Сапунов, Jenny6199@yandex.ru
14.07.2021.

Задача №9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
"""
import sys


def get_users_data():
    """
    Функция запрашивает у пользователя три числа, возвращает их в основную ветку программы в виде генератора,
    а также обеспечиивает обработку ошибок ввода.
    :return data: генератор.
    """
    try:
        data = [float(input('Введите целое или вещественное число: ')) for _ in range(3)]
        yield data
    except ValueError:
        print('\033[031m Ошибка ввода данных! \033[0m')
        sys.exit()


def get_medium_digit(v1: float, v2: float, v3: float):
    """
    Функция получает три различных числа и сравнивает их между собой, возвращает среднее значение.
    :param v1: float 1 число
    :param v2: float 1 число
    :param v3: float 1 число
    :return medium - среднее из трех полученных чисел.
    """
    # Согласно условию учебной задачи реализация выполнена в виде линейного алгоритма.
    if v1 > v2:
        if v1 > v3:
            if v3 > v2:
                medium_value = v3
            else:
                medium_value = v2
        else:
            medium_value = v1
    else:
        if v2 > v3:
            if v3 > v1:
                medium_value = v3
            else:
                medium_value = v1
        else:
            medium_value = v2
    return medium_value


def comparison():
    """
    Функция обеспечивает сравнение трех чисел, если есть равные числа выводит сообщение и завершает программу,
    если все числа между собой не равны передает данные в функцию get_medium_digit.
    """
    var1, var2, var3 = next(get_users_data())
    if var1 == var2 and var2 == var3:
        print(f'Все введенные числа равны между собой. Значение {var1}.')
        sys.exit()
    elif var1 == var2 or var2 == var3 or var1 == var3:
        print(f'Два из введенных чисел равны между собой. Наибольшее значение {max(var1, var2, var3)}.')
        sys.exit()
    else:
        medium = get_medium_digit(var1, var2, var3)
        return medium


def run():
    """Запуск работы функции и аккуратный вывод результата."""
    searched_value = comparison()
    decor = '-'*50
    print(f'{decor}\nСредним является число: \033[034m{searched_value}\033[0m.')


if __name__ == '__main__':
    run()

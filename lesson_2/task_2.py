"""
Домашнее задание к уроку №2. Алгоритмы и структуры данных на Python.
Студент: Максим Сапунов. Jenny6199@yandex.ru 18.07.2021

Задача
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""


class CheckerDigit:
    """ Подсчет количества четных и нечетных чисел в введенном числе"""
    even_list = [2, 4, 6, 8]
    odd_list = [1, 3, 5, 7, 9]

    def __init__(self):
        """ Конструктор класса."""
        print('Программа выполняет подсчет количества нечетных, четных и нулей в числе.')
        self.even = 0
        self.odd = 0
        self.zero = 0

    def counter(self, digit):
        """
        Сортирующая функция.
        :param - digit - анализируемая цифра.
        :return - None
        """
        if digit in self.even_list:
            self.even += 1
        elif digit in self.odd_list:
            self.odd += 1
        elif digit == 0:
            self.zero += 1

    def recursive_division(self, digit):
        """
        Функция рекурсивно осуществляет разделение числа на составляющие его цифры,
        Выводит на экран результирующие сведения.
        :param - digit - разделяемое на составляемые цифры число.
        :return - None
        """
        if digit == 0:  # Крайний случай рекурсии.
            print(f'Во введенном числе:\n Нечетных цифр:{self.odd}\n Четных цифр:{self.even}\n Нулей:{self.zero}')
        else:
            number = digit % 10
            digit = digit // 10
            self.counter(number)
            self.recursive_division(digit)  # Рекурсивный вызов функции.


if __name__ == '__main__':
    v1 = CheckerDigit()
    inserted_digit = int(input('Введите число: '))
    v1.recursive_division(inserted_digit)

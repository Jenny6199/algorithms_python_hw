"""
Домашнее задание к уроку №5 Алгоритмы и структуры данных на Python
Студент: Максим Сапунов Jenny6199@yandex.ru 31.07.2021

Задача №2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""


class HexDigit:
    """Содержит функции для работы с шестнадцатеричными числами"""

    # Список элементов
    string_to_digits = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'a': 10,
        'b': 11,
        'c': 12,
        'd': 13,
        'e': 14,
        'f': 15
    }

    digits_to_string = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: 'a',
        11: 'b',
        12: 'c',
        13: 'd',
        14: 'e',
        15: 'f'
    }

    def __init__(self, string):
        """Конструктор класса"""
        self.string = list(string.lower())
        self.hex_digit = list()
        self.decimal_digit = 0

    def __add__(self, other):
        if not isinstance(other, HexDigit):
            raise ValueError('Операнды должны быть объектами HexDigit')
        return HexDigit.convert_to_hex(self, self.convert_to_int() + other.convert_to_int())

    def __mul__(self, other):
        if not isinstance(other, HexDigit):
            raise ValueError('Операнды должны быть объектами HexDigit')
        return HexDigit.convert_to_hex(self, self.convert_to_int() * other.convert_to_int())

    def convert_to_int(self):
        """Преобразовавыет строковую запись шеснадцатиричного числа в десятичное число"""
        for i in range(len(self.string)):
            bar = self.string_to_digits[self.string.pop()]
            self.hex_digit.append(bar)
        number_of_hex_digits = len(self.hex_digit)
        for j in range(number_of_hex_digits):
            self.decimal_digit += self.hex_digit[j] * (16 ** j)
        self.hex_digit = []
        return self.decimal_digit

    def convert_to_hex(self, decimal_digit: int):
        """Функция преобразовывает десятичное число в шестнадцатиричное и возвращает в виде строки."""
        self.hex_digit = []
        while decimal_digit != 0:
            self.hex_digit.append(self.digits_to_string[decimal_digit % 16].upper())
            decimal_digit = decimal_digit // 16
        result = str(''.join(reversed(self.hex_digit)))
        self.hex_digit = []
        return result


a = HexDigit('a2')
b = HexDigit('c4f')
print(a + b)
print(a * b)

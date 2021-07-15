"""
Практическое задание к уроку № 1 Алгоритмы и структуры данных на Python. Базовый курс
Студент Максим Сапунов, Jenny6199@yandex.ru
12.07.2021.

Задача №2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.
"""


def bit_operations(var1=5, var2=6):
    """
    Функция обеспечивает побитовые операции над числами.
    :param var1 - int
    :param var2 - int
    :return - информационное сообщение на дисплей результаты логических операций над числами:
    'И', 'ИЛИ', 'НЕ', 'Искл.ИЛИ, логический сдвиг вправо для var1, логический сдвиг влево для var1'
    """
    bit_and = bin(var1 & var2)      # Побитовое И
    bit_or = bin(var1 | var2)       # Побитовое ИЛИ
    bit_not_var1 = bin(~var1)       # Побитовое НЕ
    bit_not_var2 = bin(~var2)
    bit_xor = bin(var1 ^ var2)      # Побитовое искл.ИЛИ
    var1_slide_right = bin(var1 >> 2)       # Логический сдвиг вправо
    var1_slide_left = bin(var1 << 2)        # Логический сдвиг влево

    print(f'{bit_and=} = {int(bit_and, 2)}')
    print(f'{bit_or=} = {int(bit_or, 2)}')
    print(f'{bit_xor=} = {int(bit_xor, 2)}')
    print(f'{bit_not_var1=} = {int(bit_not_var1, 2)}')
    print(f'{bit_not_var2=} = {int(bit_not_var2, 2)}')      # Комплемент делает число отрицательным
    print(f'{var1_slide_right=} = {int(var1_slide_right, 2)}')      # Эквивалентно var1 / 2 ** n, но в разы быстрее
    print(f'{var1_slide_left=} = {int(var1_slide_left, 2)}')        # Эквивалентно var1 * 2 ** n, но в разы быстрее


if __name__ == '__main__':
    bit_operations(81, 48)

# На игровой рулетке в казино 38 выемок для шарика: 18 красных,
# столько же черных и две зеленые, пронумерованные 0 и 00 соответственно.
# Красные числа на рулетке: 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30 32, 34 и 36.
# Остальные номера в диапазоне положительных чисел до 36 – черные.
# Импортируем модуль случайных чисел random.
import random

# Вызываем случайное число от 0 до 37 включительно через оператор randint. Цифра 37 тождественна - "00".
# Присваиваем строке число.
number = int(random.randint(0, 37))
# Создаём условие и при выполнении его присваиваем переменную number одному из условий.
if 1 <= number <= 36:
    print('Выпавший номер:', number)
    print('Выигравшая ставка:', number)
# Создаём список красных чисел.
red_number = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
# берём по очереди каждое строковое число из списка,
# присваиваем ему числовое значение и проверяем равно ли оно переменной number.
for i in red_number:
    if int(i) == number:
        # Если равно - выполняется условие.
        print('Выигравшая ставка: красное')
# Создаём список чёрных чисел.
black_number = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
# берём по очереди каждое строковое число из списка,
# присваиваем ему числовое значение и проверяем равно ли оно переменной number.
for i in black_number:
    if int(i) == number:
        # Если равно - выполняется условие.
        print('Выигравшая ставка: чёрное')
# Проверка рандомного числа на нечётность
if number != 0 and number != 37 and number % 2 == 1:
    print('Выигравшая ставка: нечётное')
# Проверка рандомного числа на чётность
if number != 0 and number != 37 and number % 2 == 0:
    print('Выигравшая ставка: чётное')
# Проверка первого условия и его вывод.
if 1 <= number <= 18:
    print('Выигравшая ставка: от 1 до 18')
# Проверка второго условия и его вывод.
if 19 <= number <= 36:
    print('Выигравшая ставка: от 19 до 36')
# Работа с условием для "0"
if number == 0:
    print('выпавший номер: 0')
    print('выигравшая ставка: 0')
# Работа с условием для "00". Цифра 37 была тождественна - "00".
if number == 37:
    print('выпавший номер: 00')
    print('выигравшая ставка: 00')

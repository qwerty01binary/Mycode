# В данном упражнении вы должны написать программу для подсчета
# среднего значения всех введенных пользователем чисел.
# Индикатором окончания ввода будет служить ноль.
# При этом программа должна выдавать соответствующее сообщение об ошибке, если первым же введенным
# пользователем значением будет ноль.

number = 0
running = True
# Создаём пустой список
enter_numbers = []
# Создаём цикл при котором переменная running есть истина.
while running:
    # Запрашиваем у пользователя ввести число.
    enter_number = int(input('Введите любое целое число: '))
# Вводим последний номер списка. При первом вводе он же - первый.
    enter_numbers.append(enter_number)
    # Проверяем, является ли первый номер - 0. Если - да, то удаляем его и выводим - "ошибка".
    if enter_numbers[0] == number:
        del enter_numbers[0]
        print('ошибка')
        # Ставим условие, что если первый номер не равен "0" а последний равен - "0", то выводим список на экран,
        # заканчиваем цикл и переходим к дальнейшей работе программы.
    elif enter_numbers[0] != number and enter_numbers[-1] == number:
        del enter_numbers[-1]
        print('Вы ввели', enter_numbers)
        break
plus = sum(enter_numbers)
print('Сумма всех введённых Ваших чисел равна:', plus)
elements = len(enter_numbers)
print('Количество введённых Вами элементов:', elements)
average = plus / elements
print('Среднее значение введённых Вами чисел составляет:', average)




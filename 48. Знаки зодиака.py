# Напишите программу, запрашивающую у пользователя дату его рождения и выводящую на экран соответствующий знак зодиака.
date_birth = int(input('Введите дату своего рождения: '))
month_birth = input('Введите месяц своего рождения: ')
# вводим условие при котором знак - козерог
if (22 <= date_birth < 30 and month_birth == 'декабрь') or (1 <= date_birth <= 19 and month_birth == 'январь'):
    print('Вы козерог')
else:
    print('Вы не козерог')

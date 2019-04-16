# Домашнее задание №1
# Упражнение №4
# Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.
# Автор Чантурия Д. Г.
import random

print('Случайное целое число:')
number_start_range = int(input('Начало границы: '))
number_end_range = int(input('Конец границы: '))

print('Случайное вещественное число:')
float_start_range = float(input('Начало границы: '))
float_end_range = float(input('Конец границы: '))

print('Случайны символ:')
symbol_start_range = ord(input('Начало границы (символ): '))
symbol_end_range = ord(input('Конец границы (символ): '))

number_random = random.randint(number_start_range, number_end_range)
float_random = random.uniform(float_start_range, float_end_range)
symbol_random = chr(random.randint(symbol_start_range, symbol_end_range))

print(f'Случайное целове число: {number_random}')
print(f'Случайное вещественное число: {float_random}')
print(f'Случайный символ: {symbol_random}')
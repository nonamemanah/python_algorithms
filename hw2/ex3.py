# Домашнее задание №2
# Упражнение №3
# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран
# Автор Чантурия Д. Г.

number = int(input('Введите целое число: '))
second = 0
result = ''
while number > 0:
    second = number % 10;
    result += f'{second}'
    number = number // 10

print(result)
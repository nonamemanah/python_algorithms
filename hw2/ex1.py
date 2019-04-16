# Домашнее задание №2
# Упражнение №1
# Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться,
# а должна запрашивать новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0'
# в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
# сообщать ему об ошибке и снова запрашивать знак операции. Также сообщать пользователю о невозможности деления на ноль,
# если он ввел 0 в качестве делителя.
# Автор Чантурия Д. Г.

def evaluate(first_number, second_number, operator):
    if operator == '+':
        return first_number + second_number
    if operator == '-':
        return second_number - first_number
    if operator == '*':
        return first_number * second_number
    if operator == '/':
        return second_number / first_number

def show_main_menu():
    operator = ''
    while operator != '0':
        print('-- Программа для сложения, вычитания, умножения и деления двух чисел --')
        operator = input('Оператор (+, -, *, /, 0 - выход): ')
        if operator != '0':
            first_number = int(input('Первое число: '))
            second_number = int(input('Второе число: '))
            print(f'{evaluate(first_number, second_number, operator)}')

show_main_menu()

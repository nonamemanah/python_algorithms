# Домашнее задание №1
# Упражнение №2
# Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
# Автор Чантурия Д. Г.
first = 5
second = 6

and_result = first & second
or_result = first | second
xor_result = first ^ second
left_result = first << 3
right_result = first >> 3
not_result = ~first

print(f'{first} in bin format {bin(first)}')
print(f'{second} in bin format {bin(second)}')
print(f'AND operation result: {bin(and_result)} ({and_result})')
print(f'OR operation result: {bin(or_result)} ({or_result})')
print(f'XOR operation result: {bin(xor_result)} ({xor_result})')
print(f'left shift operation result: {bin(left_result)} ({left_result})')
print(f'right shift operation result: {bin(right_result)} ({right_result})')
print(f'NOT 5 result: {bin(not_result)} ({not_result})')

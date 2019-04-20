'''
Задание: В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
Автор: Чантурия Д. Г.
'''
result = [0] * 8
for item in range(2, 100):
    for i in range(2, 10):
        if item % i == 0:
            result[i - 2] += 1

for idx, item in enumerate(result):
    print(f'{idx + 2}: {item}')

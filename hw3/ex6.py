'''
Задание: В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
         Сами минимальный и максимальный элементы в сумму не включать.
Автор: Чантурия Д. Г.
'''
N = 5
array = [0] * N

for i in range(N):
    array[i] = int(input('Введите число: '))

min_element = max_element = array[i]
min_index = max_index = 0
for index, element in enumerate(array):
    if element < min_element:
        min_element = element
        min_index = index
    else:
        max_element = element
        max_index = index

print(f'min: {min_element}, max: {max_element}')
if min_index > max_index:
    min_index, max_index = max_index, min_index

sum = 0
for i in range(min_index + 1, max_index):
    sum += array[i]
print(f'Сумма элементов, находящихся между минимальным и максимальным элементами: {sum}')

'''
Задание: В массиве случайных целых чисел поменять местами минимальный и максимальный элементы
Автор: Чантурия Д. Г.
'''
import random
N = 6
array = [0] * N

for i in range(N):
    array[i] = random.randint(0, 1000)

min_element = max_element = array[0]
min_element_index = max_element_index = 0
for i, item in enumerate(array):
    if item < min_element:
        min_element = item
        min_element_index = i
    if item > max_element:
        max_element = item
        max_element_index = i

print(array)
print(f'min {min_element}; max {max_element}')
print(f'min index {min_element_index}; max index {max_element_index}')
print('Перемещаем элементы.')

array[min_element_index], array[max_element_index] = array[max_element_index], array[min_element_index]
print(f'Результат: {array}')
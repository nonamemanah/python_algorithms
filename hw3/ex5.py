'''
Задание: В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Автор: Чантурия Д. Г.
'''
N = 5
array = [0] * N

for i in range(N):
    array[i] = int(input('Введите число: '))

min_element = 0
min_element_index = 0
for index, element in enumerate(array):
    if element < min_element and element < 0:
        min_element = element
        min_element_index = index

print(f'Минимальный отрецательный эдемент массива {min_element}. Позиция в массиве: {min_element_index + 1}')

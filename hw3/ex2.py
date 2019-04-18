'''
Задание: Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями
         8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
         т.к. именно в этих позициях первого массива стоят четные числа.
Автор: Чантурия Д. Г.
'''
import random
N = 6
first_array = [0] * N
second_array = []

for i in range(0, N):
    first_array[i] = int(input(f'Введите элемент {i + 1} из {N}: '))

for index, element in enumerate(first_array):
    if element % 2 == 0:
        second_array.append(index)

print(second_array)
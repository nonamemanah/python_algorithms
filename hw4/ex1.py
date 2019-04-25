"""
Задание: Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых
         трех уроков. Для получения результатов взял две реализации задачи:
         "Определить, какое число в массиве встречается чаще всего."
Автор: Чантурия Д. Г.
"""
import cProfile
import timeit

# Моя реализация из ДЗ
def my_elements_count(array):
    result = {}
    for item in array:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1

    return result

# Реализация из прикрепленной реализации
def from_u_elements_count(array):
    frequency = 0
    num = array[0]
    for i in range(len(array)):
        spam = 1
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                spam += 1
        if spam > frequency:
            frequency = spam
            num = array[i]

    return num

def main():
    my_elements_count([1, 1, 2, 3, 2, 2, 2, 2])
    from_u_elements_count([1, 1, 2, 3, 2, 2, 2, 2])


print(my_elements_count([1, 1, 2, 3, 2, 2, 2, 2]))
print(from_u_elements_count([1, 1, 2, 3, 2, 2, 2, 2]))

print(timeit.timeit("my_elements_count", setup="from __main__ import my_elements_count", number=100000))
print(timeit.timeit("from_u_elements_count", setup="from __main__ import from_u_elements_count", number=100000))
cProfile.run('main()')
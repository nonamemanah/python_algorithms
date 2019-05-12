"""
Задание: 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами
на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
!!! Сделал две сортировки. Методом пузырька и методом быстрой сортировки на 20000 элементов.
Автор: Чантурия Д. Г.
Результат:
Сортировка методом пузырька. Время сортировки 30.859375 сек.
Быстрая сортировка. Время сортировки 0.0625 сек.
"""
import random
import time

'''
Метод сортировки пузырьком
'''
def bubble_sort(items):
    result = items.copy()
    items_count = len(result)
    for j in range(items_count - 1):
        for i in range(items_count - j - 1):
            if result[i] > result[i + 1]:
                result[i], result[i + 1] = result[i + 1], result[i]
    return result


def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

'''
Метод быстрой сотрировки
'''
def quick_sort(items, low, high):
    if low < high:
        pi = partition(items, low, high)
        quick_sort(items, low, pi - 1)
        quick_sort(items, pi + 1, high)


def main():
    START_RANGE = -10000
    END_RANGE = 10000
    items = []
    for i in range(START_RANGE, END_RANGE):
        items.append(random.randint(START_RANGE, END_RANGE))
    print(f'Исходный массив: {items}')

    print('-' * 20)
    print('Сортировка методом пузырька.')
    t = time.process_time()
    print(bubble_sort(items))
    elapsed_time = time.process_time() - t
    print(f'Время сортировки {elapsed_time}')

    print('-' * 20)
    print('Бытрая сортировка.')
    t = time.process_time()
    quick_sort(items, 0, len(items) - 1)
    elapsed_time = time.process_time() - t
    print(items)
    print(f'Время сортировки {elapsed_time}')


if __name__ == '__main__':
    main()

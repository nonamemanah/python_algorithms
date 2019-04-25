"""
Задание: Написать два алгоритма нахождения i-го по счёту простого числа.
        Без использования «Решета Эратосфена»;
        Используя алгоритм «Решето Эратосфена»
        Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
        Результаты анализа сохранить в виде комментариев в файле с кодом.
Результат:
    Тестирование проводилось на 10000 элементах в массиве.
    Без использования Решета - 0.0016229
    С использованием - 0.0013625000000000026
    При использовании cProfile, профиллировщик показал, что алгоритм без использования решета
        tottime (время потраченное в данной функции) составляет 2.272 c.
        С испольщованием алгоритма - 0.003, что является отличным показателем
Автор: Чантурия Д. Г.
"""
import cProfile
import timeit

def init_array(array, n):
    for i in range(n):
        array[i] = i


def simple(n):
    a = [0] * n
    b = []
    init_array(a, n)
    for num in a:
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
        if prime:
            b.append(num)
    return b

def sieve(n):
    a = [0] * n
    init_array(a, n)

    a[1] = 0
    m = 2
    while m < n:
        if a[m] != 0:
            j = m * 2
            while j < n:
                a[j] = 0
                j += m
        m += 1

    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])

    del a
    return b

def main():
    simple(10000)
    sieve(10000)

print(timeit.timeit("simple", setup="from __main__ import simple", number=100000))
print(timeit.timeit("sieve", setup="from __main__ import sieve", number=100000))
cProfile.run('main()')
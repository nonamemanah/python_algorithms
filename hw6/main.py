"""
Задание: 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых
трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
!!! Пошел другим путем. Не стал брать алгоритмы, а просто взял приближенный к реалии кейс !!!
Автор: Чантурия Д. Г.
Результат:
------------------------------------------------------------------------------------------------------------------------
Line #    Mem usage    Increment   Line Contents
================================================
     7     24.0 MiB     24.0 MiB   @profile
     8                             def main():
     9     24.0 MiB      0.0 MiB       api = OpenExchangeRatesApi()
    10     26.1 MiB      2.1 MiB       api.load()
    11
    12     26.1 MiB      0.0 MiB       sorted_currency = api.sorted_currency
    13     26.2 MiB      0.0 MiB       for item in sorted_currency:
    14     26.2 MiB      0.0 MiB           print(item)
    15
    16     26.2 MiB      0.0 MiB       print(f'Количество ссылок на объект: {sys.getrefcount(sorted_currency)}')
------------------------------------------------------------------------------------------------------------------------
"""
from memory_profiler import profile
from api.openexchangerates import OpenExchangeRatesApi
import sys


@profile
def main():
    api = OpenExchangeRatesApi()
    api.load()

    sorted_currency = api.sorted_currency
    for item in sorted_currency:
        print(item)

    print(f'Количество ссылок на объект: {sys.getrefcount(sorted_currency)}')


if __name__ == "__main__":
    main()

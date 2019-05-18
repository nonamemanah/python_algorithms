"""
Задание: 1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.
!!! Попробовал и вариант получения hash, как в уроке, так и hash-встроенный метод.
Автор: Чантурия Д. Г.
Результат:
Хэш-buildin работает быстрее. Но это за счет того, что hash предназначен для быстрой проверки на существование
элементов. Мало того результаты этого метода могут отличаться между прогонами.
"""
import hashlib
from collections import namedtuple
import time


def print_combinations(combinations):
    """
    Печатает словоформы
    :param combinations: варианты словоыофрм и их хэши
    :return:
    """
    for item in combinations:
        print(item.string)


def get_hashes(combinations):
    """
    Получение хэшей из словоформ
    :param combinations: варианты словоыофрм и их хэши
    :return:
    """
    hashes = [c.hash_value for c in combinations]
    return hashes


def build_conditions(s):
    """
    Построение свловоформ из строки и их хэшей
    :param s: входная строк
    :return: словоформы и хэши
    """
    combinations = []
    lower_str = s.lower()
    for index, symbol in enumerate(lower_str):
        for i in range(index, len(lower_str)):
            sub_string = lower_str[index:i + 1]
            hash_value = hashlib.sha1(sub_string.encode('utf-8')).hexdigest()
            item = namedtuple('item', 'string, hash_value')
            item.string = sub_string
            item.hash_value = hash_value
            combinations.append(item)

    return combinations


def main():
    t = time.process_time()
    combinations = build_conditions('Hello')
    elapsed_time = time.process_time() - t
    print(f'Время получения вариантов {elapsed_time}')
    hashes = get_hashes(combinations)
    print(len(list(set(hashes))))


if __name__ == '__main__':
    main()

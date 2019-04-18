'''
Задание: Определить, какое число в массиве встречается чаще всего.
Автор: Чантурия Д. Г.
'''
N = 5
array = [0] * N

for i in range(N):
    array[i] = int(input('Введите число: '))

# Объявим dict, в котором ключ - число,  а значение - количество раз
result = {}
for item in array:
    if item in result:
        result[item] += 1
    else:
        result[item] = 1

# проходим по каждому элементу в dict и ищем максимальное хначения
max_i = 0
max_number = 0
for item in result:
    if result.get(item) > max_i:
        max_i = result.get(item)
        max_number = item

print(result)
print(max_number)

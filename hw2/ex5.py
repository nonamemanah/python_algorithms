# Домашнее задание №2
# Упражнение №4
# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
# Автор Чантурия Д. Г.

start_index = 32
end_index = 128
i = 0

while start_index < end_index:
    print(f'{start_index}: {chr(start_index)}', end=' ')
    start_index += 1
    i += 1
    if i % 10 == 0:
        print()
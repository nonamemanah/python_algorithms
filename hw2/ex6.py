# Домашнее задание №2
# Упражнение №4
# В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число,
# чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.
# Автор Чантурия Д. Г.
import random


def compare_answer(answer, secret_number):
    return answer == secret_number


secret_number = random.randint(0, 100)
wrong_answer_count = 0
while wrong_answer_count < 11:
    print('Отгадайте число.')
    answer = int(input('Введите число: '))
    if compare_answer(answer, secret_number):
        print('Вы выиграли!!!')
        break

    wrong_answer_count += 1
    print(f'Количество оставшихся попыток: {10 - wrong_answer_count}.')
    if secret_number > answer:
        print('Ваш ответ меньше загадываемого числа')
    else:
        print('Ваш ответ больше загадываемого числа')
    break

print(f'Загаданное число: {secret_number}')

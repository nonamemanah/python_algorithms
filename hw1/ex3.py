# Домашнее задание №1
# Упражнение №3
# По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b,
# проходящей через эти точки.
# Автор Чантурия Д. Г.
print('Введите координаты точки А.')
x1 = int(input('x1 = '))
y1 = int(input('x2 = '))

print('Введите координаты точки B.')
x2 = int(input('x2 = '))
y2 = int(input('y2 = '))

if x1 == x2:
    print(f'x = {x1:.2f}')
else:
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    print(f'y = {k:.2f} * x - {b:.2f}')
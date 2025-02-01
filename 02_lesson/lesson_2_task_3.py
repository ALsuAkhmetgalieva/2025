from math import ceil


def ceil_square(a, b):
    return ceil(a*b)


a = float(input('Введите первую сторону: '))
b = float(input('Введите вторую сторону: '))


print(f'Площадь квадрата округленная в большую сторону - {ceil_square(a, b)}')



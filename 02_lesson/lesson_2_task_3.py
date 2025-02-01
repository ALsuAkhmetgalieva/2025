from math import ceil


def ceil_square(a, b):
    return ceil(a*b)


a = float(input('Введите первое слагаемое: '))
b = float(input('Введите второе слагаемое: '))


print(f'Округленное в большую сторону произведение - {ceil_square(a, b)}')



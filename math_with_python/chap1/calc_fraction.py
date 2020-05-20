"""
calc_fraction.py

Fraction operations
"""

from fractions import Fraction


def add(a, b):
    print(f'{a} + {b} = {a + b}')


def sub(a, b):
    print(f'{a} - {b} = {a - b}')


def multi(a, b):
    print(f'{a} * {b} = {a * b}')


def div(a, b):
    print(f'{a} / {b} = {a / b}')


if __name__ == '__main__':
    try:
        a = Fraction(input('Enter first fraction: '))
        b = Fraction(input('Enter second fraction: '))
        op = input('Operation to perform (1)Add, (2)Sub, (3)Multi, (4)Div: ')
        if op == '1':
            add(a, b)
        if op == '2':
            sub(a, b)
        if op == '3':
            sub(a, b)
        if op == '4':
            div(a, b)
    except ValueError:
        print('ValueError please input correctly')

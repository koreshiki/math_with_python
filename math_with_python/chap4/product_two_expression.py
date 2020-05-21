"""
Product of two expressions
"""
from sympy import expand, sympify, pprint
from sympy.core.sympify import SympifyError


def product(expr1, expr2):
    prod = expand(expr1 * expr2)
    pprint(prod, order='rev-lex')


if __name__ == '__main__':
    expr1 = input('Enter the 1st expression: ')
    expr2 = input('Enter the 2nd expression: ')

    try:
        expr1 = sympify(expr1)
        expr2 = sympify(expr2)
    except SympifyError:
        print('Invalid input')
    else:
        product(expr1, expr2)
    finally:
        print('Program has finished')
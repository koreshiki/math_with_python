"""
Find the factor of an expression that user input
"""

from sympy import Symbol, factor, sympify
from sympy.core.sympify import SympifyError


def find_factor(expr):
    print(factor(expr))

if __name__ == '__main__':
    expr = input('Enter your expression in terms of x: ')
    try:
        expr = sympify(expr)
    except SympifyError:
        print('Invalid input')
    else:
        find_factor(expr)
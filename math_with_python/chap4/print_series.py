"""
Print the series
    x^2   x^3          x^n
x + ---- + ---- + ... + ----
     2      3            n

and calculate its value at a certain value of x
"""
from sympy import Symbol, pprint


def print_series(n):
    # initialize printing system with reverse order
    x = Symbol('x')
    series = x
    for i in range(2, n+1):
        series = series + (x ** i) / i
    pprint(series, order='rev-lex')


if __name__ == '__main__':
    n = input('Enter the number of terms you want in the series: ')
    print_series(int(n))
"""
Print the series
    x^2   x^3          x^n
x + ---- + ---- + ... + ----
     2      3            n

and calculate its value at a certain value of x
"""
from sympy import Symbol, pprint, init_printing


def print_series(n, x_value):
    # initialize printing system with reverse order
    x = Symbol('x')
    series = x
    for i in range(2, n+1):
        series = series + (x ** i) / i
    pprint(series, order='rev-lex')

    series_value = series.subs({x: x_value})
    print(f'Value of the series at {x_value}: {series_value}')


if __name__ == '__main__':
    n = input('Enter the number of terms you want in the series: ')
    x_value = input('Enter the value of x at which you want to evaluat the series: ')
    print_series(int(n), float(x_value))
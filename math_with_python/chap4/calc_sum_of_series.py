from sympy import Symbol, sympify, summation
from sympy.core.sympify import SympifyError

def calc_sum_of(expr, k):
    n = Symbol('n')
    sum = summation(expr, (n, 1, k))
    print(sum)


if __name__ == '__main__':
    expr = input('Enter the nth term: ')
    k = input('Enter the number of terms: ')
    try:
        expr = sympify(expr)
        k = int(k)
    except SympifyError:
        print('Invalid term')
    except ValueError:
        print('Invalid number')
    else:
        calc_sum_of(expr, k)
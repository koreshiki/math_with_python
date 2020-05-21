from sympy import Symbol, solve, sympify
from sympy.core.sympify import SympifyError
from sympy.plotting import plot


def draw_two_graph(expr1, expr2):
    y = Symbol('y')
    print(expr1)
    print(expr2)

    solutions1 = solve(expr1, y)
    solutions2 = solve(expr2, y)
    expr_y1 = solutions1[0]
    expr_y2 = solutions2[0]

    p = plot(expr_y1, expr_y2, legend=True, show=False)
    p[0].line_color = 'b'
    p[1].line_color = 'r'
    print(f'answer = {solve((expr1, expr2), dict=True)}')
    p.show()



if __name__ == '__main__':
    expr1 = input('Enter your 1st expression in terms of x and y: ')
    expr2 = input('Enter your 2st expression in terms of x and y: ')
    try:
        expr1 = sympify(expr1)
        expr2 = sympify(expr2)
    except SympifyError:
        print('Invalid input')
    else:
        draw_two_graph(expr1, expr2)

"""
Extended generate a multi_table
"""


def multi_table(a, b):
    for i in range(1, b + 1):
        print(f'{a} x {i} = {a * i}')


if __name__ == '__main__':
    a = input('Enter a number: ')
    b = input('Enter a range number(integer): ')
    multi_table(float(a), int(b))
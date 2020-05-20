import sys


def judge_number(number):
    return number % 2


if __name__ == '__main__':
    num = input('Enter a integer: ')
    judge = 0
    if not num.isdigit():
        print('Oops! Error occurred.\n'
              'Input a integer please.')
        sys.exit(1)

    if judge_number(int(num)):
        '''
        Odd number
        '''
        print('odd number')
    else:
        '''
        Even number
        '''
        print('even number')
    n = int(num)
    max_step = 9
    for i in range(n + 2, n + 2 * max_step, 2):
        print(f'{i}', end=', ')
    print(n + 2 * max_step + 2)




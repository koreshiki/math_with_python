import matplotlib.pyplot as plt
import numpy as np

def fibo(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1]
    a = 1
    b = 1
    series = [a, b]
    differs = [1]
    for i in range(n - 2):
        differs.append(b / a)
        c = a + b
        series.append(c)
        a = b
        b = c
    return differs


def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('No.')
    plt.ylabel('Ratio')
    plt.title('Ratio between consecutive Fibonacci numbers')
    plt.show()


if __name__ == '__main__':
    #num = int(input('Enter n(0 < n <= 100): '))
    n = 101
    x_list = np.arange(1, n, 1)
    y_list = fibo(n)
    draw_graph(x_list, y_list)
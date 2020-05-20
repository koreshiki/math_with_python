import numpy as np
import matplotlib.pyplot as plt

def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')


if __name__ == '__main__':
    x_values = np.arange(-10, 10, 0.01)
    y_values = []
    for x in x_values:
        y_values.append(x ** 2 + 2 * x + 1)

    draw_graph(x_values, y_values)
    plt.show()
import numpy as np
import matplotlib.pyplot as plt
import math

"""
Draw the trajectory of a body in projectile motion
"""
def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('Projectile motion of a ball')


def draw_trajectory(u, theta):
    theta = math.radians(theta)
    g = 9.8
    t_flight = 2 * u * math.sin(theta) / g
    intervals = np.arange(0, t_flight, 0.001)
    x = []  # distance
    y = []  # height
    for t in intervals:
        x.append(u * math.cos(theta) * t)
        y.append(u * math.sin(theta) * t - 0.5 * g * t ** 2)
    draw_graph(x, y)


if __name__ == '__main__':
    # try:
        # u = float(input('Enter the initial velocity (m/s):'))
    u_list = [20, 40, 60]
    theta = 45 # float(input('Enter the angle of projection (degrees): '))
    for u in u_list:
        draw_trajectory(u, theta)
    plt.legend(['20', '40', '60'])
    plt.show()
"""    except ValueError:
        print('You entered an invalid input')
    else:
        draw_trajectory(u, theta)
        plt.show()
"""

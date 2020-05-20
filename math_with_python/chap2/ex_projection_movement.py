import numpy as np
import matplotlib.pyplot as plt
import math
import sys


def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('x-distance (m)')
    plt.ylabel('y-height (m)')
    plt.title('Projectile motion of a ball')


def draw_trajectory(u, in_theta, results):
    theta = math.radians(in_theta)
    g = 9.8
    t_flight = 2 * u * math.sin(theta) / g
    intervals = np.arange(0, t_flight, 0.001)
    x = []  # distance
    y = []  # height
    for t in intervals:
        x.append(u * math.cos(theta) * t)
        y.append(u * math.sin(theta) * t - 0.5 * g * t ** 2)
    results.append({'init-v': u, 'degree': in_theta, 'flight-time': round(t_flight, 3), 'max-x': round(x[-1], 3), 'max-y': round(np.amax(y), 3)})
    draw_graph(x, y)


def print_results(results):
    legend_list = list()
    for result in results:
        legend_list.append((result['init-v'], result['degree']))
        print(f"(v_0 = {result['init-v']}, theta = {result['degree']}) = (flight-time:{result['flight-time']} (sec) max-x:{result['max-x']} (m) max-y:{result['max-y']} (m) )")
    plt.legend(legend_list)


if __name__ == '__main__':
    in_repeat = input('How many trajectories? ')

    if not in_repeat.isdigit():
        print('Error! please enter a natural number (ex 3)')
        sys.exit(1)

    results = []
    current = 0
    repeat = int(in_repeat)

    while True:
        if current >= repeat:
            break
        try:
            u = float(input(f'Enter the initial velocity {current + 1} (m/s): '))
            theta = float(input(f'Enter the angle of projection {current + 1} (degrees): '))
        except ValueError:
            print('You entered an invalid input')
        else:
            draw_trajectory(u, theta, results)
            current += 1

    print_results(results)
    plt.show()

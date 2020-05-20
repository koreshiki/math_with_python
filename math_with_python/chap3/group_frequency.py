import math


def create_classes(numbers, n):
    low = min(numbers)
    high = max(numbers)

    width = (high - low) / n
    classes = []
    a = low
    b = low + width
    while a < (high - width):
        classes.append((a, b))
        a = b
        b = a + width
    classes.append((a, high + 1))
    return classes


def calc_group_frequency(numbers, classes):
    num_groups = len(classes)
    N = len(numbers)
    numbers.sort()
    print(numbers)
    frequency = []
    idx = 0
    for i in range(num_groups):
        count = 0
        while True:
            if idx < N and numbers[idx] > classes[i][1] or idx == N:
                break
            idx += 1
            count += 1
        frequency.append(count)

    return frequency


if __name__ == '__main__':
    numbers = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
    classes = create_classes(numbers, 4)
    print(classes)
    freq = calc_group_frequency(numbers, classes)

    for i in range(len(freq)):
        print(f'{math.ceil(classes[i][0])}\t-\t{math.ceil(classes[i][1])}\t:\t{freq[i]}')
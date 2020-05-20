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
    numbers.sort()
    frequency = []
    for num in numbers:
        for c in classes:
            if num < c[1]:
                print('a')


if __name__ == '__main__':
    numbers = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
    classes = create_classes(numbers, 2)
    calc_group_frequency(numbers, classes)
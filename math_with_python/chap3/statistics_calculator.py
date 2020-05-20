from collections import Counter


def read_data(filename):
    numbers = []
    with open(filename) as f:
        for line in f:
            numbers.append(float(line))
    return numbers


def calculate_mean(numbers):
    return sum(numbers) / len(numbers)


def calculate_median(numbers):
    N = len(numbers)
    numbers.sort()

    if N % 2 == 0:
        m1 = N/2
        m2 = N/2 + 1
        m1 = int(m1) - 1
        m2 = int(m2) - 1
        return (numbers[m1] + numbers[m2]) / 2
    else:
        m = (N+1) / 2
        m = int(m) - 1
        return numbers[m]


def calculate_mode(numbers):
    c = Counter(numbers)
    numbers_freq = c.most_common()
    max_count = numbers_freq[0][1]

    modes = []
    for num in numbers_freq:
        if num[1] == max_count:
            modes.append(num[0])
    return modes


def find_differences(numbers):
    mean = calculate_mean(numbers)
    diff = []

    for num in numbers:
        diff.append(num - mean)
    return diff


def calculate_variance(numbers):
    diff = find_differences(numbers)
    squared_diff = []
    for d in diff:
        squared_diff.append(d**2)
    # find the variance
    sum_squared_diff = sum(squared_diff)
    variance = sum_squared_diff / len(numbers)
    return variance


def calculate_stddev(numbers):
    return calculate_variance(numbers) ** 0.5


if __name__ == '__main__':
    data = read_data('mydata.txt')
    mean = calculate_mean(data)
    median = calculate_median(data)
    mode = calculate_mode(data)
    variance = calculate_variance(data)
    std_dev = calculate_stddev(data)

    print(f'mean\t{mean}')
    print(f'median\t{median}')
    print(f'mode\t{mode}')
    print(f'variance\t{variance}')
    print(f'std_dev\t{std_dev}')

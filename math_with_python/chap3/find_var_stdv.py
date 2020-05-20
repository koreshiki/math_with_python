"""
Find the variance and standard  deviation of a list of numbers
"""


def calculate_mean(numbers):
    return sum(numbers) / len(numbers)


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


if __name__ == '__main__':
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    variance = calculate_variance(donations)
    print(f'The variance of the list of numbers is {variance}')

    std = variance ** 0.5
    print(f'The standard deviation of the list of number is {std}')
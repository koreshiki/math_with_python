"""
Calculation the mean
"""

def calculate_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    return s / N


if __name__ == '__main__':
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    mean = calculate_mean(donations)
    N = len(donations)
    print(f'Mean donation over the last {N} days is {mean}')
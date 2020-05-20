def read_data(filename):
    numbers = []
    with open(filename) as f:
        for line in f:
            numbers.append(float(line))
    return numbers


def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    data = read_data('mydata.txt')
    mean = calculate_mean(data)
    print(f'Mean: {mean}')
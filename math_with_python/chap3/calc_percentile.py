def read_data(filename):
    numbers = []
    with open(filename) as f:
        for line in f:
            numbers.append(int(line))
    return numbers


def calculate_percentile(data, p):
    data.sort()
    N = len(data)
    i = N * p / 100 + 0.5
    if i.is_integer():
        return data[int(i - 1)]
    else:
        #Integer part
        k = int(i)
        # Fraction part
        f = i - k
        print(f'k = {k}, f={f}')
        return (1-f) * data[k - 1] + f * data[k]


if __name__ == '__main__':
    data = read_data('score.txt')
    percentile = calculate_percentile(data, 50)
    print(f'Percentile of the data is {percentile}')


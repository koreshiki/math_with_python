import sys
import matplotlib.pyplot as plt


def draw_graph(data, labels):
    num_bars = len(data)
    positions = range(1, num_bars + 1)
    plt.barh(positions, data, align='center')
    plt.yticks(positions, labels)
    plt.xlabel('Amount')
    plt.ylabel('Category')
    plt.title('Weekly expenditures')
    plt.grid()
    plt.show()


def draw_expenditure(categories, expenditures):
    draw_graph(expenditures, categories)


if __name__ == '__main__':
    in_category_num = input('Enter the number of categories: ')
    if not in_category_num.isdigit():
        print('Please input a digit')
        sys.exit(1)

    repeat = 0
    category_num = int(in_category_num)
    categories = list()
    expenditures = list()

    while repeat < category_num:
        try:
            category = input('Enter category: ')
            expenditure = int(input('Expenditure: '))
        except ValueError:
            print('You entered an invalid input')
        else:
            categories.append(category)
            expenditures.append(expenditure)
            repeat += 1

    draw_expenditure(categories, expenditures)

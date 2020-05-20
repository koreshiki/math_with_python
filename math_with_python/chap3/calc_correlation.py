"""
A correlation coefficient is given follow formula

         nΣxy - ΣxΣy
------------------------------------
√{(nΣx^2 - (Σx)^2)(nΣy^2 - (Σy)^2)}

where
    n : a number of element of the set
    Σxy = (x1 * y1) + (x2 * y2) + ... + (xn * yn)
    Σx : sum of set x
    Σy : sum of set y
    (Σx)^2 = (x1 + x2 + ... + xn)^2
    (Σy)^2 = (y1 + y2 + ... + yn)^2
    Σx^2 = x1^2 + x2^2 + ... + xn^2
    Σy^2 = xy^2 + xy^2 + ... + yn^2
"""


def find_corr_x_y(x, y):
    # number of element of set
    n = len(x)

    # calc sigma(xy)
    prod = []
    for xi, yi in zip(x, y):
        prod.append(xi * yi)
    sum_prod_x_y = sum(prod)

    # calc sigma(x) and sigma(y)
    sum_x = sum(x)
    sum_y = sum(y)
    squared_sum_x = sum_x ** 2
    squared_sum_y = sum_y ** 2

    # calc sigma(x^2)
    x_square = []
    for xi in x:
        x_square.append(xi ** 2)
    x_square_sum = sum(x_square)

    # calc simga(y^2)
    y_square = []
    for yi in y:
        y_square.append(yi ** 2)
    y_square_sum = sum(y_square)

    # calc n * sigma(xy) - sum(x) * sum(y)
    numerator = n * sum_prod_x_y - sum_x * sum_y
    # calc n * sigma(x^2) - (sigma(x))^2
    denominator_term1 = n * x_square_sum - squared_sum_x
    # calc n * sigma(y^2) - (sigma(y))^2
    denominator_term2 = n * y_square_sum - squared_sum_y
    denominator = (denominator_term1 * denominator_term2) ** 0.5
    correlation = numerator / denominator

    return correlation



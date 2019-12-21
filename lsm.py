"""
Example:
    x: 1 2 3 4 5
    y: 5.3 6.3 4.8 3.8 3.3
    Result: a = -0.65, b = 6.65
"""

import matplotlib.pyplot as plt
import numpy as np


def get_valid_tuple(text_input):
    while True:
        a_str = input(text_input)
        try:
            a_tuple = tuple(float(a) for a in a_str.split(' '))
        except ValueError as err:
            print('Ошибка: невозможно преобразовать в вещественное число.')
            print(err)
        else:
            if len(a_tuple) > 1:
                return a_tuple
            else:
                print('Ошибка: введите список больше 1 элемента.')


def get_coordinates():
    x_crds = get_valid_tuple('Введите точки по оси абцисс: ')
    y_crds = get_valid_tuple('Введите точки по оси ординат: ')
    if len(x_crds) != len(y_crds):
        print('Предупреждение: разная длина списков.')
        len_min = min(len(x_crds), len(y_crds))
        return x_crds[:len_min], y_crds[:len_min]
    else:
        return x_crds, y_crds


def get_deg_poly():
    while True:
        deg = input('Введите степень полиноминальной функции: ')
        if deg.isdigit() and int(deg) >= 0:
            return int(deg)
        else:
            print('Ошибка: степень не целое число или меньше 0.')


def plotting():
    x_crds = (1, 2, 3, 4, 5)
    y_crds = (5.3, 6.3, 4.8, 3.8, 3.3)
    # x_crds = [10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74, 78, 82, 86]
    # y_crds = [0.1, 0.0714, 0.0556, 0.0455, 0.0385, 0.0333, 0.0294, 0.0263, 0.0238, 0.0217,
    #      0.02, 0.0185, 0.0172, 0.0161, 0.0152, 0.0143, 0.0135, 0.0128, 0.0122,
    #      0.0116]
    # x_crds, y_crds = get_coordinates()
    plt.scatter(x_crds, y_crds)
    plt.show()

    deg = get_deg_poly()
    lsm_func = np.polyfit(x_crds, y_crds, deg)
    print(lsm_func)
    lsm_y_crds = np.polyval(lsm_func, x_crds)

    plt.scatter(x_crds, y_crds)
    plt.plot(x_crds, lsm_y_crds)
    plt.show()


if __name__ == '__main__':
    plotting()

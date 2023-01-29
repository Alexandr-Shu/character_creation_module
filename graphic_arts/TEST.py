import math

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return math.sqrt(number)


def calc(your_number):
    """Вычисляет квадратный корень при 0 или отрицательном значении."""
    root = calculate_square_root(your_number)
    if your_number <= 0:
        return 'root = 0'
    return print(
              f'Мы вычислили квадратный корень из введённого вами числа. '
              f'Это будет: {root}'
             )


print(message)
calc(25.5)

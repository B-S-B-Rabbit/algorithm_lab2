from modules.base_classes import *
import random
from sympy import isprime


def get_rectangles(n):
    return [Rectangle(10 * i, 10 * i, 10 * (2 * n - i), 10 * (2 * n - i)) for i in range(n)]


def hash_func(p, i, n):
    return (p * i) ** 31 % (20 * n)


def generate_prime(low, high):
    while True:
        p = random.randrange(low, high)
        if isprime(p):
            return p


p_low = 10 ** 6
p_high = 10 ** 7


def get_points(n):
    p_x = generate_prime(p_low, p_high)
    p_y = generate_prime(p_low, p_high)
    points = []
    for i in range(n):
        x = hash_func(p_x, i, n)
        y = hash_func(p_y, i, n)
        point = Point2D(x, y)
        points.append(point)
    return points


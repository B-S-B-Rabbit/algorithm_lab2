from bisect import bisect_left
from modules.general_funcs import *


def fill_matrix(x_values, y_values, rectangles):
    matrix = [[0 for _ in range(len(x_values))] for _ in range(len(y_values))]
    for rect in rectangles:
        i1 = bisect_left(x_values, rect.x1)
        j1 = bisect_left(y_values, rect.y1)
        i2 = bisect_left(x_values, rect.x2)
        j2 = bisect_left(y_values, rect.y2)
        for i in range(i1, i2 + 1):
            for j in range(j1, j2 + 1):
                matrix[j][i] += 1
    return matrix


def get_count(points, x_values, y_values, matrix):
    counts = []
    for point in points:
        if point.x < x_values[0] or point.y < y_values[0]:
            counts.append(0)
            continue
        x_index = find_le(x_values, point.x)
        y_index = find_le(y_values, point.y)
        count = matrix[y_index][x_index] if 0 <= x_index < len(x_values) and 0 <= y_index < len(y_values) else 0
        counts.append(count)
    return counts

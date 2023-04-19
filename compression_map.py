from bisect import bisect_left, bisect_right, bisect
from pprint import pprint


def find_le(a, x):
    'Находит крайнее правое значение меньше или равно x'
    i = bisect_right(a, x)
    if i:
        return i-1

class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


def main():
    n = int(input())
    rectangles = [Rectangle(*(map(int, input().split()))) for _ in range(n)]
    x_values = set()
    y_values = set()
    for rect in rectangles:
        x_values.add(rect.x1)
        x_values.add(rect.x2)
        y_values.add(rect.y1)
        y_values.add(rect.y2)
        x_values.add(rect.x2 + 1)
        y_values.add(rect.y2 + 1)

    x_values = sorted(x_values)
    y_values = sorted(y_values)
    matrix = [[0 for _ in range(len(x_values))] for _ in range(len(y_values))]
    for rect in rectangles:
        i1 = bisect_left(x_values, rect.x1)
        j1 = bisect_left(y_values, rect.y1)
        i2 = bisect_left(x_values, rect.x2)
        j2 = bisect_left(y_values, rect.y2)
        for i in range(i1, i2 + 1):
            for j in range(j1, j2 + 1):
                matrix[j][i] += 1
    m = int(input())
    for i in range(m):
        point = Point2D(*map(int, input().split()))
        if point.x < x_values[0] or point.y < y_values[0]:
            print(0)
            continue
        x_index = find_le(x_values, point.x)
        y_index = find_le(y_values, point.y)
        count = matrix[y_index][x_index] if 0 <= x_index < len(x_values) and 0 <= y_index < len(y_values) else 0
        print(count, end=' ')

if __name__ == "__main__":
    main()

from bisect import bisect_left
from pprint import pprint


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

    def have(self, point):
        if self.x1 <= point.x <= self.x2 and self.y1 <= point.y <= self.y2:
            return True
        return False


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

    x_values = sorted(x_values)
    y_values = sorted(y_values)
    matrix = [[0 for _ in range(len(x_values))] for _ in range(len(y_values))]

    # Заполняем матрицу значениями для каждого прямоугольника
    for rect in rectangles:
        i1 = x_values.index(rect.x1)
        j1 = y_values.index(rect.y1)
        i2 = x_values.index(rect.x2)
        j2 = y_values.index(rect.y2)
        for i in range(i1, i2 + 1):
            for j in range(j1, j2 + 1):
                matrix[j][i] += 1
        pprint(matrix)
    m = int(input())
    for i in range(m):
        point = Point2D(*map(int, input().split()))
        x_index = bisect_left(x_values, point.x)
        y_index = bisect_left(y_values, point.y)

        print(matrix[y_index][x_index] if x_index < len(x_values) and y_index < len(y_values) else 0,end=' ')


if __name__ == "__main__":
    main()

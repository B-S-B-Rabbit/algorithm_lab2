from modules.base_classes import *
import modules.comp_map as cmp


def main():
    n = int(input())
    rectangles = [Rectangle(*(map(int, input().split()))) for _ in range(n)]

    m = int(input())
    points = [Point2D(*map(int, input().split())) for _ in range(m)]

    x_values, y_values = cmp.fill_zipped_coord(rectangles)

    matrix = cmp.fill_matrix(x_values, y_values, rectangles)

    counts = cmp.get_count(points, x_values, y_values, matrix)
    return counts


if __name__ == "__main__":
    print(*main())

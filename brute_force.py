from modules.base_classes import *


def main():
    n = int(input())
    rectangles = [Rectangle(*(map(int, input().split()))) for _ in range(n)]

    m = int(input())
    points = [Point2D(*map(int, input().split())) for _ in range(m)]

    count = 0
    counts = []
    for point in points:
        for rect in rectangles:
            if rect.have(point):
                count += 1
        counts.append(count)
        count = 0
    return counts


if __name__ == "__main__":
    print(*main())

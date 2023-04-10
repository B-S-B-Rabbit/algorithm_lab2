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


def bf():
    n = int(input())
    rect_array = []
    for i in range(n):
        rect_array.append(Rectangle(*(map(int, input().split()))))
    count = 0
    m = int(input())
    for i in range(m):
        point = Point2D(*map(int, input().split()))
        for j in rect_array:
            if j.have(point):
                count += 1
        print(count, end=' ')
        count = 0


if __name__ == "__main__":
    bf()

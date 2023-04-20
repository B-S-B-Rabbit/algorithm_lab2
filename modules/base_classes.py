class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x}, {self.y})'


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

    def __repr__(self):
        return f'({self.x1}, {self.y1}) ({self.x2}, {self.y2})'

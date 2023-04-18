from bisect import bisect_left, bisect_right

class SegmentTree:



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


def compress_values(values):
    values = list(set(values))
    values.sort()
    compressed = {v: i for i, v in enumerate(values)}
    return compressed


def main():
   pass

if __name__ == "__main__":
    main()
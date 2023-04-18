import copy
from bisect import bisect_left, bisect_right


def find_le(a, x):
    'Находит крайнее правое значение меньше или равно x'
    i = bisect_right(a, x)
    if i:
        return i - 1


class SegmentTree:
    def __init__(self, array=None):
        if array is None:
            array = []
        self.array = array
        self.roots = {}

    class Node:
        def __init__(self, start, end):
            self.start = start  # начало интервала
            self.end = end  # конец интервала
            self.list_val = 0  # сумма элементов на данном интервале
            self.modifier = 0
            self.left_child = None  # левый потомок
            self.right_child = None  # правый потомок

    def build(self, start, end):
        if start == end:
            return self.Node(start, end)

        mid = (start + end) // 2
        left_child = self.build(start, mid)
        right_child = self.build(mid + 1, end)

        node = self.Node(start, end)
        node.left_child = left_child
        node.right_child = right_child
        return node

    def update(self, root, start, end, value):
        if start > root.end or end < root.start:  # если наш диапазон не пересекается с текущим узлом
            return root

        if start <= root.start and end >= root.end:  # обновление всего диапазона
            new_root = self.Node(root.start, root.end)
            new_root.left_child = root.left_child
            new_root.right_child = root.right_child
            if new_root.left_child or new_root.right_child:
                new_root.modifier = root.modifier + value
            else:
                new_root.list_val = root.list_val + value
            return new_root

        new_root = self.Node(root.start, root.end)
        new_root.modifier = root.modifier
        new_root.left_child = self.update(root.left_child, start, end, value)
        new_root.right_child = self.update(root.right_child, start, end, value)
        if new_root.left_child or new_root.right_child:
            new_root.modifier = root.modifier + value
        else:
            new_root.list_val = root.list_val + value
        return new_root

    def print_tree(self, root, level=0):
        if root is not None:
            self.print_tree(root.right_child, level + 1)
            print(' ' * 6 * level + '->', [root.list_val, root.modifier])
            self.print_tree(root.left_child, level + 1)


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


class Event:
    def __init__(self, compX=0, compY1=0, compY2=0, status_open=False):
        self.compX = compX
        self.compY1 = compX
        self.compY2 = compX
        self.status_open = status_open

    def __repr__(self):
        return f'{self.compX}'

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
    print(x_values)
    events = []
    for i in rectangles:
        events.append(Event(find_le(x_values, i.x1), find_le(y_values, i.y1), i.y2 + 1, True))
        events.append(Event(find_le(x_values, i.x2 + 1), find_le(y_values, i.y1), i.y2 + 1, False))
    events = sorted(events, key=lambda x: x.compX)
    print(events)
    stree = SegmentTree(y_values)
    stree.roots[-1] = stree.build(0, 15)
    prev_event = -1
    for event in events:
        stree.roots[event.compX] = stree.update(stree.roots[prev_event],event.compY1, event.compY2, 1 if event.status_open else 0)
        prev_event = event.compX
    stree.print_tree(stree.roots[events[-1].compX])
if __name__ == "__main__":
    main()

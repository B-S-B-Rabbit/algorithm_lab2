from bisect import bisect_right


def find_le(a, x):
    'Находит крайнее правое значение меньше или равно x'
    i = bisect_right(a, x)
    if i:
        return i - 1


def find_vale(a, x):
    'Находит крайнее правое значение меньше или равно x'
    i = bisect_right(a, x)
    if i:
        return a[i - 1]


def findNextPowerOf2(n):
    k = 1
    while k < n:
        k = k << 1

    return k


def count_rect(root, y_ind):
    count = 0
    while root:
        count += root.list_val + root.modifier
        if root.left_child and root.left_child.start <= y_ind <= root.left_child.end:
            root = root.left_child
        elif root.right_child and root.right_child.start <= y_ind <= root.right_child.end:
            root = root.right_child
        else:
            return count
    return count


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
        return new_root


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


class Event:
    def __init__(self, compX=0, compY1=0, compY2=0, status_open=False):
        self.compX = compX
        self.compY1 = compY1
        self.compY2 = compY2
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
    events = []
    for i in rectangles:
        events.append(
            Event(find_le(x_values, i.x1), find_le(y_values, i.y1), find_le(y_values, i.y2), True))
        events.append(
            Event(find_le(x_values, i.x2 + 1), find_le(y_values, i.y1), find_le(y_values, i.y2), False))

    events = sorted(events, key=lambda x: x.compX)
    stree = SegmentTree(y_values)

    stree.roots[-1] = stree.build(0, findNextPowerOf2(len(y_values)) - 1)
    prev_event = -1
    for event in events:
        stree.roots[event.compX] = stree.update(stree.roots[prev_event], event.compY1, event.compY2,
                                                1 if event.status_open else -1)
        prev_event = event.compX

    m = int(input())
    for i in range(m):
        point = Point2D(*map(int, input().split()))
        if point.x < x_values[0] or point.y < y_values[0]:
            print(0)
            continue
        x_index = find_le(x_values, point.x)
        y_index = find_le(y_values, point.y)
        count = count_rect(stree.roots[find_vale(list(stree.roots.keys()), x_index)], y_index)
        print(count, end=' ')


if __name__ == "__main__":
    main()
# 10
# 0 0 2 2
# 0 0 1 1
# 0 0 3 3
# 0 4 2 12
# 0 8 9 10
# 2 2 6 8
# 4 0 11 6
# 5 4 9 10
# 8 2 12 12
# 5 2 9 6
# 20
# 0 0

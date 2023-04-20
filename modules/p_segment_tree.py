from modules.general_funcs import *


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


class Event:
    def __init__(self, compX=0, compY1=0, compY2=0, status_open=False):
        self.compX = compX
        self.compY1 = compY1
        self.compY2 = compY2
        self.status_open = status_open

    def __repr__(self):
        return f'{self.compX}'


def fill_events(rectangles, x_values, y_values):
    events = []
    for rect in rectangles:
        events.append(
            Event(find_le(x_values, rect.x1), find_le(y_values, rect.y1), find_le(y_values, rect.y2), True))
        events.append(
            Event(find_le(x_values, rect.x2 + 1), find_le(y_values, rect.y1), find_le(y_values, rect.y2), False))
    events = sorted(events, key=lambda x: x.compX)
    return events


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


def get_count(points, x_values, y_values, stree):
    counts = []
    for point in points:
        if point.x < x_values[0] or point.y < y_values[0]:
            counts.append(0)
            continue
        x_index = find_le(x_values, point.x)
        y_index = find_le(y_values, point.y)
        count = count_rect(stree.roots[find_vale(list(stree.roots.keys()), x_index)], y_index)
        counts.append(count)
    return counts

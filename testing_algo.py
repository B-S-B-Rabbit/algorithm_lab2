from modules.base_classes import *
import modules.p_segment_tree as pst
import modules.comp_map as cmp


def seg_tree():
    n = int(input())
    rectangles = [Rectangle(*(map(int, input().split()))) for _ in range(n)]

    m = int(input())
    points = [Point2D(*map(int, input().split())) for _ in range(m)]

    x_values, y_values = pst.fill_zipped_coord(rectangles)
    events = pst.fill_events(rectangles, x_values, y_values)

    stree = pst.SegmentTree(y_values)
    stree.roots[-1] = stree.build(0, pst.find_next_power_of2(len(y_values)) - 1)
    prev_event = -1

    for event in events:
        stree.roots[event.compX] = stree.update(stree.roots[prev_event], event.compY1, event.compY2,
                                                1 if event.status_open else -1)
        prev_event = event.compX

    counts = pst.get_count(points, x_values, y_values, stree)
    return counts


def cmp_map():
    n = int(input())
    rectangles = [Rectangle(*(map(int, input().split()))) for _ in range(n)]

    m = int(input())
    points = [Point2D(*map(int, input().split())) for _ in range(m)]

    x_values, y_values = cmp.fill_zipped_coord(rectangles)

    matrix = cmp.fill_matrix(x_values, y_values, rectangles)

    counts = cmp.get_count(points, x_values, y_values, matrix)
    return counts


def bf():
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
    pass

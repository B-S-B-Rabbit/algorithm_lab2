from modules.base_classes import *
import modules.p_segment_tree as pst


def main():
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


if __name__ == "__main__":
    print(*main())
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
# 60
# 0 0
# 0 1
# 0 2
# 0 4
# 0 3
# 0 7
# 0 10
# 1 1
# 1 5
# 1 3
# 2 2
# 2 3
# 3 3
# 3 4
# 3 5
# 3 6
# 3 7
# 3 8
# 3 9
# 3 12
# 4 2
# 4 4
# 4 8
# 4 6
# 4 20
# 20 20
# 5 12
# 5 2
# 5 4
# 5 5
# 6 7
# 6 2
# 6 4
# 5 9
# 6 14
# 7 2
# 7 90
# 7 0
# 7 5
# 8 2
# 8 5
# 8 7
# 9 2
# 9 6
# 9 10
# 9 12
# 10 1
# 10 0
# 10 10
# 10 5
# 10 4
# 11 2
# 11 0
# 12 6
# 14 0
# 12 12
# 12 0
# 13 2
# 16 7
# 11 12
# 3 3 2 1 1 1 2 3 1 1 3 2 2 1 1 1 1 2 1 0 2 2 2 2 0 0 0 3 4 4 2 3 4 2 0 2 0 1 3 3 4 2 3 4 3 1 1 1 1 2 2 2 1 1 0 1 0 0 0 1

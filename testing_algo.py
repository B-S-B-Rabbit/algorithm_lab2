import time
import modules.p_segment_tree as pst
import modules.comp_map as cmp
import modules.test_func as tf


def seg_tree(rectangles, points):
    b1 = time.perf_counter_ns()

    x_values, y_values = pst.fill_zipped_coord(rectangles)
    events = pst.fill_events(rectangles, x_values, y_values)

    stree = pst.SegmentTree(y_values)
    stree.roots[-1] = stree.build(0, pst.find_next_power_of2(len(y_values)) - 1)
    prev_event = -1

    for event in events:
        stree.roots[event.compX] = stree.update(stree.roots[prev_event], event.compY1, event.compY2,
                                                1 if event.status_open else -1)
        prev_event = event.compX

    b2 = time.perf_counter_ns()

    q1 = time.perf_counter_ns()
    counts = pst.get_count(points, x_values, y_values, stree)
    q2 = time.perf_counter_ns()
    return [b2 - b1, q2 - q1]


def cmp_map(rectangles, points):
    b1 = time.perf_counter_ns()

    x_values, y_values = cmp.fill_zipped_coord(rectangles)
    matrix = cmp.fill_matrix(x_values, y_values, rectangles)

    b2 = time.perf_counter_ns()

    q1 = time.perf_counter_ns()

    counts = cmp.get_count(points, x_values, y_values, matrix)

    q2 = time.perf_counter_ns()
    return [b2 - b1, q2 - q1]


def bf(rectangles, points):
    b1 = time.perf_counter_ns()

    count = 0
    counts = []

    b2 = time.perf_counter_ns()

    q1 = time.perf_counter_ns()

    for point in points:
        for rect in rectangles:
            if rect.have(point):
                count += 1
        counts.append(count)
        count = 0

    q2 = time.perf_counter_ns()
    return [b2 - b1, q2 - q1]


def main():
    file_bf = open('report_time_brute_force.txt', "w+")
    file_cmp = open('report_time_comp_map.txt', "w+")
    file_pst = open('report_time_p_seg_tree.txt', "w+")

    for i in [1, 10, 50, 100, 250, 500, 1000, 1250, 1500, 2000, 2500, 3000, 4000, 5000, 10000, 20000, 50000, 70000,
              100000]:

        rects = tf.get_rectangles(i)
        points = tf.get_points(i)
        t1 = time.perf_counter_ns()
        k1 = bf(rects, points)
        t2 = time.perf_counter_ns()
        print("Время выполнения наивного алгоритма для {} числа прямоуг. и {} числа точек была: {} = {} + {}".format(i, i,
                                                                                                           t2 - t1, k1[0], k1[1]),
              file=file_bf,
              end='\n')
        if i <= 500:
            t1 = time.perf_counter_ns()
            k2 = cmp_map(rects, points)
            t2 = time.perf_counter_ns()
            print(
                "Время выполнения с построением карты на сжатых координатах для {} числа прямоуг. и {} числа точек была:"
                " {} = {} + {}".format(
                    i, i,
                    t2 - t1, k2[0], k2[1]),
                file=file_cmp,
                end='\n')

        t1 = time.perf_counter_ns()
        k3 = seg_tree(rects, points)
        t2 = time.perf_counter_ns()
        print(
            "Время выполнения алгоритма с построением персистентного дерева на сжатых координатах для {} числа "
            "прямоуг. и {} числа точек была: {} = {} + {}".format(
                i, i,
                t2 - t1, k3[0], k3[1]),
            file=file_pst,
            end='\n')


if __name__ == "__main__":
    main()

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


def find_next_power_of2(n):
    k = 1
    while k < n:
        k = k << 1

    return k


def fill_zipped_coord(rectangles: list) -> (set, set):
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
    return x_values, y_values

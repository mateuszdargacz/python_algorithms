import random
from timeit import default_timer as timer
import math

__author__ = 'mateusz'
__created__ = '24.02.15'


def get_random_sets(num):
    return set((random.randint(0, num * 3), random.randint(0, num * 3)) for _ in xrange(num))


def points_distance(u, v):
    return math.sqrt(((u[0] - v[0]) ** 2 + (u[1] - v[1]) ** 2))


def bruteForce_method(points):
    delta = None
    closest_pair = None
    for f in points:
        for s in points[points.index(f) + 1:]:
            if delta is None:
                delta = points_distance(f, s)
                closest_pair = [f, s]
            elif points_distance(f, s) < delta:
                delta = points_distance(f, s)
                closest_pair = [f, s]
    return dict(closest_pair=closest_pair, delta=delta)


def divide_y(sorted_y, divider):
    l = []
    r = []
    for y in sorted_y:
        if y[0] < divider:
            l.append(y)
        else:
            r.append(y)
    return l, r


def boundry_points(points, div, delta):
    return [point for point in points if abs(div - point[0]) < delta]


def recursive_method(sorted_by_x, sorted_by_y):
    amount = len(sorted_by_x)
    if amount == 2:
        return dict(closest_pair=sorted_by_x, delta=points_distance(sorted_by_x[0], sorted_by_x[1]))
    elif amount == 3:
        return bruteForce_method(sorted_by_x)
    else:
        x_left, x_right = sorted_by_x[:len(sorted_by_x) / 2], sorted_by_x[len(sorted_by_x) / 2:]
        # divider - x coordinate of last point on the left
        divider = x_left[-1][0]
        y_left, y_right = divide_y(sorted_by_y, divider)

        x_left_result = recursive_method(x_left, y_left)
        x_right_result = recursive_method(x_right, y_right)
        if x_left_result.get('delta') < x_right_result.get('delta'):
            closest_pair = x_left_result.get('closest_pair')
            delta = x_left_result.get('delta')
        else:
            closest_pair = x_right_result.get('closest_pair')
            delta = x_right_result.get('delta')

        delta_bounded_points = boundry_points(sorted_by_y, divider, delta)
        for point in delta_bounded_points:
            lower_point = point
            for _point in delta_bounded_points[delta_bounded_points.index(point) + 1:]:
                upper_point = _point
                if _point[1] - point[1] > delta:
                    break
                if points_distance(upper_point, lower_point) < delta:
                    delta = points_distance(upper_point, lower_point)
                    closest_pair = (lower_point, upper_point)

        return dict(closest_pair=closest_pair, delta=delta)


def run():
    SET_LEN = 10000

    points = get_random_sets(SET_LEN)
    # points = [(0, 7), (5, 10), (11, 20), (0, 6)]
    sorted_by_x = sorted(points, key=lambda x: x[0])
    sorted_by_y = sorted(points, key=lambda x: x[1])
    print "Points amount", len(points)
    start = timer()
    print bruteForce_method(sorted_by_x), 'brute force result'
    brute_time = timer() - start
    print 'BRUTE TIME', brute_time
    start = timer()
    print recursive_method(sorted_by_x, sorted_by_y), 'recursive method result'
    print 'recursive', timer() - start


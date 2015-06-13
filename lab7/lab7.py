# -*- coding: utf-8 -*-
import math
import random

__author__ = 'Mateuszek'
__created__ = '5/12/15'


def get_random_sets(num):
    return set((random.randint(0, num * 2), random.randint(0, num * 2)) for _ in xrange(num))


def points_distance(u, v):
    return math.sqrt(((u[0] - v[0]) ** 2 + (u[1] - v[1]) ** 2))


# def plot_it(points, order):
# l = [list(points)[i] for i in order]
#     l.append(l[0])
#     plt.plot(*zip(*l))
#     show()
#

def place_hospitals(k, points):
    s = points[0]
    _points = [s]
    for i in xrange(2, k + 1):
        _min = []
        for point in points:
            distances = []

            for s in _points:
                if s is not point:

                    distances.append((point[0], point[1], points_distance(s, point)))
            if distances:
                _min.append(min(distances, key=lambda x: x[2]))

        _points.append(max(_min, key=lambda x: x[2]))
        if i == 2:
            _points[0] = (_points[0][0], _points[0][1], points_distance(_points[0], _points[1]))
    return _points


SET_LEN = 4
cities = get_random_sets(SET_LEN)
cities = (
    (0, 2),
    (0, 0),
    (0, 4),
    (0, 3),
    (0, 5),
    (0, 4),
    (0, 7),
    (0, 6),
)
print 'RESULTS', place_hospitals(3, list(cities))


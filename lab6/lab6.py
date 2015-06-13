# -*- coding: utf-8 -*-
__author__ = 'Mateuszek'
__created__ = '4/27/15'
import pprint
import itertools
from pylab import *


def get_random_sets(num):
    import random
    return set((random.randint(0, num * 2), random.randint(0, num * 2)) for _ in xrange(num))


def points_distance(u, v):
    return math.sqrt(((u[0] - v[0]) ** 2 + (u[1] - v[1]) ** 2))


def plot_it(points, order):
    l = [list(points)[i] for i in order]
    l.append(l[0])
    plt.plot(*zip(*l))
    show()


def tsp(points):
    all_distances = [[points_distance(x, y) for y in points] for x in points]
    A = {}
    for i, distance in enumerate(all_distances[0][1:]):
        A.update({
            (frozenset([0, i + 1]), i + 1): (distance, [0, i + 1])
        })
    amount = len(points)
    a = [0, [0 for x in points], [0 for x in points]]
    for m in range(2, amount):
        a[0] += 1
        MIN = {}
        for sub_route in [frozenset(C) | {0} for C in itertools.combinations(range(1, amount), m)]:
            a[1][a[0]] += 1
            for j in sub_route - {0}:
                a[2][a[0]] += 1
                MIN[(sub_route, j)] = min(
                    [(A[(sub_route - {j}, k)][0] + all_distances[k][j], A[(sub_route - {j}, k)][1] + [j]) for k in
                     sub_route if k != 0 and k != j])
        A = MIN
    res = min([(A[d][0] + all_distances[0][d[1]], A[d][1]) for d in iter(A)])
    print res
    return res[1]



a = [[1, 2], [3, 3], [5, 2], [4, 4]]

SET_LEN = 19
points = get_random_sets(SET_LEN)
pprint.pprint(points)
plot_it(points, tsp(points))


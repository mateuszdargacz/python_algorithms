# -*- coding: utf-8 -*-
__author__ = 'mateuszdargacz@gmail.com'
__created__ = '5/25/15'

E = .05


def linear_merge(list1, list2):
    finalList = []
    i = 0
    j = 0
    while i < len(list1):
        if j < len(list2):
            if list1[i] < list2[j]:
                finalList.append(list1[i])
                i += 1
            else:
                finalList.append(list2[j])
                j += 1
        else:
            finalList.append(list1[i])
            i += 1
    while j < len(list2):
        finalList.append(list2[j])
        j += 1
    return finalList


def trim(l, e):
    l_p = [l[0]]
    last = l[0]
    for i in xrange(1, len(l)):
        if last < float(l[i]) * (1.0 - e):
            l_p.append(l[i])
            last = l[i]
    return l_p


def exact_subset_sum(s, t):
    n = len(s)
    l = [[0]]
    e = E / n
    for i in xrange(1, n + 1):
        l.append(linear_merge(l[i - 1], map(lambda x: x + s[i - 1], l[i - 1])))
        l[i] = trim(l[i], e)
        l[i] = filter(lambda x: x <= t, l[i])

    return l[-1]


L = [104, 102, 201, 101]
print exact_subset_sum(L, 308)
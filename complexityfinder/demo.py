import math as m
import numpy as np
from complexityfinder.finder import complexity_finder, arr_generator, simple_cleaner

def qsort(arr):
    np.sort(arr, kind='quicksort')


def bubble_sort(seq):
    changed = True
    while changed:
        changed = False
        for i in range(len(seq) - 1):
            if seq[i] > seq[i + 1]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
                changed = True
    return seq


def merge_sort(m):
    def merge(l, r):
        result = []
        left_idx, right_idx = 0, 0
        while left_idx < len(l) and right_idx < len(r):
            if l[left_idx] <= r[right_idx]:
                result.append(l[left_idx])
                left_idx += 1
            else:
                result.append(r[right_idx])
                right_idx += 1

        if left_idx < len(l):
            result.extend(l[left_idx:])
        if right_idx < len(r):
            result.extend(r[right_idx:])
        return result

    if len(m) <= 1:
        return m

    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))


def doubler(arr):
    return [x * 2 for x in arr]


def add_one(arr):
    return [x + 1 for x in arr]


def simple_n3(arr):
    return [[[x + 1 for x in arr] for _ in arr] for _ in arr]


def simple_logn(arr):
    n = int(m.log(max(len(arr), 1)))
    return [x*2 for x in range(0, n)]



def demo():
    complexity_finder(bubble_sort, arr_generator, simple_cleaner, 10).print_some_info()
    complexity_finder(qsort, arr_generator, simple_cleaner, 10).print_some_info()
    complexity_finder(sorted, arr_generator, simple_cleaner, 10).print_some_info()
    complexity_finder(merge_sort, arr_generator, simple_cleaner, 10).print_some_info()
    complexity_finder(doubler, arr_generator, simple_cleaner, 10).print_some_info()
    complexity_finder(add_one, arr_generator, simple_cleaner, 10).print_some_info()
    complexity_finder(simple_n3, arr_generator, simple_cleaner, 10).print_some_info()
    complexity_finder(simple_logn, arr_generator, simple_cleaner, 10).print_some_info()

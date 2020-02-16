import itertools
import time
from collections import OrderedDict
from copy import deepcopy

import psutil

from utils import combinations



def smart_brute_force(slice_numbers, max_slices):
    """Too long in runtime"""
    opt_val = 0
    opt_ind = []
    for R in range(1, len(slice_numbers) + 1):
        opt_, opt_ind_ = combinations(slice_numbers, R, max_slices)
        if opt_ > opt_val:
            opt_val = opt_
            opt_ind = opt_ind_
    return opt_ind, opt_val


def brute_force(slice_numbers, max_slices, display=True):
    """Might run out of RAM from medium dataset and on."""
    global opt_ind
    opt_val = 0
    for j in range(len(slice_numbers)):
        print(f'{j}/{len(slice_numbers)}')
        combinations = itertools.combinations(enumerate(slice_numbers), j + 1)
        t1 = time.time()
        for _, combination in enumerate(combinations):
            # print('{:.0e}'.format(k))
            value = sum(i[1] for i in combination)
            if (value > opt_val) & (value <= max_slices):
                opt_ind = (i[0] for i in combination)
                opt_val = value
                if opt_val == max_slices:
                    return list(opt_ind), opt_val
        print("{:.3e}".format(time.time() - t1))
    opt_ind = list(opt_ind)
    return opt_ind, opt_val


def longest_path(slice_numbers, max_slices, display=True):
    opt_ind = list()
    opt_val = int()

    return opt_ind, opt_val


def recursive_fill_in(slice_numbers, max_slices, display=True):
    global opt_ind
    # 1. Sort the list [O(log(n))]
    pool = {i: slice_numbers[i] for i in range(len(slice_numbers))}
    pool = {k: v for k, v in sorted(pool.items(), key=lambda item: item[1])}
    pool = OrderedDict(pool)
    # 2. Recursively fill in the largest number [O(n)]
    opt_val = 0
    for k in deepcopy(pool):
        val = 0
        ind = []
        for i, j in pool.items():
            if val + j > max_slices:
                pass
            else:
                val += j
                ind.append(i)
        del pool[k]
        if val > opt_val:
            opt_val = val
            opt_ind = ind
    return opt_ind, opt_val

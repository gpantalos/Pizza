import argparse
import time

import psutil

import solutions
import utils


def main():
    opt_val = 0
    opt_ind = []
    parser = argparse.ArgumentParser()
    parser.add_argument('--DATASET', '-d', type=str, default='b_small')
    parser.add_argument('--METHOD', '-m', type=str, default='recursive_fill_in')
    args = parser.parse_args()

    dataset = 'datasets/' + args.DATASET + '.in'
    method = args.METHOD

    max_slices, slice_numbers = utils.read_data(dataset, display=1)
    mem_start = psutil.virtual_memory()
    time_start = time.time()

    if method == 'brute_force':
        opt_ind, opt_val = solutions.brute_force(slice_numbers, max_slices)
    elif method == 'smart_brute_force':
        opt_ind, opt_val = solutions.smart_brute_force(slice_numbers, max_slices)
    elif method == 'longest_path':
        opt_ind, opt_val = solutions.longest_path(slice_numbers, max_slices)
    elif method == 'recursive_fill_in':
        opt_ind, opt_val = solutions.recursive_fill_in(slice_numbers, max_slices)
    # elif method == "NEW_METHOD":
    #     opt_ind, opt_val = solutions.NEW_METHOD(slice_numbers, max_slices)

    time_end = time.time()
    runtime = time_end - time_start
    mem_end = psutil.virtual_memory()
    memory_used = abs(mem_end.wired - mem_start.wired) * 1e-6

    utils.print_results(opt_val, opt_ind, method, runtime, memory_used, max_slices, slice_numbers)


if __name__ == '__main__':
    main()

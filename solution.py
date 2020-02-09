import itertools
import time

import psutil


def read_data(dataset, display=True):
	"""Reads the data."""
	with open(dataset) as f: data = f.read()  # read as a string
	lines = data.split('\n')  # separate string into lines
	max_slices = int(lines[0].split(' ')[0])  # read first line
	slice_numbers = lines[1].split(' ')  # read second line
	slice_numbers = [int(i) for i in slice_numbers]  #  convert to int
	if display:
		print("max_slices:", max_slices)
		print("slice_numbers:", slice_numbers)
	return max_slices, slice_numbers


def longest_path(slice_numbers, max_slices, display=True):
	optimal_combination = list()
	optimal_combination_value = int()

	return optimal_combination, optimal_combination_value, runtime


def brute_force(slice_numbers, max_slices, display=True):
	"""Might run out of RAM from medium dataset and on."""
	mem_start = psutil.virtual_memory()
	time_start = time.time()
	combinations = list()
	for i in range(len(slice_numbers)):
		combinations.extend(list(itertools.combinations(slice_numbers, i + 1)))  # all possible combinations
	comb_sum = [sum(x) for x in combinations]  # sum of slices for each combination
	comb_sum_max = [t if t <= max_slices else 0 for t in comb_sum]  # take sums <= max_slices
	opt_comb_value = max(comb_sum_max)  # take the max
	opt_comb_index = comb_sum_max.index(opt_comb_value)  # index of the max
	opt_comb_slice = combinations[opt_comb_index]  # combination that produces the max
	opt_comb = [slice_numbers.index(i) for i in opt_comb_slice]  # pizza types that produce this combination
	time_end = time.time()
	runtime = time_end - time_start
	mem_end = psutil.virtual_memory()
	used_memory = (mem_end.used - mem_start.used) * 1e-6
	if display:
		print('-'*100)
		print("Brute force types: {:}".format(opt_comb))
		print("Brute force slice: {:}".format(opt_comb_slice))
		print("Brute force value: {:}".format(opt_comb_value))
		print("Brute force rtime: {:.0e} s".format(runtime))
		print('Brute force memor: {:.04f} MB'.format(used_memory))
	return opt_comb, opt_comb_value, runtime


def main(*args, method):
	global combination, value, runtime
	if method == "brute force":
		combination, value, runtime = brute_force(slice_numbers, max_slices)
	elif method == "longest path":
		combination, value, runtime = longest_path(slice_numbers, max_slices)
	return combination, value, runtime


if __name__ == '__main__':
	datasets = ["a_example.in", "b_small.in", "c_medium.in", "d_quite_big.in", "e_also_big.in"]
	methods = ["brute force", "longest_path"]

	dataset = "datasets/" + datasets[1]  # change the index to change the dataset
	method = methods[0]  # change the index to change the method

	max_slices, slice_numbers = read_data(dataset)
	combination, value, runtime = main(max_slices, slice_numbers, method=method)

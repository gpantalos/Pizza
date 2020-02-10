import copy
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
		print("pizza_number:", len(slice_numbers))
	return max_slices, slice_numbers


def combinations(iterable, r, m):
	opt_ind = []
	opt = 0
	pool = tuple(iterable)
	n = len(pool)
	if r > n:
		return
	indices = list(range(r))
	ind_cop = copy.deepcopy(indices)
	val = tuple(pool[i] for i in indices)
	if (sum(val) > opt) & (sum(val) <= m):
		opt = sum(val)
		opt_ind = indices
		if opt == m:
			return opt, opt_ind
	while True:
		for i in reversed(range(r)):
			if indices[i] != i + n - r:
				break
		else:
			return opt, opt_ind
		indices[i] += 1
		for j in range(i + 1, r):
			indices[j] = indices[j - 1] + 1
		val = tuple(pool[i] for i in indices)
		if (sum(val) > opt) & (sum(val) <= m):
			opt_ind = indices
			opt = sum(val)
			if opt == m:
				return opt, opt_ind


def longest_path(slice_numbers, max_slices, display=True):
	optimal_combination = list()
	optimal_combination_value = int()

	return optimal_combination, optimal_combination_value, runtime


def smart_brute_force(slice_numbers, max_slices):
	opt = 0
	ind = []
	start = time.time()
	for R in range(1, len(slice_numbers) + 1):
		opt_, opt_ind_ = combinations(slice_numbers, R, max_slices)
		if opt_ > opt:
			opt = opt_
			ind = opt_ind_
	end = time.time()
	return ind, opt, end - start


def brute_force(slice_numbers, max_slices, display=True):
	"""Might run out of RAM from medium dataset and on."""
	mem_start = psutil.virtual_memory()
	time_start = time.time()
	opt_val = 0
	for j in range(len(slice_numbers)):
		print(f'{j}/{len(slice_numbers)}')

		combinations = itertools.combinations(enumerate(slice_numbers), j + 1)  # all possible combinations
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

	time_end = time.time()
	runtime = time_end - time_start
	mem_end = psutil.virtual_memory()
	used_memory = (mem_end.used - mem_start.used) * 1e-6
	if display:
		print('-'*50)
		print("Brute force rtime: {:.0e} s".format(runtime))
		print('Brute force memor: {:.04f} MB'.format(used_memory))
	return list(opt_ind), opt_val


def main(*args, method):
	global combination, value
	if method == "brute force":
		combination, value = brute_force(slice_numbers, max_slices)
	elif method == "smart brute force":
		combination, value = smart_brute_force(slice_numbers, max_slices)
	elif method == "longest path":
		combination, value = longest_path(slice_numbers, max_slices)
	return combination, value


if __name__ == '__main__':
	DATASET = 2
	METHOD = 0

	datasets = ["a_example.in", "b_small.in", "c_medium.in", "d_quite_big.in", "e_also_big.in"]
	methods = ["brute force", "smart brute force"]

	dataset = "datasets/" + datasets[DATASET]  # change the index to change the dataset
	method = methods[METHOD]  # change the index to change the method

	max_slices, slice_numbers = read_data(dataset)
	combination, value = main(max_slices, slice_numbers, method=method)

	print(('-' * 50))
	print('optimal value:', value)
	print('optimal combination:', combination)

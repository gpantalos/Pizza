import time
import itertools


def read_data(dataset, display=True):
	with open(dataset) as f: data = f.read()  # read as a string
	max_slices = int(data.split('\n')[0].split(' ')[0])  # read first line
	slice_numbers = data.split('\n')[1].split(' ')  # read second line
	slice_numbers = [int(i) for i in slice_numbers]  #  convert to int
	if display:
		print("max_slices:", max_slices)
		print("slice_numbers:", slice_numbers)
	return max_slices, slice_numbers


def solution_1(slice_numbers, max_slices):
	optimal_combination = list()
	optimal_combination_value = int()

	return optimal_combination, optimal_combination_value


def brute_force(slice_numbers, max_slices, display=True):
	"""Might run out of RAM from medium dataset and on."""
	start = time.time()
	combinations = list()
	for i in range(len(slice_numbers)):
		combinations.extend(list(itertools.combinations(slice_numbers, i + 1)))  # all possible combinations
	comb_sum = [sum(x) for x in combinations]  # sum of slices for each combination
	comb_sum_max = [t if t <= max_slices else 0 for t in comb_sum]  # take sums <= max_slices
	opt_comb_value = max(comb_sum_max)  # take the max
	opt_comb_index = comb_sum_max.index(opt_comb_value)  # index of the max
	opt_comb_slice = combinations[opt_comb_index]  # combination that produces the max
	opt_comb = [slice_numbers.index(i) for i in opt_comb_slice]  # pizza types that produce this combination
	end = time.time()
	runtime = end - start
	if display:
		print("Brute force types: {:}".format(opt_comb))
		print("Brute force slice: {:}".format(opt_comb_slice))
		print("Brute force value: {:}".format(opt_comb_value))
		print("Brute force rtime: {:.0e} s".format(runtime))
	return opt_comb, opt_comb_value, runtime


if __name__ == '__main__':
	datasets = ['a_example.in', 'b_small.in', 'c_medium.in', 'd_quite_big.in', 'e_also_big.in']
	dataset = "datasets/" + datasets[1]  # change the index to change the dataset
	max_slices, slice_numbers = read_data(dataset)
	print('-' * 50)
	bf_combination, bf_value, bf_runtime = brute_force(slice_numbers, max_slices)
	print('-' * 50)
	# pizza_types = solution_1(slice_numbers, max_slices)
	# print('-' * 50)

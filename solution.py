# import sys
# print(f'Python version: {sys.version}')

def read_data(dataset):
	with open(dataset) as f: data = f.read()  # read as a string
	max_slices = int(data.split('\n')[0].split(' ')[0])  # read first line
	slice_numbers = data.split('\n')[1].split(' ')  # read second line
	slice_numbers = [int(i) for i in slice_numbers]  #  convert to int
	return max_slices, slice_numbers


def solution_1(slice_numbers, max_slices):
	pizza_types = list()
	# slice_numbers = sorted(slice_numbers)

	return pizza_types


if __name__ == '__main__':
	datasets = ['a_example.in', 'b_small.in', 'c_medium.in', 'd_quite_big.in', 'e_also_big.in']
	dataset = datasets[0]
	max_slices, slice_numbers = read_data(dataset)
	print(max_slices)
	print(slice_numbers)
	pizza_types = solution_1(slice_numbers, max_slices)

import copy


def read_data(dataset, display=True):
    """Reads the data."""
    with open(dataset) as f: data = f.read()  # read as a string
    lines = data.split('\n')  # separate string into lines
    max_slices = int(lines[0].split(' ')[0])  # read first line
    slice_numbers = lines[1].split(' ')  # read second line
    slice_numbers = [int(i) for i in slice_numbers]  #  convert to int
    if display:
        print("[read_data] Maximum number of slices: {}".format(max_slices))
        s = "[read_data] Number of types of pizzas:  {}".format(len(slice_numbers))
        print(s)
        print('-' * len(s))
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


def print_results(opt_val, opt_ind, method, runtime, memory_used, max_slices, slice_numbers):
    print('[{}] Optimal Value: {}/{} = {:.8f} % of the best score.'
          .format(method, opt_val, max_slices, opt_val / max_slices * 100))
    print('[{}] Runtime: {:.4f} s.'.format(method, runtime))
    print('[{}] Memory: {:.4f} MB.'.format(method, memory_used))
    s = '[{}] Number of pizzas selected: {}/{}'\
        .format(method, len(opt_ind), len(slice_numbers))
    print(s)
    print('-'*len(s))

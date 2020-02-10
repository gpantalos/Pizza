import psutil
import time

R = 4
L = [12, 54, 76, 42, 1, 3]
M = 92


def combinations(iterable, r, m):
	global opt_ind
	opt = 0
	pool = tuple(iterable)
	n = len(pool)

	if r > n:
		return
	indices = list(range(r))
	val = tuple(pool[i] for i in indices)  # list of single items
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


tim_st = time.time()
mem_st = psutil.virtual_memory().used

opt = 0
ind = []
for R in range(1, len(L) + 1):
	opt_, opt_ind_ = combinations(L, R, M)
	if opt_ > opt:
		opt = opt_
		ind = opt_ind_
print(opt)
print(ind)

tim_en = time.time()
mem_en = psutil.virtual_memory().used

print('Time spent:  {:11.01e} s.'.format(tim_en - tim_st))
print('Memory used: {:10.04f} MB.'.format((mem_en - mem_st) * 1e-6))

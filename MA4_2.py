#!/usr/bin/env python3

from person import Person
from numba import njit
import matplotlib.pyplot as plt
from time import perf_counter as pc

def fib_py(n):
	if n <= 1:
		return n
	else:
		return(fib_py(n-1) + fib_py(n-2))

@njit
def fib_numba(n):
	if n <= 1:
		return n
	else:
		return(fib_numba(n-1) + fib_numba(n-2))

def fib_comparison(a, b):
	x = []
	py = []
	num = []
	cpp = []

	for n in range(a, b+1):
		x.append(n)

		t = pc()
		print(f'Python n={n}:\t', fib_py(n))
		py.append(pc()-t)

		t = pc()
		print(f'Numba n={n}:\t', fib_numba(n))
		num.append(pc()-t)

		t = pc()
		f = Person(n)
		print(f'c++ n={n}:\t', f.fib())
		cpp.append(pc()-t)

	fig = plt.figure()
	ax = fig.add_subplot()

	ax.scatter(x, py, c='r', s=10)
	ax.scatter(x, num, c='g', s=16)
	ax.scatter(x, cpp, c='b', s=10)
	plt.savefig('fib_plot.png')








def main():
	#fib_comparison(30, 42)
	

	t = pc()
	print(f'Numba n={47}:\t', fib_numba(47))
	print('Tid för numba n = 47:\t', pc()-t)

	t = pc()
	f = Person(47)
	print(f'C++ n={47}:\t', f.fib())
	print('Tid för c++ n = 47:\t', pc()-t)

if __name__ == '__main__':
	main()

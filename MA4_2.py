#!/usr/bin/env python3

from person import Person
from numba import njit

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

def main():
	f = Person(30)
	print(f.fib())

	print(fib_py(30))
	print(fib_numba(30))

if __name__ == '__main__':
	main()

#!/usr/bin/env python3

from person import Person

def fib_py(n):
	if n <= 1:
		return n
	else:
		return(fib_py(n-1) + fib_py(n-2))

def fib_numba(n):
	a, b = 0, 1
	for _ in range(n-1):
		a, b = b, a + b
	return b


def main():
	f = Person(50)
	print(f.fib())

if __name__ == '__main__':
	main()

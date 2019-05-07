#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
	m = None
	for l in matrix:
		for i, v in enumerate(l):
			m = len(l) - 1
			print('{:d}'.format(v), end='\n' if i == m else ' ')
	if m is None:
		print()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from fractions import Fraction

def print_matrix(matrix, ostream = sys.stdout):

	for i in matrix:
		for j in i:
			ostream.write("%s " % (str(j)))
		ostream.write(os.linesep)

def elimination(matrix, offset, m, n):

	if offset >= m:
		return 0

	"""find leader"""
	leader = n
	for j in range(offset, n):
		for i in range(offset, m):
			if matrix[i][j] != 0:
				matrix[offset], matrix[i] = matrix[i], matrix[offset]
				break
		if matrix[offset][j] != 0:
			leader = j
			break;
	
	"""div leader """
	for i in range(n - 1, leader - 1, -1):
		matrix[offset][i] /= matrix[offset][leader]

	"""sub other"""
	for i in range(offset + 1, m):
		for j in range(n - 1, leader - 1, - 1):
			matrix[i][j] -= matrix[i][leader] * matrix[offset][j]

	""" recursive it lol """
	elimination(matrix, offset + 1, m, n)

	return 0

def reduce(matrix, offset, m, n):

	if offset >= m:
		return 0

	row = m - offset - 1
	"""find leader"""
	leader = n
	for i in range(0, n):
		if matrix[row][i] != 0:
			leader = i
			break

	""" sub other """
	for i in range(0, row):
		for j in range(n - 1, leader - 1, -1):
			matrix[i][j] -= matrix[i][leader] * matrix[row][j]

	""" recursive it lol """
	reduce(matrix, offset + 1, m, n)

	return 0

if __name__ == '__main__':
	
	if len(sys.argv) <= 1:
		print "Error"
		sys.exit(1)

	file = open(sys.argv[1], 'r')
	m, n = (int(i) for i in file.next().split())

	matrix = []
	for i in range(0, m):
		matrix.append([Fraction(j) for j in file.next().split()])
	file.close()

	elimination(matrix, 0, m, n)
	reduce(matrix, 0, m, n)
	ofile = None
	if len(sys.argv) >= 3:
		ofile = open(sys.argv[2], 'w')
	print_matrix(matrix, ofile or sys.stdout)

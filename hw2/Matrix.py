#!/usr/bin/env python
# -*- coding: utf8 -*-

class Matrix:

	def __init__(self, matrix = [[]]):
		
		self.matrix = matrix
		self.height = len(matrix)
		self.width = len(matrix[0])
		# I think I should check this matrix is valid

	def __add__(self, b):

		m = []
		for i in xrange(0, self.height):
			m.append([val[0] + val[1] for val in zip(self.matrix[i], b.matrix[i])])
		return Matrix(m)

	def __sub__(self, b):

		m = []
		for i in xrange(0, self.height):
			m.append([val[0] - val[1] for val in zip(self.matrix[i], b.matrix[i])])
		return Matrix(m)

	def __mul__(self, b):

		rtn = []
		m = self.matrix
		n = zip(*(b.matrix))
		for i in xrange(0, self.height):
			rtn.append([])
			for j in xrange(0, self.width):
				rtn[i].append(sum([val[0] * val[1] for val in zip(m[i], n[j])]))
		
		return Matrix(rtn)


"""
unit test
"""

if __name__ == '__main__':

	a = Matrix([[0, -1], [1, 0]])
	b = Matrix([[1, 2], [3, 4]])

	print a.matrix
	print b.matrix
	print (a + b).matrix
	print (a - b).matrix
	print (a * b).matrix

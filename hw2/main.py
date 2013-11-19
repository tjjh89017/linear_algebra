#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import math
from fractions import Fraction
from Matrix import Matrix

if __name__ == '__main__':
	
	if len(sys.argv) <= 1:
		print "Error"
		sys.exit(1)

	matrix = []
	file = open(sys.argv[1], 'r')
	for i in xrange(0, 2):
		matrix.append([Fraction(j) for j in file.next().split()])

	rad = math.radians(float(file.next()))
	file.close()

	matrix = Matrix(zip(*matrix))
	rotation = Matrix([[math.cos(rad), -math.sin(rad)], [math.sin(rad), math.cos(rad)]])
	result = rotation * matrix

	ofile = None
	if len(sys.argv) >= 3:
		ofile = open(sys.argv[2], 'w')
	ostream = ofile or sys.stdout

	ostream.write("(%.2f, %.2f)" % (result.matrix[0][0], result.matrix[1][0]))
	ostream.write(os.linesep)
	ostream.write("(%.2f, %.2f)" % (result.matrix[0][1], result.matrix[1][1]))
	ostream.write(os.linesep)

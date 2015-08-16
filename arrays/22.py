__author__ = 'mrjac'

import numpy

matrix_A=numpy.matrix('12 7 3; 4 5 6; 7 8 9')

sum=0

for i in range(len(matrix_A)*len(matrix_A)):
     sum= sum+ matrix_A.item(i)

print sum
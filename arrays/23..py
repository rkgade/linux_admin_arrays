__author__ = 'mrjac'

import numpy

matrix_A=numpy.matrix('12 7 3; 4 5 6; 7 8 9')

product=1

for i in range(len(matrix_A)*len(matrix_A)):
     product=product * matrix_A.item(i)

print product
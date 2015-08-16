__author__ = 'mrjac'

matrix_X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
transpose=[]
for i in range(len(matrix_X)):
    print i
    transpose.append([row[i] for row in matrix_X] )

print transpose
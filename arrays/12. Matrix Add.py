__author__ = 'mrjac'


matrix_X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
matrix_Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(len(matrix_X)):
   for j in range(len(matrix_Y)):
      result[i][j] = matrix_X[i][j] + matrix_Y[i][j]

for r in result:
   print(r)
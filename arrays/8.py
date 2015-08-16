__author__ = 'mrjac'
import random

n_range=input("Enter the range under which you want to generate random numbers :")
n_array_length=input("Enter the length of array you wish to populate")
n_array=[]

# Fill array with random integers
for i in range(n_array_length):
    n_array.append(random.randrange(n_range))

print n_array


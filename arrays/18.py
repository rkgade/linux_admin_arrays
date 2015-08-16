__author__ = 'mrjac'

n_const=input("Enter the constant multiplicative index of geometric progression :")

n_init= input("Enter initial value :")
value=n_init
n_range=input("Enter the number of elements of geometric progression")

for i in range(n_range):
    print value
    value=value*(n_const)


__author__ = 'mrjac'

n_comm_diff = input("Enter common deference")
n_init= input("Enter initial value :")
value=n_init
n_range=input("Enter the number of elements of arithmetic progression")

for i in range(n_range):
    print value
    value= value+n_comm_diff

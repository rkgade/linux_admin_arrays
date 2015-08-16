__author__ = 'mrjac'

n_range=input("Enter the range")
n_input=[]
for i in range(n_range):
    n_input.append(input("Enter  value : "))

max=n_input[0]
min=n_input[0]
for i in n_input:
    if i > max:
        max=i
    if i < min:
        min=i
print max
print min

__author__ = 'mrjac'

n_input = input("Enter a value for which you require the sum of all numbers until this number :")
sum=0
for i in range(n_input+1):
    sum=sum+i

print sum
print type(sum)





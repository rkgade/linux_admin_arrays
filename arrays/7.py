__author__ = 'mrjac'

# Fill array with multiples of 3.
# Remove those divisible by 5, substitute -1 in those places

n_range=input("Enter the range")
n_input=[]
number=3
for i in range(1,n_range+1):
    n_input.append(i*number)


# Check for numbers divisible by 5

for i in n_input:
    if i % 5 ==0 :
        index=n_input.index(i)
        del n_input[n_input.index(i)]
        n_input.insert(index,-1)


print n_input

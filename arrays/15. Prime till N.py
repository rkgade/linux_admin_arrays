__author__ = 'mrjac'

n_input = input("Enter the value till which you need the prime numbers")

def is_prime(n_arg):
    is_prime_val=0
    for i in range(2,n_arg):
        if n_arg % i ==0:
            is_prime_val=1
            break

    if is_prime_val ==0:
        return 0
    else:
        return 1

for i in range(2,n_input):
    if  is_prime(i) ==0 :
        print i

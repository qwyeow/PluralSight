from math import sqrt
from pprint import pprint as pp
from itertools import count, islice
import sys

def is_prime(x):
    if x <2:
        return False
    for i in range(2, (int(sqrt(x))+1)):
        if x % i == 0:
            return False
    return True

def main(num):
    print(f"Print primes below {num}:")
    num = int(num)
    print([i for i in range(num) if is_prime(i)])   
    print(f"Print a dictionary of primes: (prime square, prime cube) below {num}" )
    pp({i: (i*i, i*i*i) 
            for i in range(num) 
            if is_prime(i)}) 



if __name__ == "__main__":
    main(sys.argv[1])


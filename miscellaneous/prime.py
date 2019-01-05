"""
Using predicate statement to filter dictionary comprehension and list comprehension

"""


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
    print([i for i in range(num) if is_prime(i)])  # predicate is_prime() is used to filter list 
    print(f"Print a dictionary of primes: (prime square, prime cube) below {num}:" )
    pp({i: (i*i, i*i*i) 
            for i in range(num) 
            if is_prime(i)})  # predicate is_prime() is used to filter dictionary  



if __name__ == "__main__":
    main(sys.argv[1])

"""
$ python3 prime.py 50

Print primes below 50:
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

Print a dictionary of primes: (prime square, prime cube) below 50:
{2: (4, 8),
 3: (9, 27),
 5: (25, 125),
 7: (49, 343),
 11: (121, 1331),
 13: (169, 2197),
 17: (289, 4913),
 19: (361, 6859),
 23: (529, 12167),
 29: (841, 24389),
 31: (961, 29791),
 37: (1369, 50653),
 41: (1681, 68921),
 43: (1849, 79507),
 47: (2209, 103823)}

"""
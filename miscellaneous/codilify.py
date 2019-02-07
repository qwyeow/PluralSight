'''
1) BinaryGap
Find longest sequence of zeros in binary representation of an integer. 

A binary gap within a positive integer N is any maximal sequence of consecutive zeros   
that is surrounded by ones at both ends in the binary representation of N.
For example, number 9 has binary representation 1001 and contains a binary gap of length 2. 
The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. 
The number 20 has binary representation 10100 and contains one binary gap of length 1. 
The number 15 has binary representation 1111 and has no binary gaps. 
The number 32 has binary representation 100000 and has no binary gaps.
'''

def solution(N):     
    _ ,_ , num = str(bin(N)).partition("b")
    nums = num.split("1")
    if nums[-1] is not False:
        nums = nums[:-1]
    return max(len(i) for i in nums)

```
Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number 
and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”
```

for i in range(1,101):
    if i%(3*5) == 0:
        print("fizzbuzz")
        continue
    if i%3 == 0:
        print("fizz")
        continue
    if i%5 == 0:
        print("buzz")
        continue
    else:
        print(i)
        


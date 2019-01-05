import sys
import unittest


def digit_slicing(num):
    digit = []    
    num = int(num)
    while not num == 0:
        div, mod = divmod(num,10)
        digit.append(mod)
        num = div
    return digit

def is_palindrome(num):
    digit = digit_slicing(num)
    reverse = reversed(digit)
    for i,j in zip(digit, reverse):
        if not i == j:
            return False
    return True        
            

def main(num):
    print(is_palindrome(num))

           

class Tests(unittest.TestCase):
    def test_no(self):
        self.assertFalse(is_palindrome("1234"))

    def test_yes(self):
        self.assertTrue(is_palindrome(987654456789))    

    def test_single(self):
        for i in range(10):
            self.assertTrue(is_palindrome(i))    




if __name__ == "__main__":       
    unittest.main()
    
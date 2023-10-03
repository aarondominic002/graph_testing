from select import select
import unittest
from unittest import result

# The function to be tested 

def add_numbers(a, b):
    return a + b 

class TestFunction(unittest.TestCase):
    def test_addition(self):
        result = add_numbers(3, 5)
        self.assertEqual(result, 8)
    
    def test_addition_negative_numbers(self):
        result = add_numbers(-2, 7)
        
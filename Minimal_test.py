from select import select
import unittest
from unittest import result

# The function to be tested 



class TestFunction(unittest.TestCase):
    def test_addition(self):
        result = add_numbers(3, 5)
        self.assertEqual(result, 8)
    
    def test_addition_negative_numbers(self):
        result = add_numbers(-2, 6)
        self.assertEqual(result,4)

    def test_addition_float_numbers(self):
        result = add_numbers(1.5, 3.5)
        self.assertAlmostEqual(result, 5.0, places = 2 )

if __name__ == "__main__":
    unittest.main()

    
# test_unit.py

import unittest

def add_numbers(a, b):
    return a + b

class TestAddNumbers(unittest.TestCase):
    
    def test_add_positive_numbers(self):
        result = add_numbers(5, 10)
        self.assertEqual(result, 15)
    
    def test_add_negative_numbers(self):
        result = add_numbers(-5, -10)
        self.assertEqual(result, -15)
    
    def test_add_zero(self):
        result = add_numbers(0, 0)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()

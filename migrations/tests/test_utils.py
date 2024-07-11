# test_utils.py
import unittest
from myapp.utils import my_util_function

class TestUtils(unittest.TestCase):
    def test_util_function(self):
        result = my_util_function('input')
        self.assertEqual(result, 'expected_output')

import unittest
from katas.sum_of_digits import sum_of_digits


class TestSumOfDigits(unittest.TestCase):
    def test_empty_str(self):
        self.assertEqual(sum_of_digits(""), 0)

    def test_one_digit(self):
        self.assertEqual(sum_of_digits("2"), 1)
    def test_no_digits(self):
        self.assertEqual(sum_of_digits("hello"),0)
    def test_long(self):
        self.assertEqual(sum_of_digits("h112lkfj9k92"),6)

    


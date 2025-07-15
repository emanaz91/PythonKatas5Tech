import unittest
from katas.is_unique_str import is_unique


class TestIsUnique(unittest.TestCase):
    
    def test_one_char(self):
        str = "a"
        self.assertEqual(is_unique(str), True)

    def test_two_char(self):
        str = "Bb"
        self.assertEqual(is_unique(str), True)
    
    def test_random(self):
        str = "alm89dfjJ"
        self.assertEqual(is_unique(str), True)

    def test_random2(self):
        str = "anab59osd"
        self.assertEqual(is_unique(str), False)
import unittest
from katas.true_counter import count_true_values


class TestTrueCounter(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(count_true_values([]), 0)
    
    def test_one_true(self):
        self.assertEqual(count_true_values([True]), 1)

    def test_one_false(self):
        self.assertEqual(count_true_values([False]), 0)
    
    def test_array(self):
        self.assertEqual(count_true_values([False,True,True]), 2)

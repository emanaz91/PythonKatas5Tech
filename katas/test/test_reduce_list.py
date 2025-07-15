import unittest
from katas.reduce_list import reduce_array


class TestReduceArray(unittest.TestCase):
    def test_empty_array(self):
        lst = []
        reduce_array(lst)
        self.assertEqual(lst, [])
    
    def test_one_elemnt(self):
        lst = [1]
        reduce_array(lst)
        self.assertEqual(lst, [1])

    def test_list(self):
        lst = [1,7,0,-6]
        reduce_array(lst)
        self.assertEqual(lst, [1,6,-7,-6])    

    
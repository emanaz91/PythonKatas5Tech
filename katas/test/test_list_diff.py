import unittest
from katas.list_diff import find_difference


class TestListDiff(unittest.TestCase):
    
    def test_one_elemnt(self):
        lst = [9]
        self.assertEqual(find_difference(lst), 0)

    def test_random(self):
        lst = [9,-1,0,8,11]
        self.assertEqual(find_difference(lst), 12)
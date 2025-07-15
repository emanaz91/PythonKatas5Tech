import unittest
from katas.word_count import count_words


class TestCountWords(unittest.TestCase):
    def test_empty_str(self):
        self.assertEqual(count_words(""), 0)

    def test_one_word(self):
        self.assertEqual(count_words(" word"), 1)
    def test_sentence(self):
        self.assertEqual(count_words("hello world    8 a"),4)
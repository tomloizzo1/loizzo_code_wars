import unittest
import re
from counting_duplicates import duplicate_count


class TestOddIntFinder(unittest.TestCase):
    def test_find_it(self):
        self.assertEquals(duplicate_count(""), 0)
        self.assertEquals(duplicate_count("abcde"), 0)
        self.assertEquals(duplicate_count("abcdeaa"), 1)
        self.assertEquals(duplicate_count("abcdeaB"), 2)
        self.assertEquals(duplicate_count("Indivisibilities"), 2)


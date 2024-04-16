import unittest
from find_the_odd_int import find_it


class TestOddIntFinder(unittest.TestCase):
    def test_find_it(self):
        # Test to see which number appears an odd number of time in a seqwuence
        self.assertEquals(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]), 5)
        self.assertEquals(find_it([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]), -1)
        self.assertEquals(find_it([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]), 5)
        self.assertEquals(find_it([10]), 10)
        self.assertEquals(find_it([10, 10, 10]), 10)
        self.assertEquals(find_it([1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1]), 10)
        self.assertEquals(find_it([5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10]), 1)

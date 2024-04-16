import unittest
from playing_with_digits import dig_pow


class TestCircleArea(unittest.TestCase):
    def test_case(self):
        # Tests areas when radius >= 0
        self.assertEquals(dig_pow(89,1), 1)
        self.assertEquals(dig_pow(92, 1), -1)
        self.assertEquals(dig_pow(46288, 3), 51)
        self.assertEquals(dig_pow(41, 5), 25)
        self.assertEquals(dig_pow(114, 3), 9)
        self.assertEquals(dig_pow(8, 3), 64)
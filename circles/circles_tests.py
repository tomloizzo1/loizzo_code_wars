import unittest
from circles import circle_area
from math import pi

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        # Tests areas when radius >= 0
        self.assertAlmostEqual(circle_area(1), pi)

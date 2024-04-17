import unittest
import re
from regex_pin_code import validate_pin


class TestOddIntFinder(unittest.TestCase):
    def test_find_it(self):
        self.assertEquals(validate_pin("1"), False)
        self.assertEquals(validate_pin("12"), False)
        self.assertEquals(validate_pin("123"), False)
        self.assertEquals(validate_pin("12345"), False)
        self.assertEquals(validate_pin("1234567"), False)
        self.assertEquals(validate_pin("-1234"), False)
        self.assertEquals(validate_pin("-12345"), False)
        self.assertEquals(validate_pin("1.234"), False)
        self.assertEquals(validate_pin("00000000"), False)
        self.assertEquals(validate_pin("a234"), False)
        self.assertEquals(validate_pin(".234"), False)
        self.assertEquals(validate_pin("1234"), True)
        self.assertEquals(validate_pin("0000"), True)
        self.assertEquals(validate_pin("1111"), True)
        self.assertEquals(validate_pin("123456"), True)
        self.assertEquals(validate_pin("098765"), True)
        self.assertEquals(validate_pin("000000"), True)
        self.assertEquals(validate_pin("123456"), True)
        self.assertEquals(validate_pin("090909"), True)
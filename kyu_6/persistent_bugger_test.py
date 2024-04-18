import unittest
from persistent_bugger import persistence

class TestPersistentBugger(unittest.TestCase):
    def test_persistent_bugger(self):
        #
        self.assertEquals(persistence(39), 3)
        self.assertEquals(persistence(4), 0)
        self.assertEquals(persistence(25), 2)
        self.assertEquals(persistence(999), 4)
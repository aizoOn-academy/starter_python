from util import mysum
import unittest

class Test(unittest.TestCase):
    def test_mysum(self):
        self.assertEqual(mysum(1,2), 3)
import unittest
from generallibrary import *


class LibTest(unittest.TestCase):
    def test_depth(self):
        self.assertEqual(depth(5), 0)



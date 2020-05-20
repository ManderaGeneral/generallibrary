
import unittest

from generallibrary.values import clamp


class ValuesTest(unittest.TestCase):
    def test_clamp(self):
        self.assertEqual(5, clamp(2, 5, 10))
        self.assertEqual(7, clamp(7, 5, 10))
        self.assertEqual(10, clamp(10.1, 5, 10))
        self.assertEqual(10.2, clamp(20, 5, 10.2))
        self.assertEqual(-3, clamp(-5, -3, 10.2))
        self.assertEqual(-1.4, clamp(-1.4, -3, 10.2))

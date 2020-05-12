
import unittest

from generallibrary.functions import leadingArgsCount

class FunctionsTest(unittest.TestCase):
    def test_leadingArgsCount(self):
        self.assertEqual(0, leadingArgsCount(lambda: 5))
        self.assertEqual(1, leadingArgsCount(lambda x: 5))
        self.assertEqual(2, leadingArgsCount(lambda x, y: 5))
        self.assertEqual(1, leadingArgsCount(lambda x, y=2: 5))
        self.assertEqual(0, leadingArgsCount(lambda x=3, y=2: 5))

        def hello(x, y, z=None):
            """2 arg, 1 kwarg function"""
            pass
        self.assertEqual(2, leadingArgsCount(hello))



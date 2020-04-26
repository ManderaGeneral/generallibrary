import unittest
from generallibrary import *


class LibTest(unittest.TestCase):
    def test_depth(self):
        self.assertEqual(depth(5), 0)

    def test_typeChecker(self):
        self.assertTrue(typeChecker("hello", (bool, str)))
        self.assertTrue(typeChecker(["hello"], list, (bool, str)))
        self.assertFalse(typeChecker(["hello"], (tuple, dict), (bool, str), raiseTypeError=False))

    def test_timer(self):
        timer = Timer()
        time.sleep(0.05)
        secs = timer.seconds()
        self.assertEqual(round(secs, 2), 0.05)

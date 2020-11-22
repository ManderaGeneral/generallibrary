
import unittest
from generallibrary.text import comma_and_and

class CodeTest(unittest.TestCase):
    def test_comma_and_and(self):
        self.assertEqual("a, b, c and d.", comma_and_and("a", "b", "c", "d"))
        self.assertEqual("a, b and c.", comma_and_and("a", "b", "c"))
        self.assertEqual("a and b.", comma_and_and("a", "b"))
        self.assertEqual("a.", comma_and_and("a"))
        self.assertEqual("", comma_and_and())
        self.assertEqual("a, b, c and d", comma_and_and("a", "b", "c", "d", period=False))
        self.assertEqual("a, b and c", comma_and_and("a", "b", "c", period=False))
        self.assertEqual("a and b", comma_and_and("a", "b", period=False))
        self.assertEqual("a", comma_and_and("a", period=False))
        self.assertEqual("", comma_and_and(period=False))





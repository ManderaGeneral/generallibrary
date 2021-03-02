
from generallibrary.text import *

import unittest


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

    def test_plur_sing(self):
        self.assertEqual("0 words", plur_sing(0, "word"))
        self.assertEqual("1 word", plur_sing(1, "word"))
        self.assertEqual("2 words", plur_sing(2, "word"))

        self.assertEqual("0 kisses", plur_sing(0, "kiss", "es"))
        self.assertEqual("1 kiss", plur_sing(1, "kiss", "es"))
        self.assertEqual("1.5 kisses", plur_sing(1.5, "kiss", "es"))
        self.assertEqual("2 kisses", plur_sing(2, "kiss", "es"))





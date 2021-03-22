
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

    def test_replace(self):
        self.assertEqual("hi there hi", replace("foo bar foo", foo="hi", bar="there"))
        self.assertEqual("hello", replace("foo bar foo", **{"foo bar foo": "hello"}))
        self.assertEqual("he11o", replace("hello", l=1))
        self.assertEqual("&", replace("hello", hello="&"))
        self.assertEqual("foo/bar", replace("foobar", ob="o/b"))
        self.assertEqual("foo/bar", replace("foo\\bar", **{"\\": "/"}))
        self.assertEqual("foo\\bar", replace("foo/bar", **{"/": "\\"}))
        self.assertEqual("123", replace("abc", **{"a": 1, "b": 2, "c": 3}))

    def test_replace_reversed(self):
        tests = {
            "foo bar": {"foo": "hi", "bar": "there"},
            "abc": {"a": 1, "b": 2, "c": 3},
            "foo/bar": {"/": "\\"},
            "foo\\bar": {"\\": "/"},
        }

        for string, translation in tests.items():
            replaced = replace(string, **translation)
            self.assertNotEqual(string, replaced)
            self.assertEqual(string, replace(replaced, reverse=True, **translation))


    def test_match(self):
        self.assertEqual(True, match("foo bar", "foo"))
        self.assertEqual(True, match("foo bar", "bar"))
        self.assertEqual(True, match("foo bar", " "))
        self.assertEqual(True, match("foo bar", ""))
        self.assertEqual(True, match("foo bar", "f*r"))

        self.assertEqual(False, match("foo bar", "!"))

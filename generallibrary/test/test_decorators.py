from generallibrary.decorators import deco_require

import unittest


class DecoratorsTest(unittest.TestCase):
    def test_deco_require_simple(self):
        class X:
            def __init__(self, x):
                self.x = x

            @deco_require(lambda self: self.x == 5)
            def foo(self):
                return self.x

        self.assertEqual(5, X(5).foo())
        self.assertRaises(AssertionError, X(2).foo)

    def test_deco_require_message(self):
        class X:
            def __init__(self, x):
                self.x = x

            @deco_require(lambda self: self.x == 5, lambda func: f"{func.__name__} failed")
            def foo(self):
                return self.x

        self.assertEqual(5, X(5).foo())
        self.assertRaises(AssertionError, X(2).foo)

        self.assertRaisesRegex(AssertionError, "foo failed", X(2).foo)



